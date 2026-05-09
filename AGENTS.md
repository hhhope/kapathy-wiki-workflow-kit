# Repo Instructions

This file adds repository-specific constraints for `report-wiki-portfolio`.
Global/root instructions still own health checks, git truth-source checks, and
general execution discipline. This file owns repo-local workflow gates, routing
defaults, and delivery boundaries.

## Scope

- Repository-default collaboration policy belongs in this repo first, not in
  global instructions by default.
- Only promote a policy to global guidance when it has been shown to generalize
  beyond this repository's material-processing workflow.
- Active OpenSpec change artifacts own current scope, task progress, and
  interruption checkpoints.
- `wiki/adr/` owns stable cross-change decisions.

## Workflow Change Gate

- Treat changes to repository-default workflow, collaboration behavior, routing
  defaults, escalation boundaries, or default output rules as OpenSpec-level
  changes.
- For these changes, create or select an active OpenSpec change before editing
  `wiki/`, `scripts/`, `skills-drafts/`, `.codex/skills/`, or other repository
  guidance files.
- Do not ship temporary wiki-only or skill-draft-only fixes first and backfill
  OpenSpec later.
- If the user asks to change how Codex should usually behave in this repository,
  assume it is a workflow change unless the request is explicitly limited to one
  page or one one-off run.

Sources: `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`,
`wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`.

## Repo AGENTS Governance Gate

- For repo-level `AGENTS.md` governance work, treat migration as a phased
  workflow rather than an immediate edit target.
- Phase 0 means: accept the repo-level gate, fix repo-local governance identity
  conflicts, and publish the minimum blocking wording.
- Phase 1 means: later compression, proxy migration, or structural rewrite of
  repo `AGENTS.md`.
- Do not start Phase 1 from candidate wiki guidance alone. A repo-visible
  accepted mainline must exist first.
- Root-level `~/.codex/AGENTS.md` and `~/.claude/CLAUDE.md` are related but out
  of scope by default for repo Phase 0 or Phase 1 work.
- Before Phase 1 migration begins, the repository must have:
  - an accepted repo-visible Phase 0 mainline
  - no duplicate ADR numbering affecting current governance references
  - an explicit repo-local commit-gate decision
- Current commit-gate decision: repo-local commit hooks are not part of the
  default governance path; reversal requires a new OpenSpec change.

Sources: `wiki/adr/0027-repo-phase0-before-repo-agents-migration.md`,
`wiki/adr/0030-no-repo-local-commit-hook-default.md`,
`openspec/specs/repo-agents-governance-phase0/spec.md`,
`openspec/specs/no-repo-local-commit-hook-default/spec.md`.

## Hard Stops

| Situation | Required behavior | Source |
|---|---|---|
| Active OpenSpec change reaches `all_done` or all checkboxes are complete | Stop implementation. Default next action is archive review, not more implementation or immediate archive. | `wiki/adr/0007-archive-review-before-archive.md`, `openspec/specs/archive-review-defaults/spec.md` |
| Archive review finds a routine closing tail | Keep the blocker visible in `tasks.md` and record the reason and next action in git history. | `openspec/specs/archive-review-defaults/spec.md` |
| Archive review depends on scope ambiguity or reusable governance judgment | Add `archive-review.md` inside the current change directory. | `openspec/specs/archive-review-defaults/spec.md` |
| `$openspec-explore` is used in this repo | Before exploration continues, create or update a lightweight repo-visible trace in `wiki/ops/`. | `wiki/adr/0009-explore-trace-before-openspec-explore.md`, `openspec/specs/openspec-explore-wiki-trace/spec.md` |
| Live conversation shows drift from the last confirmed requirement | Stop continuation, re-anchor, and update a repo-visible `wiki/ops` retro unless the disagreement is already resolved in the active change. | `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`, `openspec/specs/live-conversation-reanchor-gate/spec.md` |
| External article, README, repo, or in-chat example looks useful | Capture as learning only; do not promote into `AGENTS.md`, spec `SHALL`, skill hard rule, or archive-ready claim without evidence. | `openspec/specs/example-driven-wiki-capture/spec.md`, `openspec/specs/article-learning-capture/spec.md` |
| Semantic edits to `.codex/skills/*` | Include `evaluation.md` with behavior proof and load the writing/TDD skill guidance. | `openspec/specs/skill-authoring-contract/spec.md`, `openspec/specs/skill-evaluation-evidence/spec.md`, `openspec/specs/local-skill-pressure-tests/spec.md` |
| Material-processing output | Produce readable `wiki/sources` output first, then linked `wiki/ops` output when the material contains action signals. | `.codex/skills/material-collaboration-defaults/SKILL.md` |
| Meeting-note output | Produce a review version first; do not publish or sync final notes while confirmation items remain unresolved. | `.codex/skills/meeting-note-output/SKILL.md` |

