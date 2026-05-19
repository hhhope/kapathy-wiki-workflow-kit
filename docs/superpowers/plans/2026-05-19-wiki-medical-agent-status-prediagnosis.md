# wiki-medical-agent Status Prediagnosis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a compact `wiki-medical-agent` response rule so status/blocked results still produce a read-only prediagnosis when the live user intent is to continue or modify.

**Architecture:** Create a small follow-up OpenSpec change, then update only the repo-local `wiki-medical-agent` skill and its evaluation evidence. Do not change `build_wiki_medical_agent.py`; this is a behavior-contract patch for the agent response layer.

**Tech Stack:** Markdown skill files, OpenSpec change artifacts, repo behavior-asset checker.

---

## File Structure

- Create: `openspec/changes/add-medical-agent-status-prediagnosis/proposal.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/design.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/tasks.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/specs/wiki-medical-agent/spec.md`
- Modify: `.codex/skills/wiki-medical-agent/SKILL.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md`

This is a follow-up change because `openspec/changes/introduce-wiki-medical-agent-state-machine/tasks.md` is complete and must not be reopened for adjacent behavior work.

### Task 1: Create Minimal OpenSpec Change

**Files:**
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/proposal.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/design.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/tasks.md`
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/specs/wiki-medical-agent/spec.md`

- [ ] **Step 1: Create change directory**

Run:

```bash
mkdir -p openspec/changes/add-medical-agent-status-prediagnosis/specs/wiki-medical-agent
```

Expected: directory exists.

- [ ] **Step 2: Write proposal**

Create `openspec/changes/add-medical-agent-status-prediagnosis/proposal.md`:

```markdown
# Proposal: medical-agent status prediagnosis

## Why

`wiki-medical-agent` currently reports fixed status fields, but a status result
can become a dead end when the user is actually asking to continue, modify, or
decide the next route.

## What Changes

- Add a compact `Status / Blocked Response` rule to the repo-local
  `wiki-medical-agent` skill.
- Require read-only prediagnosis before asking the user for more detail when
  the script result is non-executing status but the live intent is to continue
  or modify.
- Preserve existing write boundaries.

## Out of Scope

- No changes to `scripts/build_wiki_medical_agent.py`.
- No global agent rule.
- No automatic mutation of MOC pages, ADRs, OpenSpec lifecycle state, taxonomy
  config, relation fields, or skills beyond this scoped skill edit.
```

- [ ] **Step 3: Write design**

Create `openspec/changes/add-medical-agent-status-prediagnosis/design.md`:

```markdown
# Design: medical-agent status prediagnosis

## Scope

This is a skill-contract patch. It changes how the agent responds after the
medical-agent script returns a non-executing status result.

## Behavior

When the user only asks for status, the existing fixed-field response remains
sufficient.

When the user is trying to continue, modify, apply, repair, or decide next
steps, and the script result is `report_status`, `blocked`,
`awaiting_confirmation`, or `archive_ready`, the agent must add a read-only
prediagnosis before asking for missing details.

The prediagnosis may use already known state or at most one local read-only
check. It must not write files or expand authority.

## Response Shape

The response should include:

- script result
- interpreted live user intent
- read-only prediagnosis
- recommended next action
- remaining user decision, if any

## Proof Boundary

This change improves agent response behavior. It does not prove that future
clients will always route correctly without loading the skill.
```

- [ ] **Step 4: Write tasks**

Create `openspec/changes/add-medical-agent-status-prediagnosis/tasks.md`:

```markdown
# Tasks

- [ ] 1. Create OpenSpec proposal, design, tasks, and spec delta.
- [ ] 2. Record RED baseline evidence showing the current skill lacks status prediagnosis.
- [ ] 3. Add compact `Status / Blocked Response` wording to `.codex/skills/wiki-medical-agent/SKILL.md`.
- [ ] 4. Record GREEN replay evidence for the four pressure scenarios.
- [ ] 5. Run OpenSpec validation and behavior-asset checker.
- [ ] 6. Commit the verified implementation and stop at completion.
```

