## Why

The repository now has a hard policy that `skills-drafts/` is draft space only, but that rule still depends on human review. If a contributor later adds a new draft `SKILL.md`, the repo currently has no executable guard to catch it before the workflow regresses.

## What Changes

- Add an executable repository policy check that fails when `skills-drafts/` contains active `SKILL.md` files.
- Add tests that prove the checker fails on the forbidden state and passes on the allowed state.
- Record the new guard as the verification path for the draft-skill retirement policy.

## Capabilities

### New Capabilities
- `repo-policy-checks`: Repository-level executable checks for workflow publication boundaries.

### Modified Capabilities
- `project-local-skill-publication`: Formal skill publication now has an executable guard against draft runtime regressions.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/enforce-draft-skill-check/`.
- Adds a repo policy checker script under `scripts/`.
- Adds tests under `tests/`.
