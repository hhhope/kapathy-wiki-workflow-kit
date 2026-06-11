from pathlib import Path
import unittest


SKILL = Path(".codex/skills/product-discovery-wiki-capture/SKILL.md")
AGENTS = Path("AGENTS.md")
CHANGE = Path("openspec/changes/route-product-discovery-through-wiki-capture")
SPEC = CHANGE / "specs/product-discovery-wiki-capture/spec.md"
EVALUATION = CHANGE / "evaluation.md"
WIKI_NOTE = Path("wiki/ops/ai-agent-subscription-payments-product-discovery-2026-06-11.md")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class ProductDiscoveryWikiCaptureTest(unittest.TestCase):
    def test_agents_routes_product_discovery_capture_through_high_frequency_skills(self) -> None:
        text = read(AGENTS)

        self.assertIn("## High-Frequency Skills", text)
        self.assertIn("PM/product-discovery analysis", text)
        self.assertIn(".codex/skills/product-discovery-wiki-capture/SKILL.md", text)

    def test_skill_defines_product_discovery_wiki_capture_route(self) -> None:
        text = read(SKILL)

        self.assertIn("PM/product-discovery", text)
        self.assertIn("wiki recording intent", text)
        self.assertIn("durable memory", text)
        self.assertIn("wiki/ops/", text)
        self.assertIn("source prompt or situation", text)
        self.assertIn("opportunity framing", text)
        self.assertIn("validation experiments", text)

    def test_skill_preserves_parent_gates_and_negative_route(self) -> None:
        text = read(SKILL)

        self.assertIn("one-off", text)
        self.assertIn("Do not create durable wiki output by default", text)
        self.assertIn("learning-capture", text)
        self.assertIn("public-report-quality-gate", text)
        self.assertIn("wiki-frontmatter-taxonomy", text)

    def test_openspec_delta_records_positive_negative_and_parent_gate_scenarios(self) -> None:
        text = read(SPEC)

        self.assertIn("Repository SHALL route durable product-discovery analysis to wiki capture", text)
        self.assertIn("Product-discovery analysis has explicit wiki intent", text)
        self.assertIn("Product-discovery answer is one-off", text)
        self.assertIn("Product-discovery work uses external source learning", text)
        self.assertIn("Product-discovery output becomes reader-facing", text)

    def test_evaluation_records_replay_and_prior_art_dedupe(self) -> None:
        text = read(EVALUATION)

        self.assertIn("Pressure Scenarios", text)
        self.assertIn("positive", text)
        self.assertIn("negative", text)
        self.assertIn("parent gate", text)
        self.assertIn("input or situation shape", text)
        self.assertIn("trigger condition", text)
        self.assertIn("expected route", text)
        self.assertIn("repo-visible artifact", text)
        self.assertIn("expected output", text)
        self.assertIn("promotion or non-promotion boundary", text)
        self.assertIn("proof boundary", text)
        self.assertIn("Prior-Art / Common-Rule Dedupe", text)
        self.assertIn("Scanned:", text)
        self.assertIn("Owns:", text)
        self.assertIn("References:", text)
        self.assertIn("Rejects:", text)

    def test_current_product_discovery_note_records_capture_fields(self) -> None:
        text = read(WIKI_NOTE)

        self.assertIn("canonical_object: ai-agent-subscription-payments-product-discovery", text)
        self.assertIn("ops_area: workflow-trace", text)
        self.assertIn("Target Segment / ICP", text)
        self.assertIn("Opportunity Framing", text)
        self.assertIn("Assumptions And Risks", text)
        self.assertIn("Validation Experiments", text)
        self.assertIn("What Was Not Formalized", text)
        self.assertIn("Next Step", text)


if __name__ == "__main__":
    unittest.main()
