## Why

`openspec-explore` currently leaves most exploration context in chat history. This repository already uses `wiki/ops/` as the visible operating layer, but it has no default rule that requires an explore trace before exploration continues.

That gap creates three recurring problems:

- the repository loses the opening context of an exploration thread
- the same topic can be re-opened without a visible prior trace
- a later OpenSpec change can exist without a clear link to the exploration that opened it

The user wants a repository-default rule: every time `openspec-explore` is entered, the agent should first leave a lightweight trace in `wiki/ops/`.

## What Changes

- Define a repository-default policy that `openspec-explore` must first create or update a `wiki/ops/` explore-intake record.
- Reuse the existing `type: intake` container instead of inventing a new page type.
- Define the rule that same-topic exploration updates an existing trace instead of always creating a new page.
- Add a sample explore-intake page under `wiki/ops/` and connect it from the ops index.

## Capabilities

### New Capabilities
- `openspec-explore-wiki-trace`: The repository SHALL require a `wiki/ops/` explore-intake trace before continuing `openspec-explore`.

### Modified Capabilities
- `personal-ops`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/openspec-explore-wiki-trace/`.
- Updates repo guidance in `AGENTS.md`.
- Adds an explore-intake sample under `wiki/ops/`.
- Makes future exploration repo-visible even before a formal implementation change exists.
