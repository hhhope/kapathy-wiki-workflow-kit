## Why

The repository already has naming, frontmatter, graph extraction, and relation
analysis artifacts, but the user still cannot read the repository in the three
most basic ways:

- by time
- by artifact type
- by a human-readable relation map

That creates a practical gap:

- drift is hard to review chronologically
- same-type documents are hard to compare side by side
- graph and relation outputs exist structurally but are not yet useful as a
  reading surface

The user explicitly wants to return to the earlier requirement instead of
continuing the runtime stack. This change scopes the next step down to readable
wiki views only.

## What Changes

- Add a timeline-reading view for the evolution-bearing wiki work.
- Add an artifact-type grouping view so same-type documents can be scanned
  together.
- Add a readable graph/relation view that turns existing structural outputs into
  a human-usable reading surface.
- Wire these views into the existing wiki indexes.

## Capabilities

### New Capabilities

- `wiki-readable-views`: The repository SHALL provide basic readable views for
  timeline, artifact grouping, and relation reading.

### Modified Capabilities

- `personal-ops`
- `timeline`

## Impact

- Adds OpenSpec artifacts under `openspec/changes/add-wiki-readable-views/`.
- Adds three repository-visible reading-view pages under `wiki/`.
- Updates existing index pages so the new reading views are discoverable.
- Does not change `openspec-explore`, runtime stack behavior, or graph
  automation scope.
