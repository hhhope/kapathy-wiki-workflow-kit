---
name: lore
description: >
  Use when the current directory is a software project and the agent needs
  project memory, historical pitfalls, cross-project engineering principles,
  or wiki-backed review workflows. Also use when handling knowledge upkeep
  tasks such as lore search, weekly review, code archaeology, or wiki lint.
---

# Lore

Persistent project memory for agentic coding teams.

**Core split:**
- **OpenSpec** owns change lifecycle: explore, propose, apply, archive
- **Lore** owns memory lifecycle: query, log, synthesize, lint, reuse

**Knowledge plane split:**
- **Lore** owns durable semantic memory: project context, boundaries, pitfalls, principles, and stable facts
- **Graphify** owns code-topology evidence: likely entry points, call neighbors, bridge nodes, and structural adjacency

**Core loop:** load current change + relevant memory → execute with self-check → record deviations → weekly review → wiki stays current

All paths come from the agent schema (`AGENTS.md` / `CLAUDE.md`). Never hardcode.

---

## Hard rules

- ❌ Skip health check on project work
- ❌ Start large execution without an approved OpenSpec change
- ❌ Treat Lore as the task-progress source of truth
- ❌ Decide change close, archive approval, or requirement completion
- ❌ Search only raw logs when wiki pages already exist
- ❌ Write directly to team-level knowledge without project evidence
- ❌ Use semantic matching as the only retrieval strategy
- ❌ Treat Graphify code adjacency as durable truth when Lore pages already define the rule or boundary
- ❌ Pull OpenSpec process tracking into the same retrieval layer as Lore or Graphify

---

## Lore owns

- Project overview and current engineering context
- Domain pages and pitfall pages
- Cross-project principles
- Deviation logs and weekly synthesis
- Code archaeology and unknowns capture
- Wiki health checks (`index`, links, stale pages, orphan pages)

## Lore does not own

- Requirement status
- Requirement completion state
- Task progress tracking
- Change close / archive approval
- Change archive / close workflow
- Change acceptance truth

Those belong to OpenSpec. `tasks.md` is the only task-progress truth source.

Graphify also does not own them. Graphify is a knowledge-plane helper for code structure, not a process-plane truth source.

---

## Recommended wiki shape

```text
wiki/
├── index.md
├── projects/
│   └── <project>/
│       ├── overview.md
│       └── domains/
│           └── <domain>.md
├── pitfalls/
│   └── <pitfall>.md
└── principles/
    └── <principle>.md
```

Use Obsidian as the human interface when available. The repository must still work as plain markdown + git.
Local execution `logs/` stay in the project repo, not in the shared wiki repo.

---

## Triggers

| Trigger | Lore action |
|---|---|
| Any project task | Health check + query relevant wiki pages |
| `lore: {keyword}` | Search `index.md`, then read target pages |
| rule / boundary / pitfall question | Route through Lore pages first |
| mixed rule + code question | Route through Lore first, then consult Graphify for structural evidence |
| `weekly review` | Convert logs into wiki updates |
| `code archaeology {path}` | Extract certain / uncertain knowledge |
| `lint lore` | Check index, links, stale claims, orphan pages |
| Large task finished with deviation | Generate log |

If the user asks to initialize or migrate the shared Lore Wiki itself, route to `lore-bootstrap` instead of continuing here.

---

## Phase 1 — Health check

Before project work:

1. Confirm `PROJECT.md` exists
2. Confirm local `logs/` backlog is not excessive
3. For large work, confirm an active OpenSpec change exists with:
   - `proposal.md`
   - `design.md`
   - `tasks.md`
4. Confirm `tasks.md` is the only execution-progress truth source

If step 3 fails, stop and route back to OpenSpec propose.

---

## Phase 2 — Task start

Read the minimum context set:

1. Current OpenSpec change docs (`proposal`, `design`, `tasks`)
2. `PROJECT.md`
3. `wiki/index.md`
4. Current project `overview.md`
5. One or two matching domain pages
6. One or two matching pitfall / principle pages

Prefer `index -> target page` navigation over broad grep on raw memory.
Prefer pages whose first screen already exposes operating sections such as `Scope`, `Applies When`, `Not For`, `Top Facts`, `Watchpoints`, and directional next-hop guidance.

Classify the question before deciding whether Graphify is needed:

- **Process-plane question**
  - use OpenSpec only
  - examples: proposal status, design scope, `tasks.md` progress
- **Lore question**
  - use Lore pages only
  - examples: which rule applies, which pitfall fits, what stable facts or boundaries matter
- **Graphify question**
  - use Graphify for code-topology evidence
  - examples: entry points, module neighbors, bridge nodes, likely call paths
- **Mixed question**
  - route to Lore first for scene and stable facts
  - then use Graphify to find the relevant code structure

