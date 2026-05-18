from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts.extract_wiki_graph import parse_frontmatter


BUCKET_DIALOGUE_DISAGREEMENT = "dialogue-disagreement"
BUCKET_AGENT_DRIFT = "agent-drift"
BUCKET_REANCHOR_TRACE = "reanchor-trace"
BUCKET_SUPPORTING_EXAMPLE = "supporting-example"
BUCKET_NOT_DIALOGUE_DRIFT = "not-dialogue-drift"

PROOF_BOUNDARY_NOTES = [
    "This review classifies dialogue disagreement, agent drift, and re-anchor traces only.",
    "It does not write frontmatter, relation fields, taxonomy config, ADRs, AGENTS, skills, or OpenSpec lifecycle state.",
    "It does not approve surgery application.",
]


def _relative_path(root: Path, path: Path | str) -> str:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve()
    try:
        return resolved.relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(f"path is outside root: {path}") from exc


def _read_page(root: Path, path: Path | str) -> tuple[str, dict[str, Any], str]:
    rel = _relative_path(root, path)
    full_path = root / rel
    text = full_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    return rel, meta, body


def _title(meta: dict[str, Any], body: str) -> str:
    value = meta.get("title")
    if isinstance(value, str) and value.strip():
        return value.strip()
    for line in body.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def _joined_text(rel: str, meta: dict[str, Any], body: str) -> str:
    frontmatter_bits = [str(value) for value in meta.values()]
    return "\n".join([rel, *frontmatter_bits, body]).lower()


def _has_any(text: str, needles: tuple[str, ...]) -> str:
    for needle in needles:
        if needle.lower() in text:
            return needle
    return ""


def _artifact_type(meta: dict[str, Any]) -> str:
    value = meta.get("artifact_type") or meta.get("type") or ""
    return str(value).strip().lower()


def _recommended_next_action(bucket: str) -> str:
    if bucket == BUCKET_AGENT_DRIFT:
        return "openspec-candidate"
    if bucket in {BUCKET_DIALOGUE_DISAGREEMENT, BUCKET_NOT_DIALOGUE_DRIFT}:
        return "defer-cleanup"
    return "no-op"


def classify_dialogue_drift_page(
    root: Path | str,
    path: Path | str,
    detail_ref: str | None = None,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    rel, meta, body = _read_page(root_path, path)
    artifact_type = _artifact_type(meta)
    title = _title(meta, body)
    text = _joined_text(rel, meta, body)

    evidence = ""
    bucket = BUCKET_NOT_DIALOGUE_DRIFT

    supporting_signal = _has_any(
        text,
        (
            "sample",
            "示例",
            "replay harness",
            "replay-harness",
            "replay validation",
            "replay-validation",
        ),
    )
    if artifact_type in {"sample", "replay-harness", "replay-validation"} or supporting_signal:
        bucket = BUCKET_SUPPORTING_EXAMPLE
        evidence = supporting_signal or artifact_type
    else:
        agent_signal = _has_any(
            text,
            (
                "wrong route",
                "agent followed the wrong route",
                "output-mode boundary failure",
                "workflow boundary failure",
                "implementation boundary",
                "h5/svg",
                "agent drift",
                "route drift",
                "routing handoff failure",
                "visual output routing drift",
                "silent svg/html fallback",
            ),
        )
        reanchor_signal = _has_any(
            text,
            (
                "re-anchor",
                "reanchor",
                "continuation must stop",
                "last confirmed requirement",
                "stop continuation",
            ),
        )
        disagreement_signal = _has_any(
            text,
            (
                "Rejected Framing",
                "Corrected Framing",
                "correction pressure",
                "user correction",
                "用户纠正",
                "纠偏压力",
                "disagreement",
                "分歧",
            ),
        )
        negative_signal = _has_any(
            text,
            (
                "weekly project",
                "weekly progress",
                "milestone",
                "owner",
                "project update",
                "项目周",
                "项目管理",
                "周推进",
                "reading notes",
                "reading-notes",
                "source learning",
                "source-learning",
                "learning note",
                "learning-note",
                "report gate review",
                "report-gate-review",
            ),
        )
        if artifact_type in {
            "reading-notes",
            "source-learning",
            "learning-note",
            "report-gate-review",
            "report_gate_review",
        }:
            negative_signal = negative_signal or artifact_type

        if disagreement_signal:
            bucket = BUCKET_DIALOGUE_DISAGREEMENT
            evidence = disagreement_signal
        elif agent_signal:
            bucket = BUCKET_AGENT_DRIFT
            evidence = agent_signal
        elif reanchor_signal:
            bucket = BUCKET_REANCHOR_TRACE
            evidence = reanchor_signal
        elif negative_signal:
            bucket = BUCKET_NOT_DIALOGUE_DRIFT
            evidence = (
                "project-management"
                if negative_signal in {"weekly project", "weekly progress", "milestone", "owner", "project update", "项目周", "项目管理", "周推进"}
                else "learning"
                if "learning" in negative_signal or "reading" in negative_signal
                else negative_signal
            )
        else:
            evidence = "no explicit dialogue drift signal"

    return {
        "detail_ref": detail_ref or "",
        "path": rel,
        "title": title,
        "proposed_bucket": bucket,
        "evidence": evidence,
        "recommended_next_action": _recommended_next_action(bucket),
        "proof_boundary": "review-only; no writes approved",
    }


def _scan_ops_pages(root: Path) -> list[dict[str, str]]:
    ops_dir = root / "wiki" / "ops"
    if not ops_dir.exists():
        return []
    return [
        {"detail_ref": "", "path": path.relative_to(root).as_posix()}
        for path in sorted(ops_dir.rglob("*.md"))
        if "wiki-medical-cases" not in path.parts
        and not any(part.startswith("wiki-") and part.endswith("-runs") for part in path.parts)
    ]


def build_dialogue_drift_report(
    root: Path | str,
    candidates: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    source_items = candidates if candidates is not None else _scan_ops_pages(root_path)
    items = [
        classify_dialogue_drift_page(
            root_path,
            item["path"],
            detail_ref=item.get("detail_ref") or "",
        )
        for item in source_items
    ]
    summary = Counter(item["proposed_bucket"] for item in items)
    for bucket in (
        BUCKET_DIALOGUE_DISAGREEMENT,
        BUCKET_AGENT_DRIFT,
        BUCKET_REANCHOR_TRACE,
        BUCKET_SUPPORTING_EXAMPLE,
        BUCKET_NOT_DIALOGUE_DRIFT,
    ):
        summary.setdefault(bucket, 0)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "dialogue_agent_drift_trace_review",
        "summary": dict(sorted(summary.items())),
        "items": items,
        "proof_boundary_notes": PROOF_BOUNDARY_NOTES,
    }
