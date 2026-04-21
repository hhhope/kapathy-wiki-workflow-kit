## Context

The repository already has a pattern for bounded executable replay:

- disagreement replay harness
- re-anchor replay harness
- readable-view validation checker

This change should reuse that shape instead of inventing a broader policy
engine.

The concrete problem is narrower:

- a `distill` page can mix factual session recap with a candidate governance
  model
- once those two are blended, later readers can mistake a preferred framework
  for a stable decision
- a calibration retro can call this out, but without a replay contract the
  evidence remains narrative only

## Goals / Non-Goals

**Goals**

- Add a minimal executable replay contract for distill calibration
- Keep proof bounded to structural replay evidence
- Make it possible to fail when the calibration record omits key boundary data

**Non-Goals**

- Do not semantically judge whether a governance framework is correct
- Do not rewrite the original distill page automatically
- Do not create a generic checker for every future `distill` page
- Do not claim rollout proof or final governance consensus

## Decisions

### Decision: Validate calibration structure, not distill semantics

The checker should validate whether the replay record preserves the minimum
calibration fields:

- which section(s) are fact recap
- which section(s) are candidate model
- which phrases currently overclaim agreement
- what weaker wording is proposed instead

Alternative considered:
- Try to parse the distill page directly and infer overclaiming.
  - Rejected because that would pretend to semantically understand the prose.

### Decision: Use one record for the 2026-04-21 distill dispute first

The first record should replay the current dispute around
`agents-governance-drift-distill-2026-04-21.md`.

Alternative considered:
- Start with a synthetic record.
  - Rejected because the current repository dispute is already concrete and
    grounded.

### Decision: Keep the pass checks tied to calibration honesty

Required pass checks should prove that the replay record preserves:

- fact/model separation
- explicit overclaim markers
- softer wording candidates
- no claim that replay proof equals governance rollout proof

## Replay Contract

Minimum replay fields:

- `thread_label`
- `distill_page`
- `fact_recap_sections`
- `candidate_model_sections`
- `overclaim_markers`
- `downgraded_wording`
- `red_baseline`
- `green_result`
- `residual_risk`

Required pass checks:

- `fact_model_split_preserved`
- `overclaim_markers_explicit`
- `downgraded_wording_present`
- `candidate_model_not_treated_as_canonical`
- `no_rollout_claim`

## Risks / Trade-offs

- [Risk] The checker may be mistaken for semantic proof.
  - Mitigation: publish proof-boundary language in the harness and validation.
- [Risk] The contract may become too custom to one page.
  - Mitigation: keep it narrow and say explicitly that this is a first replay
    contract for this dispute.