## Behavior Replay Gate

- When a change, completion claim, or governance artifact says a runtime
  behavior will trigger, stop, route, reject, or persist differently in future
  sessions, include behavior replay evidence before treating the claim as
  complete or archive-ready.
- Minimum evidence: input or situation shape, trigger condition, expected route
  or stop behavior, repo-visible artifact a future agent should read, expected
  output or non-output, promotion or non-promotion boundary, and residual risk
  or proof boundary.
- Applies to semantic skill trigger changes, repo `AGENTS.md` runtime triggers,
  OpenSpec hard stops, archive / re-anchor / explore gates, link-learning
  trigger replay, and claims such as "next time this will happen".
- Does not apply by default to one-off analysis, candidate learning notes,
  source summaries, ordinary wiki capture, or exploratory thinking that does not
  claim future runtime behavior.
- Specialized gates such as skill-evaluation evidence, local pressure tests,
  link-trigger replay, disagreement replay, and re-anchor replay can satisfy
  this gate when they preserve the minimum evidence and proof boundary.

Sources: `openspec/specs/behavior-replay-gate/spec.md`,
`wiki/ops/behavior-replay-gate.md`.

## High-Frequency Skills

Use these repo-local principle skills when the request or implementation scope
matches. They complement repo governance; they do not replace OpenSpec gates.
This is a runtime routing map, not an ownership map.

| Situation | Load | Ownership |
|---|---|---|
| External articles, repos, READMEs, or examples used as learning, reference, or adaptation material | `.codex/skills/learning-capture/SKILL.md` | shared: root-candidate learning core; repo-owned output routing |
| Material, reports, attachments, preview HTML, or source files | `.codex/skills/material-collaboration-defaults/SKILL.md` | repo-owned |
| Reader-facing reports, Feishu review drafts, H5/share drafts, public materials, or reference-shaped outputs | `.codex/skills/public-report-quality-gate/SKILL.md` | repo-owned reader-facing output gate |
| Meeting notes, transcripts, minutes, or Feishu meeting-note output | `.codex/skills/meeting-note-output/SKILL.md` | repo-owned |
| Implementing an OpenSpec change | `$openspec-apply-change` (source: `plugins/report-wiki-portfolio/skills/openspec-apply-change/SKILL.md`) | shared: OpenSpec lifecycle with repo gates |
| Archiving an OpenSpec change | `$openspec-archive-change` (source: `plugins/report-wiki-portfolio/skills/openspec-archive-change/SKILL.md`) | shared: generic archive action with repo review detail |
| Exploring ideas or clarifying requirements with `$openspec-explore` | `$openspec-explore` (source: `plugins/report-wiki-portfolio/skills/openspec-explore/SKILL.md`) | shared: explore stance with repo trace gate |
| Creating a new OpenSpec proposal | `$openspec-propose` (source: `plugins/report-wiki-portfolio/skills/openspec-propose/SKILL.md`) | shared |
| Ambiguous request before silently choosing a scope | `.codex/skills/clarify-before-acting/SKILL.md` | root-candidate |
| Speculative abstractions or future-proofing are growing | `.codex/skills/simplicity-first/SKILL.md` | root-candidate |
| Narrow edit risks expanding into adjacent cleanup | `.codex/skills/surgical-changes/SKILL.md` | root-candidate |
| About to claim complete/fixed/synced without fresh evidence | `.codex/skills/verify-before-claiming/SKILL.md` | root-candidate; partly covered by root git truth-source |

