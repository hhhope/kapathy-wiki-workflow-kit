# Design

## Source Design

Primary approved design:

- `docs/superpowers/specs/2026-06-29-stripe-ai-payment-capability-sharing-design.md`

The Superpowers design owns the writing method and chapter content. This
OpenSpec change owns implementation scope, verification, and completion
evidence.

## Reader Intent

Reader:

- About 80 internal sharing participants.

Reader decision:

- Understand why AI-era payment and financial capability building is not mainly
  a feature race or payment-entry race.
- Recognize that when coding cost drops, financial domain design becomes more
  valuable: clear objects, interfaces, permissions, risk rules, settlement, and
  responsibility boundaries.
- Use Stripe as a case to study hard-but-correct domain work, not as a company
  praise piece.

Mainline:

> AI lowers coding and integration cost. The scarce capability is the ability
> to turn complex financial transactions into a clear, stable, composable
> domain design language. Stripe moves quickly into AI payment because it has
> spent years reducing fragmented payment complexity into objects, interfaces,
> permissions, risk rules, settlement relationships, and evidence trails.

Non-goals:

- Do not make Stripe a hero biography.
- Do not claim Stripe will certainly win.
- Do not turn source volume into the story.
- Do not expose repo/OpenSpec/Superpowers workflow in reader-facing H5 content.

## H5 Structure

The H5 should present eight reader-facing chapters:

1. `AI 支付最容易被误读`
2. `为什么用 Stripe 做观察样本`
3. `AI 支付需要一套金融交易设计语言`
4. `Stripe 是怎么把这套语言攒出来的`
5. `LinkedIn：Stripe 的人员能力画像`
6. `JD：Stripe 还在补什么能力`
7. `未来五年：先过规则关，再过金融结果关`
8. `我们能学什么`

Chapters 2/3/4 are the load-bearing section group:

- Chapter 2 selects the sample and states the boundary.
- Chapter 3 defines the method and domain-language model.
- Chapter 4 proves the method through Stripe's capability accumulation.

## Chapter 2 Implementation

Purpose:

- Explain why Stripe is a high-quality sample for AI payment capability
  building.

Required content:

- Stripe is not used because it is famous or because it recently mentions AI.
- Stripe spans developer access, merchant operations, platform split payment,
  billing, risk, identity, settlement, stablecoin, and agent-facing transaction
  entry.
- The H5 must compare Stripe with large model companies, wallets/card networks,
  and other payment companies to show why each sample reveals different parts
  of the system.
- The H5 must state that Stripe is a sample, not the answer.

Reader-facing acceptance:

- A reader can answer "why Stripe" before reading company history.
- The section does not read like a company introduction.

## Chapter 3 Implementation

Purpose:

- Define the financial transaction design-language framework.

Required model:

```text
金融交易设计语言 = 对象 + 接口 + 权限 + 规则 + 资金关系 + 责任证据
```

Required explanation:

- AI reduces the cost of coding a payment feature.
- The harder work is defining the domain: merchant, order, price, subscription,
  split payment, identity, permission, risk, funds, settlement, dispute.
- When the domain language is stable, integration becomes fast, interfaces stay
  clear, permissions can be larger, and platform complexity is absorbed instead
  of pushed to each user.
- Use the retail/supply-chain analogy: speed comes from well-defined product,
  inventory, price, order, fulfillment, refund, and permission objects, not
  from writing order code alone.

Reader-facing acceptance:

- A reader can repeat the formula above.
- The section does not collapse into a list of Stripe product names.

## Chapter 4 Implementation

Purpose:

- Prove that Stripe's AI payment speed comes from accumulated hard domain work.

Required stages:

1. Developer access: API, docs, test mode, dashboard, webhook.
2. Platform and merchant operations: Connect, Billing, Radar, Terminal,
   merchant onboarding, platform controls.
3. Financial operations: Tax, Identity, Issuing, Treasury, Capital,
   reconciliation, revenue recognition.
4. AI customer pressure: usage/event billing, global revenue, fraud/resource
   abuse, tax and risk pressure.
5. Agent, wallet, stablecoin, and machine payment: agent commerce, wallet
   abstraction, Bridge/stablecoin, machine-readable payment protocols.

For each stage, the H5 must answer:

- What complex domain problem did Stripe simplify?
- Which object/interface/permission/rule/settlement relationship remained?
- Why does this make AI-era integration faster?

Reader-facing acceptance:

- The chapter proves accumulation rather than listing years.
- The chapter explains "hard but correct work" explicitly.

## LinkedIn And JD

LinkedIn:

- Maps current people background and capability clusters.
- Must be framed as people-capability profile, not generic talent flow.

JD:

- Maps capability-building intent and gaps.
- Must be framed as future investment signal, not shipped-outcome evidence.

## Visual Route

Output mode: H5/HTML.

Required visual jobs:

- Sample-selection map for Chapter 2.
- Domain-language framework diagram for Chapter 3.
- Capability accumulation timeline for Chapter 4.
- People-capability map for LinkedIn.
- Capability-gap table for JD.

Visuals must carry proof tasks. Decorative visuals are out of scope.

## Verification Plan

Required checks:

- Static grep checks for new thesis terms and rejected terms.
- HTML parse for the H5.
- `git diff --check`.
- Desktop and mobile screenshot verification when browser tooling is available.
- Gate review update with hard-gate status and residual risks.

Do not claim review-ready, published, or Feishu-synced.
