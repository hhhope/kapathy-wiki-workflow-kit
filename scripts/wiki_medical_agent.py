from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

from scripts.wiki_medical_case import (
    DEFAULT_MEDICAL_CASE_DIR,
    attach_recovery_result_to_case,
    load_medical_case_file,
    overwrite_medical_case_file,
)
from scripts.build_wiki_moc_projection import load_graph
from scripts.wiki_moc_projection import build_moc_plan
from scripts.wiki_recovery import build_recovery_package, write_recovery_record
from scripts.wiki_surgery import build_surgery_plan_from_case
from scripts.wiki_treatment import (
    apply_treatment_plan,
    load_case_and_build_treatment_plan,
    update_case_file_with_treatment_result,
    write_treatment_record,
)


@dataclass(frozen=True)
class IntentResult:
    intent: str
    expected_count: int | None = None
    reason: str = ""


@dataclass(frozen=True)
class ActiveCaseResolution:
    status: str
    case_path: Path | None = None
    case_package: dict[str, Any] | None = None
    candidates: tuple[Path, ...] = ()
    blocked_reason: str = ""


@dataclass(frozen=True)
class ActionValidation:
    allowed: bool
    intent: str
    state: str
    allowed_action: str = ""
    blocked_reason: str = ""
    executable_count: int = 0
    expected_count: int | None = None


READ_ONLY_INTENTS = {"status", "diagnose"}
MOC_SIGNALS = ("obsidian", "knowledge-map", "knowledge map", "图谱导航", "知识地图")
MOC_REVIEW_SIGNALS = (
    "preview",
    "review",
    "temperature",
    "clue",
    "clues",
    "noise",
    "value",
    "worth",
    "预览",
    "surgery",
    "手术",
    "分流",
    "审核",
    "审查",
    "复核",
    "温度",
    "线索",
    "噪音",
    "价值",
    "值得",
    "进图",
    "不要写",
)
MOC_RELATION_SIGNALS = ("derived_from", "related_objects", "formalizes", "validates")


def _has_moc_signal(lowered: str) -> bool:
    if re.search(r"\bmoc\b", lowered):
        return True
    return any(signal in lowered for signal in MOC_SIGNALS)


def _is_moc_surgery_preview_request(lowered: str) -> bool:
    has_moc = _has_moc_signal(lowered)
    has_review = any(signal in lowered for signal in MOC_REVIEW_SIGNALS)
    has_relation_signal = any(signal in lowered for signal in MOC_RELATION_SIGNALS)
    return (has_moc and has_review) or (has_relation_signal and has_review)


def classify_medical_intent(text: str) -> IntentResult:
    lowered = text.lower()
    count_match = re.search(r"(\d+)", text)
    expected_count = int(count_match.group(1)) if count_match else None
    if "legacy" in lowered or "debug" in lowered:
        return IntentResult("legacy_debug", expected_count, "explicit legacy/debug request")
    if _is_moc_surgery_preview_request(lowered):
        return IntentResult(
            "moc_surgery_preview",
            expected_count,
            "user requested MOC surgery preview",
        )
    if any(token in lowered for token in ["preview", "dry-run", "dry run", "预览"]):
        return IntentResult("treatment_preview", expected_count, "user requested treatment preview")
    if any(token in lowered for token in ["apply", "应用", "治疗这", "执行治疗"]):
        return IntentResult("treatment_apply", expected_count, "user requested treatment apply")
    if any(token in lowered for token in ["确认", "确诊", "confirmed decisions"]):
        return IntentResult("confirm_decisions", expected_count, "user referenced confirmed decisions")
    if any(token in lowered for token in ["诊断", "doctor"]):
        return IntentResult("diagnose", expected_count, "user requested diagnosis")
    if any(token in lowered for token in ["手术", "surgery"]):
        return IntentResult("surgery_plan", expected_count, "user requested surgery planning")
    if any(token in lowered for token in ["复查", "recovery", "闭环"]):
        return IntentResult("recovery", expected_count, "user requested recovery")
    if any(token in lowered for token in ["归档", "archive"]):
        return IntentResult("archive_check", expected_count, "user requested archive check")
    return IntentResult("status", expected_count, "default status request")


def _case_sort_key(path: Path) -> str:
    return path.name


