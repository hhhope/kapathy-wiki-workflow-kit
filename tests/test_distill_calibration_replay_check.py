import unittest

from scripts.distill_calibration_replay_check import validate_record


VALID_RECORD = {
    "thread_label": "distill calibration",
    "distill_page": "wiki/ops/example.md",
    "fact_recap_sections": ["facts"],
    "candidate_model_sections": ["candidate"],
    "overclaim_markers": ["final framework"],
    "downgraded_wording": ["candidate framework"],
    "red_baseline": ["narrative only"],
    "green_result": ["replay exists"],
    "residual_risk": ["structural only"],
    "checks": {
        "fact_model_split_preserved": True,
        "overclaim_markers_explicit": True,
        "downgraded_wording_present": True,
        "candidate_model_not_treated_as_canonical": True,
        "no_rollout_claim": True,
    },
}


class DistillCalibrationReplayCheckTest(unittest.TestCase):
    def test_validate_record_passes_for_valid_record(self) -> None:
        self.assertEqual(validate_record(VALID_RECORD), [])

    def test_validate_record_fails_for_missing_required_list(self) -> None:
        invalid = dict(VALID_RECORD)
        invalid["overclaim_markers"] = []

        errors = validate_record(invalid)

        self.assertIn("missing or empty list field: overclaim_markers", errors)

    def test_validate_record_fails_for_required_check_false(self) -> None:
        invalid = dict(VALID_RECORD)
        invalid["checks"] = dict(VALID_RECORD["checks"])
        invalid["checks"]["no_rollout_claim"] = False

        errors = validate_record(invalid)

        self.assertIn(
            "required pass-condition failed: checks.no_rollout_claim",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
