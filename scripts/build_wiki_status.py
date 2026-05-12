#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.extract_wiki_graph import parse_frontmatter
from scripts.wiki_product_status import build_product_status, relation_fields_from_meta


DEFAULT_OUTPUT_DIR = Path("wiki/status")
GENERATED_STATUS_DIR = "wiki/status/"
TASK_PATTERN = re.compile(r"^\s*-\s+\[(?P<mark>[ xX])\]\s+")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _wiki_section(rel_path: str) -> str:
    parts = rel_path.split("/")
    if len(parts) >= 3:
        return "/".join(parts[:2])
    if len(parts) == 2:
        return "wiki/root"
    return "wiki"


def _normal_source_path(value: object) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    path = value.strip()
    if path.startswith("inbox/"):
        return path
    return f"inbox/{path}"


def _collect_wiki_pages(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    wiki_dir = root / "wiki"
    pages: list[dict[str, Any]] = []
    source_records: list[dict[str, Any]] = []
    if not wiki_dir.exists():
        return pages, source_records

    for path in sorted(wiki_dir.rglob("*.md")):
        rel = _relative(path, root)
        if rel.startswith(GENERATED_STATUS_DIR):
            continue
        text = path.read_text(encoding="utf-8")
        meta, _body = parse_frontmatter(text)
        record = {
            "path": rel,
            "section": _wiki_section(rel),
            "sha256": _sha256(path),
            "bytes": path.stat().st_size,
            "title": meta.get("title"),
            "canonical_object": meta.get("canonical_object"),
            "artifact_type": meta.get("artifact_type"),
            "status": meta.get("status"),
            **relation_fields_from_meta(meta),
        }
        pages.append(record)

        if rel.startswith("wiki/sources/") and path.name != "index.md":
            source_records.append(
                {
                    "path": rel,
                    "source_path": _normal_source_path(meta.get("source_path")),
                    "source_type": meta.get("source_type"),
                    "domain": meta.get("domain"),
                    "status": meta.get("status"),
                }
            )

    return pages, source_records


def _collect_inbox_files(root: Path, source_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    inbox_dir = root / "inbox"
    represented_paths = {
        record["source_path"]
        for record in source_records
        if isinstance(record.get("source_path"), str)
    }
    inbox_files: list[dict[str, Any]] = []
    if not inbox_dir.exists():
        return inbox_files

    for path in sorted(item for item in inbox_dir.rglob("*") if item.is_file()):
        if path.name.lower() == "readme.md":
            continue
        rel = _relative(path, root)
        inbox_files.append(
            {
                "path": rel,
                "sha256": _sha256(path),
                "bytes": path.stat().st_size,
                "represented_by_source": rel in represented_paths,
            }
        )
    return inbox_files


def _parse_task_counts(tasks_path: Path) -> tuple[int, int]:
    done = 0
    open_count = 0
    for line in tasks_path.read_text(encoding="utf-8").splitlines():
        match = TASK_PATTERN.match(line)
        if not match:
            continue
        if match.group("mark").lower() == "x":
            done += 1
        else:
            open_count += 1
    return done, open_count


def _collect_openspec_changes(root: Path) -> list[dict[str, Any]]:
    changes_dir = root / "openspec" / "changes"
    changes: list[dict[str, Any]] = []
    if not changes_dir.exists():
        return changes

    for tasks_path in sorted(changes_dir.glob("*/tasks.md")):
        change_id = tasks_path.parent.name
        if change_id == "archive":
            continue
        done, open_count = _parse_task_counts(tasks_path)
        total = done + open_count
        state = "complete" if total > 0 and open_count == 0 else "active"
        changes.append(
            {
                "change_id": change_id,
                "state": state,
                "done_tasks": done,
                "open_tasks": open_count,
                "total_tasks": total,
                "tasks_path": _relative(tasks_path, root),
            }
        )
    return changes


def build_manifest(root: Path | str) -> dict[str, Any]:
    root_path = Path(root).resolve()
    pages, source_records = _collect_wiki_pages(root_path)
    inbox_files = _collect_inbox_files(root_path, source_records)
    changes = _collect_openspec_changes(root_path)
    section_counts = Counter(page["section"] for page in pages)
    pending_inbox_files = [
        item["path"]
        for item in inbox_files
        if not item["represented_by_source"]
    ]
    active_changes = [item for item in changes if item["state"] == "active"]
    complete_changes = [item for item in changes if item["state"] == "complete"]
    product_status = build_product_status(pages, inbox_files, changes)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": root_path.as_posix(),
        "summary": {
            "wiki_page_count": len(pages),
            "source_record_count": len(source_records),
            "inbox_file_count": len(inbox_files),
            "pending_inbox_count": len(pending_inbox_files),
            "active_change_count": len(active_changes),
            "complete_change_count": len(complete_changes),
            "wiki_sections": dict(sorted(section_counts.items())),
        },
        "wiki_pages": pages,
        "source_records": source_records,
        "inbox_files": inbox_files,
        "pending_inbox_files": pending_inbox_files,
        "openspec_changes": changes,
        "product_status": product_status,
    }


def _markdown_table(headers: list[str], rows: list[list[object]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(str(cell) for cell in row) + " |" for row in rows)
    return lines


def render_status_markdown(manifest: dict[str, Any]) -> str:
    summary = manifest["summary"]
    lines = [
        "# Wiki Status",
        "",
        f"Generated at: `{manifest['generated_at']}`",
        "",
        "## Summary",
        "",
        * _markdown_table(
            ["Metric", "Value"],
            [
                ["Wiki pages", summary["wiki_page_count"]],
                ["Source records", summary["source_record_count"]],
                ["Inbox files", summary["inbox_file_count"]],
                ["Pending inbox files", summary["pending_inbox_count"]],
                ["Active OpenSpec changes", summary["active_change_count"]],
                ["Complete active-dir changes", summary["complete_change_count"]],
            ],
        ),
        "",
        "## Wiki Sections",
        "",
    ]
    section_rows = [
        [section, count]
        for section, count in sorted(summary["wiki_sections"].items())
    ]
    lines.extend(_markdown_table(["Section", "Pages"], section_rows or [["none", 0]]))
    lines.extend(["", "## Pending Inbox Files", ""])
    pending = manifest["pending_inbox_files"]
    if pending:
        lines.extend(f"- `{path}`" for path in pending)
    else:
        lines.append("- None")

    lines.extend(["", "## OpenSpec Changes", ""])
    change_rows = [
        [
            item["change_id"],
            item["state"],
            f"{item['done_tasks']}/{item['total_tasks']}",
            item["tasks_path"],
        ]
        for item in manifest["openspec_changes"]
    ]
    lines.extend(_markdown_table(["Change", "State", "Tasks", "Path"], change_rows or [["none", "-", "-", "-"]]))

    lines.extend(["", "## Next Actions", ""])
    if summary["pending_inbox_count"]:
        lines.append("- Create or link source records for pending inbox files.")
    if summary["complete_change_count"]:
        lines.append("- Review complete active-directory OpenSpec changes for archive readiness.")
    if summary["active_change_count"]:
        lines.append("- Continue active OpenSpec changes before starting unrelated implementation.")
    if not (
        summary["pending_inbox_count"]
        or summary["complete_change_count"]
        or summary["active_change_count"]
    ):
        lines.append("- No generated status actions.")
    lines.append("")
    return "\n".join(lines)


def write_status_outputs(root: Path | str, output_dir: Path | str = DEFAULT_OUTPUT_DIR) -> tuple[Path, Path]:
    root_path = Path(root).resolve()
    output_path = Path(output_dir)
    if not output_path.is_absolute():
        output_path = root_path / output_path
    output_path.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(root_path)
    manifest_path = output_path / "manifest.json"
    status_path = output_path / "wiki-status.md"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    status_path.write_text(render_status_markdown(manifest), encoding="utf-8")
    return manifest_path, status_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build wiki manifest and status report.")
    parser.add_argument("--root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    manifest_path, status_path = write_status_outputs(Path(args.root), Path(args.output_dir))
    print(f"Wrote {manifest_path}")
    print(f"Wrote {status_path}")


if __name__ == "__main__":
    main()
