# Knowledge Routing Results — behavior checks

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This file records manual behavior checks for the routing model introduced in this change.

## Goal

Prove that the new contract is not only wording-level, but also makes sense against representative question types:

1. process question
2. Lore rule or boundary question
3. Graphify structure question
4. mixed question

## Results

| Case | Expected route | Result | Verdict |
|---|---|---|---|
| process status | OpenSpec | `openspec status` answers it directly | Pass |
| Lore usage/rules | Lore | `skills/lore/SKILL.md` and `README.md` answer it directly | Pass |
| code-topology query | Graphify | `graphify query` returns nodes and edges | Pass |
| weekly-review mixed query | Lore then Graphify | Lore provides rule, Graphify provides code structure | Pass |

## Interpretation

- "Process questions route to OpenSpec" is an agent guardrail, not a new burden on the user
- the current Lore wiki remains usable and remains the durable rule-and-boundary layer
- Graphify adds value when the question becomes structural
- mixed questions now have an explicit two-step answer shape instead of an implicit guess

## Limits

- this is still manual scenario evidence
- a future follow-up could automate question classification checks
- the current Graphify graph remains code-focused rather than wiki-semantic
