import json
import tempfile
import unittest
from pathlib import Path

from WATCHDOG.engine.watchdog import evaluate_check, evaluate_registry


class WatchdogTests(unittest.TestCase):
    def test_missing_data_is_unknown_not_pass(self):
        result = evaluate_check({"id": "X1", "type": "external_monitor"})
        self.assertEqual(result["state"], "UNKNOWN")

    def test_file_exists_passes_with_evidence_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.txt").write_text("ok", encoding="utf-8")
            result = evaluate_check(
                {"id": "X2", "type": "file_exists", "path": "sample.txt"}, root
            )
            self.assertEqual(result["state"], "PASS")
            self.assertEqual(result["evidence_ref"], "sample.txt")

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            result = evaluate_check(
                {"id": "X3", "type": "file_exists", "path": "../outside.txt"},
                Path(temp),
            )
            self.assertEqual(result["state"], "FAIL")

    def test_invalid_json_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "broken.json").write_text("{", encoding="utf-8")
            result = evaluate_check(
                {"id": "X4", "type": "json_valid", "path": "broken.json"}, root
            )
            self.assertEqual(result["state"], "FAIL")

    def test_duplicate_system_id_is_rejected(self):
        system = {
            "id": "SYS1", "name": "Sample", "owner": "Owner",
            "criticality": "low", "checks": []
        }
        with self.assertRaises(ValueError):
            evaluate_registry({"schema_version": 1, "systems": [system, system]})

    def test_unknown_check_never_counts_as_pass(self):
        registry = {
            "schema_version": 1,
            "systems": [{
                "id": "SYS1", "name": "Sample", "owner": "Owner",
                "criticality": "high",
                "checks": [{"id": "C1", "type": "not_implemented", "required": True}]
            }]
        }
        result = evaluate_registry(registry)
        self.assertEqual(result["counts"]["UNKNOWN"], 1)
        self.assertEqual(result["required_pass_coverage_percent"], 0.0)


if __name__ == "__main__":
    unittest.main()
