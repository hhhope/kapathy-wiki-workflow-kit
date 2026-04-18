import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.repo_policy_check import find_draft_skill_violations


class RepoPolicyCheckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = Path(tempfile.mkdtemp(prefix="repo-policy-check-"))

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_reports_active_skill_files_under_skills_drafts(self) -> None:
        skill_path = self.tmpdir / "skills-drafts" / "example-skill" / "SKILL.md"
        skill_path.parent.mkdir(parents=True)
        skill_path.write_text("# draft skill", encoding="utf-8")

        violations = find_draft_skill_violations(self.tmpdir)

        self.assertEqual(violations, [Path("skills-drafts/example-skill/SKILL.md")])

    def test_allows_non_skill_draft_notes(self) -> None:
        draft_note = self.tmpdir / "skills-drafts" / "example-skill" / "notes.md"
        draft_note.parent.mkdir(parents=True)
        draft_note.write_text("# draft note", encoding="utf-8")

        violations = find_draft_skill_violations(self.tmpdir)

        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
