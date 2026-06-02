from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts.check_requirements_case import check_requirements_case_file
from scripts.requirements_case import load_requirements_case_file


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _dict_items(value: Any) -> list[dict[str, Any]]:
    return [item for item in _as_list(value) if isinstance(item, dict)]


def _string_list(value: Any) -> list[str]:
    return [str(item) for item in _as_list(value) if str(item).strip()]


def _blocker(code: str, reason: str) -> dict[str, str]:
    return {"code": code, "reason": reason}


def _safe_change_id(change_id: str) -> bool:
    text = str(change_id).strip()
    return bool(text) and Path(text).name == text and "/" not in text and "\\" not in text


def _story_trace(case_data: dict[str, Any]) -> list[dict[str, str]]:
    functions = {
        str(function.get("id", "")).strip(): function
        for function in _dict_items(case_data.get("acceptance_functions"))
        if str(function.get("id", "")).strip()
    }
    traces: list[dict[str, str]] = []
    for story in _dict_items(case_data.get("user_stories")):
        story_id = str(story.get("id", "")).strip() or "US-unknown"
        acceptance_ids = _string_list(story.get("acceptance_function_ids"))
        traces.append(
            {
                "story_id": story_id,
                "acceptance_ids": ", ".join(acceptance_ids) or "none",
                "role": str(story.get("role_ref") or story.get("role") or "").strip(),
                "want": str(story.get("want") or story.get("goal") or story.get("story") or story.get("summary") or "").strip(),
                "benefit": str(story.get("benefit") or story.get("value") or story.get("so_that") or "").strip(),
            }
        )
        for acceptance_id in acceptance_ids:
            function = functions.get(acceptance_id, {})
            traces.append(
                {
                    "story_id": story_id,
                    "acceptance_ids": acceptance_id,
                    "role": "",
                    "want": str(function.get("name") or function.get("summary") or function.get("then") or "").strip(),
                    "benefit": "acceptance trace",
                }
            )
    return traces


def _trace_lines(case_data: dict[str, Any]) -> list[str]:
    lines = []
    for trace in _story_trace(case_data):
        role = f" role={trace['role']}" if trace["role"] else ""
        lines.append(
            f"- {trace['story_id']} -> {trace['acceptance_ids']}:{role} "
            f"{trace['want']} ({trace['benefit']})".rstrip()
        )
    return lines or ["- No trace entries"]


def _proposal_markdown(change_id: str, case_file: Path, case_data: dict[str, Any], capability: str) -> str:
    domain = case_data.get("domain", {})
    confirmed_domain = domain.get("confirmed", "unknown") if isinstance(domain, dict) else "unknown"
    lines = [
        f"# {change_id}",
        "",
        "## Why",
        "",
        f"This draft was generated from requirements case `{case_file}` after the requirements hard gate passed.",
        "",
        "## What Changes",
        "",
        f"- Capability: {capability}",
        f"- Confirmed domain: {confirmed_domain}",
        "- Implementation requires user review before planning or coding.",
        "",
        "## Requirement Trace",
    ]
    lines.extend(_trace_lines(case_data))
    lines.extend(["", "## Out of Scope", "", "- Automatic implementation after draft creation."])
    return "\n".join(lines) + "\n"


def _design_markdown(case_file: Path, case_data: dict[str, Any]) -> str:
    lines = [
        "# Design",
        "",
        "## Source",
        "",
        f"- Requirements case: `{case_file}`",
        "- Requirements checker status: requirements_ready",
        "- Implementation requires user review.",
        "",
        "## Trace",
    ]
    lines.extend(_trace_lines(case_data))
    return "\n".join(lines) + "\n"


def _tasks_markdown(case_file: Path) -> str:
    return "\n".join(
        [
            "# Tasks",
            "",
            f"- [ ] 1. User reviews generated OpenSpec draft from `{case_file}`.",
            "- [ ] 2. Update proposal, design, tasks, and spec after review.",
            "- [ ] 3. Plan implementation only after user review is accepted.",
            "",
        ]
    )


