# Knowledge Plane Results — Lore and Graphify

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This file records RED/GREEN evidence for defining how Lore and Graphify should cooperate inside the knowledge plane without pulling OpenSpec into the same retrieval layer.

## RED — Before routing update

Observed gaps:

- the active change defined a retrieval-first Lore contract, but did not define how Graphify fits beside Lore
- OpenSpec, Lore, and Graphify could still be misread as three competing retrieval surfaces
- the graphify install snippet in `AGENTS.md` encouraged graph-first reading for broad architecture questions without distinguishing:
  - process questions
  - durable rule and boundary questions
  - pure code-topology questions
  - mixed questions that need both Lore and Graphify

Why this was still RED:

- an agent could use Graphify too early for a rule question
- an agent could ignore Graphify when the real blocker was code structure
- code adjacency could be mistaken for durable truth

## GREEN — After routing update

The updated contract now states:

- OpenSpec is the process plane
- Lore and Graphify belong to the knowledge plane
- Lore owns durable semantic truth:
  - rules
  - boundaries
  - pitfalls
  - principles
  - stable facts
- Graphify owns code-topology evidence:
  - entry points
  - node neighbors
  - bridge nodes
  - likely structure paths
- mixed questions default to:
  1. Lore first
  2. Graphify second

## Verification

Manual checks:

- `skills/lore/SKILL.md` now distinguishes process-plane questions from knowledge-plane questions
- `skills/lore/SKILL.md` now defines Lore duties versus Graphify duties in the knowledge plane
- `skills/lore/README.md` explains the same split in user-facing terms
- `proposal.md`, `design.md`, and `spec.md` now all describe the same process-plane versus knowledge-plane split
- the installed `AGENTS.md` graphify section now says:
  - OpenSpec for process
  - Lore first for durable rules and boundaries
  - Graphify for code-topology questions
  - Lore first then Graphify for mixed questions

## Limits

- this is routing-contract evidence, not runtime automatic classification
- Graphify still indexes code topology rather than team-lore wiki semantics
- this does not make Graphify the primary entry surface for all knowledge questions
