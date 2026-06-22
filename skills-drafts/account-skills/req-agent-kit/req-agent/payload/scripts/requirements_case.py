from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REQUIREMENTS_CASE_DIR = Path("wiki/ops/requirements-cases")
CASE_DATA_START = "<!-- requirements-case-data:start -->"
CASE_DATA_END = "<!-- requirements-case-data:end -->"

CASE_STATUSES = {"intake", "diagnose", "awaiting_confirmation", "candidate_pending", "requirements_ready", "blocked", "recovery_required", "archived"}
DEFAULT_PROOF_BOUNDARY_NOTES = [
    "This case file records requirement readiness evidence.",
    "Hard-gate validation belongs to the requirements checker.",
    "API, DDL, and release details are supporting evidence, not first-version requirement authority.",
]
DEFAULT_DETAILED_DESIGN_HARD_GATES = [
    {
        "gate": "current_state_material_package",
        "hard_gate": True,
        "material_status": "missing",
        "required_from": "product_owner_or_requirement_proposer",
        "required_material": (
            "Current-state material package: current subscription, payment, billing, "
            "entitlement, split, settlement, payout, and reconciliation flows, with "
            "process diagrams, screenshots, configuration samples, contract terms, "
            "invoice/accounting examples, or an explicit greenfield confirmation."
        ),
        "pass_condition": (
            "Product provides referenceable materials, or explicitly confirms there is "
            "no existing system/manual flow and gives first-release constraints."
        ),
        "blocks_until_passed": "Detailed design, API contracts, DDL/schema design, state machines, and engineering breakdown.",
    },
    {
        "gate": "business_rule_position_table",
        "hard_gate": True,
        "material_status": "missing",
        "required_from": "product_owner_with_rule_owner_and_settlement_owner",
        "required_material": (
            "Business rule position table: first-release and deferred scope for "
            "platform fees, service-provider split, rounding residuals, refunds, "
            "chargebacks, compensation, taxes, settlement conditions, payout failure, "
            "and reconciliation exceptions."
        ),
        "pass_condition": (
            "Product states whether each rule is in first release, who owns it, and "
            "which business position applies; deferred rules have explicit boundaries."
        ),
        "blocks_until_passed": "Rule model, amount calculation, settlement batch generation, reverse split, and exception handling design.",
    },
    {
        "gate": "system_boundary_contract_table",
        "hard_gate": True,
        "material_status": "missing",
        "required_from": "product_owner_with_platform_relationship_owner_and_agent_service_owner",
        "required_material": (
            "System boundary contract table: APIs, events, callbacks, idempotency keys, "
            "failure recovery, responsibility ownership, and data owners between Agent "
            "service offering, usage, seat, entitlement, and subscription payment systems."
        ),
        "pass_condition": (
            "Product identifies which system initiates each handoff, which system owns "
            "the resulting fact, how failures recover, and who owns required fields."
        ),
        "blocks_until_passed": "API design, event design, entitlement linkage, usage billing linkage, and end-to-end sequence design.",
    },
]


def _iso_timestamp(timestamp: datetime | str | None = None) -> str:
    if timestamp is None:
        return datetime.now(timezone.utc).isoformat()
    if isinstance(timestamp, datetime):
        return timestamp.astimezone(timezone.utc).isoformat()
    return timestamp


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


def _slugify(value: str | None) -> str:
    text = str(value or "requirements-case").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "requirements-case"


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _copy_dict_list(value: Any) -> list[dict[str, Any]]:
    return [copy.deepcopy(item) for item in _as_list(value) if isinstance(item, dict)]


def _copy_dict(value: Any) -> dict[str, Any]:
    return copy.deepcopy(value) if isinstance(value, dict) else {}


def _attachment_dict(value: Any) -> dict[str, list[str]]:
    if not isinstance(value, dict):
        return {}
    attachments: dict[str, list[str]] = {}
    for key, items in sorted(value.items()):
        values = [str(item) for item in _as_list(items) if str(item).strip()]
        attachments[str(key)] = values
    return attachments


