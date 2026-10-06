#!/usr/bin/env python3
"""TURISTURIS — gerar catálogo nacional de municípios a partir do RNAL normalizado."""
import json,re,unicodedata
from collections import Counter
from pathlib import Path
SRC=Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS/RNAL_NORMALIZADO_V1.json")
OUT=Path("DADOS/INDICES/rnal_municipios_catalogo.json")
def slug(s):
 s=unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()
 return re.sub(r"[^a-z0-9]+","-",s).strip("-")
def main():
 data=json.loads(SRC.read_text(encoding="utf-8")); counts=Counter()
 for r in data.get("records",[]):
  m=str(r.get("município") or r.get("municipio") or "").strip()
  if m: counts[m]+=1
 municipalities=[{"municipio":m,"slug":slug(m),"target_total":counts[m],"estado":"PENDENTE"} for m in sorted(counts,key=lambda x:x.casefold())]
 report={"schema_version":"1.0","process":"WEB-12.6-CATALOGO-MUNICIPIOS","source":str(SRC),"municipios_total":len(municipalities),"registos_rnal_total":sum(counts.values()),"municipios":municipalities}
 OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"municipios_total":len(municipalities),"registos_rnal_total":sum(counts.values())},ensure_ascii=False))
if __name__=="__main__": main()
