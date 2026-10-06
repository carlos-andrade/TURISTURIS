#!/usr/bin/env python3
"""Gera a camada pública de alojamentos RNAL de Tomar a partir do índice oficial
e das fichas RNAL capturadas e validadas.

Regra: contactos são extraídos apenas como valores públicos de contacto;
NIF/NIPC, nomes de pessoas e outros dados identificativos não são publicados.
Telefones preservam literalmente qualquer prefixo internacional explícito.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "DADOS/INDICES/rnal_tomar.json"
VALIDATION = ROOT / "DADOS/INDICES/rnal_tomar_manifest_validation_report.json"
OUT = ROOT / "CONTINENTE/DADOS/PUBLICACAO/RNAL_TOMAR_PUBLICAVEIS_V2.json"
BASE = ROOT / "FICHAS OFICIAIS RNAL"

EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PHONE_RE = re.compile(r"(?<!\d)(?:(?:\+|00)\s?\d{1,4}[\s./-]?)?(?:\(?\d{2,4}\)?[\s./-]?)?\d[\d\s./-]{6,}\d(?!\d)")

def clean(v):
    return re.sub(r"\s+", " ", str(v or "")).strip()

def contacts(records):
    emails, phones = [], []
    for r in records:
        label = clean(r.get("raw_label"))
        value = clean(r.get("raw_value"))
        text = f"{label} {value}"
        # Só recolher contactos em contexto de contacto/telefone/email.
        if not re.search(r"contact|telefone|telemóvel|email|e-mail", text, re.I):
            continue
        for e in EMAIL_RE.findall(text):
            if e.lower() not in {x.lower() for x in emails}:
                emails.append(e)
        for p in PHONE_RE.findall(text):
            p = clean(p)
            digits = re.sub(r"\D", "", p)
            if len(digits) >= 9 and len(digits) <= 15 and not ("@" in p):
                if p not in phones:
                    phones.append(p)
    return emails, phones

def main():
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    validation = json.loads(VALIDATION.read_text(encoding="utf-8"))
    if validation.get("result") != "SUCCESS" or validation.get("valid_count") != idx.get("count"):
        raise SystemExit("VALIDAÇÃO RNAL TOMAR NÃO ESTÁ COMPLETA; publicação interrompida.")

    records = []
    for row in idx["records"]:
        n = str(row["NrRNAL"])
        fp = BASE / n / "structured" / "ficha.json"
        if not fp.exists():
            raise SystemExit(f"FICHA AUSENTE: {fp}")
        raw = json.loads(fp.read_text(encoding="utf-8"))
        emails, phones = contacts(raw)
        records.append({
            "id": f"RNAL:{n}",
            "rn_al": n,
            "nome": clean(row.get("Denominacao")),
            "tipo": clean(row.get("Modalidade")),
            "capacidade": row.get("NrUtentes"),
            "morada": clean(row.get("Endereco")),
            "codigo_postal": clean(row.get("CodigoPostal")),
            "localidade": clean(row.get("LOCALIDADE")),
            "freguesia": clean(row.get("Freguesia")),
            "municipio": clean(row.get("Concelho")),
            "distrito": clean(row.get("Distrito")),
            "coordenadas": clean(row.get("LatLong")),
            "contactos": {
                "telefone": phones,
                "email": emails
            },
            "ficha_oficial": f"https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr={n}",
            "fonte": "Turismo de Portugal — RNAL"
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "2.0",
        "process": "PUBLICACAO_RNAL_TOMAR",
        "source_index": "DADOS/INDICES/rnal_tomar.json",
        "validation_report": "DADOS/INDICES/rnal_tomar_manifest_validation_report.json",
        "record_count": len(records),
        "contact_policy": "publicar_apenas_contactos_extraidos_de_contexto_de_contacto; preservar_prefixo_internacional_explicito",
        "records": records
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result":"SUCCESS","record_count":len(records),"output":str(OUT)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
