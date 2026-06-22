from __future__ import annotations

from typing import Any

from scripts.requirements_ddd_readiness import taxonomy_version


def analyze_ddd_domain(material: str, taxonomy: dict[str, Any]) -> dict[str, Any]:
    text = str(material or "")
    lowered = text.lower()
    if taxonomy_version(taxonomy) != 2:
        return _empty_domain_model()

    candidates = _candidate_terms(text)
    if candidates:
        model = _empty_domain_model(status="candidate_pending")
        model["candidates"] = candidates
        model["open_questions"] = [f"Confirm whether `{item['id']}` should become a candidate context or stay out of taxonomy." for item in candidates]
        return model

    if _looks_like_agent_subscription_payment(text, lowered):
        return _agent_subscription_payment_model()

    if _contains_any(text, ("embedded wallet", "wallet payment", "钱包", "余额支付")):
        model = _empty_domain_model(status="candidate_pending")
        model["candidates"] = [
            {
                "id": "embedded_wallet",
                "confidence": "medium",
                "reason": "material mentions embedded wallet vocabulary; current taxonomy needs candidate review",
            },
            {
                "id": "wallet_payment",
                "confidence": "medium",
                "reason": "material appears centered on wallet payment rather than confirmed DDD contexts",
            },
        ]
        return model

    if _contains_any(text, ("结算", "settlement", "payout", "分账")):
        model = _empty_domain_model(status="confirmed")
        model.update(
            {
                "business_ecosystems": ["payment_ecosystem"],
                "subdomains": ["funds_movement_settlement", "financial_operations"],
                "bounded_contexts": ["settlement_batch_context", "payout_context", "reconciliation_context"],
                "aggregate_roots": ["settlement_batch", "payout", "reconciliation_record"],
                "fact_owners": ["settlement_owner", "payout_owner", "reconciliation_owner"],
                "role_obligations": ["settlement_owner", "payout_owner", "reconciliation_owner"],
                "context_handoffs": [
                    {
                        "from_context": "settlement_batch_context",
                        "to_context": "reconciliation_context",
                        "type": "evidence",
                        "name": "SettlementBatchClosed",
                    }
                ],
            }
        )
        return model

    if _contains_any(text, ("清分", "clearing", "对账")):
        model = _empty_domain_model(status="confirmed")
        model.update(
            {
                "business_ecosystems": ["payment_ecosystem"],
                "subdomains": ["financial_operations", "funds_movement_settlement"],
                "bounded_contexts": ["reconciliation_context", "fee_accounting_context"],
                "aggregate_roots": ["reconciliation_record", "reconciliation_match"],
                "fact_owners": ["reconciliation_owner", "fee_accounting_owner"],
                "role_obligations": ["reconciliation_owner", "fee_accounting_owner"],
                "context_handoffs": [
                    {
                        "from_context": "reconciliation_context",
                        "to_context": "fee_accounting_context",
                        "type": "evidence",
                        "name": "ReconciliationMatched",
                    }
                ],
            }
        )
        return model

    if _contains_any(text, ("账户", "account", "余额", "balance", "ledger", "账本")):
        model = _empty_domain_model(status="confirmed")
        model.update(
            {
                "business_ecosystems": ["payment_ecosystem"],
                "subdomains": ["account_balance", "financial_operations"],
                "bounded_contexts": ["balance_ledger_context", "reconciliation_context"],
                "aggregate_roots": ["payment_account", "balance", "ledger_entry", "reconciliation_record"],
                "fact_owners": ["funds_account_owner", "balance_state_owner", "ledger_owner", "reconciliation_owner"],
                "role_obligations": ["funds_account_owner", "balance_state_owner", "ledger_owner", "reconciliation_owner"],
                "context_handoffs": [
                    {
                        "from_context": "balance_ledger_context",
                        "to_context": "reconciliation_context",
                        "type": "evidence",
                        "name": "LedgerEntryPosted",
                    }
                ],
                "non_domain_terms": [],
            }
        )
        return model

    return _empty_domain_model(status="candidate_pending")


def identify_actors(material: str) -> list[dict[str, str]]:
    text = str(material or "")
    actors: list[dict[str, str]] = []
    _append_actor_if(text, actors, ("AI 服务商", "服务商", "服务方", "ai service provider"), "ai_service_provider", "AI service provider", "organization")
    _append_actor_if(text, actors, ("平台", "marketplace", "platform"), "platform", "platform", "organization")
    _append_actor_if(text, actors, ("消费者", "consumer", "终端用户", "end user"), "consumer", "consumer", "person")
    _append_actor_if(text, actors, ("自动续费", "周期扣款", "recurring"), "recurring_billing_job", "recurring billing automation", "system")
    _append_actor_if(text, actors, ("支付通道", "通道", "channel"), "payment_channel", "payment channel", "external_system")
    return actors


