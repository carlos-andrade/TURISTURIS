#!/usr/bin/env python3
"""TURISTURIS — auditor seguro dos dados PUBLICAÇÃO.

Somente classifica. Nunca promove automaticamente registos sem estado
explícito. Registos sem estado ficam em REVISAO_MANUAL.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PUBLICACAO=ROOT/"CONTINENTE"/"DADOS"/"PUBLICACAO"

STATE_FIELDS=("validation_state","estado_validação","estado_validacao")
PUBLISHABLE={"VERIFICADO","CONFIRMADO_FICHA_OFICIAL","CONFIRMADO_FONTE_PUBLICA"}
BLOCKED={"EM_VERIFICACAO","EM VALIDAÇÃO","PENDENTE","FONTE_HISTORICA_A_VALIDAR"}

def collections(obj):
    found=[]
    for key in ("records","registos","alojamentos","dados","pontos"):
        if isinstance(obj.get(key),list):
            found.append((key,obj[key]))
    for key in ("experiencias","transportes","restauracao"):
        if isinstance(obj.get(key),list):
            found.append((key,obj[key]))
    return found

def classify(items):
    states={}
    for rec in items:
        state=next((rec.get(k) for k in STATE_FIELDS if rec.get(k)),None)
        states[state or "SEM_ESTADO"]=states.get(state or "SEM_ESTADO",0)+1
    publishable=sum(n for s,n in states.items() if s in PUBLISHABLE)
    blocked=sum(n for s,n in states.items() if s in BLOCKED)
    review=sum(n for s,n in states.items() if s=="SEM_ESTADO")
    if review:
        action="REVISAO_MANUAL"
    elif blocked and publishable:
        action="PUBLICAR_VALIDADO_E_MANTER_BLOQUEADO"
    elif blocked:
        action="AGUARDAR_VALIDACAO"
    elif publishable:
        action="PUBLICAR_OU_COMPLETAR"
    else:
        action="REVISAO_MANUAL"
    return states,publishable,blocked,review,action

def main():
    rows=[]
    for path in sorted(PUBLICACAO.rglob("*.json")):
        try:
            obj=json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            rows.append({"path":str(path.relative_to(ROOT)),"status":"ERRO_JSON","detail":str(exc)})
            continue
        groups=collections(obj)
        if not groups:
            continue
        for key,recs in groups:
            states,publishable,blocked,review,action=classify(recs)
            rows.append({
                "path":str(path.relative_to(ROOT)),
                "collection":key,
                "record_count":len(recs),
                "publishable_records":publishable,
                "blocked_records":blocked,
                "manual_review_records":review,
                "states":states,
                "site_action":action,
            })
    output={"schema_version":"1.1","process":"AUDITOR_PUBLICACAO_SITE","record_count":len(rows),"files":rows}
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
