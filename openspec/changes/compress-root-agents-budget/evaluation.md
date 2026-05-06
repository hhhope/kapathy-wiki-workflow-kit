# Evaluation

## Baseline Scenarios

1. Archived `compress-codex-agents-md` ended with Pattern Catalog compliance
   but did not prove reduced drift from root context.
2. The first successor framing overfit to line count: extract `Global Rule
   Routing` into `~/.codex/rule-routing.md`, then load that file for
   non-trivial work.
3. That shape is fake progressive disclosure: file size drops, but default
   practical context for non-trivial work does not.
4. `~/.codex/AGENTS.md` is personal root guidance outside this repository's git
   tracking, so repo evidence must preserve before/after counts and scope.
5. External harness-engineering sources converge on a stronger target:
   root guidance should act as an agent-legible map backed by source-of-record
   artifacts, feedback loops, and recoverable progress state.

## Before Results

- File: `~/.codex/AGENTS.md`
- Baseline count at change start: 283 lines, 1865 words, 12459 bytes.
- `Global Rule Routing`: 30 lines, 313 words, 2733 bytes.
- `Global Rule Routing` share of root AGENTS: about 10.6% of lines, 16.8% of
  words, and 21.9% of bytes.
- Baseline support file: not present at change start.
- Baseline section mapping: pending implementation.

## Harness Engineering Gate

### RED Scenario

Move `Global Rule Routing` out of `~/.codex/AGENTS.md` into
`~/.codex/rule-routing.md`, then instruct root `AGENTS.md` to load that file
before non-trivial implementation or verification.

Expected result: **FAIL**.

Reason: `AGENTS.md` line count drops, but the dominant non-trivial path still
loads the moved text. The plan optimizes file appearance rather than loaded
context or drift prevention.

### GREEN Behavior

Root `AGENTS.md` retains always-on hard stops and routing principles. Task
details load only after a concrete trigger such as git boundary, skill
authoring, frontend work, migration work, or security-sensitive code.

Moving text to another file counts as reduction only when the moved text is no
longer loaded on the default path.

## External Article Calibration

The 2026-05-06 article pass changes the target from "compress root context" to
"make root context an agent-legible governance harness."

Local target criteria:

- **Map, not manual**: `AGENTS.md` points to source-of-record artifacts instead
  of inlining detailed knowledge.
- **Legible environment**: the agent can inspect the right repo-visible files,
  validation commands, and recovery notes without relying on chat memory.
- **Stable interfaces over stale assumptions**: root instructions should be
  hard stops, stable source pointers, trigger-gated detail, or candidate
  assumptions marked for review.
- **Feedback loop**: gather context -> act -> verify -> leave artifact.
- **Evaluation by outcome**: grade whether the agent finds the right source,
  verifies the intended behavior, and leaves recoverable state; do not require
  one exact path when multiple valid paths exist.

## Evidence Standard for Best Practices

Best practices are adoptable only when backed by one of these evidence shapes:

| Evidence shape | Required proof | What it can support |
|---|---|---|
| External documentation | URL, publish/access date when available, exact section or line reference, narrow claim boundary | Candidate or adopted principle when the claim is directly supported |
| Local demo / fixture | RED/GREEN scenario, input/output, command or manual replay record | Behavior claim about this repository or this agent workflow |
| Git-like project comparison | Repository, commit/path, and observable structure or behavior difference | Structural analogy or implementation pattern, not universal proof |

Practices without one of these evidence shapes stay as candidate observations.
They must not enter root `AGENTS.md`, spec `SHALL`, skill hard rules, or
archive-ready claims.

## Evidence-Backed Best Practice Table

Access date for web sources: 2026-05-06.

