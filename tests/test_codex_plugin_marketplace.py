import unittest
from pathlib import Path


class CodexPluginMarketplaceTest(unittest.TestCase):
    def test_readme_does_not_require_plugin_marketplace_for_wiki_runtime(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertNotIn("codex plugin marketplace add", readme)
        self.assertNotIn("plugin marketplace", readme.lower())
        self.assertNotIn("install those directories into", readme)

    def test_readme_documents_wiki_skill_usage(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")

        self.assertIn("$wiki-status", readme)
        self.assertIn("$wiki-query", readme)
        self.assertIn(".codex/skills/wiki-status/SKILL.md", readme)


if __name__ == "__main__":
    unittest.main()
