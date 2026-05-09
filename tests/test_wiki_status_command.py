import unittest
from pathlib import Path


class WikiStatusCommandTest(unittest.TestCase):
    def test_codex_plugin_slash_command_refreshes_wiki_status(self) -> None:
        plugin_manifest_path = Path(".codex-plugin/plugin.json")
        command_path = Path("commands/wiki-status.md")

        self.assertTrue(plugin_manifest_path.exists())
        self.assertTrue(command_path.exists())
        manifest = plugin_manifest_path.read_text(encoding="utf-8")
        self.assertIn('"name": "report-wiki-portfolio"', manifest)
        self.assertIn('"displayName": "Report Wiki Portfolio"', manifest)

        content = command_path.read_text(encoding="utf-8")
        self.assertIn("/wiki:status", content)
        self.assertNotIn("/report-wiki-portfolio:wiki-status", content)
        self.assertIn("python3 scripts/build_wiki_status.py", content)
        self.assertIn("wiki/status/manifest.json", content)
        self.assertIn("wiki/status/wiki-status.md", content)
        self.assertIn("Do not implement query, scorecard, graph UI, or change queue", content)

    def test_no_claude_only_wiki_status_command_remains(self) -> None:
        self.assertFalse(Path(".claude/commands/wiki/status.md").exists())


if __name__ == "__main__":
    unittest.main()
