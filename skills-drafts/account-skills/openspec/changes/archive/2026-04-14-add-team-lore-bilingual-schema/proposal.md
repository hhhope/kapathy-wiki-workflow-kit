## Why

The current problem is broader than "the wiki is not bilingual enough."

`team-lore` is missing an explicit knowledge contract for how an agent should work with shared memory.

Right now:

- many pages are readable by humans but not optimized for low-cost agent retrieval
- `current facts` and similar sections are often prose-heavy instead of atomic operating facts
- page boundaries, aliases, applicability, and exclusion signals are weak
- bootstrap can create a valid wiki structure without creating agent-ready retrieval surfaces
- weekly review can promote durable knowledge without checking whether the result is efficient for future agents to load
- bilingual support is unclear because language support was never defined as part of the agent memory contract

This causes a deeper failure mode:

- the wiki may exist
- the pages may be true
- but an arbitrary agent still cannot reliably answer "what should I read, how much should I read, what is stable here, and what is merely explanation"

We need to define `team-lore` from the perspective of how any agent actually works:

1. identify likely relevant pages
2. decide whether a page applies
3. extract a minimal working set of context
4. avoid loading irrelevant prose
5. write new durable knowledge back in the same shape

This must be treated as a TDD-first change.

We should not keep revising the page model by intuition alone. The change needs explicit failing agent-memory scenarios first, then a page/workflow contract that makes those scenarios pass.

## What Changes

This change defines an agent-oriented shared-memory contract for `team-lore`.

Scope:

1. Define an agent-ready page model
   - page sections optimized for retrieval, applicability, exclusion, and minimal context loading
   - distinguish operating facts from long-form rationale

2. Define an agent memory workflow contract
   - what an agent should read first
   - how an agent decides a page is relevant
   - what fields support low-cost context loading
   - what must be present before durable knowledge is considered promotion-ready

3. Update bootstrap expectations
   - starter pages must be agent-ready, not merely non-empty
   - bootstrap completion must mean "retrieval-ready enough for agents to use"

4. Update weekly-review promotion rules
   - promoted durable knowledge must be written in agent-ready form
   - avoid allowing prose-heavy durable pages that future agents cannot efficiently reuse

5. Define language support as a sub-problem of agent usability
   - bilingual support is handled as part of agent retrieval and interpretation, not as a separate translation-only initiative
   - define which fields require bilingual support or aliases for mixed-language agent use

6. Define the first rollout slice
   - limit to the highest-value shared page types and entry pages
   - avoid full historical rewrite

7. Define RED/GREEN evidence before implementation
   - capture failing agent-memory scenarios against the current wiki shape
   - define passing conditions for retrieval, applicability, context loading, and mixed-language support

8. Define the knowledge-plane cooperation rule
   - keep OpenSpec in the process plane
   - treat Lore as the durable semantic truth source
   - treat Graphify as code-topology evidence within the same knowledge plane
   - default mixed questions to Lore first, then Graphify

Out of scope:

- translating the full historical wiki corpus
- redesigning OpenSpec lifecycle ownership
- replacing the wiki taxonomy with a different knowledge system
- broad implementation work outside shared-memory structure and workflow rules

## Capabilities

- `team-lore-agent-memory-contract` - define and enforce the minimum shared-memory contract that allows any agent to retrieve, load, and promote durable knowledge efficiently

## Expected Outcome

After this change:

- "team-lore works for agents" has a concrete meaning for the first rollout slice
- the migrated shared entry pages and highest-value durable pages are shaped for retrieval and context loading, not only human reading
- bootstrap and weekly review reinforce the same agent-ready page model
- mixed-language support reaches a minimum alias-routing contract instead of being left accidental
- Lore and Graphify also have an explicit cooperation model instead of competing as ambiguous retrieval surfaces
- broader historical backfill and fuller bilingual interpretation are left to follow-up changes rather than implied by this change
