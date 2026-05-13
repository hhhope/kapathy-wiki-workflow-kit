import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.repo_health_check import run_health_checks


class RepoHealthCheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="repo-health-check-"))
        self.write_behavior_asset_config()

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def write_behavior_asset_config(self) -> None:
        config_path = self.tmpdir / "wiki/config/behavior-asset-evaluation.yaml"
        config_path.parent.mkdir(parents=True)
        config_path.write_text(
            """
severity:
  missing_evaluation: error
  missing_required_section: error
  missing_positive_scenario: error
  missing_negative_scenario: error
  missing_parent_gate_preservation: error
  route_table_ownership_drift: error
  weak_replay_evidence: error
  shallow_text_evidence: error
required_sections:
  - "## Pressure Scenarios"
  - "## RED Baseline"
  - "## GREEN Result"
  - "## Residual Risks"
required_replay_fields:
  - "input or situation shape"
  - "trigger condition"
  - "expected route"
  - "repo-visible artifact"
  - "expected output"
  - "promotion or non-promotion boundary"
  - "proof boundary"
positive_markers:
  - "positive"
shallow_evidence_markers:
  - "text exists"
  - "presence-only"
  - "contains required text"
negative_markers:
  - "negative"
  - "should-not-trigger"
parent_gate_markers:
  - "parent gate"
  - "preserve"
covered_change_markers:
  - ".codex/skills/"
  - "AGENTS.md"
  - "runtime routing"
  - "parent gate"
ownership_rules:
  agent_intent_routing:
    owner_section: "High-Frequency Skills"
    classification_section: "Agent Intent Routing"
    forbidden_markers:
      - "Minimum routes"
      - "| Intent shape | Parent gate |"
""",
            encoding="utf-8",
        )

    def test_reports_pass_for_clean_repo(self) -> None:
        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].name, "draft-skill-runtime-surface")
        self.assertTrue(results[0].passed)
        self.assertEqual(results[0].details, [])
        self.assertEqual(results[1].name, "skill-evaluation-evidence")
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])
        self.assertEqual(results[2].name, "behavior-asset-evaluation")
        self.assertTrue(results[2].passed)
        self.assertEqual(results[2].details, [])

    def test_reports_fail_for_draft_skill_violation(self) -> None:
        skill_path = self.tmpdir / "skills-drafts" / "example-skill" / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text("# draft skill", encoding="utf-8")

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertFalse(results[0].passed)
        self.assertEqual(results[0].details, ["skills-drafts/example-skill/SKILL.md"])
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])
        self.assertTrue(results[2].passed)
        self.assertEqual(results[2].details, [])

    def test_reports_fail_for_skill_change_without_evaluation_md(self) -> None:
        change_dir = self.tmpdir / "openspec" / "changes" / "example-skill-change"
        change_dir.mkdir(parents=True)
        (change_dir / "proposal.md").write_text(
            "Publish .codex/skills/example-skill/SKILL.md\n",
            encoding="utf-8",
        )

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].passed)
        self.assertFalse(results[1].passed)
        self.assertEqual(results[1].details, ["openspec/changes/example-skill-change"])
        self.assertFalse(results[2].passed)
        self.assertEqual(len(results[2].details), 1)
        self.assertIn("missing_evaluation", results[2].details[0])

    def test_reports_pass_for_skill_change_with_valid_evaluation_md(self) -> None:
        change_dir = self.tmpdir / "openspec" / "changes" / "example-skill-change"
        change_dir.mkdir(parents=True)
        (change_dir / "proposal.md").write_text(
            "Publish .codex/skills/example-skill/SKILL.md\n",
            encoding="utf-8",
        )
        (change_dir / "evaluation.md").write_text(
            """## Pressure Scenarios

| Case | Expected |
|---|---|
| positive trigger case | load skill |
| negative should-not-trigger case | do not load skill |
| parent gate preserve case | preserve parent gate blockers |

## Replay Evidence

- input or situation shape: semantic skill change
- trigger condition: `.codex/skills/*` edit
- expected route: route through parent gate before edit
- repo-visible artifact: AGENTS.md and skill file
- expected output: route before edit
- promotion or non-promotion boundary: repo-local only
- proof boundary: local checker proof only

## RED Baseline

Before

## GREEN Result

After

## Residual Risks

Risk
""",
            encoding="utf-8",
        )

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].passed)
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])
        self.assertTrue(results[2].passed)
        self.assertEqual(results[2].details, [])

    def test_reports_fail_for_skill_change_without_pressure_test_sections(self) -> None:
        change_dir = self.tmpdir / "openspec" / "changes" / "example-skill-change"
        change_dir.mkdir(parents=True)
        (change_dir / "proposal.md").write_text(
            "Publish .codex/skills/example-skill/SKILL.md\n",
            encoding="utf-8",
        )
        (change_dir / "evaluation.md").write_text(
            """## Baseline Scenarios

Case

## Before Results

Before

## After Results

After

## Residual Risks

Risk
""",
            encoding="utf-8",
        )

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].passed)
        self.assertFalse(results[1].passed)
        self.assertEqual(results[1].details, ["openspec/changes/example-skill-change"])
        self.assertFalse(results[2].passed)
        self.assertTrue(any("missing_required_section" in detail for detail in results[2].details))

    def test_reports_fail_for_agent_intent_route_table_drift(self) -> None:
        (self.tmpdir / "AGENTS.md").write_text(
            "## High-Frequency Skills\n\n| Situation | Load |\n|---|---|\n\n"
            "## Agent Intent Routing\n\nMinimum routes:\n\n| Intent shape | Parent gate |\n|---|---|\n",
            encoding="utf-8",
        )

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 3)
        self.assertTrue(results[0].passed)
        self.assertTrue(results[1].passed)
        self.assertFalse(results[2].passed)
        self.assertEqual(results[2].name, "behavior-asset-evaluation")
        self.assertTrue(any("route_table_ownership_drift" in detail for detail in results[2].details))


if __name__ == "__main__":
    unittest.main()
