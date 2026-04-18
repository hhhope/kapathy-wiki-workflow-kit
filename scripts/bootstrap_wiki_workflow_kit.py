#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSET_ROOT = REPO_ROOT / "scripts" / "bootstrap_assets"

WIKI_FILES = [
    "wiki/index.md",
    "wiki/ai-workflow.md",
    "wiki/ops/index.md",
    "wiki/reports/index.md",
    "wiki/sources/index.md",
    "wiki/adr/index.md",
]

WIKI_DIRS = [
    "wiki/templates",
    "wiki/examples",
]

ADR_FILES = [
    "wiki/adr/0001-repository-default-workflow-changes-require-openspec.md",
    "wiki/adr/0002-stable-decisions-live-in-wiki-adr.md",
    "wiki/adr/0009-explore-trace-before-openspec-explore.md",
    "wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md",
]

ROOT_FILES = [
    "inbox/README.md",
]

SKILL_DIRS = [
    ".codex/skills/material-collaboration-defaults",
    ".codex/skills/meeting-note-output",
    ".codex/skills/openspec-explore",
    ".codex/skills/openspec-propose",
    ".codex/skills/openspec-apply-change",
    ".codex/skills/openspec-archive-change",
    ".codex/skills/weixin-reader",
    ".codex/skills/project-management-weekly-skill",
    ".codex/skills/clarify-before-acting",
    ".codex/skills/simplicity-first",
    ".codex/skills/surgical-changes",
    ".codex/skills/verify-before-claiming",
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap the wiki workflow kit.")
    parser.add_argument("--project-name", required=True, help="Project display name.")
    parser.add_argument("--target-dir", required=True, help="Target directory to initialize.")
    parser.add_argument("--owner", default="owner", help="Owner name for PROJECT.md.")
    parser.add_argument("--with-obsidian", dest="with_obsidian", action="store_true")
    parser.add_argument("--without-obsidian", dest="with_obsidian", action="store_false")
    parser.add_argument("--with-openspec", dest="with_openspec", action="store_true")
    parser.add_argument("--without-openspec", dest="with_openspec", action="store_false")
    parser.add_argument("--with-examples", dest="with_examples", action="store_true")
    parser.add_argument("--without-examples", dest="with_examples", action="store_false")
    parser.set_defaults(with_obsidian=True, with_openspec=True, with_examples=True)
    return parser.parse_args(argv)


def slugify(name: str) -> str:
    slug = name.strip().lower().replace(" ", "-")
    return "".join(ch for ch in slug if ch.isalnum() or ch == "-").strip("-") or "wiki-workflow-kit"


def ensure_clean_target(target: Path) -> None:
    if target.exists():
        contents = list(target.iterdir())
        if contents:
            raise SystemExit(f"Target directory is not empty: {target}")
    else:
        target.mkdir(parents=True, exist_ok=True)


def render_template(template_path: Path, replacements: dict[str, str]) -> str:
    text = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def write_text(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def copy_file(rel_path: str, target_root: Path) -> None:
    source = REPO_ROOT / rel_path
    target = target_root / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_dir(rel_path: str, target_root: Path) -> None:
    source = REPO_ROOT / rel_path
    target = target_root / rel_path
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)


def install_project_anchor(target_root: Path, project_name: str, owner: str, project_slug: str) -> None:
    content = f"""---
project: {project_slug}
status: active
owner: {owner}
source_of_truth: openspec
---

# {project_name}

## Purpose

This repository uses the wiki workflow kit to organize source material, operating traces, reports, and stable decisions in one markdown workspace.

## Operating Model

- `wiki/` is the durable knowledge and workflow workspace.
- `openspec/` governs workflow-level changes.
- `AGENTS.md` and `CLAUDE.md` are the AI entrypoints.
- Obsidian is the default human-facing workspace.
"""
    write_text(target_root / "PROJECT.md", content)


def install_entrypoints(target_root: Path, project_name: str, project_slug: str) -> None:
    replacements = {"PROJECT_NAME": project_name, "PROJECT_SLUG": project_slug}
    agents = render_template(ASSET_ROOT / "AGENTS.md.template", replacements)
    claude = render_template(ASSET_ROOT / "CLAUDE.md.template", replacements)
    write_text(target_root / "AGENTS.md", agents)
    write_text(target_root / "CLAUDE.md", claude)


def install_wiki(target_root: Path, with_examples: bool) -> None:
    for rel_path in ROOT_FILES:
        copy_file(rel_path, target_root)
    for rel_path in WIKI_FILES:
        copy_file(rel_path, target_root)
    for rel_path in WIKI_DIRS:
        if rel_path == "wiki/examples" and not with_examples:
            continue
        copy_dir(rel_path, target_root)
    for rel_path in ADR_FILES:
        copy_file(rel_path, target_root)


def install_skills(target_root: Path) -> None:
    for rel_path in SKILL_DIRS:
        copy_dir(rel_path, target_root)


def install_openspec(target_root: Path) -> None:
    copy_file("openspec/config.yaml", target_root)
    (target_root / "openspec" / "specs").mkdir(parents=True, exist_ok=True)
    (target_root / "openspec" / "changes" / "archive").mkdir(parents=True, exist_ok=True)


def install_obsidian(target_root: Path) -> None:
    obsidian_root = target_root / ".obsidian"
    obsidian_root.mkdir(parents=True, exist_ok=True)
    for path in (ASSET_ROOT / "obsidian").iterdir():
        shutil.copy2(path, obsidian_root / path.name)


def install_scripts(target_root: Path) -> None:
    target_scripts = target_root / "scripts"
    target_scripts.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / "scripts" / "inbox_intake.py", target_scripts / "inbox_intake.py")
    shutil.copy2(REPO_ROOT / "scripts" / "verify_wiki_workflow_kit.py", target_scripts / "verify_wiki_workflow_kit.py")


def print_next_steps(target_root: Path) -> None:
    print("Initialized wiki workflow kit:")
    print(f"- target: {target_root}")
    print("- next: review inbox/README.md and wiki/index.md for the intake flow")
    print("- next: open the repository in Obsidian")
    print("- next: review PROJECT.md, AGENTS.md, CLAUDE.md")
    print("- next: run scripts/verify_wiki_workflow_kit.py")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    target_root = Path(args.target_dir).resolve()
    project_slug = slugify(args.project_name)

    ensure_clean_target(target_root)
    install_project_anchor(target_root, args.project_name, args.owner, project_slug)
    install_entrypoints(target_root, args.project_name, project_slug)
    install_wiki(target_root, args.with_examples)
    install_skills(target_root)
    install_scripts(target_root)
    if args.with_openspec:
        install_openspec(target_root)
    if args.with_obsidian:
        install_obsidian(target_root)
    print_next_steps(target_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
