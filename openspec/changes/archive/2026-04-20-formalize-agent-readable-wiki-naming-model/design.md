# Design: Agent-Readable Wiki Naming Model

## Problem

The repository already preserves real disagreement and decision evolution, but that
evolution is still easier to read as prose than as structure.

The current title and naming patterns make object identity weak because the title
often carries too many concerns at once:

- the object
- the artifact type
- the date
- the current state
- the local symptom or framing of the moment

For agent-readable evolution, the naming system must foreground object identity first.

## Design Goals

The naming model should let an agent answer, at low cost:

- What object does this page belong to?
- What artifact type is this page?
- Does this page belong to the same evolution chain as another page?

The model is explicitly not trying to solve full-repository information architecture.

## Covered Layers

Version 1 covers only the layers that carry workflow evolution and stable decisions:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

The model does not yet apply to:

- `wiki/sources`
- `wiki/domains`
- `wiki/reports`
- `wiki/timeline`

## Core Naming Form

New pages in covered layers should use:

`canonical object / artifact type`

The title should answer only:

- what object this page belongs to
- what artifact type this page is

The title should not carry:

- dates
- statuses
- validation rounds
- change identifiers
- surface symptom words such as `gap`, `issue`, `missing`, `leak`
- sentence-shaped process descriptions

Those belong in metadata instead.

## Canonical Object Admission Rule

A topic qualifies as a canonical object only if all three are true:

1. It is not a one-time event page.
2. It already exists across at least two repository containers or artifact layers.
3. It can unify a real evolution chain instead of naming a temporary symptom.

This rule rejects candidates such as:

- `ADR 没更新`
- `TDD 没覆盖`
- `gate gap`
- pages whose identity is mainly a date or one validation run

## First Canonical Object List

The first-wave canonical objects are:

- `disagreement-management`
- `conversation-handoff`
- `example-driven-capture`

These are selected because each already spans multiple layers and can unify a real
evolution chain across repository artifacts.

## Allowed Artifact Types

### `disagreement-management`

Allowed artifact types:

- `method`
- `retro`
- `sample`
- `replay-harness`
- `replay-validation`
- `adr`
- `spec`
- `script-example`

### `conversation-handoff`

Allowed artifact types:

- `method`
- `sample`
- `retro`
- `runtime-rule`
- `adr`
- `spec`

### `example-driven-capture`

Allowed artifact types:

- `method`
- `sample`
- `runtime-validation`
- `example`
- `skill-route`
- `adr`
- `spec`

## Cross-Layer Consistency Rule

For covered layers, the canonical object name must remain identical across:

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

The repository should not rename the same object differently in different layers.

Example:

- `disagreement-management / method`
- `disagreement-management / adr`
- `disagreement-management / spec`
- `disagreement-management / replay-validation`

## Rollout Policy

The model should roll out as:

- strong constraint for new pages in covered layers
- weak constraint for existing pages until they are touched, rewritten, or intentionally migrated

This avoids a full-directory migration while still stopping new naming drift.

## Open Questions

- Whether `readme-learning` should later become its own canonical object or remain
  a specialization under `example-driven-capture`
- Which frontmatter fields should be added after title normalization stabilizes
- Whether a later follow-up should normalize filenames in addition to titles

## Non-Goals

- No immediate rename of existing pages
- No directory migration
- No graph extraction layer yet
- No automated relation-analysis tooling yet
