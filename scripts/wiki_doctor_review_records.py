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


def _limited(items: Any, limit: int | None) -> list[Any]:
    if not isinstance(items, list):
        return []
    if limit is None:
        return items
    return items[: max(0, limit)]


def _markdown_list(items: list[str]) -> list[str]:
    if not items:
        return ["- None"]
    return [f"- {item}" for item in items]


def _format_detail(item: dict[str, Any]) -> str:
    detail_ref = str(item.get("detail_id") or item.get("detail_ref") or "unknown")
    path = str(item.get("path", ""))
    risks = item.get("risk_flags", [])
    reason = ""
    judgment = item.get("judgment", {})
    if isinstance(judgment, dict):
        reason = str(judgment.get("reason", ""))
    if not reason:
        reason = str(item.get("reason", ""))
    risk_text = ", ".join(str(risk) for risk in risks) if isinstance(risks, list) and risks else "none"
    return f"{detail_ref} `{path}` risks={risk_text}: {reason}".strip()


def render_review_record_markdown(package: dict[str, Any], scan_root: Path | str, limit: int | None) -> str:
    summary = package.get("summary", {})
    eval_result = package.get("eval_result", {})
    if not isinstance(eval_result, dict):
        eval_result = {}
    warnings = eval_result.get("warnings", [])
    errors = eval_result.get("errors", [])
    generated_at = str(package.get("generated_at", "unknown"))
    detail_limit = "complete" if limit is None else str(limit)
    lines = [
        "# wiki-doctor Diagnosis Record",
        "",
        "## Source / 检查来源",
        "",
        f"- Generated at: {generated_at}",
        f"- Scan root: `{Path(scan_root)}`",
        f"- Detail limit: {detail_limit}",
        "- Source: scripts/build_wiki_content_adjudication.py",
        "",
        "## Exam Items / 检查项目",
        f"- full_detail_set: {len(package.get('full_detail_set', [])) if isinstance(package.get('full_detail_set'), list) else 0}",
        f"- review_focus_set: {len(package.get('review_focus_set', [])) if isinstance(package.get('review_focus_set'), list) else 0}",
        f"- taxonomy_candidate_set: {len(package.get('taxonomy_candidate_set', [])) if isinstance(package.get('taxonomy_candidate_set'), list) else 0}",
        f"- drift_trace_set: {len(package.get('drift_trace_set', [])) if isinstance(package.get('drift_trace_set'), list) else 0}",
        "- eval_result",
        "",
        "## Reference Standards / 判定标准",
        "- agent_uncertain: human review required before structural writes.",
        "- relation_weak_evidence: relation candidates cannot be auto-written.",
        "- openspec_required: lifecycle routing cannot be bypassed.",
        "- drift_risk: governance or agent judgment drift needs explicit review.",
        "- adr_risk: stable decision surfaces need surgery or OpenSpec handling.",
        "",
        "## Diagnosis Summary / 诊断摘要",
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

    lines.extend(["", "## Abnormal Findings / 异常发现"])
    detail_lines = []
    for item in _limited(package.get("full_detail_set", []), limit):
        if isinstance(item, dict):
            detail_lines.append(_format_detail(item))
    lines.extend(_markdown_list(detail_lines))

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
            "## Recommended Next Stage / 建议下一步",
            "- Use `wiki-confirm` to confirm which findings are accepted, rejected, deferred, treatment candidates, surgery candidates, or OpenSpec-required.",
            "- Do not apply frontmatter, taxonomy, relation, MOC, ADR, or OpenSpec changes from diagnosis alone.",
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
    limit: int | None = None,
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
