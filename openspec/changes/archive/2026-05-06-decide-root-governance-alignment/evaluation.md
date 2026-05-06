# Evaluation

## Baseline Scenarios

1. The user asks to implement the personal global AGENTS / skill / harness plan
   after a chat-level design.
2. The agent treats the chat plan as sufficient and prepares to edit behavior
   assets directly.
3. The agent treats wiki publication as either the default landing zone or an
   out-of-scope action, without explaining which learning still needs to land.
4. The design describes harness broadly enough that it can be mistaken for a
   hook, CI gate, runtime gate, or automatic compliance mechanism.
5. The design says the candidate model is reviewable but does not define
   measurable review boundaries.

## Before Results

- The implementation path was under-specified: the plan described the desired
  collaboration model but did not first bind it to the active OpenSpec change.
- The previous design compressed rules, skills, and harness evidence into an
  incomplete `AGENTS.md` / `SKILL.md` / replay-harness model.
- The first follow-up needed re-anchoring because "implement the plan" could
  mean root dotfile edits, repo wiki publication, skill authoring, or design
  artifact updates.
- Candidate routing was written too close to a settled operating model, even
  though the final responsibility split remained open.
- Wiki landing was ambiguous: the active change correctly blocked wiki method
  publication, but the learning trace itself was left unclear.
- Harness shape was too abstract; it did not clearly state the minimum
  artifacts, phased path, or proof boundary.
- The design lacked quantified criteria for deciding whether the repair stayed
  inside reviewable design scope.

## After Results

- The active change records a candidate hybrid ownership model for review
  instead of treating the model as accepted.
- The design records the SDD-first gate before any root dotfile, skill, rule, or
  wiki method change.
- The design now records the full candidate governance stack: root `AGENTS`,
  repo `AGENTS`, rules, skills, OpenSpec, harness evidence, and wiki/ADR/retro
  durable layers.
- Harness v1 is limited to manual replay evidence: `replay-harness.md`,
  fixture, and `evaluation.md`; checker work is explicitly deferred to Phase 2.
- Quantified review criteria now state that this change makes 0 root dotfile
  edits, 0 repo skill edits, 0 root rule edits, and 0 wiki method page edits.
- The existing `codex-global-agents-md` intake now records the learning
  conclusion and explains why the previous run did not land wiki material.
- Routing examples are preserved as candidate examples, not final operating
  decisions.

## Anthropic Prompt-Engineering Gate Validation (2026-05-05)

Source reference:
`https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering`.
The relevant external signal is narrow: Anthropic places success criteria,
empirical tests, and an initial prompt before prompt engineering, and notes
that not every failing criterion should be solved by prompt engineering.

Candidate heuristic under test:

> Before changing a behavior asset, identify the success criterion, the failing
> case, and the verification method. If the failure is not controllable by
> behavior wording, do not solve it by editing governance text.

### RED Baseline

1. External-reference capture risk: a new official prompt-engineering URL could
   be treated as sufficient reason to create a standalone wiki page even when
   the reusable learning has not been extracted.
2. Premature governance-edit risk: a failed agent behavior could be routed
   directly into `AGENTS.md`, `rules/`, or `skills/` without first stating the
   failing case and verification method.
3. Over-acceptance risk: a candidate insight could be promoted into `spec.md`
   as `SHALL` before its review task closes.
4. Scope-claim risk: a temporary working-tree fact could be written as durable
   evidence instead of being checked at commit or archive time.

### GREEN Walkthrough

1. Wiki landing decision: the Anthropic page does not create a new wiki page by
   itself. The extracted learning is recorded here as evaluation evidence for
   the active change, while any future wiki landing would need to fit the
   active change's permitted wiki surfaces.
2. Governance-edit decision: the source supports a review heuristic, not an
   immediate edit to root dotfiles, repo `AGENTS.md`, rules, or skills.
3. Spec-strength decision: the heuristic remains candidate evidence in
   `evaluation.md`; it does not introduce a new `SHALL` requirement while the
   design review gates remain open.
4. Scope-claim decision: this evidence records a reasoning check only. Commit
   scope, OpenSpec validation, and archive readiness remain separate fresh
   checks.

### Result

The heuristic passes this limited validation as a candidate review aid. It is
effective for this change if it prevents three mistakes: landing a standalone
wiki page from a raw link, editing governance text without a failing case, and
turning a candidate reference signal into a binding spec requirement.

It is not yet proven as a runtime rule. A later behavior-asset change should
reuse the heuristic on a real failing case before it is promoted into a method,
rule, or skill.

## Skill-gate vs. Abstraction-routing Meta-review (2026-05-05)

### Trigger

During archive-readiness planning, the reviewer agent (claude) produced two
recommendation artifacts for the user: a "four validation methods" list and a
"codex review briefing" draft. Before running either artifact, the user asked
a second agent (codex) to back-check whether those recommendations still
targeted the design's stated goal — behavior-asset abstraction routing across
all landing surfaces — or whether they had narrowed into a skill-gate frame.

