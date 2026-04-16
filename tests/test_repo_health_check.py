import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.repo_health_check import run_health_checks


class RepoHealthCheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="repo-health-check-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_reports_pass_for_clean_repo(self) -> None:
        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].name, "draft-skill-runtime-surface")
        self.assertTrue(results[0].passed)
        self.assertEqual(results[0].details, [])
        self.assertEqual(results[1].name, "skill-evaluation-evidence")
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])

    def test_reports_fail_for_draft_skill_violation(self) -> None:
        skill_path = self.tmpdir / "skills-drafts" / "example-skill" / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text("# draft skill", encoding="utf-8")

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 2)
        self.assertFalse(results[0].passed)
        self.assertEqual(results[0].details, ["skills-drafts/example-skill/SKILL.md"])
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])

    def test_reports_fail_for_skill_change_without_evaluation_md(self) -> None:
        change_dir = self.tmpdir / "openspec" / "changes" / "example-skill-change"
        change_dir.mkdir(parents=True)
        (change_dir / "proposal.md").write_text(
            "Publish .codex/skills/example-skill/SKILL.md\n",
            encoding="utf-8",
        )

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 2)
        self.assertTrue(results[0].passed)
        self.assertFalse(results[1].passed)
        self.assertEqual(results[1].details, ["openspec/changes/example-skill-change"])

    def test_reports_pass_for_skill_change_with_valid_evaluation_md(self) -> None:
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

        self.assertEqual(len(results), 2)
        self.assertTrue(results[0].passed)
        self.assertTrue(results[1].passed)
        self.assertEqual(results[1].details, [])


if __name__ == "__main__":
    unittest.main()
