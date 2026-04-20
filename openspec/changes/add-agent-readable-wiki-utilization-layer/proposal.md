# Proposal: Add Agent-Readable Wiki Utilization Layer

## Why

The repository now has the full upstream graph stack:

- naming model
- frontmatter model
- graph extraction
- relation analysis
- semantic scoring

These layers can now produce structured artifacts, but the repository still lacks the
next practical layer: how an agent should actually use these artifacts when deciding
what to read, what to trust, and what to ignore.

Without an explicit utilization layer, the stack remains descriptive only. The agent
still has no stable repo-visible rule for:

- which artifact should be consulted first
- when structural analysis is enough
- when semantic scoring can shape context selection
- when unresolved pressure should block stronger claims

## What Changes

This change adds a first agent-utilization layer on top of the existing artifact stack.

The change will:

- define a minimal utilization contract for agent-side reading and context selection
- add a workflow that summarizes which canonical objects are the best current candidates for agent attention
- produce a machine-readable utilization artifact from the existing scoring output
- publish repository-visible guidance for using the stack without overclaiming its proof level

This change does not:

- build retrieval infrastructure
- add runtime routing automation
- resolve unresolved pages automatically
- treat utilization output as rollout proof

## Success Criteria

- The repository has a stable utilization-layer spec and workflow.
- A reusable utilization artifact can be generated from current scoring output.
- The artifact can identify high-confidence object candidates for agent reading while preserving unresolved pressure and proof boundaries.
- The repository keeps the boundary explicit: utilization guidance is stronger than scoring output alone, but weaker than retrieval proof or autonomous runtime behavior.
