from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts.extract_wiki_graph import parse_frontmatter


DEFAULT_TREATMENT_RECORD_DIR = Path("wiki/ops/wiki-treatment-runs")
FRONTMATTER_FIELD_ORDER = [
    "layer",
    "domain",
    "ops_area",
    "canonical_object",
    "artifact_type",
    "classification_needed",
]


def _detail_ref(detail: dict[str, Any]) -> str:
    return str(detail.get("detail_id") or detail.get("detail_ref") or "unknown")


def _suggested_frontmatter(detail: dict[str, Any]) -> dict[str, Any]:
    candidate = detail.get("candidate", {})
    if not isinstance(candidate, dict):
        return {}
    suggested = candidate.get("suggested_frontmatter", {})
    return suggested if isinstance(suggested, dict) else {}


def _judgment_state(detail: dict[str, Any]) -> str:
    judgment = detail.get("judgment", {})
    if not isinstance(judgment, dict):
        return ""
    return str(judgment.get("state", ""))


def _risk_flags(detail: dict[str, Any]) -> list[str]:
    risks = detail.get("risk_flags", [])
    if not isinstance(risks, list):
        return []
    return [str(risk) for risk in risks if str(risk).strip()]


def _approval_for_detail(
    detail_ref: str,
    domain: str,
    approved_domains: set[str],
    approved_detail_refs: set[str],
) -> str | None:
    if detail_ref in approved_detail_refs:
        return f"detail:{detail_ref}"
    if domain in approved_domains:
        return f"domain:{domain}"
    return None


def _skip(detail: dict[str, Any], reason: str) -> dict[str, Any]:
    item = {"detail_ref": _detail_ref(detail), "reason": reason}
    if detail.get("path"):
        item["path"] = str(detail["path"])
    risks = _risk_flags(detail)
    if risks:
        item["risk_flags"] = risks
    return item


