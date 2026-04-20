# Design: Agent-Readable Wiki Utilization Layer

## Problem

The repository can now extract, analyze, and score canonical objects, but it still
does not tell an agent how to use those outputs.

That leaves an important gap:

- semantic scoring says which objects look strong
- relation analysis says where unresolved structure remains
- but no layer explains how an agent should combine those signals when selecting context

Without a utilization layer, the stack is informative but not operational.

## Design Goals

This change should:

- stay downstream of semantic scoring
- define agent-readable usage rules without pretending retrieval is solved
- produce a machine-readable artifact that highlights usable object candidates
- keep unresolved pressure visible as a utilization constraint

## Core Approach

Version 1 should stay explicit and rule-based.

The workflow should:

1. read semantic-scoring output
2. classify canonical objects into utilization bands
3. preserve reasons why an object is usable, cautious, or blocked
4. emit a small utilization artifact that an agent can inspect cheaply

## Utilization Bands

Version 1 should classify objects into at least:

- `preferred`
- `cautious`
- `blocked`

Banding should remain rule-based and transparent. Candidate signals include:

- semantic score band
- formalization depth
- unresolved repository pressure
- whether the object is only single-layer

## Minimum Output

The utilization artifact should include at least:

- overall utilization summary
- per-object utilization status
- utilization reasons
- repository-level caution signals
- proof-boundary notes

## Validation Boundary

This change should prove:

- the repository can generate deterministic agent-usage guidance from existing artifacts
- stronger and weaker usage candidates can be separated explicitly
- utilization output still preserves caution instead of flattening unresolved pressure away

This change should not claim:

- retrieval readiness
- runtime autonomy
- semantic understanding of unresolved pages
- that utilization output alone can replace direct source inspection

## Non-Goals

- no retrieval engine
- no automated runtime routing
- no page rewriting from utilization output
- no semantic expansion of unresolved pages

## Open Questions

- whether utilization should rank only canonical objects or also specific pages
- whether repository-wide unresolved pressure should globally cap utilization bands
- whether version 1 should emit a simple recommended-read list
