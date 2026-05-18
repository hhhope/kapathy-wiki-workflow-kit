from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts.extract_wiki_graph import parse_frontmatter
from scripts.check_wiki_frontmatter import build_report as build_frontmatter_report
from scripts.wiki_gate_precheck import build_precheck_report


RELATION_FIELDS = {"related_objects", "derived_from", "validates", "formalizes"}
FRONTMATTER_FIELD_ORDER = [
    "layer",
    "domain",
    "ops_area",
    "canonical_object",
    "artifact_type",
    "classification_needed",
]


def _blocking_severities(report: dict[str, Any]) -> set[str]:
    strict_gate = report.get("strict_gate", {})
    values = strict_gate.get("blocking_severities", ["error"])
    if not isinstance(values, list):
        return {"error"}
    return {str(value) for value in values}


def _blocking_entries(report: dict[str, Any]) -> list[dict[str, Any]]:
    severities = _blocking_severities(report)
    entries = report.get("entries", [])
    if not isinstance(entries, list):
        return []
    return [
        entry
        for entry in entries
        if isinstance(entry, dict) and str(entry.get("severity")) in severities
    ]


def _paths_from_report(report: dict[str, Any]) -> list[str]:
    seen: set[str] = set()
    paths: list[str] = []
    for entry in _blocking_entries(report):
        path = str(entry.get("path") or "")
        if not path or path in seen:
            continue
        seen.add(path)
        paths.append(path)
    return paths


def _target_item(root: Path, path: str) -> dict[str, Any]:
    target_report = build_precheck_report(
        root=root,
        mode="frontmatter",
        target=path,
        top=50,
        json_output=Path("/tmp/wiki-frontmatter-repair-target.json"),
        markdown_output=Path("/tmp/wiki-frontmatter-repair-target.md"),
    )
    target = target_report.get("target", {})
    entries = target.get("entries", []) if isinstance(target, dict) else []
    return {
        "path": path,
        "decision": "review_needed" if entries else "already_clean",
        "blocking_entry_count": len(entries) if isinstance(entries, list) else 0,
        "entries": entries if isinstance(entries, list) else [],
        "repair_hints": target.get("repair_hints", {}) if isinstance(target, dict) else {},
    }


def build_repair_batch(
    root: Path | str,
    *,
    limit: int = 10,
    paths: list[str] | None = None,
) -> dict[str, Any]:
    root_path = Path(root)
    full_report = build_frontmatter_report(root_path)
    selected_paths = paths or _paths_from_report(full_report)
    bounded_paths = selected_paths[: max(0, int(limit))]
    items = [_target_item(root_path, path) for path in bounded_paths]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "wiki_frontmatter_repair_batch",
        "summary": {
            "source_blocking_count": full_report.get("strict_gate", {}).get("blocking_entry_count", 0),
            "selected_count": len(items),
            "review_needed_count": sum(1 for item in items if item["decision"] == "review_needed"),
            "already_clean_count": sum(1 for item in items if item["decision"] == "already_clean"),
        },
        "items": items,
        "proof_boundary_notes": [
            "This batch is explicit frontmatter repair planning only.",
            "It does not infer taxonomy values beyond precheck hints or approved fields.",
            "It does not write relations, taxonomy config, MOC pages, ADR decisions, or OpenSpec state.",
        ],
    }


def _format_frontmatter_value(value: Any) -> list[str]:
    if isinstance(value, list):
        if not value:
            return ["[]"]
        return ["", *[f"  - {item}" for item in value]]
    text = str(value)
    if text == "":
        return ['""']
    if any(char in text for char in [":", "#", "[", "]", "{", "}", "\n"]):
        return [f'"{text}"']
    return [text]


def _render_frontmatter(meta: dict[str, Any]) -> str:
    keys = [key for key in FRONTMATTER_FIELD_ORDER if key in meta]
    keys.extend(sorted(key for key in meta if key not in keys))
    lines = ["---"]
    for key in keys:
        rendered = _format_frontmatter_value(meta[key])
        if len(rendered) == 1 and rendered[0] != "":
            lines.append(f"{key}: {rendered[0]}")
        else:
            lines.append(f"{key}:")
            lines.extend(rendered[1:])
    lines.append("---")
    return "\n".join(lines) + "\n"


def _approved_fields(values: dict[str, Any]) -> dict[str, Any]:
    return {
        str(key): value
        for key, value in values.items()
        if str(key).strip() and str(key) not in RELATION_FIELDS
    }


def _target_evidence(root: Path, path: str, suffix: str) -> dict[str, Any]:
    report = build_precheck_report(
        root=root,
        mode="frontmatter",
        target=path,
        top=50,
        json_output=Path(f"/tmp/wiki-frontmatter-repair-{suffix}.json"),
        markdown_output=Path(f"/tmp/wiki-frontmatter-repair-{suffix}.md"),
    )
    target = report.get("target", {})
    if not isinstance(target, dict):
        target = {}
    return {
        "path": str(target.get("path") or path),
        "entry_count": int(target.get("entry_count", 0) or 0),
        "entries": target.get("entries", []) if isinstance(target.get("entries", []), list) else [],
    }


def apply_frontmatter_batch(
    root: Path | str,
    batch: dict[str, Any],
    *,
    approved_frontmatter: dict[str, dict[str, Any]],
    apply: bool = False,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    results: list[dict[str, Any]] = []
    items = batch.get("items", [])
    if not isinstance(items, list):
        items = []
    for item in items:
        if not isinstance(item, dict):
            continue
        rel = str(item.get("path") or "")
        approved = _approved_fields(approved_frontmatter.get(rel, {}))
        if not rel or not approved:
            results.append({"path": rel, "status": "skipped", "reason": "missing approved frontmatter"})
            continue
        target = (root_path / rel).resolve()
        if root_path not in target.parents and target != root_path:
            results.append({"path": rel, "status": "blocked", "reason": "target path escapes root"})
            continue
        if not target.exists():
            results.append({"path": rel, "status": "blocked", "reason": "target file does not exist"})
            continue
        before = _target_evidence(root_path, rel, "before")
        if apply:
            text = target.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            target.write_text(_render_frontmatter({**meta, **approved}) + body, encoding="utf-8")
            status = "applied"
        else:
            status = "dry_run"
        after = _target_evidence(root_path, rel, "after")
        results.append(
            {
                "path": rel,
                "status": status,
                "approved_fields": sorted(approved),
                "before": before,
                "after": after,
            }
        )
    return {
        "mode": "wiki_frontmatter_repair_apply",
        "applied": apply,
        "summary": {
            "applied_count": sum(1 for item in results if item["status"] == "applied"),
            "dry_run_count": sum(1 for item in results if item["status"] == "dry_run"),
            "blocked_count": sum(1 for item in results if item["status"] == "blocked"),
            "skipped_count": sum(1 for item in results if item["status"] == "skipped"),
        },
        "results": results,
        "proof_boundary_notes": [
            "Only explicitly approved frontmatter fields are written.",
            "Relation fields are ignored by this repair workflow.",
        ],
    }
