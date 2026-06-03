---
layer: sources
domain: unclassified
classification_needed: true
source_type: external-docs
artifact_type: source-learning-note
canonical_object: payment-domain-taxonomy-prior-art
title: payment-domain-taxonomy-prior-art / stripe-adyen-airwallex / 2026-06-03
status: candidate-observation
created_at: 2026-06-03
source_title: "Stripe, Adyen, and Airwallex public documentation"
source_author: "Stripe; Adyen; Airwallex"
source_date: unknown
source_url: "https://docs.stripe.com/; https://docs.adyen.com/api-explorer; https://www.airwallex.com/docs/"
---

# Stripe / Adyen / Airwallex 支付领域划分学习记录

## Source Reference

- Stripe API and product documentation: <https://docs.stripe.com/>
- Stripe Connect: <https://docs.stripe.com/connect>
- Stripe Billing and usage-based billing: <https://docs.stripe.com/billing>
- Stripe reports and payout reconciliation: <https://docs.stripe.com/reports/balance>, <https://docs.stripe.com/payouts/reconciliation>
- Adyen API Explorer: <https://docs.adyen.com/api-explorer>
- Airwallex product docs: <https://www.airwallex.com/docs/>
- Airwallex connected accounts: <https://www.airwallex.com/docs/connected-accounts__how-connected-accounts-work>
- Airwallex payments for platforms: <https://www.airwallex.com/docs/payments-for-platforms__understanding-payments-for-platforms>
- Access date: 2026-06-03

## Source Classification

| Field | Judgment |
|---|---|
| Source class | primary source / public product documentation |
| Topic | payment ecosystem domain prior art |
| Local relevance | high for requirements taxonomy redesign; not a direct source of local taxonomy values |
| Retrospective score | 78 / 100 |
| Deep-read decision | useful as prior art, but not enough to finalize local taxonomy without domain-owner review |

## What Was Observed

The three vendors expose product and API surfaces around payment acceptance,
platform accounts, billing, payouts, issuing, risk, and reporting. Their public
navigation is useful evidence of capability clusters, but it is not a clean
domain model by itself.

Stripe is product-line oriented: Payments, Billing, Connect, Tax, Revenue
Recognition, Radar, Issuing, Treasury, Terminal, Financial Connections, and
reporting surfaces appear as product or API families.

Adyen is acquiring-and-platform oriented: Online Payments, In-person Payments,
Payouts, recurring, Platforms, Balance Platform, card issuing, business
accounts, risk, disputes, reports, and reconciliation appear as API or guide
families.

Airwallex is account-and-global-money oriented: Connected Accounts, Accounts,
Payments, Billing, Transactional FX, Payouts, Issuing, Spend, Global Treasury,
Banking as a Service, and Payments for Platforms appear as product or use-case
families.

## Correction From Live Review

The first local extraction wrongly turned public product functions into
candidate top-level domains. Examples of weak domain candidates:

- `clearing_reconciliation`
- `subscription_payments`
- `marketplace_settlement`
- `agent_subscription_payments`

These are too close to feature, scenario, or case names. They should not become
top-level requirement domains without an explicit domain-modeling pass.

## What Was Reused

Reusable prior-art signal:

- Payments companies separate customer-facing acceptance, platform enablement,
  billing/revenue, account or balance state, money movement, risk/compliance,
  and financial operations.
- Public docs mix multiple classification axes: product packaging, API
  resources, operating workflow, regulated entity model, and use case.
- A local requirements taxonomy must choose one primary axis before defining
  subdomains. Otherwise it will mix functions, workflows, and scenarios.

## What Was Modified For Local Context

For this repository, the useful next step is not to copy any vendor's product
navigation. The local taxonomy should first define:

- the top-level domain axis;
- what counts as a domain versus subdomain versus capability;
- whether `account`, `clearing`, and `settlement` are peer domains or lifecycle
  stages inside a broader payment ecosystem model;
- how platform/ecosystem work relates to account, payment, settlement, billing,
  risk, and operations.

## What Was Not Formalized

- No `requirements/config/requirements-taxonomy.yaml` change was made.
- No OpenSpec change was created by this learning note.
- No vendor product navigation was promoted into a local `SHALL`.
- No claim is made that the three vendors share one consistent domain model.
- No claim is made that `clearing_reconciliation` or similar feature-shaped
  labels are acceptable local domains.

## Repo Target

This note is input evidence for a future requirements taxonomy OpenSpec change,
likely around rebuilding the requirements domain skeleton before processing new
payment ecosystem requirements.

## Next Step

Create or select an OpenSpec change before editing the requirements taxonomy.
The design pass should define a domain skeleton first, then assign subdomains
and capability tags. Vendor documentation should be used as prior art, not as a
copy source.

Proof boundary: this record preserves external-source learning and a correction
from live review. It does not validate a final domain taxonomy and does not
authorize taxonomy config changes.