def build_treatment_plan(
    adjudication_package: dict[str, Any],
    approved_domains: set[str] | None = None,
    approved_detail_refs: set[str] | None = None,
) -> dict[str, Any]:
    domain_approvals = {str(item) for item in (approved_domains or set()) if str(item).strip()}
    detail_approvals = {
        str(item) for item in (approved_detail_refs or set()) if str(item).strip()
    }
    treatment_items: list[dict[str, Any]] = []
    skipped_items: list[dict[str, Any]] = []

    details = adjudication_package.get("full_detail_set", [])
    if not isinstance(details, list):
        details = []

    for detail in details:
        if not isinstance(detail, dict):
            continue
        suggested = _suggested_frontmatter(detail)
        detail_ref = _detail_ref(detail)
        risks = _risk_flags(detail)
        domain = str(suggested.get("domain", ""))
        approval = _approval_for_detail(detail_ref, domain, domain_approvals, detail_approvals)

        if (
            detail.get("safe_to_apply_frontmatter") is not True
            or risks
            or _judgment_state(detail) not in {"accept", "likely"}
            or not suggested
        ):
            skipped_items.append(
                _skip(detail, "detail is not a safe frontmatter treatment candidate")
            )
            continue
        if approval is None:
            skipped_items.append(_skip(detail, "missing explicit domain or detail approval"))
            continue

        treatment_items.append(
            {
                "detail_ref": detail_ref,
                "path": str(detail.get("path", "")),
                "approval": approval,
                "suggested_frontmatter": {
                    str(key): value for key, value in suggested.items() if str(key).strip()
                },
            }
        )

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "wiki_treatment_plan",
        "approved_domains": sorted(domain_approvals),
        "approved_detail_refs": sorted(detail_approvals),
        "summary": {
            "source_detail_count": len(details),
            "treatment_item_count": len(treatment_items),
            "skipped_item_count": len(skipped_items),
        },
        "treatment_items": treatment_items,
        "skipped_items": skipped_items,
        "proof_boundary_notes": [
            "Treatment writes only explicitly approved low-risk frontmatter candidates.",
            "It does not write relations, taxonomy config, MOC pages, ADR decisions, or OpenSpec state.",
            "Dry-run is the default; page mutation requires explicit apply mode.",
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


def _write_frontmatter(path: Path, suggested: dict[str, Any]) -> None:
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    merged = {**meta, **suggested}
    path.write_text(_render_frontmatter(merged) + body, encoding="utf-8")


def apply_treatment_plan(root: Path | str, plan: dict[str, Any], apply: bool = False) -> dict[str, Any]:
    root_path = Path(root)
    results: list[dict[str, Any]] = []
    for item in plan.get("treatment_items", []):
        if not isinstance(item, dict):
            continue
        rel = str(item.get("path", ""))
        target = (root_path / rel).resolve()
        root_resolved = root_path.resolve()
        if root_resolved not in target.parents and target != root_resolved:
            results.append(
                {
                    "detail_ref": item.get("detail_ref", "unknown"),
                    "path": rel,
                    "status": "blocked",
                    "reason": "target path escapes root",
                }
            )
            continue
        if apply and not target.exists():
            results.append(
                {
                    "detail_ref": item.get("detail_ref", "unknown"),
                    "path": rel,
                    "status": "blocked",
                    "reason": "target file does not exist",
                }
            )
            continue
        if not apply:
            results.append(
                {
                    "detail_ref": item.get("detail_ref", "unknown"),
                    "path": rel,
                    "status": "dry_run",
                }
            )
            continue
        _write_frontmatter(target, item.get("suggested_frontmatter", {}))
        results.append(
            {
                "detail_ref": item.get("detail_ref", "unknown"),
                "path": rel,
                "status": "applied",
            }
        )

    return {
        "applied": apply,
        "summary": {
            "applied_count": sum(1 for item in results if item["status"] == "applied"),
            "dry_run_count": sum(1 for item in results if item["status"] == "dry_run"),
            "blocked_count": sum(1 for item in results if item["status"] == "blocked"),
        },
        "results": results,
    }


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


def next_treatment_record_path(output_dir: Path, timestamp: datetime | str | None = None) -> Path:
    slug = _timestamp_slug(timestamp)
    base = output_dir / f"{slug}-treatment.md"
    if not base.exists():
        return base
    counter = 2
    while True:
        candidate = output_dir / f"{slug}-treatment-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def _item_line(item: dict[str, Any]) -> str:
    detail_ref = str(item.get("detail_ref", "unknown"))
    path = str(item.get("path", ""))
    suffix = f" `{path}`" if path else ""
    if item.get("approval"):
        return f"- {detail_ref}{suffix}: approval={item['approval']}"
    if item.get("reason"):
        return f"- {detail_ref}{suffix}: {item['reason']}"
    return f"- {detail_ref}{suffix}"


def render_treatment_record_markdown(
    plan: dict[str, Any],
    result: dict[str, Any],
    scan_root: Path | str,
) -> str:
    lines = [
        "# wiki-treatment Record",
        "",
        "## Source",
        f"- Generated at: {plan.get('generated_at', 'unknown')}",
        f"- Scan root: `{Path(scan_root)}`",
        f"- Applied: {result.get('applied', False)}",
        "",
        "## Summary",
    ]
    summary = {**plan.get("summary", {}), **result.get("summary", {})}
    for key in sorted(summary):
        lines.append(f"- {key}: {summary[key]}")

    lines.extend(["", "## Treatment Items"])
    treatment_items = plan.get("treatment_items", [])
    lines.extend(
        [_item_line(item) for item in treatment_items if isinstance(item, dict)]
        or ["- None"]
    )

    lines.extend(["", "## Skipped Items"])
    skipped_items = plan.get("skipped_items", [])
    lines.extend(
        [_item_line(item) for item in skipped_items if isinstance(item, dict)]
        or ["- None"]
    )

    lines.extend(["", "## Apply Results"])
    results = result.get("results", [])
    lines.extend([_item_line(item) for item in results if isinstance(item, dict)] or ["- None"])

    lines.extend(["", "## Proof Boundary"])
    for note in plan.get("proof_boundary_notes", []):
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"


def write_treatment_record(
    plan: dict[str, Any],
    result: dict[str, Any],
    root: Path | str,
    output_dir: Path | str | None = None,
    timestamp: datetime | str | None = None,
) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_TREATMENT_RECORD_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    markdown = render_treatment_record_markdown(plan, result, scan_root=root_path)
    while True:
        target = next_treatment_record_path(target_dir, timestamp=timestamp)
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(markdown)
            return target.resolve()
        except FileExistsError:
            continue
