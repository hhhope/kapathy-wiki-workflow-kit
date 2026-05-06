## Confirmed Problem

The last confirmed requirement is to repair
`decide-root-governance-alignment` into a reviewable design state. This step is
not root dotfile implementation, skill authoring, wiki method publication, or
runtime enforcement.

The current problem is not just that root governance files differ. The larger
problem is that behavior assets are mixed together:

- root and repo `AGENTS.md` files contain routing, hard stops, repo policy,
  workflow history, and sometimes stable decisions in the same surface
- rules and skills are both treated as behavior constraints, but their trigger
  models differ
- OpenSpec owns lifecycle, but chat-level plans can still be mistaken for
  permission to edit root behavior assets
- wiki, ADR, and retro pages preserve durable learning, but the landing route is
  sometimes decided after the fact
- harness language was ambiguous enough to sound like a new enforcement system
  instead of evidence for review

Drift judgment: the previous draft drifted by using decision language before
the alignment model was accepted, and by describing `harness` too broadly. This
repair must separate accepted boundaries, proposed design, and still-open
decisions.

## Confirmed Boundaries

- SDD-first: root dotfile, skill, rule, or wiki method changes must not happen
  from a chat-level plan alone. The active OpenSpec change must record the
  boundary, evaluation evidence, and open decisions first.
- Wiki-gated: wiki may preserve learning or calibration material, but it is not
  the default landing place for method pages or ADRs before the active design
  boundary is accepted.
- Root files are out of scope for this step: do not edit `~/.codex/AGENTS.md`,
  `~/.claude/CLAUDE.md`, repo-local skills, root rules, or wiki method pages.
- Harness v1 is evidence only. It is not a hook, CI gate, runtime gate, or
  automatic compliance mechanism.

## Benchmark Signals

External references are benchmark inputs, not imported policy. Each source
below is tagged with a verification class; principles and the Pattern
Catalog only rely on class A and class B sources. Class C sources are
recorded as background vocabulary, not as evidence supporting any
candidate rule.

Full URL list for every class A and B source is consolidated in
`wiki/ops/behavior-asset-governance-design-trace.md` §10 External
Provenance.

**Class A — Anthropic-normative (directly cited)**

- Anthropic Agent Skills engineering post (2025-10):
  `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills`
  — progressive disclosure, dynamic loading, code-as-documentation.
- anthropics/skills README:
  `https://github.com/anthropics/skills` — `SKILL.md` frontmatter
  contract.

**Class B — fact-checked in `codex-global-agents-md` intake §3 (2026-04-29)**

- GitHub Blog "how to write a great agents.md" 2,500+ repos study:
  six core areas (commands / testing / project structure / code style /
  git workflow / boundaries); no line-count recommendation is present
  in the post.
- arXiv 2602.11988 — context files increase inference cost by an average
  of 20% / 23% on SWE-bench Lite / AGENTbench for LLM-generated context;
  at most 19% for developer-provided context.
- skyzyx instruction-budget gist, citing Humanlayer Kyle — frontier
  thinking LLMs follow about 150–200 instructions consistently;
  "AGENTS.md as small as possible".
- danielrosehill Agents.md-Templates — community template index, sample
  shape only; not a normative specification.
- openai/codex `AGENTS.md` — current raw size 40 lines on 2026-04-29
  (supersedes earlier 213-line record); short entry-card shape.

**Class C — unverified benchmark names (no URL, no independent
fact-check)**

- OpenAI skills catalog; Claude skill guidance; GitHub Copilot skills
  docs; Vercel agent-skills template; getsentry agents-md guidance.
  These names were retained from earlier iterations of this design for
  vocabulary continuity. They are NOT used as evidence for any candidate
  principle, pattern, or rule below. If a future revision needs to rely
  on any of them, it SHOULD first add the URL and a verification note.

**Repository evidence**

- `codex-global-agents-md` intake measured `~/.codex/AGENTS.md` at 281
  lines, up from 223 lines in the 2026-04-03 backup: 58 lines, or about
  26 percent, over 24 days.
- The same intake corrected earlier weak benchmarks and concluded the
  file is "long and type-mixed", not automatically wrong by line count
  alone.

Candidate implication: this repository should not collapse every behavior
asset into root `AGENTS.md`, repo `AGENTS.md`, or `SKILL.md`. Root
routing, repo-local policy, standing rules, triggered skills, lifecycle
artifacts, replay evidence, and durable knowledge need separate
responsibilities.

## Design Principles

The following principles constrain every behavior-asset change in this
repository. Sources in parentheses reference the `Benchmark Signals` section
above or repository evidence already cited.

1. **Source of truth per layer.** Each behavior statement SHALL live in exactly
   one layer; other layers reference but do not duplicate. (source: repo
   `AGENTS.md` Skill Authoring Contract — "complements, but does not replace";
   Benchmark Signals class B — GitHub Blog 2,500 repos study treats commands,
   testing, project structure, code style, git workflow, and boundaries as
   distinct areas, which implies one-layer ownership per area)
