import unittest
from pathlib import Path


SOURCE_ROOT = Path("plugins/report-wiki-portfolio/skills")
REPO_SKILL_ROOT = Path(".codex/skills")

OPENSPEC_SKILLS = (
    "openspec-apply-change",
    "openspec-archive-change",
    "openspec-explore",
    "openspec-propose",
)


class OpenSpecSkillNamespaceTest(unittest.TestCase):
    def test_openspec_skill_sources_are_installable_not_repo_local(self) -> None:
        for skill_name in OPENSPEC_SKILLS:
            with self.subTest(skill=skill_name):
                source_path = SOURCE_ROOT / skill_name / "SKILL.md"
                repo_local_path = REPO_SKILL_ROOT / skill_name / "SKILL.md"

                self.assertTrue(source_path.exists(), source_path)
                self.assertFalse(repo_local_path.exists(), repo_local_path)
                content = source_path.read_text(encoding="utf-8")
                self.assertIn(f"name: {skill_name}", content)
                self.assertNotIn("report-wiki-portfolio:", content)

    def test_repo_guidance_uses_plain_openspec_skill_names(self) -> None:
        guidance = Path("AGENTS.md").read_text(encoding="utf-8")

        for skill_name in OPENSPEC_SKILLS:
            with self.subTest(skill=skill_name):
                self.assertIn(f"${skill_name}", guidance)

        self.assertNotIn(".codex/skills/openspec-", guidance)


if __name__ == "__main__":
    unittest.main()
