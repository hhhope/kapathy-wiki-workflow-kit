from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_requirements_case import check_requirements_case_file
from scripts.requirements_case import (
    build_requirements_case_package,
    write_requirements_case_file,
)


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


class RequirementsCheckerGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-checker-test-"))
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
            "status": "awaiting_confirmation",
            "domain": {
                "status": "confirmed",
                "confirmed": "account",
                "candidates": [{"id": "account", "reason": "material names accounts"}],
            },
            "roles": [
                {
                    "id": "R-finance",
                    "mention": "finance",
                    "confirmed_as": "finance",
                    "status": "confirmed",
                    "category": "business_roles",
                    "evidence_anchor": {"source_section": "roles"},
                },
                {
                    "id": "R-system",
                    "mention": "reconciliation system",
                    "confirmed_as": "system_actor",
                    "status": "confirmed",
                    "category": "system_actors",
                    "evidence_anchor": {"source_section": "systems"},
                },
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
                    "source_acceptance": "AC-1",
                }
            ],
            "soft_evidence": {},
            "timestamp": "2026-05-29T01:02:03+00:00",
        }
        data.update(overrides)
        return build_requirements_case_package(**data)

    def _legacy_package(self, **overrides: object) -> dict:
        data = {
            "case_slug": "account-reconciliation",
            "status": "awaiting_confirmation",
            "domain": {
                "status": "confirmed",
                "confirmed": "account",
                "candidates": [{"id": "account", "reason": "material names accounts"}],
            },
            "roles": [
                {"id": "finance", "label": "finance"},
                {"id": "system_actor", "label": "system actor"},
            ],
            "user_stories": [
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
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
                }
            ],
            "soft_evidence": {},
            "timestamp": "2026-05-29T01:02:03+00:00",
        }
        data.update(overrides)
        return build_requirements_case_package(**data)

    def _write_case(self, package: dict, output_dir: Path | None = None) -> Path:
        return write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir or self.tmpdir / "cases",
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def _blocker_codes(self, report: dict) -> set[str]:
        return {str(blocker.get("code", "")) for blocker in report["blockers"]}

    def test_ready_case_passes_hard_gate(self) -> None:
        path = self._write_case(self._package())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertTrue(report["summary"]["hard_gate_passed"])
        self.assertEqual(report["blockers"], [])

    def test_missing_acceptance_mapping_fails_naming_user_story(self) -> None:
        package = self._package(
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("US-1", "\n".join(blocker["reason"] for blocker in report["blockers"]))

    def test_story_without_goal_value_or_declared_role_fails(self) -> None:
        package = self._legacy_package(
            roles=[{"id": "finance", "label": "finance"}],
            user_stories=[
                {
                    "id": "US-1",
                    "role": "product",
                    "acceptance_function_ids": ["AF-1"],
                }
            ],
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=False)

        reasons = "\n".join(blocker["reason"] for blocker in report["blockers"])
        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("role is not declared", reasons)
        self.assertIn("no want, goal, story, or summary", reasons)
        self.assertIn("no benefit, value, or so_that", reasons)

    def test_acceptance_without_reverse_mapping_or_observable_content_fails(self) -> None:
        package = self._package(
            acceptance_functions=[{"id": "AF-1"}],
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        reasons = "\n".join(blocker["reason"] for blocker in report["blockers"])
        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("acceptance function AF-1 has no user_story_ids", reasons)
        self.assertIn("acceptance function AF-1 has no observable", reasons)

    def test_candidate_unconfirmed_domain_fails(self) -> None:
        path = self._write_case(
            self._package(
                domain={
                    "status": "candidate_pending",
                    "confirmed": "lending",
                    "candidates": [{"id": "lending", "reason": "material mentions loans"}],
                }
            )
        )

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        reasons = "\n".join(blocker["reason"] for blocker in report["blockers"])
        self.assertIn("domain", reasons)
        self.assertIn("candidate_pending", reasons)

    def test_unknown_role_fails(self) -> None:
        path = self._write_case(
            self._legacy_package(roles=[{"id": "mystery_owner", "label": "mystery owner"}])
        )

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=False)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("mystery_owner", "\n".join(blocker["reason"] for blocker in report["blockers"]))

    def test_role_aliases_are_known_roles(self) -> None:
        path = self._write_case(
            self._legacy_package(roles=[{"id": "财务", "label": "财务"}, {"id": "清算", "label": "清算"}])
        )

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=False)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertEqual(report["blockers"], [])

    def test_soft_evidence_does_not_fail_readiness(self) -> None:
        path = self._write_case(
            self._package(
                soft_evidence={
                    "business_rules": [{"summary": "late entries need review"}],
                    "exception_scenarios": [{"summary": "manual reversal"}],
                    "api": [{"path": "/entries"}],
                    "ddl": [{"table": "account_entries"}],
                    "adr": [{"id": "ADR-1"}],
                    "test_plan": [{"summary": "unit and acceptance"}],
                    "release_plan": [{"summary": "pilot"}],
                }
            )
        )

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertEqual(report["blockers"], [])
        self.assertEqual(len(report["warnings"]), 2)
        self.assertEqual(len(report["evidence"]), 5)

    def test_wiki_stored_case_does_not_need_wiki_frontmatter_taxonomy(self) -> None:
        wiki_case_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"
        path = self._write_case(self._package(), output_dir=wiki_case_dir)
        self.assertFalse((self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").exists())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertEqual(report["summary"]["taxonomy_path"], "requirements/config/requirements-taxonomy.yaml")

    def test_strict_story_without_role_ref_fails(self) -> None:
        package = self._package(
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                    "evidence_anchor": {"source_functions": ["F-1"]},
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("story_role_ref_missing", self._blocker_codes(report))

    def test_strict_story_referencing_candidate_role_fails(self) -> None:
        package = self._package(
            roles=[
                {
                    "id": "R-finance",
                    "mention": "finance",
                    "confirmed_as": "finance",
                    "status": "candidate_pending",
                    "category": "business_roles",
                    "evidence_anchor": {"source_section": "roles"},
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("story_role_not_confirmed", self._blocker_codes(report))

    def test_acceptance_source_acceptance_counts_as_evidence_anchor(self) -> None:
        path = self._write_case(self._package())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertNotIn("acceptance_evidence_missing", self._blocker_codes(report))

    def test_acceptance_without_evidence_anchor_fails(self) -> None:
        package = self._package(
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("acceptance_evidence_missing", self._blocker_codes(report))

    def test_legacy_case_shape_remains_readable_in_compatibility_mode(self) -> None:
        path = self._write_case(self._legacy_package())

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=False)

        self.assertEqual(report["summary"]["status"], "requirements_ready")
        self.assertTrue(report["summary"]["hard_gate_passed"])
        self.assertTrue(report["summary"]["legacy_compatible"])
        self.assertEqual(report["blockers"], [])

    def test_strict_referenced_role_without_evidence_anchor_fails(self) -> None:
        package = self._package(
            roles=[
                {
                    "id": "R-finance",
                    "mention": "finance",
                    "confirmed_as": "finance",
                    "status": "confirmed",
                    "category": "business_roles",
                }
            ]
        )
        path = self._write_case(package)

        report = check_requirements_case_file(path, repo_root=self.tmpdir, strict=True)

        self.assertEqual(report["summary"]["status"], "blocked")
        self.assertIn("role_evidence_missing", self._blocker_codes(report))


if __name__ == "__main__":
    unittest.main()
