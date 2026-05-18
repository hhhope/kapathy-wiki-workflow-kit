---
title: evolver-self-evolving-harness / reading-notes
type: learning
canonical_object: evolver-self-evolving-harness
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
domain: agent-harness
layer: ops
ops_area: learning-capture
status: active
confidence: candidate
updated_at: 2026-05-08
ai_generated: true
derived_from:
  - https://mp.weixin.qq.com/s/L8H0Kl0ecXOk7yTwpI7RTA
related_objects:
  - account-knowledge-base
  - public-report-quality-gate
  - agent-harness-article-learning
notes_scope: Source-grounded article learning. This page records scoring,
  transferable learning, and promotion boundaries; it does not directly create
  AGENTS, skill, spec, or policy changes.
---

# Evolver Self-Evolving Harness / Reading Notes

## Source

| Field | Value |
|---|---|
| Title | Evolver 拆解：一个让 Agent 自己演化自己的 Harness |
| URL | https://mp.weixin.qq.com/s/L8H0Kl0ecXOk7yTwpI7RTA |
| Author / Publisher | 克熵Sam |
| Published At | 2026-03-17 |
| Accessed At | 2026-05-08 |
| Source Type | WeChat article |
| Retrieval Method | `weixin-reader` script; first sandbox run failed, escalated Playwright run succeeded |
| Source Class | secondary interpretation + structure reference |
| Source Artifact Type | extracted markdown in session; durable page stores source map and paraphrased notes only |
| Source Artifact Path / Note | Full article text is not stored to preserve copyright boundary |

## Source Grounding Map

Copyright boundary: this page does not preserve the full article text or a full
translation. It keeps only a source map and paraphrased learning notes.

| Article Section | Source Map | Why It Matters |
|---|---|---|
| Opening problem | Starts with whether an agent can inspect its own logs, find error patterns, and patch itself. | Useful as a strong problem-first opening pattern. |
| Evolver problem statement | Frames the cost of manual prompt tuning loops. | Useful for explaining why governance cannot depend on human memory alone. |
| Signal extraction / anti-stagnation | Discusses recurring errors, missing memory, capability gaps, tool overuse, repair loops, and forced strategy switches. | Useful as evidence style for observable failure signals and anti-loop design. |
| Memory graph | Describes a chain from signal to hypothesis, attempt, and outcome. | Useful as a structure analogy for our gate-review and replay artifacts. |
| Blast-radius and solidify | Describes max file limits, forbidden paths, validation commands, canary checks, and rollback. | Useful as a boundary pattern: improvement needs bounded impact and verification. |
| Judgment section | Separates what looks strong from two concerns about gene quality and personality parameter drift. | Useful for public writing: conclude with balanced adoption boundaries, not pure praise. |

## Admission Gate

| Gate | Result | Reason |
|---|---|---|
| Source access | PASS | Original URL and fetched markdown are available in the session. |
| Source class recorded | PASS | Classified as secondary interpretation and structure reference. |
| Source grounding preserved | PASS | This page records source map and paraphrased notes. |
| Local objective exists | PASS | The user provided the article as another reference before writing a Feishu-facing draft. |
| Copyright boundary workable | PASS | Durable notes avoid full verbatim article storage or full translation. |

## Score

Score timing: retrospective. The fetch command returned the full article body
before the durable score record was written, so this score is audit evidence for
current use, not proof that admission happened before any reading.

| Criterion | Score | Reason |
|---|---:|---|
| Source access and provenance | 20 / 20 | URL, author, date, access date, and retrieval method are recorded. |
| Evidence or method density | 22 / 25 | The article contains concrete harness mechanisms, but it is not the primary project source. |
| Local capability gain | 23 / 25 | It directly improves how we write about runtime signals, replay, bounded change, and evidence boundaries. |
| Transfer path | 14 / 15 | Maps cleanly into the public report reviewer and learning-use map. |
| Verification path | 11 / 15 | Can be verified by checking the final draft for problem-first structure, signal tables, visual roles, and non-claims; technical facts still need primary-source verification. |
| Raw total | 90 / 100 |  |
| Final total | 78 / 100 | Capped because this is secondary interpretation and structure reference, not primary technical evidence. |

Decision: deep-read for structure, visual, evidence, and boundary transfer.
Do not use it as sole proof of the Evolver project implementation.

## Reading Draft

### Problem

The article asks whether agent improvement can move from manual prompt tuning to
a repeatable harness loop: inspect logs, extract signals, choose a strategy,
patch behavior, validate, and preserve successful experience.

