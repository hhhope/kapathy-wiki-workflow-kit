## Why

The repository already enforces a hard stop when an OpenSpec change reaches `all_done`, but it does not define the default closing action after that stop. As a result, completed changes accumulate under `openspec/changes/` with no consistent review path between:

- implementation complete
- archive-ready
- archived

This gap creates two recurring problems:

- `complete` changes remain mixed with still-active changes, which weakens the signal of the active change list
- archive blockers are handled inconsistently, with some cases fitting a task update and others needing an explicit governance record

The workflow needs a lightweight default that keeps human review in the loop without turning archive into an automatic directory move.

## What Changes

- Add an OpenSpec workflow change that defines `archive review` as the default next action when a change becomes `complete`.
- Define the lightweight evidence split between ordinary archive blockers and governance-heavy archive blockers.
- Record that complex archive-review judgments use a change-local `archive-review.md` file instead of hiding the reasoning only in chat or git history.
- Promote the same policy into the global personal `~/.codex/AGENTS.md` guidance after validating it in this repository.

## Capabilities

### New Capabilities
- `archive-review-defaults`: The workflow SHALL require an explicit archive review between OpenSpec completion and archival.

### Modified Capabilities
- `wiki-adr-container`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/archive-review-defaults/`.
- Updates repository workflow guidance in `AGENTS.md`.
- Adds a stable ADR clarifying how completion, archive review, and archival relate.
- Updates global personal guidance so the same closing model can be reused across repositories that follow OpenSpec.
