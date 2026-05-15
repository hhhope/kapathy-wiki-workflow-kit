import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_review_decisions import write_review_decision_record
from scripts.wiki_medical_case import (
    build_medical_case_package,
    load_medical_case_file,
    render_medical_case_markdown,
    write_medical_case_file,
)


class WikiMedicalCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-medical-case-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _decision_package(self) -> dict:
        return {
            "generated_at": "2026-05-15T01:02:03+00:00",
            "source_record": "wiki/ops/wiki-doctor-runs/diagnosis.md",
            "source_adjudication_summary": {"full_detail_count": 3},
            "summary": {
                "source_detail_count": 3,
                "treatment_candidates_count": 1,
                "surgery_candidates_count": 1,
                "openspec_required_count": 1,
            },
            "accepted_candidates": [],
            "rejected_candidates": [],
            "deferred_items": [],
            "treatment_candidates": [
                {
                    "detail_ref": "detail-treatment",
                    "path": "wiki/ops/treatment.md",
                    "risk_flags": [],
                    "reason": "safe frontmatter",
                }
            ],
            "surgery_candidates": [
                {
                    "detail_ref": "detail-confirmed-surgery",
                    "path": "wiki/ops/relation.md",
                    "risk_flags": ["relation_weak_evidence"],
                    "reason": "weak relation",
                }
            ],
            "openspec_required": [
                {
                    "detail_ref": "detail-governance",
                    "path": "wiki/ops/governance.md",
                    "risk_flags": ["openspec_required", "drift_risk"],
                    "reason": "governance drift",
                }
            ],
        }

    def test_builds_case_package_with_required_sections_and_attachments(self) -> None:
        package = build_medical_case_package(
            self._decision_package(),
            case_slug="frontmatter-relation-governance",
            confirm_record="wiki/ops/wiki-review-decisions/confirm.md",
        )

        self.assertEqual(package["case_slug"], "frontmatter-relation-governance")
        self.assertEqual(package["mode"], "wiki_medical_case")
        self.assertEqual(
            package["evidence_attachments"]["doctor"],
            ["wiki/ops/wiki-doctor-runs/diagnosis.md"],
        )
        self.assertEqual(
            package["evidence_attachments"]["confirm"],
            ["wiki/ops/wiki-review-decisions/confirm.md"],
        )
        self.assertEqual(
            package["confirmed_decisions"]["surgery_candidates"][0]["detail_ref"],
            "detail-confirmed-surgery",
        )
        self.assertEqual(package["treatment"]["status"], "pending")
        self.assertEqual(package["surgery_plan"]["status"], "pending")
        self.assertEqual(package["recovery"]["status"], "pending")
        self.assertIn("canonical case file", " ".join(package["proof_boundary_notes"]))

    def test_renders_case_markdown_with_machine_readable_case_data(self) -> None:
        package = build_medical_case_package(self._decision_package())

        markdown = render_medical_case_markdown(package, scan_root=self.tmpdir)

        for heading in [
            "# wiki-medical-case",
            "## Case Source",
            "## Diagnosis",
            "## Confirmed Decisions",
            "## Treatment",
            "## Surgery Plan",
            "## Recovery",
            "## Archive / Next Action",
            "## Evidence Attachments",
            "## Proof Boundary",
            "## Machine Case Data",
        ]:
            self.assertIn(heading, markdown)
        self.assertIn("detail-confirmed-surgery", markdown)
        self.assertIn('"mode": "wiki_medical_case"', markdown)

    def test_writes_and_loads_case_file_without_losing_confirmed_decisions(self) -> None:
        package = build_medical_case_package(
            self._decision_package(),
            case_slug="frontmatter-relation-governance",
        )
        output_dir = self.tmpdir / "wiki" / "ops" / "wiki-medical-cases"

        path = write_medical_case_file(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )
        loaded = load_medical_case_file(path)

        self.assertEqual(path.name, "2026-05-15-010203-frontmatter-relation-governance.md")
        self.assertEqual(
            loaded["confirmed_decisions"]["surgery_candidates"][0]["detail_ref"],
            "detail-confirmed-surgery",
        )
        self.assertEqual(loaded["case_slug"], "frontmatter-relation-governance")

    def test_cli_writes_case_file_by_default(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        (self.tmpdir / "wiki" / "config").mkdir(parents=True)
        (self.tmpdir / "wiki" / "ops").mkdir(parents=True)
        (self.tmpdir / "wiki" / "config" / "frontmatter-taxonomy.yaml").write_text(
            """version: 1
fields:
  domain:
    known:
      - wiki
      - unclassified
  ops_area:
    allowed:
      - wiki-runtime
strict_gate:
  enabled: true
  rule_sets: {}
""",
            encoding="utf-8",
        )
        (self.tmpdir / "wiki" / "ops" / "relation-note.md").write_text(
            "# Relation Note\n\nThis wiki runtime note has weak relation evidence.\n",
            encoding="utf-8",
        )
        record_dir = self.tmpdir / "case-records"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_case.py",
                "--root",
                str(self.tmpdir),
                "--case-slug",
                "test-case",
                "--case-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertIn("medical_case_path", payload)
        case_path = Path(payload["medical_case_path"])
        self.assertTrue(case_path.exists())
        self.assertEqual(case_path.parent, record_dir.resolve())
        self.assertIn("## Confirmed Decisions", case_path.read_text(encoding="utf-8"))

    def test_cli_builds_case_from_confirm_record_without_rescanning_existing_case_files(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        decision_package = self._decision_package()
        confirm_path = write_review_decision_record(
            decision_package,
            self.tmpdir,
            output_dir=self.tmpdir / "wiki" / "ops" / "wiki-review-decisions",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        existing_case_dir = self.tmpdir / "wiki" / "ops" / "wiki-medical-cases"
        existing_case_dir.mkdir(parents=True)
        (existing_case_dir / "2026-05-15-010000-old-case.md").write_text(
            "# old case\n\nThis old case must not be scanned into the new case decisions.\n",
            encoding="utf-8",
        )

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_case.py",
                "--root",
                str(self.tmpdir),
                "--confirm-record",
                str(confirm_path),
                "--case-record-dir",
                str(existing_case_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        loaded = load_medical_case_file(payload["medical_case_path"])

        self.assertEqual(loaded["case_source"]["source_decision_summary"]["source_detail_count"], 3)
        self.assertEqual(
            [item["detail_ref"] for item in loaded["confirmed_decisions"]["accepted_candidates"]],
            [],
        )
        self.assertNotIn(
            "old-case",
            json.dumps(loaded["confirmed_decisions"], ensure_ascii=False),
        )

    def test_case_package_has_state_active_and_proposed_decisions(self) -> None:
        package = build_medical_case_package(self._decision_package())

        self.assertEqual(package["status"], "awaiting_confirmation")
        self.assertTrue(package["active"])
        self.assertIn("proposed_decisions", package)
        self.assertEqual(package["archive_next_action"]["next_action"], "awaiting_confirmation")

    def test_updates_case_with_recovery_result_and_next_action(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        updated = attach_recovery_result_to_case(
            package,
            {
                "passed": True,
                "next_route": "archive-ready",
                "summary": {"check_count": 2, "failed_count": 0},
            },
            recovery_record="wiki/ops/wiki-recovery-runs/recovery.md",
        )

        self.assertEqual(updated["recovery"]["status"], "completed")
        self.assertEqual(updated["status"], "archive_ready")
        self.assertEqual(updated["archive_next_action"]["next_action"], "archive_ready")
        self.assertIn("wiki/ops/wiki-recovery-runs/recovery.md", updated["evidence_attachments"]["recovery"])

    def test_failed_recovery_archive_ready_route_blocks_case(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        updated = attach_recovery_result_to_case(
            package,
            {
                "passed": False,
                "next_route": "archive-ready",
                "summary": {"check_count": 2, "failed_count": 1},
            },
        )

        self.assertEqual(updated["status"], "blocked")
        self.assertEqual(updated["archive_next_action"]["next_action"], "blocked")

    def test_unknown_recovery_route_with_passed_true_blocks_case(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        updated = attach_recovery_result_to_case(
            package,
            {
                "passed": True,
                "next_route": "unexpected-route",
                "summary": {},
            },
        )

        self.assertEqual(updated["status"], "blocked")
        self.assertEqual(updated["archive_next_action"]["next_action"], "blocked")

    def test_recovery_candidates_become_proposed_decisions_requiring_confirmation(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        updated = attach_recovery_result_to_case(
            package,
            {
                "passed": True,
                "next_route": "archive-ready",
                "proposed_decisions": {
                    "treatment_candidates": [
                        {
                            "detail_ref": "detail-recovery-treatment",
                            "path": "wiki/ops/recovery-treatment.md",
                            "reason": "recovery found missing frontmatter",
                        }
                    ],
                },
            },
        )

        self.assertEqual(
            updated["proposed_decisions"]["treatment_candidates"][0]["detail_ref"],
            "detail-recovery-treatment",
        )
        self.assertEqual(updated["status"], "awaiting_confirmation")
        self.assertEqual(updated["archive_next_action"]["next_action"], "awaiting_confirmation")

    def test_repeated_recovery_attach_deduplicates_records_and_proposed_decisions(self) -> None:
        from scripts.wiki_medical_case import attach_recovery_result_to_case

        package = build_medical_case_package(self._decision_package())
        recovery_package = {
            "passed": True,
            "next_route": "archive-ready",
            "treatment_candidates": [
                {
                    "detail_ref": "detail-recovery-treatment",
                    "path": "wiki/ops/recovery-treatment.md",
                    "reason": "recovery found missing frontmatter",
                }
            ],
        }

        updated = attach_recovery_result_to_case(
            package,
            recovery_package,
            recovery_record="wiki/ops/wiki-recovery-runs/recovery.md",
        )
        updated = attach_recovery_result_to_case(
            updated,
            recovery_package,
            recovery_record="wiki/ops/wiki-recovery-runs/recovery.md",
        )

        self.assertEqual(
            updated["recovery"]["records"],
            ["wiki/ops/wiki-recovery-runs/recovery.md"],
        )
        self.assertEqual(
            updated["evidence_attachments"]["recovery"],
            ["wiki/ops/wiki-recovery-runs/recovery.md"],
        )
        self.assertEqual(len(updated["proposed_decisions"]["treatment_candidates"]), 1)


if __name__ == "__main__":
    unittest.main()
