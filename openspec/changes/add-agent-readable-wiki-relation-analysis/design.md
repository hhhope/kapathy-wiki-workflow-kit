# Design: Agent-Readable Wiki Relation Analysis

## Problem

The repository can now produce a structural graph artifact, but that artifact is still
low-level. It tells us what nodes, edges, and warnings exist, but it does not yet
summarize:

- which canonical objects have cross-layer coverage
- which objects remain weak or fragmented
- how much of the graph is still unresolved
- whether typed relations are actually appearing in practice

Without a relation-analysis layer, the repository can extract structure but cannot
reason about the quality of that structure in a reusable way.

## Design Goals

This change should:

- stay strictly downstream of graph extraction
- analyze the current extracted graph without inventing semantic guesses
- produce a machine-readable artifact that an agent can inspect cheaply
- preserve proof boundaries between structural analysis and semantic proof

## Core Approach

The workflow should:

1. read the extracted graph artifact
2. aggregate by canonical object and artifact type
3. summarize direct typed relation usage
4. summarize unresolved identity warnings by layer
5. emit an analysis artifact with stable sections

## Minimum Analysis Output

The analysis artifact should include at least:

- object coverage summary
- artifact-type distribution
- relation-type distribution
- unresolved warning summary
- analysis notes about proof boundaries

## Validation Boundary

This change should prove:

- relation analysis can be generated deterministically from the extracted graph
- the output helps identify strong object families versus unresolved legacy areas
- the boundary between structural analysis and semantic understanding stays explicit

This change should not claim:

- that the repository has semantic graph understanding
- that unresolved pages are now understood
- that relation analysis is equivalent to retrieval quality proof
- that graph analysis alone is enough to drive runtime routing

## Non-Goals

- no graph viewer
- no relation scoring with embeddings or semantic similarity
- no automatic page rewrites based on analysis output
- no full-repository migration

## Open Questions

- whether relation analysis should read the extractor output file or invoke the extractor directly
- whether first-version output should be only JSON or JSON plus a repo-visible summary page
- whether object quality should stay descriptive in v1 or include a lightweight rule-based score
