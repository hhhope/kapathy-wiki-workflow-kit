# Proposal: Add Agent-Readable Wiki Runtime Context Integration

## Why

The repository now has the full upstream artifact stack:

- naming model
- frontmatter model
- graph extraction
- relation analysis
- semantic scoring
- utilization layer

These layers can now tell us which canonical objects are stronger, weaker, preferred,
or blocked. But the repository still lacks the next practical step:

how an agent should convert that guidance into a concrete runtime context bundle for a
live task.

Without that layer, the stack still stops short of operational use. The agent can see
scores and bands, but it still must manually decide:

- which objects to load first
- which pages to treat as supporting context
- which blocked objects to keep out of the first-pass bundle
- how repository caution should appear in a runtime-ready context artifact

## What Changes

This change adds a first runtime-context integration layer on top of utilization.

The change will:

- define a minimal runtime-context contract
- derive a machine-readable context bundle from utilization guidance
- preserve repository-level caution signals in the bundle
- publish repository-visible guidance for using the context bundle in live agent work

This change does not:

- build an external retrieval system
- automate runtime routing into every agent entrypoint
- resolve unresolved pages automatically
- treat runtime-context output as autonomous runtime proof

## Success Criteria

- The repository has a stable runtime-context spec and workflow.
- A reusable context bundle can be generated from current utilization output.
- The bundle clearly separates preferred context, cautious supporting context, and blocked items.
- The repository keeps the boundary explicit: runtime-context integration is stronger than utilization guidance, but weaker than autonomous runtime behavior.
