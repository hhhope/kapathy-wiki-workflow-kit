from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ROOT_SECTIONS = {
    "business_ecosystems",
    "subdomains",
    "bounded_contexts",
    "role_archetypes",
    "context_map",
    "case_classification",
    "candidate_evolution",
    "readiness_gate_model",
}

REAL_FUNDS_REQUIRED_CONTEXTS = {"balance_ledger_context"}
REAL_FUNDS_REQUIRED_ROLES = {"funds_account_owner", "ledger_owner", "balance_state_owner"}


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _string_items(value: Any) -> list[str]:
    return [str(item) for item in _as_list(value) if str(item).strip()]


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"taxonomy must be a YAML mapping: {path}")
    return data


def validate_taxonomy(data: dict[str, Any]) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for section in sorted(ROOT_SECTIONS):
        if section not in data:
            errors.append(f"missing root section: {section}")

    if data.get("version") != 2:
        errors.append("version must be 2")
    if data.get("authority") != "requirements-ddd-model":
        errors.append("authority must be requirements-ddd-model")

    ecosystems = _as_dict(data.get("business_ecosystems"))
    subdomains = _as_dict(data.get("subdomains"))
    contexts = _as_dict(data.get("bounded_contexts"))
    roles = _as_dict(data.get("role_archetypes"))

    for ecosystem_id, ecosystem in ecosystems.items():
        for subdomain_id in _string_items(_as_dict(ecosystem).get("subdomains")):
            if subdomain_id not in subdomains:
                errors.append(f"ecosystem {ecosystem_id} references unknown subdomain {subdomain_id}")

    for subdomain_id, subdomain in subdomains.items():
        subdomain_data = _as_dict(subdomain)
        ecosystem_id = str(subdomain_data.get("business_ecosystem", "")).strip()
        if ecosystem_id and ecosystem_id not in ecosystems:
            errors.append(f"subdomain {subdomain_id} references unknown ecosystem {ecosystem_id}")
        for context_id in _string_items(subdomain_data.get("bounded_contexts")):
            if context_id not in contexts:
                errors.append(f"subdomain {subdomain_id} references unknown context {context_id}")

    for context_id, context in contexts.items():
        context_data = _as_dict(context)
        subdomain_id = str(context_data.get("subdomain", "")).strip()
        if subdomain_id and subdomain_id not in subdomains:
            errors.append(f"context {context_id} references unknown subdomain {subdomain_id}")
        if not _string_items(context_data.get("aggregate_roots")):
            errors.append(f"context {context_id} must define aggregate_roots")
        for role_id in _string_items(context_data.get("fact_owners")):
            if role_id not in roles:
                errors.append(f"context {context_id} references unknown fact owner {role_id}")

    for role_id, role in roles.items():
        role_data = _as_dict(role)
        for context_id in _string_items(role_data.get("required_by_contexts")):
            if context_id not in contexts:
                errors.append(f"role archetype {role_id} references unknown context {context_id}")

    for item in _as_list(data.get("context_map")):
        handoff = _as_dict(item)
        handoff_id = str(handoff.get("id", "missing"))
        for field in ("from_context", "to_context"):
            context_id = str(handoff.get(field, "")).strip()
            if context_id and context_id not in contexts:
                errors.append(f"context map {handoff_id} references unknown {field} {context_id}")
        if str(handoff.get("handoff_type", "")).strip() not in {
            "command",
            "domain_event",
            "policy_decision",
            "query",
            "report",
            "evidence",
        }:
            errors.append(f"context map {handoff_id} has invalid handoff_type")

    for context_id in sorted(REAL_FUNDS_REQUIRED_CONTEXTS):
        if context_id not in contexts:
            errors.append(f"real funds trigger requires context {context_id}")
    for role_id in sorted(REAL_FUNDS_REQUIRED_ROLES):
        if role_id not in roles:
            errors.append(f"real funds trigger requires role archetype {role_id}")

    candidate = _as_dict(data.get("candidate_evolution"))
    required = set(_string_items(candidate.get("promotion_required_fields")))
    expected = {
        "business_problem",
        "ubiquitous_language",
        "aggregate_roots",
        "lifecycle",
        "invariants",
        "fact_owners",
        "context_map",
        "why_existing_contexts_do_not_fit",
    }
    for field in sorted(expected - required):
        errors.append(f"candidate evolution missing promotion field {field}")

    return {"errors": errors, "warnings": warnings}


def validate_taxonomy_file(path: Path | str) -> dict[str, list[str]]:
    return validate_taxonomy(_load_yaml(Path(path)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate requirements DDD taxonomy structure.")
    parser.add_argument("--taxonomy", default="requirements/config/requirements-taxonomy.yaml")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    report = validate_taxonomy_file(args.taxonomy)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for error in report["errors"]:
            print(f"ERROR {error}")
        for warning in report["warnings"]:
            print(f"WARN {warning}")
        if not report["errors"] and not report["warnings"]:
            print("requirements DDD taxonomy is valid")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
