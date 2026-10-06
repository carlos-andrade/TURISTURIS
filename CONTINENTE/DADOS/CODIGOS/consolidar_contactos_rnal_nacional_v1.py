#!/usr/bin/env python3
"""TURISTURIS — WEB-12.6 consolidação nacional por município."""
import json, re
from pathlib import Path

CAT=Path("DADOS/INDICES/rnal_municipios_catalogo.json")
LOTS=Path("CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/LOTES")
OUT=Path("DADOS/INDICES/rnal_nacional_consolidacao.json")

def slug(s):
    import unicodedata
    s=unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+","-",s).strip("-")

def main():
    c=json.loads(CAT.read_text(encoding="utf-8"))
    municipalities=[]
    for item in c["municipios"]:
        m=item["municipio"]; total=int(item["target_total"]); s=item["slug"]
        files=[]; records=0; ids=[]; errors=[]; missing=[]
        for off in range(0,total,50):
            p=LOTS/s/f"rnal_contactos_offset_{off}.json"
            if not p.exists():
                missing.append(off); continue
            d=json.loads(p.read_text(encoding="utf-8"))
            if d.get("municipio","").casefold()!=m.casefold(): errors.append(f"{p}: municipio")
            if d.get("target_total")!=total: errors.append(f"{p}: target_total")
            if d.get("offset")!=off: errors.append(f"{p}: offset")
            rs=d.get("records",[])
            if d.get("record_count")!=len(rs): errors.append(f"{p}: record_count")
            rid=[str(r.get("id_origem")) for r in rs]
            if len(rid)!=len(set(rid)): errors.append(f"{p}: ids duplicados")
            ids.extend(rid); records+=len(rs); files.append(str(p))
        unique=len(set(ids))
        complete=(not errors and records==total and unique==total)
        municipalities.append({"municipio":m,"slug":s,"target_total":total,"lotes":len(files),"lotes_em_falta":missing,"registros":records,"ids_unicos":unique,"estado":"VALIDADO" if complete else ("EM_PROCESSAMENTO" if records else "PENDENTE"),"erros":errors})
    accepted=all(x["estado"]=="VALIDADO" for x in municipalities)
    out={"schema_version":"1.0","process":"WEB-12.6-CONSOLIDACAO-NACIONAL","municipios_total":len(municipalities),"registos_rnal_total":c["registos_rnal_total"],"municipios_validados":sum(x["estado"]=="VALIDADO" for x in municipalities),"acceptance":accepted,"municipios":municipalities}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"municipios_total":len(municipalities),"municipios_validados":out["municipios_validados"],"acceptance":accepted},ensure_ascii=False))
if __name__=="__main__": main()
