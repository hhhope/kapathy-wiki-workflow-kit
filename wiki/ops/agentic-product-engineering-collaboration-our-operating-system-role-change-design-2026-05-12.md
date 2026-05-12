---
title: agentic-product-engineering-collaboration our operating system role-change design
canonical_object: agentic-product-engineering-collaboration
artifact_type: office_hours_design
status: draft
created: 2026-05-12
target: wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
source_paths:
  - wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html
  - wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md
  - wiki/ops/agentic-product-engineering-collaboration-company-playbook-role-change-diagnosis-2026-05-12.md
  - wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md
---

# Our Operating System Role-Change Design

## Problem Statement

The `our-operating-system` H5 already says roles need to change. It names Boss,
product / PM, engineering lead, engineer, QA, and project management.

But it still leaves one practical question under-specified:

> In our own operating system, which role owns which step, what artifact do they
> produce, and what evidence proves that the step is done?

The page currently gives role statements in several places:

- section `06 · 我们能做什么`: demand entry, engineering execution, test
  verification, project management, knowledge writeback
- section `07 · 模式变化`: eight-step process
- section `08 · 工程重塑`: old / new workflow and role shifts
- section `13 · 角色变化`: role list
- section `14 · 写作流程`: writing workflow roles
- section `15 · 下一步`: 30-day pilot checklist

That is too scattered. The reader can agree with the idea but still not know
what to change in Monday's work.

## Demand Evidence

User correction:

- The company role discussion is done.
- The next question is specifically about
  `agentic-product-engineering-collaboration-our-operating-system.html`.
- The user asks: "我们的需要改的是什么呢？我们的岗位呢要看看需要变更什么".

Local evidence:

- The H5 already has the eight-step operating system:
  intent packet, Spec / ADR entry, Agent execution packet, evidence matrix,
  Review Packet, human judgment, failure writeback, weekly metrics.
- The H5 already says "产品守意图，研发交证据，测试定完成，项目管状态，老板看结果".
- The company-playbook role diagnosis clarified the stance:
  AI does not make every role a coder. It moves roles closer to executable
  artifacts, verification evidence, and sharper accountability.
- The article evidence matrix says people are not simply replaced;
  responsibility moves to goals, judgment, taste, acceptance, risk, system
  design, and end-to-end ownership.

## Status Quo

What is already good:

- The strategic boundary is clear: do not build foundation models, generic RAG,
  AI middle-platform theater, or AI usage-rate management.
- The eight-step workflow has provenance and local evidence.
- The H5 contains real local failure cases: requirement drift, missing DB
  fields, visual acceptance failure, report-shape drift.
- Role language exists and is mostly directionally right.

What is not yet good enough:

- Role changes are repeated across sections instead of becoming one operating
  responsibility map.
- Section `13 · 角色变化` says what each role should guard, but not which
  eight-step node each role owns.
- The 30-day pilot checklist says what to check, but not what each role must do
  differently during the pilot.
- The role changes are still prose. They need to become "owner / artifact /
  evidence / stop doing" so teams can execute.
- Boss / management is under-specified. The page says management should not look
  at AI usage rate, but it should name decision rights: scope priority, release
  risk, metric interpretation, and trust boundary.

## Target Reader And Narrowest Wedge

Target reader:

- Our internal product, engineering, QA, project-management, and management
  stakeholders who need to know how their day-to-day job changes if this H5
  becomes the operating model.

Narrowest useful change:

- Add one new section or replace section `13 · 角色变化` with a concrete
  responsibility map:

  `岗位怎么变：8 步流程里的 owner、产物和证据`

This should be a role-action map, not a motivational paragraph.

## Premises

1. The current H5 does not need a new strategy. It needs sharper role execution
   mapping.
2. "产品是不是要写代码" is still the wrong question. For our system, the right
   question is "产品交付什么 artifact before Agent starts?"
3. The eight-step process is the spine. Role changes should hang from that
   spine, not appear as another detached role list.
4. The first pilot should not change every team ritual. It should change the
   responsibility chain for one real workflow: dashboard metric abnormality
   explanation and handling.

## What Needs To Change In The H5

### 1. Keep the eight-step process, but add role ownership

The H5 should explicitly map:

| Step | Primary Owner | Supporting Roles | Required Artifact | Completion Evidence |
|---|---|---|---|---|
| 意图包 | 产品 / PM | Boss, project | 用户原话、业务对象、动作、结果、非目标、验收路径 | Agent can restate the task without inventing scope |
| Spec / ADR 入口 | 研发组长 | 产品, QA, project | OpenSpec or ADR decision | Scope, non-goals, acceptance, risk are reviewable |
| Agent 执行包 | 研发工程师 | Agent, QA | diff, changed files, assumptions, tests, commands, risks | Reviewer can inspect both code and reasoning trail |
| 证据矩阵 | QA / 测试 | 研发, 产品 | unit / integration / real DB / browser / visual / permission evidence list | Evidence matches user path and risk level |
| Review Packet | 研发组长 or owner | 产品, QA, project | business mapping, diff summary, proof, screenshots/logs, open decisions | Human can decide without digging through chat |
| 人类判断 | Boss / owner | 产品, 研发, QA | approve / reject / defer decision | Decision and reason are written down |
| 失败写回 | Failure owner by category | affected role | test / ADR / ops / skill / checklist update | Same failure has a future trigger or check |
| 周度指标 | Boss / project | all owners | cycle, verification, rework, incidents, writeback trend | Management sees system health, not AI usage theater |

