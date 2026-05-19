from __future__ import annotations

import argparse
import fnmatch
import shutil
from pathlib import Path

try:
    from scripts import llm_wiki_seed_manifest as manifest
except ModuleNotFoundError as exc:
    if exc.name != "scripts":
        raise
    import llm_wiki_seed_manifest as manifest

REPO_ROOT = Path(__file__).resolve().parents[1]
LOCAL_PROJECT_MARKERS = (
    "report-wiki-portfolio",
    "account-meeting-lore",
    "account-team-efficiency",
)


def build_seed(target: Path, force: bool) -> None:
    target = target.resolve()
    _validate_manifest()
    _prepare_target(target, force)

    for directory in manifest.COPY_DIRS:
        _copy_directory(directory, target)

    for file_path in manifest.COPY_FILES:
        _copy_file(file_path, target)

    for directory in manifest.CREATE_DIRS:
        target_dir = target / directory
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / ".gitkeep").touch()

    for file_path, content in manifest.GENERATED_TEXT_FILES.items():
        _write_generated_file(target, file_path, content)

    for file_path, content in manifest.GENERATED_SAMPLE_FILES.items():
        _assert_sanitized(content, file_path)
        _write_generated_file(target, file_path, content)

    _assert_excluded_paths_absent(target)


def _prepare_target(target: Path, force: bool) -> None:
    if target.exists() and any(target.iterdir()):
        if not force:
            raise ValueError(f"Refusing to write into non-empty target: {target}")
        _clear_target_contents(target)

    target.mkdir(parents=True, exist_ok=True)


def _clear_target_contents(target: Path) -> None:
    preserve_git = (target / ".git").exists()
    for child in target.iterdir():
        if preserve_git and child.name == ".git":
            continue
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def _copy_directory(relative_path: str, target: Path) -> None:
    source = _source_path(relative_path)
    destination = target / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=_ignore_excluded_paths)


def _copy_file(relative_path: str, target: Path) -> None:
    if is_excluded_path(relative_path):
        raise ValueError(f"Manifest copy file is excluded: {relative_path}")

    source = _source_path(relative_path)
    destination = target / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _write_generated_file(target: Path, relative_path: str, content: str) -> None:
    if is_excluded_path(relative_path):
        raise ValueError(f"Generated file path is excluded: {relative_path}")

    destination = target / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def _source_path(relative_path: str) -> Path:
    if _is_unsafe_relative_path(relative_path):
        raise ValueError(f"Unsafe manifest path: {relative_path}")

    source = REPO_ROOT / relative_path
    if not source.exists():
        raise FileNotFoundError(f"Manifest source path is missing: {relative_path}")
    if is_excluded_path(relative_path):
        raise ValueError(f"Manifest source path is excluded: {relative_path}")
    return source


def _validate_manifest() -> None:
    for directory in manifest.COPY_DIRS:
        source = _source_path(directory)
        if not source.is_dir():
            raise NotADirectoryError(
                f"Manifest copy directory is not a directory: {directory}"
            )

    for file_path in manifest.COPY_FILES:
        source = _source_path(file_path)
        if not source.is_file():
            raise FileNotFoundError(
                f"Manifest copy file is not a file: {file_path}"
            )

    for directory in manifest.CREATE_DIRS:
        _validate_writable_manifest_path(directory, "Create directory")

    for file_path in manifest.GENERATED_TEXT_FILES:
        _validate_writable_manifest_path(file_path, "Generated text file")

    for file_path, content in manifest.GENERATED_SAMPLE_FILES.items():
        _validate_writable_manifest_path(file_path, "Generated sample file")
        _assert_sanitized(content, file_path)


def _validate_writable_manifest_path(relative_path: str, label: str) -> None:
    if _is_unsafe_relative_path(relative_path):
        raise ValueError(f"{label} has unsafe manifest path: {relative_path}")
    if is_excluded_path(relative_path):
        raise ValueError(f"{label} path is excluded: {relative_path}")


def _ignore_excluded_paths(directory: str, names: list[str]) -> set[str]:
    ignored = set()
    root = Path(directory)

    for name in names:
        relative = (root / name).relative_to(REPO_ROOT).as_posix()
        if is_excluded_path(relative):
            ignored.add(name)

    return ignored


def _assert_excluded_paths_absent(target: Path) -> None:
    for path in target.rglob("*"):
        relative = path.relative_to(target).as_posix()
        if is_excluded_path(relative):
            raise AssertionError(f"Excluded path was created: {relative}")


def is_excluded_path(relative_path: str) -> bool:
    normalized = relative_path.replace("\\", "/")
    normalized = normalized.strip("/")

    for fragment in manifest.EXCLUDE_FRAGMENTS:
        normalized_fragment = fragment.replace("\\", "/").strip("/")
        if _matches_path_or_descendant(normalized, normalized_fragment):
            return True

    return any(
        fnmatch.fnmatch(normalized, pattern)
        for pattern in manifest.EXCLUDE_GLOBS
    )


def _matches_path_or_descendant(path: str, fragment: str) -> bool:
    return path == fragment or path.startswith(f"{fragment}/")


def _is_unsafe_relative_path(relative_path: str) -> bool:
    path = Path(relative_path)
    return path.is_absolute() or ".." in path.parts


def _assert_sanitized(content: str, relative_path: str) -> None:
    for marker in LOCAL_PROJECT_MARKERS:
        if marker in content:
            raise AssertionError(
                f"Generated sample file contains local project marker "
                f"{marker!r}: {relative_path}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a sanitized LLM-WIKI seed repository tree.",
    )
    parser.add_argument("--target-dir", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    build_seed(args.target_dir, force=args.force)


if __name__ == "__main__":
    main()
