from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.check_requirements_ddd_taxonomy import validate_taxonomy_file


class RequirementsDDDTaxonomyTests(unittest.TestCase):
    def _write_taxonomy(self, data: dict) -> Path:
        tmpdir = Path(tempfile.mkdtemp(prefix="ddd-taxonomy-test-"))
        path = tmpdir / "requirements-taxonomy.yaml"
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        self.addCleanup(lambda: tmpdir.rmdir())
        self.addCleanup(lambda: path.unlink(missing_ok=True))
        return path

    def _minimal_valid_taxonomy(self) -> dict:
        return {
            "version": 2,
            "authority": "requirements-ddd-model",
            "business_ecosystems": {
                "payment_ecosystem": {
                    "subdomains": ["billing_revenue", "account_balance"],
                },
                "agent_service_ecosystem": {
                    "subdomains": ["agent_entitlement"],
                },
            },
            "subdomains": {
                "billing_revenue": {
                    "business_ecosystem": "payment_ecosystem",
                    "bounded_contexts": ["commercial_subscription_context"],
                },
                "account_balance": {
                    "business_ecosystem": "payment_ecosystem",
                    "bounded_contexts": ["balance_ledger_context"],
                },
                "agent_entitlement": {
                    "business_ecosystem": "agent_service_ecosystem",
                    "bounded_contexts": ["agent_entitlement_context"],
                },
            },
            "bounded_contexts": {
                "commercial_subscription_context": {
                    "subdomain": "billing_revenue",
                    "aggregate_roots": ["commercial_subscription"],
                    "fact_owners": ["subscription_owner"],
                },
                "balance_ledger_context": {
                    "subdomain": "account_balance",
                    "aggregate_roots": ["payment_account", "balance", "ledger_entry", "fund_state"],
                    "fact_owners": ["funds_account_owner", "ledger_owner", "balance_state_owner"],
                },
                "agent_entitlement_context": {
                    "subdomain": "agent_entitlement",
                    "aggregate_roots": ["agent_entitlement"],
                    "fact_owners": ["agent_entitlement_owner"],
                },
            },
            "role_archetypes": {
                "subscription_owner": {"required_by_contexts": ["commercial_subscription_context"]},
                "funds_account_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "ledger_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "balance_state_owner": {"required_by_contexts": ["balance_ledger_context"]},
                "agent_entitlement_owner": {"required_by_contexts": ["agent_entitlement_context"]},
            },
            "context_map": [
                {
                    "id": "commercial_subscription_to_agent_entitlement",
                    "from_context": "commercial_subscription_context",
                    "to_context": "agent_entitlement_context",
                    "handoff_type": "domain_event",
                    "artifact": "CommercialSubscriptionActivated",
                }
            ],
            "case_classification": {
                "examples": {
                    "agent_service_subscription_payments": {
                        "business_ecosystem": "payment_ecosystem",
                        "adjacent_ecosystems": ["agent_service_ecosystem"],
                        "primary_subdomain": "billing_revenue",
                        "primary_contexts": ["commercial_subscription_context"],
                        "required_contexts": ["balance_ledger_context"],
                        "required_agent_service_contexts": ["agent_entitlement_context"],
                    }
                }
            },
            "candidate_evolution": {
                "promotion_required_fields": [
                    "business_problem",
                    "ubiquitous_language",
                    "aggregate_roots",
                    "lifecycle",
                    "invariants",
                    "fact_owners",
                    "context_map",
                    "why_existing_contexts_do_not_fit",
                ]
            },
            "readiness_gate_model": {
                "domain_model_gate": {
                    "required_fields": ["business_ecosystem", "primary_subdomain", "primary_contexts"]
                }
            },
        }

    def test_valid_minimal_taxonomy_passes(self) -> None:
        path = self._write_taxonomy(self._minimal_valid_taxonomy())

        report = validate_taxonomy_file(path)

        self.assertEqual(report["errors"], [])

    def test_missing_root_section_fails(self) -> None:
        data = self._minimal_valid_taxonomy()
        data.pop("bounded_contexts")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("missing root section: bounded_contexts", report["errors"])

    def test_unknown_context_reference_fails(self) -> None:
        data = self._minimal_valid_taxonomy()
        data["subdomains"]["billing_revenue"]["bounded_contexts"].append("missing_context")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("subdomain billing_revenue references unknown context missing_context", report["errors"])

    def test_real_funds_trigger_requires_balance_ledger_owner_set(self) -> None:
        data = self._minimal_valid_taxonomy()
        data["role_archetypes"].pop("ledger_owner")
        path = self._write_taxonomy(data)

        report = validate_taxonomy_file(path)

        self.assertIn("real funds trigger requires role archetype ledger_owner", report["errors"])
