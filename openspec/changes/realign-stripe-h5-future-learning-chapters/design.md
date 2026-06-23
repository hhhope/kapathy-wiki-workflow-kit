# Design: Future Judgment And Learning Chapter Split

## Source Of Decision

Use the live conversation continuation on 2026-06-23 and the existing redesign
document:

`docs/superpowers/specs/2026-06-22-stripe-ai-transaction-control-plane-redesign.md`

The detailed design already contains `### 12. 我们能学什么`, but the user has
now changed the final structure:

- Chapter 12 becomes future judgment.
- Chapter 13 becomes `我们能学什么`.

## Chapter 12: Future Judgment

Working title:

`未来五年：Agent 支付会先过规则关，再过金融结果关`

Purpose:

- locate the current stage;
- explain the next-five-year path;
- distinguish technical readiness from regulatory / liability readiness;
- explain why AP2 / MPP / x402 are rule systems that agents follow;
- define the business threshold for real adoption.

Core thesis:

`Agentic payment` is not agents becoming financial subjects. It is financial
rules becoming machine-readable, callable, limited, auditable, and settleable by
software.

### Visual

Use a folded line chart instead of cards.

X-axis:

- 2024
- 2025
- 2026
- 2027
- 2028
- 2029
- 2030
- 2031

Y-axis:

- L1 信息辅助
- L2 任务执行
- L3 受限交易
- L4 可审计金融执行

Lines:

- technical integration
- authorization / liability
- regulatory acceptance
- commercial outcome

Must show:

- current stage marker: `2026 / L2.5`
- 2026-2027: L3 limited payment forms
- 2027-2028: machine-readable catalogs, prices, inventory, tax, returns, and
  service objects deepen
- 2028-2029: L4 pilots expand in API, content, compute, procurement, and
  high-frequency small-value payments
- 2029-2031: early L4 institutionalization is conditional on authorization,
  audit, disputes, settlement, regulation, and liability rules

### Historical Time-Constant Strip

Add a compact reference strip below the chart. The references are analogies for
time constants, not direct equivalence:

- narrow instrument equivalence: roughly 1-2 years
- payment-account / open-banking style rule change: roughly 3-5 years
- money, credit, stablecoin, cross-platform liability, and autonomous execution
  boundaries: roughly 5-10 years

The implementation may name examples such as Check 21, PSD2 / Open Banking,
MiCA / stablecoin, and EU Digital Identity Wallet only with source boundaries.

### Trend Points To Keep

The chapter should incorporate these trend points in structured form:

- no-app / no-front-end interaction is one signal, not the whole story;
- search shifts toward fulfillment / outcome delivery;
- outcome-based pricing becomes a test of value, such as payment per resolved
  customer outcome or per financial outcome;
- agent ecosystems matter because distribution shifts toward who can complete
  a workflow, not only who can show a link;
- conversion improves when discovery, eligibility, checkout, authorization, and
  payment confirmation lose friction;
- credit terms may eventually price the financial result, not just the tool
  usage.

## Chapter 13: What We Learn

Working title:

`我们能学什么：金融创新最终比的是关系设计`

Purpose:

Convert the Stripe case into a reusable business-analysis framework.

Required points:

- AI lowers coding, integration, testing, and customization cost.
- AI does not remove the institutional subjects of finance: people,
  organizations, merchants, platforms, banks, networks, regulators, and users.
- Financial design costs rise: product design, pricing, evaluation,
  explanation, audit, liability, consumer protection, tax, accounting, risk,
  settlement, and dispute boundaries.
- Payment companies compete by turning transaction and credit relationships into
  objects, APIs, pricing, authorization rules, risk controls, settlement flows,
  and ecosystem packages.
- Stripe's lesson is compounding standardization: API, domain model, docs,
  test mode, Connect, Billing, Radar, Tax, Issuing, wallets, stablecoins,
  machine payments, and credit all reuse the same operating logic.

## Copy Rules

- Avoid AI-sounding abstractions such as "让 AI 付款" as the main explanation.
- Avoid unsupported certainty such as "agent 一定能赚钱".
- Use business thresholds: conversion, revenue, cash-flow control, risk cost,
  credit terms, dispute cost, and settlement reliability.
- Do not use internal workflow labels as page titles.
- Do not turn source citations into a standalone source-management dashboard.

## Verification

- Static grep must find Chapter 12 and Chapter 13 headings.
- Static grep must find L1-L4 labels and `2026 / L2.5`.
- Static grep must find AP2 / MPP / x402 in the rule/protocol explanation.
- Static grep must confirm the old final broad closing title is not the final
  synthesis.
- HTML parser must pass.
- `git diff --check` must pass.
- Desktop and mobile screenshots must be read back for the new chart and final
  learning chapter.
