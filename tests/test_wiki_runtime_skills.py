import re
import unittest
from pathlib import Path


SKILL_SOURCE_ROOT = Path("plugins/report-wiki-portfolio/skills")

WIKI_SKILLS = {
    "wiki-status": "plugins/report-wiki-portfolio/commands/wiki-status.md",
    "wiki-manifest": "plugins/report-wiki-portfolio/commands/wiki-manifest.md",
    "wiki-inbox": "plugins/report-wiki-portfolio/commands/wiki-inbox.md",
    "wiki-query": "plugins/report-wiki-portfolio/commands/wiki-query.md",
    "wiki-graph": "plugins/report-wiki-portfolio/commands/wiki-graph.md",
    "wiki-scorecard": "plugins/report-wiki-portfolio/commands/wiki-scorecard.md",
    "wiki-route": "plugins/report-wiki-portfolio/commands/wiki-route.md",
    "wiki-context": "plugins/report-wiki-portfolio/commands/wiki-context.md",
    "wiki-apply": "plugins/report-wiki-portfolio/commands/wiki-apply.md",
    "wiki-queue": "plugins/report-wiki-portfolio/commands/wiki-queue.md",
}


class WikiRuntimeSkillsTest(unittest.TestCase):
    def test_wiki_runtime_skill_sources_exist_with_plain_wiki_names(self) -> None:
        for skill_name, command_path in WIKI_SKILLS.items():
            with self.subTest(skill=skill_name):
                skill_path = SKILL_SOURCE_ROOT / skill_name / "SKILL.md"
                self.assertTrue(skill_path.exists(), skill_path)
                content = skill_path.read_text(encoding="utf-8")
                self.assertRegex(content, rf"(?m)^name: {re.escape(skill_name)}$")
                self.assertIn(command_path, content)
                self.assertNotIn("name: report-wiki-portfolio:", content)

    def test_wiki_runtime_skills_preserve_boundaries(self) -> None:
        for skill_name in WIKI_SKILLS:
            with self.subTest(skill=skill_name):
                content = (
                    SKILL_SOURCE_ROOT / skill_name / "SKILL.md"
                ).read_text(encoding="utf-8").lower()
                self.assertIn("do not create, modify, archive, or queue openspec changes", content)
                self.assertIn("do not mark openspec tasks complete", content)
                self.assertIn("do not execute queued work", content)

    def test_readme_documents_wiki_skill_surface_not_custom_slash_runtime(self) -> None:
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("$wiki-status", readme)
        self.assertIn("$wiki-query", readme)
        self.assertIn("plugins/report-wiki-portfolio/skills/wiki-status/SKILL.md", readme)
        self.assertNotIn("This repo also ships a repo-local Codex plugin", readme)


if __name__ == "__main__":
    unittest.main()
