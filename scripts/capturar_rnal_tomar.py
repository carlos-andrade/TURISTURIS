#!/usr/bin/env python3
import json
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

SOURCE_URL = "https://www.cm-tomar.pt/visitar/onde-dormir"
SOURCE_FALLBACK_URL = "https://www.cm-tomar.pt/index.php/visitar/onde-dormir"
SOURCE_PROXY_URL = "https://r.jina.ai/http://www.cm-tomar.pt/index.php/visitar/onde-dormir"
OUT_JSON = Path("DADOS/RAW/RNAL/TOMAR/rnal_tomar_catalogo_fonte_v1.json")
OUT_TXT = Path("DADOS/RAW/RNAL/TOMAR/rnal_tomar_fonte_municipal_raw_v1.txt")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0 Safari/537.36 "
        "TURISTURIS-RNAL-Capture/1.1"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-PT,pt;q=0.9,en;q=0.7",
}

def clean_lines(html):
    soup = BeautifulSoup(html, "html.parser")
    root = soup.body or soup
    text = root.get_text("\n", strip=True)
    return [x.strip() for x in text.splitlines() if x.strip()]

def fetch_source():
    session = requests.Session()
    last_error = None
    urls = [SOURCE_URL, SOURCE_FALLBACK_URL, SOURCE_PROXY_URL]
    for url in urls:
        for attempt in range(1, 4):
            try:
                response = session.get(
                    url,
                    timeout=(20, 60),
                    headers=HEADERS,
                    allow_redirects=True,
                )
                response.raise_for_status()
                if "ALOJAMENTO LOCAL (AL)" in response.text:
                    return response, url, attempt
                last_error = RuntimeError(
                    f"Fonte respondeu sem a secção ALOJAMENTO LOCAL (AL): {url}"
                )
            except requests.RequestException as exc:
                last_error = exc
                if attempt < 3:
                    time.sleep(2 * attempt)
    raise RuntimeError(
        "Não foi possível obter a fonte municipal de Tomar após tentativas "
        f"controladas. Último erro: {last_error}"
    ) from last_error

def main():
    response, fetch_url, attempts = fetch_source()
    html = response.text
    lines = clean_lines(html)

    try:
        start = next(i for i, x in enumerate(lines) if "ALOJAMENTO LOCAL (AL)" in x)
        end = next(
            i
            for i in range(start + 1, len(lines))
            if "TURISMO ESPAÇO RURAL" in lines[i]
        )
    except StopIteration as exc:
        raise RuntimeError(
            "Secção ALOJAMENTO LOCAL (AL) ou marcador de fim "
            "TURISMO ESPAÇO RURAL não localizado de forma segura."
        ) from exc

    al_lines = lines[start:end]
    raw = "\n".join(al_lines) + "\n"
    OUT_TXT.parent.mkdir(parents=True, exist_ok=True)
    OUT_TXT.write_text(raw, encoding="utf-8")

    rnal_re = re.compile(r"N\.º Registo:\s*([0-9]+)\s*/\s*AL", re.I)
    rnal_ids = [m.group(1) for m in map(rnal_re.search, al_lines) if m]
    dupes = sorted(
        [k for k, v in Counter(rnal_ids).items() if v > 1],
        key=int,
    )

    unit_re = re.compile(r"Unidade de alojamento:", re.I)
    unit_count = sum(1 for x in al_lines if unit_re.search(x))

    headings = {
        "Apartamentos": "Modalidade Apartamentos",
        "Estabelecimento de Hospedagem": "Modalidade Estabelecimento de Hospedagem",
        "Estabelecimento de Hospedagem - Hostel": "Modalidade Estabelecimento de Hospedagem - Hostel",
        "Moradias": "Modalidade Moradias",
        "Quartos": "Modalidade Quartos",
    }
    category_counts = {}
    current = None
    for line in al_lines:
        for name, marker in headings.items():
            if marker in line:
                current = name
                category_counts.setdefault(name, 0)
                break
        else:
            if current and rnal_re.search(line):
                category_counts[current] += 1

    record_count = len(rnal_ids)
    unit_metadata_coverage = (
        round(unit_count / record_count, 6) if record_count else 0
    )
    count_reconciliation = "PASS" if record_count > 0 and not dupes else "BLOCKED"

    result = {
        "schema_version": "1.1",
        "process": "TURISTURIS_RNAL_TOMAR_A1_SOURCE_CAPTURE",
        "territory": {"distrito": "Santarém", "municipio": "Tomar"},
        "source": {
            "authority": "Município de Tomar",
            "title": "Onde dormir",
            "url": SOURCE_URL,
            "fetch_url": fetch_url,
            "accessed_utc": datetime.now(timezone.utc).isoformat(),
            "http_status": response.status_code,
            "content_length_bytes": len(response.content),
            "fetch_attempt": attempts,
            "transport_fallback_used": fetch_url != SOURCE_URL,
            "transport": ("official_direct" if fetch_url in (SOURCE_URL, SOURCE_FALLBACK_URL) else "controlled_proxy"),
        },
        "extraction": {
            "section_start_marker": "ALOJAMENTO LOCAL (AL)",
            "section_end_marker": "TURISMO ESPAÇO RURAL",
            "al_source_line_count": len(al_lines),
            "record_count_rnal": record_count,
            "record_count_basis": "N.º Registo ... / AL",
            "unit_record_count": unit_count,
            "unit_metadata_coverage": unit_metadata_coverage,
            "count_reconciliation": count_reconciliation,
            "duplicate_rnal_ids": dupes,
            "category_rnal_counts": category_counts,
            "complete_catalogue": (
                record_count > 0
                and not dupes
                and len(al_lines) > 0
                and "ALOJAMENTO LOCAL (AL)" in al_lines[0]
            ),
        },
        "rnal_ids": rnal_ids,
        "rules": {
            "phone_country_code": "preserve_explicitly",
            "public_territory_order": ["Freguesia", "Município", "Distrito"],
            "internal_validation_status_public": False,
        },
        "next_gate": "A2 — reconciliar freguesia por registo sem inferência destrutiva.",
    }
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "record_count_rnal": record_count,
                "unit_record_count": unit_count,
                "unit_metadata_coverage": unit_metadata_coverage,
                "count_reconciliation": count_reconciliation,
                "complete_catalogue": result["extraction"]["complete_catalogue"],
                "duplicates": dupes,
                "category_rnal_counts": category_counts,
                "fetch_url": fetch_url,
                "transport_fallback_used": fetch_url != SOURCE_URL,
            },
            ensure_ascii=False,
        )
    )

if __name__ == "__main__":
    main()
