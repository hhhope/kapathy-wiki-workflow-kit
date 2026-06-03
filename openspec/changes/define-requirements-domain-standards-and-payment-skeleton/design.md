# Design

## Scope

This change establishes the requirements-domain standard and writes the first
runnable payment-domain skeleton into the requirements taxonomy. It is a
standards and configuration change, not a runtime req-agent flow change.

The next change, `add-req-domain-analysis-skill`, will add the formal
domain-analysis skill and wire it into req-agent collaboration.

## DDD Basis

This repository treats a requirements domain as a durable business problem
space, not as a feature, system, team, or implementation workflow. The standard
uses strategic DDD concepts:

- bounded context: the explicit business language and model boundary;
- ubiquitous language: terms that humans and Agents must use consistently;
- aggregate / core object: the object whose lifecycle and invariants define
  the domain;
- domain service / capability: behavior inside a domain, not a top-level domain
  by itself;
- context map: upstream/downstream/shared-kernel relationships between
  domains.

## Domain Model Construction

The domain model starts from the question: "what business problem space needs a
stable model so humans and Agents can collaborate repeatedly?"

Each accepted top-level domain must be able to express:

- the business problem it owns;
- core objects and lifecycle;
- rules and invariants;
- the owner of factual truth;
- neighboring domain boundaries;
- collaboration and handoff mode;
- typical requirement shapes;
- counterexamples that must not be admitted as top-level domains.

Candidates that cannot express those points become subdomains, capabilities,
case slugs, process names, system names, or rejected aliases.

## Payment Skeleton

The first payment-domain skeleton is intentionally broad enough to cover payment
ecosystem work but narrow enough to keep boundaries reviewable:

- `merchant_platform_relationship`
- `payment_transaction`
- `billing_revenue`
- `account_balance`
- `funds_movement_settlement`
- `financial_operations`
- `risk_compliance`
- `embedded_financial_products`

This skeleton handles the current Agent subscription payment example as a case:
its primary domain is `billing_revenue`, with collaboration across merchant /
platform relationship, payment transaction, account / balance, funds movement /
settlement, financial operations, and risk / compliance.

## Compatibility Mapping

Existing taxonomy values remain valid for compatibility:

- `account` maps toward `account_balance` when the requirement is about payment
  accounts, wallets, ownership, or balance lifecycle.
- `settlement` maps toward `funds_movement_settlement` when the requirement is
  about transfers, payouts, withdrawals, split settlement, settlement cycles, or
  receiver settlement.
- `clearing` maps toward `financial_operations` when the requirement is about
  clearing evidence, reconciliation, fee accounting, exception handling,
  reporting, or close support.

The current values are not removed in this change because historical cases and
existing readiness checks may still reference them.

## Collaboration Model

Domain collaboration is part of the standard because the goal is not taxonomy
classification for its own sake. A domain record must make work movable between
humans and Agents by exposing:

- upstream/downstream domains;
- shared language terms;
- handoff artifacts;
- role participation points;
- decision owner and fact owner;
- evidence that should compound for future cases.

## Proof Boundary

This change proves that the standard and first payment skeleton can exist in the
repo and pass current taxonomy/OpenSpec validation. It does not prove future
runtime domain analysis behavior; that proof belongs to the later
`req-domain-analysis` skill change.
