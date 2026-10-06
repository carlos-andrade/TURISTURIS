#!/usr/bin/env python3
"""Validate all official RNAL Peso da Régua fiche manifests and evidence structure."""

import json
from pathlib import Path

INDEX_PATH = Path("DADOS/INDICES/rnal_peso_da_regua.json")
ROOT = Path("FICHAS OFICIAIS RNAL")
REPORT_PATH = Path("DADOS/INDICES/rnal_peso_da_regua_manifest_validation_report.json")
RULES = "CARTA-CAPTURA-RNET-RNAL-V1"


def main():
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    expected_ids = {str(x["NrRNAL"]) for x in index["records"]}
    results = []
    failures = []

    for registry_number in sorted(expected_ids, key=int):
        base = ROOT / registry_number
        manifest_path = base / "audit" / "manifest.json"
        item = {
            "registry_number": registry_number,
            "manifest_exists": manifest_path.is_file(),
            "result": "FAILED",
            "valid": False,
        }

        if not manifest_path.is_file():
            item["error"] = "MANIFEST_MISSING"
            failures.append(item)
            results.append(item)
            continue

        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            raw_files = [p for p in (base / "raw").rglob("*") if p.is_file()] if (base / "raw").is_dir() else []
            structured_files = [p for p in (base / "structured").rglob("*") if p.is_file()] if (base / "structured").is_dir() else []

            checks = {
                "type": manifest.get("type") == "RNAL",
                "registry_number": str(manifest.get("registry_number")) == registry_number,
                "source_url": manifest.get("source_url") == f"https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr={registry_number}",
                "http_status": manifest.get("http_status") == 200,
                "source_sha256": bool(manifest.get("source_sha256")),
                "structured_sha256": bool(manifest.get("structured_sha256")),
                "result": manifest.get("result") == "SUCCESS",
                "rules": manifest.get("rules") == RULES,
                "raw_dir": (base / "raw").is_dir() and bool(raw_files),
                "structured_dir": (base / "structured").is_dir() and bool(structured_files),
                "audit_dir": (base / "audit").is_dir(),
            }
            item["checks"] = checks
            item["raw_file_count"] = len(raw_files)
            item["structured_file_count"] = len(structured_files)
            item["valid"] = all(checks.values())
            item["result"] = "SUCCESS" if item["valid"] else "FAILED"
            if not item["valid"]:
                failures.append(item)
        except Exception as exc:
            item["error"] = f"{type(exc).__name__}: {exc}"
            failures.append(item)

        results.append(item)

    report = {
        "validation_version": "V1",
        "source_index": str(INDEX_PATH),
        "expected_count": len(expected_ids),
        "validated_count": len(results),
        "valid_count": sum(1 for x in results if x["valid"]),
        "failure_count": len(failures),
        "failures": failures,
        "result": "SUCCESS" if len(expected_ids) == len(results) == sum(1 for x in results if x["valid"]) else "FAILED",
        "rules": RULES,
        "records": results,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "expected_count": report["expected_count"],
        "validated_count": report["validated_count"],
        "valid_count": report["valid_count"],
        "failure_count": report["failure_count"],
        "result": report["result"],
    }, ensure_ascii=False))

    raise SystemExit(0 if report["result"] == "SUCCESS" else 1)


if __name__ == "__main__":
    main()
