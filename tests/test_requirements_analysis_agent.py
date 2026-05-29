from __future__ import annotations

import unittest

from scripts.requirements_analysis_agent import (
    analyze_requirements_intake,
    classify_intent,
    resolve_domain,
)


class RequirementsAnalysisAgentTests(unittest.TestCase):
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
            ("账户体系需要支持冻结和解冻", "account"),
            ("结算域需要补充日切后的对账规则", "settlement"),
            ("清分流程需要输出渠道分润结果", "clearing"),
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
        self.assertEqual(result["domain"]["confirmed"], "account")
        self.assertNotIn(
            result["next_action"],
            {"implementation", "implement", "create_openspec_draft", "generate_draft"},
        )
        self.assertFalse(result["intent"]["draft_requested"])


if __name__ == "__main__":
    unittest.main()
