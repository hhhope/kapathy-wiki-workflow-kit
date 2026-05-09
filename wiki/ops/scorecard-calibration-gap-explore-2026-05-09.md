---
canonical_object: scorecard-calibration-gap
artifact_type: explore-trace
related_objects:
- learning-capture-routing
- public-report-quality-gate
- behavior-replay-gate
- product-capability-and-graph-gap
derived_from:
- .codex/skills/article-learning-capture/references/scorecard.md
- .codex/skills/readme-learning-capture/references/scorecard.md
- .codex/skills/public-report-quality-gate/references/scorecard.md
- wiki/ops/agent-harness-article-learning.md
- wiki/ops/team-knowledge-base-overview-report-gate-review.md
---

# scorecard-calibration-gap / explore-trace

## Trigger

User observed that recent multi-round discussions and article/report outputs
rarely score below 85, which suggests the current gates are too weak or the
requirements are too vague. User asked whether the model should start strict and
only widen later.

## Explore Boundary

This is `$openspec-explore`: thinking and requirement shaping only.

No scorecard, skill, OpenSpec spec, or report gate rule has been changed in this
trace.

## Current Evidence

Current scorecards serve different jobs:

```text
article/readme scorecards
  -> admission: is the source worth deep reading?

public-report scorecard
  -> output gate: is the reader-facing artifact review/sync ready?
```

This distinction is not consistently preserved in live work. A high source
admission score can be mistaken as output quality proof, and a repaired hard gate
can be mistaken as final reader quality.

Observed escape patterns:

```text
1. admission score becomes quality score
2. retrospective score looks like score-first evidence
3. hard gate PASS after repair becomes "good enough" without negative calibration
4. unclear user requirement lets the agent choose a favorable rubric
5. local usefulness receives high points even when verification is weak
6. unknown / not tested sometimes becomes residual risk instead of INVALID
```

Recent local evidence already contains warning signs:

- `route-complex-public-reports-to-reviewer` recorded a false 100/schema-score
  problem.
- `repair-account-wiki-public-drafts` recorded `92 / 100 -> INVALID` because
  hard gate failure must override numeric score.
- `constrain-feishu-image-delivery` was reopened because static skill evidence
  was not enough to claim runtime behavior.
- Feishu image write/read-back passed, but client usability failed because
  image-bearing docs could freeze clients.

## Working Judgment

The problem is not only that the numeric threshold is too low. The deeper
problem is scorecard role confusion:

```text
source admission score != output quality score
schema/rubric completeness != reader quality
read-back/audit proof != client usability
static wording proof != runtime behavior proof
```

## Strict-First Position

Starting strict and widening later is appropriate for this repository, but only
if "strict" means explicit caps and invalid states, not vague taste.

Recommended stance:

```text
default = strict

if requirement unclear:
  cap score or mark INVALID
  ask / preserve ambiguity

if user intentionally relaxes:
  downgrade target label
  e.g. draft-only, exploration-only, candidate-only
  do not keep review-ready / publish-ready label
```

## Candidate Calibration Rules

These are exploration candidates, not implemented rules:

1. If the acceptance target is unclear, no output quality score above 69.
2. If the score is retrospective, it cannot count as score-first admission
   evidence and should be capped or labeled audit-only.
3. If any hard gate is unknown, partial, not tested, or self-assessed without
   evidence, scorecard is `INVALID`.
4. A source score can only justify reading, not report publication.
5. A report score must include at least one negative calibration example or known
   bad sample from the same workflow.
6. Client-impacting delivery claims need client-side proof or must be labeled
   audit-only.
7. User-visible outputs should have two tracks:
   - `draft quality`
   - `publish/review readiness`
8. Scorecards should record the selected target before writing:
   - source learning
   - internal planning
   - review draft
   - Feishu sync
   - public publish

## Open Question

Should the next OpenSpec change modify only `public-report-quality-gate`, or
should it introduce a shared scorecard-calibration contract used by learning,
report, and behavior-replay gates?

## Non-Decisions

- No scoring threshold has been changed.
- No scorecard file has been edited.
- No new OpenSpec change has been created.
