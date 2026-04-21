## Why

The governance discussion has already converged on a practical repository
position: repo-local commit hooks should not be treated as part of the default
solution for `agents-governance-drift`.

Right now that conclusion exists in conversation, but the repository still has
older candidate material that can make the hook sound like a likely future
enforcement layer.

If this remains implicit, later work can reintroduce the hook as a default
assumption instead of as a new explicit proposal.

## What Changes

- Record a stable repository decision that repo-local commit hooks are not part
  of the accepted default governance path.
- Update repository guidance where needed so future Phase 1 work does not
  silently inherit hook assumptions.
- Record the explicit exception boundary for any future reversal.

## Capabilities

### New Capabilities

- `no-repo-local-commit-hook-default`: The repository SHALL not treat a
  repo-local commit hook as part of the default `agents-governance-drift`
  mainline unless a later change explicitly reverses that decision.

### Modified Capabilities

- `repo-agents-governance-phase0`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/decide-no-repo-local-commit-hook/`.
- Narrows future governance work by removing the hook as an implicit default.
