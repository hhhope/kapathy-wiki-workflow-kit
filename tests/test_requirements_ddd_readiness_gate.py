from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_requirements_case import check_requirements_case_file
from scripts.requirements_case import build_requirements_case_package, write_requirements_case_file


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsDddReadinessGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-ddd-gate-test-"))
        requirements_config = self.tmpdir / "requirements" / "config"
        requirements_config.mkdir(parents=True)
        shutil.copyfile(TAXONOMY_PATH, requirements_config / "requirements-taxonomy.yaml")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _write_case(self, package: dict) -> Path:
        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "cases",
            timestamp="2026-06-03T01:02:03+00:00",
        )

    def _ddd_package(self, **domain_model_overrides: object) -> dict:
        package = build_requirements_case_package(
            case_slug="agent-service-subscription-payments",
            status="awaiting_confirmation",
            domain={
                "status": "confirmed",
                "confirmed": "billing_revenue",
                "candidates": [{"id": "billing_revenue", "reason": "commercial subscription billing"}],
            },
            roles=[
                {
                    "id": "R-subscription-owner",
                    "mention": "subscription owner",
                    "confirmed_as": "subscription_owner",
                    "status": "confirmed",
                    "evidence_anchor": {"source_section": "roles"},
                },
                {
                    "id": "R-ledger-owner",
                    "mention": "ledger owner",
                    "confirmed_as": "ledger_owner",
                    "status": "confirmed",
                    "evidence_anchor": {"source_section": "funds"},
                },
            ],
            user_stories=[
                {
                    "id": "US-1",
                    "role_ref": "R-subscription-owner",
                    "want": "manage commercial subscription renewal",
                    "benefit": "paid Agent service access follows billing state",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-1"]},
                }
            ],
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "renew_subscription_and_post_ledger_entry",
                    "user_story_ids": ["US-1"],
                    "given": "a subscription is due",
                    "when": "payment succeeds",
                    "then": "subscription renews and ledger entry is posted",
                    "source_acceptance": "AC-1",
                }
            ],
            soft_evidence={},
            timestamp="2026-06-03T01:02:03+00:00",
        )
        domain_model = {
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
            "non_domain_terms": ["subscription is split by context"],
            "open_questions": ["confirm whether payout is in first release"],
        }
        domain_model.update(domain_model_overrides)
        package["domain_model"] = domain_model
        return package

    def _blocker_codes(self, report: dict) -> set[str]:
        return {str(blocker.get("code", "")) for blocker in report["blockers"]}

    def test_complete_ddd_case_passes_domain_and_delivery_gates(self) -> None:
        path = self._write_case(self._ddd_package())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertTrue(report["summary"]["hard_gate_passed"])
        self.assertTrue(report.get("domain_model_gate", {}).get("passed"))
        self.assertTrue(report.get("requirement_delivery_gate", {}).get("passed"))
        self.assertFalse(report["summary"]["legacy_compatible"])
        self.assertEqual(report["blockers"], [])

    def test_missing_bounded_context_blocks_domain_model_gate(self) -> None:
        path = self._write_case(self._ddd_package(bounded_contexts=[]))

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertFalse(report.get("domain_model_gate", {}).get("passed", True))
        self.assertTrue(report.get("requirement_delivery_gate", {}).get("passed"))
        self.assertIn("domain_model_contexts_missing", self._blocker_codes(report))

    def test_unknown_role_obligation_blocks_domain_model_gate(self) -> None:
        path = self._write_case(self._ddd_package(role_obligations=["subscription_owner", "mystery_owner"]))

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertFalse(report.get("domain_model_gate", {}).get("passed", True))
        self.assertIn("domain_model_role_obligation_unknown", self._blocker_codes(report))


if __name__ == "__main__":
    unittest.main()
