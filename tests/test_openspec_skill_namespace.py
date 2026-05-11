import unittest
from pathlib import Path


REPO_SKILL_ROOT = Path(".codex/skills")
USER_SKILL_ROOT = Path.home() / ".codex" / "skills"

OPENSPEC_SKILLS = (
    "openspec-apply-change",
    "openspec-archive-change",
    "openspec-explore",
    "openspec-propose",
)


class OpenSpecSkillNamespaceTest(unittest.TestCase):
    def test_openspec_skill_sources_are_repo_local(self) -> None:
        for skill_name in OPENSPEC_SKILLS:
            with self.subTest(skill=skill_name):
                repo_local_path = REPO_SKILL_ROOT / skill_name / "SKILL.md"

                self.assertTrue(repo_local_path.exists(), repo_local_path)
                content = repo_local_path.read_text(encoding="utf-8")
                self.assertIn(f"name: {skill_name}", content)
                self.assertNotIn("report-wiki-portfolio:", content)

    def test_repo_guidance_uses_repo_local_openspec_skill_paths(self) -> None:
        guidance = Path("AGENTS.md").read_text(encoding="utf-8")

        for skill_name in OPENSPEC_SKILLS:
            with self.subTest(skill=skill_name):
                self.assertIn(f".codex/skills/{skill_name}/SKILL.md", guidance)

        self.assertNotIn("plugins/report-wiki-portfolio/skills/openspec-", guidance)

    def test_user_scope_does_not_duplicate_repo_openspec_skills(self) -> None:
        for skill_name in OPENSPEC_SKILLS:
            with self.subTest(skill=skill_name):
                self.assertFalse(
                    (USER_SKILL_ROOT / skill_name / "SKILL.md").exists(),
                    USER_SKILL_ROOT / skill_name / "SKILL.md",
                )


if __name__ == "__main__":
    unittest.main()
