## Context

Recent workflow disputes in this repository started from visible symptoms such as:

- missing ADR updates
- arguments not landing in `wiki/ops`
- TDD not catching workflow behavior drift

But the exploration showed those were downstream symptoms, not the main problem.

The real upstream problem is that the repository does not yet have a method for managing disagreement as goal-calibration data. Without that method, the system repeatedly compresses disagreements too early:

- into governance conclusions
- into route-level explanations
- into cleaner abstractions that still lose process

The user's core project is to co-build a self-evolving agent in a space where there is no stable industry playbook yet. In that setting, disagreement is not just friction. It is one of the highest-value signals for target recalibration.

## Goals / Non-Goals

**Goals**

- Define disagreement management as an upstream workflow method, not a downstream artifact patch.
- Preserve the movement of disagreement before naming or promoting it.
- Make explicit which minimum raw material must survive any interpretation step.
- Define the states that prevent fake clarity and premature naming.
- Define how disagreement management relates to later `wiki/ops`, `ADR`, spec, skill, and archive-review actions.

**Non-Goals**

- Do not yet implement the final wiki page, AGENTS wording, or ADR promotion rule.
- Do not yet add runtime automation triggers.
- Do not treat this change as proof that rollout behavior is solved.
- Do not collapse all disagreement into one new universal template.

## Decisions

### Decision: Treat disagreement as calibration material before conclusion material

The repository should first preserve the disagreement as active calibration material before trying to convert it into conclusions.

Alternative considered:
- Continue treating disagreement as a source for better governance summaries.
  - Rejected because it starts from the wrong preservation target and reproduces premature compression.

### Decision: Preserve a minimum raw material package before summary or promotion

Before the repository summarizes, names, or promotes a disagreement, it should preserve a minimum raw package:

- rejected framing
- correction pressure
- redirection moment
- current clarity state
- protected target, if visible

Alternative considered:
- Let operators summarize freely as long as they mention the conclusion and next step.
  - Rejected because that loses the disagreement movement the method is meant to protect.

### Decision: Add explicit anti-compression states

The method should formally preserve two kinds of "not yet" states:

- `I haven't seen it clearly yet`
- `We should not name the pattern yet`

Alternative considered:
- Allow the operator to infer uncertainty implicitly from surrounding prose.
  - Rejected because the repository repeatedly over-rewarded early abstraction unless uncertainty was explicit.

### Decision: Positive naming requires an evolution threshold

The first positive name is only valid when it can explain the movement of the disagreement, not merely summarize the endpoint.

Minimum bar:

1. the rejected object has stabilized
2. redirection has occurred
3. the proposed name explains the evolution, not only the result

Alternative considered:
- Allow naming once the conversation sounds calmer or the user stops objecting.
  - Rejected because that rewards false closure.

### Decision: The method follows the disagreement, not the other way around

Method language is a mirror, not a filter. If the framework and the disagreement conflict, the disagreement wins and the framework weakens.

Alternative considered:
- Use a strong fixed method template to normalize every disagreement thread.
  - Rejected because it would recreate the same compression problem at a higher abstraction level.

## Minimal Method Shape

The upstream method should preserve, in order:

1. raw correction pressure
2. rejected framing
3. redirection
4. unclear state, if still present
5. first positive naming only after the threshold is met
6. later promotion into the lowest correct durable layer

The method should recognize that the disagreement may be doing deeper goal protection even before the deeper goal can be named confidently.

## Downstream Boundary

This method is upstream from the repository's existing durable layers.

- `wiki/ops retro`
  - likely first durable landing zone once the disagreement has enough shape to preserve repo-visibly
- `ADR`
  - later stable-decision layer when the disagreement has finished enough calibration work and produced a durable decision
- OpenSpec specs
  - formal requirement layer for repo-default workflow behavior after the method is stable enough to formalize
- repo-local skills
  - executable behavior layer after the method is stable enough to route and enforce

The repository should not skip the method layer and jump directly from live disagreement to any of those containers.

## Pressure-Test Plan

This method should be validated against at least two disagreement types:

1. a governance-shaped disagreement
2. a meta disagreement where the method itself risks becoming the compressor

The method should pass only if it preserves more calibration value than an earlier compressed framing on the same input.

## Risks / Trade-offs

- [Risk] The method could become too concept-heavy and drift away from live disagreement. -> Mitigation: preserve the minimum raw material package first and explicitly prefer material over framework.
- [Risk] Operators may still name patterns too early. -> Mitigation: formalize the positive-naming threshold and the explicit anti-compression states.
- [Risk] The repository could treat this change as rollout proof. -> Mitigation: keep pressure-test and RED/GREEN evidence explicit and separate from rollout claims.
