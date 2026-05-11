import unittest
from pathlib import Path


SKILL = Path(".codex/skills/public-report-quality-gate/SKILL.md")
SCORECARD = Path(".codex/skills/public-report-quality-gate/references/scorecard.md")
GATE_REVIEW = Path(
    ".codex/skills/public-report-quality-gate/references/gate-review-artifact.md"
)
PRESSURE = Path(".codex/skills/public-report-quality-gate/references/pressure-scenarios.md")
REVIEWER = Path(".codex/agents/public-report-reviewer.md")


class PublicReportQualityGateTest(unittest.TestCase):
    def test_skill_requires_intent_paragraph_drift_and_judgment_gates(self) -> None:
        content = SKILL.read_text(encoding="utf-8")

        self.assertIn("Article Intent Contract", content)
        self.assertIn("Section And Paragraph Drift Review", content)
        self.assertIn("Judgment Ownership Gate", content)
        self.assertIn("process can be delegated, but judgment cannot", content)

    def test_scorecard_distinguishes_invalid_total_from_diagnostic_scores(self) -> None:
        content = SCORECARD.read_text(encoding="utf-8")

        self.assertIn("Paragraph Drift Gate", content)
        self.assertIn("Judgment Ownership Gate", content)
        self.assertIn("diagnostic scores", content)
        self.assertIn("overall score remains `INVALID`", content)
        self.assertIn("0-5", content)

    def test_gate_review_artifact_records_drift_matrix_and_judgment_ledger(self) -> None:
        content = GATE_REVIEW.read_text(encoding="utf-8")

        self.assertIn("Article Intent Contract", content)
        self.assertIn("Section And Paragraph Drift Review", content)
        self.assertIn("Judgment Ledger", content)
        self.assertIn("Section objective", content)
        self.assertIn("Paragraph claim", content)
        self.assertIn("Judgment source", content)

    def test_reviewer_runs_reverse_outline_before_scoring(self) -> None:
        content = REVIEWER.read_text(encoding="utf-8")

        self.assertIn("Reverse outline", content)
        self.assertIn("paragraph drift", content)
        self.assertIn("judgment ownership", content)
        self.assertIn("retain, compress, rewrite, delete, or ask the user", content)

    def test_pressure_scenarios_cover_user_judgment_regressions(self) -> None:
        content = PRESSURE.read_text(encoding="utf-8")

        self.assertIn("Process can be delegated, but judgment cannot", content)
        self.assertIn("pretty paragraph changes the article's decision", content)
        self.assertIn("reference article's opinion becomes the local conclusion", content)
        self.assertIn("hard failure but diagnostic scores remain available", content)


if __name__ == "__main__":
    unittest.main()
