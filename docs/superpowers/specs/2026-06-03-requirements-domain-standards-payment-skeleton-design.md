# Requirements Domain Standards And Payment Skeleton Design

Date: 2026-06-03
Status: user-reviewed-split-change-direction
Repository: report-wiki-portfolio

## Problem

The current requirements taxonomy has only `account`, `settlement`, and
`clearing`. Those values are useful local vocabulary for account and
clearing/settlement work, but they are not enough to support broader payment
ecosystem requirements.

The deeper problem is not just taxonomy coverage. In AGI-era work, the
requirements workflow needs a durable domain model that lets humans and Agents
share business cognition instead of re-reading fragmented materials from zero
each time.

Current gaps:

- domain candidates can be feature names, system names, team names, or case
  slugs instead of business problem spaces;
- requirements cases can ask for a `domain` without recording why that domain
  owns the problem;
- cross-domain collaboration, handoff points, and role participation are not
  explicit domain-model outputs;
- new domain learning does not reliably compound into reusable assets for the
  next case;
- the Agent subscription-payment case cannot be represented cleanly by the
  current `account / clearing / settlement` skeleton.

## Goal

Create two OpenSpec changes.

First change:

```text
define-requirements-domain-standards-and-payment-skeleton
```

It should define:

1. DDD domain standards.
2. Payment domain skeleton.
3. Domain collaboration relationships.
4. Compounding asset mechanism.
5. Taxonomy admission standards.
6. Current taxonomy mapping.

It should also write the first payment skeleton into
`requirements/config/requirements-taxonomy.yaml` so the process can run against
real taxonomy values instead of staying as a document-only proposal.

Second change:

```text
add-req-domain-analysis-skill
```

It should add the formal `req-domain-analysis` skill and wire it into the
`req-agent` workflow.

The design's central claim:

```text
requirements domain modeling is cognitive infrastructure for human-Agent
collaboration, not a static classification list
```

## Non-Goals

- Do not claim the first payment taxonomy skeleton is perfect or final.
- Do not batch-migrate historical requirements cases.
- Do not change `wiki/config/frontmatter-taxonomy.yaml`.
- Do not implement tactical DDD objects such as aggregates, entities, value
  objects, or repositories.
- Do not make Agent subscription payments a top-level domain.
- Do not let the domain model authorize implementation without normal OpenSpec
  review.
- Do not implement `req-domain-analysis` in the first change; it is explicitly
  split into the second change.

## DDD Basis

The change uses strategic DDD only:

- `Problem Domain`: model the long-running business problem space.
- `Subdomain`: separate top-level domains, subdomains, support domains, and
  common capabilities.
- `Ubiquitous Language`: preserve shared human/Agent business language.
- `Bounded Context`: make context-specific meanings explicit.
- `Context Map`: describe upstream/downstream, collaboration, shared language,
  dependency, and handoff relationships.
- `Model Purpose`: keep the model useful for requirements collaboration rather
  than trying to describe the whole business at once.

Tactical DDD terms remain future design tools, not first-version taxonomy
admission requirements.

## OpenSpec Shape

First change should create:

```text
openspec/changes/define-requirements-domain-standards-and-payment-skeleton/
  proposal.md
  design.md
  tasks.md
  specs/
    requirements-domain-model/spec.md
```

Second change should create:

```text
openspec/changes/add-req-domain-analysis-skill/
  proposal.md
  design.md
  tasks.md
  specs/
    req-agent/spec.md
```

If existing OpenSpec conventions require different spec names, keep the change
names stable and choose the nearest existing capability names.

## Spec Requirements

### requirements-domain-model

This new spec should define domain-modeling behavior for requirements work.

Required requirements:

- Domain standard SHALL define a domain as a durable business problem space and
  cognitive boundary for human-Agent collaboration.
- Domain admission SHALL use strategic DDD concepts rather than feature,
  interface, system, team, or case names.
- Domain candidates SHALL be classified as top-level domain, subdomain,
  capability, case, or non-domain item.
- Payment domain skeleton SHALL be written into the requirements taxonomy as
  the first runnable skeleton while remaining explicitly reviewable and
  evolvable.
- Existing `account`, `clearing`, and `settlement` values SHALL be mapped to
  the new skeleton with explicit compatibility boundaries.
- Domain collaboration SHALL describe upstream, downstream, shared language,
  handoff events, role participation, and fact-owner relationships.
- Requirements domain work SHALL produce compounding assets such as boundary
  decisions, counterexamples, collaboration patterns, handoff modes, acceptance
  patterns, or taxonomy gaps.

### req-agent, in second change

The existing `req-agent` behavior should gain a domain-analysis stage.

Target flow:

```text
req-intake
  -> req-domain-analysis
  -> req-scope
  -> req-stories
  -> req-acceptance
  -> req-handoff
```

The second change should create `req-domain-analysis` as a formal repo-local
skill. It should:

- classify the primary domain candidate;
- identify supporting domains;
- classify candidate terms as domain, subdomain, capability, case, or
  non-domain;
