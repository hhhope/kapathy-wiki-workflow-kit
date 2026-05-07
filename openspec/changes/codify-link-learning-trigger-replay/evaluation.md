# Evaluation: link learning trigger replay

Date: 2026-05-07

## Scope

Validate that the "next link" behavior is discoverable from repo-visible
artifacts and not only from chat memory.

This is documentation-level behavior replay. It does not claim multi-session
rollout telemetry.

## RED Baseline

Before this change, the repo had the general rule that a bare source inside an
active learning / governance thread should trigger `learning-capture`, but it
did not provide a compact replay matrix that answered the user's exact question:
"If I give you a link next time, what happens?"

| Scenario | Baseline evidence | RED result |
|---|---|---|
| Bare article link inside learning/governance thread | `.codex/skills/learning-capture/SKILL.md` implied the trigger, but `references/routing.md` did not preserve a next-link replay output contract. | PARTIAL |
| WeChat link inside learning/governance thread | `weixin-reader` existed and article routing existed, but no replay matrix tied WeChat source grounding to the next-link behavior. | PARTIAL |
| GitHub/README link with learn/reuse/adapt intent | repo/README routing existed, but the next-link replay answer was not preserved as a strategy anchor. | PARTIAL |
| Raw fetch / news / fact lookup | negative paths existed in the intent gate, but not in a replay matrix beside positive link behavior. | PARTIAL |
| Bare link with no learning context | negative path existed, but future answers still had to reconstruct the boundary from multiple rows. | PARTIAL |

## GREEN Result

| Scenario | Expected route | GREEN evidence | Result |
|---|---|---|---|
| Bare article link inside learning/governance thread | `learning-capture` -> article module -> admission -> score | `.codex/skills/learning-capture/references/routing.md` now has `Link Trigger Replay` with this row. | PASS |
| WeChat link inside learning/governance thread | source grounding through `weixin-reader` or equivalent -> article module -> admission -> score | routing reference now names `mp.weixin.qq.com` and source grounding before scoring. | PASS |
| GitHub/README link with learn/reuse/adapt intent | repo/README module -> admission -> score | routing reference now names GitHub/GitLab repo or README replay behavior. | PASS |
| Raw fetch / news / fact lookup | no learning capture by default; use narrower path | routing reference keeps this as a negative replay row. | PASS |
| Bare link with no learning context | clarify or ordinary lookup/fetch; no durable wiki by default | routing reference keeps this as a negative replay row. | PASS |

## Artifact Citation Check

A future answer can cite:

- `.codex/skills/learning-capture/references/routing.md` -> `Link Trigger Replay`
- `wiki/ops/learning-capture-routing.md` -> `Link Trigger Replay 治理锚点`
- `openspec/changes/codify-link-learning-trigger-replay/specs/learning-capture-routing/spec.md`
  -> `Learning capture SHALL preserve link-trigger replay behavior`

## Boundary Check

| Boundary | Evidence | Result |
|---|---|---|
| Raw fetch, news/fact lookup, unclear bare link, and low-scoring source remain non-durable paths | routing reference negative rows plus wiki governance boundary | PASS |
| No promotion into `AGENTS.md`, spec `SHALL`, skill hard rules, or archive-ready claims without evidence gate | wiki governance boundary plus spec promotion scenario | PASS |
| The change does not edit root/global assets | no root file changes in this change | PASS |

## Residual Risks

- This replay is still documentation-level proof, not automated routing
  telemetry.
- The active thread context still matters; a bare link outside a learning
  context should not be forced into learning capture.
- Historical answers may still have omitted wiki line citations until agents
  use the new replay anchor.
