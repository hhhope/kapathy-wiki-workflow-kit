from __future__ import annotations

from typing import Any


LEGACY_DOMAIN_IDS = {
    "account",
    "settlement",
    "clearing",
    "merchant_platform_relationship",
    "payment_transaction",
    "billing_revenue",
    "account_balance",
    "funds_movement_settlement",
    "financial_operations",
    "risk_compliance",
    "embedded_financial_products",
}

LEGACY_ROLE_ALIASES = {
    "retail_operations": ["retail operations", "零售运营"],
    "financial_operations": ["financial operations", "金融运营"],
    "product": ["product", "产品"],
    "finance": ["finance", "财务"],
    "clearing": ["clearing", "清算", "清分"],
    "compliance": ["compliance", "合规"],
    "retail_customer": ["retail customer", "零售客户"],
    "financial_customer": ["financial customer", "金融客户"],
    "system_actor": ["system actor", "系统", "外部系统", "内部系统"],
    "engineering": ["engineering", "研发", "技术"],
    "qa": ["QA", "qa", "测试", "质量"],
    "risk_control": ["risk control", "风控", "风险控制"],
}

LEGACY_SOFT_EVIDENCE_CATEGORIES = {
    "business_rules": {"classification": "soft_warning"},
    "exception_scenarios": {"classification": "soft_warning"},
    "api": {"classification": "design_evidence"},
    "ddl": {"classification": "design_evidence"},
    "adr": {"classification": "design_evidence"},
    "test_plan": {"classification": "design_evidence"},
    "release_plan": {"classification": "design_evidence"},
}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _string_list(value: Any) -> list[str]:
    return [str(item) for item in _as_list(value) if str(item).strip()]


def _blocker(code: str, reason: str, *, field: str = "", evidence: str = "") -> dict[str, str]:
    item = {"code": code, "reason": reason}
    if field:
        item["field"] = field
    if evidence:
        item["evidence"] = evidence
    return item


def taxonomy_version(taxonomy: dict[str, Any]) -> int:
    try:
        return int(taxonomy.get("version", 1))
    except (TypeError, ValueError):
        return 1


def known_domain_ids(taxonomy: dict[str, Any]) -> set[str]:
    if taxonomy_version(taxonomy) == 2:
        subdomains = taxonomy.get("subdomains", {})
        ids = set(subdomains) if isinstance(subdomains, dict) else set()
        return ids | LEGACY_DOMAIN_IDS

    domains = taxonomy.get("domains", [])
    return {
        str(domain.get("id"))
        for domain in _as_list(domains)
        if isinstance(domain, dict) and str(domain.get("id", "")).strip()
    }


def role_lookup(taxonomy: dict[str, Any], *, include_legacy: bool = True) -> dict[str, str]:
    lookup: dict[str, str] = {}

    roles = taxonomy.get("roles", {})
    vocabulary = roles.get("vocabulary", {}) if isinstance(roles, dict) else {}
    if isinstance(vocabulary, dict):
        for role_id, role in vocabulary.items():
            canonical = str(role_id)
            lookup[canonical] = canonical
            if isinstance(role, dict):
                label = str(role.get("label", "")).strip()
                if label:
                    lookup[label] = canonical
                for alias in _string_list(role.get("aliases")):
                    lookup[alias] = canonical

    role_archetypes = taxonomy.get("role_archetypes", {})
    if isinstance(role_archetypes, dict):
        for role_id in role_archetypes:
            canonical = str(role_id)
            lookup[canonical] = canonical

    if include_legacy:
        for canonical, aliases in LEGACY_ROLE_ALIASES.items():
            lookup.setdefault(canonical, canonical)
            for alias in aliases:
                lookup.setdefault(alias, canonical)
    return lookup


def soft_evidence_categories(taxonomy: dict[str, Any]) -> dict[str, Any]:
    categories = taxonomy.get("soft_evidence_categories", {})
    return categories if isinstance(categories, dict) and categories else LEGACY_SOFT_EVIDENCE_CATEGORIES