- [ ] **Step 5: Write spec delta**

Create `openspec/changes/add-medical-agent-status-prediagnosis/specs/wiki-medical-agent/spec.md`:

```markdown
# wiki-medical-agent Specification Delta

## ADDED Requirements

### Requirement: Status responses SHALL include prediagnosis for continuation intent

When `wiki-medical-agent` returns a non-executing status result and the live
user request is to continue, modify, apply, repair, or decide next steps, the
agent SHALL provide a read-only prediagnosis before asking the user for missing
details.

#### Scenario: User asks what to do next from archive-ready state

- **GIVEN** the medical-agent result is `archive_ready`
- **WHEN** the user asks what to do next
- **THEN** the agent SHALL report the script result
- **AND** interpret the live user intent
- **AND** recommend the next safe route instead of only repeating status fields

#### Scenario: User asks to modify generated or sensitive wiki output

- **GIVEN** the medical-agent result is non-executing status
- **WHEN** the user asks to modify generated or sensitive wiki output
- **THEN** the agent SHALL preserve existing write boundaries
- **AND** provide a read-only prediagnosis of the likely route before asking for
  missing details

#### Scenario: User selects a previously offered option

- **GIVEN** the agent previously offered numbered options
- **WHEN** the user replies with a bare option number
- **THEN** the agent SHALL preserve live thread context
- **AND** continue the selected option without requiring the user to restate the
  full target
```

- [ ] **Step 6: Validate change structure**

Run:

```bash
openspec validate add-medical-agent-status-prediagnosis --strict
```

Expected: command exits 0 and reports the change is valid.

- [ ] **Step 7: Commit OpenSpec scaffolding**

Run:

```bash
git add openspec/changes/add-medical-agent-status-prediagnosis
git commit -m "docs: propose medical-agent status prediagnosis"
```

Expected: commit includes only the new OpenSpec change files.

### Task 2: Add RED Baseline Evidence

**Files:**
- Create: `openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md`

- [ ] **Step 1: Verify old skill lacks the rule**

Run:

```bash
rg -n "Status / Blocked Response|read-only prediagnosis|interpreted live user intent" .codex/skills/wiki-medical-agent/SKILL.md
```

Expected: no matches.

- [ ] **Step 2: Capture script status behavior**

Run:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "改 wiki/moc"
```

Expected: result is a non-executing status-style response, not a dedicated
prediagnosis response.

- [ ] **Step 3: Write evaluation RED section**

Create `openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md`:

```markdown
# Evaluation: medical-agent status prediagnosis

## Pressure Scenarios

1. User says `那我继续做什么` while the case is `archive_ready`.
2. User says `改 wiki/moc` and the script returns status.
3. User replies only `1` after options were presented.
4. User asks why no prediagnosis was given.

## RED Baseline

- `.codex/skills/wiki-medical-agent/SKILL.md` has no `Status / Blocked Response`
  rule.
- The skill requires fixed fields but does not require interpreted live intent,
  read-only prediagnosis, or a recommended next action when status is not enough.
- Baseline command:
  `python3 scripts/build_wiki_medical_agent.py --intent-text "改 wiki/moc"`
- Baseline result: non-executing status-style output; the skill does not require
  the agent to bridge from that status to a read-only prediagnosis.

## GREEN Result

Not recorded in this RED baseline commit. Task 4 replaces this section after
the skill wording is updated and replay expectations are checked.

## Residual Risks

- This RED baseline only proves the current skill lacks a response obligation.
- It does not prove the future wording is sufficient until Task 4 records the
  GREEN replay result.
```

- [ ] **Step 4: Commit baseline evidence**

Run:

```bash
git add openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md
git commit -m "test: record medical-agent prediagnosis baseline"
```

Expected: commit includes only `evaluation.md`.

### Task 3: Update Skill Wording

**Files:**
- Modify: `.codex/skills/wiki-medical-agent/SKILL.md`

- [ ] **Step 1: Insert compact section before `Treatment apply`**

Add this section after the Authority model block:

```markdown
Status / Blocked Response:

