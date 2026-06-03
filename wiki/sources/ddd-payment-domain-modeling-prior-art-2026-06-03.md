---
layer: sources
domain: unclassified
classification_needed: true
source_type: external-docs
artifact_type: source-learning-note
canonical_object: ddd-payment-domain-modeling-prior-art
title: ddd-payment-domain-modeling-prior-art / payment-taxonomy / 2026-06-03
status: candidate-observation
created_at: 2026-06-03
source_title: "DDD reference material and payment platform public documentation"
source_author: "Eric Evans; Martin Fowler; Microsoft Learn; Stripe; Adyen; Airwallex"
source_date: unknown
source_url: "https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf; https://martinfowler.com/bliki/BoundedContext.html; https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis"
---

# DDD 支付领域建模学习记录

## Source Reference

- Eric Evans, `Domain-Driven Design Reference`: <https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf>
- Martin Fowler, `Bounded Context`: <https://martinfowler.com/bliki/BoundedContext.html>
- Microsoft Learn, `Use Domain Analysis to Model Microservices`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis>
- Microsoft Learn, `Use Tactical DDD to Design Microservices`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/tactical-domain-driven-design>
- Microsoft Learn, `Identify microservice boundaries`: <https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries>
- Stripe docs: <https://docs.stripe.com/>
- Stripe Connect: <https://docs.stripe.com/connect>
- Stripe Billing: <https://docs.stripe.com/billing>
- Adyen API Explorer: <https://docs.adyen.com/api-explorer>
- Airwallex docs: <https://www.airwallex.com/docs/>
- Airwallex Connected Accounts: <https://www.airwallex.com/docs/connected-accounts__how-connected-accounts-work>
- Prior local note: `wiki/sources/payment-domain-taxonomy-prior-art-stripe-adyen-airwallex-2026-06-03.md`
- Access date: 2026-06-03

## Source Classification

| Field | Judgment |
|---|---|
| Source class | primary DDD reference + vendor public docs |
| Topic | DDD-style payment domain taxonomy |
| Local relevance | high for requirements taxonomy redesign |
| Retrospective score | 84 / 100 |
| Deep-read decision | use for domain skeleton proposal; not enough to change taxonomy without OpenSpec and owner review |

## DDD Principles Reused

This repository should not treat product navigation, API groups, or workflow
steps as top-level domains by default.

Reusable DDD constraints:

- A domain is the business subject area the software is applied to.
- A model selects and abstracts parts of that domain for a purpose.
- A bounded context owns a model and language boundary.
- Large systems should not force one unified model across all areas.
- The same word can mean different things in different contexts, such as
  `account` in customer onboarding, payment balance, accounting ledger, and
  platform identity.
- Boundaries should follow business capabilities and domain concerns, not
  technical layers or API navigation.
- Aggregates and services are later tactical design objects; they should not be
  used to name the first domain skeleton.
- DDD is iterative. A coarse domain skeleton is acceptable before splitting
  finer contexts.

## DDD View Of Vendor Differences

### Stripe

Stripe's public model is revenue-platform oriented. `Payments`, `Billing`, and
`Connect` are presented as separate product surfaces, but in DDD terms they hint
at different bounded contexts:

- payment acceptance and authorization;
- customer billing, subscription, pricing, invoice, and usage lifecycle;
- platform and marketplace relationship management;
- balance, transfer, payout, and reconciliation workflows;
- risk, tax, identity, issuing, and treasury as adjacent specialized contexts.

Local lesson: Stripe is strongest evidence that subscription billing is not a
small feature under payments. It has its own language, lifecycle, aggregates,
and failure modes.

### Adyen

Adyen's public model is acquiring-and-platform oriented. Its docs emphasize
online/in-person payments, recurring details, payouts, platforms, balance
platform, issuing, business accounts, risk, reports, and reconciliation.

DDD interpretation:

- Adyen keeps merchant acquiring and payment method acceptance central.
- Platform work is close to account holder onboarding, balance accounts, payout
  schedules, issuing, and operational reporting.
- Financial operations such as reports and reconciliation are visible as
  operating contexts around payment flows, not as the same model as checkout.

Local lesson: Adyen is stronger prior art for merchant/payment/acquiring and
platform operations than for subscription revenue modeling.

### Airwallex

Airwallex's public model is account-and-money-movement oriented. It presents
Connected Accounts, Accounts, Payments, Billing, FX, Payouts, Issuing, Spend,
Global Treasury, BaaS, and Payments for Platforms.