| Source | Evidence shape | Narrow supported claim | Local adoption boundary |
|---|---|---|---|
| OpenAI, `Harness engineering: leveraging Codex in an agent-first world`, `https://openai.com/index/harness-engineering/` L80-L91 | External documentation | `AGENTS.md` should be a map/table of contents, not a large manual; repository knowledge should be structured source-of-record content. | Adopt as target criterion: root `AGENTS.md` acts as map; details move only when they become inspectable source-of-record artifacts, not hidden default context. |
| OpenAI harness engineering L231-L239 | External documentation | Documentation alone is insufficient; strict boundaries and mechanical invariants prevent architectural drift. | Candidate for later automation only. This change may state the boundary, but no lint/checker is added. |
| OpenAI harness engineering L283-L290 | External documentation | Agents replicate existing patterns and drift accumulates; continuous cleanup beats periodic manual cleanup. | Adopt as residual-risk lens: root governance must avoid leaving attractive nuisance patterns; recurring cleanup automation is out of scope. |
| Anthropic, `Scaling Managed Agents`, `https://www.anthropic.com/engineering/managed-agents` L17-L25 | External documentation | Harnesses encode assumptions that can go stale; stable interfaces should outlast implementation details. | Adopt as classification rule: retained root instructions must be hard stops, stable source pointers, trigger-gated detail, or candidate assumptions. |
| Anthropic Managed Agents L35-L43 | External documentation | Decoupling session, harness, and sandbox makes failures recoverable and keeps credentials out of generated-code sandboxes. | Use as analogy only: root governance should preserve recovery artifacts and source pointers. No sandbox/tool architecture change in this repo. |
| Claude, `Common workflow patterns for AI agents`, `https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them` L278-L299 | External documentation | Workflows shape agent autonomy with checkpoints and boundaries; start with the simplest workflow and upgrade only when measurable need exists. | Adopt: current change stays sequential; no parallel agents or evaluator-optimizer loop unless a later measurable quality gap justifies it. |
| Claude, `Building agents with the Claude Agent SDK`, `https://claude.com/blog/building-agents-with-the-claude-agent-sdk` L380-L388 | External documentation | Improve agents by studying failures and asking whether they have the right information, rules, tools, or eval set. | Adopt: root rewrite must be justified by a local failure mode and verification method, not a generic best-practice appeal. |
| Anthropic, `Harness design for long-running application development`, `https://www.anthropic.com/engineering/harness-design-long-running-apps` L31-L47 | External documentation | Separate generator and evaluator roles; grade against explicit criteria, especially for subjective quality. | Candidate only for future review/evaluator loops. This change only records criteria; it does not add a separate evaluator agent. |
| Anthropic harness design L115-L122 | External documentation | Evaluator logs and granular criteria make failures actionable, but evaluator judgment needs tuning against human judgment. | Adopt as evaluation-quality warning: RED/GREEN must state why failure is fair; no claim of automated evaluator reliability. |
| Anthropic, `Demystifying evals for AI agents`, `https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents` L202-L211 | External documentation | Agent evals should check outcomes in real/sandboxed environments and choose tools based on task context. | Candidate for future runtime proof. Current root-context change uses document/manual evidence only. |
| Anthropic evals L244-L263 | External documentation | Eval environments should be isolated; graders should prefer outcome grading, partial credit, and transcript review. | Adopt: evaluate whether the agent finds the right source, verifies behavior, and leaves recovery evidence; do not require one exact path. |
| Anthropic, `Effective harnesses for long-running agents`, `https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents` L73-L101 | External documentation | Long-running agents need startup bearings, progress artifacts, basic tests before new work, and session-end progress updates. | Adopt as agent-legibility criterion: next agent must know where to read, how to verify, and what artifact preserves recovery. |
| Anthropic, `A diff tool for AI`, `https://www.anthropic.com/research/diff-tool` L18-L23 and L67-L69 | External documentation | Traditional evals catch known risks; diffing helps surface behavioral differences rather than auditing everything from scratch. | Adopt as comparison principle: review changed behavior and evidence deltas, not the whole governance corpus from scratch. |

