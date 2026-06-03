# Design

## Scope

This change updates the requirements checker and focused tests so readiness can
be evaluated against taxonomy v2. It is a checker/readiness-gate change, not a
req-agent output-shape change.

## Gate Layers

`domain_model_gate` checks that a requirement is mapped to a stable DDD model:

- confirmed `business_ecosystem`
- confirmed `subdomains`
- confirmed `bounded_contexts`
- confirmed `aggregate_roots`
- confirmed `fact_owners`
- confirmed `role_obligations`
- explicit `context_handoffs`

`requirement_delivery_gate` keeps the existing delivery checks:

- confirmed role instances
- user stories linked to role instances
- acceptance functions linked to user stories
- evidence anchors for strict mode

The final hard gate passes only when both layers pass.

## Case Shape

New v2 cases may include a `domain_model` object:

```yaml
domain_model:
  status: confirmed
  business_ecosystems:
    - payment_ecosystem
    - agent_service_ecosystem
  subdomains:
    - billing_revenue
    - account_balance
  bounded_contexts:
    - commercial_subscription_context
    - balance_ledger_context
  aggregate_roots:
    - commercial_subscription
    - ledger_entry
  fact_owners:
    - subscription_owner
    - ledger_owner
  role_obligations:
    - subscription_owner
    - ledger_owner
  context_handoffs:
    - from: commercial_subscription_context
      to: balance_ledger_context
      type: domain_event
      name: subscription_renewal_paid
```

The old `domain` object remains readable for legacy compatibility, but strict
taxonomy v2 mode should prefer `domain_model`.

## Compatibility

When the taxonomy is v1 or the checker is explicitly called with
`strict=False`, legacy domain/role behavior remains available for old case
files. Compatibility mode is a reader path, not the authority for new v2 cases.

## Proof Boundary

This change proves checker semantics for v2 DDD cases and compatibility probes
for old case shapes. It does not prove req-agent can generate the new shape by
itself; that belongs to `upgrade-req-agent-domain-analysis-for-ddd-contexts`.
