## Context

The repository already established executable policy checking for draft skills through `scripts/repo_policy_check.py`. That closed the specific regression, but it still leaves contributors with a fragmented verification surface:

- policy-specific script names must be remembered manually
- there is no stable repo-wide entry point for "run the repository health checks"

The next useful step is not to add more policy logic. It is to create one narrow aggregation layer that can host policy checks over time.

## Goals / Non-Goals

**Goals**

- Provide a single CLI entry point for repository health checks.
- Reuse the existing draft-skill policy checker rather than duplicating logic.
- Keep output explicit enough to show which check passed or failed.

**Non-Goals**

- Add new policy rules beyond the already implemented draft-skill check.
- Replace the direct `repo_policy_check.py` script.
- Add CI integration in this change.

## Decisions

### Decision: The health-check entry is an aggregator, not a new source of policy truth

The new script should call existing check functions and report consolidated results. Policy logic stays in the underlying check modules.

Alternative considered:
- Move all policy logic into one large health-check file.
  - Rejected because it would couple unrelated checks and make future extension harder.

### Decision: The first health-check surface includes exactly one named check

The repository already has one mature executable rule: no active `SKILL.md` files under `skills-drafts/`. The health-check entry should expose that one check first and expand only through later changes.

Alternative considered:
- Add placeholder checks for archive review or broader repo hygiene.
  - Rejected because those checks are not yet implemented as executable rules.

## Evaluation Plan

### Baseline scenario

- Add a test that imports a non-existent unified health-check module and expects failure before implementation.

### After-change expectation

- The health-check entry reports `PASS` when no draft-skill violations exist.
- The health-check entry reports `FAIL` and includes the violating path when a temporary repo contains `skills-drafts/**/SKILL.md`.

## Risks / Trade-offs

- [Risk] A one-check health-check may look overly small. -> Mitigation: design it as an aggregator with explicit named checks so later additions are straightforward.
- [Risk] Contributors may still run the old script directly. -> Mitigation: keep the old script as a reusable module and route the new entry through it.
