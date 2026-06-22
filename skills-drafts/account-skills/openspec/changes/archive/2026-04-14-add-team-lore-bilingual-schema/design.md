## Overview

The central issue is not that the wiki is missing some pages or missing some translations.

The central issue is that `team-lore` does not yet define a memory interface that works reliably for any agent.

An agent-oriented memory system needs to support five operations:

1. route - identify likely relevant pages
2. qualify - decide whether a page applies or should be rejected
3. load - extract a small working set of stable facts
4. act - use those facts without confusing rationale for requirements
5. promote - write back new durable knowledge in the same retrievable shape

Today, the wiki is only partially optimized for those operations.

This change also needs to define how Lore should work with Graphify without confusing either system with OpenSpec.

## Findings From Explore

### Confirmed facts

1. The current shared wiki under `/mnt/d/team-lore/wiki` exists and is structurally usable.
2. Many current pages are written as explanation-first prose rather than retrieval-first operating surfaces.
3. Existing fields such as `Summary`, `Current risks`, and `Current facts` are often too coarse for reliable low-cost agent loading.
4. `skills/lore/README.md` is bilingual, which shows language accessibility was considered at the documentation layer.
5. Lore validation currently includes English-query retrieval checks, but that validates routing quality rather than page-model completeness.
6. `lore-bootstrap` guarantees path and starter structure, but not agent-ready page shape.
7. Weekly review guarantees promotion and metrics, but not promotion into a page shape optimized for future agent reuse.
8. Graphify currently generates a code-topology graph, not a durable semantic memory graph.
9. The current graphify install snippet is useful as a reminder, but it does not yet define when Graphify should or should not be used relative to Lore.

### Root cause

The system validates the existence of memory and some retrieval outcomes, but it does not define the shape of memory that an arbitrary agent can reliably operate on.

Bilingual incompleteness is one symptom of this broader missing contract.
Knowledge-layer routing incompleteness is another: Lore and Graphify do not yet have an explicit cooperation model.

## Design Goals

1. Define a page model that is efficient for agent retrieval and context loading.
2. Keep the model small enough that weekly review and bootstrap can enforce it.
3. Treat language support as part of agent usability, not a separate documentation campaign.
4. Roll out incrementally on the highest-value pages.
5. Make success measurable with explicit RED/GREEN agent-memory scenarios before schema rollout.

## Non-Goals

1. Full translation of the entire historical wiki.
2. Complete rewrite of all existing Lore content.
3. Replacing OpenSpec or changing change-lifecycle ownership.
4. Building a new retrieval engine in this change.
5. Turning Graphify into the durable truth source for wiki knowledge.

## Process Plane vs Knowledge Plane

This change should make the layer boundary explicit:

- **OpenSpec** is the process plane
  - change status
  - proposal / design / tasks
  - execution progress truth
- **Lore + Graphify** are the knowledge plane
  - Lore owns durable semantic truth
  - Graphify owns code-topology evidence

OpenSpec is not part of knowledge retrieval.

Graphify is not part of process truth.

Lore remains the truth-bearing memory layer for rules, boundaries, pitfalls, principles, and stable facts.

## Agent Memory Contract

### Core agent questions

Every durable shared page should help an agent answer:

1. What scene does this page apply to?
2. What scene does this page explicitly not apply to?
3. What are the top stable facts I should load first?
4. What are the active watchpoints or risks?
5. Which neighboring pages should I load next only if needed?

If a page cannot answer those quickly, it is not agent-ready even if it is correct.

## Knowledge Plane Routing

Questions in the knowledge plane must be separated by what the agent is trying to learn.

### Lore-first questions

These are questions about:

- which rule applies
- which pitfall or principle fits
- what stable facts should be loaded first
- what boundaries exclude neighboring pages

These should route through Lore pages first.

### Graphify questions

These are questions about:

- code entry points
- function neighbors
- module adjacency
- bridge nodes
- likely structure paths

These should route through Graphify.

### Mixed questions

These are questions that need both:

- durable semantic framing from Lore
- code-topology follow-through from Graphify

For mixed questions, the default route is:

1. Lore first, to identify the scene and stable facts
2. Graphify second, to provide structural evidence inside code

This keeps code adjacency from being mistaken for durable truth.

## TDD Strategy

This change should be validated with agent-memory scenarios before implementation details are finalized.

### RED categories

We need explicit failing examples for at least these categories:

1. `routing-pass but load-fail`
   - the right page is found, but the first screen does not expose minimal usable operating facts

2. `page-boundary ambiguity`
   - an agent cannot tell whether a neighboring page applies or should be rejected

3. `prose-heavy durable promotion`
   - weekly review can append durable knowledge without improving future agent retrieval surfaces

