# Fresh Context Results — first rollout slice

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This file evaluates whether the draft migration slice still works when an agent starts from fresh context.

Assumption:

- no prior session memory
- no hidden knowledge from earlier turns
- the agent starts from index or project overview only

The question is not "can a smart human infer the right page?"
The question is "can a fresh agent find a workable path without depending on conversational carry-over?"

## Evaluation rule

For each scenario:

- start from the smallest plausible entry surface
- count the pages needed before the likely correct next page becomes clear
- judge whether the path is deterministic enough for a fresh agent

Scoring:

- `Pass` = fresh agent can route with low ambiguity
- `Partial` = route is workable but still depends on some interpretation
- `Fail` = route still depends too heavily on prior context or luck

## Scenario matrix

| Scenario | Entry page | Pages needed | Fresh-context routing | Notes |
|---|---|---:|---|---|
| bootstrap vs runtime lore | draft `wiki/index.md` | `2` | Pass | `Load Next` in index points to `account-skills/overview`, which then points onward to governance-installation |
| start work in account-team-efficiency | draft `wiki/index.md` | `2` | Pass | index -> project overview is explicit and project overview exposes stable startup facts |
| platform-admin wrong-team empty state | draft `projects/account-team-efficiency/overview.md` | `2` | Pass | overview -> pitfall or auth/team-scope domain is directional rather than implied |
| platform-admin team-selection rule | draft `projects/account-team-efficiency/overview.md` | `2` | Pass | overview -> principle is explicit, no need to mine unrelated sections first |
| admin-scope drift diagnosis | draft `pitfalls/admin-scope-ui-backend-drift.md` | `1` | Pass | `Top Checks` make the first diagnostic move visible without prior context |
| account-skills repo startup | draft `wiki/index.md` | `2` | Pass | index -> account-skills overview yields clear startup context and next hops |
| mixed-language route on admin rule | draft `wiki/index.md` or principle draft | `2` | Partial | aliases improve routing, but first-load interpretation still depends on English-first body text |

## Interpretation

### What this proves

- the draft migration slice is not relying on chat carry-over to make sense
- entry pages now carry enough navigation intent that a fresh agent can usually reach the right page in `1-2` hops
- the startup path is becoming deterministic rather than conversational

### What it does not prove

- it does not prove the entire historical `team-lore` corpus is fresh-context safe
- it does not prove mixed-language first-load interpretation is fully solved
- it does not replace real migration of the underlying team-lore pages

## Self-justification

This is why the current design direction is defensible:

1. It improves the weakest baseline property for arbitrary agents: first-use clarity after context reset.
2. It reduces dependence on prior chat memory by pushing next-hop intent into the page itself.
3. It still keeps language support honest by leaving the mixed-language case at `Partial` instead of claiming full completion.