This review is not about the design itself. Trace §13 forbids further copy-edit
of `design.md`, `spec.md`, or the design-trace. The meta-review is scoped only
to the reviewer agent's recommended validation and briefing, not to the design
content they were meant to validate.

### Finding

| # | Check | Result | Evidence | Reason |
|---|-------|--------|----------|--------|
| 1 | Skill is one of many landing surfaces | PARTIAL | design.md L120, L290, L308; briefing §3 subjects | Design is correct; briefing's test prompts use "writing a skill" as the default frame |
| 2 | All eight landing surfaces covered | FAIL | design.md L252, L271, L290, L308, L336, L380 cover six; "do not sink" not enumerated; validation methods do not verify per surface | Validation surface was not made the acceptance face |
| 3 | Reuses six principles / six-step / Pattern Catalog | PARTIAL | design.md L148, L151, L156 reused; validation methods introduce new heuristics ("success criterion", "failing sample", "verification method") | Reuse exists but drifts into fresh criteria |
| 4 | Respects trace §13 anti-drift | PASS | trace §13 L647, L662; recommendations explicitly forbid edits to design / spec / trace | No body-text edits requested; no new pattern / checklist / rule added |
| 5 | Makes the agent classify before writing a skill | PARTIAL | design.md L109, L156 support classification; briefing §3 phrases both test prompts with "skill" as subject | Routing is supported by the design but skill-subject prompts push validation back into a single surface |

Verdict: fidelity to "behavior-asset abstraction routing" is **medium**. The
sharpest miss is briefing §3, which reduced the real requirement into two
skill-subject prompts.

### Correction applied

The reviewer agent's validation methods and briefing §3 are rewritten from
skill-subject to routing-subject form:

- Retrospective test (method 1): sample is "last five occurrences of a repeated
  behavior being noticed", not "last five skills written". Scoring axis is "can
  the model route this to one of the eight surfaces (root / repo / rules /
  skills / wiki / ADR / OpenSpec / do-not-sink)", not "does the model help me
  decide about a skill".
- Forward test (method 2): trigger is "next time a repeated behavior is
  noticed", not "next time I am about to write a skill". Pass signal is
  whichever of the eight surfaces the six-step process selects.
- Briefing §3 question set: replaces "next time I want to write a skill, what
  does the model tell me to check" with "next time a repeated behavior is
  noticed, which of the eight surfaces does the model require me to classify
  against". Replaces "skill duplicates rule, which step catches it" with "a
  repeated behavior can land in two surfaces, which step forces the choice".

The corrections are applied to the reviewer agent's in-conversation outputs
only. No change is made to `design.md`, `spec.md`, the design-trace, or any
Pattern Catalog entry. Whether "do-not-sink" should become an enumerated
eighth pattern in the catalog is **not** decided here; that decision belongs
to a post-archive change if the pattern recurs in real use.

### Why this matters for archive readiness

If the validation methods had run in their original skill-subject form, they
would have exercised one of eight surfaces and reported a pass signal for the
design as a whole. That false pass would have made it look like the design
was validated against the real requirement when only a sliver was tested.
The meta-review surfaces that gap before any real validation run is committed.

Residual risk: even after the routing-subject rewrite, the eight-surface list
is an informal enumeration in this note, not a catalog entry. A follow-up
change may need to decide whether "do-not-sink" is a first-class pattern or
stays as the implicit default. That decision is deferred; this evaluation
records the gap, not the fix.

## Archive-readiness Review Outcome (2026-05-06)

### Scope of this review

This section closes task 5.5 (archive-readiness review) against the Archive
Readiness Criteria recorded in `design.md`. It records the three review
decisions that were open at §Design Decision Proposed For Review and confirms
that the change is ready to archive.

This review does not edit any root dotfile, repo skill, root rule, or wiki
method page. The quantified review criteria in `design.md` (0 root dotfile
edits, 0 repo skill edits, 0 root rule edits, 0 wiki method page edits)
remain intact. Root edits belong to a successor change.

### Decisions

**D1 — Adopt the governance model.**
The six Design Principles (`design.md` L103–141), the Minimum Process
(L143–166), the Self-Check Checklist (L168–228), the Pattern Catalog
(L230–402), the Pattern Skeleton Examples (L404–616), and the Issue Routing
Table (L740–789) are adopted as the repository's behavior-asset governance
model. Every principle is anchored on class A or class B evidence already
recorded in `design.md` §Benchmark Signals; the model has passed the two
audits recorded earlier in this file (Anthropic prompt-engineering gate
validation and skill-gate-vs-abstraction-routing meta-review).

Closes tasks 2.1, 2.2, 2.3, 2.4, 3.7, 3a.5, 3b.8, 3b.9, 3b.17.