4. `mixed-language routing gap`
   - English or Chinese prompt routing works inconsistently because aliases or summaries are absent

### GREEN conditions

The change should be considered successful only if the same scenarios demonstrate:

1. the correct page is routed
2. the page exposes enough operating facts in the retrieval-first sections
3. the page declares applicability and exclusion clearly enough to avoid false loading
4. promoted durable knowledge lands in reusable retrieval-first shape
5. mixed-language prompts can route and load without terminology loss in the first rollout slice

### Validation dimensions

Validation should be reported separately for:

1. routing quality
2. context-load quality
3. page-boundary clarity
4. durable-promotion shape
5. mixed-language compatibility
6. knowledge-plane routing correctness

Without that separation, we will keep overclaiming "works for agents" based only on routing success.

### Required operating sections

Durable shared pages should converge on a common retrieval-first structure:

1. `Scope`
2. `Applies When`
3. `Not For`
4. `Top Facts`
5. `Watchpoints`
6. `Related Pages`
7. `Notes` or `Rationale`

The first six sections are operating surfaces.
`Notes` or `Rationale` exists for human depth, but it should not dominate the page's first-load utility.

### Fact granularity

`Top Facts` must be atomic enough for agent reuse.

Good:

- one stable operational fact per bullet
- one boundary per bullet
- one known constraint per bullet

Bad:

- large blended paragraphs
- mixed fact + explanation + recommendation in one block
- several unrelated constraints compressed into one narrative sentence

## Language Support

Language support should be modeled as agent compatibility.

### Principle

The bilingual question is not "is every paragraph translated."

It is:

- can an agent using Chinese input route to the right page
- can an agent using English input route to the right page
- can an agent load the minimum stable facts without terminology loss

### Minimum language support

For the first rollout:

1. entry pages must support mixed-language navigation
2. reusable durable pages must expose mixed-language aliases or summaries where terminology differs
3. long-form body text does not need full mirror translation in the first slice unless the page is a top-level entry surface

## Workflow Changes

### Bootstrap

`lore-bootstrap` completion should mean:

- starter pages exist
- starter pages are retrieval-ready
- starter pages include minimum language-support surfaces where required

Bootstrap should not be treated as complete when it only creates prose-capable shells.

### Weekly review

Weekly review should promote durable knowledge into agent-ready shape:

- new durable content must update operating sections, not only append explanation
- if the promoted concept introduces cross-language terminology risk, aliases or summary support must be added
- logs stay local-language until promotion; promotion is the point where durable page structure matters

### Retrieval and validation

Validation must separate three dimensions:

1. routing quality
2. page-model completeness
3. language compatibility

Current evaluation overweights the first and under-specifies the other two.

## Rollout Plan

### Phase 1 - Schema definition

Define the common retrieval-first page model and minimum language-support rules.

Targets:

- `wiki/index.md`
- project `overview.md`
- `domain` / `pitfall` / `principle` page templates

### Phase 2 - Workflow integration

Thread the contract into:

- `lore-bootstrap`
- Lore weekly-review guidance
- validation language and acceptance checks

### Phase 3 - First page migration slice

Upgrade the highest-value existing shared pages:

- `wiki/index.md`
- `projects/account-skills/overview.md`
- `projects/account-team-efficiency/overview.md`
- the most reused shared `principle` / `pitfall` pages

## Risks

1. If the operating sections are too heavy, page upkeep will stall.
2. If the rules are too light, prose-heavy drift will continue.
3. If bilingual support is treated as full translation from day one, rollout will stall.
4. If language support is ignored entirely, mixed-language retrieval will remain fragile even with better structure.

## Acceptance Signals

This change is successful when:

1. the team can explain `team-lore` in terms of how an agent reads and writes memory
2. starter pages are judged by retrieval readiness, not only existence
3. weekly review cannot create new durable pages in prose-only shape
4. the first rollout slice produces pages that are measurably easier to route, load, and reuse
5. the RED scenarios defined for this change have corresponding GREEN evidence

## Archive Boundary

This change is archive-ready only when it is described as a first-slice contract and rollout, not as a full historical completion claim.

Archive claims allowed:

1. retrieval-first page contract is defined and applied to the initial high-value shared pages
2. `lore-bootstrap` and weekly-review guidance are aligned with that contract
3. Lore, Graphify, and OpenSpec routing boundaries are defined and checked
4. fresh-context startup is validated for the first rollout slice
5. mixed-language support is validated only at the minimal alias-routing level

Archive claims not allowed:

1. full historical `team-lore` migration is complete
2. full bilingual content completeness is complete
3. routing/classification is fully automated
4. Graphify indexes wiki semantics or replaces Lore as durable truth
