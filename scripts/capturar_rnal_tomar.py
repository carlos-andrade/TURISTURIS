#!/usr/bin/env python3
import json, re, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://www.cm-tomar.pt/visitar/onde-dormir"
OUT_JSON = Path("DADOS/RAW/RNAL/TOMAR/rnal_tomar_catalogo_fonte_v1.json")
OUT_TXT = Path("DADOS/RAW/RNAL/TOMAR/rnal_tomar_fonte_municipal_raw_v1.txt")

def clean_lines(html):
    soup = BeautifulSoup(html, "html.parser")
    root = soup.body or soup
    text = root.get_text("\n", strip=True)
    return [x.strip() for x in text.splitlines() if x.strip()]

def main():
    r = requests.get(URL, timeout=60, headers={"User-Agent": "TURISTURIS-RNAL-Capture/1.0"})
    r.raise_for_status()
    html = r.text
    lines = clean_lines(html)

    try:
        start = next(i for i, x in enumerate(lines) if "ALOJAMENTO LOCAL (AL)" in x)
        end = next(i for i in range(start + 1, len(lines)) if "TURISMO ESPAÇO RURAL" in lines[i])
    except StopIteration:
        raise RuntimeError("Secção ALOJAMENTO LOCAL (AL) não localizada de forma segura.")

    al_lines = lines[start:end]
    raw = "\n".join(al_lines) + "\n"
    OUT_TXT.parent.mkdir(parents=True, exist_ok=True)
    OUT_TXT.write_text(raw, encoding="utf-8")

    rnal_re = re.compile(r"N\.º Registo:\s*([0-9]+)\s*/\s*AL", re.I)
    rnal_ids = [m.group(1) for m in map(rnal_re.search, al_lines) if m]
    dupes = sorted([k for k, v in Counter(rnal_ids).items() if v > 1], key=int)

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

    result = {
        "schema_version": "1.0",
        "process": "TURISTURIS_RNAL_TOMAR_A1_SOURCE_CAPTURE",
        "territory": {"distrito": "Santarém", "municipio": "Tomar"},
        "source": {
            "authority": "Município de Tomar",
            "title": "Onde dormir",
            "url": URL,
            "accessed_utc": datetime.now(timezone.utc).isoformat(),
            "http_status": r.status_code,
            "content_length_bytes": len(r.content),
        },
        "extraction": {
            "section_start_marker": "ALOJAMENTO LOCAL (AL)",
            "section_end_marker": "TURISMO ESPAÇO RURAL",
            "al_source_line_count": len(al_lines),
            "record_count_rnal": len(rnal_ids),
            "unit_record_count": unit_count,
            "count_reconciliation": "PASS" if len(rnal_ids) == unit_count else "BLOCKED",
            "duplicate_rnal_ids": dupes,
            "category_rnal_counts": category_counts,
            "complete_catalogue": len(rnal_ids) == unit_count and not dupes,
        },
        "rnal_ids": rnal_ids,
        "rules": {
            "phone_country_code": "preserve_explicitly",
            "public_territory_order": ["Freguesia", "Município", "Distrito"],
            "internal_validation_status_public": False,
        },
        "next_gate": "A2 — reconciliar freguesia por registo sem inferência destrutiva.",
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "record_count_rnal": len(rnal_ids),
        "unit_record_count": unit_count,
        "count_reconciliation": result["extraction"]["count_reconciliation"],
        "complete_catalogue": result["extraction"]["complete_catalogue"],
        "duplicates": dupes,
        "category_rnal_counts": category_counts
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
