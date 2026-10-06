#!/usr/bin/env python3
"""Captura em lote todas as fichas RNAL descobertas para Peso da Régua."""
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from capturar_fichas_rnet_rnal import capture

INDEX = ROOT / "DADOS" / "INDICES" / "rnal_peso_da_regua.json"

def main():
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    rows = data["records"]
    jobs = [(str(row["NrRNAL"]), row) for row in rows]
    results, failures = [], []

    def run(item):
        number, row = item
        url = f"https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr={number}"
        return capture("RNAL", url)

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(run, item): item for item in jobs}
        for future in as_completed(futures):
            number, _ = futures[future]
            try:
                results.append(future.result())
            except Exception as exc:
                failures.append({"registry_number": number, "error": str(exc)})

    results.sort(key=lambda x: int(x["registry_number"]))
    report = {
        "source_index_count": len(rows),
        "captured_successfully": len(results),
        "failures": failures,
        "result": "SUCCESS" if len(results) == len(rows) and not failures else "FAILED",
    }
    (ROOT / "DADOS" / "INDICES" / "rnal_peso_da_regua_capture_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "SUCCESS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
