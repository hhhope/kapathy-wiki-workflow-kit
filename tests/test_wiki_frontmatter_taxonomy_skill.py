from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_taxonomy_skill_references_contract_without_vocab_duplication() -> None:
    skill = ROOT / ".codex/skills/wiki-frontmatter-taxonomy/SKILL.md"
    text = skill.read_text(encoding="utf-8")

    assert "wiki/config/frontmatter-taxonomy.yaml" in text
    assert "scripts/check_wiki_frontmatter.py" in text
    assert "Do not duplicate taxonomy vocabulary" in text
    assert "agent-governance" not in text
    assert "source-intake" not in text


def test_agents_routes_frontmatter_changes_to_taxonomy_skill() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert ".codex/skills/wiki-frontmatter-taxonomy/SKILL.md" in text
    assert "run the repo frontmatter taxonomy checker" in text
