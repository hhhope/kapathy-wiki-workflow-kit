import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_behavior_assets import check_behavior_assets


class BehaviorAssetEvaluationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="behavior-assets-"))
        (self.tmpdir / "wiki/config").mkdir(parents=True)
        (self.tmpdir / "openspec/changes").mkdir(parents=True)
        (self.tmpdir / "AGENTS.md").write_text(
            "## High-Frequency Skills\n\n| Situation | Load |\n|---|---|\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def write_config(self) -> None:
        (self.tmpdir / "wiki/config/behavior-asset-evaluation.yaml").write_text(
            """
severity:
  missing_evaluation: error
  missing_required_section: error
  missing_negative_scenario: error
  missing_parent_gate_preservation: error
  route_table_ownership_drift: error
  weak_replay_evidence: warn
required_sections:
  - "## Pressure Scenarios"
  - "## RED Baseline"
  - "## GREEN Result"
  - "## Residual Risks"
required_replay_fields:
  - "input or situation shape"
  - "trigger condition"
  - "repo-visible artifact"
  - "expected output"
  - "proof boundary"
positive_markers:
  - "positive"
  - "trigger"
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

    def test_missing_evaluation_for_skill_change_is_error(self) -> None:
        self.write_config()
        change = self.tmpdir / "openspec/changes/skill-change"
        change.mkdir(parents=True)
        (change / "proposal.md").write_text("Change .codex/skills/example/SKILL.md\n", encoding="utf-8")

        entries = check_behavior_assets(self.tmpdir)

        self.assertTrue(any(entry.kind == "missing_evaluation" for entry in entries))

    def test_route_table_ownership_drift_is_error(self) -> None:
        self.write_config()
        (self.tmpdir / "AGENTS.md").write_text(
            "## High-Frequency Skills\n\n| Situation | Load |\n|---|---|\n\n"
            "## Agent Intent Routing\n\nMinimum routes:\n\n| Intent shape | Parent gate |\n|---|---|\n",
            encoding="utf-8",
        )

        entries = check_behavior_assets(self.tmpdir)

        self.assertTrue(any(entry.kind == "route_table_ownership_drift" for entry in entries))

    def test_valid_behavior_evaluation_passes(self) -> None:
        self.write_config()
        change = self.tmpdir / "openspec/changes/skill-change"
        change.mkdir(parents=True)
        (change / "proposal.md").write_text("Change .codex/skills/example/SKILL.md parent gate\n", encoding="utf-8")
        (change / "evaluation.md").write_text(
            """## Pressure Scenarios

| Case | Expected |
|---|---|
| positive trigger case | load skill |
| negative should-not-trigger case | do not load skill |
| parent gate preserve case | preserve parent gate blockers |

## Replay Evidence

- input or situation shape: semantic skill change
- trigger condition: `.codex/skills/*` edit
- repo-visible artifact: AGENTS.md and skill file
- expected output: route before edit
- proof boundary: local checker proof only

## RED Baseline

Observed failing command: `python3 scripts/check_behavior_assets.py` reported missing gate.

## GREEN Result

Manual replay record: file paths and expected observations are listed above.

## Residual Risks

Future agents must load repo guidance.
""",
            encoding="utf-8",
        )

        entries = check_behavior_assets(self.tmpdir)

        self.assertEqual([entry for entry in entries if entry.severity == "error"], [])


if __name__ == "__main__":
    unittest.main()
