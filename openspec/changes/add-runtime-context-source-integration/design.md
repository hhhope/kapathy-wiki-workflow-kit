# Design: Runtime Context Source Integration

## Problem

The repository can now generate a runtime-ready bundle, but that bundle still contains
object-level guidance rather than concrete sources to read next.

That means the stack is still missing one operational bridge:

- runtime context says which objects matter
- but it does not point to the actual pages or files the agent should open

Without that bridge, every live usage still requires one manual translation step.

## Design Goals

This change should:

- stay downstream of runtime context
- resolve canonical objects into repository-visible source references only
- preserve blocked-state boundaries
- produce a machine-readable artifact an agent can inspect cheaply

## Core Approach

Version 1 should stay deterministic and repository-local.

The workflow should:

1. read the runtime-context artifact
2. map canonical objects to known repository source references
3. attach those references to preferred and supporting entries
4. preserve blocked objects without resolving them into first-pass reading targets

## Source Resolution Strategy

Version 1 should resolve only repository-local sources such as:

- `wiki/ops` method pages
- `wiki/adr` decision pages
- `openspec/specs` spec pages
- `wiki/examples` example pages

The mapping should stay explicit and deterministic rather than heuristic-heavy.

## Minimum Output

The source-integrated runtime artifact should include at least:

- summary
- preferred sources
- supporting sources
- blocked objects
- source-resolution notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can enrich runtime context with concrete source references
- preferred and supporting entries can point to real repo-visible paths
- blocked entries remain isolated from first-pass source selection

This change should not claim:

- external retrieval integration
- autonomous source loading
- semantic understanding of unresolved pages
- runtime autonomy

## Non-Goals

- no Feishu integration
- no vector index integration
- no automatic context injection into all agent runs
- no blocked-object override logic

## Open Questions

- whether version 1 should resolve only one source per object or a small ordered source list
- whether ADR pages should outrank method pages when both exist
- whether supporting objects should resolve fewer sources than preferred ones
