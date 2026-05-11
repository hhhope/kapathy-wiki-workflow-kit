import unittest
from pathlib import Path


class CodexPluginMarketplaceTest(unittest.TestCase):
    def test_repo_does_not_publish_runtime_skills_through_plugin_metadata(self) -> None:
        self.assertFalse(Path(".agents/plugins/marketplace.json").exists())
        self.assertFalse(Path("plugins/report-wiki-portfolio/.codex-plugin/plugin.json").exists())
        self.assertFalse(Path("plugins/report-wiki-portfolio/skills").exists())

    def test_readme_does_not_require_plugin_marketplace_for_wiki_runtime(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertNotIn("codex plugin marketplace add", readme)
        self.assertNotIn("install those directories into", readme)
        self.assertIn("Do not reintroduce repo plugin marketplace metadata", readme)

    def test_readme_documents_wiki_skill_usage(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("$wiki-status", readme)
        self.assertIn("$wiki-query", readme)
        self.assertIn(".codex/skills/wiki-status/SKILL.md", readme)


if __name__ == "__main__":
    unittest.main()
