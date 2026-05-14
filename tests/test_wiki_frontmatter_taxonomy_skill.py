import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WikiFrontmatterTaxonomySkillTest(unittest.TestCase):
    def test_taxonomy_skill_references_contract_without_vocab_duplication(self) -> None:
        skill = ROOT / ".codex/skills/wiki-frontmatter-taxonomy/SKILL.md"
        text = skill.read_text(encoding="utf-8")

        self.assertIn("scripts/wiki_gate_precheck.py", text)
        self.assertIn("wiki/config/frontmatter-taxonomy.yaml", text)
        self.assertIn("scripts/check_wiki_frontmatter.py", text)
        self.assertIn(
            "Run `python3 scripts/wiki_gate_precheck.py --mode frontmatter` first",
            text,
        )
        self.assertIn("Do not load the full taxonomy YAML or checker by default", text)
        self.assertIn("Do not duplicate taxonomy vocabulary", text)
        self.assertNotIn("agent-governance", text)
        self.assertNotIn("source-intake", text)


    def test_agents_routes_frontmatter_changes_to_taxonomy_skill(self) -> None:
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn(".codex/skills/wiki-frontmatter-taxonomy/SKILL.md", text)
        self.assertIn("run the repo frontmatter taxonomy checker", text)
