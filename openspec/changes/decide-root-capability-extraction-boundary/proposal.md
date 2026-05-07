## Why

The repo `AGENTS.md` now works as a compact loaded-context map, but recent
review exposed a boundary gap: some high-frequency skills are generic agent
capabilities while others are repository-specific workflows.

Because both kinds are listed under repo High-Frequency Skills, future agents
can misread runtime availability as ownership. That keeps root-capability
questions circulating inside repo governance instead of being classified for a
root successor change.

## What Changes

- Record the gap as a repo-visible retro.
- Record a stable ADR for root-capability extraction boundaries.
- Update the principle-skills and repo-AGENTS-loaded-context specs so runtime
  skill maps must distinguish ownership status.
- Update repo `AGENTS.md` minimally so High-Frequency Skills is explicitly a
  runtime map, not an ownership table.
- Do not edit root `~/.codex/AGENTS.md` or `~/.claude/CLAUDE.md`.

## Impact

- Adds `wiki/ops/root-capability-extraction-retro.md`.
- Adds `wiki/adr/0031-root-capability-extraction-boundary.md`.
- Updates `wiki/adr/index.md`.
- Updates repo `AGENTS.md`.
- Updates OpenSpec specs for principle skills and repo AGENTS loaded context.
- Does not migrate or rewrite any skill body.
- Does not promote root candidates into root behavior assets.
