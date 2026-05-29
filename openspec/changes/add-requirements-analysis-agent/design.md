# Design

## Boundary

The requirements analysis agent is an intent-aware lifecycle controller. It is not a generic detailed-design reviewer.

The first version hard gate checks only:

- confirmed domain
- roles
- user stories
- acceptance functions

Business rules, exception scenarios, ADRs, APIs, DDL, test plans, and release plans are classified as soft warnings or design evidence.

## Authority

`requirements/config/requirements-taxonomy.yaml` owns requirement-readiness vocabulary. `wiki/config/frontmatter-taxonomy.yaml` remains limited to wiki page identity and graph-facing metadata.

Requirements case files own diagnosis, confirmation, normalization, and readiness. OpenSpec owns formal change lifecycle after readiness.

## Lifecycle

The state model is:

```text
intake -> diagnose -> confirm -> normalize -> gate -> recovery -> archive
```

OpenSpec draft handoff occurs only after the hard gate passes.

## Intent Recognition

The agent classifies user intent before taking action. Supported first-version intents are:

- `new_requirement_intake`
- `append_material`
- `diagnose_requirement`
- `confirm_requirement`
- `normalize_requirement`
- `check_requirements_ready`
- `create_openspec_draft`
- `status`

## Domain Recognition

Known domains are matched from `requirements-taxonomy.yaml`. Unknown domains remain candidates until the user confirms them. A case cannot become `requirements_ready` with an unconfirmed domain.

## OpenSpec Draft Handoff

Draft creation writes:

```text
openspec/changes/<change-id>/
  proposal.md
  design.md
  tasks.md
  specs/<capability>/spec.md
```

Drafts require user review before implementation planning.
