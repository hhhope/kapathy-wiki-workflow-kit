# Proposal: Add Agent-Readable Wiki Semantic Scoring

## Why

The repository now has four upstream layers:

- naming model
- frontmatter model
- graph extraction
- relation analysis

These layers can already describe structural coverage, but they still do not provide a
stable semantic-strength signal for canonical objects.

The next step is not retrieval or runtime use yet. It is a bounded semantic-scoring
layer that helps answer:

- which canonical objects already have strong evidence of meaning and coverage
- which objects remain structurally present but semantically thin
- which unresolved areas still block stronger graph understanding

## What Changes

This change adds a first semantic-scoring layer on top of relation analysis.

The change will:

- define a minimal semantic-scoring contract
- add a workflow that scores canonical objects using bounded repository evidence
- generate a machine-readable semantic-scoring artifact
- publish repository-visible guidance for interpreting semantic scores

This change does not:

- add embeddings or semantic vector infrastructure
- add retrieval or runtime routing
- treat scores as rollout proof
- resolve unresolved pages automatically

## Success Criteria

- The repository has a stable semantic-scoring spec and workflow.
- A reusable semantic-scoring artifact can be generated from current repository state.
- The scoring artifact distinguishes stronger object families from weaker ones using explicit bounded signals.
- The proof boundary remains explicit: semantic scoring is stronger than structural analysis, but weaker than retrieval proof or runtime proof.
