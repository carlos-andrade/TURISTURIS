#!/usr/bin/env python3
"""WEB-12.1 — ingestão controlada RNET + RNAL.

Não grava dados na árvore principal por execução acidental.
A execução gera RAW em CONTINENTE/DADOS/RAW/ALOJAMENTOS/ e um manifesto.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

RNET = "https://geo.turismodeportugal.pt/server/rest/services/TDP/OpenData_ETExistentes/MapServer/0/query"
RNAL = "https://geo.turismodeportugal.pt/server/rest/services/TDP/OpenData_AL/MapServer/6/query"

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "RAW" / "ALOJAMENTOS"

PAGE_SIZE = 200000


def fetch_all(endpoint: str, key: str) -> list[dict]:
    offset = 0
    records: list[dict] = []

    while True:
        params = {
            "where": "1=1",
            "outFields": "*",
            "returnGeometry": "true",
            "f": "json",
            "resultOffset": offset,
            "resultRecordCount": PAGE_SIZE,
            "orderByFields": "OBJECTID",
        }
        url = endpoint + "?" + urlencode(params)
        req = Request(url, headers={"User-Agent": "TURISTURIS-WEB-12.1"})
        with urlopen(req, timeout=120) as response:
            payload = json.load(response)

        if "error" in payload:
            raise RuntimeError(f"{key}: API error: {payload['error']}")

        batch = payload.get("features", [])
        records.extend(batch)

        if len(batch) < PAGE_SIZE:
            break
        offset += len(batch)

    return records


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()

    datasets = {
        "RNET": fetch_all(RNET, "RNET"),
        "RNAL": fetch_all(RNAL, "RNAL"),
    }

    manifest = {
        "schema_version": "1.0",
        "process": "WEB-12.1",
        "generated_at_utc": now,
        "sources": {
            "RNET": RNET,
            "RNAL": RNAL,
        },
        "records": {name: len(rows) for name, rows in datasets.items()},
        "rule": "RAW preservado antes da normalização; nenhuma publicação automática.",
    }

    for name, rows in datasets.items():
        target = RAW / f"{name}_RAW_V1.json"
        target.write_text(
            json.dumps(
                {
                    "source": name,
                    "retrieved_at_utc": now,
                    "features": rows,
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    (RAW / "MANIFESTO_INGESTAO_V1.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
