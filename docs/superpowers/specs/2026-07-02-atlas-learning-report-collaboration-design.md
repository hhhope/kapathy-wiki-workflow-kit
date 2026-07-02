# Atlas Learning / Report Collaboration Design

## Route Status

Route: `$superpowers:brainstorming` -> Superpowers design spec.

This document is a brainstorming design artifact. It does not implement Atlas,
does not modify repo-local skills, and does not change OpenSpec lifecycle state.

## 1. Problem

The Stripe AI payment sharing work exposed a repeatable collaboration failure.

The repo already has useful workers and gates:

- `learning-capture` for source learning and evidence strength.
- `public-report-quality-gate` for reader-facing report/H5/share quality.
- `visual-agent` for visual mode, visual routing, and visual verification.
- `material-collaboration-defaults` for source-first material processing.
- `wiki-medical-agent`, `req-agent`, and `openspec-router` as examples of
  controller-style skills.

The missing layer is not another writing-method worker. The missing layer is a
stateful collaboration controller for learning/reporting work.

In the Stripe run, confirmed chapter titles, section structures, speaker notes,
transitions, evidence boundaries, and per-section visuals were repeatedly lost
after the user said "continue", "confirm", or asked for repair. The failure was
not that a reference file was missing. The failure was that confirmed state did
not control the next action.

## 2. Why Not `writing-method-composer`

`writing-method-composer` is still useful, but it solves a different problem.

It answers:

```text
What kind of article/share artifact is this?
What is the mainline?
Which proof modules and writing methods are needed?
Which evidence depth is required?
```

Atlas answers:

```text
What has already been confirmed?
What phase is the collaboration in?
What is allowed in this continuation?
What is blocked?
Which worker skill should run next?
Can the result claim completion, or did it drift?
```

Therefore Atlas should not be merged into `writing-method-composer`, and
`writing-method-composer` should not become a state controller.

## 3. Design Goal

Add a repo-local controller skill named `atlas`.

Display name:

```text
Atlas：学习汇报协作图谱
```

One-line role:

```text
Atlas coordinates stateful learning/report collaborations by preserving
confirmed anchors, routing worker skills, and checking final drift before
completion.
```

Chinese intent:

```text
Atlas 管学习/汇报类多轮协作：守住确认锚点，路由学习、报告和视觉
skill，并在完成前检查是否漂移。
```

## 4. Scope

Atlas applies to learning/reporting collaboration, especially:

- source learning that will shape a report, H5, share draft, speech, wiki output,
  or public-facing artifact;
- multi-turn report, H5, PPT, share, speaking script, visual package, or
  material-processing work;
- tasks with confirmed anchors, user corrections, locked structure, selected
  output shape, evidence boundaries, or drift history;
- continuation after the user has approved, corrected, or rejected a prior
  artifact.

Atlas does not apply to:

- one-off shell commands;
- ordinary code implementation without learning/report output state;
- OpenSpec lifecycle state;
- full-repo governance;
- global agent behavior;
- writing prose, drawing visuals, fetching sources, or publishing artifacts.

## 5. Core Decision

Use B+C:

```text
B = Continuation State Gate
C = Final Drift Gate
```

Atlas should not start with a heavy state machine. It should use a lightweight
state model plus hard continuation/final gates.

This keeps the scope narrow while solving the actual failure:

```text
confirmed anchors existed
  -> continuation skipped read-back
  -> worker skill produced a new shape
  -> final output looked complete but had drifted
```

## 6. Architecture

Atlas is a controller. It routes to workers but does not replace them.

```text
                    User
                     |
                     v
          +----------------------+
          |        Atlas         |
          | 学习汇报协作图谱       |
          +----------------------+
          | - current phase      |
          | - confirmed anchors  |
          | - allowed actions    |
          | - blocked actions    |
          | - open gaps          |
          | - worker routing     |
          | - final drift gate   |
          +----------+-----------+
                     |
        +------------+------------+
        |            |            |
        v            v            v
+---------------+ +----------------+ +--------------+
| learning-     | | public-report- | | visual-agent |
| capture       | | quality-gate   | |              |
| 学习/证据      | | 汇报/表达       | | 视觉/图示     |
+---------------+ +----------------+ +--------------+
        |            |            |
        +------------+------------+
                     |
                     v
          +----------------------+
          | Reader-facing Output |
          | 分享稿 / H5 / 报告     |
          +----------------------+
                     |
                     v
          +----------------------+
          | Final Drift Gate     |
          | 完成前漂移检查         |
          +----------------------+
```

## 7. Trigger Model

Atlas must trigger by situation, not fixed phrases.

Trigger when both are true:

```text
1. The user signals continuation, repair, confirmation, approval, implementation,
   or asks to keep going.
2. The current task is stateful learning/report collaboration.
```

Stateful learning/report collaboration means the thread already has at least one
of:

- confirmed titles, chapters, sections, speaker notes, transitions, or visual
  designs;
