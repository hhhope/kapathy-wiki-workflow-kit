from __future__ import annotations

from typing import Any

from scripts.requirements_ddd_readiness import taxonomy_version


IN_SCOPE_COVERAGE_TYPES = {
    "full_coverage",
    "primary",
    "required_payment",
    "conditional_payment_in_scope",
    "adjacent_agent_service",
    "adjacent_agent_service_conditional",
    "supporting_payment",
}
EXPLICIT_NON_FULL_COVERAGE_TYPES = {"light_coverage", "out_of_scope", "follow_up"}
KNOWN_COVERAGE_TYPES = IN_SCOPE_COVERAGE_TYPES | EXPLICIT_NON_FULL_COVERAGE_TYPES
REQUIRED_ACCEPTANCE_TYPES = {"state_change", "handoff", "failure_path", "evidence"}
FAILURE_CONTEXTS = {"revenue_recovery_context", "payment_attempt_authorization_context"}
FAILURE_AGGREGATES = {"dunning_case", "grace_period", "retry_schedule", "payment_attempt"}
EVIDENCE_CONTEXTS = {
    "balance_ledger_context",
    "reconciliation_context",
    "split_allocation_context",
    "settlement_batch_context",
    "payout_context",
}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _dict_items(value: Any) -> list[dict[str, Any]]:
    return [item for item in _as_list(value) if isinstance(item, dict)]


def _string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        value = [value]
    return [str(item).strip() for item in _as_list(value) if str(item).strip()]


def _blocker(code: str, reason: str, *, field: str = "", evidence: str = "") -> dict[str, str]:
    item = {"code": code, "reason": reason}
    if field:
        item["field"] = field
    if evidence:
        item["evidence"] = evidence
    return item


def _known_sets(taxonomy: dict[str, Any]) -> tuple[set[str], set[str], set[str]]:
    subdomains = taxonomy.get("subdomains", {})
    contexts = taxonomy.get("bounded_contexts", {})
    known_subdomains = set(subdomains) if isinstance(subdomains, dict) else set()
    known_contexts = set(contexts) if isinstance(contexts, dict) else set()
    known_aggregates: set[str] = set()
    for collection in (subdomains, contexts):
        if not isinstance(collection, dict):
            continue
        for item in collection.values():
            if isinstance(item, dict):
                known_aggregates.update(_string_list(item.get("aggregate_roots")))
    return known_subdomains, known_contexts, known_aggregates


def _coverage_items(case_data: dict[str, Any]) -> list[dict[str, Any]]:
    top_level = _dict_items(case_data.get("domain_coverage"))
    if top_level:
        return top_level
    soft_evidence = case_data.get("soft_evidence", {})
    if isinstance(soft_evidence, dict):
        return _dict_items(soft_evidence.get("domain_coverage_matrix"))
    return []


def _coverage_type(item: dict[str, Any]) -> str:
    return str(item.get("coverage_type") or item.get("type") or "").strip()


def _coverage_story_ids(item: dict[str, Any]) -> list[str]:
    return _string_list(item.get("user_story_ids") or item.get("user_stories"))


def _coverage_acceptance_ids(item: dict[str, Any]) -> list[str]:
    return _string_list(item.get("acceptance_function_ids") or item.get("acceptance_functions"))


def _item_note(item: dict[str, Any]) -> str:
    return str(item.get("review_note") or item.get("reason") or item.get("next_action") or "").strip()


def _missing_required(
    blockers: list[dict[str, str]],
    required: set[str],
    covered: set[str],
    *,
    code: str,
    field: str,
) -> None:
    for value in sorted(required - covered):
        blockers.append(
            _blocker(
                code,
                f"domain coverage must classify required {field}: {value}",
                field="domain_coverage",
                evidence=value,
            )
        )


def _require_known_refs(
    blockers: list[dict[str, str]],
    *,
    owner_id: str,
    refs: list[str],
    known: set[str],
    missing_code: str,
    unknown_code: str,
    field: str,
) -> None:
    if not refs:
        blockers.append(_blocker(missing_code, f"{owner_id} has no {field}", field=field, evidence=owner_id))
        return
    for ref in sorted(ref for ref in refs if ref not in known and not ref.startswith(("candidate:", "follow_up:"))):
        blockers.append(_blocker(unknown_code, f"{owner_id} references unknown {field}: {ref}", field=field, evidence=ref))


def _acceptance_types(function: dict[str, Any]) -> set[str]:
    values = _string_list(function.get("coverage_types"))
    if not values:
        values = _string_list(function.get("coverage_type"))
    return set(values)


def _has_classified_handoff(items: list[dict[str, Any]], from_context: str, to_context: str) -> bool:
    for item in items:
        coverage_type = _coverage_type(item)
        if coverage_type not in EXPLICIT_NON_FULL_COVERAGE_TYPES:
            continue
        contexts = set(_string_list(item.get("contexts")))
        if from_context in contexts and to_context in contexts and _item_note(item):
            return True
    return False


