# Proposal: Add Runtime Context Source Integration

## Why

The repository now has a bounded runtime-context layer that tells an agent:

- which canonical objects are preferred
- which are supporting
- which are blocked

But the runtime bundle still stops one step short of direct use. It names canonical
objects, yet it does not resolve those objects into concrete source references that an
agent can open next.

Without source integration, the runtime bundle is still abstract. The agent must
manually translate:

- `preferred_context` objects
- `supporting_context` objects

into actual page paths or source files to read.

## What Changes

This change adds a first source-integration layer on top of runtime context.

The change will:

- define a minimal runtime-context source-integration contract
- derive concrete source references from runtime-context objects
- generate a machine-readable source-integrated runtime bundle
- publish repository-visible guidance for how an agent should use those source references

This change does not:

- connect external systems such as Feishu or vector databases
- automate runtime routing into every agent entrypoint
- override blocked objects automatically
- treat source integration as autonomous retrieval proof

## Success Criteria

- The repository has a stable source-integration spec and workflow.
- A runtime-context bundle can be enriched with direct source references from current repository state.
- Preferred and supporting objects resolve into concrete source references while blocked objects remain isolated.
- The repository keeps the boundary explicit: source integration is stronger than abstract runtime context, but weaker than autonomous retrieval.