def build_requirements_case_package(
    *,
    case_slug: str | None = None,
    status: str = "intake",
    active: bool = True,
    current_intent: dict[str, Any] | None = None, domain: dict[str, Any] | None = None,
    roles: list[dict[str, Any]] | None = None, user_stories: list[dict[str, Any]] | None = None,
    acceptance_functions: list[dict[str, Any]] | None = None, soft_evidence: dict[str, Any] | None = None,
    domain_coverage: list[dict[str, Any]] | None = None,
    blockers: list[dict[str, Any]] | None = None, evidence_attachments: dict[str, list[str]] | None = None,
    proof_boundary_notes: list[str] | None = None, case_source: dict[str, Any] | None = None,
    timestamp: datetime | str | None = None,
) -> dict[str, Any]:
    normalized_status = status if status in CASE_STATUSES else str(status or "intake")
    normalized_soft_evidence = _copy_dict(soft_evidence)
    normalized_soft_evidence.setdefault(
        "detailed_design_hard_gates",
        copy.deepcopy(DEFAULT_DETAILED_DESIGN_HARD_GATES),
    )
    return {
        "generated_at": _iso_timestamp(timestamp),
        "mode": "requirements_case",
        "case_slug": _slugify(case_slug),
        "status": normalized_status,
        "active": bool(active),
        "current_intent": _copy_dict(current_intent),
        "case_source": _copy_dict(case_source),
        "domain": {
            "status": str((domain or {}).get("status", "candidate_pending")),
            "confirmed": str((domain or {}).get("confirmed", "")),
            "candidates": _copy_dict_list((domain or {}).get("candidates", [])),
        },
        "roles": _copy_dict_list(roles or []),
        "user_stories": _copy_dict_list(user_stories or []),
        "acceptance_functions": _copy_dict_list(acceptance_functions or []),
        "domain_coverage": _copy_dict_list(domain_coverage or []),
        "soft_evidence": normalized_soft_evidence,
        "blockers": _copy_dict_list(blockers or []),
        "readiness_next_action": {
            "status": normalized_status,
            "next_action": "run_requirements_checker",
            "reason": "Hard-gate validation belongs to the requirements checker lifecycle.",
        },
        "evidence_attachments": _attachment_dict(evidence_attachments or {}),
        "proof_boundary_notes": [
            str(note)
            for note in _as_list(proof_boundary_notes or DEFAULT_PROOF_BOUNDARY_NOTES)
        ],
    }


def _frontmatter_lines(package: dict[str, Any]) -> list[str]:
    created_at = str(package.get("generated_at", "")).split("T", 1)[0] or datetime.now(timezone.utc).date().isoformat()
    return [
        "---",
        "layer: ops",
        "domain: unclassified",
        "classification_needed: true",
        "ops_area: workflow-trace",
        "canonical_object: requirements-case-file",
        "artifact_type: requirements-case",
        f"status: {package.get('status', 'intake')}",
        f"case_slug: {package.get('case_slug', 'requirements-case')}",
        f"created_at: {created_at}",
        "---",
        "",
    ]


def _summary_lines(value: Any) -> list[str]:
    if isinstance(value, dict) and value:
        return [f"- {key}: {value[key]}" for key in sorted(value)]
    if isinstance(value, list) and value:
        return [f"- {item}" for item in value]
    return ["- None"]


def _role_line(item: dict[str, Any]) -> str:
    role_id = str(item.get("id") or item.get("role") or "unknown")
    mention = str(item.get("mention") or item.get("label") or role_id)
    confirmed_as = str(item.get("confirmed_as", ""))
    status = str(item.get("status", ""))
    category = str(item.get("category", ""))
    parts = [
        mention,
        f"confirmed_as={confirmed_as}" if confirmed_as else "",
        f"status={status}" if status else "",
        f"category={category}" if category else "",
    ]
    return f"- {role_id}: {'; '.join(part for part in parts if part)}"


