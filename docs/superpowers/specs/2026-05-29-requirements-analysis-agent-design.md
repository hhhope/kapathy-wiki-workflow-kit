# Requirements Analysis Agent Design

Date: 2026-05-29
Status: design-approved-for-spec-review
Repository: report-wiki-portfolio

## Problem

Implementation work is often started before the requirement is clear enough to
code. The common failure pattern is not missing code detail first; it is missing
requirement shape:

- the business domain is unclear or guessed
- the core roles and systems are not named
- user stories do not preserve role, goal, and value
- acceptance functions do not map back to user stories
- detailed design content such as ADR, API, DDL, and release plans is mixed into
  the same document and can be mistaken for confirmed requirement authority

The repository already has wiki frontmatter taxonomy and a medical-agent style
case-file state machine. The new requirements agent should reuse the discipline
of case files and deterministic gates without turning the first version into a
full detailed-design reviewer.

## Goal

Create a design for an intent-aware requirements lifecycle controller that can
turn raw requirement material into a normalized requirements case, verify a
small hard gate, and generate an OpenSpec draft only after the requirement is
ready.

The first version focuses on requirement readiness, not implementation design
correctness.

## Non-Goals

- Do not validate API correctness, DDL correctness, architecture quality,
  release readiness, or test-plan completeness in the first version.
- Do not make wiki frontmatter taxonomy the source of requirement quality.
- Do not auto-enter implementation after creating an OpenSpec draft.
- Do not force every unknown domain into an existing taxonomy value.
- Do not require wiki presence for the agent to operate.

## Core Positioning

```text
requirements-analysis-agent = intent-aware requirements lifecycle controller
check_requirements_case.py = deterministic gate evidence provider
requirements-taxonomy.yaml = requirement readiness contract
```

The agent's primary capability is intent recognition and requirement
understanding. Python checks provide reproducible evidence, but the checker is
not the agent.

## Authority Model

The design separates three authorities:

```text
requirements case file
  owns requirement diagnosis, confirmation, normalization, and readiness

OpenSpec
  owns formal change lifecycle after requirement readiness

implementation plan / code
  may start only from a reviewed OpenSpec change
```

If a wiki exists, the requirements case can be stored inside the wiki. If a wiki
does not exist, the same requirement gate still applies outside the wiki.

Wiki taxonomy and requirements taxonomy are separate:

```text
wiki/config/frontmatter-taxonomy.yaml
  validates page identity, layer, domain, ops_area, and graph-facing metadata

requirements/config/requirements-taxonomy.yaml
  validates requirement readiness: domain, roles, user stories, and acceptance
```

## Lifecycle

The first version uses a seven-stage state model:

```text
intake -> diagnose -> confirm -> normalize -> gate -> recovery -> archive
```

- `intake`: collect source material and optional wiki/OpenSpec context.
- `diagnose`: detect missing domain, missing roles, weak user stories, missing
  acceptance mappings, and mixed design evidence.
- `confirm`: move only user-confirmed facts into confirmed requirement data.
- `normalize`: produce a structured requirements case and a readable Markdown
  view.
- `gate`: run deterministic readiness checks.
- `recovery`: rerun checks after fixes or OpenSpec draft generation.
- `archive`: preserve the final case, evidence, checker result, and draft paths.

OpenSpec draft handoff happens after `gate` passes. It is not a lifecycle stage
that grants implementation permission by itself.

## Intent Recognition

The agent must classify the user request before deciding what to do.

First-version intents:

- `new_requirement_intake`
- `append_material`
- `diagnose_requirement`
- `confirm_requirement`
- `normalize_requirement`
- `check_requirements_ready`
- `create_openspec_draft`
- `status`

Intent recognition determines whether the agent should create a new case,
append evidence, ask for confirmation, run the checker, or create an OpenSpec
draft. A short user approval such as "可以" only advances the current gate; it
does not imply implementation permission.

## Domain Recognition

Domain recognition is a first-class agent responsibility.

Rules:

