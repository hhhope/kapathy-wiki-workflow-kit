from __future__ import annotations

from pathlib import Path

import pytest

from scripts import llm_wiki_seed_manifest as manifest
from scripts.build_llm_wiki_seed import build_seed, is_excluded_path
from scripts.verify_llm_wiki_seed import verify_seed


def test_build_seed_creates_required_structure_under_target(
    tmp_path: Path,
) -> None:
    target = tmp_path / "seed"

    build_seed(target, force=False)

    for copied_dir in manifest.COPY_DIRS:
        assert (target / copied_dir).is_dir()

    for copied_file in manifest.COPY_FILES:
        assert (target / copied_file).is_file()

    for created_dir in manifest.CREATE_DIRS:
        path = target / created_dir
        assert path.is_dir()
        assert (path / ".gitkeep").is_file()

    for generated_file in {
        *manifest.GENERATED_TEXT_FILES,
        *manifest.GENERATED_SAMPLE_FILES,
    }:
        assert (target / generated_file).is_file()


def test_build_seed_output_passes_seed_verifier(tmp_path: Path) -> None:
    target = tmp_path / "seed"

    build_seed(target, force=False)

    assert verify_seed(target) == 0


def test_verify_seed_short_circuits_when_target_is_missing(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    result = verify_seed(tmp_path / "missing")

    output = capsys.readouterr().out
    assert result == 1
    assert "missing target directory" in output
    assert "missing required file" not in output
    assert "missing required directory" not in output


def test_verify_seed_short_circuits_when_target_is_not_directory(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    target = tmp_path / "not-a-dir"
    target.write_text("not a directory\n", encoding="utf-8")

    result = verify_seed(target)

    output = capsys.readouterr().out
    assert result == 1
    assert "target is not a directory" in output
    assert "missing required file" not in output
    assert "missing required directory" not in output


def test_build_seed_writes_sanitized_examples_without_local_project_names(
    tmp_path: Path,
) -> None:
    target = tmp_path / "seed"

    build_seed(target, force=False)

    generated_text = "\n".join(
        (target / path).read_text(encoding="utf-8")
        for path in manifest.GENERATED_SAMPLE_FILES
    )

    assert "Sanitized seed note" in generated_text
    assert "report-wiki-portfolio" not in generated_text
    assert "account-meeting-lore" not in generated_text
    assert "account-team-efficiency" not in generated_text


def test_build_seed_refuses_non_empty_target_without_force(
    tmp_path: Path,
) -> None:
    target = tmp_path / "seed"
    target.mkdir()
    (target / "existing.txt").write_text("keep me\n", encoding="utf-8")

    with pytest.raises(ValueError, match="non-empty"):
        build_seed(target, force=False)

    assert (target / "existing.txt").read_text(encoding="utf-8") == "keep me\n"


def test_build_seed_force_preserves_existing_git_directory(
    tmp_path: Path,
) -> None:
    target = tmp_path / "seed"
    git_dir = target / ".git"
    git_dir.mkdir(parents=True)
    (git_dir / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
    (target / "stale.txt").write_text("remove me\n", encoding="utf-8")

    build_seed(target, force=True)

    assert (git_dir / "HEAD").read_text(encoding="utf-8") == "ref: refs/heads/main\n"
    assert not (target / "stale.txt").exists()
    assert (target / "PROJECT.md").is_file()


def test_build_seed_force_unlinks_directory_symlink(
    tmp_path: Path,
) -> None:
    target = tmp_path / "seed"
    linked_dir = tmp_path / "linked"
    linked_dir.mkdir()
    target.mkdir()
    symlink = target / "linked-dir"
    symlink.symlink_to(linked_dir, target_is_directory=True)

    build_seed(target, force=True)

    assert linked_dir.is_dir()
    assert not symlink.exists()
    assert (target / "PROJECT.md").is_file()


def test_build_seed_preserves_forced_target_when_manifest_source_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "seed"
    target.mkdir()
    existing_file = target / "existing.txt"
    existing_file.write_text("keep me\n", encoding="utf-8")
    monkeypatch.setattr(
        manifest,
        "COPY_FILES",
        [*manifest.COPY_FILES, "definitely/missing/file.md"],
    )

    with pytest.raises(FileNotFoundError):
        build_seed(target, force=True)

    assert existing_file.read_text(encoding="utf-8") == "keep me\n"


def test_exclusion_matching_requires_exact_path_or_directory_boundary() -> None:
    assert is_excluded_path("wiki/.obsidian")
    assert is_excluded_path("wiki/.obsidian/workspace.json")
    assert is_excluded_path("openspec/changes/archive")
    assert is_excluded_path("openspec/changes/archive/old-change/tasks.md")
    assert is_excluded_path("wiki/reports/reports.zip")
    assert is_excluded_path("wiki/reports/private-bundle.zip")

    assert not is_excluded_path("wiki/.obsidian-notes")
    assert not is_excluded_path("wiki/.obsidian-notes/index.md")
    assert not is_excluded_path("openspec/changes/archive-notes")
    assert not is_excluded_path("openspec/changes/archive-notes/summary.md")
