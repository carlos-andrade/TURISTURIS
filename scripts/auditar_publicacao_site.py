#!/usr/bin/env python3
"""TURISTURIS — auditor de dados PUBLICACAO prontos para o SITE.

Regra: não altera dados. Classifica ficheiros de publicação pela presença
de registos e, quando existir um campo de estado conhecido, separa
registos publicáveis dos que ainda estão em validação.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PUBLICACAO=ROOT/"CONTINENTE"/"DADOS"/"PUBLICACAO"

KNOWN_STATE_FIELDS=("validation_state","estado_validação","estado_validacao")
BLOCKED=("EM_VERIFICACAO","EM VALIDAÇÃO","PENDENTE","FONTE_HISTORICA_A_VALIDAR")

def records(obj):
    for key in ("records","registos","alojamentos","dados"):
        if isinstance(obj.get(key),list):
            return obj[key],key
    return [],None

def main():
    rows=[]
    for path in sorted(PUBLICACAO.rglob("*.json")):
        try:
            obj=json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            rows.append({"path":str(path.relative_to(ROOT)),"status":"ERRO_JSON","detail":str(exc)})
            continue
        recs,key=records(obj)
        if key is None:
            continue
        states={}
        blocked=0
        for rec in recs:
            state=next((rec.get(k) for k in KNOWN_STATE_FIELDS if rec.get(k)),None)
            states[state or "SEM_ESTADO"]=states.get(state or "SEM_ESTADO",0)+1
            if state in BLOCKED:
                blocked+=1
        rows.append({
            "path":str(path.relative_to(ROOT)),
            "record_count":len(recs),
            "records_key":key,
            "blocked_records":blocked,
            "publishable_records":len(recs)-blocked,
            "states":states,
            "site_action":"PUBLICAR_OU_COMPLETAR" if recs and blocked < len(recs) else "AGUARDAR_VALIDACAO"
        })
    output={"schema_version":"1.0","process":"AUDITOR_PUBLICACAO_SITE","record_count":len(rows),"files":rows}
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