def _spec_markdown(capability: str, case_data: dict[str, Any]) -> str:
    lines = ["## ADDED Requirements", ""]
    functions = {
        str(function.get("id", "")).strip(): function
        for function in _dict_items(case_data.get("acceptance_functions"))
        if str(function.get("id", "")).strip()
    }
    for story in _dict_items(case_data.get("user_stories")):
        story_id = str(story.get("id", "")).strip() or "US-unknown"
        want = str(story.get("want") or story.get("goal") or story.get("story") or story.get("summary") or "Requirement").strip()
        acceptance_ids = _string_list(story.get("acceptance_function_ids"))
        lines.extend([f"### Requirement: {want}", "", f"Trace: user story `{story_id}`; acceptance functions `{', '.join(acceptance_ids)}`.", ""])
        for acceptance_id in acceptance_ids:
            function = functions.get(acceptance_id, {})
            scenario = str(function.get("name") or function.get("summary") or acceptance_id).strip()
            given = str(function.get("given") or "the requirement preconditions are met").strip()
            when = str(function.get("when") or "the user performs the required action").strip()
            then = str(function.get("then") or function.get("expected") or scenario).strip()
            lines.extend([f"#### Scenario: {scenario}", "", f"Trace: user story `{story_id}`; acceptance function `{acceptance_id}`.", "", f"- **GIVEN** {given}", f"- **WHEN** {when}", f"- **THEN** {then}", ""])
    lines.extend([f"### Requirement: {capability} draft implementation requires review", "", "Implementation requires user review after draft creation.", "", "#### Scenario: Draft is created", "", "- **WHEN** the OpenSpec draft files are generated", "- **THEN** implementation remains blocked until user review is accepted", ""])
    return "\n".join(lines)


def create_openspec_draft_from_case(
    case_file: Path | str,
    change_id: str,
    repo_root: Path | str = ".",
    capability: str = "requirements-analysis-agent",
) -> dict[str, Any]:
    root = Path(repo_root)
    case_path = Path(case_file)
    readiness = check_requirements_case_file(case_path, repo_root=root, strict=True)
    if readiness.get("summary", {}).get("status") != "requirements_ready":
        return {"status": "blocked", "reason": "requirements_not_ready", "blockers": _dict_items(readiness.get("blockers")), "checker": readiness, "created_files": [], "requires_user_review": True}

    if not _safe_change_id(change_id):
        return {"status": "blocked", "reason": "invalid_change_id", "blockers": [_blocker("invalid_change_id", "change id must be a single path segment")], "checker": readiness, "created_files": [], "requires_user_review": True}
    if not _safe_change_id(capability):
        return {"status": "blocked", "reason": "invalid_capability", "blockers": [_blocker("invalid_capability", "capability must be a single path segment")], "checker": readiness, "created_files": [], "requires_user_review": True}

    change_dir = root / "openspec" / "changes" / change_id
    if change_dir.exists():
        return {"status": "blocked", "reason": "change_id_collision", "blockers": [_blocker("change_id_collision", f"OpenSpec change `{change_id}` already exists; choose a different change id or explicitly select the existing change.")], "checker": readiness, "created_files": [], "requires_user_review": True}

    case_data = load_requirements_case_file(case_path)
    spec_dir = change_dir / "specs" / capability
    (root / "openspec" / "changes").mkdir(parents=True, exist_ok=True)
    spec_dir.mkdir(parents=True)
    files = {
        change_dir / "proposal.md": _proposal_markdown(change_id, case_path, case_data, capability),
        change_dir / "design.md": _design_markdown(case_path, case_data),
        change_dir / "tasks.md": _tasks_markdown(case_path),
        spec_dir / "spec.md": _spec_markdown(capability, case_data),
    }
    created_files: list[str] = []
    for path, content in files.items():
        with path.open("x", encoding="utf-8") as handle:
            handle.write(content)
        created_files.append(str(path))

    return {"status": "draft_created", "reason": "requirements_ready", "blockers": [], "checker": readiness, "change_dir": str(change_dir), "created_files": created_files, "requires_user_review": True}
