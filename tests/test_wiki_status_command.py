import unittest
from pathlib import Path


class WikiStatusCommandTest(unittest.TestCase):
    def test_claude_slash_command_refreshes_wiki_status(self) -> None:
        command_path = Path(".claude/commands/wiki/status.md")

        self.assertTrue(command_path.exists())
        content = command_path.read_text(encoding="utf-8")
        self.assertIn("/wiki:status", content)
        self.assertIn("python3 scripts/build_wiki_status.py", content)
        self.assertIn("wiki/status/manifest.json", content)
        self.assertIn("wiki/status/wiki-status.md", content)
        self.assertIn("Do not implement query, scorecard, graph UI, or change queue", content)


if __name__ == "__main__":
    unittest.main()
