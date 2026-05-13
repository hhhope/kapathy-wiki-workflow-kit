from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "AGENTS.md"
PUBLIC_SKILL = ROOT / ".codex/skills/public-report-quality-gate/SKILL.md"
PRESSURE = ROOT / ".codex/skills/public-report-quality-gate/references/pressure-scenarios.md"
CHANGE = ROOT / "openspec/changes/route-repo-public-artifacts-through-agent-intent"
SPEC = CHANGE / "specs/agent-intent-routing/spec.md"
EVALUATION = CHANGE / "evaluation.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class AgentIntentRoutingTest(unittest.TestCase):
    def test_agents_declares_agent_intent_routing_entry_rule(self) -> None:
        text = read(AGENTS)

        self.assertIn("## Agent Intent Routing", text)
        self.assertIn("Before acting, classify the user intent", text)
        self.assertIn("repo-public artifact", text)
        self.assertIn(".codex/skills/public-report-quality-gate/SKILL.md", text)
        self.assertIn("wiki frontmatter taxonomy gate", text)

    def test_agent_intent_routing_references_single_route_table(self) -> None:
        text = read(AGENTS)

        self.assertIn("## High-Frequency Skills", text)
        self.assertIn("## Agent Intent Routing", text)
        agent_intent = text.split("## Agent Intent Routing", 1)[1].split("\n## ", 1)[0]
        self.assertIn("High-Frequency Skills", agent_intent)
        self.assertNotIn("Minimum routes", agent_intent)
        self.assertNotIn("| Intent shape | Parent gate |", agent_intent)

    def test_public_gate_skill_defines_repo_public_lightweight_path(self) -> None:
        text = read(PUBLIC_SKILL)

        self.assertIn("repo-public artifact", text)
        self.assertIn("README.md", text)
        self.assertIn("docs/*", text)
        self.assertIn("examples/*", text)
        self.assertIn("lightweight path", text)
        self.assertIn("reader and job-to-be-done", text)
        self.assertIn("artifact-specific constraint scan", text)
        self.assertIn("does not require a `wiki/ops/*-report-gate-review.md`", text)

    def test_pressure_scenarios_replay_agent_intent_routing(self) -> None:
        text = read(PRESSURE)

        self.assertIn("Agent Intent Routing Replay", text)
        self.assertIn("readMe写一下", text)
        self.assertIn("repo-public artifact", text)
        self.assertIn("README constraint scan", text)
        self.assertIn("这个外部 README 学一下能不能复用", text)
        self.assertIn("learning-capture", text)
        self.assertIn("改一下 wiki frontmatter", text)
        self.assertIn("wiki-frontmatter-taxonomy", text)

    def test_openspec_change_requires_repo_public_routing(self) -> None:
        text = read(SPEC)

        self.assertIn("Repository SHALL classify agent intent before acting", text)
        self.assertIn("Repo-public artifacts SHALL route through public gate lightweight path", text)
        self.assertIn("Agent intent routing SHALL not steal specialized gates", text)
        self.assertIn("Agent intent routing SHALL include behavior replay evidence", text)

    def test_evaluation_records_red_green_replay_and_residual_risk(self) -> None:
        text = read(EVALUATION)

        self.assertIn("RED Baseline", text)
        self.assertIn("GREEN Result", text)
        self.assertIn("readMe写一下", text)
        self.assertIn("repo-visible trigger artifacts", text)
        self.assertIn("Proof Boundary", text)
        self.assertIn("Residual Risks", text)


if __name__ == "__main__":
    unittest.main()
