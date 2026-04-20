# Proposal: Add Agent-Readable Wiki Relation Analysis

## Why

The repository has already completed the upstream layers for:

- naming model
- frontmatter model
- graph extraction
- small migration proof

At this point the repository can extract structure, but it still cannot analyze that
structure in a reusable way. The next missing layer is relation analysis: turning the
extracted graph into stable signals that help explain object coverage, unresolved
structure, and where the graph is still weak.

## What Changes

This change adds a first relation-analysis layer on top of the extracted wiki graph.

The change will:

- define a minimal relation-analysis contract
- analyze extracted nodes, edges, and warnings into a machine-readable report
- make explicit which signals are structural and which are not semantic proof
- publish repository-visible guidance for interpreting the analysis

This change does not:

- build a graph viewer
- add retrieval or runtime agent routing
- bulk-migrate old pages
- treat relation analysis as rollout proof for the whole repository

## Success Criteria

- The repository has a stable relation-analysis spec and workflow.
- A reusable analysis artifact can be generated from the extracted graph.
- The analysis distinguishes structural coverage from unresolved legacy areas.
- The repository keeps the proof boundary explicit: analysis is stronger than raw extraction, but weaker than semantic understanding or rollout proof.
