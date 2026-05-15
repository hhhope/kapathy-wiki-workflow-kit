from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_SURGERY_RECORD_DIR = Path("wiki/ops/wiki-surgery-runs")
SURGERY_RISK_FLAGS = {
    "relation_weak_evidence",
    "drift_risk",
    "adr_risk",
    "openspec_required",
    "taxonomy_candidate",
}
GOVERNANCE_RISK_FLAGS = {"drift_risk", "adr_risk", "openspec_required"}
MOC_SURGERY_ACTIONS = {"create", "update", "orphan"}


def _timestamp_slug(timestamp: datetime | str | None) -> str:
    if timestamp is None:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    if isinstance(timestamp, datetime):
        return timestamp.astimezone(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    try:
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        return timestamp
    return parsed.astimezone(timezone.utc).strftime("%Y-%m-%d-%H%M%S")


def _detail_ref(detail: dict[str, Any]) -> str:
    return str(detail.get("detail_id") or detail.get("detail_ref") or "unknown")


def _risk_flags(detail: dict[str, Any]) -> list[str]:
    risks = detail.get("risk_flags", [])
    if not isinstance(risks, list):
        return []
    return [str(risk) for risk in risks if str(risk).strip()]


def _judgment_reason(detail: dict[str, Any]) -> str:
    judgment = detail.get("judgment", {})
    if isinstance(judgment, dict) and judgment.get("reason"):
        return str(judgment["reason"])
    if detail.get("reason"):
        return str(detail["reason"])
    return "structural or governance risk requires surgery planning"


def _surgery_item(detail: dict[str, Any]) -> dict[str, Any]:
    item = {
        "detail_ref": _detail_ref(detail),
        "path": str(detail.get("path", "")),
        "risk_flags": _risk_flags(detail),
        "reason": _judgment_reason(detail),
    }
    return item


def _moc_projection_items(moc_plan: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(moc_plan, dict):
        return []
    entries = moc_plan.get("entries", [])
    if not isinstance(entries, list):
        return []
    items: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        action = str(entry.get("action", ""))
        if action not in MOC_SURGERY_ACTIONS:
            continue
        items.append(
            {
                "action": action,
                "kind": str(entry.get("kind", "")),
                "key": str(entry.get("key", "")),
                "path": str(entry.get("path", "")),
                "link_count": int(entry.get("link_count", 0) or 0),
                "reason": "MOC projection write requires surgery review",
            }
        )
    return items


def build_surgery_plan(
    adjudication_package: dict[str, Any],
    moc_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    eval_result = adjudication_package.get("eval_result", {})
    if isinstance(eval_result, dict) and eval_result.get("passed") is False:
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "mode": "wiki_surgery_plan",
            "status": "blocked",
            "source_adjudication_summary": adjudication_package.get("summary", {}),
            "source_moc_summary": moc_plan.get("summary", {}) if isinstance(moc_plan, dict) else {},
            "summary": {
                "source_detail_count": 0,
                "surgery_item_count": 0,
                "relation_rebuild_count": 0,
                "governance_change_count": 0,
                "taxonomy_decision_count": 0,
                "moc_projection_count": 0,
            },
            "surgery_items": [],
            "relation_rebuild_items": [],
            "governance_change_items": [],
            "taxonomy_decision_items": [],
            "moc_projection_items": [],
            "proof_boundary_notes": [
                "Surgery planning is blocked because adjudication eval did not pass.",
                "It does not write frontmatter, taxonomy config, relations, MOC pages, ADR decisions, or OpenSpec state.",
            ],
            "next_review_actions": [
                "Fix or review adjudication eval errors before surgery planning.",
            ],
            "blocked_reason": "adjudication eval failed",
            "eval_result": eval_result,
        }

    details = adjudication_package.get("full_detail_set", [])
    if not isinstance(details, list):
        details = []

    surgery_items: list[dict[str, Any]] = []
    for detail in details:
        if not isinstance(detail, dict):
            continue
        risks = set(_risk_flags(detail))
        if risks & SURGERY_RISK_FLAGS:
            surgery_items.append(_surgery_item(detail))

    relation_rebuild = [
        item for item in surgery_items if "relation_weak_evidence" in item["risk_flags"]
    ]
    governance_change = [
        item for item in surgery_items if set(item["risk_flags"]) & GOVERNANCE_RISK_FLAGS
    ]
    taxonomy_decision = [
        item for item in surgery_items if "taxonomy_candidate" in item["risk_flags"]
    ]
    moc_items = _moc_projection_items(moc_plan)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "wiki_surgery_plan",
        "status": "planned",
        "source_adjudication_summary": adjudication_package.get("summary", {}),
        "source_moc_summary": moc_plan.get("summary", {}) if isinstance(moc_plan, dict) else {},
        "summary": {
            "source_detail_count": len(details),
            "surgery_item_count": len(surgery_items),
            "relation_rebuild_count": len(relation_rebuild),
            "governance_change_count": len(governance_change),
            "taxonomy_decision_count": len(taxonomy_decision),
            "moc_projection_count": len(moc_items),
        },
        "surgery_items": surgery_items,
        "relation_rebuild_items": relation_rebuild,
        "governance_change_items": governance_change,
        "taxonomy_decision_items": taxonomy_decision,
        "moc_projection_items": moc_items,
        "proof_boundary_notes": [
            "This is a surgery plan only, not surgery approval.",
            "It does not write frontmatter, taxonomy config, relations, MOC pages, ADR decisions, or OpenSpec state.",
            "Surgery application requires a later explicit OpenSpec or human-approved apply workflow.",
        ],
        "next_review_actions": [
            "Human review: decide which surgery items are real, duplicate, or obsolete.",
            "OpenSpec: route governance, ADR, taxonomy, and broad relation changes to explicit changes.",
            "MOC: review projection create/update/orphan entries before any generated file write.",
            "Recovery: run checkers and doctor again only after surgery is applied.",
        ],
    }


def _limited(items: Any, limit: int) -> list[Any]:
    if not isinstance(items, list):
        return []
    return items[: max(0, limit)]


def _item_line(item: dict[str, Any]) -> str:
    path = str(item.get("path", ""))
    ref = str(item.get("detail_ref") or item.get("key") or item.get("action") or "unknown")
    prefix = f"{ref} `{path}`" if path else ref
    parts = []
    risks = item.get("risk_flags", [])
    if isinstance(risks, list) and risks:
        parts.append("risks=" + ", ".join(str(risk) for risk in risks))
    if item.get("action"):
        parts.append(f"action={item['action']}")
    if item.get("reason"):
        parts.append(str(item["reason"]))
    return f"- {prefix}: {'; '.join(parts)}" if parts else f"- {prefix}"


def render_surgery_record_markdown(
    plan: dict[str, Any],
    scan_root: Path | str,
    limit: int = 50,
) -> str:
    lines = [
        "# wiki-surgery Plan Record",
        "",
        "## Source",
        f"- Generated at: {plan.get('generated_at', 'unknown')}",
        f"- Scan root: `{Path(scan_root)}`",
        f"- Detail limit: {limit}",
        "",
        "## Summary",
    ]
    for key, value in sorted(plan.get("summary", {}).items()):
        lines.append(f"- {key}: {value}")

    sections = [
        ("Surgery Items", "surgery_items"),
        ("Relation Rebuild Items", "relation_rebuild_items"),
        ("Governance Change Items", "governance_change_items"),
        ("Taxonomy Decision Items", "taxonomy_decision_items"),
        ("MOC Projection Items", "moc_projection_items"),
    ]
    for title, key in sections:
        lines.extend(["", f"## {title}"])
        items = [_item_line(item) for item in _limited(plan.get(key, []), limit) if isinstance(item, dict)]
        lines.extend(items or ["- None"])

    lines.extend(["", "## Proof Boundary"])
    for note in plan.get("proof_boundary_notes", []):
        lines.append(f"- {note}")

    lines.extend(["", "## Next Review Actions"])
    for action in plan.get("next_review_actions", []):
        lines.append(f"- {action}")
    return "\n".join(lines) + "\n"


def next_surgery_record_path(output_dir: Path, timestamp: datetime | str | None = None) -> Path:
    slug = _timestamp_slug(timestamp)
    base = output_dir / f"{slug}-surgery.md"
    if not base.exists():
        return base
    counter = 2
    while True:
        candidate = output_dir / f"{slug}-surgery-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def write_surgery_record(
    plan: dict[str, Any],
    root: Path | str,
    output_dir: Path | str | None = None,
    timestamp: datetime | str | None = None,
    limit: int = 50,
) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_SURGERY_RECORD_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    markdown = render_surgery_record_markdown(plan, scan_root=root_path, limit=limit)
    while True:
        target = next_surgery_record_path(target_dir, timestamp=timestamp)
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(markdown)
            return target.resolve()
        except FileExistsError:
            continue