- If the material matches a registered domain in
  `requirements/config/requirements-taxonomy.yaml`, the agent may set
  `matched_domain`.
- If no registered domain matches, the agent must produce `candidate_domains`
  and ask for confirmation.
- Unknown domains must not be forced into an existing domain.
- Unconfirmed domain candidates keep the case in
  `awaiting_domain_confirmation`.
- The hard gate cannot pass without a confirmed domain.

Example for `Embedded Wallet.md`:

```json
{
  "intent": "new_requirement_intake",
  "domain_resolution": {
    "status": "candidate_pending",
    "matched_domain": "",
    "candidate_domains": [
      {
        "domain_id": "wallet-payment",
        "confidence": "medium",
        "reason": "document mentions wallet account, payment password, card binding, balance payment"
      },
      {
        "domain_id": "account-clearing",
        "confidence": "low",
        "reason": "document includes reconciliation and account ledger, but the core scenario is wallet payment"
      }
    ],
    "requires_user_confirmation": true
  },
  "next_action": "confirm_domain"
}
```

## Requirements Taxonomy

Add an independent requirements taxonomy:

```text
requirements/config/requirements-taxonomy.yaml
```

The first version must support a built-in account, settlement, and clearing
domain set:

```yaml
domains:
  account-clearing:
    aliases:
      - account
      - clearing
      - settlement
      - 账户
      - 结算
      - 清分
      - 清算
      - 清结算
```

The account-clearing role set is split by responsibility type:

```yaml
role_sets:
  account-clearing:
    business_actors:
      - retail_customer
      - financial_customer
      - merchant
      - split_recipient
      - agent_partner

    operation_owners:
      - retail_operator
      - financial_operator
      - finance_operator
      - clearing_operator
      - settlement_operator
      - compliance_operator
      - risk_operator
      - channel_operator
      - member_operator
      - product_owner

    system_actors:
      - member_system
      - product_shelf_system
      - account_system
      - clearing_system
      - settlement_system
      - payment_system
      - billing_system
      - reconciliation_system
      - risk_system
      - channel_system

    delivery_owners:
      - product_owner
      - engineering_owner
      - test_owner
      - release_owner
      - operations_owner
```

Business, operation, and system roles are used for requirement readiness.
Delivery owners are checked during OpenSpec handoff, not during basic
requirement readiness.

Unknown domains may define case-local roles, but each role must include its
responsibility, boundary, and related user-story or acceptance references.

## Case File Shape

The case file may live in either location:

```text
wiki/ops/requirements-cases/YYYY-MM-DD-HHMMSS-<slug>.md
requirements/cases/YYYY-MM-DD-HHMMSS-<slug>.md
```

When stored under `wiki/`, the file also needs normal wiki frontmatter. That
frontmatter is only page identity; it is not requirement readiness evidence.

The authoritative requirement data lives in a structured block:

```markdown
<!-- requirements-case-data:start -->
{
  "status": "awaiting_domain_confirmation",
  "context_source": "wiki_enhanced",
  "intent": "new_requirement_intake",
  "domain_resolution": {
    "matched_domain": "",
    "candidate_domains": [],
    "confirmed_domain": ""
  },
  "confirmed_requirements": {
    "domain": "",
    "roles": [],
    "user_stories": [],
    "acceptance_functions": []
  },
  "design_evidence": [],
  "soft_warnings": [],
  "gate": {
    "status": "blocked",
    "blocking_reasons": [],
    "checker_report": ""
  },
  "openspec_handoff": {
    "status": "not_ready",
    "change_id": "",
    "draft_paths": []
  },
  "proof_boundary_notes": []
}
<!-- requirements-case-data:end -->
```

Markdown around the block is a human-readable view. The structured block is the
checker source.

## Hard Gate

The first-version hard gate is intentionally small:

```yaml
required_sections:
  hard_gate:
    - domain
    - roles
    - user_stories
    - acceptance_functions

  soft_warnings:
    - business_rules
    - exception_scenarios
    - api_candidates
    - ddl_candidates
    - adr_candidates
    - test_plan_candidates
```

