#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.check_wiki_frontmatter import build_report as build_frontmatter_report
from scripts.check_wiki_frontmatter import load_taxonomy
from scripts.check_wiki_frontmatter import matching_rule_sets
from scripts.check_wiki_frontmatter import render_markdown_report


DEFAULT_FULL_JSON = Path("/tmp/wiki-frontmatter-taxonomy-report.json")
DEFAULT_FULL_MARKDOWN = Path("/tmp/wiki-frontmatter-taxonomy-report.md")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _entry_digest(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": entry.get("path"),
        "severity": entry.get("severity"),
        "kind": entry.get("kind"),
        "field": entry.get("field"),
        "value": entry.get("value"),
        "message": entry.get("message"),
    }


def _top_blockers(entries: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    samples: dict[tuple[str, str, str, str], list[str]] = defaultdict(list)
    for entry in entries:
        key = (
            str(entry.get("severity") or ""),
            str(entry.get("kind") or ""),
            str(entry.get("field") or ""),
            str(entry.get("dimension") or ""),
        )
        if key not in grouped:
            grouped[key] = {
                "severity": key[0],
                "kind": key[1],
                "field": key[2] or None,
                "dimension": key[3] or None,
                "count": 0,
            }
        grouped[key]["count"] += 1
        if len(samples[key]) < 3:
            samples[key].append(str(entry.get("path") or ""))

    rows = []
    for key, row in grouped.items():
        rows.append({**row, "sample_paths": samples[key]})
    return sorted(rows, key=lambda item: (-int(item["count"]), str(item["kind"])))[:limit]


def _dedupe_ordered(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _target_repair_hints(root: Path, target_path: str, config: dict[str, Any]) -> dict[str, Any]:
    required: list[str] = []
    exact: dict[str, Any] = {}
    for _rule_name, rule in matching_rule_sets(target_path, config):
        required.extend(str(field) for field in rule.get("required", []))
        expected = rule.get("expected", {})
        if isinstance(expected, dict):
            for field, value in expected.items():
                exact[str(field)] = value

    field_options: dict[str, list[str]] = {}
    fields = config.get("fields", {})
    if isinstance(fields, dict):
        for field in _dedupe_ordered(required):
            field_config = fields.get(field, {})
            if not isinstance(field_config, dict):
                continue
            options = field_config.get("allowed") or field_config.get("known")
            if isinstance(options, list):
                field_options[field] = [str(option) for option in options]

    return {
        "required_fields": _dedupe_ordered(required),
        "exact_frontmatter": exact,
        "field_options": field_options,
        "notes": [
            "Use exact_frontmatter values as-is.",
            "Choose field_options values only when they match the page content and repo routing.",
            "Load wiki/config/frontmatter-taxonomy.yaml only when these hints are insufficient.",
        ],
    }


def build_precheck_report(
    *,
    root: Path | str = ROOT,
    mode: str = "frontmatter",
    target: str | None = None,
    top: int = 5,
    json_output: Path | str = DEFAULT_FULL_JSON,
    markdown_output: Path | str = DEFAULT_FULL_MARKDOWN,
) -> dict[str, Any]:
    if mode != "frontmatter":
        raise ValueError(f"unsupported precheck mode: {mode}")

    root_path = Path(root)
    config = load_taxonomy(root_path)
    json_path = Path(json_output)
    markdown_path = Path(markdown_output)
    full_report = build_frontmatter_report(root_path)
    _write_text(
        json_path,
        json.dumps(full_report, ensure_ascii=False, indent=2) + "\n",
    )
    _write_text(markdown_path, render_markdown_report(full_report))

    entries = list(full_report.get("entries", []))
    max_items = max(0, int(top))
    target_path = target.replace("\\", "/") if target else None
    target_entries = [
        _entry_digest(entry)
        for entry in entries
        if target_path and entry.get("path") == target_path
    ]

    strict_gate = full_report.get("strict_gate", {})
    scorecard = full_report.get("scorecard", {})
    blocking_count = int(strict_gate.get("blocking_entry_count", 0))
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "gate": "wiki-frontmatter-taxonomy",
        "mode": mode,
        "passed": blocking_count == 0,
        "score": int(scorecard.get("score", 0)),
        "minimum_pass_score": int(scorecard.get("minimum_pass_score", 100)),
        "blocking_count": blocking_count,
        "summary": full_report.get("summary", {}),
        "top_blockers": _top_blockers(entries, max_items),
        "target": {
            "path": target_path,
            "entry_count": len(target_entries),
            "entries": target_entries[:max_items],
            "repair_hints": _target_repair_hints(root_path, target_path, config),
        }
        if target_path
        else None,
        "full_report": {
            "json": json_path.as_posix(),
            "markdown": markdown_path.as_posix(),
        },
        "proof_boundary": [
            "This precheck is an agent-readable summary of the configured frontmatter gate.",
            "It does not replace the full checker report written to full_report paths.",
            "It does not infer missing business domains from prose.",
        ],
    }


def render_precheck_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Wiki Gate Precheck",
        "",
        f"Generated at: `{report['generated_at']}`",
        f"Gate: `{report['gate']}`",
        f"Mode: `{report['mode']}`",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Passed | {report['passed']} |",
        f"| Score | {report['score']} / {report['minimum_pass_score']} |",
        f"| Blocking entries | {report['blocking_count']} |",
        f"| Full JSON | `{report['full_report']['json']}` |",
        f"| Full Markdown | `{report['full_report']['markdown']}` |",
        "",
        "## Top Blockers",
        "",
    ]
    blockers = report.get("top_blockers", [])
    if not blockers:
        lines.append("- None")
    else:
        for blocker in blockers:
            field = blocker.get("field") or "-"
            sample_paths = ", ".join(f"`{path}`" for path in blocker.get("sample_paths", []))
            lines.append(
                f"- `{blocker['severity']}` `{blocker['kind']}` field=`{field}` "
                f"count={blocker['count']} samples={sample_paths}"
            )

    target = report.get("target")
    if target:
        lines.extend(["", "## Target", ""])
        lines.append(f"Path: `{target['path']}`")
        lines.append(f"Entries: `{target['entry_count']}`")
        for entry in target.get("entries", []):
            field = entry.get("field") or "-"
            lines.append(
                f"- `{entry['severity']}` `{entry['kind']}` field=`{field}`: "
                f"{entry['message']}"
            )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run compact wiki gate prechecks.")
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--mode", choices=["frontmatter"], default="frontmatter")
    parser.add_argument("--target")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--full-json-output", default=DEFAULT_FULL_JSON)
    parser.add_argument("--full-markdown-output", default=DEFAULT_FULL_MARKDOWN)
    parser.add_argument("--compact-markdown-output")
    args = parser.parse_args()

    report = build_precheck_report(
        root=Path(args.root),
        mode=args.mode,
        target=args.target,
        top=args.top,
        json_output=Path(args.full_json_output),
        markdown_output=Path(args.full_markdown_output),
    )
    if args.compact_markdown_output:
        _write_text(Path(args.compact_markdown_output), render_precheck_markdown(report))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