## After Results

- File: `~/.codex/AGENTS.md`
- After count: 271 lines, 1750 words, 11812 bytes.
- Delta: -12 lines, -115 words, -647 bytes from the 283-line baseline.
- Target files edited: `~/.codex/AGENTS.md` only.
- Root-local support file: none added.
- `Global Rule Routing`: not extracted; no `~/.codex/rule-routing.md` file was
  created, so no hidden default-loaded support file was introduced.

## Loaded-Context Evidence

| Metric | Before | After | Result |
|---|---:|---:|---|
| Default loaded context | `~/.codex/AGENTS.md`: 283 lines / 1865 words / 12459 bytes | `~/.codex/AGENTS.md`: 271 lines / 1750 words / 11812 bytes | Reduced by consolidating duplicate execution/git wording |
| Triggered loaded context | Task-specific rule / skill files load only after the `Global Rule Routing` table matches a concrete trigger | Same trigger model; no new default-loaded support file | Preserved |
| Fake progressive disclosure | Proposed `rule-routing.md` on the default non-trivial path would fail | No support file added; routing table remains explicit in root | Avoided |

## Section Mapping

| Before section | After section | Change | Preserved behavior |
|---|---|---|---|
| `Execution discipline` + `Git discipline` | `Execution and git discipline` | Consolidated duplicated dirty-tree, commit, branch, resume, push, and truth-source wording | Preserve unrelated changes, avoid destructive git, commit verified task-related files, branch off `main`, verify status/log before git claims |
| `Global Rule Routing` | `Global Rule Routing` | Unchanged | Triggered references remain visible; no deferred routing-table rows were pulled into scope |

## Agent-Legibility Check

| Question | Result | Evidence |
|---|---|---|
| Where should the next agent read? | pass | Root `AGENTS.md` still points to `PROJECT.md`, OpenSpec change docs, wiki entry pages, and triggered rules / skills |
| How should the next agent verify? | pass | Root `AGENTS.md` requires fresh `git status --short` and `git log -1 --oneline`; this change also validates with `openspec validate compress-root-agents-budget --strict` |
| Which artifact preserves recovery? | pass | This `evaluation.md`, `tasks.md`, git history, and any later `archive-review.md` preserve the root edit evidence because `~/.codex/AGENTS.md` is outside repo tracking |

## Behavior Pressure Check

| Scenario | Old wording result | New wording result |
|---|---|---|
| Dirty repo with unrelated report changes plus task-related OpenSpec edits | Required preserving unrelated changes, committing task-related files, and verifying status/log, but split the same behavior across two overlapping sections | Same required behavior is present in one section; no behavior weakened |
| Agent wants to claim `already committed` after interruption | Blocked by git truth-source text | Still blocked: fresh `git status --short` and `git log -1 --oneline` are required before git-based completion claims |
| Current branch is `main` and user asks for feature work | Blocked until a feature branch is created | Still blocked until a feature branch is created |

## Self-Check

| Column | Result | Evidence |
|---|---|---|
| Structural | pass | `openspec validate compress-root-agents-budget --strict` returned valid on 2026-05-06 |
| Semantic | pass | Target remains Root AGENTS; support files are allowed only as trigger-gated references |
| Evidence | pass | Baseline and after counts, loaded-context metrics, RED/GREEN gate, article calibration, evidence standard, source-backed best-practice table, section mapping, and agent-legibility check are recorded |
| Boundary | pass | No new Pattern Catalog pattern, checklist item, skill, wiki method page, or repo policy introduced |

## Residual Risks

- `~/.codex/` is outside this repository's git tracking.
- A support file can become hidden default context if root `AGENTS.md` points to
  it too broadly.
- Line count can still be useful supporting evidence, but it can no longer be
  treated as the primary success metric.
- The consolidation is a modest reduction, not a full root rewrite; larger
  reductions still need a future scoped change with measured trigger behavior.