def compatibility_domain_summary(domain_model: dict[str, Any]) -> dict[str, Any]:
    subdomains = [str(item) for item in domain_model.get("subdomains", []) if str(item).strip()]
    status = str(domain_model.get("status", "candidate_pending"))
    if status == "confirmed" and subdomains:
        confirmed = subdomains[0]
        return {
            "status": "confirmed",
            "confirmed": confirmed,
            "candidates": [{"id": confirmed, "reason": "derived from DDD domain_model primary subdomain"}],
            "requires_user_confirmation": False,
        }
    candidates = domain_model.get("candidates", [])
    return {
        "status": "candidate_pending",
        "confirmed": "",
        "candidates": candidates if isinstance(candidates, list) else [],
        "requires_user_confirmation": True,
    }


def _agent_subscription_payment_model() -> dict[str, Any]:
    model = _empty_domain_model(status="confirmed")
    obligations = [
        "subscription_owner",
        "subscription_policy_owner",
        "billing_ops_owner",
        "payment_ops_owner",
        "funds_account_owner",
        "ledger_owner",
        "balance_state_owner",
        "reconciliation_owner",
        "mandate_owner",
        "compliance_owner",
        "agent_entitlement_owner",
        "access_policy_owner",
        "usage_rating_owner",
        "agent_usage_owner",
        "metering_owner",
        "workspace_owner",
        "seat_owner",
        "split_rule_owner",
        "settlement_owner",
        "payout_owner",
    ]
    model.update(
        {
            "business_ecosystems": ["payment_ecosystem", "agent_service_ecosystem"],
            "subdomains": [
                "billing_revenue",
                "merchant_platform_relationship",
                "payment_transaction",
                "account_balance",
                "funds_movement_settlement",
                "financial_operations",
                "risk_compliance",
                "agent_entitlement",
                "agent_usage_metering",
                "agent_workspace_seat",
            ],
            "bounded_contexts": [
                "commercial_subscription_context",
                "billing_invoice_context",
                "revenue_recovery_context",
                "payment_intent_context",
                "payment_attempt_authorization_context",
                "balance_ledger_context",
                "fund_state_context",
                "reconciliation_context",
                "mandate_authorization_context",
                "agent_entitlement_context",
                "agent_usage_metering_context",
                "agent_workspace_seat_context",
                "split_allocation_context",
                "settlement_batch_context",
                "payout_context",
            ],
            "aggregate_roots": [
                "commercial_subscription",
                "invoice",
                "dunning_case",
                "payment_intent",
                "payment_attempt",
                "ledger_entry",
                "fund_state",
                "reconciliation_record",
                "mandate",
                "agent_entitlement",
                "usage_event",
                "seat_assignment",
                "split_rule",
                "settlement_batch",
                "payout",
            ],
            "fact_owners": list(obligations),
            "role_obligations": list(obligations),
            "context_handoffs": [
                {
                    "from_context": "commercial_subscription_context",
                    "to_context": "billing_invoice_context",
                    "type": "command",
                    "name": "GenerateInvoice",
                },
                {
                    "from_context": "billing_invoice_context",
                    "to_context": "payment_intent_context",
                    "type": "command",
                    "name": "ChargeInvoice",
                },
                {
                    "from_context": "payment_attempt_authorization_context",
                    "to_context": "balance_ledger_context",
                    "type": "domain_event",
                    "name": "PaymentSucceeded",
                },
                {
                    "from_context": "commercial_subscription_context",
                    "to_context": "agent_entitlement_context",
                    "type": "domain_event",
                    "name": "CommercialSubscriptionActivated",
                },
            ],
            "non_domain_terms": ["subscription", "account", "settlement"],
            "open_questions": ["Confirm first-release payout/split settlement scope."],
            "candidates": [],
        }
    )
    return model


def _empty_domain_model(status: str = "candidate_pending") -> dict[str, Any]:
    return {
        "status": status,
        "business_ecosystems": [],
        "subdomains": [],
        "bounded_contexts": [],
        "aggregate_roots": [],
        "fact_owners": [],
        "role_obligations": [],
        "context_handoffs": [],
        "non_domain_terms": [],
        "open_questions": [],
        "candidates": [],
    }


def _candidate_terms(text: str) -> list[dict[str, str]]:
    lowered = text.lower()
    candidates: list[dict[str, str]] = []
    if "carbon credit wallet" in lowered or "绿色积分" in text:
        candidates.append(
            {
                "id": "carbon_credit_wallet",
                "confidence": "low",
                "reason": "material mentions carbon credit wallet vocabulary not present in taxonomy v2",
            }
        )
    return candidates


def _looks_like_agent_subscription_payment(text: str, lowered: str) -> bool:
    agent_signal = "agent" in lowered or "智能体" in text or "AI 服务" in text
    subscription_signal = "订阅" in text or "subscription" in lowered or "续费" in text
    payment_signal = "支付" in text or "payment" in lowered or "扣款" in text
    return agent_signal and subscription_signal and payment_signal


def _append_actor_if(text: str, actors: list[dict[str, str]], markers: tuple[str, ...], actor_id: str, label: str, actor_type: str) -> None:
    if not _contains_any(text, markers):
        return
    if any(actor["id"] == actor_id for actor in actors):
        return
    actors.append({"id": actor_id, "label": label, "type": actor_type})


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)
