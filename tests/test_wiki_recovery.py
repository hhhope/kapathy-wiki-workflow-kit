import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_recovery import (
    build_recovery_package,
    render_recovery_record_markdown,
    write_recovery_record,
)


class WikiRecoveryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-recovery-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_builds_package_and_preserves_nonzero_check(self) -> None:
        checks = [
            {"check_id": "pass-check", "command": ["pass"]},
            {"check_id": "fail-check", "command": ["fail"]},
        ]

        def runner(command, cwd):
            if command == ["pass"]:
                return 0, json.dumps({"summary": {"ok": 1}, "status": "pass"}), ""
            return 2, json.dumps({"summary": {"errors": 3}}), "bad drift"

        package = build_recovery_package(self.tmpdir, checks=checks, runner=runner)

        self.assertEqual(package["summary"]["check_count"], 2)
        self.assertEqual(package["summary"]["failed_count"], 1)
        self.assertFalse(package["passed"])
        self.assertEqual(package["next_route"], "blocked_by_recovery_findings")
        self.assertEqual(package["checks"][0]["parsed_summary"], {"ok": 1, "status": "pass"})
        self.assertEqual(package["checks"][1]["exit_code"], 2)
        self.assertEqual(package["checks"][1]["stderr_tail"], "bad drift")
        self.assertIn("does not apply treatment", " ".join(package["proof_boundary_notes"]))

    def test_writes_recovery_record_without_overwriting_existing_file(self) -> None:
        package = build_recovery_package(
            self.tmpdir,
            checks=[{"check_id": "pass-check", "command": ["pass"]}],
            runner=lambda command, cwd: (0, json.dumps({"summary": {"ok": 1}}), ""),
        )
        output_dir = self.tmpdir / "records"

        first = write_recovery_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )
        second = write_recovery_record(
            package,
            self.tmpdir,
            output_dir=output_dir,
            timestamp="2026-05-15T01:02:03+00:00",
        )

        self.assertEqual(first.name, "2026-05-15-010203-recovery.md")
        self.assertEqual(second.name, "2026-05-15-010203-recovery-2.md")
        self.assertIn("# wiki-recovery Record", first.read_text(encoding="utf-8"))

    def test_renders_record_with_check_results_and_boundaries(self) -> None:
        package = build_recovery_package(
            self.tmpdir,
            checks=[{"check_id": "pass-check", "command": ["pass"]}],
            runner=lambda command, cwd: (0, json.dumps({"summary": {"ok": 1}}), ""),
        )

        markdown = render_recovery_record_markdown(package, scan_root=self.tmpdir)

        self.assertIn("## Check Results", markdown)
        self.assertIn("pass-check", markdown)
        self.assertIn("## Proof Boundary", markdown)
        self.assertIn("does not apply treatment", markdown)

    def test_cli_outputs_json_and_writes_record_only_when_requested(self) -> None:
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
        record_dir = self.tmpdir / "recovery-records"

        default_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        default_payload = json.loads(default_result.stdout)

        self.assertIn("checks", default_payload)
        self.assertNotIn("recovery_record_path", default_payload)
        self.assertFalse(record_dir.exists())

        write_result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
                "--write-recovery-record",
                "--recovery-record-dir",
                str(record_dir),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        write_payload = json.loads(write_result.stdout)

        self.assertIn("recovery_record_path", write_payload)
        self.assertTrue(Path(write_payload["recovery_record_path"]).exists())

    def test_cli_updates_case_file_with_recovery_result(self) -> None:
        from scripts.wiki_medical_case import (
            build_medical_case_package,
            load_medical_case_file,
            write_medical_case_file,
        )

        repo_root = Path(__file__).resolve().parents[1]
        case_package = build_medical_case_package(
            {
                "generated_at": "2026-05-15T01:02:03+00:00",
                "summary": {},
                "source_adjudication_summary": {},
                "accepted_candidates": [],
                "rejected_candidates": [],
                "deferred_items": [],
                "surgery_candidates": [],
                "openspec_required": [],
                "treatment_candidates": [],
            },
            case_slug="recovery-case",
        )
        case_package["status"] = "recovery_required"
        case_path = write_medical_case_file(
            case_package,
            self.tmpdir,
            output_dir=self.tmpdir / "cases",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        record_dir = self.tmpdir / "recovery-records"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
                "--case-file",
                str(case_path),
                "--write-recovery-record",
                "--recovery-record-dir",
                str(record_dir),
                "--update-case-file",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        loaded = load_medical_case_file(case_path)

        self.assertIn("updated_case_file", payload)
        self.assertEqual(loaded["recovery"]["status"], "completed")
        self.assertIn(
            payload["recovery_record_path"],
            loaded["evidence_attachments"]["recovery"],
        )
        self.assertIn(loaded["archive_next_action"]["next_action"], {"archive_ready", "blocked"})

    def test_cli_missing_update_case_file_does_not_write_recovery_record(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        record_dir = self.tmpdir / "recovery-records"

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
                "--case-file",
                str(self.tmpdir / "missing.md"),
                "--write-recovery-record",
                "--recovery-record-dir",
                str(record_dir),
                "--update-case-file",
            ],
            cwd=repo_root,
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(record_dir.exists())

    def test_cli_case_file_without_update_does_not_mutate_case_file(self) -> None:
        from scripts.wiki_medical_case import (
            build_medical_case_package,
            write_medical_case_file,
        )

        repo_root = Path(__file__).resolve().parents[1]
        case_package = build_medical_case_package(
            {
                "generated_at": "2026-05-15T01:02:03+00:00",
                "summary": {},
                "source_adjudication_summary": {},
                "accepted_candidates": [],
                "rejected_candidates": [],
                "deferred_items": [],
                "surgery_candidates": [],
                "openspec_required": [],
                "treatment_candidates": [],
            },
            case_slug="read-only-recovery-case",
        )
        case_package["status"] = "recovery_required"
        case_path = write_medical_case_file(
            case_package,
            self.tmpdir,
            output_dir=self.tmpdir / "cases",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        before = case_path.read_text(encoding="utf-8")

        subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_recovery.py",
                "--root",
                str(self.tmpdir),
                "--case-file",
                str(case_path),
                "--write-recovery-record",
                "--recovery-record-dir",
                str(self.tmpdir / "recovery-records"),
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )

        self.assertEqual(case_path.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main()
