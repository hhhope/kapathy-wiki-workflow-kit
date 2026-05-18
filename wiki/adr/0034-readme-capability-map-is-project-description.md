---
layer: adr
domain: none
canonical_object: readme-capability-map-boundary
artifact_type: adr
formalizes:
  - readme-capability-map-boundary
derived_from:
  - wiki-runtime-layer-boundary
  - brainstorming-drift-wiki-trace
  - openspec/changes/document-readme-capability-map-boundary/design.md
---

# ADR-0034 README Capability Map Is Project Description

## Status

Accepted

## Context

The repository README is a public orientation artifact. During the 2026-05-14
Obsidian graph and MOC projection discussion, the user asked to describe the
whole project's layered capability map in README before continuing runtime
work.

The request was twice misread:

- first as a request to create a separate runtime-readable capability-map
  artifact outside README
- then as a possible runtime first-read contract

Both readings changed the object of the task. The user clarified that README is
project description, and the requested work is to describe the project's
capabilities and layers there.

## Decision

README may describe the repository capability map, but README is not runtime
authority.

- README may summarize wiki layers, capabilities, runtime surfaces, and current
  or planned projection boundaries.
- README should point readers to durable owners such as OpenSpec, ADR, skills,
  command docs, wiki ops traces, and generated status artifacts.
- README does not own runtime behavior, routing contracts, repair execution,
  projection generation, archive state, or OpenSpec lifecycle.
- README descriptions of future work, such as Obsidian MOC projection, must not
  be treated as proof that the capability already exists.

## Consequences

- Updating README can improve orientation without changing runtime behavior.
- Future agents must not infer permission to execute status, graph, apply,
  react, eval, or MOC work from README alone.
- Runtime or workflow changes still require their proper OpenSpec and
  implementation evidence.
- Stable behavior boundaries discovered while editing README still belong in
  ADR or OpenSpec, not only in README prose.
