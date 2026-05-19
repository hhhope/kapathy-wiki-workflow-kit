#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path

try:
    from scripts import llm_wiki_seed_manifest as manifest
except ModuleNotFoundError as exc:
    if exc.name != "scripts":
        raise
    import llm_wiki_seed_manifest as manifest


REQUIRED_MARKERS = {
    "README.md": [
        "Runnable seed repository",
        "This first migration intentionally keeps README minimal",
    ],
    "AGENTS.md": [
        "LLM-maintained wiki seed",
        "Use the medical loop for wiki maintenance",
    ],
    "wiki/sources/lixiang-interview-reading-sanitized.md": [
        "Sanitized seed note",
        "public-source learning shape",
    ],
    "wiki/ops/llm-wiki-self-evolution-medical-loop.md": [
        "doctor diagnoses; review confirms",
        "archive preserves",
    ],
}


def verify_seed(target: Path) -> int:
    target = target.resolve()
    failures: list[str] = []

    if not target.exists():
        failures.append(f"missing target directory: {target}")
    elif not target.is_dir():
        failures.append(f"target is not a directory: {target}")

    if failures:
        _print_failures(failures)
        return 1

    _check_required_paths(target, failures)
    _check_forbidden_paths(target, failures)
    _check_required_markers(target, failures)

    if failures:
        _print_failures(failures)
        return 1

    print(f"OK: seed verification passed for {target}")
    return 0


def _print_failures(failures: list[str]) -> None:
    for failure in failures:
        print(f"FAIL: {failure}")


def _check_required_paths(target: Path, failures: list[str]) -> None:
    required_files = {
        *manifest.GENERATED_TEXT_FILES,
        *manifest.COPY_FILES,
        *manifest.GENERATED_SAMPLE_FILES,
    }
    required_dirs = {*manifest.COPY_DIRS, *manifest.CREATE_DIRS}

    for relative_path in sorted(required_files):
        path = target / relative_path
        if not path.is_file():
            failures.append(f"missing required file: {relative_path}")

    for relative_path in sorted(required_dirs):
        path = target / relative_path
        if not path.is_dir():
            failures.append(f"missing required directory: {relative_path}")

    for relative_path in sorted(manifest.CREATE_DIRS):
        path = target / relative_path / ".gitkeep"
        if not path.is_file():
            failures.append(f"missing required file: {relative_path}/.gitkeep")

    for relative_path in sorted(manifest.COPY_DIRS):
        path = target / relative_path / "SKILL.md"
        if relative_path.startswith(".codex/skills/") and not path.is_file():
            failures.append(f"missing required skill entry: {relative_path}/SKILL.md")


def _check_forbidden_paths(target: Path, failures: list[str]) -> None:
    if not target.exists() or not target.is_dir():
        return

    for path in sorted(target.rglob("*")):
        relative_path = path.relative_to(target).as_posix()
        if _is_forbidden_path(relative_path):
            failures.append(f"forbidden path present: {relative_path}")


def _check_required_markers(target: Path, failures: list[str]) -> None:
    for relative_path, markers in REQUIRED_MARKERS.items():
        path = target / relative_path
        if not path.is_file():
            continue

        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                failures.append(
                    f"missing text marker in {relative_path}: {marker!r}"
                )


def _is_forbidden_path(relative_path: str) -> bool:
    normalized = relative_path.replace("\\", "/").strip("/")

    for fragment in manifest.EXCLUDE_FRAGMENTS:
        normalized_fragment = fragment.replace("\\", "/").strip("/")
        if normalized == normalized_fragment or normalized.startswith(
            f"{normalized_fragment}/"
        ):
            return True

    return any(
        fnmatch.fnmatch(normalized, pattern.replace("\\", "/").strip("/"))
        for pattern in manifest.EXCLUDE_GLOBS
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify a generated LLM-WIKI seed repository tree.",
    )
    parser.add_argument("--target-dir", default=".", type=Path)
    args = parser.parse_args()

    raise SystemExit(verify_seed(args.target_dir))


if __name__ == "__main__":
    main()
