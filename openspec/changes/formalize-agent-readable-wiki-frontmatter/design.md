# Design: Agent-Readable Wiki Frontmatter

## Problem

The repository now has stable naming guidance for evolution-bearing pages, but the
pages still lack a minimal shared metadata contract for object identity and cross-page
relations.

That means an agent can often infer the right object from title and prose, but it still
cannot reliably answer low-cost structural questions such as:

- What canonical object does this page belong to?
- What artifact type is this page?
- Which other pages are directly related?
- Is this relation derivation, validation, formalization, or example linkage?

## Design Goals

The frontmatter model should:

- preserve the naming model as the primary title contract
- add minimal structure, not a full ontology
- support future graph and relation work without prematurely implementing it
- be cheap enough to apply to new pages consistently

## Covered Layers

Version 1 covers only:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

It does not yet cover:

- `wiki/sources`
- `wiki/domains`
- `wiki/reports`
- `wiki/timeline`

## Required Fields

Every new page in covered layers should carry at least:

- `canonical_object`
- `artifact_type`

These two fields are the structural mirror of the naming model.

## Required Relation Fields

Every new page in covered layers should be able to express direct links through:

- `related_objects`
- `derived_from`
- `validates`
- `formalizes`

Not every page must populate every relation field, but the field vocabulary itself
must be stable across covered layers.

## Optional Helper Fields

These helper fields remain optional in version 1:

- `supersedes`
- `replaces`
- `notes_scope`

They are useful, but not required for the first structural contract.

## Field Semantics

### `canonical_object`

The stable object family this page belongs to.

### `artifact_type`

The layer-specific artifact type, such as:

- `method`
- `retro`
- `adr`
- `spec`
- `example`
- `runtime-validation`

### `related_objects`

Peer object families directly related to this page's object.

### `derived_from`

Upstream material or page this page was derived from.

### `validates`

The object, method, or artifact this page validates.

### `formalizes`

The object, method, or operating rule this page formalizes into a more stable layer.

## Rollout Policy

The frontmatter model should roll out as:

- strong for new pages in covered layers
- weak for existing pages until they are touched or intentionally migrated

## Non-Goals

- no graph extractor yet
- no relation-scoring system yet
- no bulk metadata backfill yet
- no forced migration for old pages

## Open Questions

- whether `related_pages` is needed in addition to typed relation fields
- whether `supersedes` should become required for later revisions
- whether `readme-learning` eventually needs specialization fields beyond the shared contract
