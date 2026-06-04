from __future__ import annotations

import json
from typing import Any


_PAYMENT_MEANINGS = {
    "payment_transaction": "A payment transaction subdomain covering payment intent, attempt, authorization, charge, and final status convergence.",
    "payment_intent_context": "Records why a renewal invoice needs payment, the amount, linked subscription period, and final payment state.",
    "payment_attempt_authorization_context": "Records each charge attempt and whether a valid authorization exists before charging.",
    "payment_method_context": "Records the payment method that can be charged and its current validity.",
    "charge": "The transaction fact produced by a successful or failed charge attempt.",
    "payment_attempt": "One concrete payment attempt; one payment intent can have multiple attempts.",
    "payment_intent": "One payable intent, usually linked to one renewal invoice or billing period.",
    "payment_method_authorization": "The authorization evidence that allows recurring billing against a payment method.",
}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _dict_items(value: Any) -> list[dict[str, Any]]:
    return [item for item in _as_list(value) if isinstance(item, dict)]


def _string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        value = [value]
    return [str(item).strip() for item in _as_list(value) if str(item).strip()]


def _first_text(item: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        value = str(item.get(key, "")).strip()
        if value:
            return value
    return ""


def _coverage_items(package: dict[str, Any]) -> list[dict[str, Any]]:
    coverage = _dict_items(package.get("domain_coverage"))
    if coverage:
        return coverage
    soft_evidence = package.get("soft_evidence", {})
    if isinstance(soft_evidence, dict):
        return _dict_items(soft_evidence.get("domain_coverage_matrix"))
    return []


def _meaning(ref_id: str, category: str) -> str:
    if ref_id in _PAYMENT_MEANINGS:
        return _PAYMENT_MEANINGS[ref_id]
    readable = ref_id.replace("_", " ")
    if category == "domain":
        return f"Subdomain responsibility for {readable}."
    if category == "context":
        return f"Bounded context responsibility for {readable}."
    if category == "aggregate":
        return f"Business object lifecycle covered by {readable}."
    return f"Meaning for {readable}."


def _refs(ids: list[str], category: str) -> list[dict[str, str]]:
    return [{"id": ref_id, "meaning": _meaning(ref_id, category)} for ref_id in ids]


def _coverage_decision(coverage_type: str) -> str:
    if coverage_type in {"out_of_scope", "follow_up", "light_coverage"}:
        return coverage_type
    return "full_story"


def _story_lookup(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(story.get("id", "")).strip(): story
        for story in _dict_items(package.get("user_stories"))
        if str(story.get("id", "")).strip()
    }


def _acceptance_lookup(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(function.get("id", "")).strip(): function
        for function in _dict_items(package.get("acceptance_functions"))
        if str(function.get("id", "")).strip()
    }


def _story_summary(story: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(story.get("id", "")),
        "role_ref": str(story.get("role_ref", "")),
        "want": _first_text(story, ("want", "story", "summary")),
        "benefit": _first_text(story, ("benefit", "value", "so_that")),
    }


def _acceptance_summary(function: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(function.get("id", "")),
        "coverage_types": _string_list(function.get("coverage_types")),
        "then": _first_text(function, ("then", "expected", "summary", "name")),
    }


def _review_block(
    package: dict[str, Any],
    coverage: dict[str, Any],
    stories_by_id: dict[str, dict[str, Any]],
    functions_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    story_ids = _string_list(coverage.get("user_story_ids") or coverage.get("user_stories"))
    function_ids = _string_list(coverage.get("acceptance_function_ids") or coverage.get("acceptance_functions"))
    coverage_type = str(coverage.get("coverage_type") or coverage.get("type") or "").strip()
    contexts = _string_list(coverage.get("contexts"))
    aggregates = _string_list(coverage.get("aggregate_roots"))
    subdomain = str(coverage.get("subdomain") or coverage.get("domain") or "").strip()
    review_note = str(coverage.get("review_note") or coverage.get("reason") or "").strip()
    stories = [stories_by_id[story_id] for story_id in story_ids if story_id in stories_by_id]
    acceptances = [functions_by_id[function_id] for function_id in function_ids if function_id in functions_by_id]
    primary_story = stories[0] if stories else {}

    return {
        "coverage_item": subdomain,
        "story": _story_summary(primary_story) if primary_story else {},
        "review_judgment": {
            "coverage_decision": _coverage_decision(coverage_type),
            "business_meaning": _first_text(primary_story, ("want", "story", "summary")) or review_note,
            "why_this_domain": review_note or f"Derived from coverage metadata for {subdomain}.",
            "first_release_scope": aggregates,
            "out_of_scope": _string_list(coverage.get("out_of_scope")),
            "future_work": _string_list(coverage.get("future_work")),
            "reviewer_question": (
                f"Does first-release scope for {subdomain} cover only {', '.join(aggregates)}?"
                if aggregates
                else f"Does the reviewer accept the derived scope for {subdomain}?"
            ),
        },
        "taxonomy_refs": {
            "domains": _refs([subdomain] if subdomain else [], "domain"),
            "contexts": _refs(contexts, "context"),
            "aggregates": _refs(aggregates, "aggregate"),
        },
        "acceptance_functions": [_acceptance_summary(function) for function in acceptances],
        "gate_closure": {
            "domain_model_gate": "Domain model declares the taxonomy references that this review block explains.",
            "domain_coverage_gate": "Domain coverage binds subdomain, context, aggregate, story, and acceptance references.",
            "requirement_delivery_gate": "Stories keep role, want, benefit, and acceptance mappings; acceptance functions keep observable outcomes.",
            "human_review_gate": "Reviewer checks the stated business meaning, first-release scope, deferred work, and reviewer question.",
        },
        "eval_plan": {
            "red_cases": [
                "Compressed taxonomy labels without review_judgment are not reviewable.",
                "Taxonomy references without meaning are not reviewable.",
                "Full-story coverage without first_release_scope is not reviewable.",
                "Acceptance mappings without gate_closure do not explain why the gates close.",
            ],
            "green_cases": [
                "Review block includes review_judgment, taxonomy_refs, acceptance_functions, gate_closure, and eval_plan.",
                "Every taxonomy reference includes id and meaning.",
                "Machine case data remains unchanged after rendering.",
                "Human reviewer can answer why this domain, what is first release, and what is deferred.",
            ],
        },
    }


def render_reviewable_coverage(package: dict[str, Any]) -> list[str]:
    coverage_items = _coverage_items(package)
    if not coverage_items:
        return []

    stories_by_id = _story_lookup(package)
    functions_by_id = _acceptance_lookup(package)
    blocks = [
        _review_block(package, coverage, stories_by_id, functions_by_id)
        for coverage in coverage_items
    ]
    rendered = json.dumps(blocks, ensure_ascii=False, indent=2, sort_keys=True)
    return ["", "## Reviewable Coverage", "```json", rendered, "```"]
