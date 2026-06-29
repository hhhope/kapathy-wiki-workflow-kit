# Native Superpowers OpenSpec Check/Archive Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the repo-local agent workflow preserve Superpowers-native spec/plan execution while using OpenSpec only for check, evidence, and archive unless scope changes.

**Architecture:** Add a narrow repo workflow contract to existing behavior assets instead of creating a new workflow system. Preserve Superpowers plans as implementation progress, keep OpenSpec tasks as check/archive ledger, and prove the distinction with RED/GREEN replay evidence in the active OpenSpec change.

**Tech Stack:** Markdown behavior assets, OpenSpec change artifacts, Python unit tests using the existing `unittest` style, `scripts/check_behavior_assets.py`, `openspec validate`.

---

## File Structure

- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/proposal.md`
  - Reframe the change from "OpenSpec preserves Superpowers overlay" to "Superpowers-native execution with OpenSpec check/archive".
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/design.md`
  - Add the final workflow model, plan-check boundary, resume order, conflict handling, and OpenSpec role.
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md`
  - Replace implementation-overlay wording with check/archive lifecycle tasks.
- Create: `openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md`
  - Record pressure scenarios, RED baseline, GREEN result, prior-art dedupe, and residual risks.
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/specs/openspec-apply-change/spec.md`
  - Replace overlay-preservation scenarios with check/archive and scope-change scenarios.
- Create: `tests/test_native_superpowers_openspec_workflow.py`
  - Add RED/GREEN checks for repo-local workflow wording and active change evidence.
- Modify: `.codex/skills/openspec-apply-change/SKILL.md`
  - Clarify that OpenSpec apply is not the implementation plan when a Superpowers plan is active; it handles check/archive or scope-change transitions.
- Modify: `.codex/skills/openspec-apply-change/references/execution-overlay.md`
  - Update the example from "execution overlay inside OpenSpec" to "Superpowers plan as implementation plan; OpenSpec as check/archive ledger".
- Optionally modify: `AGENTS.md`
  - Only if the skill-level rule is not enough for routing. Keep this small and do not duplicate long examples.

## Task 1: RED Workflow Replay Tests

**Files:**
- Create: `tests/test_native_superpowers_openspec_workflow.py`

- [ ] **Step 1: Add RED tests for the missing workflow contract**

Create `tests/test_native_superpowers_openspec_workflow.py`:

```python
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class NativeSuperpowersOpenSpecWorkflowTest(unittest.TestCase):
    def read(self, rel_path: str) -> str:
        return (ROOT / rel_path).read_text(encoding="utf-8")

    def test_openspec_apply_skill_preserves_superpowers_native_execution(self) -> None:
        text = self.read(".codex/skills/openspec-apply-change/SKILL.md")
        self.assertIn("Superpowers plan is the implementation plan", text)
        self.assertIn("OpenSpec tasks are the check/archive ledger", text)
        self.assertIn("do not track Superpowers block progress in tasks.md", text)
        self.assertIn("scope changes stop implementation", text)

    def test_active_change_defines_plan_check_without_new_plan(self) -> None:
        design = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/design.md")
        self.assertIn("plan-check belongs to Superpowers plan review", design)
        self.assertIn("plan-check does not create a new plan", design)
        self.assertIn("Acceptance Spec lives inside the Superpowers design spec", design)

    def test_tasks_are_check_archive_only(self) -> None:
        tasks = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md")
        self.assertIn("This file is not the implementation plan", tasks)
        self.assertIn("Use the Superpowers plan for block execution", tasks)
        forbidden = ["Run RED", "Implement GREEN", "Edit file", "Add function"]
        for marker in forbidden:
            self.assertNotIn(marker, tasks)

    def test_evaluation_records_drift_and_negative_cases(self) -> None:
        evaluation = self.read("openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md")
        self.assertIn("positive trigger", evaluation)
        self.assertIn("negative should-not-trigger", evaluation)
        self.assertIn("Stripe H5 drift", evaluation)
        self.assertIn("scope change", evaluation)
```

- [ ] **Step 2: Run RED tests and confirm failure**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_native_superpowers_openspec_workflow -v
```

Expected:

```text
FAILED
```

At least one failure should mention missing workflow wording in `.codex/skills/openspec-apply-change/SKILL.md` or missing `evaluation.md`.

- [ ] **Step 3: Commit RED tests only**

Run:

```bash
git add tests/test_native_superpowers_openspec_workflow.py
git commit -m "Add native Superpowers OpenSpec workflow RED tests"
```

## Task 2: Reframe The Active OpenSpec Change

**Files:**
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/proposal.md`
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/design.md`
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md`
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/specs/openspec-apply-change/spec.md`
- Create: `openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md`

- [ ] **Step 1: Rewrite proposal framing**

Update `proposal.md` so its model is:

```md
# Native Superpowers With OpenSpec Check/Archive

## Why

The repository needs Superpowers-native design and implementation planning to
remain uninterrupted. OpenSpec is still useful for acceptance, evidence,
scope-change stops, and archive review, but it must not become a second
implementation plan.

