from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_case import (
    build_requirements_case_package,
    write_requirements_case_file,
)
from scripts.requirements_analysis_agent import (
    analyze_requirements_intake,
    build_role_instance,
    classify_intent,
    create_openspec_draft_from_case,
    resolve_domain,
)


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsAnalysisAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-agent-test-"))
        requirements_config = self.tmpdir / "requirements" / "config"
        requirements_config.mkdir(parents=True)
        shutil.copyfile(
            TAXONOMY_PATH,
            requirements_config / "requirements-taxonomy.yaml",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _package(self, **overrides: object) -> dict:
        data = {
            "case_slug": "account-reconciliation",
            "status": "requirements_ready",
            "domain": {
                "status": "confirmed",
                "confirmed": "account_balance",
                "candidates": [{"id": "account_balance", "reason": "material names accounts"}],
            },
            "roles": [
                build_role_instance(
                    role_id="R-finance",
                    mention="finance",
                    confirmed_as="ledger_owner",
                    category="business_roles",
                    source_section="roles",
                ),
                build_role_instance(
                    role_id="R-system",
                    mention="reconciliation system",
                    confirmed_as="reconciliation_owner",
                    category="system_actors",
                    source_section="systems",
                ),
            ],
            "user_stories": [
                {
                    "id": "US-1",
                    "role_ref": "R-finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-1"]},
                }
            ],
            "acceptance_functions": [
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                    "source_acceptance": "AC-001",
                }
            ],
            "timestamp": "2026-05-29T01:02:03+00:00",
        }
        data.update(overrides)
        package = build_requirements_case_package(**data)
        package["domain_model"] = {
            "status": "confirmed",
            "business_ecosystems": ["payment_ecosystem"],
            "subdomains": ["account_balance", "financial_operations"],
            "bounded_contexts": ["balance_ledger_context", "reconciliation_context"],
            "aggregate_roots": ["payment_account", "ledger_entry", "reconciliation_record"],
            "fact_owners": ["ledger_owner", "reconciliation_owner"],
            "role_obligations": ["ledger_owner", "reconciliation_owner"],
            "context_handoffs": [
                {
                    "from_context": "balance_ledger_context",
                    "to_context": "reconciliation_context",
                    "type": "evidence",
                    "name": "LedgerEntryPosted",
                }
            ],
        }
        return package

    def _write_case(self, package: dict) -> Path:
        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def test_classify_intent_treats_raw_requirement_material_as_intake_not_draft(self) -> None:
        result = classify_intent(
            """
            账户调账需求：
            作为财务，我希望能按账户查询未平账流水，以便在日终前完成差异处理。
            验收：给定存在未平账记录，进入调账页面时，应展示记录和差异原因。
            """
        )

        self.assertEqual(result["intent"], "new_requirement_intake")
        self.assertFalse(result["draft_requested"])
        self.assertNotEqual(result["next_action"], "create_openspec_draft")

    def test_classify_intent_detects_requirements_ready_check_requests(self) -> None:
        for material in [
            "这个需求是否可以进入开发？",
            "Please check whether this requirement is ready to proceed.",
            "看一下这份需求是否ready",
            "请跑一下需求门禁，校验这份需求",
        ]:
            with self.subTest(material=material):
                result = classify_intent(material)

                self.assertEqual(result["intent"], "check_requirements_ready")
                self.assertFalse(result["draft_requested"])

    def test_classify_intent_detects_explicit_openspec_draft_request(self) -> None:
        result = classify_intent("请基于这份已确认需求创建 OpenSpec draft。")

        self.assertEqual(result["intent"], "create_openspec_draft")
        self.assertTrue(result["draft_requested"])
        self.assertEqual(result["next_action"], "create_openspec_draft")

    def test_resolve_domain_matches_known_taxonomy_aliases_including_chinese(self) -> None:
        cases = [
            ("账户体系需要支持冻结和解冻", "account_balance"),
            ("结算域需要补充日切后的对账规则", "funds_movement_settlement"),
            ("清分流程需要输出渠道分润结果", "financial_operations"),
        ]

        for material, expected_domain in cases:
            with self.subTest(expected_domain=expected_domain):
                result = resolve_domain(material)

                self.assertEqual(result["status"], "confirmed")
                self.assertEqual(result["confirmed"], expected_domain)
                self.assertFalse(result["requires_user_confirmation"])

    def test_resolve_domain_keeps_unknown_wallet_domain_as_candidate_pending(self) -> None:
        result = resolve_domain(
            "embedded wallet payment requires balance reservation before checkout capture"
        )

        self.assertEqual(result["status"], "candidate_pending")
        self.assertEqual(result["confirmed"], "")
        self.assertTrue(result["requires_user_confirmation"])
        candidate_ids = {candidate["id"] for candidate in result["candidates"]}
        self.assertTrue({"embedded_wallet", "wallet_payment"} & candidate_ids)
        self.assertFalse({"account", "settlement", "clearing"} & candidate_ids)

    def test_wallet_material_with_account_word_is_not_forced_to_seeded_domain(self) -> None:
        result = resolve_domain(
            "embedded wallet account balance reservation before wallet payment capture"
        )

        self.assertEqual(result["status"], "candidate_pending")
        self.assertEqual(result["confirmed"], "")
        candidate_ids = {candidate["id"] for candidate in result["candidates"]}
        self.assertTrue({"embedded_wallet", "wallet_payment"} & candidate_ids)
        self.assertFalse({"account", "settlement", "clearing"} & candidate_ids)

    def test_analyze_requirements_intake_combines_intent_and_domain_without_generation(self) -> None:
        result = analyze_requirements_intake(
            """
            账户调账需求：
            作为财务，我希望能按账户查询未平账流水，以便在日终前完成差异处理。
            验收：给定存在未平账记录，进入调账页面时，应展示记录和差异原因。
            """
        )

        self.assertEqual(result["intent"]["intent"], "new_requirement_intake")
        self.assertEqual(result["domain"]["status"], "confirmed")
        self.assertEqual(result["domain"]["confirmed"], "account_balance")
        self.assertIn("account_balance", result["domain_model"]["subdomains"])
        self.assertNotIn(
            result["next_action"],
            {"implementation", "implement", "create_openspec_draft", "generate_draft"},
        )
        self.assertFalse(result["intent"]["draft_requested"])

    def test_create_openspec_draft_blocks_unready_case_without_creating_files(self) -> None:
        case_file = self._write_case(
            self._package(
                status="awaiting_confirmation",
                user_stories=[
                    {
                        "id": "US-1",
                        "role": "finance",
                        "want": "review unreconciled account entries",
                        "benefit": "settlement exceptions are resolved before close",
                    }
                ],
            )
        )

        result = create_openspec_draft_from_case(
            case_file,
            "draft-blocked-case",
            repo_root=self.tmpdir,
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "requirements_not_ready")
        self.assertFalse((self.tmpdir / "openspec" / "changes" / "draft-blocked-case").exists())
        blocker_text = "\n".join(blocker["reason"] for blocker in result["blockers"])
        self.assertIn("US-1", blocker_text)
        self.assertIn("acceptance_function_ids", blocker_text)

    def test_create_openspec_draft_blocks_candidate_role_reference(self) -> None:
        case_file = self._write_case(
            self._package(
                roles=[
                    build_role_instance(
                        role_id="R-ops",
                        mention="finance ops",
                        confirmed_as="financial_operations",
                        status="candidate_pending",
                        category="business_roles",
                        source_section="roles",
                    )
                ],
                user_stories=[
                    {
                        "id": "US-1",
                        "role_ref": "R-ops",
                        "want": "review unreconciled account entries",
                        "benefit": "settlement exceptions are resolved before close",
                        "acceptance_function_ids": ["AF-1"],
                        "evidence_anchor": {"source_functions": ["F-1"]},
                    }
                ],
            )
        )

        result = create_openspec_draft_from_case(
            case_file,
            "draft-candidate-role-reference",
            repo_root=self.tmpdir,
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "requirements_not_ready")
        self.assertFalse((self.tmpdir / "openspec" / "changes" / "draft-candidate-role-reference").exists())
        blocker_codes = {blocker["code"] for blocker in result["blockers"]}
        self.assertIn("story_role_not_confirmed", blocker_codes)

    def test_create_openspec_draft_writes_traceable_files_for_ready_case(self) -> None:
        case_file = self._write_case(self._package())

        result = create_openspec_draft_from_case(
            case_file,
            "draft-account-reconciliation",
            repo_root=self.tmpdir,
        )

        change_dir = self.tmpdir / "openspec" / "changes" / "draft-account-reconciliation"
        self.assertEqual(result["status"], "draft_created")
        self.assertTrue(result["requires_user_review"])
        expected_files = [
            change_dir / "proposal.md",
            change_dir / "design.md",
            change_dir / "tasks.md",
            change_dir / "specs" / "requirements-analysis-agent" / "spec.md",
        ]
        for path in expected_files:
            with self.subTest(path=path):
                self.assertTrue(path.exists())
        combined = "\n".join(path.read_text(encoding="utf-8") for path in expected_files)
        self.assertIn("US-1", combined)
        self.assertIn("AF-1", combined)
        self.assertIn("review unreconciled account entries", combined)
        self.assertIn("Implementation requires user review", combined)

    def test_create_openspec_draft_blocks_existing_change_id_without_overwrite(self) -> None:
        case_file = self._write_case(self._package())
        change_dir = self.tmpdir / "openspec" / "changes" / "draft-existing"
        change_dir.mkdir(parents=True)
        existing_proposal = change_dir / "proposal.md"
        existing_proposal.write_text("existing proposal\n", encoding="utf-8")

        result = create_openspec_draft_from_case(
            case_file,
            "draft-existing",
            repo_root=self.tmpdir,
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "change_id_collision")
        self.assertEqual(existing_proposal.read_text(encoding="utf-8"), "existing proposal\n")
        blocker_text = "\n".join(blocker["reason"] for blocker in result["blockers"])
        self.assertIn("draft-existing", blocker_text)
        self.assertIn("different change id", blocker_text)

    def test_create_openspec_draft_blocks_invalid_capability_path(self) -> None:
        case_file = self._write_case(self._package())

        result = create_openspec_draft_from_case(
            case_file,
            "draft-invalid-capability",
            repo_root=self.tmpdir,
            capability="../outside",
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "invalid_capability")
        self.assertFalse((self.tmpdir / "openspec" / "changes" / "draft-invalid-capability").exists())


if __name__ == "__main__":
    unittest.main()