def evaluate_domain_model_gate(case_data: dict[str, Any], taxonomy: dict[str, Any], *, strict: bool) -> tuple[dict[str, Any], list[dict[str, str]]]:
    if taxonomy_version(taxonomy) != 2 or not strict:
        return {"passed": True, "mode": "legacy_compatibility"}, []

    domain_model = case_data.get("domain_model", {})
    blockers: list[dict[str, str]] = []
    if not isinstance(domain_model, dict) or not domain_model:
        return {
            "passed": False,
            "mode": "ddd",
            "status": "missing",
        }, [_blocker("domain_model_missing", "strict DDD readiness requires domain_model", field="domain_model")]

    status = str(domain_model.get("status", "")).strip()
    if status != "confirmed":
        blockers.append(
            _blocker(
                "domain_model_not_confirmed",
                f"domain_model status must be confirmed; status={status or 'missing'}",
                field="domain_model",
            )
        )

    ecosystems = taxonomy.get("business_ecosystems", {})
    subdomains = taxonomy.get("subdomains", {})
    contexts = taxonomy.get("bounded_contexts", {})
    role_archetypes = taxonomy.get("role_archetypes", {})
    known_ecosystems = set(ecosystems) if isinstance(ecosystems, dict) else set()
    known_subdomains = set(subdomains) if isinstance(subdomains, dict) else set()
    known_contexts = set(contexts) if isinstance(contexts, dict) else set()
    known_roles = set(role_archetypes) if isinstance(role_archetypes, dict) else set()
    known_aggregates = _known_aggregate_roots(subdomains, contexts)

    _require_known_list(blockers, domain_model, "business_ecosystems", known_ecosystems, "domain_model_ecosystems")
    _require_known_list(blockers, domain_model, "subdomains", known_subdomains, "domain_model_subdomains")
    context_values = _require_known_list(blockers, domain_model, "bounded_contexts", known_contexts, "domain_model_contexts")
    _require_known_list(blockers, domain_model, "aggregate_roots", known_aggregates, "domain_model_aggregate_roots")
    _require_known_list(blockers, domain_model, "fact_owners", known_roles, "domain_model_fact_owners")
    _require_known_list(blockers, domain_model, "role_obligations", known_roles, "domain_model_role_obligation")
    _require_handoffs(blockers, domain_model, known_contexts)

    return {
        "passed": not blockers,
        "mode": "ddd",
        "status": status or "missing",
        "bounded_contexts": context_values,
    }, blockers


def _known_aggregate_roots(subdomains: Any, contexts: Any) -> set[str]:
    roots: set[str] = set()
    for collection in (subdomains, contexts):
        if not isinstance(collection, dict):
            continue
        for item in collection.values():
            if isinstance(item, dict):
                roots.update(_string_list(item.get("aggregate_roots")))
    return roots


def _require_known_list(
    blockers: list[dict[str, str]],
    domain_model: dict[str, Any],
    field: str,
    known_values: set[str],
    code_prefix: str,
) -> list[str]:
    values = _string_list(domain_model.get(field))
    if not values:
        blockers.append(_blocker(f"{code_prefix}_missing", f"domain_model.{field} is required", field="domain_model"))
        return values
    unknown = sorted(value for value in values if value not in known_values)
    for value in unknown:
        blockers.append(
            _blocker(
                f"{code_prefix}_unknown",
                f"domain_model.{field} references unknown value: {value}",
                field="domain_model",
                evidence=value,
            )
        )
    return values


def _require_handoffs(blockers: list[dict[str, str]], domain_model: dict[str, Any], known_contexts: set[str]) -> None:
    handoffs = [item for item in _as_list(domain_model.get("context_handoffs")) if isinstance(item, dict)]
    if not handoffs:
        blockers.append(_blocker("domain_model_handoffs_missing", "domain_model.context_handoffs is required", field="domain_model"))
        return
    for index, handoff in enumerate(handoffs, start=1):
        from_context = str(handoff.get("from_context") or handoff.get("from") or "").strip()
        to_context = str(handoff.get("to_context") or handoff.get("to") or "").strip()
        handoff_type = str(handoff.get("type") or handoff.get("handoff_type") or "").strip()
        if from_context not in known_contexts:
            blockers.append(_blocker("domain_model_handoff_from_unknown", f"context_handoff {index} has unknown from_context: {from_context or 'missing'}", field="domain_model", evidence=from_context))
        if to_context not in known_contexts:
            blockers.append(_blocker("domain_model_handoff_to_unknown", f"context_handoff {index} has unknown to_context: {to_context or 'missing'}", field="domain_model", evidence=to_context))
        if not handoff_type:
            blockers.append(_blocker("domain_model_handoff_type_missing", f"context_handoff {index} has no type", field="domain_model"))
