#!/usr/bin/env python3
"""
TURISTURIS — Orquestrador canónico de fases.

Executa gates determinísticos por fase, sem saltar etapas e sem voltar
automaticamente a uma fase anterior. O orquestrador valida o estado atual
do repositório e produz um relatório auditável.

Uso:
  python3 scripts/orquestrador_fases_turisturis.py --fase A
  python3 scripts/orquestrador_fases_turisturis.py --fase ALL
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "DADOS" / "INDICES" / "turisturis_orquestrador_fases_ultimo.json"

PHASES = {
    "A": "Fecho Peso da Régua",
    "B": "Padronização territorial",
    "C": "Escala territorial",
    "D": "Consolidação do portal",
}


class GateFailure(Exception):
    pass


def load_json(path: Path):
    if not path.exists():
        raise GateFailure(f"Ficheiro inexistente: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise GateFailure(f"JSON inválido: {path.relative_to(ROOT)}: {exc}") from exc


def read_text(path: Path):
    if not path.exists():
        raise GateFailure(f"Ficheiro inexistente: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def gate(name, fn):
    try:
        result = fn()
        return {"gate": name, "status": "PASS", "detail": result or "OK"}
    except GateFailure as exc:
        return {"gate": name, "status": "FAIL", "detail": str(exc)}
    except Exception as exc:
        return {"gate": name, "status": "ERROR", "detail": repr(exc)}


def phase_a():
    results = []

    pub = load_json(ROOT / "CONTINENTE/DADOS/PUBLICACAO/RNAL_PESO_DA_REGUA_PUBLICAVEIS_V1.json")
    records = pub.get("records", [])

    results.append(gate("A1 — publicação RNAL existe e tem 182 registos",
        lambda: f"record_count={pub.get('record_count')}"
        if pub.get("record_count") == 182 and len(records) == 182
        else (_ for _ in ()).throw(GateFailure(
            f"Esperado 182; record_count={pub.get('record_count')}, records={len(records)}"
        ))))

    def territorial():
        bad = []
        for r in records:
            if r.get("município") != "Peso da Régua" or r.get("distrito") != "Vila Real":
                bad.append(r.get("id"))
        if bad:
            raise GateFailure(f"Enquadramento inválido em {len(bad)} registos: {bad[:10]}")
        return "Município=Peso da Régua; Distrito=Vila Real em 100% dos registos"
    results.append(gate("A2 — Município/Distrito canónicos", territorial))

    def freguesia():
        missing = [r.get("id") for r in records if not str(r.get("freguesia") or "").strip()]
        if missing:
            raise GateFailure(f"Freguesia ausente em {len(missing)} registos: {missing[:10]}")
        return "Freguesia presente em 100% dos registos"
    results.append(gate("A3 — Freguesia estruturada", freguesia))

    def vilarinho():
        matches = [r for r in records if r.get("freguesia") == "Vilarinho dos Freires"]
        if len(matches) != 8:
            raise GateFailure(f"Esperados 8 registos em Vilarinho dos Freires; encontrados {len(matches)}")
        return "8 registos"
    results.append(gate("A4 — Vilarinho dos Freires", vilarinho))

    audit = load_json(ROOT / "DADOS/INDICES/rnal_peso_da_regua_contactos_auditoria_2026-10-06.json")
    def contacts():
        cmp = audit.get("comparacao_telefone_com_fonte_oficial", {})
        if audit.get("resultado") != "APROVADO_PARA_PUBLICACAO_CONTACTOS":
            raise GateFailure(f"Resultado da auditoria: {audit.get('resultado')}")
        if cmp.get("correspondencias_exatas") != 115 or cmp.get("divergencias") != 0 or cmp.get("ausencias_na_fonte") != 0:
            raise GateFailure(f"Auditoria telefónica não aprovada: {cmp}")
        return "115/115 correspondências; 0 divergências; 0 ausências"
    results.append(gate("A5 — contactos auditados", contacts))

    index = read_text(ROOT / "index.html")
    def public_rules():
        required = ["Freguesia:", "Município:", "Distrito:"]
        missing = [x for x in required if x not in index]
        if missing:
            raise GateFailure(f"Rótulos públicos ausentes: {missing}")
        if re.search(r"Website:</strong>|<strong>Website", index, re.I):
            raise GateFailure("Website ainda aparece no HTML público")
        if "estado_validação" in index or "grau_confiança" in index:
            raise GateFailure("Campos de validação interna aparecem no HTML público")
        return "Freguesia → Município → Distrito; Website e estados internos ocultos"
    results.append(gate("A6 — regras de publicação pública", public_rules))

    return results


def phase_b():
    results = []
    letters = [
        "GOVERNANÇA/CARTAS/CARTA_REGENTE.md",
        "GOVERNANÇA/CARTAS/CARTA_DE_DADOS.md",
        "GOVERNANÇA/CARTAS/CARTA_CAPTURA_RIGIDA_FICHAS_RNET_RNAL.md",
        "GOVERNANÇA/CARTAS/CARTA_PARA_CARTAS.md",
    ]

    def governance():
        needle = "Freguesia"
        missing = []
        for rel in letters:
            text = read_text(ROOT / rel)
            if needle not in text or "Município" not in text or "Distrito" not in text:
                missing.append(rel)
        if missing:
            raise GateFailure(f"Regra territorial ausente em: {missing}")
        return "As 4 cartas regentes contêm o padrão territorial"
    results.append(gate("B1 — governação territorial", governance))

    def structured():
        pub = load_json(ROOT / "CONTINENTE/DADOS/PUBLICACAO/RNAL_PESO_DA_REGUA_PUBLICAVEIS_V1.json")
        for r in pub.get("records", []):
            if not all(str(r.get(k) or "").strip() for k in ("freguesia", "município", "distrito")):
                raise GateFailure(f"Registo sem território estruturado: {r.get('id')}")
        return "Território estruturado; não depende de texto manual da ficha pública"
    results.append(gate("B2 — modelo territorial estruturado", structured))

    return results


def phase_c():
    results = []

    prerequisites_a = phase_a()
    a_ok = all(item["status"] == "PASS" for item in prerequisites_a)
    results.append({
        "gate": "C1.A — pré-requisitos da Fase A",
        "status": "PASS" if a_ok else "BLOCKED",
        "detail": "Todos os gates da Fase A estão aprovados."
        if a_ok
        else f"Fase A não aprovada: {[item for item in prerequisites_a if item['status'] != 'PASS']}",
    })

    prerequisites_b = phase_b()
    b_ok = all(item["status"] == "PASS" for item in prerequisites_b)
    results.append({
        "gate": "C1.B — pré-requisitos da Fase B",
        "status": "PASS" if b_ok else "BLOCKED",
        "detail": "Todos os gates da Fase B estão aprovados."
        if b_ok
        else f"Fase B não aprovada: {[item for item in prerequisites_b if item['status'] != 'PASS']}",
    })

    if a_ok and b_ok:
        results.append({
            "gate": "C1 — expansão territorial",
            "status": "PASS",
            "detail": "Fase A e Fase B aprovadas integralmente; Fase C elegível para promoção.",
        })
    else:
        results.append({
            "gate": "C1 — expansão territorial",
            "status": "BLOCKED",
            "detail": "Fase C só pode ser promovida depois da aprovação integral das fases A e B.",
        })

    return results


def phase_d():
    return [{
        "gate": "D1 — consolidação do portal",
        "status": "BLOCKED",
        "detail": "Fase D depende da promoção formal das fases anteriores.",
    }]


RUNNERS = {"A": phase_a, "B": phase_b, "C": phase_c, "D": phase_d}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fase", choices=["A", "B", "C", "D", "ALL"], default="A")
    args = parser.parse_args()

    phases = list(PHASES) if args.fase == "ALL" else [args.fase]
    report = {
        "schema_version": "1.0",
        "process": "ORQUESTRADOR_FASES_TURISTURIS",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "requested_phase": args.fase,
        "repository": "carlos-andrade/TURISTURIS",
        "phases": [],
    }

    overall = True
    for phase in phases:
        results = RUNNERS[phase]()
        status = "PASS" if all(x["status"] == "PASS" for x in results) else "BLOCKED"
        if any(x["status"] in ("FAIL", "ERROR") for x in results):
            overall = False
        if any(x["status"] == "BLOCKED" for x in results):
            overall = False
        report["phases"].append({
            "id": phase,
            "name": PHASES[phase],
            "status": status,
            "gates": results,
        })
        if status != "PASS":
            break

    report["overall_status"] = "PASS" if overall else "BLOCKED"
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if overall else 1)


if __name__ == "__main__":
    main()

# Execução formal solicitada: [FASE:C]
