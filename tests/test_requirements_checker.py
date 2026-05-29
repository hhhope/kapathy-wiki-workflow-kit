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

    def test_taxonomy_defines_initial_known_domains(self) -> None:
        taxonomy = self.load_taxonomy()

        domain_ids = {domain["id"] for domain in taxonomy["domains"]}
        domain_aliases = {
            alias
            for domain in taxonomy["domains"]
            for alias in domain.get("aliases", [])
        }

        self.assertSetEqual(domain_ids, {"account", "settlement", "clearing"})
        self.assertTrue({"账户", "结算", "清分"}.issubset(domain_aliases))

    def test_taxonomy_declares_independent_requirements_authority(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertEqual(taxonomy["authority"], "requirements-readiness")
        self.assertIn(
            "wiki/config/frontmatter-taxonomy.yaml",
            taxonomy["independent_from"],
        )

    def test_taxonomy_defines_roles_and_categories(self) -> None:
        taxonomy = self.load_taxonomy()

        roles = taxonomy["roles"]["vocabulary"]
        role_labels = {role["label"] for role in roles.values()}
        role_categories = {role["category"] for role in roles.values()}
        role_aliases = {
            alias
            for role in roles.values()
            for alias in role.get("aliases", [])
        }

        self.assertSetEqual(
            role_labels,
            {
                "retail operations",
                "financial operations",
                "product",
                "finance",
                "clearing",
                "compliance",
                "retail customer",
                "financial customer",
                "system actor",
                "engineering",
                "QA",
                "risk control",
            },
        )
        self.assertSetEqual(
            role_categories,
            {
                "business_actors",
                "operation_owners",
                "system_actors",
                "delivery_owners",
            },
        )
        self.assertSetEqual(
            set(taxonomy["roles"]["categories"]),
            {
                "business_actors",
                "operation_owners",
                "system_actors",
                "delivery_owners",
            },
        )
        self.assertTrue(
            {
                "零售运营",
                "金融运营",
                "产品",
                "财务",
                "清算",
                "合规",
                "零售客户",
                "金融客户",
            }.issubset(role_aliases)
        )

    def test_taxonomy_defines_hard_gate_fields(self) -> None:
        taxonomy = self.load_taxonomy()

        self.assertSetEqual(
            set(taxonomy["hard_gate_fields"]),
            {"domain", "roles", "user_stories", "acceptance_functions"},
        )

    def test_taxonomy_defines_soft_evidence_categories(self) -> None:
        taxonomy = self.load_taxonomy()

        soft_evidence = taxonomy["soft_evidence_categories"]

        self.assertSetEqual(
            set(soft_evidence),
            {
                "business_rules",
                "exception_scenarios",
                "api",
                "ddl",
                "adr",
                "test_plan",
                "release_plan",
            },
        )
        classifications = {
            category["classification"] for category in soft_evidence.values()
        }
        self.assertLessEqual(classifications, {"soft_warning", "design_evidence"})


if __name__ == "__main__":
    unittest.main()