## Skill Authoring Contract

- Repo-local `.codex/skills/*` files are English-first behavior assets. Do not
  let the wiki's Chinese-first policy bleed into `SKILL.md`.
- Keep repo-local `SKILL.md` files compact. Put only trigger conditions, hard
  rules, anti-patterns, and short loading pointers in the main body.
- Move long examples, templates, or heavy format details into linked
  `references/` files when they would bloat trigger-time retrieval.
- Before authoring or editing a repo-local skill, read this repo `AGENTS.md` and
  any repo pages that define delivery boundaries for that workflow.
- If a skill affects Feishu-facing, reader-facing, or other delivery-sensitive
  outputs, make the repo boundary explicit in the skill or reference the
  governing repo document directly.
- Semantic skill changes must include local pressure-test evidence in
  `evaluation.md`: `Pressure Scenarios`, `RED Baseline`, `GREEN Result`, and
  `Residual Risks`.
- Multi-end or rollout proof is optional follow-up evidence, not the minimum
  completion gate for a semantic skill change.

Sources: `openspec/specs/skill-authoring-contract/spec.md`,
`openspec/specs/skill-evaluation-evidence/spec.md`,
`openspec/specs/local-skill-pressure-tests/spec.md`.

## Output Routing

- Raw upstream material belongs in `wiki/sources`.
- Workflow, governance, operating learnings, traces, and retros belong in
  `wiki/ops`.
- Validated output-shape examples belong in `wiki/examples`.
- Stable cross-change decisions belong in `wiki/adr`.
- Scoped repository-default behavior changes belong in an OpenSpec change.
- Public-facing repo artifacts such as README, docs, examples, or published
  templates belong in that target repo when that repo is the active work target;
  this wiki records internal learning and evidence, not every public artifact.

External link routing:

- A link by itself does not require a wiki page.
- If the discussion extracts reusable learning, create or update a repo-visible
  wiki record in the same turn.
- Minimum record fields: time, source reference, what was reused, what was
  modified, what was not formalized, repo target, and next step.
- Unsupported learning stays a `candidate observation`.

Sources: `openspec/specs/example-driven-wiki-capture/spec.md`,
`openspec/specs/article-learning-capture/spec.md`,
`openspec/specs/learning-capture-routing/spec.md`,
`wiki/ops/example-driven-wiki-capture.md`,
`wiki/ops/learning-capture-routing.md`.

## Conversation Governance

- Handoff mode starts when the live conversation repeatedly converges on the
  same north-star goal. Preserve north star, constraints, failure modes,
  preferences, disagreements, open questions, candidate practices, and repo
  targets. Do not auto-edit behavior assets directly from conversation state.
- Disagreement that is still calibrating the goal stays as calibration material
  first. Preserve rejected framing, correction pressure, redirection moment,
  current clarity state, and protected target before promotion.
- First positive naming is valid only after the rejected object stabilizes and
  redirection has occurred.
- Live re-anchor is mandatory when continuation may now mean a materially
  different next step.

Sources: `openspec/specs/conversation-north-star-handoff/spec.md`,
`wiki/ops/conversation-handoff-mode.md`,
`openspec/specs/disagreement-management-method/spec.md`,
`wiki/ops/disagreement-management-method.md`,
`openspec/specs/live-conversation-reanchor-gate/spec.md`.

## Wiki Runtime Stack

The long wiki runtime chain is governed by stable source records. Do not
restate the full model here, and do not overclaim runtime autonomy from these
structural proofs.

