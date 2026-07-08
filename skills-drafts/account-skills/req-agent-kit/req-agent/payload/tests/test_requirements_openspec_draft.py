from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_case import build_requirements_case_package, write_requirements_case_file
from scripts.requirements_openspec_draft import create_openspec_draft_from_case


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsOpenSpecDraftTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-openspec-draft-test-"))
        requirements_config = self.tmpdir / "requirements" / "config"
        requirements_config.mkdir(parents=True)
        shutil.copyfile(TAXONOMY_PATH, requirements_config / "requirements-taxonomy.yaml")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _package(self) -> dict:
        package = build_requirements_case_package(
            case_slug="agent-service-subscription-payments",
            status="requirements_ready",
            domain={
                "status": "confirmed",
                "confirmed": "billing_revenue",
                "candidates": [{"id": "billing_revenue", "reason": "subscription billing"}],
            },
            roles=[
                {
                    "id": "R-provider",
                    "mention": "AI service provider",
                    "confirmed_as": "subscription_owner",
                    "status": "confirmed",
                    "evidence_anchor": {"source_section": "roles"},
                }
            ],
            user_stories=[
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
            acceptance_functions=[
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
            domain_coverage=[
                {
                    "subdomain": "billing_revenue",
                    "coverage_type": "primary",
                    "contexts": ["commercial_subscription_context"],
                    "aggregate_roots": ["commercial_subscription"],
                    "user_story_ids": ["US-1"],
                    "acceptance_function_ids": ["AF-1"],
                    "review_note": "subscription lifecycle",
                },
                {
                    "subdomain": "account_balance",
                    "coverage_type": "required_payment",
                    "contexts": ["balance_ledger_context"],
                    "aggregate_roots": ["ledger_entry"],
                    "user_story_ids": ["US-1"],
                    "acceptance_function_ids": ["AF-1"],
                    "review_note": "ledger evidence",
                },
            ],
            timestamp="2026-06-03T01:02:03+00:00",
        )
        package["domain_model"] = {
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
        }
        return package

    def _write_case(self, package: dict) -> Path:
        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "wiki" / "ops" / "requirements-cases",
            timestamp="2026-06-03T01:02:03+00:00",
        )

    def test_draft_includes_domain_coverage_summary(self) -> None:
        path = self._write_case(self._package())

        result = create_openspec_draft_from_case(path, "add-agent-subscription-payment", repo_root=self.tmpdir)

        self.assertEqual(result["status"], "draft_created")
        proposal = (self.tmpdir / "openspec" / "changes" / "add-agent-subscription-payment" / "proposal.md").read_text(encoding="utf-8")
        design = (self.tmpdir / "openspec" / "changes" / "add-agent-subscription-payment" / "design.md").read_text(encoding="utf-8")
        spec = (self.tmpdir / "openspec" / "changes" / "add-agent-subscription-payment" / "specs" / "requirements-analysis-agent" / "spec.md").read_text(encoding="utf-8")
        for text in (proposal, design, spec):
            self.assertIn("Domain Coverage", text)
            self.assertIn("billing_revenue", text)
            self.assertIn("commercial_subscription_context", text)
            self.assertIn("AF-1", text)

    def test_draft_rejects_domain_coverage_blocked_case(self) -> None:
        package = self._package()
        package.pop("domain_coverage")
        path = self._write_case(package)

        result = create_openspec_draft_from_case(path, "add-agent-subscription-payment", repo_root=self.tmpdir)

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["reason"], "requirements_not_ready")
        self.assertFalse(result["checker"]["domain_coverage_gate"]["passed"])


if __name__ == "__main__":
    unittest.main()
