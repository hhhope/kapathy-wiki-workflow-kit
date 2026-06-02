from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scripts.requirements_openspec_draft import create_openspec_draft_from_case


TAXONOMY_PATH = Path("requirements/config/requirements-taxonomy.yaml")


def _load_taxonomy(repo_root: Path | str = ".") -> dict[str, Any]:
    with (Path(repo_root) / TAXONOMY_PATH).open(encoding="utf-8") as handle:
        taxonomy = yaml.safe_load(handle)
    if not isinstance(taxonomy, dict):
        raise ValueError(f"requirements taxonomy is not an object: {TAXONOMY_PATH}")
    return taxonomy


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def build_role_instance(
    *,
    role_id: str,
    mention: str,
    confirmed_as: str,
    status: str = "confirmed",
    category: str = "",
    source_section: str = "",
) -> dict[str, object]:
    role: dict[str, object] = {
        "id": role_id,
        "mention": mention,
        "confirmed_as": confirmed_as,
        "status": status,
        "source_actors": [mention],
    }
    if category:
        role["category"] = category
    if source_section:
        role["evidence_anchor"] = {"source_section": source_section}
    return role


def classify_intent(material: str) -> dict[str, Any]:
    text = str(material or "").strip()
    if _contains_any(text, ("openspec draft", "open spec draft", "创建 openspec", "生成 openspec")):
        return {
            "intent": "create_openspec_draft",
            "draft_requested": True,
            "next_action": "create_openspec_draft",
        }
    if _contains_any(text, ("是否可以进入开发", "是否ready", "ready to proceed", "requirement is ready", "需求是否可以", "能不能开发", "需求门禁", "校验需求", "需求校验")):
        return {
            "intent": "check_requirements_ready",
            "draft_requested": False,
            "next_action": "run_requirements_checker",
        }
    return {
        "intent": "new_requirement_intake",
        "draft_requested": False,
        "next_action": "diagnose_requirement",
    }


def _domain_aliases(taxonomy: dict[str, Any]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    domains = taxonomy.get("domains", [])
    if not isinstance(domains, list):
        return aliases
    for domain in domains:
        if not isinstance(domain, dict):
            continue
        domain_id = str(domain.get("id", "")).strip()
        if not domain_id:
            continue
        aliases[domain_id.lower()] = domain_id
        label = str(domain.get("label", "")).strip()
        if label:
            aliases[label.lower()] = domain_id
        for alias in domain.get("aliases", []) if isinstance(domain.get("aliases"), list) else []:
            text = str(alias).strip()
            if text:
                aliases[text.lower()] = domain_id
    return aliases


def _unknown_domain_candidates(material: str) -> list[dict[str, str]]:
    if _contains_any(material, ("embedded wallet", "wallet payment", "钱包", "余额支付")):
        return [
            {
                "id": "embedded_wallet",
                "confidence": "medium",
                "reason": "material mentions embedded wallet or wallet payment vocabulary",
            },
            {
                "id": "wallet_payment",
                "confidence": "medium",
                "reason": "material appears centered on wallet payment rather than the seeded domains",
            },
        ]
    return [
        {
            "id": "unknown_requirement_domain",
            "confidence": "low",
            "reason": "no seeded requirements taxonomy domain matched the material",
        }
    ]


def resolve_domain(material: str, repo_root: Path | str = ".") -> dict[str, Any]:
    text = str(material or "")
    lowered = text.lower()
    if _contains_any(text, ("embedded wallet", "wallet payment", "钱包", "余额支付")):
        return {
            "status": "candidate_pending",
            "confirmed": "",
            "candidates": _unknown_domain_candidates(text),
            "requires_user_confirmation": True,
        }
    for alias, domain_id in sorted(_domain_aliases(_load_taxonomy(repo_root)).items(), key=lambda item: len(item[0]), reverse=True):
        if alias and alias in lowered:
            return {
                "status": "confirmed",
                "confirmed": domain_id,
                "candidates": [{"id": domain_id, "reason": f"matched taxonomy alias `{alias}`"}],
                "requires_user_confirmation": False,
            }
    return {
        "status": "candidate_pending",
        "confirmed": "",
        "candidates": _unknown_domain_candidates(text),
        "requires_user_confirmation": True,
    }


def analyze_requirements_intake(material: str, repo_root: Path | str = ".") -> dict[str, Any]:
    intent = classify_intent(material)
    domain = resolve_domain(material, repo_root=repo_root)
    next_action = "confirm_domain" if domain["status"] == "candidate_pending" else "normalize_requirement"
    if intent["intent"] == "check_requirements_ready":
        next_action = "run_requirements_checker"
    elif intent["intent"] == "create_openspec_draft":
        next_action = "check_requirements_ready"
    return {
        "intent": intent,
        "domain": domain,
        "next_action": next_action,
    }