## What Changes

- Keep Superpowers design spec and writing-plan as the implementation authority.
- Treat OpenSpec tasks as check/archive lifecycle items only.
- Put Acceptance Spec inside the Superpowers design spec.
- Run plan-check as part of Superpowers plan review, not as OpenSpec progress.
- Use OpenSpec during execution only when scope changes or after implementation
  for check, evidence, validation, and archive review.

## Out Of Scope

- No upstream Superpowers plugin edits.
- No OpenSpec CLI changes.
- No continuous OpenSpec progress syncing during Superpowers execution.
- No requirement to create OpenSpec for small one-session work.
```

- [ ] **Step 2: Rewrite design with the final workflow**

Ensure `design.md` contains these exact boundary sentences:

```md
Superpowers plan is the implementation plan.
OpenSpec tasks are the check/archive ledger.
plan-check belongs to Superpowers plan review.
plan-check does not create a new plan.
Acceptance Spec lives inside the Superpowers design spec.
scope changes stop implementation.
```

Also add resume order:

```text
Superpowers spec -> Superpowers plan -> git status -> git log -1 -> current unfinished block
```

- [ ] **Step 3: Rewrite tasks as check/archive lifecycle only**

Replace `tasks.md` with:

```md
# Tasks

This file is not the implementation plan.
Use the Superpowers plan for block execution.
Do not track Superpowers block progress in tasks.md.

- [ ] 1. Add RED replay tests for the workflow boundary.
- [ ] 2. Update repo-local workflow guidance.
- [ ] 3. Record behavior replay evidence.
- [ ] 4. Run focused tests, behavior asset checks, and OpenSpec validation.
- [ ] 5. Stop at completion boundary and perform archive review separately.
```

- [ ] **Step 4: Rewrite OpenSpec delta scenarios**

Update `specs/openspec-apply-change/spec.md` with scenarios for:

- Superpowers-native implementation remains uninterrupted.
- OpenSpec tasks are check/archive only.
- Scope changes stop implementation and route to OpenSpec.
- Completion evidence summarizes Superpowers block evidence instead of replacing it.

- [ ] **Step 5: Create evaluation evidence**

Create `evaluation.md` with required sections:

```md
# Evaluation

## Pressure Scenarios

| Case | Input or situation shape | Trigger condition | Expected route | Repo-visible artifact | Expected output | Promotion or non-promotion boundary | Proof boundary |
|---|---|---|---|---|---|---|---|
| positive trigger: Superpowers plan approved for multi-file work | User has approved Superpowers spec and plan | Work needs check/archive | implement from Superpowers plan, use OpenSpec only for check/archive | Superpowers plan, this OpenSpec change | plan blocks drive execution | OpenSpec does not replace plan | local replay only |
| negative should-not-trigger: small one-session edit | Simple one-file fix | No lifecycle/archive need | no OpenSpec wrapper required | none | direct small-task flow | no durable wrapper | local replay only |
| drift case: Stripe H5 drift | Superpowers design used as supporting context | Verification checks keywords/screenshots only | fail plan-check/check evidence | Stripe drift records | missing acceptance path is reported | no archive-ready claim | local replay only |
| scope change | Implementation discovers new scope | plan no longer matches scope | stop and update/create OpenSpec | active change | no silent merge | user confirms scope | local replay only |

## Replay Evidence

- input or situation shape: Superpowers-native work with possible OpenSpec lifecycle.
- trigger condition: approved Superpowers plan plus multi-file or long-lived check/archive need.
- expected route: execute from Superpowers plan; use OpenSpec for check/archive or scope-change stops.
- repo-visible artifact: `.codex/skills/openspec-apply-change/SKILL.md`, this change, Superpowers spec/plan.
- expected output: no second implementation plan in `tasks.md`.
- promotion or non-promotion boundary: repo-local workflow guidance only.
- proof boundary: local unit tests and manual replay, not multi-session telemetry.

## RED Baseline

Observed current failure: existing guidance permits OpenSpec to preserve or
rewrite an overlay instead of clearly stating that Superpowers plan remains the
implementation plan and OpenSpec tasks are check/archive only.

## GREEN Result

Pending until tests and validation pass.

## Prior-Art / Common-Rule Dedupe

Scanned:
- `AGENTS.md`
- `.codex/skills/openspec-router/SKILL.md`
- `.codex/skills/openspec-apply-change/SKILL.md`
- `openspec/specs/openspec-apply-change/spec.md`
- `wiki/ops/stripe-ai-company-evolution-h5-structure-explore-2026-06-23.md`

Owns:
- Repo-local Superpowers/OpenSpec check/archive boundary.

References:
- Existing OpenSpec source-of-truth and archive rules.
- Superpowers native brainstorming and writing-plans rules.

Rejects:
- Editing upstream Superpowers plugins.
- Turning OpenSpec tasks into a second implementation plan.

## Residual Risks

