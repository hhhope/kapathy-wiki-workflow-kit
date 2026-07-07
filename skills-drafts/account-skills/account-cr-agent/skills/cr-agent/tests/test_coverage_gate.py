import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import coverage_gate
import eval_cr_replay


class CoverageGateTest(unittest.TestCase):
    def test_loads_yaml_config_from_skill_repo_and_case_with_strict_merge(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            skill_dir = root / "skill"
            repo = root / "repo"
            case_dir = repo / "CR" / "yqt-trade" / "cases" / "case-1"
            (skill_dir / "rules").mkdir(parents=True)
            case_dir.mkdir(parents=True)
            (repo / "CR" / "yqt-trade").mkdir(parents=True, exist_ok=True)

            (skill_dir / "rules" / "global.yaml").write_text(
                """
rules:
  money:
    title: Money and numeric units
    match:
      any: [amount, balance]
    create_checks:
      required:
        - Input unit is clear
        - Output unit is clear
""".strip(),
                encoding="utf-8",
            )
            (repo / "CR" / "yqt-trade" / "cr-agent.yaml").write_text(
                """
rules:
  money:
    match:
      any: [fee]
""".strip(),
                encoding="utf-8",
            )
            (case_dir / "cr-agent.yaml").write_text(
                """
rules:
  money:
    create_checks:
      required:
        - Normal numeric example closes the flow
settings:
  oversized_hunk_line_threshold: 7
""".strip(),
                encoding="utf-8",
            )

            merged = coverage_gate.load_rule_config(
                skill_dir=skill_dir,
                repo_root=repo,
                project="yqt-trade",
                case_id="case-1",
            )

            money = merged.config["rules"]["money"]
            self.assertEqual(
                money["match"]["any"],
                ["amount", "balance", "fee"],
            )
            self.assertEqual(
                money["create_checks"]["required"],
                [
                    "Input unit is clear",
                    "Output unit is clear",
                    "Normal numeric example closes the flow",
                ],
            )
            self.assertEqual(merged.config["settings"]["oversized_hunk_line_threshold"], 7)
            self.assertEqual(len(merged.sources), 3)
            self.assertTrue(merged.config_hash)

    def test_rejects_config_that_weakens_global_required_checks(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            skill_dir = root / "skill"
            repo = root / "repo"
            (skill_dir / "rules").mkdir(parents=True)
            (repo / "CR" / "yqt-trade").mkdir(parents=True)
            (skill_dir / "rules" / "global.yaml").write_text(
                """
rules:
  money:
    title: Money
    match:
      any: [amount]
    create_checks:
      required: [Input unit is clear, Output unit is clear]
""".strip(),
                encoding="utf-8",
            )
            (repo / "CR" / "yqt-trade" / "cr-agent.yaml").write_text(
                """
rules:
  money:
    create_checks:
      required: [Input unit is clear]
""".strip(),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(coverage_gate.ConfigError, "weakens"):
                coverage_gate.load_rule_config(
                    skill_dir=skill_dir,
                    repo_root=repo,
                    project="yqt-trade",
                    case_id="case-1",
                )

    def test_oversized_money_hunk_creates_child_units_checks_and_blocked_gate(self):
        diff_text = """diff --git a/src/Balance.java b/src/Balance.java
index 1111111..2222222 100644
--- a/src/Balance.java
+++ b/src/Balance.java
@@ -1,2 +1,7 @@
 public class Balance {
-  return oldBalance;
+  BigDecimal amount = bank.getBalance();
+  BigDecimal centAmount = AmountUtil.yuanToCent(amount);
+  ledger.setAvailableBalance(centAmount);
+  ledger.setFreezeBalance(AmountUtil.yuanToCent(bank.getFreezeBalance()));
+  return AmountUtil.yuanToCent(ledger.getAvailableBalance());
 }
"""
        config = {
            "settings": {"oversized_hunk_line_threshold": 2},
            "rules": {
                "money": {
                    "title": "Money and numeric units",
                    "match": {"any": ["amount", "balance", "yuanToCent"]},
                    "create_checks": {
                        "required": [
                            "Input unit is clear",
                            "Internal unit is clear",
                            "Output unit is clear",
                            "Repeated or missing conversion is checked",
                        ]
                    },
                }
            },
        }

        result = coverage_gate.analyze_diff_text(
            diff_text,
            config,
            range_metadata={
                "cr_type": "merge_cr",
                "base": "base",
                "head": "head",
                "merge_base": "base",
                "range_hash": "range",
                "config_hash": "config",
                "agent_version": "test",
            },
        )

        units = result["diff_units"]
        parent = next(unit for unit in units if unit["unit_type"] == "hunk")
        children = [unit for unit in units if unit["unit_type"] == "child_hunk"]
        self.assertEqual(parent["status"], "open")
        self.assertEqual(len(children), 3)
        self.assertTrue(all(child["parent_id"] == parent["id"] for child in children))
        self.assertGreaterEqual(len(result["checks"]), 4)
        self.assertEqual(result["gate"]["decision"], "blocked")
        self.assertIn("open required check", result["gate"]["reasons"])
        self.assertTrue(result["review_groups"])

    def test_diff_ledger_records_file_and_special_units(self):
        diff_text = """diff --git a/src/Old.java b/src/New.java
similarity index 91%
rename from src/Old.java
rename to src/New.java
diff --git a/src/Binary.bin b/src/Binary.bin
new file mode 100644
index 0000000..1111111
Binary files /dev/null and b/src/Binary.bin differ
diff --git a/src/Text.java b/src/Text.java
index 1111111..2222222 100644
--- a/src/Text.java
+++ b/src/Text.java
@@ -1 +1 @@
-old
+new
"""
        result = coverage_gate.analyze_diff_text(
            diff_text,
            {
                "settings": {"oversized_hunk_line_threshold": 80},
                "rules": {
                    "state": {
                        "title": "State",
                        "match": {"any": ["new"]},
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

        types = [unit["unit_type"] for unit in result["diff_units"]]
        self.assertIn("file", types)
        self.assertIn("special", types)
        self.assertIn("hunk", types)


    def test_webank_replay_fixture_declares_expected_blocked_coverage_gate(self):
        fixture = ROOT / "replay" / "webank-split-balance-unit.json"
        data = json.loads(fixture.read_text(encoding="utf-8"))

        self.assertEqual(data["expected_gate"], "blocked")
        self.assertIn("input_diff_artifacts", data)
        self.assertIn("required_consumer_evidence", data)
        self.assertIn("expected_checks", data)
        self.assertEqual(data["expected_money_checker_status"], "blocked")
        self.assertTrue(
            any("Repeated or missing conversion" in check for check in data["expected_checks"])
        )
        self.assertEqual(eval_cr_replay.validate(fixture), [])

    def test_known_good_replay_fixture_allows_empty_issue_list(self):
        fixture = ROOT / "replay" / "known-good-empty-range.json"
        data = json.loads(fixture.read_text(encoding="utf-8"))

        self.assertEqual(data["expected_gate"], "allow")
        self.assertEqual(data["expected_issues"], [])
        self.assertEqual(eval_cr_replay.validate(fixture), [])

    def test_formal_report_replay_fixture_preserves_repo_template_shape(self):
        fixture = ROOT / "replay" / "yqt-formal-report-repo-existing.json"
        data = json.loads(fixture.read_text(encoding="utf-8"))

        self.assertEqual(data["formal_report"]["report_profile"], "repo_existing")
        self.assertEqual(eval_cr_replay.validate(fixture), [])

    def test_formal_report_replay_fails_when_expected_shape_is_missing(self):
        fixture = ROOT / "replay" / "yqt-formal-report-repo-existing.json"
        data = json.loads(fixture.read_text(encoding="utf-8"))
        data["formal_report"]["expected_contains"].append("text that cannot be rendered")

        with tempfile.TemporaryDirectory() as raw:
            broken = Path(raw) / "broken-formal-report.json"
            broken.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

            errors = eval_cr_replay.validate(broken)

        self.assertTrue(errors)
        self.assertTrue(any("expected formal report text not found" in error for error in errors))