DDD interpretation:

- The connected-account relationship is a strong bounded-context candidate
  because it defines who owns funds, who performs operations, what compliance
  applies, and how platform/customer responsibilities split.
- Wallet, multi-currency account, FX, payout, issuing, and spend are separate
  money-operation contexts that share account identity but use different models.
- Payments for Platforms combines payment acceptance, connected-account
  ownership, split/routing, payout, FX, and compliance.

Local lesson: Airwallex is strongest prior art for account ownership, wallet,
multi-currency funds movement, platform acting-on-behalf-of, and regulatory
responsibility boundaries.

## Local Domain Skeleton Candidate

This is not a taxonomy change. It is a DDD-informed candidate for an OpenSpec
proposal.

### Merchant And Platform Relationship

Owns merchant/platform/service-provider identity, onboarding, qualification,
capability enablement, platform responsibility, and platform-customer
relationship rules.

Why this is a domain: the same party can be a merchant, platform customer,
connected account holder, service provider, or settlement receiver. The meaning
depends on relationship and responsibility.

### Payment Transaction

Owns payment order, payment method, authorization, capture, debit, refund,
dispute, status convergence, retry, and payment-facing failure semantics.

Why this is a domain: it owns the lifecycle of a payment attempt and the rules
for whether money has been successfully collected or reversed.

### Billing And Revenue

Owns customer subscription, pricing, usage, seat, invoice, bill run, dunning,
grace period, revenue recovery, and revenue recognition handoff.

Why this is a domain: subscription and usage billing have their own lifecycle
before and after payment execution. The business question is not only "can we
charge?" but "what should this customer owe, when, under which plan, and how do
we recover failed revenue?"

### Account And Balance

Owns payment account, wallet, balance, available/pending/reserved funds, ledger
view, ownership, and account capability.

Why this is a domain: account state is not the same as payment state or invoice
state. It is the source of funds availability and ownership semantics.

### Funds Movement And Settlement

Owns transfer, payout, withdrawal, split, settlement batch, settlement cycle,
platform fee allocation, receiver settlement, and external bank movement.

Why this is a domain: after payment collection, money must be moved, split,
scheduled, and settled under ownership and liability rules.

### Financial Operations

Owns clearing evidence, reconciliation, reports, fee accounting, exception
handling, financial close support, and operational auditability.

Why this is a domain: reconciliation and reporting are not the same as
settlement execution. They answer "what happened, why does it match or not
match, and can finance close books?"

### Risk And Compliance

Owns KYC/KYB, AML, sanctions, fraud, transaction monitoring, refund/dispute
risk, auto-debit authorization constraints, tax/compliance evidence, and
consumer protection.

Why this is a domain: it cuts across payment, platform, billing, and settlement,
but has its own rules, decisions, and accountability.

### Embedded Financial Products

Owns issuing, treasury, cards, capital, spend, and other regulated financial
products when the platform moves beyond payments and settlement.

Why this is a domain: these capabilities have separate product economics,
regulation, account state, and lifecycle. They should not be forced under
ordinary payment acceptance.

## Local Mapping For Agent Subscription Payments

The Agent subscription-payment requirement should not be its own top-level
domain. In this skeleton:

- primary domain: `Billing And Revenue`;
- supporting domains: `Payment Transaction`, `Merchant And Platform Relationship`,
  `Funds Movement And Settlement`, `Financial Operations`, `Risk And Compliance`;
- conditional domain: `Account And Balance` if wallet/balance/escrow-like
  behavior is in scope;
- out-of-scope unless explicitly requested: `Embedded Financial Products`.

## What Was Not Formalized

- No requirements taxonomy file was changed.
- No OpenSpec proposal was created in this note.
- The English domain names above are candidate labels, not final YAML IDs.
- This note does not decide whether existing `account`, `clearing`, and
  `settlement` values should be kept, renamed, nested, or migrated.
- This note does not define aggregates, entities, or services.

## Next Step

OpenSpec proposal `reshape-requirements-domain-taxonomy` should define:

- domain versus subdomain versus capability versus case slug;
- acceptance criteria for promoting a candidate domain into taxonomy;
- compatibility strategy for current `account`, `clearing`, and `settlement`;
- DDD context map draft for the payment ecosystem;
- concrete mapping of Agent subscription-payment material through the new
  skeleton.

Proof boundary: this learning record combines DDD reference material and vendor
public documentation into local candidate reasoning. It is not an approved
taxonomy, not a requirements readiness gate change, and not a behavior rule.