def _story_line(item: dict[str, Any]) -> str:
    story_id = str(item.get("id", "unknown"))
    role_ref = str(item.get("role_ref", ""))
    role = str(item.get("role", ""))
    role_part = f"role_ref={role_ref}" if role_ref else f"role={role}" if role else ""
    want = str(item.get("want") or item.get("story") or item.get("summary") or "")
    benefit = str(item.get("benefit", ""))
    refs = ", ".join(str(ref) for ref in _as_list(item.get("acceptance_function_ids")))
    parts = [
        part
        for part in [
            role_part,
            want,
            f"benefit={benefit}" if benefit else "",
            f"acceptance={refs}" if refs else "",
        ]
        if part
    ]
    return f"- {story_id}: {'; '.join(parts)}" if parts else f"- {story_id}"


def _acceptance_line(item: dict[str, Any]) -> str:
    function_id = str(item.get("id", "unknown"))
    name = str(item.get("name") or item.get("summary") or "")
    refs = ", ".join(str(ref) for ref in _as_list(item.get("user_story_ids")))
    coverage = ", ".join(str(ref) for ref in _as_list(item.get("coverage_types")))
    parts = [part for part in [name, f"stories={refs}" if refs else "", f"coverage={coverage}" if coverage else "", str(item.get("then", ""))] if part]
    return f"- {function_id}: {'; '.join(parts)}" if parts else f"- {function_id}"


def _coverage_line(item: dict[str, Any]) -> str:
    subdomain = str(item.get("subdomain") or item.get("domain") or "unknown")
    coverage_type = str(item.get("coverage_type") or item.get("type") or "")
    contexts = ", ".join(str(ref) for ref in _as_list(item.get("contexts")))
    aggregates = ", ".join(str(ref) for ref in _as_list(item.get("aggregate_roots")))
    stories = ", ".join(str(ref) for ref in _as_list(item.get("user_story_ids") or item.get("user_stories")))
    functions = ", ".join(str(ref) for ref in _as_list(item.get("acceptance_function_ids") or item.get("acceptance_functions")))
    note = str(item.get("review_note") or item.get("reason") or item.get("next_action") or "")
    parts = [
        part
        for part in [
            f"coverage_type={coverage_type}" if coverage_type else "",
            f"contexts={contexts}" if contexts else "",
            f"aggregates={aggregates}" if aggregates else "",
            f"stories={stories}" if stories else "",
            f"acceptance={functions}" if functions else "",
            f"note={note}" if note else "",
        ]
        if part
    ]
    return f"- {subdomain}: {'; '.join(parts)}" if parts else f"- {subdomain}"


def _domain_coverage(package: dict[str, Any]) -> list[dict[str, Any]]:
    coverage = _copy_dict_list(package.get("domain_coverage", []))
    if coverage:
        return coverage
    soft_evidence = package.get("soft_evidence", {})
    if isinstance(soft_evidence, dict):
        return _copy_dict_list(soft_evidence.get("domain_coverage_matrix", []))
    return []


