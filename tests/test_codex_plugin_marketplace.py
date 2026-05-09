import json
import unittest
from pathlib import Path


class CodexPluginMarketplaceTest(unittest.TestCase):
    def test_repo_marketplace_installs_report_wiki_plugin(self) -> None:
        marketplace_path = Path(".agents/plugins/marketplace.json")
        plugin_root = Path("plugins/report-wiki-portfolio")
        plugin_manifest_path = plugin_root / ".codex-plugin/plugin.json"
        command_path = plugin_root / "commands/wiki-status.md"

        self.assertTrue(marketplace_path.exists())
        self.assertTrue(plugin_manifest_path.exists())
        self.assertTrue(command_path.exists())

        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
        self.assertEqual("report-wiki-portfolio", marketplace["name"])
        self.assertEqual("Report Wiki Portfolio", marketplace["interface"]["displayName"])

        plugins = marketplace["plugins"]
        self.assertEqual(1, len(plugins))
        plugin = plugins[0]
        self.assertEqual("report-wiki-portfolio", plugin["name"])
        self.assertEqual(
            {"source": "local", "path": "./plugins/report-wiki-portfolio"},
            plugin["source"],
        )
        self.assertEqual("AVAILABLE", plugin["policy"]["installation"])
        self.assertEqual("ON_INSTALL", plugin["policy"]["authentication"])
        self.assertEqual("Productivity", plugin["category"])

    def test_readme_documents_codex_plugin_install_and_usage(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("codex plugin marketplace add .", readme)
        self.assertIn("/wiki:status", readme)
        self.assertIn("plugins/report-wiki-portfolio/commands/wiki-status.md", readme)


if __name__ == "__main__":
    unittest.main()
