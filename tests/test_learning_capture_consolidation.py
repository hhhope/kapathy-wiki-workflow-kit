from __future__ import annotations

from pathlib import Path


def test_readme_learning_is_not_a_separate_active_skill() -> None:
    assert not Path(".codex/skills/readme-learning-capture/SKILL.md").exists()


def test_repo_readme_module_is_self_contained_under_learning_capture() -> None:
    repo_module = Path(".codex/skills/learning-capture/references/repo-readme.md")
    text = repo_module.read_text(encoding="utf-8")

    assert ".codex/skills/readme-learning-capture" not in text
    assert "repo-readme-scorecard.md" in text
    assert "repo-readme-pressure-scenarios.md" in text

    assert Path(
        ".codex/skills/learning-capture/references/repo-readme-scorecard.md"
    ).is_file()
    assert Path(
        ".codex/skills/learning-capture/references/repo-readme-pressure-scenarios.md"
    ).is_file()


def test_active_manifests_do_not_require_retired_readme_skill() -> None:
    active_paths = [
        Path("scripts/llm_wiki_seed_manifest.py"),
        Path("tests/test_llm_wiki_seed_manifest.py"),
    ]
    combined = "\n".join(path.read_text(encoding="utf-8") for path in active_paths)

    assert ".codex/skills/readme-learning-capture" not in combined


def test_learning_capture_controller_links_matrix_references_and_stays_compact() -> None:
    skill = Path(".codex/skills/learning-capture/SKILL.md")
    text = skill.read_text(encoding="utf-8")

    assert "references/levels.md" in text
    assert "references/learning-types.md" in text
    assert "references/research-methods.md" in text
    assert "references/evidence-strength.md" in text
    assert "references/output-contract.md" in text
    assert "references/source-queue.md" in text
    assert "references/public-writing-method.md" in text
    assert len(text.splitlines()) <= 140
