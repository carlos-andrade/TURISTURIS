#!/usr/bin/env python3
"""WEB-12.7 — extrai contactos do bloco oficial de titular/explorador das fichas RNAL já capturadas."""
import csv, json, re
from pathlib import Path

ROOT=Path("FICHAS OFICIAIS RNAL")
TABLE=Path("DADOS/TABELAS/rnal_peso_da_regua_tabela_mestra.csv")
OUT=Path("CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/RNAL_CONTACTOS_FICHAS_OFICIAIS_V2.json")

ROLE_LABELS={
    "PROPRIETÁRIO","COMODATÁRIO","ARRENDATÁRIO","USUFRUTUÁRIO",
    "EXPLORADOR","TITULAR","ENTIDADE EXPLORADORA","EXPLORADOR DO ALOJAMENTO"
}
EMAIL_RE=re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}",re.I)
PHONE_RE=re.compile(r"(?<!\d)(?:\+351\s*)?(?:2\d{2}|9\d{2})[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)")

def norm(s):
    return re.sub(r"\s+"," ",s or "").strip()

def extract(rnal):
    p=ROOT/str(rnal)/"structured"/"ficha.json"
    if not p.exists():
        return {"NrRNAL":str(rnal),"status":"SEM_FICHA_LOCAL","telefone":[],"email":[]}
    try:
        data=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        return {"NrRNAL":str(rnal),"status":"ERRO_JSON","erro":str(e)[:200],"telefone":[],"email":[]}

    phones=set(); emails=set(); roles=[]
    for item in data:
        label=norm(item.get("raw_label"))
        value=norm(item.get("raw_value"))
        if item.get("element_type")!="table_field":
            continue
        if item.get("table_index") == 5 and label.upper() in ROLE_LABELS:
            roles.append(label)
            phones.update(PHONE_RE.findall(value))
            emails.update(EMAIL_RE.findall(value))

    phones=sorted(phones); emails=sorted(e.lower() for e in emails)
    if phones or emails:
        status="CONFIRMADO_FICHA_OFICIAL"
    elif roles:
        status="FICHA_OFICIAL_SEM_CONTACTO"
    else:
        status="SEM_TITULAR_EXPLORADOR_CONTACTO"

    return {
        "NrRNAL":str(rnal),"status":status,
        "roles":sorted(set(roles)),
        "telefone":phones,"email":emails,
        "ficha_local":str(p)
    }

rows=list(csv.DictReader(TABLE.open(encoding="utf-8-sig",newline="")))
results=[extract(r["NrRNAL"].strip()) for r in rows if r.get("NrRNAL")]
counts={}
for r in results:
    counts[r["status"]]=counts.get(r["status"],0)+1

OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps({
    "schema_version":"2.0","process":"WEB-12.7","source":"FICHAS OFICIAIS RNAL",
    "rnal_total":len(results),"status_counts":counts,"records":results
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rnal_total":len(results),"status_counts":counts},ensure_ascii=False))
