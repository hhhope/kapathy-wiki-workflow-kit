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

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "draft-skill-runtime-surface")
        self.assertTrue(results[0].passed)
        self.assertEqual(results[0].details, [])

    def test_reports_fail_for_draft_skill_violation(self) -> None:
        skill_path = self.tmpdir / "skills-drafts" / "example-skill" / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text("# draft skill", encoding="utf-8")

        results = run_health_checks(self.tmpdir)

        self.assertEqual(len(results), 1)
        self.assertFalse(results[0].passed)
        self.assertEqual(results[0].details, ["skills-drafts/example-skill/SKILL.md"])


if __name__ == "__main__":
    unittest.main()
