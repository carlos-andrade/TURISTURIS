#!/usr/bin/env python3
"""TURISTURIS — WEB-12.6: validação formal da consolidação RNAL Peso da Régua."""
import csv, json
from datetime import datetime, timezone
from pathlib import Path

MASTER = Path("DADOS/INDICES/rnal_peso_da_regua_tabela_mestra.csv")
LOTS = Path("CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/LOTES")
REPORT = Path("DADOS/INDICES/rnal_peso_da_regua_validacao_consolidacao_report.json")
EXPECTED = {0: 50, 50: 50, 100: 50, 150: 32}

def fail(msg):
    raise SystemExit(f"VALIDACAO_FALHOU: {msg}")

def main():
    rows = list(csv.DictReader(MASTER.open(encoding="utf-8", newline="")))
    if len(rows) != 182:
        fail(f"master_records={len(rows)} != 182")
    master_ids = [str(r["id_origem"]) for r in rows]
    if len(set(master_ids)) != 182:
        fail("id_origem duplicado na tabela mestra")

    lot_files = sorted(LOTS.glob("rnal_contactos_offset_*.json"),
                       key=lambda p: int(p.stem.rsplit("_", 1)[-1]))
    offsets = [int(p.stem.rsplit("_", 1)[-1]) for p in lot_files]
    if offsets != [0, 50, 100, 150]:
        fail(f"offsets={offsets} != [0,50,100,150]")

    all_ids = []
    lot_results = []
    for path in lot_files:
        data = json.loads(path.read_text(encoding="utf-8"))
        offset = int(data["offset"])
        records = data.get("records", [])
        ids = [str(r.get("id_origem")) for r in records]
        if data.get("schema_version") != "1.2":
            fail(f"{path}: schema_version inválido")
        if data.get("process") != "WEB-12.6":
            fail(f"{path}: process inválido")
        if data.get("source") != "RNT/RNAL":
            fail(f"{path}: source inválido")
        if data.get("municipio") != "Peso da Régua":
            fail(f"{path}: municipio inválido")
        if data.get("target_total") != 182:
            fail(f"{path}: target_total inválido")
        if data.get("record_count") != EXPECTED[offset] or len(records) != EXPECTED[offset]:
            fail(f"{path}: contagem inválida")
        if len(set(ids)) != len(ids):
            fail(f"{path}: id_origem duplicado")
        if any(i not in set(master_ids) for i in ids):
            fail(f"{path}: id_origem inexistente na tabela mestra")
        if any(r.get("status") != "CONTACTOS_GENERICOS_FONTE" for r in records):
            fail(f"{path}: status inesperado")
        all_ids.extend(ids)
        lot_results.append({
            "offset": offset,
            "record_count": len(records),
            "unique_ids": len(set(ids)),
            "empty_contacts": sum(1 for r in records if not (r.get("telefone") or []) and not (r.get("email") or [])),
        })

    if len(all_ids) != 182 or len(set(all_ids)) != 182:
        fail("cobertura global dos lotes não fecha 182 IDs únicos")
    missing = sorted(set(master_ids) - set(all_ids))
    extra = sorted(set(all_ids) - set(master_ids))
    if missing or extra:
        fail(f"cobertura divergente: missing={missing}, extra={extra}")

    report = {
        "schema_version": "1.0",
        "process": "WEB-12.6-VALIDACAO-CONSOLIDACAO",
        "municipio": "Peso da Régua",
        "target_total": 182,
        "master_records": len(rows),
        "master_unique_id_origem": len(set(master_ids)),
        "lotes_lidos": len(lot_files),
        "lot_results": lot_results,
        "registros_lotes": len(all_ids),
        "ids_unicos_lotes": len(set(all_ids)),
        "master_ids_cobertos": len(set(master_ids) & set(all_ids)),
        "master_ids_em_falta": len(missing),
        "lot_ids_fora_master": len(extra),
        "acceptance": True,
        "executed_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()
