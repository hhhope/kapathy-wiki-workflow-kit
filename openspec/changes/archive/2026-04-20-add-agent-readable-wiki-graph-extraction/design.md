# Design: Agent-Readable Wiki Graph Extraction

## Problem

The repository now defines stable object names and minimal frontmatter fields, but
there is still no machine-readable artifact that collects those structures into one
graph-shaped output.

Without extraction, agents still have to read many pages directly to reconstruct:

- object families
- artifact layers
- typed relations

That is workable at small scale, but it does not scale cleanly as the wiki grows.

## Design Goals

The extraction workflow should:

- depend first on naming model and frontmatter model
- produce a minimal graph artifact, not a full graph platform
- separate extraction proof from visualization or scoring layers
- stay limited to the covered layers already formalized

## Covered Layers

Version 1 only extracts from:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

It does not yet extract from:

- `wiki/sources`
- `wiki/domains`
- `wiki/reports`
- `wiki/timeline`

## Extraction Contract

The extractor should emit at least:

- nodes
- edges

Each node should preserve:

- page path
- canonical object
- artifact type
- source layer

Each edge should preserve:

- source page path
- relation type
- target object or target page

## Supported Relation Types

Version 1 should support extraction of:

- `related_objects`
- `derived_from`
- `validates`
- `formalizes`

It may also preserve:

- `supersedes`
- `replaces`

as optional relation types when present.

## Output Shape

The minimal output should be a machine-readable artifact such as JSON.

The artifact should be designed for:

- agent inspection
- later graph analysis
- later visualization work

It should not assume a specific UI.

## Validation Boundary

The extraction proof should confirm:

- covered pages were scanned
- nodes were emitted with required identity fields
- typed edges were emitted from the shared relation vocabulary

The extraction proof should not claim:

- semantic completeness of every historical page
- full coverage of old pages predating the new model
- graph quality scoring
- visualization correctness

## Non-Goals

- no full graph viewer yet
- no relation scoring yet
- no forced old-page migration
- no semantic inference fallback as the primary contract

## Open Questions

- whether the first artifact should be a single JSON file or a JSON plus markdown report pair
- whether missing required fields should fail hard or emit warnings for v1
- whether extraction should include outbound-only edges or also resolved inbound summaries
