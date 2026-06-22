# Minimal Page Contract — team-lore agent memory

This file distills the minimum page contract implied by the RED scenarios.

It is intentionally smaller than a full style guide. Its job is to identify the smallest set of page sections and writing rules that make the RED scenarios tractable.

---

## Contract goal

A durable shared Lore page should let an arbitrary agent do four things cheaply:

1. decide whether the page is relevant
2. decide whether the page is primary or secondary for the current task
3. load a minimal stable fact set
4. know what page to open next only if needed

If a page cannot do those four things, it may still be correct, but it is not agent-ready.

---

## The minimum sections

The RED set implies eight minimum sections for durable shared pages.

### 1. `Scope`

Purpose:

- defines what the page covers at the highest level

Agent question answered:

- "What kind of problem or system slice is this page about?"

### 2. `Applies When`

Purpose:

- lists the task scenes, symptoms, or triggers where this page should be loaded

Agent question answered:

- "Why should I read this page for my current task?"

### 3. `Not For`

Purpose:

- excludes neighboring scenes that are easy to confuse with this page

Agent question answered:

- "When should I reject this page and load another one instead?"

### 4. `Top Facts`

Purpose:

- exposes the 3-5 most important stable operating facts first

Agent question answered:

- "What should I load now without reading the whole page?"

Writing rule:

- one operational fact per bullet
- no blended narrative paragraphs

### 5. `Watchpoints`

Purpose:

- records fragile edges, recurring failure modes, or places where behavior drifts

Agent question answered:

- "What is likely to go wrong even if I understood the main contract?"

### 6. `Load Next`

Purpose:

- names adjacent pages to read only if the current question expands

Agent question answered:

- "What is the next page, and why?"

This section is different from a generic related-links bucket. It should be selective and directional.

### 7. `Aliases`

Purpose:

- exposes cross-language or cross-terminology routing terms that help agents hit the page reliably

Agent question answered:

- "If the prompt uses a different language or synonymous term, should this page still be considered?"

Rule:

- include only routing-relevant aliases
- do not dump keyword spam

### 8. `Notes` or `Rationale`

Purpose:

- keeps longer explanation, origin story, and human-depth context

Agent question answered:

- "If I need deeper explanation, where is it?"

Rule:

- this section must not dominate first-load utility

---

## Writing constraints implied by the RED scenarios

### A. Facts must be atomic

Bad:

- multiple concerns compressed into one bullet
- mixed explanation and constraint in one paragraph

Good:

- one boundary per bullet
- one stable behavior per bullet
- one known compatibility constraint per bullet

### B. Applicability must be explicit

Do not assume a page boundary is obvious from title alone.

Every page should contain enough signals that two different agents can independently justify:

- why this page applies
- why a neighboring page does not apply first

### C. Next-hop guidance must be directional

`Related pitfalls` and `Related principles` are useful but too weak on their own.

At least entry and high-overlap pages need directional navigation such as:

- if your issue is bootstrap completeness, read `pitfalls/bootstrap-entry` next
- if your issue is runtime retrieval, read the runtime domain page instead

### D. Long-form explanation must be demoted

Explanation is still useful, but it cannot occupy the same layer as first-load operating context.

The first screen should answer:

- what this page is for
- what the top facts are
- what it is not for

Only after that should the page expand into rationale.

### E. Mixed-language routing must be explicit where terminology drifts

If a page can be asked for using different Chinese/English terms, it should declare those routing aids explicitly instead of hoping title similarity is enough.

The minimum acceptable surface is:

- `Aliases`

Optional additions for entry or high-traffic pages:

- short bilingual routing summary
- bilingual load-next wording

---

## Page-type implications

### `index`

Needs:

- navigation-first structure
- explicit next-hop guidance
- mixed-language navigation support

### `project overview`

Needs:

- startup-friendly `Top Facts`
- explicit `Load Next`
- enough exclusion guidance to stop the overview from becoming a catch-all page

### `domain`

Needs:

- strong `Applies When` / `Not For`
- compact `Top Facts`
- neighboring-page disambiguation

### `pitfall`

Needs:

- fast diagnostic surface
- top checks or top facts before longer avoidance narrative

### `principle`

Needs:

- clear stable rule
- strong applicability boundary
- evidence kept separate from the rule itself

---

## Language-support sub-contract

Language support is subordinate to the page contract, not separate from it.

The minimal rule is:

- if terminology can diverge across Chinese and English prompts, the page needs routing aids

Routing aids may include:

- aliases
- English summary
- Chinese summary
- bilingual top-level terminology mapping

The first rollout does not require full mirrored translation for every durable page.
It does require enough language support that mixed-language routing and first-load interpretation stop being accidental.

---

## What this contract changes immediately

It changes how we judge page quality.

A page is no longer "good enough" merely because:

- it exists
- it is true
- it links to related pages

A page is good enough only if an agent can:

1. route to it
2. accept or reject it quickly
3. load minimal facts cheaply
4. navigate onward deliberately

---

## Intended use

This contract should drive the next three design steps:

1. update page templates
2. update bootstrap completion semantics
3. update weekly-review promotion rules
