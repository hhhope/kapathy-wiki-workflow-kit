import unittest
from pathlib import Path


class WikiStatusCommandTest(unittest.TestCase):
    def test_codex_skill_refreshes_wiki_status(self) -> None:
        plugin_root = Path("plugins/report-wiki-portfolio")
        skill_path = Path(".codex/skills/wiki-status/SKILL.md")
        command_path = plugin_root / "commands/wiki-status.md"

        self.assertTrue(skill_path.exists())
        self.assertTrue(command_path.exists())
        skill = skill_path.read_text(encoding="utf-8")
        self.assertIn("name: wiki-status", skill)
        self.assertIn("plugins/report-wiki-portfolio/commands/wiki-status.md", skill)

        content = command_path.read_text(encoding="utf-8")
        self.assertIn("/wiki:status", content)
        self.assertNotIn("/report-wiki-portfolio:wiki-status", content)
        self.assertIn("python3 scripts/build_wiki_status.py", content)
        self.assertIn("wiki/status/manifest.json", content)
        self.assertIn("wiki/status/wiki-status.md", content)
        self.assertIn("natural-language query engine", content)
        self.assertIn("scorecard, graph UI", content)
        self.assertIn("change queue", content)
        self.assertIn("Do not mark OpenSpec tasks complete", content)

    def test_no_claude_only_wiki_status_command_remains(self) -> None:
        self.assertFalse(Path(".claude/commands/wiki/status.md").exists())


if __name__ == "__main__":
    unittest.main()
