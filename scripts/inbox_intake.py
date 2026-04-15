from __future__ import annotations

import argparse
import re
from pathlib import Path


MEETING_KEYWORDS = (
    "会议纪要",
    "纪要",
    "周会",
    "例会",
    "晨会",
    "晚会",
    "sync",
    "weekly sync",
    "meeting",
    "minutes",
    "review",
    "retro",
    "复盘",
    "对齐",
    "kickoff",
)

REPORT_KEYWORDS = (
    "周报",
    "月报",
    "日报",
    "汇报",
    "总结",
    "weekly report",
    "monthly report",
    "status report",
)

ATTACHMENT_KEYWORDS = (
    "截图",
    "附件",
    "录音",
    "导出",
    "export",
    "image",
    "attachment",
)


def _slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "untitled"


def _detect_language(text: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh-CN"
    return "en"


def _contains_keywords(text: str, keywords: tuple[str, ...]) -> bool:
    normalized = text.lower()
    return any(keyword.lower() in normalized for keyword in keywords)


def _infer_domain(source_file: Path, inbox_dir: Path) -> str:
    try:
        relative_parent = source_file.relative_to(inbox_dir).parent
    except ValueError:
        relative_parent = source_file.parent
    if str(relative_parent) in {".", ""}:
        return "unclassified"
    return _slugify(relative_parent.parts[0])


def _classify_source(source_file: Path, text: str) -> tuple[str, str, str]:
    haystack = f"{source_file.stem}\n{text}"
    if _contains_keywords(haystack, MEETING_KEYWORDS):
        return "meeting-note", "high", "meeting note"
    if _contains_keywords(haystack, REPORT_KEYWORDS):
        return "report", "medium", "report draft or report input"
    if _contains_keywords(haystack, ATTACHMENT_KEYWORDS):
        return "attachment", "medium", "supporting attachment"
    return "note", "low", "raw intake"


def generate_source_draft(
    source_file: Path,
    wiki_sources_dir: Path,
    inbox_dir: Path | None = None,
) -> Path:
    text = source_file.read_text(encoding="utf-8")
    language = _detect_language(text)
    source_type, confidence, source_class = _classify_source(source_file, text)
    title = source_file.stem.replace("_", " ").replace("-", " ").strip() or "untitled"
    inbox_root = inbox_dir or source_file.parent
    source_path = source_file.relative_to(inbox_root).as_posix()
    domain = _infer_domain(source_file, inbox_root)
    slug_parts = list(Path(source_path).parts)
    if slug_parts:
        slug_parts[-1] = Path(slug_parts[-1]).stem
    slug = _slugify("-".join(slug_parts))
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
source_path: inbox/{source_path}
source_type: {source_type}
language: {language}
domain: {domain}
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
- Source class: {source_class}
- Ownership hint:
- Sync state: manual placeholder
- Intake confidence: {confidence}

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


def generate_intake_draft(
    source_file: Path,
    wiki_ops_dir: Path,
    inbox_dir: Path | None = None,
) -> Path:
    text = source_file.read_text(encoding="utf-8")
    language = _detect_language(text)
    source_type, confidence, source_class = _classify_source(source_file, text)
    title = source_file.stem.replace("_", " ").replace("-", " ").strip() or "untitled"
    inbox_root = inbox_dir or source_file.parent
    source_path = source_file.relative_to(inbox_root).as_posix()
    domain = _infer_domain(source_file, inbox_root)
    slug_parts = list(Path(source_path).parts)
    if slug_parts:
        slug_parts[-1] = Path(slug_parts[-1]).stem
    slug = _slugify("-".join(slug_parts))
    output_path = wiki_ops_dir / f"{slug}-intake.md"

    summary = (
        "待补充：请基于英文原文整理这条输入的中文操作摘要。"
        if language == "en"
        else "待补充：请基于原始输入整理这条输入的中文操作摘要。"
    )
    english_notes = text.strip() if language == "en" else ""

    content = f"""---
title: {title}
type: intake
language: {language}
source_path: inbox/{source_path}
source_type: {source_type}
audience: self
knowledge_level: working
domain: {domain}
period: evergreen
confidence: {confidence}
status: active
updated_at: YYYY-MM-DD
ai_generated: true
related_sources:
  - ../sources/{slug}.md
related_focus_threads: []
related_reminders: []
---

# {title}

## 输入摘要

{summary}

## 输入类型判断

- 行为类型：待判断
- 来源类型：{source_class}
- 受众判断：self
- 当前置信度：{confidence}

## 建议关联

- 来源页：../sources/{slug}.md
- 主线页：
- 提醒页：

## 待确认项

- 待 agent 进一步判断是否应升级为 focus-thread、reminder 或 codex-handoff

## English Notes

{english_notes}
"""
    wiki_ops_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def process_inbox(
    inbox_dir: Path,
    wiki_sources_dir: Path,
    wiki_ops_dir: Path | None = None,
) -> list[Path]:
    output_paths: list[Path] = []
    supported_suffixes = {".md", ".txt"}

    for source_file in sorted(inbox_dir.rglob("*")):
        if not source_file.is_file():
            continue
        if source_file.name.lower() == "readme.md":
            continue
        if source_file.suffix.lower() not in supported_suffixes:
            continue
        output_paths.append(generate_source_draft(source_file, wiki_sources_dir, inbox_dir))
        if wiki_ops_dir is not None:
            output_paths.append(generate_intake_draft(source_file, wiki_ops_dir, inbox_dir))

    return output_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate source drafts from inbox files.")
    parser.add_argument("--inbox", type=Path, default=Path("inbox"))
    parser.add_argument("--sources", type=Path, default=Path("wiki/sources"))
    parser.add_argument("--ops", type=Path, default=Path("wiki/ops"))
    args = parser.parse_args()

    output_paths = process_inbox(args.inbox, args.sources, args.ops)
    for output_path in output_paths:
        print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
