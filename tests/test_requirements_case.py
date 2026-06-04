from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_case import (
    build_requirements_case_package,
    load_requirements_case_file,
    render_requirements_case_markdown,
    write_requirements_case_file,
)


class RequirementsCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-case-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _package(self) -> dict:
        return build_requirements_case_package(
            case_slug="account-reconciliation",
            status="awaiting_confirmation",
            current_intent={"intent": "new_requirement_intake"},
            domain={
                "status": "confirmed",
                "confirmed": "account",
                "candidates": [{"id": "account", "reason": "material names accounts"}],
            },
            roles=[
                {"id": "finance", "label": "finance"},
                {"id": "system_actor", "label": "system actor"},
            ],
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "domain_refs": ["account_balance"],
                    "context_refs": ["balance_ledger_context"],
                    "aggregate_refs": ["ledger_entry"],
                }
            ],
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "coverage_types": ["state_change", "evidence"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                }
            ],
            domain_coverage=[
                {
                    "subdomain": "account_balance",
                    "coverage_type": "primary",
                    "contexts": ["balance_ledger_context"],
                    "aggregate_roots": ["ledger_entry"],
                    "user_story_ids": ["US-1"],
                    "acceptance_function_ids": ["AF-1"],
                    "review_note": "ledger review lifecycle",
                }
            ],
            soft_evidence={
                "business_rules": [{"summary": "late entries need review"}],
            },
            blockers=[],
            evidence_attachments={
                "material": ["inbox/account-reconciliation.md"],
                "diagnosis": ["wiki/ops/requirements-diagnosis.md"],
            },
            proof_boundary_notes=["This case does not validate API or DDL correctness."],
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def _payment_transaction_package(self) -> dict:
        return build_requirements_case_package(
            case_slug="agent-subscription-payment",
            status="requirements_ready",
            current_intent={"intent": "new_requirement_intake"},
            domain={
                "status": "confirmed",
                "confirmed": "billing_revenue",
                "candidates": [{"id": "billing_revenue", "reason": "subscription payment"}],
            },
            roles=[
                {
                    "id": "R-payment-ops-owner",
                    "mention": "支付交易处理责任方",
                    "confirmed_as": "payment_ops_owner",
                    "status": "confirmed",
                    "evidence_anchor": {"source_section": "原始痛点: 周期扣款"},
                }
            ],
            user_stories=[
                {
                    "id": "US-012",
                    "role_ref": "R-payment-ops-owner",
                    "want": "作为支付交易处理责任方，我希望订阅账单扣款能够生成支付意图和支付尝试，并收敛出唯一支付结果。",
                    "benefit": "订阅续费不会停留在账单视角，支付交易状态可以明确驱动权益、入账、催缴和分账。",
                    "acceptance_function_ids": ["AF-017"],
                    "domain_refs": ["payment_transaction"],
                    "context_refs": [
                        "payment_attempt_authorization_context",
                        "payment_intent_context",
                        "payment_method_context",
                    ],
                    "aggregate_refs": [
                        "charge",
                        "payment_attempt",
                        "payment_intent",
                        "payment_method_authorization",
                    ],
                    "evidence_anchor": {"source_section": "US-012 / 订阅账单扣款"},
                }
            ],
            acceptance_functions=[
                {
                    "id": "AF-017",
                    "name": "支付意图和支付尝试收敛唯一结果",
                    "user_story_ids": ["US-012"],
                    "coverage_types": ["state_change"],
                    "context_refs": [
                        "payment_attempt_authorization_context",
                        "payment_intent_context",
                        "payment_method_context",
                    ],
                    "aggregate_refs": [
                        "charge",
                        "payment_attempt",
                        "payment_intent",
                        "payment_method_authorization",
                    ],
                    "then": "订阅账单发起扣款后，系统创建 payment_intent 和 payment_attempt；支付完成、失败或处理中状态最终收敛为一个可查询的最终结果。",
                    "source_acceptance": "AC-017",
                }
            ],
            domain_coverage=[
                {
                    "subdomain": "payment_transaction",
                    "coverage_type": "required_payment",
                    "contexts": [
                        "payment_attempt_authorization_context",
                        "payment_intent_context",
                        "payment_method_context",
                    ],
                    "aggregate_roots": [
                        "charge",
                        "payment_attempt",
                        "payment_intent",
                        "payment_method_authorization",
                    ],
                    "user_story_ids": ["US-012"],
                    "acceptance_function_ids": ["AF-017"],
                    "review_note": "升级为首版完整故事；首版覆盖支付意图、支付尝试、授权校验和扣款结果收敛。",
                }
            ],
            timestamp="2026-06-04T01:02:03+00:00",
        )

    def test_builds_package_with_mode_status_and_hard_gate_sections(self) -> None:
        package = self._package()

        self.assertEqual(package["mode"], "requirements_case")
        self.assertEqual(package["status"], "awaiting_confirmation")
        self.assertTrue(package["active"])
        self.assertEqual(package["domain"]["confirmed"], "account")
        self.assertEqual(package["roles"][0]["id"], "finance")
        self.assertEqual(package["user_stories"][0]["id"], "US-1")
        self.assertEqual(package["acceptance_functions"][0]["id"], "AF-1")

    def test_renders_required_sections_and_machine_data(self) -> None:
        markdown = render_requirements_case_markdown(self._package(), scan_root=self.tmpdir)

        for heading in [
            "## Case Source",
            "## Intent",
            "## Domain",
            "## Domain Coverage",
            "## Roles",
            "## User Stories",
            "## Acceptance Functions",
            "## Soft Evidence",
            "## Readiness / Next Action",
            "## Evidence Attachments",
            "## Proof Boundary",
            "## Machine Case Data",
        ]:
            self.assertIn(heading, markdown)
        self.assertIn('"mode": "requirements_case"', markdown)
        self.assertIn("domain: unclassified", markdown)
        self.assertIn("classification_needed: true", markdown)
        self.assertIn("ops_area: workflow-trace", markdown)
        self.assertIn("US-1", markdown)
        self.assertIn("AF-1", markdown)
        self.assertIn("account_balance", markdown)
        self.assertIn("coverage_type=primary", markdown)

    def test_renders_reviewable_json_for_payment_transaction_story(self) -> None:
        markdown = render_requirements_case_markdown(self._payment_transaction_package(), scan_root=self.tmpdir)

        self.assertIn("## Reviewable Coverage", markdown)
        self.assertIn('"review_judgment"', markdown)
        self.assertIn('"coverage_decision": "full_story"', markdown)
        self.assertIn('"taxonomy_refs"', markdown)
        self.assertIn('"id": "payment_transaction"', markdown)
        self.assertIn('"id": "payment_intent_context"', markdown)
        self.assertIn('"id": "payment_attempt"', markdown)
        self.assertIn('"meaning"', markdown)
        self.assertIn('"gate_closure"', markdown)
        self.assertIn('"domain_model_gate"', markdown)
        self.assertIn('"human_review_gate"', markdown)
        self.assertIn('"eval_plan"', markdown)
        self.assertIn('"red_cases"', markdown)
        self.assertIn('"green_cases"', markdown)

    def test_write_and_load_round_trip_preserves_stories_and_acceptance_functions(self) -> None:
        package = self._package()
        output_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"

        path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-29T01:02:03+00:00",
        )
        loaded = load_requirements_case_file(path)

        self.assertEqual(path.name, "2026-05-29-010203-account-reconciliation.md")
        self.assertEqual(loaded["user_stories"], package["user_stories"])
        self.assertEqual(loaded["acceptance_functions"], package["acceptance_functions"])
        self.assertEqual(loaded["domain_coverage"], package["domain_coverage"])

    def test_write_suffixes_existing_filename_without_overwriting(self) -> None:
        package = self._package()
        output_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"
        output_dir.mkdir(parents=True)
        existing = output_dir / "2026-05-29-010203-account-reconciliation.md"
        existing.write_text("existing case\n", encoding="utf-8")

        path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-29T01:02:03+00:00",
        )

        self.assertEqual(path.name, "2026-05-29-010203-account-reconciliation-2.md")
        self.assertEqual(existing.read_text(encoding="utf-8"), "existing case\n")

    def test_loader_raises_useful_error_when_machine_block_is_absent(self) -> None:
        path = self.tmpdir / "missing-block.md"
        path.write_text("# no machine data\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "requirements case data block not found"):
            load_requirements_case_file(path)


if __name__ == "__main__":
    unittest.main()