| Layer | Use | Sources |
|---|---|---|
| Naming model | Name new evolution-bearing pages by canonical object and artifact type. | `openspec/specs/wiki-naming-model/spec.md`, `wiki/ops/agent-readable-wiki-naming-model.md`, `wiki/adr/0013-agent-readable-wiki-naming-before-graph-growth.md` |
| Frontmatter model | Add minimal graph-ready fields to covered new pages. | `openspec/specs/wiki-frontmatter-model/spec.md`, `wiki/ops/agent-readable-wiki-frontmatter.md`, `wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md` |
| Graph extraction | Extract structural nodes and relations only. | `openspec/specs/wiki-graph-extraction/spec.md`, `wiki/ops/agent-readable-wiki-graph-extraction.md`, `wiki/adr/0015-agent-readable-wiki-graph-extraction-after-structure.md` |
| Relation analysis | Summarize object coverage and unresolved structure without semantic invention. | `openspec/specs/wiki-relation-analysis/spec.md`, `wiki/ops/agent-readable-wiki-relation-analysis.md`, `wiki/adr/0016-agent-readable-wiki-relation-analysis-after-extraction.md` |
| Semantic scoring | Score explicit canonical objects with audit-friendly factors; no embeddings or hidden guesses. | `openspec/specs/wiki-semantic-scoring/spec.md`, `wiki/ops/agent-readable-wiki-semantic-scoring.md`, `wiki/adr/0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md` |
| Utilization layer | Classify objects into explicit usage bands with caution reasons. | `openspec/specs/wiki-utilization-layer/spec.md`, `wiki/ops/agent-readable-wiki-utilization-layer.md`, `wiki/adr/0018-agent-readable-wiki-utilization-layer-after-semantic-scoring.md` |
| Runtime context | Bundle preferred, supporting, blocked, and caution context. | `openspec/specs/wiki-runtime-context/spec.md`, `wiki/ops/agent-readable-wiki-runtime-context.md`, `wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md` |
| Source integration | Resolve only repository-local sources from covered layers. | `openspec/specs/wiki-runtime-context-source-integration/spec.md`, `wiki/ops/agent-readable-wiki-runtime-context-source-integration.md`, `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md` |
| Runtime auto routing | Produce `open_first`, `open_next`, and `do_not_open_first` from source-integrated context. | `openspec/specs/wiki-runtime-auto-routing/spec.md`, `wiki/ops/agent-readable-wiki-runtime-auto-routing.md`, `wiki/adr/0021-agent-readable-wiki-runtime-auto-routing-after-source-integration.md` |
| Context injection | Inject bounded excerpts from runtime auto-routing output. | `openspec/specs/wiki-context-injection/spec.md`, `wiki/ops/agent-readable-wiki-context-injection.md`, `wiki/adr/0022-agent-readable-wiki-context-injection-after-runtime-auto-routing.md` |
| Self-directed execution | Map injected context to bounded `execute_now`, `defer_for_followup`, and `do_not_execute` actions. | `openspec/specs/wiki-self-directed-execution/spec.md`, `wiki/ops/agent-readable-wiki-self-directed-execution.md`, `wiki/adr/0023-agent-readable-wiki-self-directed-execution-after-context-injection.md` |

## Delivery Workflows

Material processing:

- Formal workflow publication uses
  `.codex/skills/material-collaboration-defaults/SKILL.md`.
- `skills-drafts/` is draft space only; workflow changes cannot stop with an
  active draft `SKILL.md`.
- Before a workflow-level skill change is complete, every draft skill must be
  either promoted into `.codex/skills/` or explicitly retired.
- When the user drops materials and asks Codex to process them, do not stop at
  placeholder intake output.
- Default completion means readable `wiki/sources` output first, then linked
  `wiki/ops` output when the material contains action signals.
- Ask the user only at real output fork-points, such as whether to update
  `html/h5/preview` artifacts in addition to wiki records.

Meeting-note output:

- Formal workflow publication uses `.codex/skills/meeting-note-output/SKILL.md`.
- `skills-drafts/meeting-note-output/` is draft space only; it does not count as
  a formally published repo skill.
- Manual agent role templates are not a substitute for meeting-note workflow
  routing.
- When handling meeting notes or transcripts, use the repository's fixed
  meeting-note format rather than a generic summary layout.
- The main meeting-note output must include: meeting metadata, core agenda,
  numbered topic sections, explicit final/rejected options when applicable, a
  structured action-item table, and a closing summary.
- Treat note text as the primary output and transcript text as supporting
  evidence for disputes or rationale.
- Default to a review version first. Review versions must include `待确认` and
  `需你澄清`.
- Do not publish or sync a final Feishu meeting note until unresolved
  confirmation items are either answered or explicitly marked as pending.
