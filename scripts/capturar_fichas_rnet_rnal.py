#!/usr/bin/env python3
"""
Captura rígida das fichas oficiais RNET/RNAL.

Regras:
- raw HTML é preservado byte a byte;
- raw_value nunca é substituído por valor normalizado;
- field_code é derivado do rótulo do campo, não do valor;
- a relação rótulo -> valor é preservada;
- células, linhas e sequência DOM são mantidas para auditoria;
- RNET e RNAL permanecem fisicamente separados;
- falha de fonte não gera ficha artificialmente completa.
"""
import csv
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests
from bs4 import BeautifulSoup

SOURCES = {
    "RNET": "https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803",
    "RNAL": "https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=15642",
}
ROOT = Path(__file__).resolve().parents[1]
HEADERS = {
    "User-Agent": "TURISTURIS-Official-Ficha-Capture/2.0",
    "Accept": "text/html,application/xhtml+xml",
}
TIMEOUT = 30
MAX_ATTEMPTS = 3


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def registry_number(url):
    return parse_qs(urlparse(url).query).get("nr", ["unknown"])[0]


def raw_text(node):
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()


def field_code(label, fallback_index):
    value = re.sub(r"[^A-Z0-9À-ÖØ-Ý]+", "_", label.upper()).strip("_")
    return value[:80] or f"FIELD_{fallback_index:04d}"


def base_path(kind, number):
    folder = "FICHAS OFICIAIS RNET" if kind == "RNET" else "FICHAS OFICIAIS RNAL"
    return ROOT / folder / number


def add_record(records, counts, *, kind, number, source_url, captured,
               source_hash, sequence, element_type, raw_label, raw_value,
               table_index="", row_index="", column_index=""):
    label = raw_label or ""
    code = field_code(label, len(records) + 1)
    counts[code] = counts.get(code, 0) + 1
    occurrence = counts[code]
    records.append({
        "sequence": sequence,
        "element_type": element_type,
        "table_index": table_index,
        "row_index": row_index,
        "column_index": column_index,
        "raw_label": label,
        "raw_value": raw_value,
        "field_code": code,
        "occurrence": occurrence,
        "record_key": f"{kind}:{number}:{code}:{occurrence:03d}",
        "source_url": source_url,
        "capture_utc": captured,
        "source_sha256": source_hash,
    })


def parse_html(html, kind, number, url, captured, source_hash):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "template"]):
        tag.decompose()

    records = []
    counts = {}
    sequence = 0

    # Tabelas: preserva cada célula e, quando possível, a relação
    # primeira célula (rótulo) -> segunda célula (valor).
    for table_index, table in enumerate(soup.find_all("table"), 1):
        for row_index, tr in enumerate(table.find_all("tr"), 1):
            cells = tr.find_all(["th", "td"], recursive=False)
            values = [raw_text(cell) for cell in cells]

            if not values:
                continue

            # Cabeçalhos de tabela continuam como evidência, sem inventar valor.
            if any(cell.name == "th" for cell in cells):
                for column_index, value in enumerate(values, 1):
                    if value:
                        sequence += 1
                        add_record(
                            records, counts, kind=kind, number=number,
                            source_url=url, captured=captured,
                            source_hash=source_hash, sequence=sequence,
                            element_type="table_header",
                            raw_label=value, raw_value=value,
                            table_index=table_index, row_index=row_index,
                            column_index=column_index,
                        )
                continue

            if len(values) >= 2 and values[0]:
                label = values[0]
                value = " | ".join(v for v in values[1:] if v)
                sequence += 1
                add_record(
                    records, counts, kind=kind, number=number,
                    source_url=url, captured=captured,
                    source_hash=source_hash, sequence=sequence,
                    element_type="table_field",
                    raw_label=label, raw_value=value,
                    table_index=table_index, row_index=row_index,
                    column_index=1,
                )
            else:
                value = values[0]
                if value:
                    sequence += 1
                    add_record(
                        records, counts, kind=kind, number=number,
                        source_url=url, captured=captured,
                        source_hash=source_hash, sequence=sequence,
                        element_type="table_text",
                        raw_label="", raw_value=value,
                        table_index=table_index, row_index=row_index,
                        column_index=1,
                    )

    # Elementos fora de tabelas: preservados como texto bruto de estrutura,
    # sem fingir que são pares rótulo/valor.
    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]):
        value = raw_text(tag)
        if not value:
            continue
        sequence += 1
        add_record(
            records, counts, kind=kind, number=number,
            source_url=url, captured=captured,
            source_hash=source_hash, sequence=sequence,
            element_type=tag.name,
            raw_label="", raw_value=value,
        )

    return soup, records


def capture(kind, url):
    number = registry_number(url)
    base = base_path(kind, number)
    for name in ("raw", "structured", "audit"):
        (base / name).mkdir(parents=True, exist_ok=True)

    response = None
    error = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            break
        except Exception as exc:
            error = str(exc)
            if attempt < MAX_ATTEMPTS:
                time.sleep(attempt * 2)

    if response is None:
        manifest = {
            "capture_id": f"{kind}:{number}:FAILED",
            "type": kind,
            "registry_number": number,
            "source_url": url,
            "capture_utc": datetime.now(timezone.utc).isoformat(),
            "result": "FAILED",
            "error": error,
            "rules": "CARTA-CAPTURA-RNET-RNAL-V1",
        }
        (base / "audit" / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        raise RuntimeError(f"Falha de captura {kind} {number}: {error}")

    html = response.content
    source_hash = sha256(html)
    captured = datetime.now(timezone.utc).isoformat()

    # Evidência primária: exatamente os bytes recebidos.
    (base / "raw" / "source.html").write_bytes(html)

    soup, records = parse_html(
        html, kind, number, url, captured, source_hash
    )

    structured = json.dumps(
        records, ensure_ascii=False, indent=2
    ).encode("utf-8")
    (base / "structured" / "ficha.json").write_bytes(structured)

    if records:
        with (base / "structured" / "ficha.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as handle:
            writer = csv.DictWriter(
                handle, fieldnames=list(records[0].keys())
            )
            writer.writeheader()
            writer.writerows(records)

    manifest = {
        "capture_id": f"{kind}:{number}:{captured}",
        "type": kind,
        "registry_number": number,
        "source_url": url,
        "capture_utc": captured,
        "http_status": response.status_code,
        "content_type": response.headers.get("Content-Type", ""),
        "source_sha256": source_hash,
        "structured_sha256": sha256(structured),
        "field_count": len(records),
        "table_count": len(soup.find_all("table")),
        "result": "SUCCESS",
        "rules": "CARTA-CAPTURA-RNET-RNAL-V1",
    }
    (base / "audit" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return manifest


def main():
    results = []
    failures = []
    for kind, url in SOURCES.items():
        try:
            results.append(capture(kind, url))
        except Exception as exc:
            failures.append({
                "type": kind,
                "url": url,
                "error": str(exc),
            })

    output = {"results": results, "failures": failures}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
