# Design: Agent-Readable Wiki Semantic Scoring

## Problem

Relation analysis can now tell the repository which objects are cross-layer and which
relations exist, but it still cannot express whether an object family has strong
meaningful coverage.

For example, an object may:

- appear in multiple layers
- have some relations
- still remain thin in practice because the pages are few, narrow, or weakly linked

Without a semantic-scoring layer, the repository can describe structure, but it cannot
produce a reusable "how semantically mature is this object family" signal.

## Design Goals

This change should:

- stay downstream of relation analysis
- use explicit bounded repository evidence instead of hidden semantic guessing
- produce a machine-readable artifact an agent can inspect cheaply
- keep proof boundaries explicit

## Scoring Approach

Version 1 semantic scoring should stay rule-based and transparent.

The workflow should:

1. read relation-analysis output
2. score each canonical object using explicit factors
3. emit both the score and the factor breakdown
4. preserve blocking signals such as unresolved warnings and missing layers

## Candidate Scoring Factors

The score should stay bounded and interpretable. Version 1 should use explicit factors
such as:

- cross-layer presence
- artifact-type variety
- relation presence
- formalization depth
- unresolved-structure penalty

Each factor should be visible in the output so the score is audit-friendly.

## Minimum Output

The semantic-scoring artifact should include at least:

- overall summary
- per-object semantic score
- factor breakdown per object
- residual unresolved structure notes
- proof-boundary notes

## Validation Boundary

This change should prove:

- semantic scoring can be generated deterministically from repository-visible evidence
- the score breakdown is explainable and bounded
- stronger objects and weaker objects are distinguishable in a reusable artifact

This change should not claim:

- semantic understanding of unresolved pages
- retrieval readiness
- runtime routing readiness
- objective truth about page meaning outside repository evidence

## Non-Goals

- no embeddings
- no LLM-based scoring
- no retrieval integration
- no automatic migration from score output

## Open Questions

- whether version 1 should score only canonical objects or also layers
- whether unresolved penalty should be global or object-local
- whether score output should be 0-10 or 0-100
