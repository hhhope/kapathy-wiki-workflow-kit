## Why

The repository already records workflow decisions, but the current container is inconsistent. Some decisions live only in chat, some in `AGENTS.md`, and some in `adr.md` files under individual OpenSpec changes. That makes decision review harder than it should be and blurs the line between:

- current change artifacts
- stable project decisions
- retros and event-layer notes

The repository has now converged on a clearer model: stable ADRs should live in the project wiki, not inside a single change folder. This change formalizes that container so decisions remain project-visible and reviewable across changes.

## What Changes

- Add a project-level ADR container under `wiki/adr/` with an index page.
- Migrate the current stable workflow/governance ADRs from change-local `adr.md` files into wiki ADR pages.
- Update repository instructions so future workflow-level ADRs are written to `wiki/adr/` while change artifacts keep links and checkpoints.
- Keep retros and logs separate from ADRs so decisions and failures remain independently reviewable.

## Capabilities

### New Capabilities
- `wiki-adr-container`: The repository SHALL provide a project-level ADR container for stable workflow and governance decisions.

### Modified Capabilities
- `material-collaboration-defaults`
- `agent-self-evolution-review-trace`

## Impact

- Adds ADR pages under `wiki/adr/`.
- Changes repository decision-observability guidance in `AGENTS.md`.
- Reframes change-local ADR files as references to the canonical wiki ADR pages rather than the only durable location.
