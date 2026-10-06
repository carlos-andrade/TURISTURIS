#!/usr/bin/env python3
"""Descobre todos os RNAL do concelho de Peso da Régua na fonte oficial de dados abertos do Turismo de Portugal."""
import csv
import json
from pathlib import Path
import requests

URL = "https://geo.turismodeportugal.pt/server/rest/services/TDP/OpenData_AL/MapServer/6/query"
WHERE = "Concelho='Peso da Régua'"
FIELDS = [
    "NrRNAL","Denominacao","DataRegisto","DataAberturaPublico","Modalidade",
    "NrUtentes","Endereco","CodigoPostal","LOCALIDADE","LatLong","Freguesia",
    "Concelho","Distrito","SeloCleanSafe"
]
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "DADOS" / "INDICES"
OUT.mkdir(parents=True, exist_ok=True)

params = {
    "where": WHERE,
    "outFields": ",".join(FIELDS),
    "returnGeometry": "false",
    "f": "json",
    "resultRecordCount": 2000,
}
r = requests.get(URL, params=params, timeout=60)
r.raise_for_status()
data = r.json()
if "error" in data:
    raise RuntimeError(data["error"])

features = data.get("features", [])
rows = [f.get("attributes", {}) for f in features]
rows = [x for x in rows if x.get("NrRNAL") is not None]
rows.sort(key=lambda x: int(x["NrRNAL"]))

if not rows:
    raise RuntimeError("Nenhum RNAL encontrado para Peso da Régua.")

payload = {
    "source": URL,
    "where": WHERE,
    "capture_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
    "count": len(rows),
    "records": rows,
}
(OUT / "rnal_peso_da_regua.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
)
with (OUT / "rnal_peso_da_regua.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)

print(json.dumps({"count": len(rows), "output": str(OUT)}, ensure_ascii=False))
