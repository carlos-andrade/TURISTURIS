#!/usr/bin/env python3
"""WEB-12.2 — normalização nacional RNET + RNAL."""
from __future__ import annotations
import json
import re
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "RAW" / "ALOJAMENTOS"
OUT = ROOT / "NORMALIZAÇÃO" / "ALOJAMENTOS"
SOURCE_CONFIG = {
    "RNET": {"file": "RNET_RAW_V1.json", "source_id": "NrRNET", "tipo": "alojamento_turistico", "prefix": "PT-ALOJ-RNET"},
    "RNAL": {"file": "RNAL_RAW_V1.json", "source_id": "NrRNAL", "tipo": "alojamento_local", "prefix": "PT-ALOJ-RNAL"},
}
def slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", value or "").strip("-").upper() or "SEM-ID"
def first(*values):
    for value in values:
        if value not in (None, "", "null"):
            return value
    return None
def normalize_feature(source: str, feature: dict, verified_at: str) -> dict:
    a = feature.get("attributes") or {}
    g = feature.get("geometry") or {}
    cfg = SOURCE_CONFIG[source]
    source_value = first(a.get(cfg["source_id"]), a.get("OBJECTID"))
    territory = first(a.get("Concelho"), a.get("Distrito"), "PORTUGAL")
    canonical_id = f'{cfg["prefix"]}-{slug(territory)}-{slug(str(source_value))}'
    coordinates = None
    if isinstance(g, dict) and g.get("x") is not None and g.get("y") is not None:
        coordinates = {"latitude": g["y"], "longitude": g["x"]}
    endpoint = "https://geo.turismodeportugal.pt/server/rest/services/TDP/" + ("OpenData_ETExistentes/MapServer/0" if source == "RNET" else "OpenData_AL/MapServer/6")
    return {"id": canonical_id, "nome": first(a.get("Denominacao"), f"{source} {source_value}"), "tipo": cfg["tipo"], "país": "Portugal", "região": first(a.get("NUTSII")), "distrito_arquipélago": first(a.get("Distrito")), "município": first(a.get("Concelho")), "localidade": first(a.get("LocalidadeCP"), a.get("LOCALIDADE")), "endereço": first(a.get("Endereco")), "coordenadas": coordinates, "descrição": None, "história": None, "interesse_turístico": "alojamento turístico", "contactos": None, "telefone": None, "email": first(a.get("Email")), "website": first(a.get("Website")), "horários": None, "preços": None, "acessibilidade": None, "serviços": None, "reservas": None, "fontes": [{"fonte": source, "id_origem": source_value, "endpoint": endpoint, "data_recolha": verified_at}], "data_verificação": verified_at, "data_atualização": verified_at, "estado_validação": "EM_VERIFICACAO", "grau_confiança": "MÉDIO", "observações": f"Normalizado da fonte {source}; campos ausentes permanecem vazios. Não houve deduplicação entre RNET e RNAL.", "origem_raw": source}
def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    manifest = {"schema_version": "1.0", "process": "WEB-12.2", "generated_at_utc": now, "rule": "RNET e RNAL permanecem conjuntos independentes; nenhuma deduplicação cross-source.", "datasets": {}}
    for source, cfg in SOURCE_CONFIG.items():
        payload = json.loads((RAW / cfg["file"]).read_text(encoding="utf-8"))
        rows = [normalize_feature(source, f, now) for f in payload.get("features", [])]
        target = OUT / f"{source}_NORMALIZADO_V1.json"
        target.write_text(json.dumps({"schema_version": "1.0", "source": source, "generated_at_utc": now, "record_count": len(rows), "records": rows}, ensure_ascii=False), encoding="utf-8")
        manifest["datasets"][source] = {"raw_file": cfg["file"], "normalized_file": target.name, "record_count": len(rows)}
    (OUT / "MANIFESTO_NORMALIZACAO_V1.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
if __name__ == "__main__":
    main()