- selected output shape such as report, H5, share, PPT, speaking script, or wiki
  output;
- user-owned judgments or corrections;
- evidence boundaries, source roles, or missing-evidence constraints;
- prior drift/reanchor history;
- a named reader-facing target.

Atlas must also trigger before completion claims when a reader-facing or
delivery-sensitive output has confirmed anchors or drift history.

## 8. Continuation State Gate

Before a worker skill continues a stateful learning/report task, Atlas emits a
compact state block.

Minimum shape:

```text
- `Using atlas`
- `Current Object`
- `Current Phase`
- `Confirmed Anchors`
- `Allowed Actions`
- `Blocked Actions`
- `Open Gaps`
- `Worker Route`
- `Next Output`
```

Example:

```text
- `Using atlas`
- `Current Object`: Stripe AI payment sharing H5
- `Current Phase`: visual_binding
- `Confirmed Anchors`: chapter 1-3 locked; chapter 7 has five battle lines;
  each section needs its own visual
- `Allowed Actions`: repair chapter 7 visual mapping
- `Blocked Actions`: rename chapters; merge sections; compress visuals into one
  overview; change the mainline
- `Open Gaps`: market/regulation timeline still needs source verification
- `Worker Route`: public-report-quality-gate -> visual-agent
- `Next Output`: chapter 7 visual re-anchor table only
```

If the state block exposes a blocker, Atlas stops and asks for the missing
confirmation or returns a repair target. It must not continue into drafting,
H5 implementation, visual generation, or skill edits.

## 9. Lightweight Phase Model

Atlas starts with a small phase set:

```text
intent_calibration
structure_lock
evidence_mapping
drafting
visual_binding
implementation
review_or_reanchor
```

These phases are not a full workflow engine. They are a shared vocabulary for
allowed/blocked action decisions.

If a task does not fit these phases, Atlas should use:

```text
phase: unclear
allowed_actions: clarify or re-anchor only
blocked_actions: produce or edit delivery artifact
```

## 10. Confirmed Anchors

Confirmed anchors are user-approved or user-corrected facts that cannot be
silently changed.

Anchor categories:

```text
content_anchor       = mainline, thesis, argument, user-owned judgment
structure_anchor     = chapter, section, subsection, order, time allocation
voice_anchor         = speaker-note style, professional drama, wording level
evidence_anchor      = source role, evidence strength, missing evidence, boundary
visual_anchor        = per-section visual, visual form, visual proof task
output_shape_anchor  = report, H5, share, PPT, wiki, Feishu, markdown
boundary_anchor      = allowed action, blocked action, non-goal
```

Atlas does not need to persist a database in v1. It can recover anchors from the
current chat and repo-visible records. Future versions may add structured state
files if replay proves chat recovery is insufficient.

## 11. Acceptance Scorecard

Atlas owns a collaboration scorecard registry, not a fixed 11-item checklist.

The Stripe retro produced the first signal set, but future work will add more.
Therefore scorecards must use progressive disclosure:

```text
Core Gates
  - state inheritance
  - execution boundary
  - final consistency
  - generic vs custom boundary

Reader Artifact Gates
  - mainline clarity
  - section integrity
  - narrative progression
  - professional drama

Evidence Gates
  - evidence duty
  - claim strength
  - method fit

Visual Gates
  - visual proof binding
  - per-section visual integrity

Boundary Gates
  - hard failure
  - user-owned judgment
```

Atlas loads only the relevant gate families.

Examples:

```text
simple material cleanup       -> Core only
complex report                -> Core + Reader + Evidence
H5/share visual draft                   -> Core + Reader + Visual
source-heavy strategy report            -> Core + Reader + Evidence + Final Drift
learning/report workflow behavior talk  -> Core + Boundary, not Reader
```

## 12. Final Drift Gate

Before claiming completion for a stateful learning/report artifact, Atlas runs a
final drift check.

Minimum checks:

```text
- Did any confirmed anchor disappear?
- Did chapter/section count or names change without approval?
- Did speaker notes, transitions, or evidence boundaries get compressed away?
- Did a load-bearing claim lack the required evidence status?
- Did visual output merge per-section visuals into a composite without approval?
- Did the output shape change from the selected shape?
- Did a custom Stripe-specific rule get promoted into a generic rule?
- Did a generic collaboration rule get omitted from the candidate governance
  layer?
```

Failure behavior:

```text
Do not claim done.
Report the failed gate.
Return to the relevant phase.
Name the smallest repair target.
```

## 13. Worker Ownership

Atlas owns:

- stateful learning/report detection;
- phase selection;
- confirmed anchor read-back;
- allowed/blocked action decisions;
- worker routing;
- final drift gate;
- re-anchor decision when drift is found.

Atlas does not own:

