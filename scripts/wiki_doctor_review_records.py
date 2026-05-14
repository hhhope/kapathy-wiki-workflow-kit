from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REVIEW_RECORD_DIR = Path("wiki/ops/wiki-doctor-runs")


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


def _limited(items: Any, limit: int) -> list[Any]:
    if not isinstance(items, list):
        return []
    return items[: max(0, limit)]


def _markdown_list(items: list[str]) -> list[str]:
    if not items:
        return ["- None"]
    return [f"- {item}" for item in items]


def render_review_record_markdown(package: dict[str, Any], scan_root: Path | str, limit: int) -> str:
    summary = package.get("summary", {})
    eval_result = package.get("eval_result", {})
    if not isinstance(eval_result, dict):
        eval_result = {}
    warnings = eval_result.get("warnings", [])
    errors = eval_result.get("errors", [])
    generated_at = str(package.get("generated_at", "unknown"))
    lines = [
        "# wiki-doctor Review Record",
        "",
        "## Scan",
        "",
        f"- Generated at: {generated_at}",
        f"- Scan root: `{Path(scan_root)}`",
        f"- Detail limit: {limit}",
        "- Source: scripts/build_wiki_content_adjudication.py",
        "",
        "## Summary Counts",
    ]

    if isinstance(summary, dict) and summary:
        for key in sorted(summary):
            lines.append(f"- {key}: {summary[key]}")
    else:
        lines.append("- None")
    lines.extend(
        [
            f"- eval_passed: {bool(eval_result.get('passed', False))}",
            f"- eval_error_count: {len(errors) if isinstance(errors, list) else 0}",
            f"- eval_warning_count: {len(warnings) if isinstance(warnings, list) else 0}",
        ]
    )

    lines.extend(["", "## Taxonomy Candidates"])
    taxonomy_lines = []
    for item in _limited(package.get("taxonomy_candidate_set", []), limit):
        refs = ", ".join(str(ref) for ref in item.get("detail_refs", [])) or "none"
        taxonomy_lines.append(
            f"{item.get('field', 'unknown')}=`{item.get('value', '')}` refs={refs}: "
            f"{item.get('reason', '')}"
        )
    lines.extend(_markdown_list(taxonomy_lines))

    lines.extend(["", "## Drift Traces"])
    drift_lines = []
    for item in _limited(package.get("drift_trace_set", []), limit):
        risks = ", ".join(str(risk) for risk in item.get("risk_flags", [])) or "none"
        drift_lines.append(
            f"{item.get('detail_ref', 'unknown')} `{item.get('path', '')}` risks={risks}: "
            f"{item.get('reason', '')}"
        )
    lines.extend(_markdown_list(drift_lines))

    lines.extend(["", "## Eval Errors"])
    lines.extend(_markdown_list([str(item) for item in _limited(errors, limit)]))

    lines.extend(["", "## Eval Warnings"])
    lines.extend(_markdown_list([str(item) for item in _limited(warnings, limit)]))

    lines.extend(["", "## Proof Boundary"])
    proof_notes = [str(item) for item in _limited(package.get("proof_boundary_notes", []), limit)]
    proof_notes.append("This record is diagnosis only.")
    lines.extend(_markdown_list(proof_notes))

    lines.extend(
        [
            "",
            "## Next Review Actions",
            "- Human review: inspect taxonomy candidates and review focus refs before accepting any structure change.",
            "- Discard: ignore candidates that lack evidence or only preserve historical drift.",
            "- OpenSpec candidate: create or select a change for taxonomy or workflow behavior changes.",
            "- Later explicit repair: apply frontmatter, taxonomy, or MOC changes only after approval.",
        ]
    )
    return "\n".join(lines) + "\n"


def next_review_record_path(output_dir: Path, timestamp: datetime | str | None = None) -> Path:
    slug = _timestamp_slug(timestamp)
    base = output_dir / f"{slug}-review.md"
    if not base.exists():
        return base
    counter = 2
    while True:
        candidate = output_dir / f"{slug}-review-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def write_review_record(
    package: dict[str, Any],
    root: Path | str,
    output_dir: Path | str | None = None,
    timestamp: datetime | str | None = None,
    limit: int = 50,
) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_REVIEW_RECORD_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    markdown = render_review_record_markdown(package, scan_root=root_path, limit=limit)

    while True:
        target = next_review_record_path(target_dir, timestamp=timestamp)
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(markdown)
            return target.resolve()
        except FileExistsError:
            continue
