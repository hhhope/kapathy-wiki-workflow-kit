# Atlas Learning Report Collaboration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repo-local `atlas` controller for stateful learning/report
collaboration so confirmed anchors, evidence boundaries, and visual decisions
survive short-approval continuation and worker-skill handoff.

**Architecture:** Keep Superpowers-native execution. Atlas is a compact
controller skill with reference files and replay evidence. It routes existing
worker skills instead of replacing them. It adds B+C control: Continuation State
Gate before continuing, and Final Drift Gate before completion claims.

**Tech Stack:** Markdown behavior assets, repo-local skills, behavior-asset
checker, local pressure scenarios, existing Superpowers design spec.

**Source Spec:** `docs/superpowers/specs/2026-07-02-atlas-learning-report-collaboration-design.md`

---

## Route Boundary

This plan is the Superpowers implementation plan. It does not create or depend
on a new OpenSpec change in this step.

Do not modify `openspec/changes/*` while executing this plan unless the user
explicitly reopens the OpenSpec route.

Before semantic skill edits, still obey repo skill-authoring gates:

- load the relevant skill-authoring / TDD guidance required by repo rules
- include RED baseline, GREEN result, and residual risk evidence
- run `scripts/check_behavior_assets.py`

---

## File Structure

Create:

- `.codex/skills/atlas/SKILL.md`
- `.codex/skills/atlas/references/continuation-state-gate.md`
- `.codex/skills/atlas/references/scorecard-registry.md`
- `.codex/skills/atlas/references/worker-routing.md`
- `.codex/skills/atlas/references/final-drift-gate.md`
- `.codex/skills/atlas/references/replay-scenarios.md`
- `.codex/skills/atlas/evaluation.md`

Modify:

- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/public-report-quality-gate/SKILL.md`
- `.codex/skills/visual-agent/SKILL.md`
- optionally `.codex/skills/material-collaboration-defaults/SKILL.md`

Do not modify in this plan:

- global `AGENTS.md`
- repo OpenSpec lifecycle skills
- `writing-method-composer`
- H5/report artifacts such as `wiki/reports/*`
- Stripe sharing稿正文
- Feishu publish/sync behavior
- persistent state files or databases

---

## Acceptance Spec

Atlas passes only if these behaviors are true:

1. Short approvals do not create unbounded continuation.
   - Given a stateful learning/report artifact with confirmed anchors
   - When the user says `继续`, `可以`, `确认`, `做吧`, or `修吧`
   - Then Atlas emits a compact state block before continuing
   - And it states current object, phase, anchors, allowed actions, blocked
     actions, worker route, and next output.

2. Confirmed anchors cannot be silently rewritten.
   - Given locked chapter names, section names, talk-track structure, evidence
     boundaries, or visual decisions
   - When a worker skill is routed
   - Then the worker must preserve the anchors or return a blocker.

3. Visual implementation cannot compress approved per-section visuals.
   - Given the user confirmed that every section needs its own visual
   - When H5/visual work continues
   - Then Atlas + visual-agent block one generic composite visual unless the
     user approves the compression.

4. Evidence gaps remain explicit.
   - Given LinkedIn/JD/sample evidence is incomplete
   - When a report claim depends on organization capability, hiring direction,
     profile background, or strategic success
   - Then Atlas routes to learning-capture evidence boundary instead of
     overclaiming.

5. Final completion requires drift review.
   - Given a reader-facing artifact is about to be claimed done
   - When the artifact has confirmed anchors or drift history
   - Then Atlas checks against the anchors and reports repair/blocker instead
     of claiming completion if drift is found.

6. Atlas does not over-trigger.
   - Given a simple one-off task with no learning/report state
   - When the user asks for a direct answer or small command
   - Then Atlas stays inactive.

---

## Task 1: Skill Authoring Gate And Prior-Art Read

**Files:**

- Read: `docs/superpowers/specs/2026-07-02-atlas-learning-report-collaboration-design.md`
- Read: `.codex/skills/learning-capture/SKILL.md`
- Read: `.codex/skills/public-report-quality-gate/SKILL.md`
- Read: `.codex/skills/visual-agent/SKILL.md`
- Read: `.codex/skills/material-collaboration-defaults/SKILL.md`
- Read: repo skill-authoring / TDD guidance required by `AGENTS.md`

- [x] **Step 1: Confirm SS source spec**

Read the Atlas design spec. Confirm these source decisions are preserved:

- Atlas is a controller, not a writer or visual worker
- scope is stateful learning/report collaboration
- B+C is the control model
- no OpenSpec lifecycle replacement
- no persistent state database in v1
- no `writing-method-composer` merge

- [x] **Step 2: Confirm worker ownership**

Read worker skills and record this mapping in `.codex/skills/atlas/evaluation.md`:

```text
Atlas owns:
- stateful collaboration detection
- confirmed anchor read-back
- phase and allowed/blocked action
- worker routing
- final drift gate

Worker skills own:
- learning-capture: source/evidence learning boundary
- public-report-quality-gate: reader-facing report quality
- visual-agent: visual classification and verification
- material-collaboration-defaults: material intake defaults
```

- [x] **Step 3: Record prior-art dedupe**

In `.codex/skills/atlas/evaluation.md`, record why Atlas is not:

- `writing-method-composer`
- `public-report-quality-gate`
- `visual-agent`
- `learning-capture`
- OpenSpec router

Commit after this task if files were created.

---

## Task 2: Add Atlas Skill Skeleton

**Files:**

- Create: `.codex/skills/atlas/SKILL.md`

- [x] **Step 1: Create compact trigger body**

`SKILL.md` must include only:

- purpose
- trigger conditions
- non-trigger conditions
- mandatory route block
- hard stops
- reference-loading pointers
- worker ownership boundary

Do not put long examples, scorecards, or replay tables in `SKILL.md`.

- [x] **Step 2: Include route block**

The route block must contain:

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

- [x] **Step 3: Include hard stops**

Hard stops must include:

- do not continue when phase is unclear
- do not rename or merge confirmed sections silently
- do not compress approved per-section visuals
- do not claim completion before Final Drift Gate
- do not use Atlas for simple one-off work

Run:

```bash
rg -n "Current Object|Confirmed Anchors|Blocked Actions|Final Drift Gate|one-off" .codex/skills/atlas/SKILL.md
```

Expected: all required phrases appear.

Commit after this task.

---

## Task 3: Add Atlas References

**Files:**

- Create: `.codex/skills/atlas/references/continuation-state-gate.md`
- Create: `.codex/skills/atlas/references/scorecard-registry.md`
- Create: `.codex/skills/atlas/references/worker-routing.md`
- Create: `.codex/skills/atlas/references/final-drift-gate.md`
- Create: `.codex/skills/atlas/references/replay-scenarios.md`

- [x] **Step 1: Write continuation-state-gate**

Include:

- when it triggers
- required state block
- how to handle unknown phase
- how to handle blocked action
- examples for report, H5, skill-change, and one-off negative case

- [x] **Step 2: Write scorecard-registry**

Use progressive disclosure:

```text
Core Gates
Reader Artifact Gates
Evidence Gates
Visual Gates
Boundary Gates
```

Do not freeze the Stripe-specific eleven-point list as universal behavior.

- [x] **Step 3: Write worker-routing**

Preserve the ownership boundaries from the design spec:

- Atlas first for stateful continuation
- learning-capture for source/evidence
- public-report-quality-gate for reader-facing quality
- visual-agent for visual classification and verification
- worker blocker routes back to Atlas

- [x] **Step 4: Write final-drift-gate**

Include checks for:

- missing confirmed anchors
- changed chapter/section names
- compressed talk track or transition
- unsupported evidence claim
- visual compression
- output-shape drift
- Stripe-specific rule promoted to generic rule
- generic rule not captured as candidate governance

- [x] **Step 5: Write replay-scenarios**

Include the five required scenarios from the source spec:

- locked chapters + continue
- per-section visuals + H5 continuation
- incomplete LinkedIn/JD evidence
- skill behavior changes after retro
- simple one-off task

Run:

```bash
rg -n "Core Gates|Reader Artifact Gates|Evidence Gates|Visual Gates|Boundary Gates|worker blocker|Final Drift|LinkedIn|one-off" .codex/skills/atlas
```

Expected: all required phrases appear in references.

Commit after this task.

---

## Task 4: Add RED Baseline Evaluation

**Files:**

- Create/modify: `.codex/skills/atlas/evaluation.md`

- [ ] **Step 1: Write pressure scenarios**

For each scenario, include:

```text
Input shape
Old failure
Expected Atlas route
Expected blocked action
Expected output or non-output
Proof boundary
```

- [ ] **Step 2: Write RED baseline**

Document the old failure based on the Stripe collaboration retro:

- continuing without reading anchors
- treating H5 as visual-only
- losing confirmed chapter/section names
- overclaiming or underusing LinkedIn/JD evidence
- compressing visuals
- treating OpenSpec as the next step before SS approval

Do not fabricate command output.

Commit after this task.

---

## Task 5: Integrate Worker Skills Minimally

**Files:**

- Modify: `.codex/skills/learning-capture/SKILL.md`
- Modify: `.codex/skills/public-report-quality-gate/SKILL.md`
- Modify: `.codex/skills/visual-agent/SKILL.md`
- Optionally modify: `.codex/skills/material-collaboration-defaults/SKILL.md`

- [ ] **Step 1: Integrate learning-capture**

Add only minimal wording:

- when routed by Atlas, preserve Atlas allowed/blocked actions
- return evidence blockers to Atlas
- do not turn incomplete LinkedIn/JD data into organization-wide claims

- [ ] **Step 2: Integrate public-report-quality-gate**

Add only minimal wording:

- when routed by Atlas, preserve confirmed anchors
- report Final Drift Gate failure for stateful output
- do not rewrite confirmed section structure as a new generic template

- [ ] **Step 3: Integrate visual-agent**

Add only minimal wording:

- when routed by Atlas, preserve visual anchors
- per-section visual approval cannot be compressed into a generic visual package
  without user approval
- visual verification must check the visual proof task, not only layout

- [ ] **Step 4: Decide material-collaboration-defaults**

Modify only if needed. If modified, wording must be limited to:

- rich material/report continuation with confirmed anchors or drift history
  should route to Atlas first

Run:

```bash
rg -n "Atlas|atlas|confirmed anchors|Final Drift|visual anchors|evidence blocker" .codex/skills/learning-capture/SKILL.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/visual-agent/SKILL.md .codex/skills/material-collaboration-defaults/SKILL.md
```

Expected: only small Atlas integration wording appears.

Commit after this task.

---

## Task 6: GREEN Replay And Behavior Checks

**Files:**

- Modify: `.codex/skills/atlas/evaluation.md`

- [ ] **Step 1: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Record the result in `.codex/skills/atlas/evaluation.md`.

- [ ] **Step 2: Run text checks**

Run:

```bash
rg -n "Atlas|Final Drift|confirmed anchors|visual anchors|evidence blocker" .codex/skills/atlas .codex/skills/learning-capture/SKILL.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/visual-agent/SKILL.md .codex/skills/material-collaboration-defaults/SKILL.md
git diff --check -- .codex/skills/atlas .codex/skills/learning-capture/SKILL.md .codex/skills/public-report-quality-gate/SKILL.md .codex/skills/visual-agent/SKILL.md .codex/skills/material-collaboration-defaults/SKILL.md
```

Expected:

- required Atlas route markers appear
- no whitespace errors

- [ ] **Step 3: Record GREEN result**

For each pressure scenario, record:

- expected Atlas state block
- expected worker route
- expected blocker or allowed output
- proof boundary

Commit after this task.

---

## Task 7: Final SS Plan Check

**Files:**

- Read: `docs/superpowers/specs/2026-07-02-atlas-learning-report-collaboration-design.md`
- Read: `docs/superpowers/plans/2026-07-02-atlas-learning-report-collaboration.md`
- Read: `.codex/skills/atlas/evaluation.md`

- [ ] **Step 1: Check scope**

Confirm the implementation still does not include:

- OpenSpec lifecycle replacement
- global AGENTS changes
- writing-method-composer merge
- full skill governance knowledge base
- H5/report artifact rewrite
- persistent state DB

- [ ] **Step 2: Check acceptance**

Confirm all Acceptance Spec items are covered by skill wording or evaluation
evidence.

- [ ] **Step 3: Check git boundary**

Run:

```bash
git status --short
git log -1 --oneline
```

Classify unrelated dirty files and do not stage them.

- [ ] **Step 4: Completion statement**

Completion may only claim:

```text
Atlas SS implementation is complete according to the approved plan.
```

It must not claim:

```text
Atlas is globally proven.
OpenSpec archive is ready.
All future drift is impossible.
Stripe H5 has been fixed.
```