- If the user only asks for status, report the fixed fields above.
- If the user is trying to continue, modify, apply, repair, or decide next
  steps, and the medical-agent result is `report_status`, `blocked`,
  `awaiting_confirmation`, or `archive_ready`, do not stop at the fixed fields.
- Before asking the user for missing details, provide a read-only prediagnosis
  based on already available state or at most one local read-only check.
- Include: script result, interpreted live user intent, read-only
  prediagnosis, recommended next action, and the specific point that still
  requires user confirmation, if any.
- This rule does not expand write authority or bypass the case-file authority
  model.
```

- [ ] **Step 2: Verify wording exists**

Run:

```bash
rg -n "Status / Blocked Response|read-only prediagnosis|interpreted live user intent" .codex/skills/wiki-medical-agent/SKILL.md
```

Expected: matches the new section.

- [ ] **Step 3: Commit skill wording**

Run:

```bash
git add .codex/skills/wiki-medical-agent/SKILL.md
git commit -m "docs: require medical-agent status prediagnosis"
```

Expected: commit includes only `.codex/skills/wiki-medical-agent/SKILL.md`.

### Task 4: Record GREEN Replay And Validate

**Files:**
- Modify: `openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md`
- Modify: `openspec/changes/add-medical-agent-status-prediagnosis/tasks.md`

- [ ] **Step 1: Update evaluation GREEN section**

Replace the pending GREEN and residual risk sections in `evaluation.md` with:

```markdown
## GREEN Result

The updated skill now requires `Status / Blocked Response` handling.

Replay expectations:

- `那我继续做什么`: report script status, interpret the live intent as next-route
  selection, and recommend archive review or the bounded next workflow.
- `改 wiki/moc`: report script status, preserve generated-output write
  boundaries, provide a read-only prediagnosis, and recommend the safe next
  route before asking for missing details.
- Bare `1`: preserve prior option context and continue that option without
  forcing the user to restate the full target.
- `为什么没有预判断`: identify that fixed-field status was treated too
  mechanically and state what prediagnosis should have happened.

## Residual Risks

- This is skill-level behavior evidence, not proof that clients will comply
  without loading the skill.
- No script intent classifier was changed; unusual phrasing may still return
  `status`, but the skill now defines how the agent should respond to that.
```

- [ ] **Step 2: Run OpenSpec validation**

Run:

```bash
openspec validate add-medical-agent-status-prediagnosis --strict
```

Expected: exits 0.

- [ ] **Step 3: Run behavior-asset checker**

Run:

```bash
python3 scripts/check_behavior_assets.py
```

Expected: exits 0. If it exits non-zero for a known existing issue, copy the
summary into `evaluation.md` under `Residual Risks` before continuing.

- [ ] **Step 4: Mark tasks complete**

Update `openspec/changes/add-medical-agent-status-prediagnosis/tasks.md` so all
completed checkboxes are marked `[x]`.

- [ ] **Step 5: Commit validation evidence**

Run:

```bash
git add openspec/changes/add-medical-agent-status-prediagnosis/evaluation.md openspec/changes/add-medical-agent-status-prediagnosis/tasks.md
git commit -m "test: validate medical-agent status prediagnosis"
```

Expected: commit includes only evaluation and task progress.

### Task 5: Final Verification Boundary

**Files:**
- No file changes expected.

- [ ] **Step 1: Verify latest commit and status**

Run:

```bash
git log -3 --oneline
git status --short
```

Expected: latest commits reflect the OpenSpec scaffold, baseline, skill wording,
and validation evidence. Existing unrelated dirty files may remain; do not
include them in this work.

- [ ] **Step 2: Stop at completion**

Do not archive this change in the same pass. Report that implementation is
complete and the next action is archive review.
