# Proposal: Formalize Agent-Readable Wiki Naming Model

## Why

The repository already contains real evolution material across `wiki/ops`, `wiki/adr`,
`openspec/specs`, and `wiki/examples`, especially around disagreement management,
conversation handoff, and example-driven capture.

The problem is not missing content. The problem is that the same object family is
still named inconsistently across layers, and many titles still mix:

- topic object
- artifact type
- date
- status
- surface symptom phrasing

That makes the wiki harder for agents to read as an object network. The repository
needs a naming model that helps an agent distinguish:

- what object a page belongs to
- what artifact type the page is
- whether multiple pages belong to the same evolution chain

## What Changes

This change formalizes a repository naming model for evolution-bearing pages.

The model will:

- define a `canonical object / artifact type` naming structure
- define the admission rule for canonical objects
- define the first canonical object list
- define allowed artifact-type vocabularies for the first object families
- require cross-layer consistency of canonical object names across covered layers
- define rollout policy as strong-for-new and weak-for-old

This change only covers:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

This change does not:

- rename existing pages
- migrate directories
- define graph extraction metadata
- implement relation analysis or graph tooling

## Success Criteria

- New pages in covered layers stop inventing ad hoc title patterns.
- The same object can be traced across `ops`, `ADR`, `spec`, and `example` layers
  using one canonical object name.
- Dates, statuses, and symptom phrasing are clearly pushed out of the main title model.
- Future graph or relation-analysis work can use canonical object names as stable anchors.
