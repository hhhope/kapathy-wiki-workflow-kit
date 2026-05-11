import unittest
from pathlib import Path


SKILL = Path(".codex/skills/public-report-quality-gate/SKILL.md")
SCORECARD = Path(".codex/skills/public-report-quality-gate/references/scorecard.md")
GATE_REVIEW = Path(
    ".codex/skills/public-report-quality-gate/references/gate-review-artifact.md"
)
PRESSURE = Path(".codex/skills/public-report-quality-gate/references/pressure-scenarios.md")
REVIEWER = Path(".codex/agents/public-report-reviewer.md")
AGENTS = Path("AGENTS.md")


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

    def test_gate_blocks_reference_shape_drift_from_newspaper_reference(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        scorecard = SCORECARD.read_text(encoding="utf-8")
        gate_review = GATE_REVIEW.read_text(encoding="utf-8")
        pressure = PRESSURE.read_text(encoding="utf-8")

        self.assertIn("Reference Output Shape Gate", skill)
        self.assertIn("selected output shape", skill)
        self.assertIn("image prompts", skill)

        self.assertIn("Reference Output Shape Gate", scorecard)
        self.assertIn("modular grid", scorecard)
        self.assertIn("comparison table", scorecard)

        self.assertIn("Reference Output Shape", gate_review)
        self.assertIn("retained patterns", gate_review)
        self.assertIn("rejected patterns", gate_review)

        self.assertIn("Reference Output Shape Replay", pressure)
        self.assertIn("company analysis becomes repeated cards", pressure)
        self.assertIn("final takeaway becomes a 2x2 card wall", pressure)

    def test_reference_shape_gate_uses_replayable_non_subjective_wording(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        scorecard = SCORECARD.read_text(encoding="utf-8")
        gate_review = GATE_REVIEW.read_text(encoding="utf-8")
        pressure = PRESSURE.read_text(encoding="utf-8")

        self.assertIn("Reference Output Shape Gate", skill)
        self.assertIn("selected output shape", skill)
        self.assertIn("explicit user approval", skill)
        self.assertNotIn("colored-panel", skill)
        self.assertNotIn("card-wall", skill)
        self.assertNotIn("dashboard grid", skill)

        self.assertIn("Reference Output Shape Gate", scorecard)
        self.assertIn("silently replaces the selected output shape", scorecard)
        self.assertIn("Observable failures", scorecard)
        self.assertNotIn("colored-panel taxonomies", scorecard)

        self.assertIn("Reference Output Shape", gate_review)
        self.assertIn("selected output shape", gate_review)
        self.assertIn("user-approved shape changes", gate_review)

        self.assertIn("Reference Output Shape Replay", pressure)
        self.assertIn("without explicit user approval", pressure)

    def test_public_output_visual_work_stays_under_outer_gate(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        pressure = PRESSURE.read_text(encoding="utf-8")
        agents = AGENTS.read_text(encoding="utf-8")

        self.assertIn("Outer Gate Role", skill)
        self.assertIn("owns the outer gate", skill)
        self.assertIn("knowledge-article-visual", skill)
        self.assertIn("infographic-onepager", skill)
        self.assertIn("imagegen", skill)
        self.assertIn("lark-doc", skill)
        self.assertIn("must not bypass", skill)

        self.assertIn("Public Output Delegation Replay", pressure)
        self.assertIn("基于这个对外 H5 生成知识卡和一图流", pressure)
        self.assertIn("每家公司一张知识卡", pressure)
        self.assertIn("routes directly to `imagegen`", pressure)

        self.assertIn("high-level router/gate", agents)
        self.assertIn("tool wrapper", agents)
        self.assertIn("delivery-sensitive module", agents)
        self.assertIn("parent gate", agents)


if __name__ == "__main__":
    unittest.main()
