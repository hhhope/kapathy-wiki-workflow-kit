from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

from scripts.requirements_ddd_readiness import (
    evaluate_domain_model_gate,
    known_domain_ids,
    role_lookup as ddd_role_lookup,
    soft_evidence_categories,
    taxonomy_version,
)
from scripts.requirements_case import load_requirements_case_file
from scripts.requirements_domain_coverage import evaluate_domain_coverage_gate


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")
READY_STATUS = "requirements_ready"
BLOCKED_STATUS = "blocked"
DETAILED_DESIGN_HARD_GATE_IDS = {
    "current_state_material_package",
    "business_rule_position_table",
    "system_boundary_contract_table",
}
DETAILED_DESIGN_PASS_STATUSES = {"provided", "waived"}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _dict_items(value: Any) -> list[dict[str, Any]]:
    return [item for item in _as_list(value) if isinstance(item, dict)]


def _string_list(value: Any) -> list[str]:
    return [str(item) for item in _as_list(value) if str(item).strip()]


def _load_taxonomy(repo_root: Path | str) -> dict[str, Any]:
    taxonomy_file = Path(repo_root) / TAXONOMY_PATH
    with taxonomy_file.open(encoding="utf-8") as handle:
        taxonomy = yaml.safe_load(handle)
    if not isinstance(taxonomy, dict):
        raise ValueError(f"requirements taxonomy is not an object: {taxonomy_file}")
    return taxonomy


def _known_domains(taxonomy: dict[str, Any]) -> set[str]:
    return known_domain_ids(taxonomy)


def _role_lookup(taxonomy: dict[str, Any], *, include_legacy: bool = True) -> dict[str, str]:
    return ddd_role_lookup(taxonomy, include_legacy=include_legacy)


def _blocker(
    code: str,
    reason: str,
    *,
    field: str = "",
    question: str = "",
    evidence: str = "",
) -> dict[str, str]:
    item = {"code": code, "reason": reason}
    if field:
        item["field"] = field
    if question:
        item["question"] = question
    if evidence:
        item["evidence"] = evidence
    return item


def _has_value(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set)):
        return any(_has_value(item) for item in value)
    if isinstance(value, dict):
        return any(_has_value(item) for item in value.values())
    return False


def has_evidence_anchor(item: dict[str, Any], object_type: str) -> bool:
    common_fields = (
        "evidence_refs",
        "evidence_anchor",
        "source_section",
        "source_quote",
        "source_line",
    )
    if any(_has_value(item.get(field)) for field in common_fields):
        return True
    if object_type == "user_story":
        return _has_value(item.get("source_functions"))
    if object_type == "acceptance_function":
        return _has_value(item.get("source_acceptance")) or _has_value(item.get("source_functions"))
    if object_type == "role":
        return _has_value(item.get("source_actors")) and _has_value(item.get("normalization_note"))
    return False


def _role_confirmed_as(role: dict[str, Any]) -> str:
    return str(role.get("confirmed_as") or role.get("id") or role.get("role") or role.get("label") or "").strip()


def _role_instance_id(role: dict[str, Any]) -> str:
    return str(role.get("id") or role.get("role") or role.get("label") or "").strip()


