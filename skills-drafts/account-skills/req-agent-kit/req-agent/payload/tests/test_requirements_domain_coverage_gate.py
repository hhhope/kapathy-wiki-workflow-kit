from __future__ import annotations

import copy
import unittest
from pathlib import Path

import yaml

from scripts.check_requirements_case import check_requirements_case


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsDomainCoverageGateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.taxonomy = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))

    def _case(self) -> dict:
        return {
            "case_slug": "agent-service-subscription-payments",
            "status": "requirements_ready",
            "domain": {
                "status": "confirmed",
                "confirmed": "billing_revenue",
                "candidates": [{"id": "billing_revenue", "reason": "subscription billing"}],
            },
            "domain_model": {
                "status": "confirmed",
                "business_ecosystems": ["payment_ecosystem", "agent_service_ecosystem"],
                "subdomains": ["billing_revenue", "account_balance"],
                "bounded_contexts": ["commercial_subscription_context", "balance_ledger_context"],
                "aggregate_roots": ["commercial_subscription", "ledger_entry"],
                "fact_owners": ["subscription_owner", "ledger_owner"],
                "role_obligations": ["subscription_owner", "ledger_owner"],
                "context_handoffs": [
                    {
                        "from_context": "commercial_subscription_context",
                        "to_context": "balance_ledger_context",
                        "type": "domain_event",
                        "name": "CommercialSubscriptionRenewed",
                    }
                ],
            },
            "domain_coverage": [
                {
                    "subdomain": "billing_revenue",
                    "coverage_type": "primary",
                    "contexts": ["commercial_subscription_context"],
                    "aggregate_roots": ["commercial_subscription"],
                    "user_story_ids": ["US-1"],
                    "acceptance_function_ids": ["AF-1"],
                    "review_note": "first-release subscription lifecycle",
                },
                {
                    "subdomain": "account_balance",
                    "coverage_type": "required_payment",
                    "contexts": ["balance_ledger_context"],
                    "aggregate_roots": ["ledger_entry"],
                    "user_story_ids": ["US-1"],
                    "acceptance_function_ids": ["AF-1"],
                    "review_note": "renewal posts ledger evidence",
                },
            ],
            "roles": [
                {
                    "id": "R-provider",
                    "mention": "AI service provider",
                    "confirmed_as": "subscription_owner",
                    "status": "confirmed",
                    "evidence_anchor": {"source_section": "roles"},
                }
            ],
            "user_stories": [
                {
                    "id": "US-1",
                    "role_ref": "R-provider",
                    "want": "renew a commercial Agent subscription and post ledger facts",
                    "benefit": "service access and fund evidence stay consistent",
                    "acceptance_function_ids": ["AF-1"],
                    "domain_refs": ["billing_revenue", "account_balance"],
                    "context_refs": ["commercial_subscription_context", "balance_ledger_context"],
                    "aggregate_refs": ["commercial_subscription", "ledger_entry"],
                    "evidence_anchor": {"source_functions": ["subscription renewal"]},
                }
            ],
            "acceptance_functions": [
                {
                    "id": "AF-1",
                    "name": "renew_subscription_and_post_ledger_entry",
                    "user_story_ids": ["US-1"],
                    "coverage_types": ["state_change", "handoff", "evidence"],
                    "context_refs": ["commercial_subscription_context", "balance_ledger_context"],
                    "aggregate_refs": ["commercial_subscription", "ledger_entry"],
                    "given": "a subscription is due",
                    "when": "payment succeeds",
                    "then": "subscription renews and a ledger entry is posted",
                    "source_acceptance": "AC-1",
                }
            ],
        }

    def _report(self, case_data: dict) -> dict:
        return check_requirements_case(case_data, self.taxonomy, strict=True)

    def _codes(self, report: dict) -> set[str]:
        return {str(blocker.get("code", "")) for blocker in report["blockers"]}

    def test_complete_domain_coverage_passes(self) -> None:
        report = self._report(self._case())

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertTrue(report["domain_coverage_gate"]["passed"])
        self.assertEqual(report["blockers"], [])

    def test_domain_model_without_coverage_blocks_readiness(self) -> None:
        case_data = self._case()
        case_data.pop("domain_coverage")

        report = self._report(case_data)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertFalse(report["domain_coverage_gate"]["passed"])
        self.assertIn("domain_coverage_missing", self._codes(report))

    def test_missing_story_lifecycle_refs_block_readiness(self) -> None:
        case_data = self._case()
        story = case_data["user_stories"][0]
        story.pop("domain_refs")
        story.pop("context_refs")
        story.pop("aggregate_refs")

        report = self._report(case_data)

        codes = self._codes(report)
        self.assertFalse(report["domain_coverage_gate"]["passed"])
        self.assertIn("domain_coverage_story_domain_refs_missing", codes)
        self.assertIn("domain_coverage_story_context_refs_missing", codes)
        self.assertIn("domain_coverage_story_aggregate_refs_missing", codes)

    def test_acceptance_coverage_types_block_missing_observable_surfaces(self) -> None:
        case_data = self._case()
        function = case_data["acceptance_functions"][0]
        function["coverage_types"] = []

        report = self._report(case_data)

        codes = self._codes(report)
        self.assertFalse(report["domain_coverage_gate"]["passed"])
        self.assertIn("domain_coverage_acceptance_types_missing", codes)
        self.assertIn("domain_coverage_state_change_missing", codes)
        self.assertIn("domain_coverage_handoff_missing", codes)
        self.assertIn("domain_coverage_evidence_missing", codes)

    def test_missing_failure_path_acceptance_blocks_when_revenue_recovery_is_in_scope(self) -> None:
        case_data = copy.deepcopy(self._case())
        case_data["domain_model"]["bounded_contexts"].append("revenue_recovery_context")
        case_data["domain_model"]["aggregate_roots"].append("retry_schedule")
        case_data["domain_coverage"][0]["contexts"].append("revenue_recovery_context")
        case_data["domain_coverage"][0]["aggregate_roots"].append("retry_schedule")
        case_data["user_stories"][0]["context_refs"].append("revenue_recovery_context")
        case_data["user_stories"][0]["aggregate_refs"].append("retry_schedule")
        case_data["acceptance_functions"][0]["context_refs"].append("revenue_recovery_context")
        case_data["acceptance_functions"][0]["aggregate_refs"].append("retry_schedule")

        report = self._report(case_data)

        self.assertFalse(report["domain_coverage_gate"]["passed"])
        self.assertIn("domain_coverage_failure_path_missing", self._codes(report))


if __name__ == "__main__":
    unittest.main()
