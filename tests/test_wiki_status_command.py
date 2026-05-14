import unittest
from pathlib import Path


class WikiStatusSkillTest(unittest.TestCase):
    def test_wiki_status_skill_is_self_contained(self) -> None:
        skill_path = Path(".codex/skills/wiki-status/SKILL.md")

        self.assertTrue(skill_path.exists())
        skill = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: wiki-status", skill)
        self.assertIn("python3 scripts/build_wiki_status.py", skill)
        self.assertIn("wiki/status/manifest.json", skill)
        self.assertIn("wiki/status/wiki-status.md", skill)
        self.assertIn("strict frontmatter gate", skill)
        self.assertIn("Do not mark OpenSpec tasks complete", skill)
        self.assertNotIn("Command contract:", skill)
        self.assertNotIn("/wiki:status", skill)
        self.assertNotIn("plugins/report-wiki-portfolio/commands", skill)

    def test_no_claude_only_wiki_status_command_remains(self) -> None:
        self.assertFalse(Path(".claude/commands/wiki/status.md").exists())


if __name__ == "__main__":
    unittest.main()
