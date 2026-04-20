## Why

The repository now has at least one executable policy guard, but it still has to be run through a tool-specific script. Contributors do not yet have a single repo-level health-check entry point for workflow policy verification.

## What Changes

- Add a unified `repo health-check` script entry for repository policy checks.
- Route the existing draft-skill publication check through that entry point.
- Add tests proving the unified entry reports clean and failing states correctly.

## Capabilities

### New Capabilities
- `repo-health-check`: A single repository entry point for executable workflow-policy checks.

### Modified Capabilities
- `repo-policy-checks`: Policy checks now run through a stable repo-level health-check entry.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-repo-health-check/`.
- Adds a health-check script under `scripts/`.
- Adds tests under `tests/`.
