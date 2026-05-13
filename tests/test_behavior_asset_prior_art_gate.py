from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.check_behavior_assets import check_behavior_assets


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "wiki/config/behavior-asset-evaluation.yaml"


class BehaviorAssetPriorArtGateTest(unittest.TestCase):
    def make_repo(self, evaluation: str) -> Path:
        tmp = Path(tempfile.mkdtemp(prefix="behavior-prior-art-"))
        self.addCleanup(shutil.rmtree, tmp)

        (tmp / "wiki/config").mkdir(parents=True)
        shutil.copy(CONFIG, tmp / "wiki/config/behavior-asset-evaluation.yaml")

        change = tmp / "openspec/changes/add-sample-rule"
        (change / "specs/sample").mkdir(parents=True)
        (change / "proposal.md").write_text(
            "Change `rules/sample.md` and AGENTS.md behavior routing.\n",
            encoding="utf-8",
        )
        (change / "evaluation.md").write_text(evaluation, encoding="utf-8")
        return tmp

    def test_missing_prior_art_dedupe_is_error_for_rule_change(self) -> None:
        repo = self.make_repo(
            """# Evaluation

## Pressure Scenarios

positive trigger: rule change routes future behavior.
negative should-not-trigger: unrelated docs do not trigger.

## Replay Evidence

input or situation shape
trigger condition
expected route
repo-visible artifact
expected output
promotion or non-promotion boundary
proof boundary

## RED Baseline

Old wording had no rule.

## GREEN Result

New wording changes behavior.

## Residual Risks

Text-level evidence can miss subtle drift.
"""
        )

        entries = check_behavior_assets(repo)

        self.assertTrue(
            any(entry.kind == "missing_prior_art_dedupe" for entry in entries),
            entries,
        )

    def test_prior_art_dedupe_section_satisfies_rule_change_gate(self) -> None:
        repo = self.make_repo(
            """# Evaluation

## Pressure Scenarios

positive trigger: rule change routes future behavior.
negative should-not-trigger: unrelated docs do not trigger.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo AGENTS.md, ~/.codex/AGENTS.md, ~/.codex/rules/common, and existing rules/.
- Owns: sample-specific behavior.
- References: common large-file, git, testing, and behavior-asset gates.
- Rejects: external generic thresholds as local hard rules.

## Replay Evidence

input or situation shape
trigger condition
expected route
repo-visible artifact
expected output
promotion or non-promotion boundary
proof boundary

## RED Baseline

Old wording had no rule.

## GREEN Result

New wording changes behavior.

## Residual Risks

Text-level evidence can miss subtle drift.
"""
        )

        entries = check_behavior_assets(repo)

        self.assertFalse(
            [entry for entry in entries if entry.kind == "missing_prior_art_dedupe"],
            entries,
        )


if __name__ == "__main__":
    unittest.main()
