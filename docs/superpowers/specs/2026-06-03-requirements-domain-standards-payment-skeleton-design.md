# Requirements Domain Standards And Payment Skeleton Design

Date: 2026-06-03
Status: written-for-user-review
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

Create an OpenSpec change named
`define-requirements-domain-standards-and-payment-skeleton`.

The change should define:

1. DDD domain standards.
2. Payment domain skeleton.
3. Domain collaboration relationships.
4. Compounding asset mechanism.
5. Taxonomy admission standards.
6. Current taxonomy mapping.
7. A `req-agent` domain-analysis stage that brings the standard into the
   requirements workflow.

The design's central claim:

```text
requirements domain modeling is cognitive infrastructure for human-Agent
collaboration, not a static classification list
```

## Non-Goals

- Do not finalize all payment taxonomy values in this change.
- Do not batch-migrate historical requirements cases.
- Do not change `wiki/config/frontmatter-taxonomy.yaml`.
- Do not implement tactical DDD objects such as aggregates, entities, value
  objects, or repositories.
- Do not make Agent subscription payments a top-level domain.
- Do not let the domain model authorize implementation without normal OpenSpec
  review.

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

Create:

```text
openspec/changes/define-requirements-domain-standards-and-payment-skeleton/
  proposal.md
  design.md
  tasks.md
  specs/
    requirements-domain-model/spec.md
    req-agent/spec.md
```

If existing OpenSpec conventions require a different spec name, keep the change
name stable and choose the nearest existing capability name.

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
- Payment domain skeleton SHALL be recorded as candidate first-pass structure,
  not final taxonomy approval.
- Existing `account`, `clearing`, and `settlement` values SHALL be mapped to
  the new skeleton with explicit compatibility boundaries.
- Domain collaboration SHALL describe upstream, downstream, shared language,
  handoff events, role participation, and fact-owner relationships.
- Requirements domain work SHALL produce compounding assets such as boundary
  decisions, counterexamples, collaboration patterns, handoff modes, acceptance
  patterns, or taxonomy gaps.

### req-agent

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

`req-domain-analysis` should:

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

The OpenSpec change should preserve these as candidates, not final approved
taxonomy IDs:

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

The change should not redesign the full requirements case schema in one step.
It should add a minimal domain-analysis section that can be rendered in case
files and checked for OpenSpec handoff readiness.

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

The OpenSpec change should include verification for:

- domain standard text is present in specs or design;
- payment skeleton candidates are documented and explicitly marked non-final;
- existing taxonomy mapping for `account`, `clearing`, and `settlement` is
  documented;
- `req-agent` routing includes domain analysis between intake and scope;
- readiness/handoff behavior does not allow taxonomy gaps to become automatic
  taxonomy mutations;
- Agent subscription-payment material can be analyzed as `计费与收入` primary
  domain with supporting domains.

## Risks

- The payment skeleton could still read like a function list if each candidate
  domain is not backed by problem space, language, object, lifecycle, rule, and
  collaboration evidence.
- Adding `req-domain-analysis` could bloat the first version if it tries to
  solve all taxonomy migration and case migration at once.
- Existing `account`, `clearing`, and `settlement` values must remain
  compatible until migration is explicitly scoped.
- Domain standards must not become a checklist that hides the original purpose:
  compounding human-Agent business cognition.

## Review Questions

1. Is this OpenSpec change scope correct, or should the domain standard and
   `req-agent` domain-analysis stage be split into separate changes?
2. Should `req-domain-analysis` be a formal repo-local skill in the first
   implementation, or only a new case section and controller route?
3. Should payment skeleton candidates be added to
   `requirements/config/requirements-taxonomy.yaml` in the first implementation,
   or only documented as candidates until owner review?
4. Is `define-requirements-domain-standards-and-payment-skeleton` the right
   change name?
