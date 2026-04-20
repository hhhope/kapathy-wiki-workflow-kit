## Context

The repository has accumulated enough formal assets to support structured
reading, but not enough reading views to make those assets usable under pressure.

What already exists:

- naming and frontmatter rules
- graph extraction and relation analysis
- drift retro and ADR history

What is still missing:

- a direct timeline view for the relevant evolution chain
- a same-type grouping view for cross-document comparison
- a readable relation view that does not require reading raw JSON artifacts

The user has already rejected further runtime-stack expansion in this thread.
This change therefore stays at the reading layer only.

## Goals / Non-Goals

**Goals**

- Make the recent evolution chain readable in time order
- Make same-type documents readable by grouped artifact type
- Make current graph/relation outputs readable without opening scripts or JSON
- Keep scope inside repo-visible wiki views

**Non-Goals**

- Do not change the `openspec-explore` command
- Do not redefine the explore-trace model
- Do not add new automation scripts
- Do not continue runtime, routing, injection, or autonomy work
- Do not bulk-migrate old pages

## Decisions

### Decision: Add a dedicated timeline reading page instead of overloading `wiki/timeline/index.md`

`wiki/timeline/index.md` should remain the stable entry point. The new readable
timeline belongs on its own page so the chronology can be expanded without
turning the index into a mixed navigation-and-analysis page.

### Decision: Add artifact grouping as a human-readable wiki page, not a script

The immediate gap is reading under pressure, not more machine-readable output.
The grouping view should therefore exist as a wiki page first.

### Decision: Add a readable relation map page that summarizes the existing structural layers

The repository already has graph extraction and relation analysis methods. The
missing part is a readable summary that points to the important objects, layers,
and warnings without requiring direct inspection of sample JSON output.

### Decision: Keep all three views narrow and index-linked

The views must be easy to find from:

- `wiki/index.md`
- `wiki/timeline/index.md`
- `wiki/ops/index.md`

This keeps the user on the reading surface instead of forcing code or artifact
inspection.

## View Shapes

### Timeline view

Must answer:

- what happened first
- where drift started
- what should still be considered part of the original requirement

### Artifact grouping view

Must answer:

- which pages belong to the same artifact family
- which layers currently hold those artifact families
- where the main comparison points live

### Readable relation view

Must answer:

- which canonical objects currently matter most
- which layers already exist for each object
- where unresolved reading pressure still exists

## Evaluation Plan

### Baseline scenario

- The user opens `wiki/index.md` and `wiki/ops/index.md`
- The user still cannot quickly reconstruct chronology, compare same-type pages,
  or use the graph/relation work as a reading surface

### After-change scenario

- The user can open one timeline page to review the relevant chronology
- The user can open one grouping page to compare same-type artifacts
- The user can open one readable relation page to understand current objects and
  reading pressure without touching JSON

### Evidence to record

- Before: existing indexes point to many individual pages but do not provide the
  three missing reading views
- After: the three views exist, are index-linked, and stay inside reading-layer
  scope
