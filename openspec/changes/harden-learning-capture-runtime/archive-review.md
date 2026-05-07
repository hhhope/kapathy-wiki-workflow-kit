## Archive Review

Date: 2026-05-07

## Scope

Review change `harden-learning-capture-runtime` for archive readiness after
strict TDD replay of the learning-capture behavior assets.

## Artifact Completion

| Artifact | Status | Evidence |
|---|---|---|
| Proposal | PASS | `proposal.md` states runtime trigger, topic anchoring, README scoring, retrospective score, and non-goals. |
| Design | PASS | `design.md` records runtime trigger separation, 75-point threshold, topic anchoring, and static proof boundary. |
| Tasks | PASS | `tasks.md` has all tasks checked with dated evidence comments. |
| Evaluation | PASS with nuance | `evaluation.md` records RED/GREEN evidence and residual risks. Strict replay confirms most RED gaps, while old article threshold already existed in article references. |
| Spec deltas | PASS | Deltas cover learning-capture routing, article-learning capture, and README learning skill behavior. |

## Strict TDD Replay Outcome

| Scenario | RED Replay | GREEN Replay | Archive Judgment |
|---|---|---|---|
| `learning-capture` runtime trigger in repo `AGENTS.md` | PASS: old `AGENTS.md` did not list the trigger. | PASS: current `AGENTS.md` lists external-source learning under High-Frequency Skills. | Ready |
| Batch source intake avoids default deep-read-all | PARTIAL: old article guidance already said score before deep reading, but did not define batch triage in the router. | PASS: current router and pressure scenarios require batch triage first. | Ready |
| Article 75 / 60-74 / below-60 score bands | PARTIAL: old article references already had score bands; the main article skill did not expose the threshold as a hard rule. | PASS: current article skill and router expose the threshold. | Ready |
| Retrospective score boundary | PASS: old guidance did not mark retrospective scores as non-admission evidence. | PASS: current article skill and scorecard mark retrospective scores and exclude them from score-first admission evidence. | Ready |
| Explicit topic anchoring | PASS: old router did not require checking existing wiki topic anchors. | PASS: current router checks topic anchors before durable notes. | Ready |
| Weak topic match path | PASS: old router did not define weak matches as weekly-review candidates. | PASS: current router keeps weak matches as weekly-review candidates. | Ready |
| README/repo admission and scoring | PASS: old README skill lacked admission gate, score-first rule, and 75 threshold. | PASS: current README skill and scorecard define admission, scoring, and score bands. | Ready |

## Evaluation Correction Check

No direct edit to `evaluation.md` is required before archive.

Reason: the RED baseline does not claim the old article system lacked all score
bands. The only article-side RED claims are retrospective-score ambiguity and
missing explicit batch-triage behavior. Both are supported by replay. Archive
readers should not reinterpret this change as the first introduction of the
article 75-point scorecard; the change hardens runtime exposure, retrospective
score handling, batch triage, topic anchoring, and README/repo parity.

## Residual Risks

- Replay remains documentation-level behavior proof, not multi-session rollout
  telemetry.
- Weekly review is a candidate outlet but still not automated.
- Historical learning pages may still contain retrospective scores or weak
  source grounding until reviewed separately.
- Root `~/.codex/AGENTS.md` remains out of scope.

## Archive Decision

PASS. The change is archive-ready after this review.
