# Lore Knowledge Routing Results

Date: 2026-04-13
Branch: `feat/team-lore-bilingual-openspec`

This file records behavior-level routing checks for the current Lore and Graphify contract.

Important clarification:

- "process questions route to OpenSpec" is an agent-routing rule
- it is not a claim that the human user needs a new command to work with the repo
- the purpose is to stop the agent from answering process questions with stale wiki or graph output

## Current usability judgment

The current Lore wiki is still usable.

What changed in this round is not "make the wiki exist."
What changed is:

- make the routing boundary explicit
- keep the wiki as the durable rule-and-boundary layer
- use Graphify only when code topology is actually needed

## Summary

| Case | Expected route | Verdict |
|---|---|---|
| `process` | OpenSpec | Pass |
| `lore` | Lore | Pass |
| `graphify` | Graphify | Pass |
| `mixed` | Lore then Graphify | Pass |

## Limits

- these are representative behavior checks, not a general-purpose classifier benchmark
- Graphify currently covers code topology only; it does not index team-lore wiki semantics
- the current wiki can be used now, but the stronger guarantee is still "Lore first for rules, Graphify when structure is needed"
