## Why

The repository has already completed three upstream steps:

- formalized the disagreement-management method
- promoted it into stable policy and ADR form
- added replay / harness validation beyond the initial formalization thread

What is still missing is runtime integration.

Right now the repository knows what disagreement management is, but it still does not fully connect that method to default behavior at the key runtime boundaries where drift actually happens:

- when a live disagreement should land in `wiki/ops retro`
- when archive review must check whether disagreement preservation or promotion was skipped

Without those runtime hooks, the method remains correct but too easy to bypass in real work.

## What Changes

- Integrate disagreement management into repository-default runtime behavior.
- Define when a live disagreement should default to `wiki/ops retro` rather than staying only in chat or jumping straight to conclusion layers.
- Add an archive-review check that asks whether the active change produced disagreement material that should have remained in method/retro form or been promoted.
- Keep the change focused on runtime routing and review gates, not executable harnesses or new replay evidence.

## Capabilities

### Modified Capabilities

- `disagreement-management-method`
- `archive-review-defaults`
- `personal-ops`

## Impact

- Adds a new OpenSpec change under `openspec/changes/integrate-disagreement-management-runtime/`.
- Will update repo guidance and `wiki/ops` operating documentation.
- May add or update an ops retro sample if needed to make the runtime landing shape explicit.
