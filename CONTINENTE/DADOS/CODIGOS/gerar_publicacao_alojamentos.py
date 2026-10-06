#!/usr/bin/env python3
"""WEB-12.4 — gerar catálogo público nacional de alojamentos a partir da normalização validada."""
import json
from pathlib import Path

BASE = Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS")
OUT = Path("CONTINENTE/DADOS/PUBLICACAO/ALOJAMENTOS_PUBLICAVEIS_V1.json")
FILES = {"RNET": BASE / "RNET_NORMALIZADO_V1.json", "RNAL": BASE / "RNAL_NORMALIZADO_V1.json"}

def slim(r, source):
    fonte = (r.get("fontes") or [{}])[0]
    return {
        "id": r.get("id"),
        "nome": r.get("nome"),
        "tipo": r.get("tipo"),
        "região": r.get("região"),
        "distrito": r.get("distrito ou arquipélago"),
        "município": r.get("município"),
        "localidade": r.get("localidade"),
        "endereço": r.get("endereço"),
        "coordenadas": r.get("coordenadas"),
        "email": r.get("email"),
        "website": r.get("website"),
        "fonte": source,
        "id_origem": fonte.get("id_origem"),
        "estado_validação": r.get("estado_validação"),
        "grau_confiança": r.get("grau_confiança"),
    }

records = []
for source, path in FILES.items():
    payload = json.loads(path.read_text(encoding="utf-8"))
    records.extend(slim(r, source) for r in payload["records"])

records.sort(key=lambda x: (
    (x.get("região") or ""),
    (x.get("distrito") or ""),
    (x.get("município") or ""),
    (x.get("nome") or ""),
))

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "schema_version": "1.0",
    "process": "WEB-12.4",
    "source_process": "WEB-12.3",
    "record_count": len(records),
    "records": records,
}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

print(json.dumps({"output": str(OUT), "record_count": len(records)}, ensure_ascii=False))
