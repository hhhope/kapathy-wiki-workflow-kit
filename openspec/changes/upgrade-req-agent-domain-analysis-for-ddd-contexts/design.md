# Design

## Scope

This change upgrades requirements analysis and worker guidance so new cases can
be analyzed against taxonomy v2. It does not change the taxonomy skeleton or
the readiness checker gate semantics.

## Output Layers

Requirements analysis should produce three distinct layers:

- `actors`: real people, organizations, systems, or automation mentioned by the
  material.
- `domain_model`: DDD classification against taxonomy v2.
- `role_obligations`: fact-owner obligations derived from selected bounded
  contexts, trigger rules, and handoffs.

`actors` are allowed to become user-story role refs. `role_obligations` are not
user-story actors by themselves; they are obligations that scope must assign to
people, systems, or owners.

## Domain Model Shape

The output should include a `domain_model` object compatible with the strict
readiness checker:

```yaml
domain_model:
  status: confirmed
  business_ecosystems: []
  subdomains: []
  bounded_contexts: []
  aggregate_roots: []
  fact_owners: []
  role_obligations: []
  context_handoffs: []
  non_domain_terms: []
  open_questions: []
```

## First Case Mapping

Agent service subscription payment material should map to:

- `payment_ecosystem`
- adjacent `agent_service_ecosystem`
- `billing_revenue`, `payment_transaction`, `account_balance`,
  `financial_operations`, `risk_compliance`
- Agent-service contexts for entitlement and optional usage/seats
- payment contexts for subscription, invoice, authorization, ledger, and
  reconciliation

When real funds are in scope, `account_balance` and `balance_ledger_context`
must be present.

## Skill Guidance

`req-domain-analysis` must avoid saying that `subscription_owner` or similar
role obligations are user actors. It should tell `req-scope` what obligations
must be assigned.

`req-scope` should turn actor evidence and role obligations into concrete
owners, boundaries, and open questions.

## Compatibility

The old `domain` field may remain in output as a compatibility summary, but the
authoritative strict gate shape is `domain_model`.

## Proof Boundary

This change proves new analysis output and skill guidance for DDD domain
analysis. It does not prove every historical case can pass strict v2 readiness.