def evaluate_domain_coverage_gate(case_data: dict[str, Any], taxonomy: dict[str, Any], *, strict: bool) -> tuple[dict[str, Any], list[dict[str, str]]]:
    if taxonomy_version(taxonomy) != 2 or not strict:
        return {"passed": True, "mode": "legacy_compatibility"}, []

    domain_model = case_data.get("domain_model", {})
    if not isinstance(domain_model, dict) or not domain_model:
        return {"passed": False, "mode": "ddd", "status": "domain_model_missing"}, []

    known_subdomains, known_contexts, known_aggregates = _known_sets(taxonomy)
    required_subdomains = set(_string_list(domain_model.get("subdomains")))
    required_contexts = set(_string_list(domain_model.get("bounded_contexts")))
    required_aggregates = set(_string_list(domain_model.get("aggregate_roots")))
    items = _coverage_items(case_data)
    blockers: list[dict[str, str]] = []

    if not items:
        blockers.append(_blocker("domain_coverage_missing", "strict DDD readiness requires domain_coverage", field="domain_coverage"))

    story_ids = {str(story.get("id", "")).strip() for story in _dict_items(case_data.get("user_stories")) if str(story.get("id", "")).strip()}
    function_ids = {str(function.get("id", "")).strip() for function in _dict_items(case_data.get("acceptance_functions")) if str(function.get("id", "")).strip()}
    covered_subdomains: set[str] = set()
    covered_contexts: set[str] = set()
    covered_aggregates: set[str] = set()

    for index, item in enumerate(items, start=1):
        label = str(item.get("subdomain") or item.get("domain") or f"item-{index}").strip()
        subdomain = str(item.get("subdomain") or item.get("domain") or "").strip()
        coverage_type = _coverage_type(item)
        contexts = _string_list(item.get("contexts"))
        aggregates = _string_list(item.get("aggregate_roots"))
        item_story_ids = _coverage_story_ids(item)
        item_function_ids = _coverage_acceptance_ids(item)

        if not subdomain:
            blockers.append(_blocker("domain_coverage_subdomain_missing", f"domain coverage item {index} has no subdomain", field="domain_coverage"))
        elif subdomain not in known_subdomains:
            blockers.append(_blocker("domain_coverage_subdomain_unknown", f"domain coverage references unknown subdomain: {subdomain}", field="domain_coverage", evidence=subdomain))
        else:
            covered_subdomains.add(subdomain)

        if not coverage_type:
            blockers.append(_blocker("domain_coverage_type_missing", f"domain coverage {label} has no coverage_type", field="domain_coverage", evidence=label))
        elif coverage_type not in KNOWN_COVERAGE_TYPES:
            blockers.append(_blocker("domain_coverage_type_unknown", f"domain coverage {label} uses unknown coverage_type: {coverage_type}", field="domain_coverage", evidence=coverage_type))
        elif coverage_type in EXPLICIT_NON_FULL_COVERAGE_TYPES and not _item_note(item):
            blockers.append(_blocker("domain_coverage_note_missing", f"domain coverage {label} must explain {coverage_type}", field="domain_coverage", evidence=label))

        for context in contexts:
            if context not in known_contexts:
                blockers.append(_blocker("domain_coverage_context_unknown", f"domain coverage {label} references unknown context: {context}", field="domain_coverage", evidence=context))
            else:
                covered_contexts.add(context)
        for aggregate in aggregates:
            if aggregate not in known_aggregates and not aggregate.startswith(("candidate:", "follow_up:")):
                blockers.append(_blocker("domain_coverage_aggregate_unknown", f"domain coverage {label} references unknown aggregate root: {aggregate}", field="domain_coverage", evidence=aggregate))
            else:
                covered_aggregates.add(aggregate)

        if coverage_type in IN_SCOPE_COVERAGE_TYPES:
            if not item_story_ids:
                blockers.append(_blocker("domain_coverage_story_refs_missing", f"domain coverage {label} has no user_story_ids", field="domain_coverage", evidence=label))
            if not item_function_ids:
                blockers.append(_blocker("domain_coverage_acceptance_refs_missing", f"domain coverage {label} has no acceptance_function_ids", field="domain_coverage", evidence=label))
        for story_id in sorted(ref for ref in item_story_ids if ref not in story_ids):
            blockers.append(_blocker("domain_coverage_story_ref_unknown", f"domain coverage {label} references unknown user story: {story_id}", field="domain_coverage", evidence=story_id))
        for function_id in sorted(ref for ref in item_function_ids if ref not in function_ids):
            blockers.append(_blocker("domain_coverage_acceptance_ref_unknown", f"domain coverage {label} references unknown acceptance function: {function_id}", field="domain_coverage", evidence=function_id))

    _missing_required(blockers, required_subdomains, covered_subdomains, code="domain_coverage_subdomain_required_missing", field="subdomain")
    _missing_required(blockers, required_contexts, covered_contexts, code="domain_coverage_context_required_missing", field="bounded_context")
    _missing_required(blockers, required_aggregates, covered_aggregates, code="domain_coverage_aggregate_required_missing", field="aggregate_root")

    for story in _dict_items(case_data.get("user_stories")):
        story_id = str(story.get("id", "")).strip() or "missing"
        _require_known_refs(blockers, owner_id=story_id, refs=_string_list(story.get("domain_refs")), known=known_subdomains, missing_code="domain_coverage_story_domain_refs_missing", unknown_code="domain_coverage_story_domain_ref_unknown", field="domain_refs")
        _require_known_refs(blockers, owner_id=story_id, refs=_string_list(story.get("context_refs")), known=known_contexts, missing_code="domain_coverage_story_context_refs_missing", unknown_code="domain_coverage_story_context_ref_unknown", field="context_refs")
        _require_known_refs(blockers, owner_id=story_id, refs=_string_list(story.get("aggregate_refs")), known=known_aggregates, missing_code="domain_coverage_story_aggregate_refs_missing", unknown_code="domain_coverage_story_aggregate_ref_unknown", field="aggregate_refs")

    all_acceptance_types: set[str] = set()
    handoff_functions: list[dict[str, Any]] = []
    for function in _dict_items(case_data.get("acceptance_functions")):
        function_id = str(function.get("id", "")).strip() or "missing"
        coverage_types = _acceptance_types(function)
        if not coverage_types:
            blockers.append(_blocker("domain_coverage_acceptance_types_missing", f"acceptance function {function_id} has no coverage_types", field="acceptance_functions", evidence=function_id))
        for coverage_type in sorted(coverage_types):
            if coverage_type not in REQUIRED_ACCEPTANCE_TYPES:
                blockers.append(_blocker("domain_coverage_acceptance_type_unknown", f"acceptance function {function_id} uses unknown coverage type: {coverage_type}", field="acceptance_functions", evidence=coverage_type))
        all_acceptance_types.update(coverage_types & REQUIRED_ACCEPTANCE_TYPES)
        if "handoff" in coverage_types:
            handoff_functions.append(function)
        if coverage_types:
            _require_known_refs(blockers, owner_id=function_id, refs=_string_list(function.get("context_refs")), known=known_contexts, missing_code="domain_coverage_acceptance_context_refs_missing", unknown_code="domain_coverage_acceptance_context_ref_unknown", field="context_refs")
            _require_known_refs(blockers, owner_id=function_id, refs=_string_list(function.get("aggregate_refs")), known=known_aggregates, missing_code="domain_coverage_acceptance_aggregate_refs_missing", unknown_code="domain_coverage_acceptance_aggregate_ref_unknown", field="aggregate_refs")

    if required_aggregates and "state_change" not in all_acceptance_types:
        blockers.append(_blocker("domain_coverage_state_change_missing", "aggregate lifecycles require at least one state_change acceptance function", field="acceptance_functions"))

    for index, handoff in enumerate(_dict_items(domain_model.get("context_handoffs")), start=1):
        from_context = str(handoff.get("from_context") or handoff.get("from") or "").strip()
        to_context = str(handoff.get("to_context") or handoff.get("to") or "").strip()
        has_acceptance = any(
            from_context in set(_string_list(function.get("context_refs")))
            and to_context in set(_string_list(function.get("context_refs")))
            for function in handoff_functions
        )
        if not has_acceptance and not _has_classified_handoff(items, from_context, to_context):
            blockers.append(_blocker("domain_coverage_handoff_missing", f"context handoff {index} needs handoff acceptance or explicit coverage note", field="acceptance_functions", evidence=f"{from_context}->{to_context}"))

    if (required_contexts & FAILURE_CONTEXTS or required_aggregates & FAILURE_AGGREGATES) and "failure_path" not in all_acceptance_types:
        blockers.append(_blocker("domain_coverage_failure_path_missing", "failure-prone renewal or payment contexts require failure_path acceptance", field="acceptance_functions"))
    if required_contexts & EVIDENCE_CONTEXTS and "evidence" not in all_acceptance_types:
        blockers.append(_blocker("domain_coverage_evidence_missing", "ledger, reconciliation, settlement, split, or payout contexts require evidence acceptance", field="acceptance_functions"))

    return {
        "passed": not blockers,
        "mode": "ddd",
        "coverage_count": len(items),
        "covered_subdomains": sorted(covered_subdomains),
        "covered_contexts": sorted(covered_contexts),
        "covered_aggregate_roots": sorted(covered_aggregates),
    }, blockers