- Final `evaluation.md` can still be written late; mitigation is block-level plan evidence and commits.
- Future agents must load repo guidance.
```

- [ ] **Step 6: Commit reframed OpenSpec artifacts**

Run:

```bash
git add openspec/changes/preserve-superpowers-plan-tdd-overlay
git commit -m "Reframe OpenSpec role as Superpowers check archive"
```

## Task 3: Update Repo-Local Agent Guidance

**Files:**
- Modify: `.codex/skills/openspec-apply-change/SKILL.md`
- Modify: `.codex/skills/openspec-apply-change/references/execution-overlay.md`
- Optionally modify: `AGENTS.md`

- [ ] **Step 1: Update `openspec-apply-change` skill**

Add a compact section:

```md
## Superpowers-Native Check/Archive Boundary

When a Superpowers design spec and writing-plan are active:

- Superpowers plan is the implementation plan.
- OpenSpec tasks are the check/archive ledger.
- Do not track Superpowers block progress in tasks.md.
- Run plan-check during Superpowers plan review, not as OpenSpec progress.
- During implementation, resume from the Superpowers plan and git state.
- Use OpenSpec during implementation only when scope changes.
- After all Superpowers blocks complete, use OpenSpec for acceptance evidence,
  validation, and archive review.

If scope changes, stop implementation and update or create OpenSpec before
continuing.
```

- [ ] **Step 2: Update the reference example**

In `references/execution-overlay.md`, replace the old good-shape authority block with:

```md
Authority:
- Superpowers plan is the implementation plan.
- OpenSpec tasks are the check/archive ledger.
- Do not track block progress in OpenSpec tasks.
- Summarize block evidence into OpenSpec evaluation after implementation.
```

- [ ] **Step 3: Decide whether AGENTS needs a short pointer**

If tests or manual replay show skill guidance is not discoverable enough, add only this short pointer to `AGENTS.md`:

```md
For Superpowers-native work, execute from the approved Superpowers plan. Use
OpenSpec for scope changes, acceptance evidence, validation, and archive review;
do not turn OpenSpec `tasks.md` into a second implementation plan.
```

If `.codex/skills/openspec-apply-change/SKILL.md` is sufficient, skip AGENTS.

- [ ] **Step 4: Run GREEN focused tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_native_superpowers_openspec_workflow -v
```

Expected:

```text
OK
```

- [ ] **Step 5: Commit guidance updates**

Run:

```bash
git add .codex/skills/openspec-apply-change/SKILL.md .codex/skills/openspec-apply-change/references/execution-overlay.md AGENTS.md
git commit -m "Clarify Superpowers native OpenSpec check archive boundary"
```

If `AGENTS.md` was not changed, omit it from `git add`.

## Task 4: Validation And Completion Evidence

**Files:**
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md`
- Modify: `openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md`

- [ ] **Step 1: Run behavior asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected:

```text
No behavior asset evaluation drift found.
```

If unrelated existing drift appears, copy the exact relevant lines into `evaluation.md#Residual Risks`.

- [ ] **Step 2: Run OpenSpec validation**

Run:

```bash
openspec validate preserve-superpowers-plan-tdd-overlay --strict
```

Expected:

```text
Change 'preserve-superpowers-plan-tdd-overlay' is valid
```

PostHog DNS flush warnings after the valid line are non-blocking telemetry noise.

- [ ] **Step 3: Update GREEN result**

Replace the pending GREEN section in `evaluation.md` with:

```md
## GREEN Result

- Focused workflow tests passed:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_native_superpowers_openspec_workflow -v`
- Behavior asset checker result: paste the exact final stdout line, for example
  `No behavior asset evaluation drift found.`, or paste the unrelated blocker
  lines copied into `## Residual Risks`.
- OpenSpec strict validation result: paste the exact valid line,
  `Change 'preserve-superpowers-plan-tdd-overlay' is valid`.
- Manual replay: Stripe-style keyword/screenshot-only verification fails the new check/archive boundary because the Superpowers acceptance path is not evidenced.
```

- [ ] **Step 4: Mark completed tasks**

Update `tasks.md` only for completed lifecycle items. Do not add implementation steps.

- [ ] **Step 5: Commit validation evidence**

Run:

```bash
git add openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md
git commit -m "Record Superpowers OpenSpec workflow validation"
```

## Task 5: Stop At Completion Boundary

**Files:**
- Read: `openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md`
- Read: `openspec/changes/preserve-superpowers-plan-tdd-overlay/evaluation.md`

- [ ] **Step 1: Confirm all lifecycle tasks are checked**

Run:

```bash
sed -n '1,120p' openspec/changes/preserve-superpowers-plan-tdd-overlay/tasks.md
```

Expected: every listed lifecycle task is `- [x]`.

- [ ] **Step 2: Run final status checks**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: only unrelated pre-existing workspace changes remain unstaged, and the latest commit is the validation evidence commit.

- [ ] **Step 3: Stop before archive**

Do not archive immediately. Report:

```text
Implementation complete for preserve-superpowers-plan-tdd-overlay.
Default next action is archive review.
```

Archive review is a separate step under repo rules.