def resolve_active_case(root: Path | str) -> ActiveCaseResolution:
    root_path = Path(root)
    case_dir = root_path / DEFAULT_MEDICAL_CASE_DIR
    if not case_dir.exists():
        return ActiveCaseResolution(status="no_case")
    candidates: list[Path] = []
    for path in sorted(case_dir.glob("*.md"), key=_case_sort_key):
        try:
            package = load_medical_case_file(path)
        except (OSError, ValueError):
            continue
        if package.get("active", True) is True and str(package.get("status", "")) != "closed":
            candidates.append(path.resolve())
    if not candidates:
        return ActiveCaseResolution(status="no_case")
    if len(candidates) > 1:
        return ActiveCaseResolution(
            status="blocked",
            candidates=tuple(candidates),
            blocked_reason="multiple_active_cases",
        )
    package = load_medical_case_file(candidates[0])
    package["case_path"] = candidates[0].as_posix()
    return ActiveCaseResolution(status="ok", case_path=candidates[0], case_package=package)


def _confirmed_treatment_decisions(case_package: dict[str, Any]) -> list[dict[str, Any]]:
    confirmed = case_package.get("confirmed_decisions", {})
    if not isinstance(confirmed, dict):
        return []
    values = confirmed.get("treatment_candidates", [])
    if not isinstance(values, list):
        return []
    return [item for item in values if isinstance(item, dict)]


def validate_case_action(
    case_package: dict[str, Any],
    intent: str,
    expected_count: int | None = None,
) -> ActionValidation:
    state = str(case_package.get("status", "awaiting_confirmation"))
    treatment_count = len(_confirmed_treatment_decisions(case_package))
    if intent == "status":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="report_status",
            executable_count=treatment_count,
        )
    if intent == "diagnose":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="run_diagnosis",
            executable_count=treatment_count,
        )
    if intent == "confirm_decisions":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="record_confirmed_decisions",
            executable_count=treatment_count,
        )
    if intent == "moc_surgery_preview":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="preview_moc_surgery_plan",
            executable_count=treatment_count,
        )
    if intent == "treatment_preview":
        if treatment_count == 0:
            return ActionValidation(
                False,
                intent,
                state,
                blocked_reason="no_executable_confirmed_treatment_decisions",
            )
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="preview_confirmed_treatments",
            executable_count=treatment_count,
        )
    if intent == "treatment_apply":
        if treatment_count == 0:
            return ActionValidation(
                False,
                intent,
                state,
                blocked_reason="no_executable_confirmed_treatment_decisions",
                executable_count=0,
                expected_count=expected_count,
            )
        if state not in {"ready_for_treatment", "treatment_previewed"}:
            return ActionValidation(
                False,
                intent,
                state,
                blocked_reason="state_does_not_allow_treatment_apply",
                executable_count=treatment_count,
                expected_count=expected_count,
            )
        if expected_count is not None and expected_count != treatment_count:
            return ActionValidation(
                False,
                intent,
                state,
                blocked_reason="confirmed_decision_count_mismatch",
                executable_count=treatment_count,
                expected_count=expected_count,
            )
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="apply_confirmed_treatments",
            executable_count=treatment_count,
            expected_count=expected_count,
        )
    if intent == "recovery":
        if state not in {"treatment_applied", "recovery_required"}:
            return ActionValidation(
                False,
                intent,
                state,
                blocked_reason="state_does_not_require_recovery",
                executable_count=treatment_count,
            )
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="run_recovery",
            executable_count=treatment_count,
        )
    if intent == "surgery_plan":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="plan_surgery",
            executable_count=treatment_count,
        )
    if intent == "archive_check":
        return ActionValidation(
            True,
            intent,
            state,
            allowed_action="report_archive_readiness",
            executable_count=treatment_count,
        )
    return ActionValidation(
        False,
        intent,
        state,
        blocked_reason="unsupported_intent",
        executable_count=treatment_count,
    )


