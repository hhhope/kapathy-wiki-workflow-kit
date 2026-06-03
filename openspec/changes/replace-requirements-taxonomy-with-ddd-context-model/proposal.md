# Proposal

## Why

The current requirements taxonomy is a flat `domains` and `roles` vocabulary.
It can classify simple requirements, but it cannot carry DDD concepts such as
business ecosystem, subdomain, bounded context, aggregate root, lifecycle,
invariant, context handoff, fact owner, role obligation, or candidate evolution.

That gap caused the Agent service subscription payment draft to miss the
`account_balance` collaboration and funds/ledger owners after real funds
processing was confirmed.

## What Changes

- Replace the flat requirements taxonomy model with a DDD context model.
- Define `payment_ecosystem` and `agent_service_ecosystem`.
- Define payment subdomains, bounded contexts, aggregate roots, fact owners, and
  disambiguation rules.
- Define context-map handoffs for command, event, policy decision, and evidence.
- Define candidate subdomain/context evolution rules.
- Add a DDD taxonomy structure validator for this model.
- Include the Agent service subscription payment case mapping example.

## What Does Not Change

- Does not update `check_requirements_case.py`.
- Does not update `req-agent`, `req-domain-analysis`, or `req-scope` runtime behavior.
- Does not migrate historical requirement cases.
- Does not archive previous OpenSpec changes.
- Does not publish the final Feishu standard.

## Source Design

- `docs/superpowers/specs/2026-06-03-requirements-ddd-context-model-design.md`
