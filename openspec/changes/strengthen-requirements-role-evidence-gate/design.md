# Design

## Model

`RequirementCase` remains the workflow state. The taxonomy remains the
vocabulary. The checker remains the readiness gate.

Roles become case-local role instances:

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

User stories reference role instances:

```yaml
user_stories:
  - id: US-006
    role_ref: R-embedded-account-front
    want: 按已绑卡优先级轮询发起快捷支付
    benefit: 高优先级卡明确失败后继续尝试低优先级卡
    acceptance_function_ids:
      - AF-012
    evidence_anchor:
      source_functions:
        - F-006
```

Acceptance functions can use existing source anchors:

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

## Evidence Anchors

The checker uses `has_evidence_anchor(item, object_type)`.

Common anchors:

- `evidence_refs`
- `evidence_anchor`
- `source_section`
- `source_quote`
- `source_line`

Object-specific anchors:

- UserStory: `source_functions`
- AcceptanceFunction: `source_acceptance`, `source_functions`
- Role: `evidence_anchor` OR `source_actors` plus `normalization_note`

For roles, `normalization_note` is optional when `evidence_anchor` exists.
New cases should prefer `evidence_anchor` because it makes the role source
trace directly readable.

## Checker Modes

Strict mode is required for OpenSpec handoff. Compatibility mode lets legacy
case files remain readable.

Strict mode blocks:

- story has no `role_ref`
- `role_ref` points to a missing role
- `role_ref` points to non-confirmed role
- referenced role's `confirmed_as` does not map to taxonomy
- referenced confirmed role lacks role evidence, where role evidence passes
  with `evidence_anchor` OR `source_actors` plus `normalization_note`
- story or acceptance function lacks an evidence anchor

Compatibility mode allows legacy `story.role` checks and reports
`legacy_compatible: true` in the summary.

## Golden Sample

Only `wiki/ops/requirements-cases/2026-05-29-191857-embedded-account-phase1.md`
is migrated as a golden sample. Other historical cases are left untouched.