def validate_resolved_case_action(
    resolution: ActiveCaseResolution,
    intent: str,
    expected_count: int | None = None,
) -> ActionValidation:
    if resolution.status == "ok" and resolution.case_package is not None:
        return validate_case_action(resolution.case_package, intent, expected_count)
    if resolution.status == "no_case":
        if intent in READ_ONLY_INTENTS:
            return ActionValidation(
                True,
                intent,
                "no_case",
                allowed_action="report_status" if intent == "status" else "run_diagnosis",
                expected_count=expected_count,
            )
        return ActionValidation(
            False,
            intent,
            "no_case",
            blocked_reason="no_active_case",
            expected_count=expected_count,
        )
    if resolution.status == "blocked" and resolution.blocked_reason == "multiple_active_cases":
        if intent in READ_ONLY_INTENTS:
            return ActionValidation(
                True,
                intent,
                "multiple_active_cases",
                allowed_action="report_status" if intent == "status" else "run_diagnosis",
                expected_count=expected_count,
            )
        return ActionValidation(
            False,
            intent,
            "multiple_active_cases",
            blocked_reason="multiple_active_cases",
            expected_count=expected_count,
        )
    return ActionValidation(
        False,
        intent,
        resolution.status,
        blocked_reason=resolution.blocked_reason or "case_resolution_failed",
        expected_count=expected_count,
    )


MECHANICAL_RELATION_FAMILIES = {"derived_from", "related_objects"}


