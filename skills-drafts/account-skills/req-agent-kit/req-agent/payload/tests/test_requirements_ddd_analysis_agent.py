from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_analysis_agent import analyze_requirements_intake


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


AGENT_SUBSCRIPTION_PAYMENT_MATERIAL = """
AI 服务商希望向消费者提供订阅制 Agent 服务。平台需要提供支付、订阅、
自动续费、宽限期、催缴、用量计费、席位计费和分账结算能力。
本期处理真实资金，支付成功后需要入账、生成账本流水，并影响 Agent 服务访问权限。
"""


class RequirementsDddAnalysisAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-ddd-analysis-test-"))
        requirements_config = self.tmpdir / "requirements" / "config"
        requirements_config.mkdir(parents=True)
        shutil.copyfile(TAXONOMY_PATH, requirements_config / "requirements-taxonomy.yaml")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_agent_subscription_payment_analysis_outputs_ddd_domain_model(self) -> None:
        result = analyze_requirements_intake(AGENT_SUBSCRIPTION_PAYMENT_MATERIAL, repo_root=self.tmpdir)

        domain_model = result["domain_model"]

        self.assertEqual(domain_model["status"], "confirmed")
        self.assertIn("payment_ecosystem", domain_model["business_ecosystems"])
        self.assertIn("agent_service_ecosystem", domain_model["business_ecosystems"])
        self.assertIn("billing_revenue", domain_model["subdomains"])
        self.assertIn("account_balance", domain_model["subdomains"])
        self.assertIn("commercial_subscription_context", domain_model["bounded_contexts"])
        self.assertIn("balance_ledger_context", domain_model["bounded_contexts"])
        self.assertIn("agent_entitlement_context", domain_model["bounded_contexts"])
        self.assertIn("commercial_subscription", domain_model["aggregate_roots"])
        self.assertIn("ledger_entry", domain_model["aggregate_roots"])
        self.assertIn("subscription_owner", domain_model["role_obligations"])
        self.assertIn("ledger_owner", domain_model["role_obligations"])
        self.assertIn("agent_entitlement_owner", domain_model["role_obligations"])
        self.assertTrue(domain_model["context_handoffs"])

    def test_analysis_keeps_real_actors_separate_from_role_obligations(self) -> None:
        result = analyze_requirements_intake(AGENT_SUBSCRIPTION_PAYMENT_MATERIAL, repo_root=self.tmpdir)

        actors = result["actors"]
        actor_ids = {actor["id"] for actor in actors}
        obligation_ids = set(result["domain_model"]["role_obligations"])

        self.assertIn("ai_service_provider", actor_ids)
        self.assertIn("platform", actor_ids)
        self.assertNotIn("subscription_owner", actor_ids)
        self.assertNotIn("ledger_owner", actor_ids)
        self.assertIn("subscription_owner", obligation_ids)
        self.assertIn("ledger_owner", obligation_ids)

    def test_unknown_terms_remain_candidates_in_ddd_analysis(self) -> None:
        result = analyze_requirements_intake(
            "Agent 服务需要引入 carbon credit wallet 来做绿色积分抵扣。",
            repo_root=self.tmpdir,
        )

        candidate_ids = {candidate["id"] for candidate in result["domain_model"]["candidates"]}

        self.assertEqual(result["domain_model"]["status"], "candidate_pending")
        self.assertIn("carbon_credit_wallet", candidate_ids)
        self.assertNotIn("carbon_credit_wallet", result["domain_model"]["subdomains"])


if __name__ == "__main__":
    unittest.main()