def render_requirements_case_markdown(package: dict[str, Any], scan_root: Path | str) -> str:
    lines = _frontmatter_lines(package)
    lines.extend(
        [
            "# requirements-case",
            "",
            "## Case Source",
            f"- Generated at: {package.get('generated_at', 'unknown')}",
            f"- Scan root: `{Path(scan_root)}`",
        ]
    )
    lines.extend(_summary_lines(package.get("case_source", {})))

    lines.extend(["", "## Intent"])
    lines.extend(_summary_lines(package.get("current_intent", {})))

    domain = package.get("domain", {})
    lines.extend(["", "## Domain"])
    if isinstance(domain, dict):
        lines.append(f"- Status: {domain.get('status', 'candidate_pending')}")
        lines.append(f"- Confirmed: {domain.get('confirmed', '')}")
        lines.append("### Candidates")
        candidates = _copy_dict_list(domain.get("candidates", []))
        lines.extend([f"- {item.get('id', 'unknown')}: {item.get('reason', '')}" for item in candidates] or ["- None"])
    else:
        lines.append("- None")

    lines.extend(["", "## Domain Coverage"])
    lines.extend([_coverage_line(item) for item in _domain_coverage(package)] or ["- None"])

    lines.extend(["", "## Roles"])
    lines.extend([_role_line(item) for item in _copy_dict_list(package.get("roles", []))] or ["- None"])

    lines.extend(["", "## User Stories"])
    lines.extend([_story_line(item) for item in _copy_dict_list(package.get("user_stories", []))] or ["- None"])

    lines.extend(["", "## Acceptance Functions"])
    lines.extend([_acceptance_line(item) for item in _copy_dict_list(package.get("acceptance_functions", []))] or ["- None"])

    lines.extend(["", "## Soft Evidence"])
    soft_evidence = package.get("soft_evidence", {})
    if isinstance(soft_evidence, dict) and soft_evidence:
        for key in sorted(soft_evidence):
            lines.append(f"### {str(key).replace('_', ' ').title()}")
            values = soft_evidence[key]
            if isinstance(values, list):
                lines.extend([f"- {json.dumps(item, ensure_ascii=False, sort_keys=True)}" for item in values] or ["- None"])
            else:
                lines.append(f"- {values}")
    else:
        lines.append("- None")

    lines.extend(["", "## Readiness / Next Action"])
    readiness = package.get("readiness_next_action", {})
    if isinstance(readiness, dict):
        lines.append(f"- Status: {readiness.get('status', package.get('status', 'intake'))}")
        lines.append(f"- Next action: {readiness.get('next_action', '')}")
        lines.append(f"- Reason: {readiness.get('reason', '')}")
    blockers = _copy_dict_list(package.get("blockers", []))
    lines.append("### Blockers")
    lines.extend([f"- {item.get('id', 'blocker')}: {item.get('reason', item.get('summary', ''))}" for item in blockers] or ["- None"])

    lines.extend(["", "## Evidence Attachments"])
    evidence = package.get("evidence_attachments", {})
    if isinstance(evidence, dict) and evidence:
        for key in sorted(evidence):
            lines.append(f"### {str(key).title()}")
            lines.extend([f"- `{value}`" for value in _as_list(evidence.get(key))] or ["- None"])
    else:
        lines.append("- None")

    lines.extend(["", "## Proof Boundary"])
    lines.extend([f"- {note}" for note in _as_list(package.get("proof_boundary_notes"))] or ["- None"])

    machine_json = json.dumps(package, ensure_ascii=False, indent=2, sort_keys=True)
    lines.extend(
        [
            "",
            "## Machine Case Data",
            CASE_DATA_START,
            "```json",
            machine_json,
            "```",
            CASE_DATA_END,
        ]
    )
    return "\n".join(lines) + "\n"


def next_requirements_case_path(output_dir: Path, case_slug: str | None = None, timestamp: datetime | str | None = None) -> Path:
    slug = _timestamp_slug(timestamp)
    case_part = _slugify(case_slug)
    base = output_dir / f"{slug}-{case_part}.md"
    if not base.exists():
        return base
    counter = 2
    while True:
        candidate = output_dir / f"{slug}-{case_part}-{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def write_requirements_case_file(package: dict[str, Any], root: Path | str, output_dir: Path | str | None = None, timestamp: datetime | str | None = None) -> Path:
    root_path = Path(root)
    target_dir = Path(output_dir) if output_dir is not None else root_path / DEFAULT_REQUIREMENTS_CASE_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    markdown = render_requirements_case_markdown(package, scan_root=root_path)
    while True:
        target = next_requirements_case_path(target_dir, case_slug=str(package.get("case_slug", "")), timestamp=timestamp)
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(markdown)
            return target.resolve()
        except FileExistsError:
            continue


def load_requirements_case_file(path: Path | str) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    start = text.find(CASE_DATA_START)
    end = text.find(CASE_DATA_END)
    if start < 0 or end < 0 or end <= start:
        raise ValueError(f"requirements case data block not found: {path}")
    data = text[start + len(CASE_DATA_START) : end].strip()
    if data.startswith("```json"):
        data = data[len("```json") :].strip()
    if data.endswith("```"):
        data = data[:-3].strip()
    payload = json.loads(data)
    if not isinstance(payload, dict):
        raise ValueError(f"requirements case data is not an object: {path}")
    return payload