- source reading or evidence scoring owned by `learning-capture`;
- reader-facing report quality owned by `public-report-quality-gate`;
- visual mode and visual verification owned by `visual-agent`;
- material intake defaults owned by `material-collaboration-defaults`;
- OpenSpec lifecycle owned by repo OpenSpec skills;
- final prose style owned by future writing workers or the current drafting
  context.

## 14. Skill Collaboration Rules

Atlas should be the first skill for stateful learning/report continuation.

Worker skills must preserve Atlas state when routed by Atlas:

```text
Atlas -> learning-capture
  learning-capture handles source roles, levels, evidence strength, and output
  use. It must not widen the allowed action.

Atlas -> public-report-quality-gate
  public-report-quality-gate handles Article Intent Contract, Reference Output
  Shape, paragraph drift, judgment ownership, and publish/review boundaries. It
  must not drop confirmed anchors.

Atlas -> visual-agent
  visual-agent handles mode choice, task classification, visual proof binding,
  output verification, and visual worker routing. It must not merge per-section
  visuals unless Atlas state or the user explicitly allows it.
```

If a worker identifies a new blocker, the route returns to Atlas:

```text
worker blocker -> Atlas re-anchor -> user confirmation or narrowed next output
```

## 15. First Implementation Scope

Future implementation should create a compact repo-local skill:

```text
.codex/skills/atlas/
  SKILL.md
  references/
    continuation-state-gate.md
    scorecard-registry.md
    final-drift-gate.md
    worker-routing.md
    replay-scenarios.md
  evaluation.md
```

Expected skill changes after OpenSpec approval:

```text
add .codex/skills/atlas/*

update .codex/skills/learning-capture/SKILL.md
  - recognize Atlas-routed learning/report collaboration
  - preserve Atlas allowed/blocked actions
  - return evidence blockers to Atlas

update .codex/skills/public-report-quality-gate/SKILL.md
  - preserve Atlas confirmed anchors
  - call out Atlas final drift failures for stateful outputs

update .codex/skills/visual-agent/SKILL.md
  - preserve Atlas visual anchors
  - reject per-section visual compression without approval

optionally update .codex/skills/material-collaboration-defaults/SKILL.md
  - route rich material/report continuation through Atlas when confirmed
    anchors or drift history exist
```

## 16. Explicit Non-Goals

Do not implement these in the first Atlas change:

- global AGENTS changes;
- full skill governance knowledge base;
- code task state machine;
- OpenSpec lifecycle replacement;
- `writing-method-composer`;
- persistent state database;
- broad rewrite of `learning-capture`, `public-report-quality-gate`, or
  `visual-agent`;
- automatic Feishu sync or publish behavior.

## 17. Checker And Evaluation Expectations

Reference text alone is not enough. Future implementation must include replay
evidence.

Minimum evaluation scenarios:

```text
1. User says "continue" after chapters are locked.
   RED: agent drafts or edits without reading anchors.
   GREEN: Atlas emits state block and blocks chapter rename/section merge.

2. User approved per-section visuals.
   RED: H5 implementation compresses sections into one composite visual.
   GREEN: Atlas/visual-agent route fails final drift and returns to
   visual_binding.

3. LinkedIn/JD evidence is incomplete.
   RED: output claims organization capability from weak samples.
   GREEN: Atlas routes to learning-capture evidence blocker or marks
   proof-boundary.

4. User asks for skill behavior changes after a retro.
   RED: agent edits skill directly from conversation.
   GREEN: Atlas marks behavior asset as out of direct scope and requires
   OpenSpec / skill authoring gate.

5. Simple one-off task.
   RED: Atlas over-applies heavy state block to a trivial command.
   GREEN: Atlas does not trigger because there is no stateful collaboration.
```

Minimum acceptance criteria:

- Atlas has a compact `SKILL.md`.
- Atlas route block includes current object, phase, anchors, allowed actions,
  blocked actions, worker route, and next output.
- Atlas does not duplicate worker skill bodies.
- Worker skills preserve Atlas state when routed by Atlas.
- Final Drift Gate prevents completion claims after anchor loss.
- Evaluation includes RED/GREEN replay from the Stripe H5 failure.

## 18. Migration Path

Use staged rollout:

```text
Stage 0: This design only.
Stage 1: OpenSpec proposal for Atlas.
Stage 2: Add Atlas skill and evaluation with replay.
Stage 3: Minimal worker skill integration.
Stage 4: Use Stripe sharing/H5 as acceptance replay.
Stage 5: Decide whether writing-method-composer is still needed separately.
```

Do not move to Stage 2 from this design document alone.

## 19. Self-Review Notes

- Scope is limited to learning/report stateful collaboration.
- Atlas is a controller, not a worker.
- The design uses B+C: Continuation State Gate plus Final Drift Gate.
- The design does not depend on fixed trigger phrases.
- The design preserves `learning-capture`, `public-report-quality-gate`, and
  `visual-agent` ownership.
- The first implementation scope is explicit and excludes global governance.
- Replay evidence is required before future runtime behavior claims.
