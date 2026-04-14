from __future__ import annotations

import argparse
import re
from pathlib import Path


def _slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "untitled"


def _detect_language(text: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh-CN"
    return "en"


def generate_source_draft(source_file: Path, wiki_sources_dir: Path) -> Path:
    text = source_file.read_text(encoding="utf-8")
    language = _detect_language(text)
    title = source_file.stem.replace("_", " ").replace("-", " ").strip() or "untitled"
    slug = _slugify(source_file.stem)
    output_path = wiki_sources_dir / f"{slug}.md"

    english_notes = text.strip() if language == "en" else ""
    summary = (
        "待补充：请基于英文原文整理中文摘要。"
        if language == "en"
        else "待补充：请基于原始输入整理中文摘要。"
    )

    content = f"""---
title: {title}
type: source
source_path: inbox/{source_file.name}
source_type: note
language: {language}
domain: unclassified
audience: project
knowledge_level: working
period: evergreen
source_links: []
status: draft
updated_at: YYYY-MM-DD
ai_generated: true
---

# {title}

## Source Metadata

- Source system: inbox
- Source class: raw intake
- Ownership hint:
- Sync state: manual placeholder
- Intake confidence: low

## Audience Decision

- Source pages are usually for `self` or `project`, not `team`.
- Keep `knowledge_level: working` because source pages are evidence, not promoted team knowledge.

## Summary Context

Capture the minimum useful context even if the full body stays external.

## 中文摘要

{summary}

## English Notes

{english_notes}

## Reused By

- 待 agent 关联
"""
    wiki_sources_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def process_inbox(inbox_dir: Path, wiki_sources_dir: Path) -> list[Path]:
    output_paths: list[Path] = []
    supported_suffixes = {".md", ".txt"}

    for source_file in sorted(inbox_dir.iterdir()):
        if not source_file.is_file():
            continue
        if source_file.name.lower() == "readme.md":
            continue
        if source_file.suffix.lower() not in supported_suffixes:
            continue
        output_paths.append(generate_source_draft(source_file, wiki_sources_dir))

    return output_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate source drafts from inbox files.")
    parser.add_argument("--inbox", type=Path, default=Path("inbox"))
    parser.add_argument("--sources", type=Path, default=Path("wiki/sources"))
    args = parser.parse_args()

    output_paths = process_inbox(args.inbox, args.sources)
    for output_path in output_paths:
        print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
