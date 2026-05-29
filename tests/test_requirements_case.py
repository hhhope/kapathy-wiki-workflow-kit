from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.requirements_case import (
    build_requirements_case_package,
    load_requirements_case_file,
    render_requirements_case_markdown,
    write_requirements_case_file,
)


class RequirementsCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="requirements-case-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _package(self) -> dict:
        return build_requirements_case_package(
            case_slug="account-reconciliation",
            status="awaiting_confirmation",
            current_intent={"intent": "new_requirement_intake"},
            domain={
                "status": "confirmed",
                "confirmed": "account",
                "candidates": [{"id": "account", "reason": "material names accounts"}],
            },
            roles=[
                {"id": "finance", "label": "finance"},
                {"id": "system_actor", "label": "system actor"},
            ],
            user_stories=[
                {
                    "id": "US-1",
                    "role": "finance",
                    "want": "review unreconciled account entries",
                    "benefit": "settlement exceptions are resolved before close",
                    "acceptance_function_ids": ["AF-1"],
                }
            ],
            acceptance_functions=[
                {
                    "id": "AF-1",
                    "name": "list_unreconciled_entries",
                    "user_story_ids": ["US-1"],
                    "given": "entries exist",
                    "when": "finance opens reconciliation",
                    "then": "unreconciled entries are visible",
                }
            ],
            soft_evidence={
                "business_rules": [{"summary": "late entries need review"}],
            },
            blockers=[],
            evidence_attachments={
                "material": ["inbox/account-reconciliation.md"],
                "diagnosis": ["wiki/ops/requirements-diagnosis.md"],
            },
            proof_boundary_notes=["This case does not validate API or DDL correctness."],
            timestamp="2026-05-29T01:02:03+00:00",
        )

    def test_builds_package_with_mode_status_and_hard_gate_sections(self) -> None:
        package = self._package()

        self.assertEqual(package["mode"], "requirements_case")
        self.assertEqual(package["status"], "awaiting_confirmation")
        self.assertTrue(package["active"])
        self.assertEqual(package["domain"]["confirmed"], "account")
        self.assertEqual(package["roles"][0]["id"], "finance")
        self.assertEqual(package["user_stories"][0]["id"], "US-1")
        self.assertEqual(package["acceptance_functions"][0]["id"], "AF-1")

    def test_renders_required_sections_and_machine_data(self) -> None:
        markdown = render_requirements_case_markdown(self._package(), scan_root=self.tmpdir)

        for heading in [
            "## Case Source",
            "## Intent",
            "## Domain",
            "## Roles",
            "## User Stories",
            "## Acceptance Functions",
            "## Soft Evidence",
            "## Readiness / Next Action",
            "## Evidence Attachments",
            "## Proof Boundary",
            "## Machine Case Data",
        ]:
            self.assertIn(heading, markdown)
        self.assertIn('"mode": "requirements_case"', markdown)
        self.assertIn("domain: unclassified", markdown)
        self.assertIn("classification_needed: true", markdown)
        self.assertIn("ops_area: workflow-trace", markdown)
        self.assertIn("US-1", markdown)
        self.assertIn("AF-1", markdown)

    def test_write_and_load_round_trip_preserves_stories_and_acceptance_functions(self) -> None:
        package = self._package()
        output_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"

        path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-29T01:02:03+00:00",
        )
        loaded = load_requirements_case_file(path)

        self.assertEqual(path.name, "2026-05-29-010203-account-reconciliation.md")
        self.assertEqual(loaded["user_stories"], package["user_stories"])
        self.assertEqual(loaded["acceptance_functions"], package["acceptance_functions"])

    def test_write_suffixes_existing_filename_without_overwriting(self) -> None:
        package = self._package()
        output_dir = self.tmpdir / "wiki" / "ops" / "requirements-cases"
        output_dir.mkdir(parents=True)
        existing = output_dir / "2026-05-29-010203-account-reconciliation.md"
        existing.write_text("existing case\n", encoding="utf-8")

        path = write_requirements_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-29T01:02:03+00:00",
        )

        self.assertEqual(path.name, "2026-05-29-010203-account-reconciliation-2.md")
        self.assertEqual(existing.read_text(encoding="utf-8"), "existing case\n")

    def test_loader_raises_useful_error_when_machine_block_is_absent(self) -> None:
        path = self.tmpdir / "missing-block.md"
        path.write_text("# no machine data\n", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "requirements case data block not found"):
            load_requirements_case_file(path)


if __name__ == "__main__":
    unittest.main()
