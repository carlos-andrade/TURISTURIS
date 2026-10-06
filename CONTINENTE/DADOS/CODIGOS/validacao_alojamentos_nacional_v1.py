#!/usr/bin/env python3
import json
from pathlib import Path

BASE = Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS")
MANIFEST = BASE / "MANIFESTO_NORMALIZACAO_V1.json"
CONFIG = {
    "RNET": {"file": "RNET_NORMALIZADO_V1.json", "prefix": "PT-ALOJ-RNET-", "source_id": "NrRNET"},
    "RNAL": {"file": "RNAL_NORMALIZADO_V1.json", "prefix": "PT-ALOJ-RNAL-", "source_id": "NrRNAL"},
}
REQUIRED = {
    "id", "nome", "tipo", "país", "região", "distrito ou arquipélago",
    "município", "localidade", "endereço", "descrição", "interesse turístico",
    "fontes", "data_verificação", "data_atualização", "estado_validação",
    "grau_confiança", "observações",
}
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
assert manifest["process"] == "WEB-12.2"
results = {}
for dataset, cfg in CONFIG.items():
    payload = json.loads((BASE / cfg["file"]).read_text(encoding="utf-8"))
    assert isinstance(payload, dict) and isinstance(payload.get("records"), list), f"{dataset}: envelope inválido"
    records = payload["records"]
    ids = set()
    for i, r in enumerate(records):
        missing = REQUIRED - set(r)
        assert not missing, f"{dataset}: registro {i} sem campos {sorted(missing)}"
        rid = r["id"]
        assert isinstance(rid, str) and rid and rid.startswith(cfg["prefix"]), f"{dataset}: ID inválido no registro {i}"
        assert rid not in ids, f"{dataset}: ID duplicado {rid}"
        ids.add(rid)
        assert r["estado_validação"] == "EM_VERIFICACAO", f"{dataset}: estado inválido"
        assert r["grau_confiança"] == "MÉDIO", f"{dataset}: confiança inválida"
        assert r["nome"] and r["tipo"] and r["descrição"], f"{dataset}: campos obrigatórios vazios no registro {i}"
        fontes = r["fontes"]
        assert isinstance(fontes, list) and fontes, f"{dataset}: proveniência ausente no registro {i}"
        assert any(f.get("fonte") == dataset and f.get("id_origem") is not None for f in fontes), f"{dataset}: id_origem ausente na proveniência do registro {i}"
    expected = manifest["datasets"][dataset]["record_count"]
    assert len(records) == expected, f"{dataset}: manifesto={expected}, arquivo={len(records)}"
    results[dataset] = {"record_count": len(records), "unique_ids": len(ids), "state": "VALIDADO_ESTRUTURALMENTE"}
out = {
    "schema_version": "1.0",
    "process": "WEB-12.3",
    "validation_type": "VALIDACAO_ESTRUTURAL_E_PROVENIENCIA_V3",
    "input_process": "WEB-12.2",
    "datasets": results,
    "total_records": sum(x["record_count"] for x in results.values()),
    "status": "APROVADO",
}
print(json.dumps(out, ensure_ascii=False, indent=2))
