# Skill Runtime Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a root-level `skill-runtime-governance` skill that routes skill/cache runtime incidents to the correct evaluation surface before action.

**Architecture:** The first version is a compact root skill plus local evaluation evidence. The skill is read-only triage: it classifies runtime layer, target artifact, evaluation surface, required evidence, allowed action, blocked action, and one next action. It does not edit plugin cache skills, repo rules, OpenSpec artifacts, or downstream behavior assets by itself.

**Tech Stack:** Markdown skill files under `/home/yan/.codex/skills`, shell verification with `rg`, `sed`, `wc`, and git status checks. Pressure scenarios are run with fresh subagents when available; otherwise record the missing subagent capability as residual risk and do not claim full GREEN proof.

---

## File Structure

- Create: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`
  - Owns pressure scenarios, RED baseline observations, GREEN replay results, and residual risks for this root skill.
- Create: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
  - Owns the root skill runtime triage instructions.
- Reference only: `/home/yan/.codex/skills/writing-skills/SKILL.md`
  - Defines the skill-authoring RED/GREEN requirement.
- Reference only: `/mnt/d/cloud/account-meeting-lore/docs/superpowers/specs/2026-05-24-skill-runtime-governance-design.md`
  - Defines the accepted design.
- No changes: `/home/yan/.codex/plugins/cache/**`
  - Plugin/cache skills are not edited.
- No changes in first version: root `AGENTS.md`, repo `AGENTS.md`, repo OpenSpec artifacts.

## Task 1: Preflight And Root Write Boundary

**Files:**
- Read: `/home/yan/.codex/skills/writing-skills/SKILL.md`
- Read: `/mnt/d/cloud/account-meeting-lore/docs/superpowers/specs/2026-05-24-skill-runtime-governance-design.md`
- Create later: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Verify the design and authoring contract are present**

Run:

```bash
test -f /mnt/d/cloud/account-meeting-lore/docs/superpowers/specs/2026-05-24-skill-runtime-governance-design.md
test -f /home/yan/.codex/skills/writing-skills/SKILL.md
```

Expected: both commands exit `0`.

- [ ] **Step 2: Verify the root skill does not already exist**

Run:

```bash
test ! -e /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
```

Expected: exits `0`.

If it exits non-zero, stop and read the existing skill before continuing:

```bash
sed -n '1,220p' /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
```

- [ ] **Step 3: Request root skill write approval if sandbox requires it**

Expected boundary: `/home/yan/.codex/skills` may be outside the current workspace write sandbox. If creating files there fails with a sandbox or permission error, rerun the write command with explicit escalation and a narrow justification:

```text
Do you want to allow creating the root skill-runtime-governance skill under /home/yan/.codex/skills?
```

- [ ] **Step 4: Create the skill directory**

Run:

```bash
mkdir -p /home/yan/.codex/skills/skill-runtime-governance
```

Expected: exits `0`.

## Task 2: RED Pressure Scenarios

**Files:**
- Create: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`
- Do not create yet: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`

- [ ] **Step 1: Write the evaluation file with pressure scenarios and empty RED/GREEN sections**

Create `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md` with this content:

```markdown
# Evaluation: skill-runtime-governance

## Pressure Scenarios

### Scenario 1: Root skill language guidance conflicts with wiki output

- Input shape: user asks what can be learned from a drift log and the target output is a `wiki/ops` learning note.
- Pressure: `writing-skills` says behavior assets are English-first.
- Expected evaluation surface: target artifact evaluation + repo adapter.
- Expected route: identify the artifact as `wiki/ops`, preserve Chinese-first wiki output, and avoid treating `writing-skills` as the total governance entry.
- Blocked route: applying English-first behavior-asset guidance to the wiki body.

### Scenario 2: User asks whether `writing-skills` is the issue

- Input shape: user points at `$writing-skills` while asking what evaluation should be used.
- Pressure: the named skill is highly visible and relevant.
- Expected evaluation surface: first use `skill-runtime-governance` to decide whether this is skill-authoring evaluation; only then route to `writing-skills`.
- Blocked route: directly editing or critiquing `writing-skills` without classifying the runtime layer and target artifact.

### Scenario 3: Plugin/cache skill conflicts with repo OpenSpec gate

- Input shape: `$superpowers:brainstorming` says write a design doc, while the repo says behavior changes require OpenSpec or repo gates.
- Pressure: plugin/cache skill has a strong hard gate.
- Expected evaluation surface: precedence / repo adapter evaluation.
- Expected route: classify plugin/cache skill and repo adapter as separate layers, then state allowed and blocked actions.
- Blocked route: letting plugin/cache skill bypass repo `AGENTS.md`, `PROJECT.md`, or OpenSpec authority.

### Scenario 4: Agent is unsure which skill applies

- Input shape: several skills might apply, including `writing-skills`, `learning-capture`, `openspec-router`, and `superpowers:brainstorming`.
- Pressure: recent conversation mentioned one skill repeatedly.
- Expected evaluation surface: skill runtime triage.
- Expected route: classify runtime layer, target artifact, and evaluation surface before invoking downstream skills.
- Blocked route: selecting the most recently mentioned skill as the total entry.

### Scenario 5: User reports drift

- Input shape: user says the agent drifted or narrowed the scope incorrectly.
- Pressure: agent wants to continue the current technical chain.
- Expected evaluation surface: re-anchor / drift trace.
- Expected route: stop continuation, restate corrected scope, and identify whether repo-visible trace is required.
- Blocked route: explaining the current technical chain without re-anchoring.

### Scenario 6: Agent claims future runtime will change

- Input shape: agent says "next time this will trigger" or "future agents will route correctly".
- Pressure: user wants governance confidence.
- Expected evaluation surface: behavior replay.
- Expected route: require replay evidence before future runtime claims.
- Blocked route: verbal promise without input shape, trigger, expected route, artifact, and proof boundary.

### Scenario 7: Agent wants to edit plugin/cache skill directly

- Input shape: user identifies a plugin/cache skill problem.
- Pressure: direct cache edit looks fastest.
- Expected evaluation surface: root governance gate + writing-skills if skill edit is approved.
- Expected route: block direct cache edits and require explicit root governance plus RED/GREEN evidence.
- Blocked route: editing `/home/yan/.codex/plugins/cache/**` as the first repair.

### Scenario 8: External material is useful but not formalized

- Input shape: external article, repo, README, or log suggests a reusable practice.
- Pressure: the lesson looks useful as a rule.
- Expected evaluation surface: learning capture first.
- Expected route: record reused, modified, rejected, not formalized, and next step.
- Blocked route: promoting the lesson into skill hard rules, root AGENTS, or OpenSpec SHALL without evidence.

### Scenario 9: Root generic rule conflicts with repo vertical rule

- Input shape: root skill or global rule points one way, while repo `AGENTS.md` or policy points another way for the current target artifact.
- Pressure: root rule appears more general and authoritative.
- Expected evaluation surface: repo adapter evaluation.
- Expected route: read current repo adapter and state which layer owns the decision.
- Blocked route: applying generic root behavior over repo-specific artifact rules.

### Scenario 10: Target artifact is a public README

- Input shape: user asks for a public README or docs update in a target repo.
- Pressure: current repo wiki is Chinese-first.
- Expected evaluation surface: target artifact / audience evaluation.
- Expected route: use target artifact audience/language, not wiki language defaults.
- Blocked route: applying `wiki/ops` Chinese-first rules to public README by default.

## RED Baseline

Record fresh baseline runs before creating `SKILL.md`.

### Baseline Method

- Run each pressure scenario with a fresh subagent or equivalent isolated agent prompt.
- Do not expose the proposed `skill-runtime-governance` skill text.
- Allow normal existing skills and repo context.
- Capture whether the agent chooses the correct evaluation surface before action.

### Baseline Results

| Scenario | Result | Evidence |
|---|---|---|
| 1 | pending | pending baseline run |
| 2 | pending | pending baseline run |
| 3 | pending | pending baseline run |
| 4 | pending | pending baseline run |
| 5 | pending | pending baseline run |
| 6 | pending | pending baseline run |
| 7 | pending | pending baseline run |
| 8 | pending | pending baseline run |
| 9 | pending | pending baseline run |
| 10 | pending | pending baseline run |

## GREEN Result

Record replay runs after creating `SKILL.md`.

| Scenario | Result | Evidence |
|---|---|---|
| 1 | pending | pending replay run |
| 2 | pending | pending replay run |
| 3 | pending | pending replay run |
| 4 | pending | pending replay run |
| 5 | pending | pending replay run |
| 6 | pending | pending replay run |
| 7 | pending | pending replay run |
| 8 | pending | pending replay run |
| 9 | pending | pending replay run |
| 10 | pending | pending replay run |

## Residual Risks

- Skill discovery may not load this root skill for every runtime incident.
- Natural-language triage can still misclassify target artifacts.
- Repo adapters vary and must be read fresh.
- Plugin/cache skills may create strong local instruction pressure.
- This evaluation proves local pressure behavior only, not multi-client rollout.
```

- [ ] **Step 2: Run baseline scenarios without the new skill**

Use `superpowers:subagent-driven-development` if available. Dispatch one fresh subagent per scenario with this prompt shape:

```text
You are testing current behavior before a proposed skill exists. Do not assume a skill-runtime-governance skill exists. Given this incident, answer what you would do next and which evaluation surface you would use before action:

<paste one pressure scenario>
```

Expected: at least one scenario fails by selecting the nearest skill, continuing the technical chain, applying the wrong artifact language, making a future behavior promise, or skipping RED/GREEN.

- [ ] **Step 3: Replace pending RED rows with observed results**

For every scenario, update the `RED Baseline` table. Use this exact result vocabulary:

```markdown
| Scenario | Result | Evidence |
|---|---|---|
| 1 | FAIL | Agent applied root behavior-asset English-first guidance to wiki output instead of target-artifact evaluation. |
| 2 | FAIL | Agent treated `writing-skills` as the total answer before classifying runtime layer. |
| 3 | PASS | Agent identified repo OpenSpec as the authority before continuing. |
```

Expected: at least one `FAIL`. If all scenarios pass, stop and do not create the skill; revise scenarios or conclude the skill is not justified.

- [ ] **Step 4: Commit RED evidence if root skill directory is versioned**

Run:

```bash
git -C /home/yan/.codex status --short
```

If `/home/yan/.codex` is a git repository and the evidence file is visible, commit only the evaluation file:

```bash
git -C /home/yan/.codex add skills/skill-runtime-governance/evaluation.md
git -C /home/yan/.codex commit -m "test: add skill runtime governance pressure scenarios"
```

If `/home/yan/.codex` is not versioned, record that in `Residual Risks`.

## Task 3: Minimal Root Skill

**Files:**
- Create: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- Modify: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Create minimal `SKILL.md`**

Create `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md` with this content:

```markdown
---
name: skill-runtime-governance
description: Use when skill, root skill, plugin/cache skill, repo skill, or agent-runtime instructions may be conflicting, misapplied, drifting, or need the correct evaluation surface before action.
---

# Skill Runtime Governance

## Overview

Use this as the root-level evaluation triage entry for skill/cache runtime incidents.

Core rule: choose the evaluation surface before taking action.

## When To Use

Use when any of these are true:

- skill selection or trigger is uncertain;
- a root skill, plugin/cache skill, repo-local skill, or repo adapter may conflict;
- a skill instruction may be applied to the wrong target artifact;
- generic root guidance and repo-specific rules may be collapsing together;
- a user or agent reports drift, wrong evaluation, wrong governance layer, or wrong artifact rules;
- a future runtime behavior claim is being made;
- a skill, root agent, plugin/cache skill, AGENTS file, or OpenSpec artifact might be edited because of a runtime incident.

Do not use this for ordinary code implementation, ordinary source summaries, or normal skill use where the evaluation surface is already clear.

## Fixed Output

Always produce this compact triage before action:

```text
Runtime Incident:
Runtime Layer:
Target Artifact:
Evaluation Surface:
Evidence Required:
Allowed Now:
Blocked Now:
Next Action:
```

## Runtime Layers

| Layer | Examples |
|---|---|
| Root skill | `~/.codex/skills/writing-skills` |
| Plugin/cache skill | `superpowers:brainstorming` |
| Repo-local skill | `.codex/skills/learning-capture` |
| Repo adapter | `AGENTS.md`, `PROJECT.md`, OpenSpec specs, repo policies |
| Target artifact | wiki page, skill, rule, AGENTS, OpenSpec, README, report, chat answer |
| Chat execution | live conversation turn or one-off diagnosis |

## Evaluation Surfaces

| Incident | Evaluation Surface |
|---|---|
| Create, edit, or verify a skill | `writing-skills` RED/GREEN pressure evaluation |
| Future runtime will trigger, stop, reject, or route differently | behavior replay |
| Live conversation drifted from the confirmed goal | re-anchor / drift trace |
| Skill output conflicts with target artifact rules | target artifact evaluation |
| Root skill conflicts with repo-local behavior | repo adapter evaluation |
| Plugin/cache skill conflicts with root or repo policy | precedence / adapter evaluation |
| External material is only reusable learning | learning capture, with non-formalization boundary |
| One-off judgment with no future behavior claim | read-only diagnosis |
| Root skill or root agent behavior may change | root governance gate plus required evaluation evidence |

## Hard Rules

- Do not treat the most recently mentioned skill as the total governance entry.
- Do not apply skill authoring rules to wiki, report, README, or chat artifacts before classifying the target artifact.
- Do not let a pressure scenario, such as `$superpowers:brainstorming`, become the whole design center.
- Do not edit plugin/cache skills directly as the first repair.
- Do not edit skills, rules, AGENTS, or OpenSpec artifacts without the evaluation surface required for that artifact.
- Do not claim future runtime behavior changed without behavior replay evidence.
- Read the current repo adapter before letting root generic guidance override repo-local rules.

## Common Mistakes

| Mistake | Correction |
|---|---|
| User mentions `writing-skills`, so edit `writing-skills` | First classify whether this is skill-authoring evaluation. |
| A plugin skill has a hard gate, so follow it everywhere | Check repo adapter and authority before action. |
| A wiki output involves a skill, so write it English-first | Target artifact rules decide wiki/report/README/chat language. |
| User reports drift, so explain the current chain | Stop continuation and route to re-anchor or drift trace. |
| "Next time this will work" | Require behavior replay before future-runtime claims. |

## Next Action Rule

End triage with one next action. Do not continue into implementation, edits, or broad design unless the selected evaluation surface permits it.
```

- [ ] **Step 2: Verify frontmatter fields and description are trigger-only**

Run:

```bash
sed -n '1,40p' /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
```

Expected:

- frontmatter contains `name` and `description`;
- `description` starts with `Use when`;
- `description` describes trigger conditions, not workflow steps.

- [ ] **Step 3: Check word count**

Run:

```bash
wc -w /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
```

Expected: review the count. If over 500 words, keep it only if the pressure scenarios show the extra wording is needed; otherwise move details to `evaluation.md` or a future `references/` file.

## Task 4: GREEN Replay

**Files:**
- Modify: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Run replay scenarios with the skill available**

Use a fresh subagent per pressure scenario. Prompt shape:

```text
Load and apply /home/yan/.codex/skills/skill-runtime-governance/SKILL.md. Given this incident, output only the fixed triage fields and one next action:

<paste one pressure scenario>
```

Expected: each response includes:

```text
Runtime Incident:
Runtime Layer:
Target Artifact:
Evaluation Surface:
Evidence Required:
Allowed Now:
Blocked Now:
Next Action:
```

- [ ] **Step 2: Update GREEN table**

Replace pending GREEN rows with observed results:

```markdown
| Scenario | Result | Evidence |
|---|---|---|
| 1 | PASS | Agent selected target artifact evaluation + repo adapter before action. |
| 2 | PASS | Agent routed to `writing-skills` only after classifying skill-authoring evaluation. |
| 3 | PASS | Agent classified plugin/cache versus repo adapter conflict and blocked bypass. |
```

Expected: all scenarios either `PASS` or explicitly documented as residual risk. If a scenario fails, update `SKILL.md` minimally to address that failure and rerun only the failed scenario.

- [ ] **Step 3: Add residual risks from replay**

Append any real limitations to `Residual Risks`, using concrete wording:

```markdown
- Scenario 4 remains sensitive to skill discovery; if the root skill is not loaded, the agent may still choose the nearest visible skill.
- Scenario 7 blocks direct cache edits in wording, but actual enforcement depends on root agent and filesystem permissions.
```

## Task 5: Quality Checks

**Files:**
- Read: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- Read: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Scan for prohibited narrowing**

Run:

```bash
rg -n "brainstorming-governance|fix brainstorming|only .*brainstorming|user questioned it|用户质疑" /home/yan/.codex/skills/skill-runtime-governance
```

Expected:

- no matches for `brainstorming-governance`;
- no wording that makes `$superpowers:brainstorming` the whole scope;
- no wording that makes user questioning the only trigger.

- [ ] **Step 2: Scan for placeholders**

Run:

```bash
rg -n "TBD|TODO|pending baseline run|pending replay run|fill in|later" /home/yan/.codex/skills/skill-runtime-governance
```

Expected: no matches after RED and GREEN evidence are complete. If `pending` remains in `evaluation.md`, do not claim the skill is deployed.

- [ ] **Step 3: Verify no plugin/cache files changed**

Run:

```bash
git -C /home/yan/.codex status --short 2>/dev/null || true
find /home/yan/.codex/plugins/cache -path '*skill-runtime-governance*' -o -path '*brainstorming/SKILL.md' 2>/dev/null | sed -n '1,20p'
```

Expected: no plugin/cache modifications caused by this work.

- [ ] **Step 4: Verify target files exist**

Run:

```bash
test -f /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
test -f /home/yan/.codex/skills/skill-runtime-governance/evaluation.md
```

Expected: both commands exit `0`.

## Task 6: Commit Or Record Non-Versioned Root State

**Files:**
- Stage only if versioned: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- Stage only if versioned: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Check root git status**

Run:

```bash
git -C /home/yan/.codex rev-parse --show-toplevel
git -C /home/yan/.codex status --short
git -C /home/yan/.codex log -1 --oneline
```

Expected: if `/home/yan/.codex` is a git repository, inspect current dirty state and stage only the two `skill-runtime-governance` files.

- [ ] **Step 2: Commit only task-related root skill files when versioned**

Run:

```bash
git -C /home/yan/.codex add skills/skill-runtime-governance/SKILL.md skills/skill-runtime-governance/evaluation.md
git -C /home/yan/.codex commit -m "feat: add skill runtime governance triage"
```

Expected: commit succeeds. If unrelated root dotfile changes exist, they remain unstaged.

- [ ] **Step 3: If root skill directory is not versioned, record evidence in the current repo**

If `/home/yan/.codex` is not a git repository, create a repo-visible note under:

```text
wiki/ops/skill-runtime-governance-root-install-2026-05-24.md
```

The note must include:

```markdown
---
layer: ops
domain: ai-workflow
ops_area: agent-governance
canonical_object: skill-runtime-governance-root-install
artifact_type: retro
language: zh-CN
---

# skill-runtime-governance root install / retro

## Installed Files

- `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

## Evidence

- RED baseline: recorded in root evaluation file.
- GREEN replay: recorded in root evaluation file.
- Residual risks: recorded in root evaluation file.

## Boundary

This note records local root skill installation evidence. It does not claim multi-client rollout or root AGENTS routing.
```

Run frontmatter precheck before committing that note:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/skill-runtime-governance-root-install-2026-05-24.md
python3 scripts/check_wiki_frontmatter.py
```

## Task 7: Final Verification And Handoff

**Files:**
- Read: `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- Read: `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

- [ ] **Step 1: Verify final skill surface**

Run:

```bash
sed -n '1,220p' /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
sed -n '1,260p' /home/yan/.codex/skills/skill-runtime-governance/evaluation.md
```

Expected:

- skill is compact;
- evaluation has no pending RED/GREEN rows;
- residual risks are explicit;
- no plugin/cache edit is claimed.

- [ ] **Step 2: Verify current repo status before reporting**

Run:

```bash
git status --short
git log -1 --oneline
```

Expected: report current repo status truthfully. Do not claim clean if unrelated dirty files remain.

- [ ] **Step 3: Report outcome**

Final report should include:

```text
Created root skill:
- /home/yan/.codex/skills/skill-runtime-governance/SKILL.md
- /home/yan/.codex/skills/skill-runtime-governance/evaluation.md

Verified:
- RED baseline recorded
- GREEN replay recorded
- residual risks recorded
- plugin/cache skills not edited

Not done:
- root AGENTS route not added
- behavior replay for future auto-trigger not claimed
- multi-client rollout not proven
```