`check_requirements_case.py` blocks only when:

- confirmed domain is missing
- a user story lacks role, goal, or value
- an acceptance function does not map back to a user story
- a core role has no responsibility or system/business boundary
- a core unresolved placeholder affects requirement meaning
- OpenSpec draft generation is requested before `requirements_ready`

The checker emits soft warnings for business rules, exception scenarios, API,
DDL, ADR, test plans, release plans, and other detailed-design evidence. These
items are useful context but not first-version requirement authority.

Example result:

```json
{
  "passed": false,
  "status": "blocked",
  "blocking_reasons": [
    "user_story EW-US-003 has no acceptance_function_refs"
  ],
  "soft_warnings": [
    "DDL section found; classified as design_evidence, not requirement authority"
  ],
  "proof_boundary": [
    "This checker validates requirement readiness only.",
    "It does not validate API, DDL, architecture, release, or implementation correctness."
  ]
}
```

## Handling Mixed Documents

The `Embedded Wallet.md` sample is a mixed requirement and design document. It
contains user stories, acceptance standards, ADRs, sequence diagrams, API lists,
DDL, test cases, release material, and rollback plans.

First-version behavior:

- extract requirement-layer facts into `confirmed_requirements` only after
  confirmation
- classify ADR, API, DDL, release, and detailed test sections as
  `design_evidence`
- emit soft warnings for design evidence found in the source
- do not let design evidence make the hard gate pass
- do not block requirement readiness only because detailed design fields contain
  placeholders

The point is to prevent detailed design from polluting requirement authority
while still preserving it for later OpenSpec review.

## OpenSpec Draft Handoff

When the hard gate passes, the case becomes:

```text
status: requirements_ready
```

Only then may the agent create an OpenSpec draft:

```text
openspec/changes/<change-id>/
  proposal.md
  design.md
  tasks.md
  specs/<capability>/spec.md
```

Mapping rules:

- `proposal.md` comes from the confirmed domain, problem statement, and user
  story goals.
- `design.md` records high-level constraints and lists design evidence as
  candidate context, not final authority.
- `tasks.md` maps every acceptance function to at least one implementation or
  verification task.
- `spec.md` maps acceptance functions into OpenSpec requirements and scenarios.

Hard rules:

- no OpenSpec draft when `requirements_ready` is false
- generated drafts require user review before implementation planning
- design evidence does not become an implementation task unless confirmed in
  scope
- user-story and acceptance-function IDs must be traceable from OpenSpec draft
  back to the requirements case

## Expected User-Facing Output

Every normal agent response should show:

- intent
- case path or candidate case
- domain status
- hard-gate status
- blocking reasons, when blocked
- soft warnings, when relevant
- next action

Compact example:

```text
Intent: new_requirement_intake
Domain: candidate_pending (wallet-payment medium, account-clearing low)
Case: requirements/cases/2026-05-29-embedded-wallet.md
Gate: blocked
Blocked: confirmed domain required before requirements_ready
Soft warnings: API, DDL, ADR, and release sections found as design evidence
Next Action: confirm_domain
```

## Testing And Evidence

The implementation plan should include focused tests for:

- intent classification
- known-domain matching
- unknown-domain candidate handling
- hard gate passing and blocking
- soft warning classification for mixed documents
- OpenSpec draft blocked before readiness
- OpenSpec draft generation after readiness
- wiki-optional operation

Use `Embedded Wallet.md` as a mixed-document fixture shape, but avoid depending
on that desktop path as a permanent repo fixture unless the material is copied
or reduced into a committed test fixture.

## Proof Boundary

This design only proves a requirement can be normalized and checked for
first-version readiness. It does not prove that the later architecture, API,
database schema, implementation plan, or code is correct.

Before implementation begins, accepted behavior must be copied into an OpenSpec
change because OpenSpec remains the repository source of truth for large
changes.
