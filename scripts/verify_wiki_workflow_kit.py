#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


ALWAYS_REQUIRED_PATHS = [
    "README.md",
    "PROJECT.md",
    "AGENTS.md",
    "CLAUDE.md",
    "inbox/README.md",
    "wiki/index.md",
    "wiki/ai-workflow.md",
    "wiki/ops/index.md",
    "wiki/reports/index.md",
    "wiki/sources/index.md",
    "wiki/adr/index.md",
    "wiki/templates",
    ".codex/skills/material-collaboration-defaults/SKILL.md",
    ".codex/skills/meeting-note-output/SKILL.md",
    ".codex/skills/openspec-explore/SKILL.md",
    ".codex/skills/weixin-reader/SKILL.md",
    "scripts/inbox_intake.py",
    "scripts/verify_wiki_workflow_kit.py",
]

OPENSPEC_REQUIRED_PATHS = [
    "openspec/config.yaml",
    "openspec/changes/archive",
]

OBSIDIAN_REQUIRED_PATHS = [
    ".obsidian/core-plugins.json",
]

EXAMPLE_REQUIRED_PATHS = [
    "wiki/examples/index.md",
]


@dataclass
class VerificationResult:
    missing_required: list[str]
    missing_optional: list[str]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify an installed wiki workflow kit.")
    parser.add_argument("--root", default=".", help="Root directory to verify.")
    parser.add_argument("--with-openspec", dest="with_openspec", action="store_true")
    parser.add_argument("--without-openspec", dest="with_openspec", action="store_false")
    parser.add_argument("--with-obsidian", dest="with_obsidian", action="store_true")
    parser.add_argument("--without-obsidian", dest="with_obsidian", action="store_false")
    parser.add_argument("--with-examples", dest="with_examples", action="store_true")
    parser.add_argument("--without-examples", dest="with_examples", action="store_false")
    parser.set_defaults(with_openspec=True, with_obsidian=True, with_examples=True)
    return parser.parse_args(argv)


def _missing_paths(root: Path, rel_paths: list[str]) -> list[str]:
    return [path for path in rel_paths if not (root / path).exists()]


def verify_installation(
    root: Path,
    *,
    with_openspec: bool,
    with_obsidian: bool,
    with_examples: bool,
) -> VerificationResult:
    missing_required = _missing_paths(root, ALWAYS_REQUIRED_PATHS)
    if with_openspec:
        missing_required.extend(_missing_paths(root, OPENSPEC_REQUIRED_PATHS))
    if with_obsidian:
        missing_required.extend(_missing_paths(root, OBSIDIAN_REQUIRED_PATHS))
    if with_examples:
        missing_required.extend(_missing_paths(root, EXAMPLE_REQUIRED_PATHS))

    missing_optional: list[str] = []
    if not with_openspec:
        missing_optional.extend(_missing_paths(root, OPENSPEC_REQUIRED_PATHS))
    if not with_obsidian:
        missing_optional.extend(_missing_paths(root, OBSIDIAN_REQUIRED_PATHS))
    if not with_examples:
        missing_optional.extend(_missing_paths(root, EXAMPLE_REQUIRED_PATHS))

    return VerificationResult(
        missing_required=sorted(missing_required),
        missing_optional=sorted(missing_optional),
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    result = verify_installation(
        root,
        with_openspec=args.with_openspec,
        with_obsidian=args.with_obsidian,
        with_examples=args.with_examples,
    )
    if result.missing_required:
        print("Missing required kit paths:")
        for path in result.missing_required:
            print(f"- {path}")
        if result.missing_optional:
            print("\nMissing optional paths for disabled surfaces:")
            for path in result.missing_optional:
                print(f"- {path}")
        return 1
    if result.missing_optional:
        print("Optional surfaces not installed for the selected mode:")
        for path in result.missing_optional:
            print(f"- {path}")
    print("Wiki workflow kit verification passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
