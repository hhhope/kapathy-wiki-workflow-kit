# Requirements Case Role Evidence Design

## Context

`req-agent` already treats requirements case data as the live workflow state and
uses `requirements/config/requirements-taxonomy.yaml` as the requirements
readiness authority. The current checker verifies confirmed domain, taxonomy
roles, user stories, acceptance functions, and bidirectional story/acceptance
mappings.

A pressure test with `embedded-account-phase1` exposed a gap. The existing case
can pass readiness while roles are flattened into taxonomy buckets such as
`system_actor`. For example, `system_actor` can contain merchant system, unified
gateway, notification center, embedded account front, account core,
subscription payment product, and Baofoo channel. User stories that reference
only `system_actor` do not say which case-local actor performs the behavior.

The same pressure test showed that evidence must be enforced carefully. A
mechanical `evidence_refs` requirement produced noisy blockers for acceptance
functions even though each acceptance function already had `source_acceptance`
and often `source_functions`. The requirement should be a traceable evidence
anchor contract, not one mandatory field name.

## Goal

Strengthen requirements readiness without introducing a full knowledge graph,
RAG layer, weighting model, or cross-case entity merge.

The design keeps `RequirementCase` as the core state model and adds:

- case-local role instances;
- role confirmation status;
- `role_ref` from user stories to confirmed role instances;
- evidence anchor validation by object type;
- strict checker behavior for OpenSpec handoff;
- one migrated `embedded-account-phase1` golden sample.

## Non-Goals

- Do not modify `requirements/config/requirements-taxonomy.yaml`.
- Do not modify `wiki/config/frontmatter-taxonomy.yaml`.
- Do not batch-migrate all historical requirements cases.
- Do not add role weights, ranking, embeddings, RAG retrieval, or a general
  knowledge graph.
- Do not make generated OpenSpec drafts authorize implementation.

## Approach

Use the scoped schema plus checker approach:

1. New case generation writes case-local role instances.
2. Strict readiness checks require story roles to point to confirmed role
   instances.
3. Evidence is validated through an evidence anchor contract.
4. Legacy case shape remains readable, but strict handoff reports legacy
   blockers instead of silently treating old role fields as fully ready.
5. `embedded-account-phase1` is migrated as the single golden sample and test
   fixture.

This is intentionally smaller than a full requirements graph. Taxonomy remains
the vocabulary; the case file remains the state; the checker remains the gate.

## Data Model

### Roles

Roles become case-local role instances. A role instance identifies the exact
actor mention in the requirement material and maps it to a taxonomy role.

Example:

```yaml
roles:
  - id: R-embedded-account-front
    mention: 嵌入式账户前置
    confirmed_as: system_actor
    status: confirmed
    category: system_actors
    source_actors:
      - 嵌入式账户前置
    evidence_anchor:
      source_section: "5.1 参与角色/系统"
```

Allowed `status` values:

- `confirmed`
- `candidate_pending`
- `rejected`

Only confirmed role instances can satisfy strict readiness for user-story
actors.

Supporting roles can remain in the case. A supporting role that is not
referenced by any user story does not block handoff by itself.

### User Stories

User stories reference case-local role instances with `role_ref` instead of
only a taxonomy role.

Example:

```yaml
user_stories:
  - id: US-006
    role_ref: R-embedded-account-front
    want: 按已绑卡优先级轮询发起快捷支付
    benefit: 高优先级卡明确失败后继续尝试低优先级卡
    acceptance_function_ids:
      - AF-012
      - AF-013
      - AF-014
    evidence_anchor:
      source_functions:
        - F-006
```

Stories can keep legacy `role` as display or compatibility metadata, but strict
readiness uses `role_ref`.

### Acceptance Functions

Acceptance functions keep the current mapped structure. They must be
traceable, but `source_acceptance` and `source_functions` count as evidence
anchors.

Example:

```yaml
acceptance_functions:
  - id: AF-014
    source_acceptance: AC-014
    source_functions:
      - F-006
      - F-007
    user_story_ids:
      - US-006
      - US-007
    then: 当前卡支付结果未明时，系统先查单，不直接切下一张卡。
```

## Evidence Anchor Contract

The checker should validate traceability through
`has_evidence_anchor(item, object_type)` rather than a single required field.

Common accepted anchors:

- `evidence_refs`
- `evidence_anchor`
- `source_section`
- `source_quote`
- `source_line`

Additional accepted anchors:

- `UserStory`: `source_functions`
- `AcceptanceFunction`: `source_acceptance`, `source_functions`
- `Role`: `source_actors` plus `normalization_note`, with `evidence_anchor`
  preferred for new output

This preserves scientific traceability without creating field-name noise. In
the pressure test, all 26 acceptance functions had `source_acceptance`, so they
should pass evidence validation even without `evidence_refs`.

## Checker Rules

Strict readiness should require:

