import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.completion_bridge_gate import validate_record


VALID_EXPERIMENT_RECORD = {
    "thread_label": "dual-track workflow experiment",
    "delivery_result": "OpenSpec change completed and focused tests passed.",
    "original_question_required": True,
    "original_question": "What did the Superpowers + OpenSpec dual-track run prove?",
    "bridge_answer": "It proved the lifecycle can stay bounded, but completion reporting needs this bridge gate.",
    "next_action": "archive_review",
    "red_baseline": ["final report listed commits and tests but did not answer the dual-track question"],
    "green_result": ["final report includes delivery_result, original_question, and bridge_answer"],
    "residual_risk": ["structural replay only; live agent behavior still needs rollout observation"],
    "checks": {
        "delivery_result_present": True,
        "original_question_identified": True,
        "bridge_answer_present": True,
        "no_scope_continuation": True,
        "no_unearned_runtime_claim": True,
    },
}


class CompletionBridgeGateTest(unittest.TestCase):
    def test_validate_record_passes_for_explicit_original_question(self) -> None:
        self.assertEqual(validate_record(VALID_EXPERIMENT_RECORD), [])

    def test_delivery_only_report_fails_when_original_question_was_required(self) -> None:
        invalid = dict(VALID_EXPERIMENT_RECORD)
        invalid["original_question"] = ""
        invalid["bridge_answer"] = ""
        invalid["checks"] = dict(VALID_EXPERIMENT_RECORD["checks"])
        invalid["checks"]["original_question_identified"] = False
        invalid["checks"]["bridge_answer_present"] = False

        errors = validate_record(invalid)

        self.assertIn("missing original_question for required completion bridge", errors)
        self.assertIn("missing bridge_answer for required completion bridge", errors)
        self.assertIn("required pass-condition failed: checks.original_question_identified", errors)
        self.assertIn("required pass-condition failed: checks.bridge_answer_present", errors)

    def test_lightweight_completion_passes_without_original_question(self) -> None:
        record = {
            "thread_label": "small docs update",
            "delivery_result": "Updated one doc and validated OpenSpec.",
            "original_question_required": False,
            "next_action": "no_action",
            "red_baseline": ["not applicable: no broader question was asked"],
            "green_result": ["concise delivery summary with verification evidence"],
            "residual_risk": ["no runtime behavior claim"],
            "checks": {
                "delivery_result_present": True,
                "original_question_identified": True,
                "bridge_answer_present": True,
                "no_scope_continuation": True,
                "no_unearned_runtime_claim": True,
            },
        }

        self.assertEqual(validate_record(record), [])

    def test_follow_up_cannot_continue_inside_completed_scope(self) -> None:
        invalid = dict(VALID_EXPERIMENT_RECORD)
        invalid["next_action"] = "continue_implementation"
        invalid["checks"] = dict(VALID_EXPERIMENT_RECORD["checks"])
        invalid["checks"]["no_scope_continuation"] = False

        errors = validate_record(invalid)

        self.assertIn("invalid next_action: continue_implementation", errors)
        self.assertIn("required pass-condition failed: checks.no_scope_continuation", errors)

    def test_cli_reports_pass_for_valid_record(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "completion-bridge.json"
            path.write_text(json.dumps(VALID_EXPERIMENT_RECORD), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).resolve().parents[1] / "scripts" / "completion_bridge_gate.py"),
                    str(path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertIn("PASS: completion bridge replay record satisfies the executable contract.", result.stdout)


if __name__ == "__main__":
    unittest.main()
