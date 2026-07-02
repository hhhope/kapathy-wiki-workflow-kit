# Atlas Evaluation

## Scope

This evaluation belongs to the repo-local `atlas` skill implementation plan:

- `docs/superpowers/specs/2026-07-02-atlas-learning-report-collaboration-design.md`
- `docs/superpowers/plans/2026-07-02-atlas-learning-report-collaboration.md`

Atlas is a stateful learning/report collaboration controller. It preserves
confirmed anchors, routes worker skills, and blocks completion claims when the
output has drifted.

## Task 1 Evidence

### Source Spec Decisions Preserved

- Atlas is a controller, not a writer, report worker, source reader, or visual
  worker.
- Atlas scope is stateful learning/report collaboration: reports, H5/share
  drafts, presentations, wiki/Feishu-facing drafts, and multi-round material
  work with confirmed anchors or drift history.
- The control model is B+C:
  - Continuation State Gate before continuing after short approvals.
  - Final Drift Gate before completion claims.
- Atlas v1 does not introduce a persistent state database.
- Atlas does not replace OpenSpec lifecycle gates.
- Atlas does not merge into `writing-method-composer`.
- Atlas does not rewrite H5/report artifacts as part of this skill work.

### Worker Ownership

Atlas owns:

- stateful learning/report collaboration detection
- confirmed anchor read-back
- phase selection
- allowed and blocked action decisions
- worker routing
- final drift gate
- re-anchor decision after drift

Worker skills own:

- `learning-capture`: source role, learning level, evidence strength, source
  grounding, output-use handoff, and evidence blockers.
- `public-report-quality-gate`: reader-facing intent, output shape, report
  quality gates, paragraph drift, judgment ownership, review/publish boundary,
  and Feishu-facing blockers.
- `visual-agent`: visual intent detection, mode choice, visual task
  classification, visual proof binding, visual worker routing, and visual
  verification.
- `material-collaboration-defaults`: material intake defaults and source-first
  processing for dropped meeting notes, reports, attachments, preview HTML, and
  related source files.

## Prior-Art / Common-Rule Dedupe

### Not `writing-method-composer`

`writing-method-composer` decides the writing method contract: artifact type,
main line, proof modules, and source depth. Atlas decides whether already
confirmed anchors can safely continue into the next action. The Stripe failure
was not only missing writing methodology; it was missing state inheritance and
final drift control.

### Not `public-report-quality-gate`

`public-report-quality-gate` owns reader-facing quality and hard gates. It does
not own the cross-turn continuation state that says which section names,
visual decisions, evidence boundaries, and rejected framings are already locked.
Atlas should preserve those anchors before this gate or its child routes act.

### Not `visual-agent`

`visual-agent` owns visual classification and verification. It should not decide
whether a confirmed chapter structure, talk track, LinkedIn/JD evidence boundary,
or approved output shape may be changed. Atlas routes visual work only after the
state block says what visual anchors must be preserved.

### Not `learning-capture`

`learning-capture` owns source learning and evidence boundaries. It should not
be responsible for preserving report/H5 section structure, talk-track flow, or
visual decisions across continuation. Atlas routes evidence blockers to
`learning-capture` when claims need source support.

### Not OpenSpec Router

OpenSpec router owns lifecycle routing and prevents Superpowers/OpenSpec bypass.
Atlas does not create, apply, validate, or archive OpenSpec changes. It controls
learning/report collaboration state inside the Superpowers-native execution
path.

## RED Baseline

The baseline failure is reconstructed from the Stripe AI payment sharing/H5
collaboration:

| Scenario | Old failure |
|---|---|
| Short approval after locked chapters | The agent continued drafting or editing without reading back confirmed chapter names, section names, talk-track structure, or blocked actions. |
| H5 continuation after visual approval | The agent treated the H5 as visual-only and compressed approved per-section visuals into a generic composite structure. |
| LinkedIn/JD evidence gap | The agent alternated between overclaiming organization capability from weak evidence and underusing the requested people/JD analysis. |
| Drift complaint during report production | The agent kept producing new drafts instead of stopping, naming the drift chain, and re-anchoring to the last confirmed structure. |
| Workflow behavior change after retro | The agent moved too early into OpenSpec or skill editing before the Superpowers design/plan gate had been explicitly crossed. |
| Simple one-off task | A heavy controller route would be overkill when there is no durable learning/report artifact, confirmed-anchor state, or worker collaboration need. |

## Pressure Scenarios To Prove Later

The GREEN result is not claimed yet. Later tasks must prove these cases after
`SKILL.md` and references exist:

1. User says `continue` after chapters are locked.
2. User approved per-section visuals before H5 continuation.
3. LinkedIn/JD evidence is incomplete.
4. User asks for skill behavior changes after a retro.
5. User asks a simple one-off task that should not trigger Atlas.

## Residual Risks

- This Task 1 file is evidence only; it does not create runtime behavior.
- Chat-memory reconstruction can still be incomplete. Atlas v1 intentionally
  avoids a persistent state file until replay evidence proves it is necessary.
- Worker skill integration is still pending, so current worker skills do not yet
  preserve Atlas state.
- The repository still has many unrelated dirty files. Atlas implementation
  commits must stage only task-related files.
