# Baseline Results — current team-lore pages

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This baseline scores the current shared wiki pages against the RED scenario set.

Scoring:

- `Pass` = scenario dimension is satisfied well enough for first rollout
- `Partial` = useful but inconsistent
- `Fail` = not good enough for the agent-memory contract

## Scenario matrix

| Scenario | Primary pages | Hit-rate | First-load readability | Boundary clarity | Mixed-language compatibility | Verdict |
|---|---|---|---|---|---|---|
| RED-01 | platform-admin-auth-and-team-scope + pitfall | Pass | Fail | Partial | Partial | Fail |
| RED-02 | two domains + pitfall | Pass | Partial | Fail | n/a | Fail |
| RED-03 | account-team-efficiency overview | Pass | Fail | Fail | n/a | Fail |
| RED-04 | promoted durable page in general | Pass | Fail | Partial | n/a | Fail |
| RED-05 | platform-admin-auth-and-team-scope | Pass | Partial | n/a | Fail | Fail |
| RED-06 | index + account-skills overview | Pass | Fail | Fail | Partial | Fail |
| RED-07 | bootstrap-entry pitfall style | Pass | Partial | Partial | n/a | Partial |
| RED-08 | completion claim evidence set | Partial | Fail | Fail | Fail | Fail |

## Totals

| Dimension | Result |
|---|---|
| Hit-rate | `7 Pass / 1 Partial / 0 Fail` |
| First-load readability | `0 Pass / 3 Partial / 5 Fail` |
| Boundary clarity | `0 Pass / 3 Partial / 5 Fail` |
| Mixed-language compatibility | `0 Pass / 2 Partial / 2 Fail` |

## Interpretation

### What the current pages already do well

- the expected page can usually still be found
- the wiki taxonomy is not broken
- the pages are generally true and useful for a human reader

### Why that is still RED

- first-load readability is the weakest dimension
- neighboring-page rejection is too inference-heavy
- mixed-language support is accidental rather than contractual
- current evidence can justify "the wiki exists and routing can work" but not "the wiki is agent-ready"

## Self-justification notes

The current pages are not being marked down for lacking information.
They are being marked down because the information is not packaged in a way that an arbitrary agent can load cheaply and consistently.
