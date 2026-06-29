from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class NativeSuperpowersOpenSpecWorkflowTest(unittest.TestCase):
    def read(self, rel_path: str) -> str:
        return (ROOT / rel_path).read_text(encoding="utf-8")

    def test_openspec_apply_skill_preserves_superpowers_native_execution(self) -> None:
        text = self.read(".codex/skills/openspec-apply-change/SKILL.md")
        self.assertIn("Superpowers plan is the implementation plan", text)
        self.assertIn("OpenSpec tasks are the check/archive ledger", text)
        self.assertIn("do not track Superpowers block progress in tasks.md", text)
        self.assertIn("scope changes stop implementation", text)

    def test_active_change_defines_plan_check_without_new_plan(self) -> None:
        design = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/design.md")
        self.assertIn("plan-check belongs to Superpowers plan review", design)
        self.assertIn("plan-check does not create a new plan", design)
        self.assertIn("Acceptance Spec lives inside the Superpowers design spec", design)

    def test_tasks_are_check_archive_only(self) -> None:
        tasks = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md")
        self.assertIn("This file is not the implementation plan", tasks)
        self.assertIn("Use the Superpowers plan for block execution", tasks)
        forbidden = ["Run RED", "Implement GREEN", "Edit file", "Add function"]
        for marker in forbidden:
            self.assertNotIn(marker, tasks)

    def test_evaluation_records_drift_and_negative_cases(self) -> None:
        evaluation = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md")
        self.assertIn("positive trigger", evaluation)
        self.assertIn("negative should-not-trigger", evaluation)
        self.assertIn("Stripe H5 drift", evaluation)
        self.assertIn("scope change", evaluation)