**Retrieval rule:**
- Layer 1: index entry or filename suggests relevance
- Layer 2: page summary matches the task scene
- Layer 3: page boundary does not exclude the task

If no strong page matches, stay silent and continue with OpenSpec + `PROJECT.md`.

Target startup budget:
- P50: 3-4 pages
- P90: <= 6 pages

Graphify should not be consulted by default for every question. Use it when the task needs code structure, or when a mixed question needs structural follow-through after Lore has already identified the scene.

---

## Phase 3 — Execution with self-check

Before writing code, classify the task:
- Write operation
- External call
- DB operation

Then self-check:

**Write operation**
- Concurrent access handled?
- Lock strategy needed?
- Idempotent?

**External call**
- Timeout defined?
- Fallback defined?
- Allowed by project boundaries?

**DB operation**
- Known debt on affected tables?
- Missing fields or schema risks?

When new facts appear during execution:
- operational fact -> log it
- unresolved uncertainty -> `UNKNOWNS`
- stable reusable lesson -> promote during weekly review, not inline

---

## Phase 4 — Task complete

If a large task had corrections, follow-ups, or direction changes:
- deliver the result
- generate a log entry

Small task:
- deliver the result only

Log entries are event-layer artifacts. They are not the long-term retrieval layer.

---

## Phase 5 — Lore search

Trigger: `lore: {keyword}`

Workflow:
1. Search `index.md`
2. Return top candidate pages
3. Read only the most relevant pages
4. Respond with:
   - page
   - scope
   - one-line insight

If nothing matches:
- say so
- suggest adjacent domain or pitfall names

If the question is actually about code topology rather than durable rules or boundaries, say so and switch to Graphify instead of pretending the wiki should answer it.

---

## Phase 6 — Code archaeology

Trigger: `code archaeology {path}`

Workflow:
1. Read the target module
2. Output:
   - Certain: what the code demonstrably does
   - Uncertain: what cannot be justified yet
3. Convert stable findings into wiki draft updates
4. Convert unresolved items into `UNKNOWNS`

Do not turn guesses into wiki knowledge.
Do not turn Graphify adjacency into durable knowledge unless it is checked against code and then promoted through normal Lore review.

---

## Phase 7 — Weekly review

Trigger: `weekly review`

Workflow:
1. Read unreviewed logs
2. Decide for each log:
   - discard
   - absorb into project overview
   - absorb into a domain page
   - absorb into a pitfall page
   - absorb into a principle page
3. Update `index.md`
4. Mark the log as reviewed and record target pages
5. If a lesson is valid across projects, prepare promotion to shared/team lore

Weekly review must output concrete target-page updates or page diffs. Free-form prose summary alone is insufficient.
Weekly review should improve retrieval-first operating sections where possible:
- `Top Facts`
- `Watchpoints`
- `Applies When`
- `Not For`
- directional next-hop guidance

Do not treat prose-only append as sufficient durable promotion when the destination page still lacks a usable operating surface.

Weekly review must also report a metrics block. Minimum fields:
- reviewed logs count
- absorbed logs count
- discarded logs count
- `absorbed-to` completion rate
- absorption success rate for logs accepted into durable knowledge
- dominant destinations by page type: overview / domain / pitfall / principle

Scope rule:
- Weekly review owns event-layer closure and knowledge absorption quality
- Weekly review does **not** decide task completion, change close, or archive approval
- The weekly report is a Lore quality report, not an OpenSpec progress report

---

## Phase 8 — Lore lint

Trigger: `lint lore`

Check for:
- orphan pages
- stale summaries
- conflicting claims
- missing backlinks
- pages that should split because they are too large
- recurring log themes not yet reflected in wiki pages

Return findings first, then suggested updates.

---

## Acceptance checks

Use these as the first-pass TDD targets for the workflow:

- Large work without OpenSpec propose must be blocked
- Archive with unabsorbed logs must be blocked by the surrounding process
- Similar-task recall should be strong enough to be useful
- Irrelevant-page noise should stay controlled
- `log -> wiki` absorption should succeed reliably
- Task-start page load should stay within the context budget

Detailed validation assets:
- `references/TDD-SPEC.md`
- `references/PRESSURE-TEST.md`
- `references/BASELINE-RESULTS.md`
- `references/SKILL-EVAL.md`
- `evals/evals.json`
- `evals/MANUAL-RESULTS.md`
- `evals/COMMAND-RESULTS.md`
- `evals/PRESSURE-RESULTS.md`
- `evals/LIVE-AGENT-RETRIEVAL.md`
- `evals/LIVE-WEEKLY-REVIEW.md`
- `evals/LIVE-INTEGRATION-RESULTS.md`

Validation rule:
- fixture and manual walkthrough evidence are intermediate proof
- final rollout proof still requires a live agent run
