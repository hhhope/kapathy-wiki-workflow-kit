# Lore Knowledge Plane Results

Date: 2026-04-13
Branch: `feat/team-lore-bilingual-openspec`

This file records RED/GREEN evidence for defining how Lore should work with Graphify without collapsing OpenSpec into the same layer.

## RED — Before knowledge-plane update

Observed gaps:

- `skills/lore/SKILL.md` explained Lore versus OpenSpec, but did not explain how Lore should cooperate with Graphify
- the current `AGENTS.md` graphify install snippet treated graphify as a generic pre-search hint instead of a bounded code-topology layer
- there was no explicit rule for telling apart:
  - process questions
  - durable rule or boundary questions
  - code-topology questions
  - mixed questions that need both Lore and Graphify
- this left a real failure mode where an agent could:
  - use Graphify too early for a rule question
  - skip Graphify for a structure question
  - confuse code adjacency with durable knowledge truth

Why this was still RED:

- OpenSpec, Lore, and Graphify did not yet have a complete routing model across process memory and knowledge memory
- Lore had a retrieval-first page contract, but not a clear contract for when Graphify should or should not be consulted
- Graphify had generated a code graph, but its output did not explain whether it was a truth source, a routing helper, or only a structural evidence layer

## GREEN — After knowledge-plane update

The updated contract should make these decisions explicit:

- OpenSpec stays in the process plane and is not part of knowledge retrieval
- Lore and Graphify belong to the same knowledge plane, but with different jobs
- Lore owns durable semantic truth:
  - rules
  - boundaries
  - pitfalls
  - principles
  - stable top facts
- Graphify owns code-topology evidence:
  - code entry points
  - function and module neighbors
  - bridge nodes
  - likely structure paths
- mixed questions should default to:
  - Lore first for scene and stable facts
  - Graphify second for code structure evidence

## Verification

Manual checks after the update should confirm:

- `skills/lore/SKILL.md` distinguishes process-plane questions from knowledge-plane questions
- `skills/lore/SKILL.md` distinguishes Lore duties from Graphify duties inside the knowledge plane
- `skills/lore/README.md` explains the same split in user-facing terms
- the active OpenSpec change records:
  - OpenSpec as process memory
  - Lore + Graphify as knowledge memory
  - mixed-question routing as Lore-first then Graphify
- the installed `AGENTS.md` graphify section no longer implies that every architecture or codebase question should consult Graphify before Lore routing

## Limits

- this validates routing and documentation contract, not runtime auto-classification
- this does not require Graphify to index wiki pages in v1
- this does not yet make Graphify the primary entry surface for knowledge retrieval
