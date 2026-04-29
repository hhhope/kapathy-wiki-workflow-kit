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

External references are benchmark inputs, not imported policy:

- OpenAI skills catalog: skills are packaged instructions, scripts, and
  resources for repeatable tasks.
- Claude skill guidance: keep skills concise, structured, tested, and use
  progressive disclosure for supporting material.
- GitHub Copilot skills docs: use repository or personal skills for relevant
  task-specific instructions; keep broad always-on guidance in custom
  instructions.
- Vercel agent-skills template: skill packages can include `SKILL.md`,
  scripts, references, packaging rules, and context-efficiency guidance.
- getsentry agents-md guidance: agent-facing instructions should stay
  high-signal and reference existing docs instead of duplicating them.

Repository evidence adds two concrete signals:

- `codex-global-agents-md` intake measured `~/.codex/AGENTS.md` at 281 lines,
  up from 223 lines in the 2026-04-03 backup: 58 lines, or about 26 percent,
  over 24 days.
- The same intake corrected earlier weak benchmarks and concluded the file is
  "long and type-mixed", not automatically wrong by line count alone.

Candidate implication: this repository should not collapse every behavior asset
into either root `AGENTS.md` or `SKILL.md`. Routing, standing rules, triggered
skills, lifecycle artifacts, replay evidence, and durable knowledge need
separate responsibilities.

## Design Decision Proposed For Review

Proposed review baseline: hybrid split with a six-layer governance stack.

This candidate says the repository may record the relationship between repo
governance and personal root dotfiles, but it does not own the full content of
personal global dotfiles. Root files may align on shared safety boundaries while
keeping personal or agent-specific behavior separate.

Proposed responsibility split:

1. `root AGENTS`: entrance card for source-order, intent routing, hard stop
   gates, escalation boundaries, health checks, branch safety, and git
   truth-source checks. It should not carry full workflow history or method
   bodies.
2. `rules`: always-available cross-cutting execution constraints such as git,
   testing, security, development workflow, and behavior-asset gates. Rules
   apply because the work type matches, not because a user names a skill.
3. `skills`: on-demand behavior contracts for triggered capabilities such as
   `openspec-explore`, `openspec-propose`, `openspec-apply-change`,
   `openspec-archive-change`, and `meeting-note-output`. `SKILL.md` should stay
   compact and point to references or scripts when detail would bloat trigger
   context.
4. `OpenSpec`: proposal, design, tasks, spec deltas, and evaluation lifecycle
   for workflow and behavior changes. OpenSpec owns scoped change progress and
   prevents chat-level plans from becoming direct behavior-asset edits.
5. `harness`: replay evidence for behavior design review. Harness artifacts
   record what failed before, what should pass after, and what remains outside
   proof. They do not enforce behavior.
6. `wiki / ADR / retro`: durable recovery and stable decision layers. Wiki
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
- permitted wiki change: one intake learning update that explains why the
  learning needed to land without promoting a method or ADR

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
- only active change artifacts plus the named wiki intake are touched
- `tasks.md` does not mark final alignment, ownership, or six-layer
  responsibility decisions complete
- `evaluation.md` records the RED baseline, GREEN target, and residual risks
  without claiming runtime behavior changed
- `openspec validate decide-root-governance-alignment` passes
- search checks do not find over-acceptance signals such as checked `2.1`,
  `2.2`, or `2.3` tasks, or wording that presents the candidate model as the
  final model

## Open Questions

- Should the final root/repo relationship be hybrid split, intentional
  divergence, full alignment on selected clauses, or something else?
- Which exact clauses must align across repo `AGENTS.md`,
  `~/.codex/AGENTS.md`, and `~/.claude/CLAUDE.md`?
- Who owns future updates when root defaults and repo policy disagree?
- Should the six-layer model be adopted as the review baseline, revised, or
  rejected?
- Should harness Phase 1 proceed as manual templates only?
- Is a targeted `wiki/ops retro` needed after review, or is the intake update
  and active change sufficient durable recovery?
- What evidence is required before archive readiness?
