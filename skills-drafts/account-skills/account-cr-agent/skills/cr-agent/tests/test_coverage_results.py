import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import coverage_gate


class CoverageResultsTest(unittest.TestCase):
    def _state_result(self):
        return coverage_gate.analyze_diff_text(
            """diff --git a/src/A.java b/src/A.java
index 1111111..2222222 100644
--- a/src/A.java
+++ b/src/A.java
@@ -1 +1 @@
-old
+new
""",
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
                "range_hash": "range-v2",
                "config_hash": "config",
                "agent_version": "test",
            },
        )

    def test_checker_results_issues_waivers_and_report_are_artifact_driven(self):
        result = coverage_gate.analyze_diff_text(
            """diff --git a/src/Pay.java b/src/Pay.java
index 1111111..2222222 100644
--- a/src/Pay.java
+++ b/src/Pay.java
@@ -1 +1 @@
-oldAmount
+newAmount
""",
            {
                "settings": {"oversized_hunk_line_threshold": 80},
                "rules": {
                    "money": {
                        "title": "Money",
                        "match": {"any": ["amount"]},
                        "create_checks": {"required": ["Input unit is clear"]},
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
        check_id = result["checks"][0]["id"]

        updated = coverage_gate.apply_checker_results(
            result,
            [
                {
                    "check_id": check_id,
                    "status": "issue",
                    "conclusion": "unit chain missing",
                    "evidence_refs": ["diff-units.jsonl:1"],
                    "risk": "high",
                    "unresolved_questions": ["bank payload unit"],
                    "linked_diff_units": result["checks"][0]["diff_unit_ids"],
                }
            ],
            [
                {
                    "owner": "release-owner",
                    "reason": "temporary manual release decision",
                    "expiry": "2026-07-07",
                    "affected_checks": [check_id],
                    "residual_risk": "display may remain wrong until fixed",
                }
            ],
        )

        self.assertEqual(updated["checks"][0]["status"], "waived")
        self.assertEqual(updated["issues"][0]["source_worker"], "coverage_gate")
        self.assertEqual(updated["gate"]["decision"], "blocked")
        report = coverage_gate.render_report(updated)
        self.assertIn("Gate Decision: `blocked`", report)
        self.assertIn("Checks:", report)
        self.assertIn("Waivers: 1", report)

    def test_resume_invalidates_stale_checker_results(self):
        result = self._state_result()
        result["state"].update(
            {
                "range_hash": "range-v2",
                "config_hash": "config",
                "diff_ledger_hash": "ledger-v2",
                "agent_version": "test",
            }
        )
        result["checker_results"] = [
            {
                "check_id": result["checks"][0]["id"],
                "status": "satisfied",
                "conclusion": "old basis",
                "evidence_refs": ["old"],
                "risk": "low",
                "unresolved_questions": [],
                "linked_diff_units": result["checks"][0]["diff_unit_ids"],
                "range_hash": "range-v1",
                "config_hash": "config",
                "diff_ledger_hash": "ledger-v1",
                "agent_version": "test",
            }
        ]

        invalidated = coverage_gate.invalidate_stale_checker_results(result)

        self.assertEqual(invalidated["checker_results"][0]["status"], "blocked")
        self.assertIn("stale", invalidated["checker_results"][0]["conclusion"])
        self.assertEqual(invalidated["gate"]["decision"], "blocked")

    def test_written_report_renders_coverage_artifacts(self):
        result = self._state_result()
        with tempfile.TemporaryDirectory() as raw:
            case_dir = Path(raw)

            coverage_gate.write_case_artifacts(case_dir, result)

            report = (case_dir / "report.md").read_text(encoding="utf-8")
        self.assertIn("Gate Decision:", report)
        self.assertIn("## Coverage", report)
        self.assertIn("Checks:", report)
        self.assertIn("## Checks by Rule", report)
        self.assertIn("state: open=", report)

    def test_money_unit_checker_blocks_when_consumer_evidence_is_missing(self):
        result = coverage_gate.analyze_diff_text(
            """diff --git a/src/WZOpenBankLedgerListService.java b/src/WZOpenBankLedgerListService.java
index 1111111..2222222 100644
--- a/src/WZOpenBankLedgerListService.java
+++ b/src/WZOpenBankLedgerListService.java
@@ -1 +1,3 @@
-ledger.setAvailableBalance(item.getAvailableBalance());
+ledger.setAmount(AmountUtil.yuanToCent(item.getAmount()));
+ledger.setAvailableBalance(AmountUtil.yuanToCent(item.getAvailableBalance()));
+ledger.setFreezeBalance(AmountUtil.yuanToCent(item.getFreezeBalance()));
""",
            {
                "settings": {"oversized_hunk_line_threshold": 80},
                "rules": {
                    "money": {
                        "title": "Money",
                        "match": {"any": ["amount", "balance", "yuanToCent"]},
                        "create_checks": {
                            "required": [
                                "Input unit is clear",
                                "Output unit is clear",
                                "Repeated or missing conversion is checked",
                            ]
                        },
                    }
                },
            },
            {
                "cr_type": "post_incident_cr",
                "base": "d80cdd702^",
                "head": "d80cdd702",
                "merge_base": "d80cdd702^",
                "range_hash": "range",
                "config_hash": "config",
                "agent_version": "test",
            },
        )

        checker_results = coverage_gate.run_money_unit_checker(
            result,
            consumer_evidence=[],
        )

        self.assertTrue(checker_results)
        self.assertTrue(all(item["status"] == "blocked" for item in checker_results))
        self.assertTrue(any("consumer evidence" in item["conclusion"] for item in checker_results))
        self.assertTrue(any("QueryBalanceHandle" in question for item in checker_results for question in item["unresolved_questions"]))
        self.assertTrue(any(item.get("review_group_ids") for item in checker_results))

        updated = coverage_gate.apply_checker_results(result, checker_results)

        self.assertEqual(updated["gate"]["decision"], "blocked")
        self.assertTrue(updated["issues"])
        self.assertTrue(any(issue["related_review_groups"] for issue in updated["issues"]))

    def test_formal_report_keeps_reader_template_and_shows_open_checks_by_rule(self):
        result = self._state_result()

        report = coverage_gate.render_formal_report(
            result,
            project="yqt-trade",
            report_target="RCYW-16690",
            report_profile="repo",
            case_report_path="CR/yqt-trade/cases/RCYW-16690/report.md",
        )

        self.assertIn("最终结论（是否可发布）", report)
        self.assertIn("CR 执行审计", report)
        self.assertIn("覆盖矩阵", report)
        self.assertIn("state", report)
        self.assertIn("open=", report)
        self.assertIn("Case Coverage Artifact", report)
        self.assertLess(report.index("最终结论（是否可发布）"), report.index("覆盖矩阵"))

    def test_confirmed_issues_feed_registry_gate_and_stage_report(self):
        result = self._state_result()
        check_id = result["checks"][0]["id"]
        unit_id = result["checks"][0]["diff_unit_ids"][0]

        updated = coverage_gate.apply_confirmed_issues(
            result,
            [
                {
                    "CR-ID": "CR-TECH-001",
                    "severity": "high",
                    "category": "state_machine",
                    "title": "WZ retry route calls WS processor",
                    "evidence_refs": ["OpenAccountEntFacadeImpl.java:215"],
                    "impact": "WZ retry cannot enter the WZ ledger flow",
                    "required_action": "Route WZ retry to wzOpenAccountBiz",
                    "blocking": True,
                    "linked_check_ids": [check_id],
                    "linked_diff_unit_ids": [unit_id],
                    "source_worker": "cr-technical-review",
                }
            ],
        )

        self.assertEqual(updated["checks"][0]["status"], "issue")
        self.assertEqual(updated["issues"][0]["CR-ID"], "CR-TECH-001")
        self.assertEqual(updated["issues"][0]["related_checks"], [check_id])
        self.assertEqual(updated["gate"]["decision"], "blocked")
        self.assertIn("high issue", updated["gate"]["reasons"])

        report = coverage_gate.render_formal_report(
            updated,
            project="yqt-trade",
            report_target="RCYW-16690",
            report_profile="repo",
            case_report_path="CR/yqt-trade/cases/RCYW-16690/report.md",
        )

        self.assertIn("Report State: `stage_report`", report)
        self.assertIn("WZ retry route calls WS processor", report)
        self.assertIn("## Gate Blocker Sources", report)
        self.assertIn("confirmed high/severe issues: 1", report)
        self.assertIn("## Open Check Drilldown", report)
        self.assertIn("check-", report)
        self.assertIn("Full checks list:", report)

    def test_formal_report_preserves_repo_existing_template_wrappers(self):
        result = self._state_result()
        with tempfile.TemporaryDirectory() as raw:
            reference = Path(raw) / "2026-07-01.md"
            reference.write_text(
                "\n".join(
                    [
                        "---",
                        "title: 代码评审报告 — yqt-trade 2026-07-01",
                        "tags: [CR, 代码评审, yqt-trade]",
                        "---",
                        "",
                        "# 代码评审报告 — yqt-trade 2026-07-01",
                        "",
                        "> [!tip] 本报告可关联到 [[README|项目 CR 索引页]]",
                        "",
                        "> 标签：`#CR` `#代码评审`",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            report = coverage_gate.render_formal_report(
                result,
                project="yqt-trade",
                report_target="RCYW-16690",
                report_profile="repo_existing",
                case_report_path="CR/yqt-trade/cases/RCYW-16690/report.md",
                reference_report_path=str(reference),
            )

        self.assertTrue(report.startswith("---\n"))
        self.assertIn("title: 代码评审报告 — yqt-trade RCYW-16690", report)
        self.assertIn("# 代码评审报告 — yqt-trade RCYW-16690", report)
        self.assertIn("[!tip]", report)
        self.assertNotIn("# CR Report:", report)

    def test_cr_report_skill_scopes_wrapper_rules_by_profile(self):
        skill_text = (ROOT.parent / "cr-report" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("`plugin_plain` forbids wiki/Obsidian wrappers", skill_text)
        self.assertIn("`repo_existing` may preserve wiki/Obsidian wrappers", skill_text)
        self.assertNotIn("Use a plain Markdown CR template. Do not emit wiki/Obsidian wrappers", skill_text)

    def test_case_artifacts_can_resume_without_model_memory(self):
        result = self._state_result()
        with tempfile.TemporaryDirectory() as raw:
            case_dir = Path(raw)
            coverage_gate.write_case_artifacts(case_dir, result)

            resumed = coverage_gate.read_case_artifacts(case_dir)

        self.assertEqual(resumed["gate"]["decision"], result["gate"]["decision"])
        self.assertEqual(len(resumed["diff_units"]), len(result["diff_units"]))
        self.assertEqual(len(resumed["checks"]), len(result["checks"]))
