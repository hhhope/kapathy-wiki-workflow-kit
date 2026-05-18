# Design: README capability map boundary

## Reader And Job

README is a repo-public artifact for future contributors, agents, and the user
when opening the repository cold. Its job is to explain what this repository is,
how its layers fit together, what capabilities exist, and which documents own
behavioral authority.

README should help a reader choose the next artifact to inspect. It should not
become the artifact that owns runtime behavior.

## Capability Map Shape

README should describe these repository layers:

| Layer | Role |
| --- | --- |
| `wiki/sources` | Source evidence and upstream material records. |
| `wiki/domains` | Durable business or topic understanding. |
| `wiki/timeline` | Period-based review and reporting views. |
| `wiki/reports` | Reader-facing drafts and report artifacts. |
| `wiki/ops` | Workflow traces, runtime methods, governance evidence, and learning records. |
| `wiki/adr` | Stable cross-change decisions. |
| `openspec` | Change lifecycle, specs, tasks, and evaluation evidence. |
| `wiki/status` | Generated health and diagnostic surfaces. |
| Future `wiki/moc` | Obsidian-visible projection pages, if approved by a later change. |

README should also describe capability groups:

- source capture and material processing
- frontmatter taxonomy and graph identity
- graph extraction and relation analysis
- status, scorecard, and health diagnostics
- wiki runtime routing, apply preview, and decision trace eval
- learning capture and OpenSpec lifecycle
- future Obsidian MOC projection

## Boundary

README may summarize the model and point readers to durable sources, but:

- OpenSpec owns scoped behavior changes and implementation tasks.
- ADR owns stable cross-change decisions.
- `wiki/ops` owns traces, retros, and operational evidence.
- Skills and command docs own operational entrypoint instructions.
- Generated status files own current health snapshots.
- README must not be treated as permission to execute runtime work or bypass
  OpenSpec.

## Drift Handling

The user explicitly flagged that the previous answer drifted from the requested
README description into runtime-entrypoint design. This change records that
correction in:

- `wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md`
- `wiki/adr/0034-readme-capability-map-is-project-description.md`

## Verification

Verification should confirm:

- README contains a clear capability map and boundary statement.
- The ops trace records the rejected framing and corrected framing.
- The ADR records the stable decision.
- New wiki pages pass targeted frontmatter precheck.
- OpenSpec validates this change.
- No runtime scripts, skills, AGENTS, or command behavior files are modified.