### Method / Architecture / Process

The useful process shape is:

```text
runtime traces
  -> signal extraction
  -> strategy / gene selection
  -> mutation or patch
  -> solidify validation
  -> outcome memory
  -> future strategy advice
```

For our writing work, this is not a system to copy directly. It is a pattern for
showing that a knowledge system needs:

- observable signals, not vague feelings
- anti-loop handling when the same failure repeats
- bounded change size
- validation before promotion
- memory of failed and successful attempts

### Evidence Type

The article is a secondary technical teardown with screenshots and project-level
implementation descriptions. It is useful for method framing and writing
structure, but promotion of any technical claim requires checking the original
project or local replay.

### Applicability Conditions

Applicable when a draft needs to explain:

- why repeated agent failures should become observable signals
- why self-improvement needs gates and rollback
- why learning artifacts should record attempt/outcome, not only conclusions
- why future automation must be bounded by evidence and blast radius

### What It Does Not Prove

- It does not prove Evolver's implementation quality in this repo.
- It does not prove we should build an automated self-evolution daemon.
- It does not justify automatic promotion into `AGENTS.md`, specs, or skills.
- It does not provide local metrics for our Account Harness Wiki draft.

## Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
| Opening and problem statement | Start with a concrete system question before architecture. | The article opens by asking whether self-patching agents can be engineered. | Use for the Account Harness Wiki opening: begin with daily behavior becoming a reusable, verifiable system. | Do not copy the topic; reuse the problem-first move. | accepted |
| Signal extraction section | Repeated failures should become named, counted signals. | Article lists recurring errors, missing memory, tool overuse, capability gaps, and stagnation signals. | Use in validation/cases page to make drift, failed drafts, missing template choice, and false scores observable. | Local signal names must come from our own gate-review history. | candidate |
| Anti-stagnation mechanism | Repeating the same repair loop should force a strategy change. | Article describes suppressing frequent repeated signals and switching strategy after failures. | Use as writing evidence style for why reviewer routing exists: it interrupts repeated draft-repair loops. | Do not claim automated loop-breaking exists here. | candidate |
| Memory graph | Attempt/outcome history is more useful than raw transcript memory. | Article frames SignalSnapshot -> Hypothesis -> Attempt -> Outcome. | Use as analogy for why gate-review artifacts must preserve failed drafts, decisions, and residual risks. | Keep as analogy; no graph automation claim. | accepted |
| Solidify and blast radius | Any self-improvement needs bounded scope and validation before persistence. | Article describes max file limits, forbidden path checks, validation, canary checks, and rollback. | Use in boundary sections: changes to behavior assets require gates, replay, and scoped promotion. | Do not imply our process has automatic rollback beyond git/manual checks. | accepted |
| Judgment section | Useful references should end with concerns and non-claims. | Article names concerns about gene quality and parameter drift. | Use in public report ending: distinguish current capability, next step, and what is not proven. | Concerns must be local, not copied from Evolver. | accepted |

## Output-Use Handoff

| Learning artifact | Domain / topic | Capability type | Learning point | Intended output use | Skip reason |
|---|---|---|---|---|---|
| This page | self-evolving agent harness | `structure` | Problem-first opening, then mechanism teardown, then judgment. | Candidate template for the next Feishu draft if user chooses the "problem-led teardown" template. | None if that template is selected. |
| This page | self-evolving agent harness | `visual` | Each major mechanism benefits from a visual/table that carries a relationship, not decoration. | Require each Account Harness Wiki section to have a diagram/table role before final draft. | None; final image assets may still be deferred. |
| This page | self-evolving agent harness | `evidence` | Observable signals and attempt/outcome records make improvement auditable. | Use in validation/cases page and overview evidence table. | Do not invent local metric values. |
| This page | self-evolving agent harness | `boundary` | Secondary teardown can shape writing, but cannot prove technical facts or local automation. | Add non-claim section: no self-evolution daemon, no automatic promotion, no unverified metrics. | None. |

## Rejected Moves

- Do not copy the article's Evolver technical claims into the Account Harness
  Wiki as if they were local facts.
- Do not use the article to justify automatic updates to `AGENTS.md`, specs, or
  skills.
- Do not present the current repo as having automated signal suppression,
  canary rollback, or cross-agent capsule sharing.

## Next Action

Use this as a writing/reference input in
`wiki/ops/team-knowledge-base-overview-report-gate-review.md` before the next
Feishu draft. The next gate must choose a template before writing.