def _safe_int(value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        return 0
    return value


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return sorted({item.strip() for item in value if isinstance(item, str) and item.strip()})


def _temperature_value(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    if value < 0 or value > 100:
        return None
    return value


def _temperature_band(value: Any) -> str:
    if isinstance(value, str) and value.strip():
        return value.strip()
    temperature = _temperature_value(value)
    if temperature is None:
        return "unreviewed"
    if temperature >= 80:
        return "strong"
    if temperature >= 60:
        return "supporting"
    if temperature >= 40:
        return "weak"
    return "noise"


def _clue_sort_key(window: dict[str, Any]) -> tuple[int, str, str]:
    status_rank = 0 if str(window.get("status", "")) == "needs_review" else 1
    temperature = _temperature_value(window.get("temperature"))
    return (
        status_rank,
        -(temperature if temperature is not None else -1),
        str(window.get("relation_type") or window.get("relation") or ""),
    )


def _compact_clue(window: dict[str, Any]) -> dict[str, Any]:
    relation_type = str(window.get("relation_type") or window.get("relation") or "").strip()
    source_page = str(window.get("source_page") or "").strip()
    source_object = str(window.get("source_object") or source_page).strip()
    target_object = str(window.get("target_object") or "").strip()
    evidence_refs = window.get("evidence_refs", [])
    if not isinstance(evidence_refs, list):
        evidence_refs = []
    clean_refs = [str(item) for item in evidence_refs if isinstance(item, str) and item.strip()]
    temperature = _temperature_value(window.get("temperature"))
    band = _temperature_band(window.get("temperature_band") or temperature)
    rationale = str(window.get("rationale") or "").strip()
    if not rationale:
        rationale = "Needs human review before it can become a MOC admission."
    return {
        "candidate_id": str(window.get("candidate_id") or ""),
        "relation_type": relation_type,
        "source_page": source_page,
        "source_object": source_object,
        "target_object": target_object,
        "evidence_refs": clean_refs[:3],
        "temperature": temperature,
        "temperature_band": band,
        "rationale": rationale,
        "confirmation_question": f"confirm whether {relation_type} should be admitted as a MOC clue",
    }


def _sample_moc_items(plan: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    items = plan.get("moc_projection_items", [])
    if not isinstance(items, list):
        return []
    sample: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        sample.append(
            {
                "action": str(item.get("action", "")),
                "kind": str(item.get("kind", "")),
                "key": str(item.get("key", "")),
                "path": str(item.get("path", "")),
                "link_count": int(item.get("link_count", 0) or 0),
            }
        )
        if len(sample) >= limit:
            break
    return sample


def _build_moc_temperature_prediagnosis(
    moc_plan: dict[str, Any],
    surgery_sample_items: list[dict[str, Any]],
) -> dict[str, Any]:
    moc_summary = moc_plan.get("summary", {})
    if not isinstance(moc_summary, dict):
        moc_summary = {}
    admission = moc_plan.get("temperature_admission", {})
    if not isinstance(admission, dict):
        admission = {}
    counts = admission.get("counts", admission.get("summary", {}))
    if not isinstance(counts, dict):
        counts = {}
    blocked_relations = _string_list(admission.get("blocked_relations"))
    review_needed_relations = _string_list(admission.get("review_needed_relations"))
    admitted_relations = _string_list(admission.get("admitted_relations"))
    windows_value = admission.get("clue_windows", admission.get("windows", []))
    windows = [item for item in windows_value if isinstance(item, dict)] if isinstance(windows_value, list) else []
    review_windows = [
        window
        for window in windows
        if str(window.get("status", "")) == "needs_review"
        or str(window.get("relation_type") or window.get("relation") or "") in review_needed_relations
    ]
    compact_clues = [_compact_clue(window) for window in sorted(review_windows, key=_clue_sort_key)[:5]]
    mechanical_families = [
        {
            "relation_type": relation,
            "status": "blocked",
            "reason": "mechanical source/proximity relation; not a standalone MOC reading clue by default",
        }
        for relation in blocked_relations
        if relation in MECHANICAL_RELATION_FAMILIES
    ]
    orphan_relation_pages = [
        {
            "relation_type": str(item.get("key") or "").strip(),
            "path": str(item.get("path") or "").strip(),
            "surgery_candidate": True,
            "reason": "orphan generated relation MOC page; review as cleanup candidate, not active clue value",
        }
        for item in surgery_sample_items
        if item.get("action") == "orphan" and item.get("kind") == "relation"
    ]
    return {
        "kind": "moc_temperature",
        "script_result_summary": {
            "moc_projection": {
                "candidate_count": _safe_int(moc_summary.get("candidate_count")),
                "create_count": _safe_int(moc_summary.get("create_count")),
                "update_count": _safe_int(moc_summary.get("update_count")),
                "noop_count": _safe_int(moc_summary.get("noop_count")),
                "orphan_count": _safe_int(moc_summary.get("orphan_count")),
            },
            "temperature_admission": {
                "admitted": _safe_int(counts.get("admitted")),
                "blocked": _safe_int(counts.get("blocked")),
                "needs_review": _safe_int(counts.get("needs_review")),
                "total": _safe_int(counts.get("total")),
                "admitted_relations": admitted_relations,
                "blocked_relations": blocked_relations,
                "review_needed_relations": review_needed_relations,
            },
        },
        "interpreted_live_intent": (
            "The user is asking whether current MOC evidence contains real reading clues, "
            "not asking to apply MOC writes."
        ),
        "mechanical_relation_families": mechanical_families,
        "review_needed_clues": compact_clues,
        "orphan_relation_moc_pages": orphan_relation_pages,
        "confirmation_points": [
            "admit a specific clue candidate into review",
            "block a relation family",
            "route orphan relation MOC pages to cleanup surgery",
            "expand one object chain for deeper diagnosis",
            "keep everything read-only",
        ],
        "write_boundary": "read_only_no_files_written",
    }


def build_moc_surgery_preview_payload(
    root: Path | str,
    case_path: Path | str,
    moc_plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    case_file = Path(case_path).resolve()
    if root_path not in case_file.parents and case_file != root_path:
        raise ValueError("case path escapes root")
    case_package = load_medical_case_file(case_file)
    case_package["case_path"] = case_file.as_posix()
    if moc_plan is None:
        graph = load_graph(root_path, None)
        moc_plan = build_moc_plan(root_path, graph)
    surgery_plan = build_surgery_plan_from_case(case_package, moc_plan=moc_plan)
    moc_summary = dict(moc_plan.get("summary", {})) if isinstance(moc_plan, dict) else {}
    temperature_admission = (
        copy.deepcopy(moc_plan.get("temperature_admission", {})) if isinstance(moc_plan, dict) else {}
    )
    surgery_summary = surgery_plan.get("summary", {})
    moc_projection_count = 0
    if isinstance(surgery_summary, dict):
        moc_projection_count = int(surgery_summary.get("moc_projection_count", 0) or 0)
    return {
        "moc_projection": moc_summary,
        "temperature_admission": temperature_admission,
        "surgery_preview": {
            "moc_projection_count": moc_projection_count,
            "sample_items": _sample_moc_items(surgery_plan),
        },
        "next_action": (
            "review_moc_surgery_preview"
            if moc_projection_count > 0
            else "moc_projection_clean"
        ),
    }


def build_status_payload(root: Path | str, intent_text: str) -> dict[str, Any]:
    intent = classify_medical_intent(intent_text)
    resolution = resolve_active_case(root)
    validation = validate_resolved_case_action(resolution, intent.intent, intent.expected_count)
    payload: dict[str, Any] = {
        "intent": intent.intent,
        "case_path": resolution.case_path.as_posix() if resolution.case_path else "",
        "state": validation.state,
        "allowed": validation.allowed,
        "allowed_action": validation.allowed_action,
        "blocked_reason": validation.blocked_reason,
        "next_action": validation.allowed_action or validation.blocked_reason,
    }
    if resolution.status == "no_case":
        payload["next_action"] = "diagnose"
    if resolution.status == "blocked":
        payload["candidate_cases"] = [path.as_posix() for path in resolution.candidates]
        payload["next_action"] = "select_active_case"
    if resolution.case_package is not None:
        archive = resolution.case_package.get("archive_next_action", {})
        next_action = archive.get("next_action") if isinstance(archive, dict) else ""
        payload["executable_count"] = validation.executable_count
        payload["expected_count"] = validation.expected_count
        if validation.allowed and intent.intent == "moc_surgery_preview" and resolution.case_path is not None:
            payload.update(build_moc_surgery_preview_payload(root, resolution.case_path))
        elif validation.allowed and next_action:
            payload["next_action"] = str(next_action)
    return payload


def apply_confirmed_treatment_and_recover(
    root: Path | str,
    case_path: Path | str,
    approved_domains: set[str] | None = None,
    approved_detail_refs: set[str] | None = None,
) -> dict[str, Any]:
    root_path = Path(root).resolve()
    case_file = Path(case_path).resolve()
    if root_path not in case_file.parents and case_file != root_path:
        raise ValueError("case path escapes root")
    if not (approved_domains or approved_detail_refs):
        raise ValueError("missing explicit treatment approval")
    resolution = resolve_active_case(root_path)
    if resolution.status != "ok" or resolution.case_path is None or resolution.case_package is None:
        raise ValueError(resolution.blocked_reason or resolution.status)
    if resolution.case_path.resolve() != case_file:
        raise ValueError("supplied case path is not the active case")
    validation = validate_case_action(resolution.case_package, "treatment_apply")
    if not validation.allowed:
        raise ValueError(validation.blocked_reason or "treatment_apply_not_allowed")
    plan = load_case_and_build_treatment_plan(
        case_file,
        approved_domains=approved_domains or set(),
        approved_detail_refs=approved_detail_refs or set(),
    )
    result = apply_treatment_plan(root_path, plan, apply=True)
    treatment_record = write_treatment_record(plan, result, root_path)
    update_case_file_with_treatment_result(
        case_file,
        plan,
        result,
        root_path,
        treatment_record=treatment_record.as_posix(),
    )
    if result["summary"]["blocked_count"] > 0:
        case_package = load_medical_case_file(case_file)
        case_package["status"] = "blocked"
        case_package["archive_next_action"] = {
            "status": "blocked",
            "next_action": "blocked",
            "reason": "treatment blocked results must be resolved before recovery.",
        }
        overwrite_medical_case_file(case_file, case_package, root_path)
        return {
            "applied": result["summary"]["applied_count"],
            "blocked": result["summary"]["blocked_count"],
            "treatment_record": treatment_record.as_posix(),
            "next_action": "blocked",
        }
    recovery = build_recovery_package(
        root_path,
        frontmatter_targets=[
            str(item.get("path", ""))
            for item in plan.get("treatment_items", [])
            if isinstance(item, dict) and str(item.get("path", "")).strip()
        ],
    )
    recovery_record = write_recovery_record(recovery, root_path)
    case_package = load_medical_case_file(case_file)
    updated_case = attach_recovery_result_to_case(
        case_package,
        recovery,
        recovery_record=recovery_record.as_posix(),
    )
    overwrite_medical_case_file(case_file, updated_case, root_path)
    next_action = updated_case.get("archive_next_action", {}).get("next_action", "")
    return {
        "applied": result["summary"]["applied_count"],
        "blocked": result["summary"]["blocked_count"],
        "treatment_record": treatment_record.as_posix(),
        "recovery": {
            "status": updated_case["recovery"]["status"],
            "record": recovery_record.as_posix(),
            "passed": recovery.get("passed", False),
        },
        "next_action": next_action,
    }