1. `domain.status` is `confirmed`.
2. `domain.confirmed` exists in the requirements taxonomy.
3. Every user-story `role_ref` exists in `roles`.
4. Every referenced role has `status: confirmed`.
5. Every referenced role's `confirmed_as` maps to a taxonomy role.
6. Every user story has `role_ref`, `want`, `benefit`, and
   `acceptance_function_ids`.
7. Every user story has an evidence anchor.
8. Every acceptance function has `user_story_ids`.
9. Every acceptance function has an observable `then`, `expected`, `summary`,
   or `name`.
10. Every acceptance function has an evidence anchor.
11. Story-to-acceptance and acceptance-to-story mappings are bidirectional.

Legacy compatibility:

- Existing cases with only `story.role` remain readable in compatibility mode.
- Strict handoff mode reports `story_role_ref_missing` instead of silently
  passing the legacy shape.
- Default OpenSpec handoff uses strict mode.

Blockers should identify the field and the next question, for example:

```json
{
  "code": "story_role_ref_missing",
  "field": "user_stories.US-006.role_ref",
  "reason": "user story must reference a confirmed case-local role instance",
  "question": "Select the role instance that performs US-006.",
  "evidence": "source_functions: F-006"
}
```

## Generation And Migration

New intake should generate role instances first, then map each instance to a
taxonomy role. It must not collapse all systems into a single `system_actor`
entry.

Example migration for system actors:

```yaml
roles:
  - id: R-merchant-system
    mention: 商户系统
    confirmed_as: system_actor
    status: confirmed

  - id: R-unified-gateway
    mention: 统一网关
    confirmed_as: system_actor
    status: confirmed

  - id: R-embedded-account-front
    mention: 嵌入式账户前置
    confirmed_as: system_actor
    status: confirmed

  - id: R-account-core
    mention: 账户核心
    confirmed_as: system_actor
    status: confirmed

  - id: R-subscription-payment-product
    mention: 订阅支付产品
    confirmed_as: system_actor
    status: confirmed

  - id: R-baofoo-channel
    mention: 宝付通道
    confirmed_as: system_actor
    status: confirmed
```

Example business actor mappings:

```yaml
roles:
  - id: R-merchant
    mention: 商户
    confirmed_as: financial_customer
    status: confirmed

  - id: R-terminal-user
    mention: 终端用户
    confirmed_as: retail_customer
    status: confirmed
```

`embedded-account-phase1` should be migrated as the only golden sample. It
should prove:

- strict checker can pass a real PRD-derived case;
- `source_acceptance` satisfies acceptance evidence;
- `role_ref` avoids the `system_actor` bucket problem;
- historical cases do not need immediate batch migration.

## Components

### `scripts/requirements_case.py`

- Render the new role instance shape for newly built case packages.
- Preserve compatibility with existing machine case data.
- Keep the markdown output readable for human review.

### `scripts/check_requirements_case.py`

- Add `has_evidence_anchor`.
- Add strict role instance checks.
- Add compatibility handling for legacy role shape.
- Return blockers with `code`, `field`, `reason`, and, when available,
  `question` and `evidence`.

### `scripts/build_requirements_analysis_agent.py` And Analysis Helpers

- Generate role instances instead of taxonomy role buckets.
- Keep unknown actors as `candidate_pending` with a confirmation question.
- Do not mutate requirements taxonomy.

### `scripts/requirements_openspec_draft.py`

- Require strict-ready case data before draft creation.
- Preserve role, story, acceptance, and evidence traceability in generated
  drafts.
- Keep draft creation as a stop condition.

## Tests

Add or update tests for:

- story with `role` but no `role_ref` is blocked in strict mode;
- `role_ref` pointing to a missing role is blocked;
- `role_ref` pointing to `candidate_pending` is blocked;
- `role_ref` pointing to a confirmed role passes;
- acceptance function with `source_acceptance` passes evidence validation;
- acceptance function with no evidence anchor is blocked;
- legacy case shape remains readable in compatibility mode;
- strict handoff mode reports legacy blockers;
- migrated `embedded-account-phase1` strict checker passes;
- `US-006` and `US-007` in the golden sample reference
  `R-embedded-account-front`, not bare `system_actor`;
- OpenSpec draft generation blocks when any referenced role is not confirmed.

## Acceptance Criteria

- New requirements cases use case-local role instances.
- Strict checker prevents flattened taxonomy buckets from satisfying story
  actor readiness.
- Evidence anchor validation is object-aware and does not require every object
  to use `evidence_refs`.
- Migrated `embedded-account-phase1` is a golden sample and passes strict
  checker.
- Existing non-migrated cases remain readable.
- No taxonomy file is changed.
- No historical batch migration is performed.
- User-facing `req-agent` blockers can show precise field, question, and
  evidence.

## Open Questions Resolved

- Scope: migrate only `embedded-account-phase1` as a golden sample.
- Strictness: only roles referenced by user stories must be confirmed role
  instances for handoff.
- Evidence: require traceability, not a mandatory `evidence_refs` field name.
- Approach: implement case schema plus checker plus golden sample, not a full
  requirements graph.