2. **Load order is not authority order.** Nearer layers are easier to discover;
   nearness does not grant override rights over repo governance. Authority
   follows explicit carve-outs, not proximity. (source: official `agents.md`
   precedence + repo `AGENTS.md` "principle-skills complements, but does not
   replace, repo governance")
3. **Triggered over ambient.** `rules/` load by work-type match; `skills/` load
   by explicit `/name` or stated intent. Ambient `AGENTS` content stays
   entrance-card sized, not encyclopedia-sized. (source: Benchmark Signals
   class A — Anthropic Agent Skills engineering post, progressive disclosure
   and dynamic loading; class B — skyzyx instruction budget 150–200 citing
   Humanlayer Kyle)
4. **Instruction budget is finite.** Root `AGENTS.md` is a shared budget across
   every repo; adding repo-specific rules to root taxes every other repo.
   (source: `codex-global-agents-md` intake measurement — 223 to 281 lines in
   24 days; Benchmark Signals class B — skyzyx-Humanlayer 150–200 instruction
   budget)
5. **Evidence precedes runtime change.** Behavior-asset edits require before
   and after evidence in `evaluation.md`; replay-harness evidence is required
   only when trigger or refusal semantics change. (source: in-repo harness
   shape `wiki/ops/disagreement-management-replay-harness.md` and
   `scripts/disagreement_replay_check.py`; repo `AGENTS.md` High-Frequency
   Principles — "evaluation.md is the behavior-proof artifact")
6. **Candidate versus decided is visible.** Design artifacts label every
   non-accepted rule as `candidate`, `proposed for review`, or `open
   question`; spec requirements use `SHALL` or `MUST` only after explicit
   review. (source: `codex-global-agents-md` intake §11 quantification audit —
   retracting unverified claims)

## Minimum Process

The minimum steps for a behavior-asset change. No step may be skipped; adding
steps is allowed when the change is large.

1. **Declare target layer and semantic weight.** Name the layer (root `AGENTS`,
   repo `AGENTS`, `rules/`, `skills/`) and state whether the edit changes
   trigger semantics, refusal semantics, or is pure wording. (Principle 1)
2. **Check source of truth.** If the behavior is already stated elsewhere,
   reference it; do not duplicate. (Principle 1)
3. **Check authority precedence.** If the edit loosens a layer the current
   layer does not own, reject the change until a carve-out is added in the
   owning layer. (Principle 2)
4. **Pick the change surface by semantic weight.** (Principles 3 and 5)
   - Root `AGENTS` edit or skill trigger/refusal change: OpenSpec change
     required (proposal, design, tasks, evaluation, spec delta).
   - Repo `AGENTS` edit: OpenSpec change OR in-repo decision record (ADR,
     wiki retro, change evaluation entry).
   - Pure wording or routing cleanup: in-repo edit acceptable.
5. **Record before/after evidence.** Update `evaluation.md`. Attach
   replay-harness evidence only when trigger or refusal semantics change.
   (Principle 5)
6. **Run the Self-Check Checklist before marking tasks complete.** (Principle
   6)

## Self-Check Checklist

Run this checklist before marking any behavior-asset change task complete.
Unresolved items SHALL be recorded as blockers in `tasks.md` or
`evaluation.md`.

**Structural**

- [ ] `openspec validate <change-id>` passes.
- [ ] `openspec change show <change-id> --json --deltas-only` shows every new
  requirement's `text` field as a complete sentence. If the parser truncates,
  the first paragraph contains a physical line break and must be compressed
  to one line.
- [ ] `deltaCount` matches the intended scope. New requirements are not added
  when the change advertises itself as design-only or candidate-only.

**Semantic**

- [ ] Target layer declared. No layer is edited without declaration.
- [ ] Authority precedence respected. Skill changes do not override repo
  `AGENTS.md` boundaries without an explicit repo carve-out.
- [ ] Source of truth single. No duplication of a rule that already lives in
  another layer.
- [ ] Candidate items labeled. Spec requirements use `SHALL` or `MUST` only
  after explicit review.

**Evidence**

- [ ] `evaluation.md` updated with `Baseline Scenarios`, `Before Results`,
  `After Results`, and `Residual Risks`.
- [ ] Replay-harness evidence attached if trigger or refusal semantics
  changed.
- [ ] Intake or prior trace referenced if the change answers a recorded
  finding.

**Boundary**

- [ ] `git diff --name-only HEAD` scope matches the change's declared
  `Impact`.
- [ ] Phase 0 promise intact if the change is Phase 0: zero root dotfile
  edits, zero repo skill edits, zero root rule edits, zero wiki method page
  edits.

**Item declaration (required for each item above):**

For each checklist item the change SHALL declare one of:

- `applicable` — the item applies; record the command output or evidence
  location.
- `not applicable` — the item does not apply; record the reason (for
  example: "no trigger or refusal semantics changed, so replay-harness
  evidence is not required"; "change is design-only, so no new requirements
  are added").
- `blocker` — the item applies but is unresolved; record a tracking entry
  in `tasks.md` or `evaluation.md`.

A task SHALL NOT be marked complete while any `blocker` item is open.
`applicable` items must have recorded evidence; `not applicable` items must
have a recorded reason. This three-state declaration is the mechanism that
keeps candidate-only or design-only changes from being trapped by checklist
items that do not apply to them.

## Pattern Catalog

Each entry below is decided as of 2026-05-06; see `evaluation.md`
§Archive-readiness Review Outcome. Every behavior-asset change SHOULD
declare the following fields for its target pattern type before a task is
marked complete. The SHOULD binding remains; promotion to SHALL is deferred
until three real pattern additions in successor changes verify the
five-field shape is workable (D2, 2026-05-06).

- *Purpose* — what this asset type exists for.
- *Owns* — the semantics it alone decides.
- *Must Not Own* — semantics that belong to another layer.
- *Required Evidence* — what must accompany a change.
- *Anti-patterns* — shapes that trigger rejection.
- *References* — citable sources, or `internal observation; no external
  source` when no verified external reference exists.

Provenance rule: every external reference in this catalog traces back to a
URL that is already fact-checked in
`wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` §3 External
Reference Summary, OR to an Anthropic-normative document cited by its canonical
URL. Claims must not re-state what a source does not actually contain.

### Root AGENTS pattern

- **Purpose**: Cross-repo safety floor and entrance routing for a single
  agent family. Reads first at session start.
- **Owns**: Destructive git gate, external call boundary, dirty-tree gate,
  hard stops, cross-repo path conventions.
- **Must Not Own**: Repo-local workflow steps, OpenSpec archive-review
  detail, repo-specific file paths, method-page bodies.
- **Required Evidence**: OpenSpec change plus `evaluation.md` before edit.
  A chat plan is not sufficient.
- **Anti-patterns**: Inlining repo policy (intake C2); hard-coded WSL
  absolute paths (intake C3); cross-repo rule duplication across root files;
  accreting past the instruction budget without removing older content.
- **References**: skyzyx gist — instruction budget 150–200 instructions per
  Humanlayer Kyle (intake §3); arXiv 2602.11988 — context file cost 20%+
  inference overhead (intake §3); openai/codex `AGENTS.md` — short-card
  shape (intake §3); repo `AGENTS.md` High-Frequency Principles —
  "complements, but does not replace".

### Repo AGENTS pattern

- **Purpose**: Repo-local policy surface — OpenSpec triggers, wiki routing,
  skill authoring contract, repo-specific stop conditions.
- **Owns**: Repo workflow phases, skill contract gates, delivery-boundary
  routing, repo-local decision observability.
- **Must Not Own**: Cross-repo safety floor (that is root), personal global
  preferences, method-page bodies.
- **Required Evidence**: OpenSpec change OR in-repo decision record (ADR,
  wiki retro, change `evaluation.md`).
- **Anti-patterns**: Replacing root safety floor; absorbing personal global
  preferences; duplicating rule text that lives in `rules/`; describing
  repo behavior as a template instead of a repo-specific policy.
- **References**: GitHub Blog "how to write a great agents.md" — six core
  areas: commands, testing, project structure, code style, git workflow,
  boundaries (intake §3); danielrosehill Agents.md-Templates — community
  sample shape (intake §3); in-repo `AGENTS.md` self-documenting
  Governance Phase sections.

### Rule pattern (`~/.codex/rules/` and repo equivalents)

- **Purpose**: Persistent work-type-matched constraints — git, testing,
  security, development workflow — that load ambiently when the work type
  matches, without a skill trigger.
- **Owns**: Cross-cutting execution constraints. Applies by matching the
  current work type, not by naming a skill.
- **Must Not Own**: Task-flow orchestration; triggered capabilities; repo
  policy; agent-specific preferences.
- **Required Evidence**: In-repo edit acceptable when wording only;
  OpenSpec change when the rule changes how any trigger or refusal fires.
- **Anti-patterns**: Rule text that duplicates repo AGENTS content; rules
  that describe a specific task rather than a work-type constraint; rules
  that silently change trigger semantics without an OpenSpec change.
- **References**: Internal observation; no external source. See
  `~/.codex/rules/{common,python,web}/` directory shape and the
  rule-routing references inside repo `AGENTS.md`.

### Skill pattern (`.codex/skills/*` and `~/.codex/skills/*`)

- **Purpose**: On-demand behavior contract for a triggered capability.
  Loads only on `/name` match or clearly stated intent. Structured as a
  compact `SKILL.md` with optional `references/` and `scripts/`.
- **Owns**: Trigger description, hard rules, anti-patterns, pointers to
  `references/` and `scripts/`. Follows progressive disclosure — metadata
  first, body next, resources on demand.
- **Must Not Own**: Repo governance. Skills complement repo AGENTS; they
  do not replace it. A skill MAY tighten a repo boundary but MUST NOT
  loosen or bypass one without an explicit repo `AGENTS.md` carve-out.
- **Required Evidence**: New skill — complete `SKILL.md` contract with
  frontmatter `name` and `description` (optional `disable-model-invocation`,
  `user-invocable`, `allowed-tools`). Edit to trigger or hard rules —
  before/after evaluation evidence; replay-harness fixture when trigger
  or refusal semantics change.
- **Anti-patterns**: Inlining long examples into `SKILL.md` body;
  overriding a repo `AGENTS.md` boundary; making a skill ambient-loading
  instead of trigger-gated; duplicating rule content.
- **References**: Anthropic Agent Skills engineering post — progressive
  disclosure, dynamic loading, code-as-documentation
  (https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills,
  2025-10); anthropics/skills README — SKILL.md frontmatter contract
  (https://github.com/anthropics/skills); in-repo worked examples
  `.codex/skills/clarify-before-acting/SKILL.md`,
  `.codex/skills/verify-before-claiming/SKILL.md`,
  `.codex/skills/openspec-propose/SKILL.md`.

### OpenSpec change pattern

- **Purpose**: Lifecycle container for a scoped change — `proposal.md`,
  `design.md`, `tasks.md`, `evaluation.md`, and `specs/*/spec.md` deltas
  — that forces chat-level ideas through an evidence gate.
- **Owns**: Scope, task list, candidate-versus-decided labeling,
  before/after evidence, spec deltas.
- **Must Not Own**: Long-term knowledge base; method-page bodies; stable
  decisions after archive (those promote to ADR or spec).
- **Required Evidence**: The artifacts themselves. `openspec validate`
  passes; `openspec change show <id> --json --deltas-only` shows every
  new requirement as a complete sentence.
- **Anti-patterns**: Mixing candidate and decided rules in one spec delta;
  letting a chat plan bypass OpenSpec for root AGENTS or skill-semantic
  edits; archiving with `tasks.md` entries still candidate; requirements
  whose first paragraph contains a physical line break and gets truncated
  by the parser.
- **References**: Internal observation; no external source. See archived
  changes under `openspec/changes/archive/` and repo `AGENTS.md` OpenSpec
  Trigger and Archive Review Default sections.

### Harness pattern (`wiki/ops/*-replay-harness.md` + `scripts/*_replay_check.py`)

Terminology caveat: public "agent harness" often means a runtime wrapper;
this design uses "harness" only as review evidence, not runtime
infrastructure.

- **Purpose**: Replay evidence for behavior design review. Records what
  failed before, what should pass after, and what is outside proof.
- **Owns**: RED baseline, GREEN expectation, residual risks, proof
  boundary, optional structural checker.
- **Must Not Own**: Runtime enforcement; hooks; CI gates; compliance
  automation.
- **Required Evidence**: Harness artifact attached only when the change
  alters trigger or refusal semantics. Pure wording or routing cleanup
  does not require a harness.
- **Anti-patterns**: Treating a harness script as a runtime gate;
  claiming replay evidence proves rollout; adding a harness for
  wording-only edits; writing a harness for a behavior that has no
  preceding RED baseline.
- **References**: Internal observation; no external source. See in-repo
  `wiki/ops/disagreement-management-replay-harness.md` and
  `scripts/disagreement_replay_check.py` as the canonical shape.

### Wiki / ADR / retro pattern

- **Purpose**: Durable learning and stable-decision layer. Intake captures
  initial trace; retro captures drift; distill captures candidate
  consolidation; method page captures accepted workflow; ADR captures
  accepted cross-change decision.
- **Owns**: Recovered context, fact-checked quantifications, cross-change
  indexing, candidate-versus-decided labeling.
- **Must Not Own**: Unaccepted rules presented as decided; runtime
  triggers; skill bodies; repo policy text that duplicates AGENTS.
- **Required Evidence**: Intake/retro — frontmatter plus trigger, current
  focus, proof boundary. Distill/design-trace — candidate labeling plus
  link to the active OpenSpec change. Method/ADR — only after the
  originating OpenSpec change closes.
- **Anti-patterns**: Publishing a method page before the active change
  closes (Wiki Landing Gated rule); promoting a candidate distill or
  design-trace directly to ADR; duplicating `rules/` or skill content in
  a method page; using file names that carry dates, status words, or
  change identifiers (Wiki Naming Model v1).
- **References**: Internal observation; no external source. See in-repo
  `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` and
  the Wiki Naming Model Default plus Wiki Frontmatter Model Default
  sections in repo `AGENTS.md`.

## Pattern Skeleton Examples

Minimal markdown skeletons for each of the seven pattern types. Each skeleton
is a candidate starting shape; fenced blocks show the file body, not the
surrounding filesystem. Comments inside skeletons use markdown headings or
inline notes, not code comments. Authority still follows the Catalog above;
a skeleton does not grant the asset its own authority.

### Root AGENTS skeleton (`~/.codex/AGENTS.md` or `~/.claude/CLAUDE.md`)

    # Personal Global AGENTS

    ## Identity & Scope
    One paragraph: which agent family, which operator, cross-repo scope.

    ## Hard Stops (safety floor, not loosened by repo or skill)
    - destructive git operations require explicit user intent
    - external calls require declared boundary
    - dirty working tree requires user decision, not silent continuation

    ## Startup Checklist
    1. Git truth — no claims about clean/committed/pushed without checking.
    2. Project context — load `PROJECT.md` if substantial project work.
    3. Lore — load per-domain entries, not the whole file.

    ## Routing to Repo & Rules
    - repo-local workflow → repo `AGENTS.md`
    - cross-cutting constraints → `~/.codex/rules/common/*.md`
    - language-specific → `~/.codex/rules/python/*.md`, `web/*.md`

    ## Non-goals (kept out by design)
    - repo-specific policy lives in repo `AGENTS.md`
    - method bodies live in wiki, not here

### Repo AGENTS skeleton (`./AGENTS.md`)

    # Repo AGENTS

    ## Project Object
    One paragraph: what this repo is, what its source-of-truth is.

    ## OpenSpec Triggers
    - semantic change to behavior asset → open OpenSpec change
    - new skill or skill-trigger edit → open OpenSpec change
    - pure wording fix → in-repo edit acceptable

    ## Skill Authoring Contract
    - complements, does not replace, repo governance
    - `evaluation.md` required for semantic edits
    - trigger description single-paragraph, hard rules bulleted

    ## Wiki Routing
    - intake → `wiki/ops/<canonical-object>-<artifact>.md`
    - method page → only after originating change archived

    ## Archive Review Default
    One paragraph: how `complete` turns into `archive-ready`.

### Rule skeleton (`~/.codex/rules/common/git-workflow.md` shape)

    # git-workflow

    ## When this rule applies
    Any work type that involves git state or git operations.

    ## Hard constraints
    - never force-push to `main`
    - never skip hooks unless user asks explicitly
    - stage specific files, not `git add -A`

    ## Boundary with other rules
    - destructive ops → safety rule in root AGENTS
    - branch naming → repo AGENTS or branch-naming skill

    ## Non-goals
    - not a task-flow orchestration
    - not a per-skill trigger

### Skill skeleton (`.codex/skills/<name>/SKILL.md`)

    ---
    name: <slug-case>
    description: One sentence. Agent reads this to decide whether to load.
    # optional: disable-model-invocation: true
    # optional: user-invocable: false
    # optional: allowed-tools: [Read, Bash]
    ---

    # <Skill title>

    ## When to use
    Bulleted triggers: exact phrases, intent shapes, file types. Keep short.

    ## Hard rules
    - the three to five non-negotiable constraints
    - each rule one line, no prose

    ## Anti-patterns
    - what loading this skill should never do

    ## Workflow
    Step-by-step, one or two screens max. Long forms go to
    `references/<topic>.md`; executable helpers go to `scripts/<name>.sh`.

    ## References (progressive disclosure)
    - `references/examples.md` — worked examples
    - `scripts/check.sh` — on-demand helper

### OpenSpec change skeleton (`openspec/changes/<id>/`)

    # proposal.md
    ## Why
    One paragraph motivating the change.
    ## What Changes
    Bulleted list, concrete.
    ## Capabilities
    ### New | Modified | Removed

    # design.md
    ## Confirmed Problem
    ## Confirmed Boundaries
    ## Benchmark Signals
    ## Design Principles
    ## Minimum Process
    ## Self-Check Checklist
    ## Candidate Pattern Catalog (if behavior-asset change)
    ## Design Decision Proposed For Review
    ## Quantified Review Criteria
    ## Open Questions

    # tasks.md
    ## 1. Change Setup
    - [ ] 1.1 ...
    ## 2. Open Decisions
    - [ ] 2.1 ...
    ## 3. Reviewable Design
    - [x] 3.1 ...

    # evaluation.md
    ## Baseline Scenarios
    ## Before Results
    ## After Results
    ## Residual Risks

    # specs/<capability>/spec.md
    ## ADDED | MODIFIED | REMOVED Requirements
    ### Requirement: <complete single-sentence MUST or SHALL>
    <single-line first paragraph — parser truncates on line break>
    #### Scenario: <name>
    - **WHEN** ...
    - **THEN** ...

### Harness skeleton (`wiki/ops/<topic>-replay-harness.md`)

    ---
    canonical_object: <topic>
    artifact_type: replay-harness
    validates: <topic>
    ---

    # <topic> / replay-harness

    ## Behavior under review
    One paragraph: exact behavior, exact trigger, exact refusal condition.

    ## RED baseline (what used to fail)
    - observable signal
    - minimal reproducer

    ## GREEN expectation (what should now hold)
    - observable signal
    - minimal reproducer

    ## Proof boundary
    - what this harness does prove
    - what it does not prove

    ## Optional checker
    Path to `scripts/<topic>_replay_check.py` if a structural checker exists;
    otherwise note "manual replay only."

### Wiki / ADR / retro skeleton (covered layer, minimal frontmatter)

    ---
    title: <canonical-object> / <artifact-type>
    type: <intake | retro | distill | design-trace | method | adr>
    canonical_object: <object>
    artifact_type: <matches type>
    language: <zh-CN | en>
    audience: self
    domain: <domain>
    status: active
    updated_at: YYYY-MM-DD
    derived_from:
      - <in-repo path or URL>
    related_objects:
      - <object>
    notes_scope: One paragraph stating what this page carries and what it
      does not carry.
    ---

    # <canonical-object> / <artifact-type>

    ## 1. Purpose
    One paragraph. For intake / trace, state candidate-vs-decided clearly.

    ## 2. Body
    Sectioned content. Avoid inlining `SKILL.md` or rule text verbatim.

    ## N. Proof Boundary
    - verified by this page
    - not verified by this page
    - candidate only (if applicable)

## Proposed Wiki Artifact Types

This change proposes `design-trace` as a `wiki/ops` `artifact_type` value for
candidate design snapshots tied to an active OpenSpec change. The value
becomes accepted only after this change is archived; while the change is
active, the trace is recorded as a candidate alongside the repo's Wiki
Naming Model Default. Upon archive, the archive review decides whether to
promote the trace content to a method page or ADR. If promotion happens,
the trace is superseded; if promotion does not happen, the trace either
remains as a frozen candidate record or is retracted by the same archive
review. Promotion is never automatic.

Existing `wiki/ops` artifact types still apply: `intake`, `retro`, `distill`,
`method`, `adr`, plus the vocabulary already listed in repo `AGENTS.md` Wiki
Naming Model Default and Wiki Frontmatter Model Default. This change does
not rename existing pages or force migration.

## Design Decision Proposed For Review

**Decision**: adopted 2026-05-06. See `evaluation.md`
§Archive-readiness Review Outcome (D1).

Proposed review baseline: hybrid split with a root/repo-aware governance stack.

This candidate says the repository may record the relationship between repo
governance and personal root dotfiles, but it does not own the full content of
personal global dotfiles. Root files may align on shared safety boundaries while
keeping personal or agent-specific behavior separate.

Proposed responsibility split:

1. `root AGENTS`: personal global entrance card for cross-repo source-order,
   intent routing, hard stop gates, escalation boundaries, health checks,
   branch safety, and git truth-source checks. It should not carry repo-local
   workflow history or method bodies.
2. `repo AGENTS`: repository-local policy surface for repo defaults, OpenSpec
   triggers, wiki routing, local skill contracts, and project-specific stop
   conditions. It should not be treated as a personal global template.
3. `rules`: always-available cross-cutting execution constraints such as git,
   testing, security, development workflow, and behavior-asset gates. Rules
   apply because the work type matches, not because a user names a skill.
4. `skills`: on-demand behavior contracts for triggered capabilities such as
   `openspec-explore`, `openspec-propose`, `openspec-apply-change`,
   `openspec-archive-change`, and `meeting-note-output`. `SKILL.md` should stay
   compact and point to references or scripts when detail would bloat trigger
   context.
5. `OpenSpec`: proposal, design, tasks, spec deltas, and evaluation lifecycle
   for workflow and behavior changes. OpenSpec owns scoped change progress and
   prevents chat-level plans from becoming direct behavior-asset edits.
6. `harness`: replay evidence for behavior design review. Harness artifacts
   record what failed before, what should pass after, and what remains outside
   proof. They do not enforce behavior.
7. `wiki / ADR / retro`: durable recovery and stable decision layers. Wiki
   pages preserve learning and calibration; retros preserve drift and
   disagreement; ADRs preserve accepted cross-change decisions.

Candidate route examples:

- `/plan`: planning stance, converge toward an implementation plan, no writes.
- `$openspec-explore`: thinking stance first, ambiguity preservation first,
  implementation never; repo-visible trace or retro routing is decided after
  the exploration object is understood.
- `openspec-propose`: convert stable intent into proposal, design, tasks, and
  spec deltas without treating the proposal as implementation approval.
- `openspec-apply-change`: implement only approved change scope and keep
  `tasks.md` synchronized with verified progress.
- `openspec-archive-change`: perform archive review, keep blockers visible, and
  archive only after review passes.
- behavior-asset edit: route through the development-workflow rule, require
  before/after evaluation evidence, and use harness evidence only as review
  evidence.

## Codex Source Order

Candidate load order and conflict adjudication for the three Codex layers
(`~/.codex/AGENTS.md`, repo `AGENTS.md`, triggered skill). Proposed for review,
not decided.

- Load order: root `~/.codex/AGENTS.md` first, then repo `AGENTS.md`, then any
  triggered skill under `~/.codex/skills/` or repo `.codex/skills/`.
- Load-order nearness (discovery): later layers are more local and more recent;
  they MAY add triggers, add routing, and narrow hard stops.
- Authority precedence (governance): repo `AGENTS.md` SHALL NOT be overridden
  by `~/.codex/skills/` or `.codex/skills/` entries. Skills complement repo
  governance; they do not replace it. A skill MAY tighten a repo boundary
  but SHALL NOT loosen or bypass one without an explicit repo `AGENTS.md`
  carve-out.
- Safety floor exception: destructive git, external call boundary, write-target
  boundary, and dirty-tree gates are owned by root. Repo and skill layers may
  tighten these but SHALL NOT loosen them.
- Legitimate divergence: personal global startup preferences, agent-specific
  capability differences, cross-repo defaults, and local machine paths.
- Illegitimate conflict: the same in-repo behavior is asserted with contradictory
  semantics across the three layers while all three are active in the current
  repository.

## Interaction Protocol

Candidate rules for how the three Codex layers compose with `rules/`, OpenSpec,
and harness evidence. Proposed for review, not decided.

1. Trigger. A skill loads only when the user enters a matching `/name` or the
   skill description matches the stated intent. A skill MAY declare rule
   dependencies in its `SKILL.md` preamble; when a skill makes such a
   declaration, triggering it SHALL load the declared `rules/` entries.
   This protocol does not create a new required field in `SKILL.md`; the
   declaration is opt-in, and the Skill pattern Required Evidence only
   covers rule-dependency loading for skills that opt in. `rules/` entries
   MAY also load when the current work type matches, even without a skill.
2. Edit gate. Any edit to a behavior-asset layer SHALL declare target layer and
   impact surface before writing.
   - Root `AGENTS.md`: requires an OpenSpec change plus `evaluation.md` before
     edits. A chat-level plan is not sufficient.
   - Repo `AGENTS.md`: requires an OpenSpec change or an in-repo decision record
     (ADR, wiki retro, or change evaluation entry).
   - Skills: new skills require a complete `SKILL.md` contract; edits to an
     existing skill's trigger or hard rules require before/after evaluation
     evidence.
3. Decision record. A decision is recorded in the layer where it binds. Changes
   with cross-layer effect SHALL be indexed from `design.md` or an ADR so the
   effect is discoverable from every affected layer.
4. Harness hook. Replay-harness evidence is required only when an edit changes
   when a behavior triggers or when it refuses. Pure wording, routing cleanup,
   and path normalization edits do not require harness evidence.

## Issue Routing Table

Candidate mapping of every intake finding in `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md`
to a target layer and action class. The action classes are:

- `candidate-root-edit`: after protocol acceptance the item may be edited in
  the listed layer. This change does not perform the edit; it is deferred to
  Phase 1 or a successor change. The name intentionally says "candidate" and
  "root-edit" so the row cannot be misread as "edit inside this change."
- `defer-change`: requires a separate OpenSpec change named below.
- `accept-as-divergence`: legitimate divergence under Codex Source Order; no
  reconciliation needed.
- `reject-claim`: intake claim is not supported by the current fact-check; the
  table records the rejection so it is not re-raised.

Candidate mapping (review required before acceptance):

| ID | Item | Layer | Action | Reason |
|----|------|-------|--------|--------|
| C1 | team-lore path fork (`/mnt/d/team-lore/wiki` vs `~/team-lore/LORE.md`) | root | candidate-root-edit | Shared path used by both agents should converge at the root layer |
| C2 | Global file carries OpenSpec archive-review detail (lines 115-127) | root | candidate-root-edit | Self-violates the line 280 "repo semantics stay in repo" statement |
| C3 | Hard-coded WSL absolute path `/mnt/d/team-lore/wiki` | root | candidate-root-edit | Cross-machine portability risk in a personal global file |
| S1 | REQ identification reads as dead code once OpenSpec is default | root | defer-change | Requires a separate decision on progressive disclosure for global files |
| S2 | `active OpenSpec change` vs `approved OpenSpec change` wording inconsistency | root | candidate-root-edit | Wording alignment only |
| S3 | Three git-discipline phrases, "each appears twice" | root | reject-claim | 2026-04-27 grep fact-check retracted the string-count claim; semantic-overlap argument not yet reopened |
| S4 | Rule precedence covers `rules/*` only, not `agents/*` | root | candidate-root-edit | Precedence text completion |
| S5 | Lore navigation model diverges across agents (Codex wiki tree vs Claude flat grep) | root + repo | defer-change | Affects claude side; requires cross-agent decision outside this change |
| A1 | Branch naming convention defined only on Claude side | root | accept-as-divergence | Legitimate agent-specific difference under Source Order |
| A2 | Technical checkpoints split across lines 110 / 157 / 246 in root file | root | candidate-root-edit | Consolidation, no behavior change |
| A3 | Health check strictness diverges (Claude hard-stop vs Codex soft-advise on dirty tree) | root | accept-as-divergence | Agent-specific risk calibration |
| A4 | Proceed-signal vocabulary (Codex 9 tokens vs Claude 4) | root | accept-as-divergence | Agent-specific trigger breadth |
| A5 | `graphify` skill only on Claude side | skill | defer-change | Requires a separate decision on Codex parity |
| M1 | `AGENTS.md.bak-20260403-193625` residue | root | candidate-root-edit | File deletion |
| M2 | `task-related` vs `local junk` undefined | root | candidate-root-edit | Definition line addition |
| M3 | Large-file guardrails only cover Python plus Vue/JS/TS | root | candidate-root-edit | Language-list expansion |
| M4 | `Paths` section has a single entry | root | candidate-root-edit | Merge into Identity section |
| M5 | Self-check omits read-only and UI operation types | root | candidate-root-edit | Checklist semantics addition |

Intake §5 open questions also fall under the routing table. Their candidate
placements:

- Q1 team-lore unified form (wiki vs flat LORE.md): root, `defer-change`; tied to C1.
- Q2 archive-review detail already covered by each repo `AGENTS.md`: repo, `defer-change`; requires per-repo verification.
- Q3 Codex wider proceed-signal set: root, `accept-as-divergence`; resolved by A4.
- Q4 Graphify parity for Codex: skill, `defer-change`; resolved by A5.
- Q5 Branch naming copied to Codex: root, `accept-as-divergence`; resolved by A1.
- Q6 Shared canonical object with repo `agents-governance-drift`: design, `defer-change`; the routing table itself is this answer when accepted.

The mapping is candidate, not decided. Acceptance of this change means the
table is reviewable; the individual rows stay open until reviewed.

## Harness Minimal Shape

Harness v1 should be deliberately small:

- `replay-harness.md`: records the behavior under review, scenario fields, pass
  criteria, and proof boundary.
- fixture: a markdown or JSON scenario with RED baseline, GREEN expectation,
  and residual risk.
- `evaluation.md`: records before/after results inside the OpenSpec change.
- optional checker: deferred to Phase 2; if added later, it may only perform
  structural validation such as required fields or forbidden overclaim phrases.

Harness v1 proves only that review evidence exists in a replayable shape. It
does not prove rollout, automatic compliance, skill trigger behavior, or runtime
enforcement.

## Phased Change Path

Phase 0 is this design repair:

- root dotfile edits: 0
- repo skill edits: 0
- root rule edits: 0
- wiki method page edits: 0
- permitted wiki changes (exhaustive list, two items only):
  1. one intake learning update at
     `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` that
     explains why the learning needed to land without promoting a method
     or ADR
  2. one candidate design trace at
     `wiki/ops/behavior-asset-governance-design-trace.md` that mirrors
     the active design snapshot; this is the only permitted new wiki file
     in Phase 0

Phase 1, if accepted, may add manual templates:

- one minimal `replay-harness.md` template
- one fixture template
- one `evaluation.md` example or guidance note
- no checker, hook, CI, or root runtime behavior change

Phase 2, only after Phase 1 is useful, may add a structural checker:

- check required fields
- check forbidden overclaim signals such as treating candidate models as
  accepted decisions
- keep the checker out of runtime behavior enforcement

Phase 3, only after repeated evidence, may discuss stronger gates:

- require at least three behavior-asset changes to use the manual harness shape
  before considering automation
- require a new OpenSpec change before connecting checker output to hooks, CI,
  or archive blockers

## Quantified Review Criteria

The design is ready for review when:

- exactly 0 root dotfiles, repo skills, root rules, or wiki method pages are
  edited by this change
- touched files are limited to the active change artifacts, the named wiki
  intake `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md`,
  and the candidate design trace
  `wiki/ops/behavior-asset-governance-design-trace.md`
- `tasks.md` does not mark final alignment, ownership, or root/repo-aware
  responsibility decisions complete
- `evaluation.md` records the RED baseline, GREEN target, and residual risks
  without claiming runtime behavior changed
- `openspec validate decide-root-governance-alignment` passes
- search checks do not find over-acceptance signals such as checked `2.1`,
  `2.2`, or `2.3` tasks, or wording that presents the candidate model as the
  final model

## Archive Readiness Criteria

The change SHALL NOT enter archive review until every item below is true. This
list is the answer to the previously open question "What evidence is required
before archive readiness?"

- tasks 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7 resolved (either decided or
  explicitly deferred to a named successor change recorded in `tasks.md`)
- task 3.7 resolved (root/repo-aware governance model adopted, revised, or
  rejected)
- task 3a.5 resolved (each Issue Routing Table row confirmed, revised, or
  rejected)
- tasks 3b.8, 3b.9, 3b.15, 3b.16, 3b.17 resolved (Design Principles,
  Self-Check Checklist, Pattern Catalog SHOULD-vs-SHALL, Interaction Protocol
  skill-preamble, and routing-class rename reviewed)
- `spec.md` contains no `SHALL` or `MUST` whose review gate is still open in
  `tasks.md`
- `design.md` Phase 0 permitted-files list matches the actual
  `git diff --name-only HEAD` scope
- `openspec validate decide-root-governance-alignment --strict` passes
- `evaluation.md` records an archive-readiness outcome

## Open Questions

The questions below were open when the section was written. D1/D2/D3
were closed 2026-05-06; see `evaluation.md` §Archive-readiness Review
Outcome.

- Should the final root/repo relationship be hybrid split, intentional
  divergence, full alignment on selected clauses, or something else?
  *(closed 2026-05-06 — hybrid split adopted per D1)*
- Which exact clauses must align across repo `AGENTS.md`,
  `~/.codex/AGENTS.md`, and `~/.claude/CLAUDE.md`?
  *(deferred to successor change that performs root edits; Pattern
  Catalog now defines the alignment rules per layer)*
- Who owns future updates when root defaults and repo policy disagree?
  *(closed 2026-05-06 — Principle 1 source-of-truth-per-layer + Pattern
  Catalog Owns / Must Not Own fields answer this)*
- Should the root/repo-aware model be adopted as the review baseline, revised,
  or rejected?
  *(closed 2026-05-06 — adopted per D1)*
- Should harness Phase 1 proceed as manual templates only?
  *(closed 2026-05-06 — yes, per task 2.6 decision)*
- Is a targeted `wiki/ops retro` needed after review, or is the intake update
  and active change sufficient durable recovery?
  *(closed 2026-05-06 — intake + trace + Chinese companion sufficient;
  retro/method/ADR deferred to successor change if pattern recurs)*
