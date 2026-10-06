#!/usr/bin/env python3
"""TURISTURIS — WEB-12.6: consolidar lotes de contactos RNAL sem perda."""
import csv, json
from pathlib import Path

MASTER=Path("DADOS/INDICES/rnal_peso_da_regua_tabela_mestra.csv")
LOTS=Path("CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/LOTES")
OUT=Path("DADOS/INDICES/rnal_peso_da_regua_tabela_mestra.csv")
REPORT=Path("DADOS/INDICES/rnal_peso_da_regua_contactos_consolidacao_report.json")

def main():
    rows=list(csv.DictReader(MASTER.open(encoding="utf-8",newline="")))
    by_id={str(r["id_origem"]):r for r in rows}
    lote_files=sorted(LOTS.glob("rnal_contactos_offset_*.json"), key=lambda p:int(p.stem.rsplit("_",1)[-1]))
    applied=0
    duplicate_ids=set()
    status_counts={}
    for p in lote_files:
        data=json.loads(p.read_text(encoding="utf-8"))
        for rec in data.get("records",[]):
            rid=str(rec.get("id_origem") or "")
            if not rid or rid not in by_id:
                continue
            r=by_id[rid]
            phones=rec.get("telefone") or []
            emails=rec.get("email") or []
            r["telefone"]="; ".join(sorted(set(phones)))
            r["email"]="; ".join(sorted(set(emails)))
            r["estado_contacto"]=rec.get("status") or "SEM_STATUS"
            r["fonte_contacto"]=rec.get("ficha_oficial") or ""
            r["contacto_captura_utc"]=rec.get("data_recolha_utc") or ""
            applied+=1
            status_counts[r["estado_contacto"]]=status_counts.get(r["estado_contacto"],0)+1
    with OUT.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    report={
      "schema_version":"1.0","process":"WEB-12.6-CONSOLIDACAO",
      "master_records":len(rows),"lotes_lidos":len(lote_files),
      "registros_aplicados":applied,"registros_sem_perda":len(by_id),
      "status_counts":status_counts
    }
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__": main()
