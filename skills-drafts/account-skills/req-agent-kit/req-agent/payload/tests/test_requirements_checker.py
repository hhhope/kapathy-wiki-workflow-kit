from __future__ import annotations

import unittest
from pathlib import Path

import yaml


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsTaxonomyTests(unittest.TestCase):
    def load_taxonomy(self) -> dict:
        with TAXONOMY_PATH.open(encoding="utf-8") as handle:
            taxonomy = yaml.safe_load(handle)
        self.assertIsInstance(taxonomy, dict)
        return taxonomy

    def test_taxonomy_declares_ddd_authority(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertEqual(taxonomy["version"], 2)
        self.assertEqual(taxonomy["authority"], "requirements-ddd-model")
        self.assertIn("wiki/config/frontmatter-taxonomy.yaml", taxonomy["independent_from"])

    def test_taxonomy_exposes_ddd_model_roots(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertSetEqual(
            {
                "business_ecosystems",
                "subdomains",
                "bounded_contexts",
                "role_archetypes",
                "context_map",
                "case_classification",
                "candidate_evolution",
                "readiness_gate_model",
            },
            {
                key
                for key in taxonomy
                if key
                in {
                    "business_ecosystems",
                    "subdomains",
                    "bounded_contexts",
                    "role_archetypes",
                    "context_map",
                    "case_classification",
                    "candidate_evolution",
                    "readiness_gate_model",
                }
            },
        )

    def test_payment_and_agent_service_ecosystems_are_defined(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertSetEqual(
            set(taxonomy["business_ecosystems"]),
            {"payment_ecosystem", "agent_service_ecosystem"},
        )
        self.assertIn("billing_revenue", taxonomy["business_ecosystems"]["payment_ecosystem"]["subdomains"])
        self.assertIn("agent_entitlement", taxonomy["business_ecosystems"]["agent_service_ecosystem"]["subdomains"])

    def test_role_archetypes_include_funds_and_agent_obligations(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertTrue(
            {
                "subscription_owner",
                "ledger_owner",
                "funds_account_owner",
                "agent_entitlement_owner",
                "access_policy_owner",
            }.issubset(taxonomy["role_archetypes"])
        )

    def test_readiness_gate_model_splits_domain_and_delivery_gates(self) -> None:
        taxonomy = self.load_taxonomy()
        readiness = taxonomy["readiness_gate_model"]

        self.assertIn("domain_model_gate", readiness)
        self.assertIn("requirement_delivery_gate", readiness)
        self.assertIn("bounded_contexts", readiness["domain_model_gate"]["required_fields"])
        self.assertIn(
            "acceptance_functions_for_handoffs",
            readiness["requirement_delivery_gate"]["required_fields"],
        )


if __name__ == "__main__":
    unittest.main()
