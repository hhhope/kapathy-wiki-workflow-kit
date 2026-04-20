## Why

The repository already preserves disagreement better than before:

- disagreement can remain as calibration material
- anti-compression states are explicit
- unstable disagreement prefers `wiki/ops retro` before `ADR`

But a newer failure mode is still open. When live conversation already exposes scope drift or goal drift, the repository does not yet force a stop-and-reanchor step before more implementation continues. In practice that means:

- the agent can keep following the current technical chain after the user says the work has drifted
- `continue` can inherit the wrong branch of work
- disagreement may be preserved later, but not early enough to interrupt the wrong continuation

The missing layer is not another preservation rule. It is a live conversation re-anchor gate.

## What Changes

- Define a repository-default live conversation re-anchor gate downstream of disagreement detection but upstream of further implementation continuation.
- Define concrete trigger signals for scope drift / goal drift during live conversation.
- Define mandatory actions once the gate fires:
  - stop implementation continuation
  - restate the original confirmed requirement
  - compare the current execution chain against that requirement
  - create or update a repo-visible `wiki/ops retro` unless the disagreement is already fully resolved in the active change
- Define unblock conditions before implementation can continue.

## Capabilities

### New Capabilities

- `live-conversation-reanchor-gate`: The repository SHALL stop continuation and re-anchor to the last confirmed requirement when live conversation signals scope drift or goal drift.

### Modified Capabilities

- `disagreement-management-method`
- `personal-ops`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-live-conversation-reanchor-gate/`.
- Extends repository policy in `AGENTS.md`.
- Extends the disagreement-management method page with a re-anchor gate section.
- Records the current scope-drift dispute as repo-visible retro evidence.
