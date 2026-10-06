#!/usr/bin/env python3
import json
from pathlib import Path

BASE = Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS")
MANIFEST = BASE / "MANIFESTO_NORMALIZACAO_V1.json"

CONFIG = {
    "RNET": {
        "file": "RNET_NORMALIZADO_V1.json",
        "prefix": "PT-ALOJ-RNET-",
        "source_id": "NrRNET",
        "expected_state": "EM_VERIFICACAO",
        "expected_confidence": "MÉDIO",
    },
    "RNAL": {
        "file": "RNAL_NORMALIZADO_V1.json",
        "prefix": "PT-ALOJ-RNAL-",
        "source_id": "NrRNAL",
        "expected_state": "EM_VERIFICACAO",
        "expected_confidence": "MÉDIO",
    },
}

REQUIRED = {
    "id", "nome", "tipo", "país", "região", "distrito/arquipélago",
    "município", "localidade", "endereço", "fontes",
    "data_verificação", "data_atualização", "estado_validação",
    "grau_confiança", "observações",
}

def fail(message):
    raise AssertionError(message)

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
assert manifest["process"] == "WEB-12.2", "Manifesto de entrada não é WEB-12.2"

results = {}
for dataset, cfg in CONFIG.items():
    path = BASE / cfg["file"]
    records = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(records, list), f"{dataset}: saída não é lista"

    ids = set()
    source_ids = set()
    invalid = []
    missing_required = []
    bad_prefix = []
    bad_source = []

    for i, r in enumerate(records):
        missing = sorted(REQUIRED - set(r))
        if missing:
            missing_required.append({"index": i, "fields": missing})
        rid = r.get("id")
        if not isinstance(rid, str) or not rid:
            invalid.append({"index": i, "reason": "id inválido"})
        elif rid in ids:
            invalid.append({"index": i, "reason": f"id duplicado: {rid}"})
        else:
            ids.add(rid)

        if not isinstance(rid, str) or not rid.startswith(cfg["prefix"]):
            bad_prefix.append({"index": i, "id": rid})

        src = r.get("fontes")
        if not isinstance(src, list) or not src:
            bad_source.append({"index": i, "reason": "fontes vazio"})
        else:
            source_values = json.dumps(src, ensure_ascii=False)
            if cfg["source_id"] not in source_values:
                bad_source.append({"index": i, "reason": f"{cfg['source_id']} ausente em fontes"})

        if r.get("estado_validação") != cfg["expected_state"]:
            invalid.append({"index": i, "reason": "estado_validação inesperado"})
        if r.get("grau_confiança") != cfg["expected_confidence"]:
            invalid.append({"index": i, "reason": "grau_confiança inesperado"})

        if not r.get("tipo"):
            invalid.append({"index": i, "reason": "tipo vazio"})
        if not r.get("nome"):
            invalid.append({"index": i, "reason": "nome vazio"})

    assert not invalid, f"{dataset}: {len(invalid)} inconsistências"
    assert not missing_required, f"{dataset}: campos canônicos ausentes"
    assert not bad_prefix, f"{dataset}: IDs fora do prefixo canônico"
    assert not bad_source, f"{dataset}: proveniência inválida"

    expected = manifest["datasets"][dataset]["record_count"]
    assert len(records) == expected, f"{dataset}: manifesto={expected}, arquivo={len(records)}"

    results[dataset] = {
        "record_count": len(records),
        "unique_ids": len(ids),
        "source_id": cfg["source_id"],
        "state": "VALIDADO_ESTRUTURALMENTE",
    }

out = {
    "schema_version": "1.0",
    "process": "WEB-12.3",
    "validation_type": "VALIDACAO_ESTRUTURAL_E_PROVENIENCIA_V1",
    "input_process": "WEB-12.2",
    "datasets": results,
    "total_records": sum(x["record_count"] for x in results.values()),
    "rules": [
        "RNET e RNAL permanecem conjuntos independentes.",
        "Contagens devem coincidir com o manifesto WEB-12.2.",
        "IDs devem ser únicos dentro de cada dataset e respeitar o prefixo canônico.",
        "Proveniência deve permanecer presente e referenciar o identificador da fonte.",
        "Estado inicial permanece EM_VERIFICACAO e confiança MÉDIO.",
        "Campos canônicos ausentes não são inventados.",
    ],
    "status": "APROVADO",
}

print(json.dumps(out, ensure_ascii=False, indent=2))