### 2. Replace vague role language with "stop / start / artifact"

The role section should say:

- Boss:
  - Stop: asking "AI usage rate high or low?"
  - Start: asking "which step is the bottleneck and which owner has unclear
    evidence?"
  - Artifact: weekly operating-system review.

- Product / PM:
  - Stop: handing off polished requirement summaries without user-original
    evidence.
  - Start: owning intent packet, non-goals, acceptance path, and scope tradeoff.
  - Artifact: intent packet and user-path acceptance examples.

- Engineering lead:
  - Stop: treating every request as a small implementation ticket.
  - Start: deciding Spec / ADR entry, decomposition, review packet standard, and
    rollback boundary.
  - Artifact: accepted spec, ADR, review packet template, execution boundary.

- Engineer:
  - Stop: using AI to produce code without explaining assumptions and evidence.
  - Start: submitting an execution packet: diff, assumptions, validation,
    risk, and not-done list.
  - Artifact: Agent execution packet.

- QA / test:
  - Stop: waiting for implementation completion before entering.
  - Start: defining the evidence matrix before or during execution.
  - Artifact: risk-based evidence matrix and replay cases.

- Project management:
  - Stop: reporting "doing / delayed / done" as the main state.
  - Start: tracking the eight-state workflow: intent captured, spec accepted,
    execution done, evidence ready, review packet ready, human judgment made,
    real environment verified, failure written back.
  - Artifact: operating state board and blocked-owner list.

### 3. Make the 30-day pilot role-specific

The existing pilot has a useful checklist, but it should show who changes what:

- Product chooses one metric-abnormality scenario and writes the first intent
  packet.
- Engineering lead decides whether it needs Spec / ADR and defines execution
  boundaries.
- Engineer uses Agent to build or repair the path, then submits execution
  packet.
- QA defines real DB / real API / browser / screenshot evidence.
- Project management tracks which state each task is in, not just date delay.
- Boss reviews weekly trend: fewer repeated failures, clearer owners, better
  evidence, not "more AI use".

### 4. Compress duplicate role sections

The H5 currently has role ideas in sections `06`, `08`, `13`, and `14`.

Recommended cleanup:

- Keep `06` as "what we can do".
- Keep `07` as the eight-step operating workflow.
- Keep `08` as old-to-new model.
- Rewrite `13` as the concrete role responsibility map.
- Keep `14` about writing process, but remove role overlap if it repeats the
  same "Who" logic.
- Keep `15` pilot, but add role-specific pilot behavior.

## Approaches Considered

### Approach A: Minimal Patch

Summary: Add a small paragraph under section `13` explaining that product does
not become a coder and each role owns evidence.

Effort: S

Risk: Low

Pros:

- Fastest and least disruptive.
- Good if the H5 only needs a light clarification.

Cons:

- It does not solve the scattering problem.
- The reader still has to infer owners and artifacts from multiple sections.

Reuses:

- Existing section `13 · 角色变化`.

### Approach B: Responsibility Map Replacement

Summary: Rewrite section `13 · 角色变化` into a role responsibility map, and
lightly update section `15 · 下一步` so the 30-day pilot assigns concrete role
actions.

Effort: M

Risk: Low to medium

Pros:

- Directly answers "我们的岗位需要变更什么".
- Keeps the current H5 strategy and visual structure intact.
- Turns role change from slogans into executable owner / artifact / evidence
  rules.
- Avoids pretending every role becomes a coder.

Cons:

- Requires tightening duplicated role language across sections.
- Needs careful layout so the H5 does not become a dense table report.

Reuses:

- Existing eight-step workflow.
- Existing section `13`.
- Existing 30-day pilot.
- Company-playbook role-change diagnosis stance.

### Approach C: Role-First Rewrite

Summary: Rewrite the back half of the H5 around Boss, product, engineering lead,
engineer, QA, project management, and knowledge owner.

Effort: L

Risk: Medium to high

Pros:

- Strong if the final goal is training material for the team.
- Most direct for people asking "what happens to my job?"

Cons:

- It would weaken the operating-system story.
- It may repeat company-playbook role content.
- It risks becoming a generic internal role manual instead of a report H5.

Reuses:

- Role diagnosis and article evidence matrix, but less of the current H5
  article structure.

## Recommendation

Choose Approach B.

Reason: the H5's spine is already right. The missing part is execution ownership.
Rewrite section `13` into a concrete role responsibility map, then make the
30-day pilot role-specific.

## Success Criteria

- A product reader can answer: "Before Agent starts, what exactly do I owe the
  workflow?"
- An engineering lead can answer: "Which work needs Spec / ADR, and what review
  packet standard am I enforcing?"
- An engineer can answer: "What is a complete Agent execution packet?"
- QA can answer: "Which evidence is required before we call this done?"
- Project management can answer: "Which state is blocked, and by which owner?"
- Boss can answer: "Which operating metric shows this system is improving?"

## The Assignment

Do not ask "which岗位要不要会写代码".

Ask this instead:

> For every step in the eight-step operating system, who owns the artifact, and
> what evidence proves the step is done?

If accepted, the next implementation should modify only:

- `wiki/reports/agentic-product-engineering-collaboration-our-operating-system.html`
- `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`
- `wiki/reports/agentic-product-engineering-collaboration-our-operating-system-share.zip`
