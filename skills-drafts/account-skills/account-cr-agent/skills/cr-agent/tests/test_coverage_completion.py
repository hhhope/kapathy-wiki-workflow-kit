import sys
import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import coverage_gate


class CoverageCompletionTest(unittest.TestCase):
    def test_range_stale_invalid_type_and_high_unresolved_question_block_gate(self):
        gate = coverage_gate.evaluate_gate(
            {
                "cr_type": "unknown_cr",
                "base": "base",
                "head": "head",
                "merge_base": "base",
                "range_hash": "range",
                "config_hash": "config",
                "agent_version": "test",
                "range_stale": True,
            },
            [],
            [],
            [
                {
                    "status": "satisfied",
                    "risk": "high",
                    "unresolved_questions": ["unit chain unclear"],
                    "evidence_refs": ["evidence"],
                }
            ],
        )

        self.assertEqual(gate["decision"], "blocked")
        self.assertIn("invalid CR type", gate["reasons"])
        self.assertIn("stale range", gate["reasons"])
        self.assertIn("high-risk unresolved question", gate["reasons"])

    def test_large_file_special_unit_and_shared_signal_review_group(self):
        diff_text = """diff --git a/src/A.java b/src/A.java
index 1111111..2222222 100644
--- a/src/A.java
+++ b/src/A.java
@@ -1,2 +1,5 @@
-old
+ledgerId = request.getLedgerId();
+status = query(ledgerId);
+return status;
diff --git a/src/B.java b/src/B.java
index 3333333..4444444 100644
--- a/src/B.java
+++ b/src/B.java
@@ -1 +1,2 @@
-old
+return ledgerId;
"""
        result = coverage_gate.analyze_diff_text(
            diff_text,
            {
                "settings": {"oversized_hunk_line_threshold": 2},
                "rules": {
                    "state": {
                        "title": "State",
                        "match": {"any": ["status"]},
                        "create_checks": {"required": ["State behavior is checked"]},
                    }
                },
            },
            {
                "cr_type": "merge_cr",
                "base": "base",
                "head": "head",
                "merge_base": "base",
                "range_hash": "range",
                "config_hash": "config",
                "agent_version": "test",
            },
        )

        special_types = {unit.get("special_type") for unit in result["diff_units"]}
        group_types = {group.get("group_type") for group in result["review_groups"]}
        self.assertIn("large_file", special_types)
        self.assertIn("shared_signal", group_types)

    def test_manual_checker_fallback_and_blocked_case_result(self):
        check = {
            "id": "check-1",
            "diff_unit_ids": ["unit-1"],
            "title": "Input unit is clear",
        }

        fallback = coverage_gate.manual_checker_fallback(check, "checker unavailable")
        blocked = coverage_gate.blocked_case_result("config failure")

        self.assertEqual(fallback["status"], "blocked")
        self.assertEqual(fallback["linked_diff_units"], ["unit-1"])
        self.assertEqual(blocked["gate"]["decision"], "blocked")
        self.assertEqual(blocked["checker_results"][0]["status"], "blocked")
        self.assertIn("config failure", blocked["gate"]["reasons"])

    def test_cli_handles_delete_and_rename_metadata_without_filtering(self):
        with tempfile.TemporaryDirectory() as raw:
            repo = Path(raw) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "cr-agent@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "CR Agent"], cwd=repo, check=True)
            (repo / "DeleteMe.java").write_text("class DeleteMe {}\n", encoding="utf-8")
            (repo / "RenameMe.java").write_text("class RenameMe {}\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "base"], cwd=repo, check=True, stdout=subprocess.DEVNULL)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()

            (repo / "DeleteMe.java").unlink()
            (repo / "Renamed.java").write_text((repo / "RenameMe.java").read_text(encoding="utf-8"), encoding="utf-8")
            (repo / "RenameMe.java").unlink()
            subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-m", "rename delete"], cwd=repo, check=True, stdout=subprocess.DEVNULL)
            head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()

            with contextlib.redirect_stdout(io.StringIO()):
                code = coverage_gate.main([
                    "--repo", str(repo),
                    "--project", "yqt-trade",
                    "--case-id", "rename-delete",
                    "--base", base,
                    "--head", head,
                ])

            case_dir = repo / "CR" / "yqt-trade" / "cases" / "rename-delete"
            result = coverage_gate.read_case_artifacts(case_dir)
        special_types = {unit.get("special_type") for unit in result["diff_units"]}
        special_ids = [unit["id"] for unit in result["diff_units"] if unit["unit_type"] == "special"]
        self.assertEqual(code, 3)
        self.assertIn("delete", special_types)
        self.assertIn("rename", special_types)
        self.assertTrue(all(item.startswith("special-") for item in special_ids))
