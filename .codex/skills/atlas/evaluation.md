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

## GREEN Result

The GREEN result is based on local artifact inspection after adding
`SKILL.md`, references, and minimal worker integration.

### Scenario 1: Locked Chapters + Continue

Expected Atlas state block:

- `Current Object`: the active report or sharing draft
- `Current Phase`: `structure_lock` or the smallest fitting phase
- `Confirmed Anchors`: locked chapter and section names, talk-track shape,
  evidence boundary, and transition format
- `Blocked Actions`: rename, merge, reorder, or compress confirmed structure

Expected worker route:

- `public-report-quality-gate`

Expected blocker or allowed output:

- allowed output is only the next approved section or repair target
- blocked output is a new outline or compressed summary

Proof boundary:

- This proves the route contract exists in Atlas files. It is local replay
  evidence, not proof from a future live session.

### Scenario 2: Per-Section Visuals + H5 Continuation

Expected Atlas state block:

- `Current Phase`: `visual_binding`
- `Confirmed Anchors`: per-section visual decisions and visual proof tasks
- `Blocked Actions`: generic visual package or one composite visual unless
  approved

Expected worker route:

- `public-report-quality-gate -> visual-agent`

Expected blocker or allowed output:

- allowed output is a visual binding table, repair plan, or narrow H5 visual
  fix
- blocked output is direct H5 implementation that compresses approved visuals

Proof boundary:

- This proves skill wording and worker integration. It does not prove browser
  screenshots, bitmap generation, or final H5 quality.

### Scenario 3: Incomplete LinkedIn/JD Evidence

Expected Atlas state block:

- `Open Gaps`: sample size, profile/JD source role, historical distribution, or
  proof-boundary gap
- `Blocked Actions`: broad organization or strategy claims from weak samples

Expected worker route:

- `learning-capture`

Expected blocker or allowed output:

- allowed output states source role, claim strength, and proof boundary
- blocked output claims organization-wide capability, tenure structure, or
  strategic success without support

Proof boundary:

- This proves the evidence-boundary wording exists. It does not create or verify
  a LinkedIn/JD dataset.

### Scenario 4: Skill Behavior Change After Retro

Expected Atlas state block:

- `Current Object`: active skill or behavior asset
- `Current Phase`: `implementation`, `review_or_reanchor`, or `unclear`
- `Blocked Actions`: unrelated behavior edits, OpenSpec route when SS is active,
  or runtime claims without replay evidence

Expected worker route:

- skill-authoring and TDD gates before semantic skill edits

Expected blocker or allowed output:

- allowed output is the current checked plan task only
- blocked output is direct governance expansion from conversation state

Proof boundary:

- This proves Atlas references the route boundary. It does not replace repo
  OpenSpec governance.

### Scenario 5: Simple One-Off Task

Expected Atlas state block:

- no Atlas state block

Expected worker route:

- no Atlas route; use the normal direct or narrow skill path

Expected blocker or allowed output:

- allowed output is the direct answer or command result
- blocked output is heavy state routing without a durable artifact

Proof boundary:

- This proves the non-trigger rule is documented. Live routing still depends on
  future sessions loading the skill correctly.

## Command Results

- `rg -n "Atlas|Final Drift|confirmed anchors|visual anchors|evidence blocker"
  ...`: passed; required route markers appear in Atlas files and worker skill
  integrations.
- `git diff --check -- .codex/skills/atlas ...`: passed.
- `python3 /home/yan/.codex/skills/.system/skill-creator/scripts/quick_validate.py
  .codex/skills/atlas`: passed with `Skill is valid!`.
- `python3 scripts/check_behavior_assets.py`: failed because of unrelated
  existing OpenSpec evaluation issues in
  `openspec/changes/enforce-named-skill-gate`,
  `openspec/changes/initialize-llm-wiki-seed-repo`, and
  `openspec/changes/realign-stripe-h5-redesign-sections`. No Atlas-specific
  failure was reported in the observed output.

## Residual Risks

- This evaluation is local replay evidence; it does not prove future live
  sessions will always load or apply Atlas correctly.
- Chat-memory reconstruction can still be incomplete. Atlas v1 intentionally
  avoids a persistent state file until replay evidence proves it is necessary.
- Worker skill integration is minimal. It preserves Atlas routing boundaries but
  does not prove future live sessions will always route correctly.
- The repository still has many unrelated dirty files. Atlas implementation
  commits must stage only task-related files.
