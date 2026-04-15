from __future__ import annotations

import argparse
import re
import zipfile
from html import unescape
from pathlib import Path
from xml.etree import ElementTree


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
    normalized = name.strip().lower().replace("_", "-")
    slug = re.sub(r"[^\w\-]+", "-", normalized, flags=re.UNICODE)
    slug = re.sub(r"[-_]+", "-", slug).strip("-")
    return slug or "untitled"


def _detect_language(text: str) -> str:
    if re.search(r"[\u4e00-\u9fff]", text):
        return "zh-CN"
    return "en"


def _strip_html(html: str) -> str:
    without_script = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.IGNORECASE)
    without_style = re.sub(r"<style[\s\S]*?</style>", " ", without_script, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", without_style)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def _extract_xml_text(xml_text: str) -> str:
    root = ElementTree.fromstring(xml_text)
    return " ".join(part.strip() for part in root.itertext() if part.strip())


def _read_source_text(source_file: Path) -> str:
    suffix = source_file.suffix.lower()
    if suffix in {".md", ".txt"}:
        return source_file.read_text(encoding="utf-8")
    if suffix == ".html":
        return _strip_html(source_file.read_text(encoding="utf-8", errors="ignore"))
    if suffix in {".docx", ".xlsx"}:
        with zipfile.ZipFile(source_file) as archive:
            xml_names = [
                name
                for name in archive.namelist()
                if name.endswith(".xml") and (name.startswith("word/") or name.startswith("xl/"))
            ]
            chunks: list[str] = []
            for name in xml_names:
                try:
                    chunks.append(_extract_xml_text(archive.read(name).decode("utf-8")))
                except (UnicodeDecodeError, ElementTree.ParseError):
                    continue
        return "\n".join(chunk for chunk in chunks if chunk.strip())
    return ""


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
    text = _read_source_text(source_file)
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
    related_source_ref: str | None = None,
) -> Path:
    text = _read_source_text(source_file)
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
    source_ref = related_source_ref or f"../sources/{slug}.md"

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
  - {source_ref}
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

- 来源页：{source_ref}
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
    supported_suffixes = {".md", ".txt", ".html", ".docx", ".xlsx"}
    existing_source_refs = _collect_existing_source_refs(wiki_sources_dir)
    existing_source_paths = set(existing_source_refs)
    existing_intake_paths = set(_collect_existing_source_refs(wiki_ops_dir)) if wiki_ops_dir is not None else set()

    for source_file in sorted(inbox_dir.rglob("*")):
        if not source_file.is_file():
            continue
        if source_file.name.lower() == "readme.md":
            continue
        if source_file.suffix.lower() not in supported_suffixes:
            continue
        source_path = f"inbox/{source_file.relative_to(inbox_dir).as_posix()}"
        if source_path not in existing_source_paths:
            output_paths.append(generate_source_draft(source_file, wiki_sources_dir, inbox_dir))
        if wiki_ops_dir is not None and source_path not in existing_intake_paths:
            output_paths.append(
                generate_intake_draft(
                    source_file,
                    wiki_ops_dir,
                    inbox_dir,
                    existing_source_refs.get(source_path),
                )
            )

    return output_paths


def _collect_existing_source_refs(target_dir: Path | None) -> dict[str, str]:
    if target_dir is None or not target_dir.exists():
        return {}
    source_refs: dict[str, str] = {}
    for markdown_file in target_dir.rglob("*.md"):
        content = markdown_file.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"^source_path:\s*(.+)\s*$", content, flags=re.MULTILINE)
        if match:
            source_path = match.group(1).strip()
            relative_ref = f"../sources/{markdown_file.name}"
            if target_dir.name == "sources":
                source_refs[source_path] = relative_ref
            else:
                source_refs[source_path] = markdown_file.name
    return source_refs


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
