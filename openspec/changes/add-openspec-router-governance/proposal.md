# Add OpenSpec Router Governance

## Why

This repository already has OpenSpec lifecycle gates and Superpowers method
skills, but it did not have a small pre-action router for mixed
Superpowers/OpenSpec situations.

The current incident showed the gap: `$superpowers:brainstorming` was active,
but the agent moved directly into OpenSpec edits after a short approval. That
created valid-looking governance artifacts while bypassing the Superpowers
written-spec review gate.

Without a repo-visible router, future agents can repeat the same mistake:
OpenSpec may bypass Superpowers, or Superpowers artifacts may be mistaken for
authoritative lifecycle state.

## What Changes

- Add a repo-local `openspec-router` skill.
- Add an OpenSpec requirement for explicit workflow routing before mixed
  Superpowers/OpenSpec actions.
- Update `AGENTS.md` with a compact Workflow Routing section.
- Update `PROJECT.md` with one operating-model bullet for agent workflow
  routing.
- Add Superpowers design, plan, and replay artifacts for the router.
- Add evaluation evidence that checks skill behavior, AGENTS, PROJECT,
  OpenSpec delta, and the original incident route.

## Out Of Scope

- Product code changes.
- Runtime, backend, frontend, migration, API, report, or wiki medical-loop
  behavior changes.
- Global skill promotion.
- Archiving any existing OpenSpec change.
- Replacing OpenSpec as the source of truth.
