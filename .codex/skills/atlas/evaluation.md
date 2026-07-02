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

### Scenario 1: Locked Chapters + Continue

Input shape:

- A report or sharing稿 has confirmed chapter names, section names, talk track,
  evidence boundary, and transition format.
- The user says `继续`, `可以`, or `确认`.

Old failure:

- The agent keeps drafting from memory.
- Confirmed names and section shape are compressed, renamed, or replaced.

Expected Atlas route:

- Atlas emits the Continuation State Gate block.
- Worker route is `public-report-quality-gate` only after anchors are visible.

Expected blocked action:

- Rename locked chapters.
- Merge confirmed sections.
- Drop talk track, transition, or evidence boundary.

Expected output or non-output:

- Output only the next approved section or a narrowed repair target.

Proof boundary:

- This scenario proves continuation state inheritance for report-like artifacts;
  it does not prove visual or source evidence handling.

### Scenario 2: Per-Section Visuals + H5 Continuation

Input shape:

- The user confirmed that every section needs its own visual.
- The current artifact is an H5/share draft or visual report package.
- The user asks to continue implementation or visual repair.

Old failure:

- The agent treats H5 as a visual-only implementation task.
- Approved per-section visuals are collapsed into one generic visual system.

Expected Atlas route:

- Atlas emits state with visual anchors.
- Worker route is `public-report-quality-gate -> visual-agent`.

Expected blocked action:

- Compress per-section visuals into one composite visual.
- Verify layout while ignoring the visual proof task.

Expected output or non-output:

- Output a visual binding table, repair plan, or blocked-action note before
  touching H5 implementation.

Proof boundary:

- This scenario proves route and visual-anchor preservation; it does not prove
  bitmap quality or browser rendering.

### Scenario 3: Incomplete LinkedIn/JD Evidence

Input shape:

- The artifact needs organization capability, talent background, hiring
  direction, or strategic inference from LinkedIn/JD data.
- The profile/JD sample is incomplete, has no historical distribution, or lacks
  a clear sample size.

Old failure:

- The agent overclaims company capability from weak profile/JD evidence.
- Or the agent drops the requested people/JD analysis and replaces it with
  generic strategic commentary.

Expected Atlas route:

- Atlas marks the evidence gap in `Open Gaps`.
- Worker route is `learning-capture` for evidence boundary.

Expected blocked action:

- Claim organization-wide staff composition, tenure structure, background mix,
  or strategic success without sample support.

Expected output or non-output:

- Output source role, sample size, claim strength, and proof boundary before
  drafting the claim.

Proof boundary:

- JD can indicate current hiring firepower and investment direction. It cannot
  by itself prove product adoption or strategic success.

### Scenario 4: Skill Behavior Change After Retro

Input shape:

- A collaboration retro identifies repeated drift.
- The user asks to continue toward a skill or behavior change.

Old failure:

- The agent edits behavior assets directly from conversation state.
- Or the agent jumps into OpenSpec before the Superpowers design/plan route is
  approved.

Expected Atlas route:

- Atlas names the active plan and phase.
- Skill-authoring/TDD guidance is loaded before semantic skill edits.

Expected blocked action:

- Edit unrelated behavior assets.
- Start OpenSpec artifacts when the SS route is still active.
- Claim future runtime behavior without replay evidence.

Expected output or non-output:

- Output the smallest allowed plan block or implement the current checked task
  only.

Proof boundary:

- This proves Atlas respects current route boundaries. It does not make Atlas
  an OpenSpec lifecycle controller.

### Scenario 5: Simple One-Off Task

Input shape:

- The user asks for a direct command result, narrow lookup, small grammar edit,
  or isolated code task.
- No durable learning/report artifact, confirmed anchors, or worker
  collaboration need exists.

Old failure:

- A controller over-applies and emits a heavy state block.

Expected Atlas route:

- No Atlas route.

Expected blocked action:

- Do not force a state block or multi-skill routing.

Expected output or non-output:

- Use the normal direct response or applicable narrow skill.

Proof boundary:

- This scenario proves the non-trigger boundary.

## Residual Risks

- This Task 1 file is evidence only; it does not create runtime behavior.
- Chat-memory reconstruction can still be incomplete. Atlas v1 intentionally
  avoids a persistent state file until replay evidence proves it is necessary.
- Worker skill integration is still pending, so current worker skills do not yet
  preserve Atlas state.
- The repository still has many unrelated dirty files. Atlas implementation
  commits must stage only task-related files.