def _first_text(item: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        value = str(item.get(key, "")).strip()
        if value:
            return value
    return ""


def _soft_evidence_report(taxonomy: dict[str, Any], case_data: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    categories = soft_evidence_categories(taxonomy)
    soft_evidence = case_data.get("soft_evidence", {})
    warnings: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    if not isinstance(categories, dict) or not isinstance(soft_evidence, dict):
        return warnings, evidence

    for category_id in sorted(categories):
        values = _as_list(soft_evidence.get(category_id))
        if not values:
            continue
        category = categories[category_id]
        classification = str(category.get("classification", "")) if isinstance(category, dict) else ""
        item = {
            "category": str(category_id),
            "classification": classification,
            "count": str(len(values)),
        }
        if classification == "soft_warning":
            warnings.append(item)
        else:
            evidence.append(item)
    return warnings, evidence


def _detailed_design_gate(case_data: dict[str, Any]) -> dict[str, Any]:
    soft_evidence = case_data.get("soft_evidence", {})
    values = soft_evidence.get("detailed_design_hard_gates", []) if isinstance(soft_evidence, dict) else []
    gates = _dict_items(values)
    gates_by_id = {str(gate.get("gate", "")).strip(): gate for gate in gates if str(gate.get("gate", "")).strip()}
    blockers: list[dict[str, str]] = []

    for gate_id in sorted(DETAILED_DESIGN_HARD_GATE_IDS):
        gate = gates_by_id.get(gate_id)
        if gate is None:
            blockers.append(
                _blocker(
                    "detailed_design_gate_missing",
                    f"detailed design hard gate is missing: {gate_id}",
                    field="soft_evidence.detailed_design_hard_gates",
                    evidence=gate_id,
                )
            )
            blockers[-1]["gate"] = gate_id
            continue

        status = str(gate.get("material_status", "")).strip()
        has_material_evidence = _has_value(gate.get("evidence_ref")) or _has_value(gate.get("evidence_refs"))
        has_waiver_evidence = _has_value(gate.get("waiver_reason")) or _has_value(gate.get("waiver_ref"))
        if status == "provided" and has_material_evidence:
            continue
        if status == "waived" and has_waiver_evidence:
            continue

        if status not in DETAILED_DESIGN_PASS_STATUSES:
            reason = f"detailed design hard gate {gate_id} requires product material or explicit waiver; material_status={status or 'missing'}"
        elif status == "provided":
            reason = f"detailed design hard gate {gate_id} is marked provided but has no evidence_ref or evidence_refs"
        else:
            reason = f"detailed design hard gate {gate_id} is marked waived but has no waiver_reason or waiver_ref"
        blockers.append(
            _blocker(
                "detailed_design_gate_not_satisfied",
                reason,
                field="soft_evidence.detailed_design_hard_gates",
                evidence=gate_id,
            )
        )
        blockers[-1]["gate"] = gate_id

    return {
        "passed": not blockers,
        "mode": "product_materials_required",
        "required_gates": sorted(DETAILED_DESIGN_HARD_GATE_IDS),
        "blockers": sorted(blockers, key=lambda item: (item.get("gate", ""), item["reason"])),
    }


def check_requirements_case(case_data: dict[str, Any], taxonomy: dict[str, Any], *, strict: bool = True) -> dict[str, Any]:
    blockers: list[dict[str, str]] = []
    domains = _known_domains(taxonomy)
    legacy_compatible = False
    use_ddd_gate = strict and taxonomy_version(taxonomy) == 2
    role_lookup = _role_lookup(taxonomy, include_legacy=not use_ddd_gate)
    domain_model_gate, domain_model_blockers = evaluate_domain_model_gate(case_data, taxonomy, strict=strict)
    domain_coverage_gate, domain_coverage_blockers = evaluate_domain_coverage_gate(case_data, taxonomy, strict=strict)
    blockers.extend(domain_model_blockers)
    blockers.extend(domain_coverage_blockers)

    if not use_ddd_gate:
        domain = case_data.get("domain", {})
        domain_status = str(domain.get("status", "")) if isinstance(domain, dict) else ""
        confirmed_domain = str(domain.get("confirmed", "")).strip() if isinstance(domain, dict) else ""
        if domain_status != "confirmed" or not confirmed_domain or confirmed_domain not in domains:
            blockers.append(
                _blocker(
                    "domain_not_confirmed_known",
                    f"domain must be confirmed and known; status={domain_status or 'missing'} confirmed={confirmed_domain or 'missing'}",
                )
            )

    case_roles = _dict_items(case_data.get("roles"))
    declared_roles: set[str] = set()
    role_instances: dict[str, dict[str, Any]] = {}
    if not case_roles:
        blockers.append(_blocker("roles_missing", "roles are required"))
    for role in case_roles:
        role_id = _role_instance_id(role)
        if role_id:
            role_instances[role_id] = role
        taxonomy_role = _role_confirmed_as(role)
        canonical = role_lookup.get(taxonomy_role)
        if not taxonomy_role or not canonical:
            blockers.append(_blocker("role_unknown", f"role is missing or unknown: {taxonomy_role or 'missing'}"))
        else:
            declared_roles.add(canonical)
        if strict and str(role.get("status", "")).strip() == "confirmed" and not has_evidence_anchor(role, "role"):
            blockers.append(
                _blocker(
                    "role_evidence_missing",
                    f"confirmed role {role_id or taxonomy_role or 'missing'} has no evidence anchor",
                    field="roles",
                    evidence=role_id or taxonomy_role,
                )
            )

    stories = _dict_items(case_data.get("user_stories"))
    story_ids = {str(story.get("id", "")).strip() for story in stories if str(story.get("id", "")).strip()}
    if not stories:
        blockers.append(_blocker("user_stories_missing", "user_stories are required"))

    functions = _dict_items(case_data.get("acceptance_functions"))
    function_ids = {str(function.get("id", "")).strip() for function in functions if str(function.get("id", "")).strip()}
    if not functions:
        blockers.append(_blocker("acceptance_functions_missing", "acceptance_functions are required"))

    for story in stories:
        story_id = str(story.get("id", "")).strip() or "missing"
        if strict:
            story_role_ref = str(story.get("role_ref", "")).strip()
            referenced_role = role_instances.get(story_role_ref)
            if not story_role_ref:
                blockers.append(_blocker("story_role_ref_missing", f"user story {story_id} has no role_ref", field="user_stories"))
            elif referenced_role is None:
                blockers.append(
                    _blocker(
                        "story_role_ref_unknown",
                        f"user story {story_id} references unknown role_ref: {story_role_ref}",
                        field="user_stories",
                        evidence=story_role_ref,
                    )
                )
            else:
                role_status = str(referenced_role.get("status", "")).strip()
                role_taxonomy = str(referenced_role.get("confirmed_as", "")).strip()
                role_canonical = role_lookup.get(role_taxonomy)
                if role_status != "confirmed":
                    blockers.append(
                        _blocker(
                            "story_role_not_confirmed",
                            f"user story {story_id} references role {story_role_ref} with status={role_status or 'missing'}",
                            field="user_stories",
                            evidence=story_role_ref,
                        )
                    )
                if not role_canonical:
                    blockers.append(
                        _blocker(
                            "story_role_taxonomy_unknown",
                            f"user story {story_id} references role {story_role_ref} with unknown taxonomy role: {role_taxonomy or 'missing'}",
                            field="user_stories",
                            evidence=story_role_ref,
                        )
                    )
            if not has_evidence_anchor(story, "user_story"):
                blockers.append(
                    _blocker(
                        "story_evidence_missing",
                        f"user story {story_id} has no evidence anchor",
                        field="user_stories",
                        evidence=story_id,
                    )
                )
        else:
            story_role = str(story.get("role", "")).strip()
            story_role_canonical = role_lookup.get(story_role)
            if not story_role:
                blockers.append(_blocker("story_role_missing", f"user story {story_id} has no role"))
            elif not story_role_canonical:
                blockers.append(_blocker("story_role_unknown", f"user story {story_id} has unknown role: {story_role}"))
            elif story_role_canonical not in declared_roles:
                blockers.append(_blocker("story_role_not_declared", f"user story {story_id} role is not declared: {story_role}"))
            else:
                legacy_compatible = True
        if not _first_text(story, ("want", "goal", "story", "summary")):
            blockers.append(_blocker("story_goal_missing", f"user story {story_id} has no want, goal, story, or summary"))
        if not _first_text(story, ("benefit", "value", "so_that")):
            blockers.append(_blocker("story_value_missing", f"user story {story_id} has no benefit, value, or so_that"))
        refs = _string_list(story.get("acceptance_function_ids"))
        if not refs:
            blockers.append(_blocker("story_acceptance_mapping_missing", f"user story {story_id} has no acceptance_function_ids"))
            continue
        missing_refs = [ref for ref in refs if ref not in function_ids]
        if missing_refs:
            blockers.append(
                _blocker(
                    "story_acceptance_mapping_unknown",
                    f"user story {story_id} references missing acceptance functions: {', '.join(sorted(missing_refs))}",
                )
            )

    for function in functions:
        function_id = str(function.get("id", "")).strip() or "missing"
        story_refs = _string_list(function.get("user_story_ids"))
        if not story_refs:
            blockers.append(_blocker("acceptance_story_mapping_missing", f"acceptance function {function_id} has no user_story_ids"))
        if not _first_text(function, ("then", "expected", "summary", "name")):
            blockers.append(_blocker("acceptance_observable_missing", f"acceptance function {function_id} has no observable then, expected, summary, or name"))
        missing_story_refs = [ref for ref in story_refs if ref not in story_ids]
        if missing_story_refs:
            blockers.append(
                _blocker(
                    "acceptance_story_mapping_unknown",
                    f"acceptance function {function_id} references missing user stories: {', '.join(sorted(missing_story_refs))}",
                )
            )
        if strict and not has_evidence_anchor(function, "acceptance_function"):
            blockers.append(
                _blocker(
                    "acceptance_evidence_missing",
                    f"acceptance function {function_id} has no evidence anchor",
                    field="acceptance_functions",
                    evidence=function_id,
                )
            )

    delivery_blockers = [
        blocker
        for blocker in blockers
        if not blocker["code"].startswith("domain_model_")
        and not blocker["code"].startswith("domain_coverage_")
    ]
    requirement_delivery_gate = {
        "passed": not delivery_blockers,
        "mode": "strict" if strict else "legacy_compatibility",
    }
    detailed_design_gate = _detailed_design_gate(case_data)
    warnings, evidence = _soft_evidence_report(taxonomy, case_data)
    status = READY_STATUS if not blockers else BLOCKED_STATUS
    return {
        "summary": {
            "status": status,
            "hard_gate_passed": not blockers,
            "taxonomy_path": str(TAXONOMY_PATH),
            "case_slug": str(case_data.get("case_slug", "")),
            "strict": strict,
            "legacy_compatible": legacy_compatible,
        },
        "domain_model_gate": domain_model_gate,
        "domain_coverage_gate": domain_coverage_gate,
        "requirement_delivery_gate": requirement_delivery_gate,
        "detailed_design_gate": detailed_design_gate,
        "blockers": sorted(blockers, key=lambda item: (item["code"], item["reason"])),
        "warnings": warnings,
        "evidence": evidence,
    }


def check_requirements_case_file(case_file: Path | str, repo_root: Path | str = ".", *, strict: bool = True) -> dict[str, Any]:
    taxonomy = _load_taxonomy(repo_root)
    case_data = load_requirements_case_file(case_file)
    return check_requirements_case(case_data, taxonomy, strict=strict)


def render_markdown_report(report: dict[str, Any]) -> str:
    lines = [
        "# Requirements Case Check",
        "",
        f"- Status: {report.get('summary', {}).get('status', BLOCKED_STATUS)}",
        f"- Hard gate passed: {report.get('summary', {}).get('hard_gate_passed', False)}",
        f"- Taxonomy: `{report.get('summary', {}).get('taxonomy_path', TAXONOMY_PATH)}`",
        f"- Detailed design gate passed: {report.get('detailed_design_gate', {}).get('passed', False)}",
        "",
        "## Blockers",
    ]
    blockers = _dict_items(report.get("blockers"))
    lines.extend([f"- {item.get('code')}: {item.get('reason')}" for item in blockers] or ["- None"])
    lines.append("")
    lines.append("## Detailed Design Gate")
    design_gate = report.get("detailed_design_gate", {})
    design_blockers = _dict_items(design_gate.get("blockers")) if isinstance(design_gate, dict) else []
    lines.extend([f"- {item.get('gate')}: {item.get('reason')}" for item in design_blockers] or ["- None"])
    lines.append("")
    lines.append("## Warnings")
    warnings = _dict_items(report.get("warnings"))
    lines.extend([f"- {item.get('category')}: {item.get('classification')} ({item.get('count')})" for item in warnings] or ["- None"])
    lines.append("")
    lines.append("## Evidence")
    evidence = _dict_items(report.get("evidence"))
    lines.extend([f"- {item.get('category')}: {item.get('classification')} ({item.get('count')})" for item in evidence] or ["- None"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check requirements case readiness.")
    parser.add_argument("case_file")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--compat", action="store_true", help="Use legacy story.role compatibility mode.")
    args = parser.parse_args()

    report = check_requirements_case_file(args.case_file, repo_root=args.repo_root, strict=not args.compat)
    if args.format == "markdown":
        print(render_markdown_report(report), end="")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["summary"]["hard_gate_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
