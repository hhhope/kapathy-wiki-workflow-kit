import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.wiki_medical_case import build_medical_case_package, write_medical_case_file
from scripts.wiki_medical_agent import (
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


if __name__ == "__main__":
    unittest.main()
