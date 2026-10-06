#!/usr/bin/env python3
"""Gera a tabela-mestra RNAL de Peso da Régua a partir da fonte oficial.

Contactos só entram quando estiverem persistidos na tabela de contactos.
Ausência de contacto NÃO significa que não exista.
"""

import csv, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"DADOS/INDICES/rnal_peso_da_regua.csv"
CONTACTS=ROOT/"DADOS/CONTACTOS/contactos_existentes_peso_da_regua.csv"
OUT=ROOT/"DADOS/TABELAS/rnal_peso_da_regua_tabela_mestra.csv"
REPORT=ROOT/"DADOS/TABELAS/rnal_peso_da_regua_tabela_mestra.json"
CONTACT_FIELDS=["Telefone","Email","Website","OutrosContactos","FonteContacto","EstadoContacto"]

with SOURCE.open(encoding="utf-8-sig",newline="") as f:
    official=list(csv.DictReader(f))

contacts={}
if CONTACTS.exists():
    with CONTACTS.open(encoding="utf-8-sig",newline="") as f:
        for r in csv.DictReader(f):
            if r.get("NrRNAL","").strip():
                contacts[r["NrRNAL"].strip()]=r

rows=[]
for r in official:
    out=dict(r)
    c=contacts.get(r["NrRNAL"].strip(),{})
    for k in CONTACT_FIELDS:
        out[k]=c.get(k,"")
    if c:
        out["EstadoContacto"]=c.get("EstadoContacto") or "PRESERVADO_DE_FONTE_EXISTENTE"
    else:
        out["EstadoContacto"]="PENDENTE_RECUPERACAO"
    rows.append(out)

OUT.parent.mkdir(parents=True,exist_ok=True)
fields=list(official[0])+CONTACT_FIELDS
with OUT.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

report={
 "result":"SUCCESS","source":str(SOURCE.relative_to(ROOT)),
 "expected_count":len(official),"output_count":len(rows),
 "contacts_preserved_count":sum(r["EstadoContacto"]!="PENDENTE_RECUPERACAO" for r in rows),
 "contacts_pending_count":sum(r["EstadoContacto"]=="PENDENTE_RECUPERACAO" for r in rows),
 "contact_source":str(CONTACTS.relative_to(ROOT)),
 "rule":"CONTACTOS EXISTENTES DEVEM SER PRESERVADOS; AUSÊNCIA NÃO É INFERIDA."
}
REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if len(rows)!=len(official): raise SystemExit("ERRO: contagem divergente.")
print(json.dumps(report,ensure_ascii=False,indent=2))
