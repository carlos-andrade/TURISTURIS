#!/usr/bin/env python3
"""Gera o catálogo público completo de pontos turísticos a partir da normalização municipal."""
from pathlib import Path
import json
import re

ROOT=Path("CONTINENTE/DADOS/NORMALIZAÇÃO")
OUT=Path("CONTINENTE/DADOS/PUBLICACAO/PONTOS_TURISTICOS_PUBLICAVEIS_COMPLETO_V1.json")
pattern=re.compile(r"^\|\s*\d+\s*\|\s*(PT-[^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|")

records=[]
for path in sorted(ROOT.glob("*_PONTOS_TURISTICOS_V1.md")):
    text=path.read_text(encoding="utf-8")
    for line in text.splitlines():
        m=pattern.match(line)
        if not m:
            continue
        ident,name,kind,municipality,district,state,confidence=[x.strip() for x in m.groups()]
        records.append({
            "id":ident,
            "name":name,
            "type":kind,
            "municipality":municipality,
            "district":district,
            "validation_state":state,
            "confidence":confidence,
            "normalization_source":str(path).replace("\\","/")
        })

unique={}
for record in records:
    unique.setdefault(record["id"],record)

ordered=sorted(unique.values(),key=lambda x:(x["district"].casefold(),x["municipality"].casefold(),x["name"].casefold()))
payload={
    "schema_version":"1.0",
    "generated_from":"CONTINENTE/DADOS/NORMALIZAÇÃO/",
    "purpose":"Catálogo público completo dos pontos turísticos presentes nos documentos municipais de normalização.",
    "publication_rule":"Os estados e níveis de confiança são preservados da normalização; normalização não equivale a validação operacional.",
    "municipality_count":len({x["municipality"] for x in ordered}),
    "record_count":len(ordered),
    "records":ordered
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"municipios={payload['municipality_count']} registros={payload['record_count']} arquivo={OUT}")
