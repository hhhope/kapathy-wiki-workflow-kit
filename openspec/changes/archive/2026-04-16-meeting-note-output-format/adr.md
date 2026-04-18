# ADR Set: Meeting Note Output Format

This file records decision-level notes for the `meeting-note-output-format` change.

## ADR-001: Meeting note output uses a strong delivery format, not generic summary blocks

- Status: accepted
- Date: 2026-04-15

### Context

The repository could already classify meeting materials and produce readable summaries, but the output did not meet the user's requirement for a directly usable meeting-minutes document. The weak point was not extraction quality alone; it was the absence of a fixed delivery structure.

### Decision

Meeting-note outputs in this repository will use a fixed section contract that includes:

- meeting metadata
- core agenda
- numbered topic sections
- final / rejected options when relevant
- structured action-item table
- closing summary and next steps

### Consequences

- Generic summary-only note output is no longer sufficient for meeting-note completion.
- Feishu meeting-note output and wiki source pages should share the same structure.

## ADR-002: Repo-local draft skill plus AGENTS is the enforceable path for now

- Status: accepted
- Date: 2026-04-15

### Context

The writable repository environment cannot host a new formally installed skill under `.codex/skills/`, but the user still wants future meeting-note processing to follow a fixed skill-like pattern.

### Decision

Until a writable formal skill location is available, the authoritative mechanism is:

- repo `AGENTS.md`
- repo-local `skills-drafts/meeting-note-output/`
- wiki template files

### Consequences

- Future sessions can follow a stable meeting-note format now.
- Promotion to a formally installed skill remains a separate follow-up step.
