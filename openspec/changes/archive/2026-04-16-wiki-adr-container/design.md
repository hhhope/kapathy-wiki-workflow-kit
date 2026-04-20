## Overview

This change establishes the canonical container for stable project decisions.

The repository needs four clearly separated layers:

- `OpenSpec change artifacts`
  - current scope, tasks, and implementation boundary
- `wiki/adr/`
  - stable project decisions and governance boundaries
- `retro / logs`
  - failures, deviations, and event-layer evidence
- `team lore candidates`
  - possible cross-project promotion later

The goal is not to duplicate all change design into ADRs. The goal is to extract only the stable decisions that remain useful after the originating change is over.

## Canonical placement

### OpenSpec

Keep these under `openspec/changes/<change>/`:

- `proposal.md`
- `design.md`
- `tasks.md`
- `specs/.../spec.md`
- `checkpoint.md` or equivalent branch note if work is interrupted

These files answer: "what is this change doing right now?"

### ADR

Keep stable decisions under `wiki/adr/`:

- one index page
- numbered ADR pages
- status per ADR such as `accepted` or `proposed`

These files answer: "what has this project decided and why?"

### Retro and logs

Keep failures and event-layer learnings outside ADR pages:

- `wiki/ops/...retro...`
- future project `logs/` if enabled

These files answer: "what happened and what went wrong?"

## Migration scope

This change migrates the current stable decisions from:

- `openspec/changes/material-collaboration-defaults/adr.md`
- `openspec/changes/hermes-skill-governance-review/adr.md`

into project-level wiki ADR pages.

The change-local ADR files remain as short reference stubs so existing change history stays understandable.

## ADR set

The initial wiki ADR set should cover:

1. repository-default workflow changes require OpenSpec
2. stable decisions belong in `wiki/adr/`
3. retros stay separate from ADRs
4. Hermes is treated as agent self-evolution governance, not just skill governance
5. incremental refresh is preferred over default full reprocessing

## Non-goals

- Do not add team-lore promotion in this change.
- Do not enable `logs/` as a mandatory container in this change.
- Do not rewrite all historical changes into ADRs.
- Do not turn every design detail into an ADR.