**D2 — Keep `SHOULD` for Pattern Catalog field declaration.**
`spec.md` requirement "Behavior-asset changes SHOULD declare Pattern Catalog
fields before completion" remains `SHOULD`. Promotion to `SHALL` is deferred
until three real pattern additions in successor changes verify that the
five-field shape is workable. Reason: the five-field shape has been used
once (this change itself); promoting to `SHALL` on a single use would bind
future authors to a form that has not been road-tested.

Closes task 3b.15. `spec.md` is not edited in this archive pass.

**D3 — Skill rule-preamble stays opt-in.**
The skill rule-preamble field remains an optional declaration in `SKILL.md`
rather than a required field. Reason: required would retroactively
invalidate every existing `.codex/skills/*/SKILL.md` file in the repository
and in `~/.codex/skills/`; the repository has 14 in-repo skills and 56
global skills as of 2026-05-06. The opt-in shape is consistent with
Principle 3 (triggered over ambient) — a skill that does not declare rule
dependencies loads no rules.

Closes task 3b.16.

### Other closed tasks

- Task 2.5: targeted wiki trace is already landed at
  `wiki/ops/behavior-asset-governance-design-trace.md` (with §14 language
  carve-out) and the Chinese companion at
  `wiki/ops/behavior-asset-governance-zh.md`. No retro, method page, or ADR
  is promoted in this archive pass; method/ADR promotion is deferred to a
  successor change if the pattern recurs.
- Task 2.6: harness Phase 1 proceeds as manual templates only. Checker work
  stays deferred to Phase 2 per `design.md` §Phased Change Path.
- Task 2.7: claude-side symmetry is confirmed out of scope for this change;
  reopen after the Codex protocol is applied.
- Task 4.1 / 4.2: not applicable. This change does not require any root-
  level edits to make the reviewed model visible; the model is fully
  visible in `design.md`, `spec.md`, this `evaluation.md`, the design
  trace, and the Chinese companion.

### Evidence chain

- `design.md` L103–410 + L740–789 — the adopted model.
- `spec.md` four requirements — the `SHALL` commitments, `SHOULD` binding
  for field declaration unchanged.
- `evaluation.md` §Anthropic Prompt-Engineering Gate Validation (2026-05-05)
  — heuristic validation.
- `evaluation.md` §Skill-gate vs. Abstraction-routing Meta-review
  (2026-05-05) — codex back-check that the reviewer's recommendations
  matched the design's real goal; verified faithful in a second codex pass
  on 2026-05-06.
- `wiki/ops/behavior-asset-governance-design-trace.md` §13 — anti-drift
  rules; subsequent non-archive edits are drift by rule.

### Residual risks after archive

- `~/.codex/AGENTS.md` remains at 281 lines. Compression / routing of the
  18 intake findings (C1–C3 / S1–S5 / A1–A5 / M1–M5) belongs to a
  successor change, which will use the adopted model as its input.
- The other three in-flight changes (`phase1-repo-agents-compression`,
  `decide-no-repo-local-commit-hook`,
  `close-agents-governance-candidate-materials`) stand at zero progress
  since 2026-04-21. They are not closed by this archive; whether they
  stay, get renamed, or get withdrawn is a separate decision once the
  Phase 1 disambiguation in trace §13 is resolved.
- The "do-not-sink" eighth landing surface is not enumerated in the
  Pattern Catalog; it is recorded as a gap in the meta-review section
  above. Promotion to a catalog entry waits for a recurring case.

### Outcome

Archive-readiness review: PASS. The change is ready for
`openspec archive decide-root-governance-alignment`. The next change opened
against `~/.codex/AGENTS.md` will use this adopted model as its input.

## Residual Risks

- No root dotfile has been edited yet, so runtime behavior has not changed.
- No skill has been authored or modified, so skill trigger behavior remains
  untested.
- Root rules and behavior-asset routing have not been changed, so this repair
  does not alter execution constraints.
- Replay-harness v1 remains evidence only; it has not been converted into a
  hook, CI gate, runtime gate, or enforcement path for this topic.
- The final root/repo alignment model, ownership responsibility, and
  root/repo-aware responsibility split remain open pending review.
- The optional minimum sync tasks remain open and must not be treated as done
  until root-level edits, if any, are separately accepted and verified.

## Post-archive Clean-up (2026-05-06)

- `close-agents-governance-candidate-materials` was withdrawn on 2026-05-06.
  The candidate / mainline relationship it aimed to record is now covered
  by this change's Pattern Catalog (decided), design-trace §13 anti-drift
  rules, and the routing table adopted under D1. Keeping it open would
  duplicate governance that is already visible in accepted artifacts.
- `phase1-repo-agents-compression` was parked on 2026-05-06, not
  withdrawn. Scope (repo AGENTS compression) is independently legitimate,
  but the name conflicts with the intake §12 "Phase 1 = manual harness
  template" definition and the right sequencing is to compress root
  `~/.codex/AGENTS.md` first, then revisit repo compression with real
  experience.
- `decide-no-repo-local-commit-hook` stays open untouched — it is an
  independent small SHALL-NOT decision whose content is unrelated to this
  change's model and will be handled after root compression.