- record the domain decision reason;
- expose taxonomy gaps without mutating taxonomy;
- identify domain collaboration signals and handoff points;
- record candidate compounding assets for later review.

It should not:

- create user stories;
- write acceptance functions;
- create OpenSpec drafts;
- mutate `requirements/config/requirements-taxonomy.yaml`;
- silently force unknown domains into existing taxonomy values.

## Payment Domain Skeleton Candidate

The first OpenSpec change should write these into the requirements taxonomy as
the first runnable payment skeleton:

| Candidate Domain | Business Concern |
|---|---|
| 商户与平台关系 | merchant, platform, service provider, onboarding, qualification, capability enablement, platform responsibility |
| 支付交易 | payment order, payment method, authorization, debit, refund, dispute, payment state, retry |
| 计费与收入 | subscription, plan, pricing, usage, seat, invoice, dunning, grace period, revenue recovery |
| 账户与余额 | payment account, wallet, balance, ownership, available/pending/reserved funds, ledger view |
| 资金流转与结算 | transfer, payout, withdrawal, split, settlement batch, settlement cycle, platform fees |
| 财务运营 | clearing evidence, reconciliation, reports, fee accounting, exceptions, financial close support |
| 风险与合规 | KYC/KYB, AML, fraud, transaction monitoring, authorization constraints, consumer protection, tax/compliance evidence |
| 嵌入式金融产品 | issuing, treasury, capital, spend, BaaS; only when financial product scope is explicit |

Existing taxonomy mapping:

- `account` maps toward `账户与余额`.
- `settlement` maps toward `资金流转与结算`.
- `clearing` maps mostly toward `财务运营`, with a boundary to
  `资金流转与结算` when clearing directly drives payable/receivable and
  settlement execution.

## Agent Subscription Payment Mapping

Agent subscription payment is a case, not a top-level domain.

Expected mapping:

- primary domain: `计费与收入`;
- supporting domains: `支付交易`, `商户与平台关系`, `资金流转与结算`,
  `财务运营`, `风险与合规`;
- conditional domain: `账户与余额` if wallet, balance, escrow, or custody-like
  behavior enters scope;
- out of scope by default: `嵌入式金融产品`.

## Data And Case Shape

The second change should not redesign the full requirements case schema in one
step. It should add a minimal domain-analysis section that can be rendered in
case files and checked for OpenSpec handoff readiness.

Candidate section shape:

```yaml
domain_analysis:
  status: candidate_pending | confirmed
  primary_domain:
    id: ""
    label: ""
    status: confirmed | candidate_pending
    decision_reason: ""
  supporting_domains:
    - id: ""
      label: ""
      reason: ""
      handoff_signal: ""
  candidate_terms:
    - term: ""
      classification: domain | subdomain | capability | case | non_domain
      reason: ""
  taxonomy_gaps:
    - gap: ""
      reason: ""
      next_action: ""
  collaboration:
    upstream: []
    downstream: []
    shared_language: []
    handoff_events: []
    required_roles: []
  compounding_assets:
    - type: boundary_decision | counterexample | collaboration_pattern | handoff_pattern | acceptance_pattern | taxonomy_gap
      note: ""
```

This shape is a design candidate. The OpenSpec implementation may adjust field
names to fit existing scripts and case output conventions.

## Verification

The first OpenSpec change should include verification for:

- domain standard text is present in specs or design;
- payment skeleton values are present in
  `requirements/config/requirements-taxonomy.yaml`;
- existing taxonomy mapping for `account`, `clearing`, and `settlement` is
  documented;
- taxonomy checker / requirements checker still handles known domain values;
- Agent subscription-payment material can be mapped to `计费与收入` primary
  domain at analysis level.

The second OpenSpec change should include verification for:

- `req-agent` routing includes domain analysis between intake and scope;
- readiness/handoff behavior does not allow taxonomy gaps to become automatic
  taxonomy mutations;
- Agent subscription-payment material can be analyzed by `req-domain-analysis`
  as `计费与收入` primary domain with supporting domains.

## Risks

- The payment skeleton could still read like a function list if each candidate
  domain is not backed by problem space, language, object, lifecycle, rule, and
  collaboration evidence.
- Writing the first payment skeleton directly into taxonomy could create
  naming debt if domain owners later disagree with labels.
- Adding `req-domain-analysis` could bloat the second change if it tries to
  solve all taxonomy migration and case migration at once.
- Existing `account`, `clearing`, and `settlement` values must remain
  compatible until migration is explicitly scoped.
- Domain standards must not become a checklist that hides the original purpose:
  compounding human-Agent business cognition.

## User Decisions

1. The user decided to split this into two changes:
   `define-requirements-domain-standards-and-payment-skeleton` and
   `add-req-domain-analysis-skill`.
2. The user decided `req-domain-analysis` should be a formal repo-local skill.
3. The user decided the payment skeleton should be written directly into
   `requirements/config/requirements-taxonomy.yaml` in the first implementation.
4. The user accepted `define-requirements-domain-standards-and-payment-skeleton`
   as the first change name.
