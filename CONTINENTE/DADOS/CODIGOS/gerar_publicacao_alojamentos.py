#!/usr/bin/env python3
"""WEB-12.5 — catálogo público nacional de alojamentos com contactos públicos disponíveis."""
import json
from pathlib import Path

BASE = Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS")
OUT = Path("CONTINENTE/DADOS/PUBLICACAO/ALOJAMENTOS_PUBLICAVEIS_V2.json")
FILES = {"RNET": BASE / "RNET_NORMALIZADO_V1.json", "RNAL": BASE / "RNAL_NORMALIZADO_V1.json"}

def source_url(source, source_id):
    if source == "RNAL":
        return "https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=" + str(source_id)
    return "https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=" + str(source_id)

def slim(r, source):
    fonte = (r.get("fontes") or [{}])[0]
    source_id = fonte.get("id_origem")
    return {
        "id": r.get("id"), "nome": r.get("nome"), "tipo": r.get("tipo"),
        "região": r.get("região"), "distrito": r.get("distrito ou arquipélago"),
        "município": r.get("município"), "localidade": r.get("localidade"),
        "morada": r.get("endereço"), "endereço": r.get("endereço"),
        "coordenadas": r.get("coordenadas"), "telefone": r.get("telefone"),
        "email": r.get("email"), "website": r.get("website"),
        "fonte": source, "id_origem": source_id,
        "ficha_oficial": source_url(source, source_id) if source_id else None,
        "estado_validação": r.get("estado_validação"), "grau_confiança": r.get("grau_confiança"),
    }

records = []
for source, path in FILES.items():
    payload = json.loads(path.read_text(encoding="utf-8"))
    records.extend(slim(r, source) for r in payload["records"])

records.sort(key=lambda x: (x.get("região") or "", x.get("distrito") or "", x.get("município") or "", x.get("nome") or ""))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "schema_version": "2.0", "process": "WEB-12.5", "source_process": "WEB-12.3",
    "record_count": len(records),
    "contact_rule": "Apenas contactos públicos efetivamente presentes na fonte normalizada são exibidos. A ficha oficial é mantida como referência para dados públicos adicionais.",
    "records": records,
}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(json.dumps({"output": str(OUT), "record_count": len(records)}, ensure_ascii=False))
