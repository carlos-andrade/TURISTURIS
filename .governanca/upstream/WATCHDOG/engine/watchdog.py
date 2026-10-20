#!/usr/bin/env python3
"""Validador inicial WATCHDOG: configuração e verificações locais, sem sondagem externa."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

VERSION = "0.1.0"
ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "WATCHDOG" / "registry" / "sistemas-monitorizados.json"
VALID_STATES = {"PASS", "WARN", "FAIL", "UNKNOWN"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def evaluate_check(check: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    check_id = str(check.get("id", "UNIDENTIFIED"))
    kind = check.get("type")
    result: dict[str, Any] = {
        "check_id": check_id,
        "name": check.get("name", check_id),
        "state": "UNKNOWN",
        "details": "",
        "evidence_ref": "",
        "evaluator_version": VERSION,
    }
    relative = check.get("path")
    if kind in {"file_exists", "nonempty_file", "json_valid"}:
        if not isinstance(relative, str) or not relative.strip():
            result["state"] = "FAIL"
            result["details"] = "O tipo de verificação exige um caminho relativo."
            return result
        path = (root / relative).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError:
            result["state"] = "FAIL"
            result["details"] = "O caminho sai da raiz permitida."
            return result
        result["evidence_ref"] = str(path.relative_to(root.resolve()))
        if kind == "file_exists":
            result["state"] = "PASS" if path.is_file() else "FAIL"
            result["details"] = "Ficheiro encontrado." if path.is_file() else "Ficheiro obrigatório ausente."
        elif kind == "nonempty_file":
            ok = path.is_file() and path.stat().st_size > 0
            result["state"] = "PASS" if ok else "FAIL"
            result["details"] = "Ficheiro presente e não vazio." if ok else "Ficheiro ausente ou vazio."
        else:
            try:
                load_json(path)
                result["state"] = "PASS"
                result["details"] = "JSON válido."
            except (OSError, json.JSONDecodeError) as exc:
                result["state"] = "FAIL"
                result["details"] = f"JSON inválido ou inacessível: {exc.__class__.__name__}."
    else:
        result["state"] = "UNKNOWN"
        result["details"] = "Tipo de verificação não implementado; não há prova de sucesso."
    return result


def evaluate_registry(registry: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    if registry.get("schema_version") != 1 or not isinstance(registry.get("systems"), list):
        raise ValueError("Registo inválido: esperado schema_version=1 e systems como lista.")
    systems = registry["systems"]
    ids: set[str] = set()
    checks_out = []
    for system in systems:
        if not isinstance(system, dict):
            raise ValueError("Cada sistema deve ser um objeto JSON.")
        required = ("id", "name", "owner", "criticality", "checks")
        missing = [field for field in required if field not in system]
        if missing:
            raise ValueError(f"Sistema sem campos obrigatórios {missing}.")
        if system["id"] in ids:
            raise ValueError(f"ID de sistema duplicado: {system['id']}.")
        ids.add(system["id"])
        if system["criticality"] not in {"critical", "high", "medium", "low"}:
            raise ValueError(f"Criticidade inválida no sistema {system['id']}.")
        if not isinstance(system["checks"], list):
            raise ValueError(f"checks deve ser uma lista no sistema {system['id']}.")
        check_ids: set[str] = set()
        for check in system["checks"]:
            if not isinstance(check, dict) or not isinstance(check.get("id"), str):
                raise ValueError(f"Verificação sem ID válido no sistema {system['id']}.")
            if check["id"] in check_ids:
                raise ValueError(f"ID de verificação duplicado: {check['id']}.")
            check_ids.add(check["id"])
            item = evaluate_check(check, root)
            item["system_id"] = system["id"]
            item["required"] = bool(check.get("required", False))
            checks_out.append(item)
    counts = {state: sum(1 for item in checks_out if item["state"] == state) for state in sorted(VALID_STATES)}
    required_checks = [item for item in checks_out if item["required"]]
    required_pass = sum(1 for item in required_checks if item["state"] == "PASS")
    coverage = round(required_pass / len(required_checks) * 100, 1) if required_checks else 100.0
    return {
        "watchdog_version": VERSION,
        "registry": str(REGISTRY.relative_to(root.resolve())) if root.resolve() in REGISTRY.resolve().parents else "custom",
        "system_count": len(systems),
        "check_count": len(checks_out),
        "required_check_count": len(required_checks),
        "required_pass_count": required_pass,
        "required_pass_coverage_percent": coverage,
        "counts": counts,
        "checks": checks_out,
        "limitations": "Validação local de configuração e ficheiros; não prova disponibilidade de serviços externos.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validar o registo e executar verificações locais.")
    parser.add_argument("--registry", type=Path, default=REGISTRY, help="Caminho alternativo para o registo JSON.")
    args = parser.parse_args()
    try:
        registry = load_json(args.registry)
        result = evaluate_registry(registry, ROOT)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"state": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    # UNKNOWN não é sucesso; o MVP informa a lacuna, mas só falhas verificáveis
    # bloqueiam a validação. A cobertura operacional continua explicitamente parcial.
    return 1 if result["counts"]["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
