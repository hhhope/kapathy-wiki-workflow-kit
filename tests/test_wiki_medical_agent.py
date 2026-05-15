import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_medical_case import build_medical_case_package, load_medical_case_file, write_medical_case_file
from scripts.wiki_medical_agent import (
    apply_confirmed_treatment_and_recover,
    build_status_payload,
    classify_medical_intent,
    resolve_active_case,
    validate_case_action,
)


class WikiMedicalAgentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="wiki-medical-agent-test-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def _case_package(self, status: str = "ready_for_treatment", active: bool = True) -> dict:
        package = build_medical_case_package(
            {
                "generated_at": "2026-05-15T01:02:03+00:00",
                "summary": {},
                "source_adjudication_summary": {},
                "accepted_candidates": [],
                "rejected_candidates": [],
                "deferred_items": [],
                "surgery_candidates": [],
                "openspec_required": [],
                "treatment_candidates": [
                    {
                        "detail_ref": "detail-safe",
                        "path": "wiki/ops/safe.md",
                        "risk_flags": [],
                        "suggested_frontmatter": {
                            "layer": "ops",
                            "domain": "wiki",
                            "ops_area": "wiki-runtime",
                            "canonical_object": "safe",
                            "artifact_type": "method",
                        },
                    }
                ],
            },
            case_slug="confirmed-case",
            timestamp="2026-05-15T01:02:03+00:00",
        )
        package["status"] = status
        package["active"] = active
        return package

    def _write_case(self, package: dict, timestamp: str) -> Path:
        return write_medical_case_file(
            package,
            self.tmpdir,
            output_dir=self.tmpdir / "wiki" / "ops" / "wiki-medical-cases",
            timestamp=timestamp,
        )

    def _target_text(self) -> str:
        return (self.tmpdir / "wiki" / "ops" / "safe.md").read_text(encoding="utf-8")

    def test_classifies_natural_language_intents(self) -> None:
        self.assertEqual(classify_medical_intent("看下 wiki 现在什么状态").intent, "status")
        self.assertEqual(classify_medical_intent("诊断需要处理的问题").intent, "diagnose")
        self.assertEqual(classify_medical_intent("我确认病例里的 Confirmed Decisions").intent, "confirm_decisions")
        self.assertEqual(classify_medical_intent("apply 已确认的 10 个 treatment candidates").intent, "treatment_apply")
        self.assertEqual(classify_medical_intent("做 recovery，告诉我是否闭环").intent, "recovery")

    def test_classifies_preview_before_apply(self) -> None:
        self.assertEqual(
            classify_medical_intent("dry-run apply confirmed treatments").intent,
            "treatment_preview",
        )
        self.assertEqual(
            classify_medical_intent("dry run apply confirmed treatments").intent,
            "treatment_preview",
        )
        self.assertEqual(
            classify_medical_intent("preview apply confirmed treatments").intent,
            "treatment_preview",
        )

    def test_resolve_active_case_blocks_multiple_active_cases(self) -> None:
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:03+00:00")
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:04+00:00")

        resolved = resolve_active_case(self.tmpdir)

        self.assertEqual(resolved.status, "blocked")
        self.assertEqual(resolved.blocked_reason, "multiple_active_cases")
        self.assertEqual(len(resolved.candidates), 2)

    def test_validate_blocks_treatment_without_confirmed_decisions(self) -> None:
        package = self._case_package(status="awaiting_confirmation")
        package["confirmed_decisions"]["treatment_candidates"] = []

        result = validate_case_action(package, "treatment_apply", expected_count=10)

        self.assertFalse(result.allowed)
        self.assertEqual(result.blocked_reason, "no_executable_confirmed_treatment_decisions")

    def test_validate_allows_matching_confirmed_treatment_count(self) -> None:
        result = validate_case_action(self._case_package(), "treatment_apply", expected_count=1)

        self.assertTrue(result.allowed)
        self.assertEqual(result.allowed_action, "apply_confirmed_treatments")

    def test_status_payload_allows_status_without_active_case(self) -> None:
        payload = build_status_payload(self.tmpdir, "看下 wiki 现在什么状态")

        self.assertEqual(payload["intent"], "status")
        self.assertEqual(payload["case_path"], "")
        self.assertEqual(payload["state"], "no_case")
        self.assertTrue(payload["allowed"])
        self.assertEqual(payload["allowed_action"], "report_status")
        self.assertEqual(payload["blocked_reason"], "")
        self.assertEqual(payload["next_action"], "diagnose")

    def test_status_payload_blocks_write_when_multiple_cases_are_active(self) -> None:
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:03+00:00")
        self._write_case(self._case_package(active=True), "2026-05-15T01:02:04+00:00")

        payload = build_status_payload(self.tmpdir, "apply 已确认的 2 个 treatment candidates")

        self.assertEqual(payload["intent"], "treatment_apply")
        self.assertEqual(payload["state"], "multiple_active_cases")
        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "multiple_active_cases")
        self.assertEqual(len(payload["candidate_cases"]), 2)
        self.assertEqual(payload["next_action"], "select_active_case")

    def test_blocked_payload_does_not_use_stale_archive_next_action(self) -> None:
        package = self._case_package(status="awaiting_confirmation")
        package["archive_next_action"] = {"next_action": "archive_ready"}
        self._write_case(package, "2026-05-15T01:02:03+00:00")

        payload = build_status_payload(self.tmpdir, "apply 已确认的 1 个 treatment candidates")

        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "state_does_not_allow_treatment_apply")
        self.assertNotEqual(payload["next_action"], "archive_ready")
        self.assertEqual(payload["next_action"], "state_does_not_allow_treatment_apply")

    def test_cli_status_outputs_intent_case_state_and_next_action(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        case_path = self._write_case(self._case_package(), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "看下 wiki 现在什么状态",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "status")
        self.assertEqual(payload["case_path"], case_path.as_posix())
        self.assertEqual(payload["state"], "ready_for_treatment")
        self.assertIn("next_action", payload)

    def test_cli_applies_confirmed_treatment_then_runs_recovery(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        target = self.tmpdir / "wiki" / "ops" / "safe.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Safe\n", encoding="utf-8")
        case_path = self._write_case(self._case_package(status="ready_for_treatment"), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 1 个 treatment candidates",
                "--approved-detail",
                "detail-safe",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertEqual(payload["intent"], "treatment_apply")
        self.assertEqual(payload["case_path"], case_path.as_posix())
        self.assertEqual(payload["applied"], 1)
        self.assertEqual(payload["recovery"]["status"], "completed")
        self.assertIn(payload["next_action"], {"archive_ready", "blocked"})

    def test_direct_apply_rejects_wrong_state_before_writing_records(self) -> None:
        target = self.tmpdir / "wiki" / "ops" / "safe.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Safe\n", encoding="utf-8")
        case_path = self._write_case(
            self._case_package(status="awaiting_confirmation"),
            "2026-05-15T01:02:03+00:00",
        )

        with self.assertRaisesRegex(ValueError, "state_does_not_allow_treatment_apply"):
            apply_confirmed_treatment_and_recover(
                self.tmpdir,
                case_path,
                approved_detail_refs={"detail-safe"},
            )

        self.assertEqual(self._target_text(), "# Safe\n")
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-treatment-runs").exists())
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-recovery-runs").exists())

    def test_cli_apply_missing_approval_writes_nothing(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        target = self.tmpdir / "wiki" / "ops" / "safe.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Safe\n", encoding="utf-8")
        self._write_case(self._case_package(status="ready_for_treatment"), "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 1 个 treatment candidates",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)

        self.assertFalse(payload["allowed"])
        self.assertEqual(payload["blocked_reason"], "missing_explicit_treatment_approval")
        self.assertEqual(self._target_text(), "# Safe\n")
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-treatment-runs").exists())
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-recovery-runs").exists())

    def test_partial_treatment_failure_blocks_before_recovery(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        target = self.tmpdir / "wiki" / "ops" / "safe.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Safe\n", encoding="utf-8")
        package = self._case_package(status="ready_for_treatment")
        package["confirmed_decisions"]["treatment_candidates"].append(
            {
                "detail_ref": "detail-missing",
                "path": "wiki/ops/missing.md",
                "risk_flags": [],
                "suggested_frontmatter": {
                    "layer": "ops",
                    "domain": "wiki",
                    "ops_area": "wiki-runtime",
                    "canonical_object": "missing",
                    "artifact_type": "method",
                },
            }
        )
        case_path = self._write_case(package, "2026-05-15T01:02:03+00:00")

        result = subprocess.run(
            [
                sys.executable,
                "scripts/build_wiki_medical_agent.py",
                "--root",
                str(self.tmpdir),
                "--intent-text",
                "apply 已确认的 2 个 treatment candidates",
                "--approved-detail",
                "detail-safe",
                "--approved-detail",
                "detail-missing",
                "--apply",
            ],
            cwd=repo_root,
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        loaded_case = load_medical_case_file(case_path)

        self.assertEqual(payload["applied"], 1)
        self.assertEqual(payload["blocked"], 1)
        self.assertEqual(payload["next_action"], "blocked")
        self.assertIn("treatment_record", payload)
        self.assertTrue(Path(payload["treatment_record"]).exists())
        self.assertNotIn("recovery", payload)
        self.assertFalse((self.tmpdir / "wiki" / "ops" / "wiki-recovery-runs").exists())
        self.assertEqual(loaded_case["archive_next_action"]["next_action"], "blocked")
        self.assertIn("treatment blocked", loaded_case["archive_next_action"]["reason"])


if __name__ == "__main__":
    unittest.main()
