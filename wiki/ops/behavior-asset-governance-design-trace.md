---
title: behavior-asset-governance / design-trace
type: design-trace
canonical_object: behavior-asset-governance
artifact_type: design-trace
language: en
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: decided
updated_at: 2026-05-06
ai_generated: true
policy_waiver: design-trace-english
policy_waiver_note: >
  Covered by wiki/language-policy.md "design-trace 英文豁免" carve-out.
  Chinese companion: wiki/ops/behavior-asset-governance-zh.md.
derived_from:
  - openspec/changes/decide-root-governance-alignment/design.md
  - openspec/changes/decide-root-governance-alignment/specs/root-governance-alignment/spec.md
  - openspec/changes/archive/2026-05-06-decide-root-governance-alignment/evaluation.md
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/agent-harness-article-learning.md
  - openspec/changes/compress-root-agents-budget/proposal.md
  - openspec/changes/phase1-repo-agents-compression/proposal.md
  - AGENTS.md
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  - https://github.com/anthropics/skills
  - https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
  - https://arxiv.org/html/2602.11988v1
  - https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b
  - https://github.com/danielrosehill/Agents.md-Templates
  - https://raw.githubusercontent.com/openai/codex/main/AGENTS.md
  - https://www.philschmid.de/agent-harness-2026
  - https://calv.info/agents-feb-2026
  - https://github.com/github/spec-kit/blob/main/spec-driven.md
  - https://inspect.aisi.org.uk/
  - https://www.promptfoo.dev/docs/red-team
  - https://promptfoo.dev/docs/integrations/ci-cd/
related_objects:
  - codex-global-agents-md
  - agents-governance-drift
  - root-governance-alignment
  - agent-harness-article-learning
  - compress-root-agents-budget
  - phase1-repo-agents-compression
notes_scope: Candidate design-trace of the design currently under review in
  decide-root-governance-alignment. Captures candidate principles, candidate
  minimum process, candidate self-check, three ASCII diagrams, a pattern
  catalog summary, the 2026-05-04 patch round that resolved the codex review
  items, and a benchmarking note comparing the design against public
  governance / harness examples. Non-decided. Not a method page, not an ADR.
  Original external references come from the codex-global-agents-md intake.
  Anthropic Agent Skills URLs are newly added for the Skill pattern; their
  claims are not re-verified here beyond the Anthropic docs themselves. The
  2026-05-04 public-example URLs are benchmark signals only, not imported
  policy. The `wiki/ops` artifact_type `design-trace` is proposed by the
  active change's design.md; it becomes an accepted artifact_type only after
  the change is archived. Page body is English under the
  `wiki/language-policy.md` "design-trace 英文豁免" carve-out; the Chinese
  companion summary is `wiki/ops/behavior-asset-governance-zh.md`. See §14.
  §15 is a post-archive successor calibration note; it does not rewrite the
  original design-trace body.
---

# behavior-asset-governance / design-trace

## 1. Purpose

This page is a candidate design-trace of the design currently under review
in `openspec/changes/decide-root-governance-alignment/`. Every rule below
is proposed, not decided. Promotion to a method page or an ADR requires the
active change to close first.

The trace records four proposals:

- candidate principles that would constrain every behavior-asset change,
- a candidate minimum process that would apply when editing a behavior-asset
  layer,
- three ASCII diagrams for layer domains, authority order, and process
  rhythm,
- a seven-entry pattern catalog summary pointing at the authoritative
  catalog in `design.md`.

External reference provenance: original benchmark URLs (GitHub Blog 2,500
repos study; arXiv 2602.11988; skyzyx instruction budget gist;
danielrosehill Agents.md-Templates; openai/codex raw AGENTS.md) are carried
by `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` §3.
Anthropic Agent Skills URLs used in the Skill pattern are inherited from the
active change's `design.md`; they are not re-verified here beyond what the
Anthropic docs themselves state.

## 2. Candidate Principles

Each principle is labeled as a candidate; it becomes binding only if the
active change is reviewed and accepted. Provenance tags point to internal
inputs; the intake carries the external URLs.

1. *Candidate principle — source of truth per layer.* Each behavior
   statement should live in exactly one layer; other layers should
   reference rather than duplicate. (provenance: design.md principle 1
   — repo `AGENTS.md` Skill Authoring Contract "complements, but does
   not replace" + Benchmark Signals class B GitHub Blog 2,500 repos
   study six core areas)
2. *Candidate principle — load order is not authority order.* Nearer
   layers are easier to discover; nearness should not grant override
   rights over repo governance. (provenance: intake §3 — official
   `agents.md` precedence; repo `AGENTS.md` High-Frequency Principles —
   principle-skills "complements, but does not replace")
3. *Candidate principle — triggered over ambient.* `rules/` would load
   by work-type match; `skills/` would load by explicit `/name` or
   stated intent; ambient `AGENTS` content should stay entrance-card
   sized. (provenance: Anthropic Agent Skills engineering post —
   progressive disclosure and dynamic loading; intake §3 —
   skyzyx-Humanlayer 150–200 instruction budget)
4. *Candidate principle — instruction budget is finite.* Root
   `AGENTS.md` is a shared budget across all repos; adding repo-specific
   rules to root should be avoided. (provenance: intake §4.1 measurement
   — 223 to 281 lines over 24 days; intake §3 — skyzyx-Humanlayer budget
   guidance)
5. *Candidate principle — evidence precedes runtime change.* Behavior
   asset edits should carry before-and-after evidence; replay-harness
   evidence should be added only when trigger or refusal semantics
   change. (provenance: in-repo harness shape —
   `wiki/ops/disagreement-management-replay-harness.md`; repo
   `AGENTS.md` High-Frequency Principles — "evaluation.md is the
   behavior-proof artifact")
6. *Candidate principle — candidate versus decided is visible.*
   Non-accepted rules should be labeled `candidate` or `proposed for
   review`; spec requirements should use `SHALL` or `MUST` only after
   explicit review. (provenance: intake §11 quantification audit —
   retracting unverified claims)

## 3. Layer Domain Map

Each layer has its own proposed domain of responsibility. Edges describe
proposed authority or loading relationships — not yet runtime rules.

```
      ┌─────────────────────────────────────────────────────┐
      │ root ~/.codex/AGENTS.md                             │
      │   domain: cross-repo safety floor, entrance routing │
      │   owns:   destructive git gate, external call gate, │
      │           dirty-tree gate, hard stops               │
      └────────────────┬────────────────────────────────────┘
                       │ candidate: should not be loosened
                       ▼
      ┌─────────────────────────────────────────────────────┐
      │ repo AGENTS.md                                      │
      │   domain: repo-local policy, workflow triggers,     │
      │           delivery boundaries                       │
      │   owns:   OpenSpec triggers, wiki routing, skill    │
      │           contracts                                 │
      └──────┬──────────────────────────────────┬───────────┘
             │ candidate: loads rules           │ candidate: authorizes
             ▼ by work-type                     ▼ complements
      ┌──────────────────┐            ┌───────────────────┐
      │ ~/.codex/rules/  │            │ .codex/skills/*   │
      │   common/        │            │ ~/.codex/skills/* │
      │   python/        │            │   trigger-gated   │
      │   web/           │            │   /name or intent │
      │   ambient by     │            │   complements     │
      │   work-type      │            │   repo governance │
      └──────────────────┘            └───────────────────┘

      evidence lanes (orthogonal to layers):
        OpenSpec change   ── proposes, designs, tracks
        evaluation.md     ── before/after results
        replay-harness    ── trigger/refusal semantics only
        wiki/ops trace    ── design snapshots, not methods
```

Reading notes:

- The edge from root to repo is proposed as a floor, not a push. Root would
  set hard stops; repo would not loosen them.
- The two edges under repo go to different proposed loading models. `rules/`
  would load automatically when the work type matches. `skills/` would load
  only when triggered.
- Evidence lanes would be orthogonal. A change may need OpenSpec, evaluation,
  and harness evidence, or only a subset, depending on what it edits.

## 4. Authority versus Load Order (candidate distinction)

Two orders would be distinct. Confusing them caused this round's correction.

```
  load order (discovery):                authority order (governance):

  root AGENTS.md                         root safety floor
        │ loads first                          │ candidate: not loosened
        ▼                                      ▼
  repo AGENTS.md                         repo AGENTS.md
        │ loads next                          │ candidate: governs repo
        ▼                                      ▼
  triggered skill                        skills complement
        │ loads on /name                      │ candidate: may tighten
        ▼                                      ▼
      (nearest)                        (no override without carve-out)

  NEAR is not AUTHORITATIVE.  Nearness tells you what you can SEE last;
  authority would tell you who can SAY last.
```

Candidate implication: a skill that appears to contradict repo `AGENTS.md`
should not be treated as the override. The skill would be asking for a repo
`AGENTS` carve-out that does not yet exist. Candidate fix path: update the
authority chain via OpenSpec, not the skill directly.

## 5. Candidate Minimum Process Rhythm

Six proposed steps, candidate. Each step would bind to one of the candidate
principles.

```
  declare  →  source-of-truth  →  authority  →  surface  →  evidence  →  self-check
    │           check               check         pick        record        pass
    │           (Principle 1)       (P2)          (P3/P5)     (P5)          (P6)
    │
    ▼
  (layer + semantic weight)

  candidate surface picker (P3, P5):
    root AGENTS edit ─────────────► OpenSpec change proposed
    skill trigger / refusal edit ─► OpenSpec change proposed
    repo AGENTS edit ─────────────► OpenSpec change OR in-repo decision record
    pure wording / routing ───────► in-repo edit acceptable

  candidate evidence picker (P5):
    semantic edit       ─► evaluation.md before/after proposed
    trigger/refusal     ─► add replay-harness fixture proposed
    wording only        ─► no harness proposed

  candidate gate (P6):
    any task complete? ─► self-check proposed before completion
```

## 6. Candidate Self-Check Snapshot

Authoritative form lives in
`openspec/changes/decide-root-governance-alignment/design.md` (Self-Check
Checklist section). Short candidate form for daily reference:

- structural: `openspec validate` passes; `openspec change show ... --json
  --deltas-only` shows complete sentences; `deltaCount` matches declared
  scope
- semantic: target layer declared; authority precedence respected; source of
  truth single; candidate items labeled
- evidence: `evaluation.md` updated; harness attached if trigger or refusal
  changed; intake or prior trace referenced
- boundary: diff scope matches `Impact`; Phase 0 promise intact if
  applicable

## 7. Pattern Catalog Summary

Seven candidate pattern types. Each line points to the authoritative entry
in `design.md` (Candidate Pattern Catalog) for the full five fields
(Purpose / Owns / Must Not Own / Required Evidence / Anti-patterns) and
references.

- **Root AGENTS pattern** — cross-repo safety floor and entrance routing;
  owns hard stops; must not carry repo policy → see design.md § Candidate
  Pattern Catalog.
- **Repo AGENTS pattern** — repo-local policy, OpenSpec triggers, skill
  contracts; must not replace root safety floor → see design.md.
- **Rule pattern** — ambient, work-type-matched constraints; must not do
  task orchestration; internal observation, no external source → see
  design.md.
- **Skill pattern** — on-demand behavior contract with `SKILL.md`,
  references/, scripts/; cites Anthropic Agent Skills post and
  anthropics/skills README → see design.md.
- **OpenSpec change pattern** — lifecycle container; must not become
  long-term knowledge base; internal observation, no external source → see
  design.md.
- **Harness pattern** — replay evidence artifact; must not act as runtime
  gate; internal observation, no external source → see design.md.
- **Wiki / ADR / retro pattern** — durable learning and stable-decision
  layer; must not publish method pages before the active change closes;
  internal observation, no external source → see design.md.

## 8. Change Anchor

Active OpenSpec change:
`openspec/changes/decide-root-governance-alignment/`.

Primary internal inputs (see frontmatter `derived_from` for the full list):

- `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` —
  intake that surfaced the original drift, the fact-checked measurement,
  and the external benchmark URLs
- `AGENTS.md` — repo entrance card whose `principle-skills complements,
  but does not replace` clause is the authority anchor for this design
- `openspec/changes/decide-root-governance-alignment/design.md` — the
  design currently under review; this trace tracks its candidate rules
- Anthropic Agent Skills engineering post and anthropics/skills README —
  cited only by the Skill pattern

## 9. Proof Boundary

**Verified by this trace**

- Candidate principles 1, 4, and 6 trace back to the intake's `Benchmark
  Signals` and §11 fact-check. The measurement 223 → 281 lines over 24
  days is from intake §4.1 and §11 quantification audit.
- Candidate principle 2 traces to repo `AGENTS.md` "principle-skills
  complements, but does not replace, repo governance".
- Candidate principle 3 traces partly to the Anthropic Agent Skills post
  (progressive disclosure, dynamic loading) and partly to the intake
  (skyzyx instruction budget).
- Candidate principle 5 traces to the in-repo harness shape and repo
  `AGENTS.md`; this was corrected away from the earlier overstated
  attribution to "OpenAI skills catalog + Vercel agent-skills template".

**Not verified by this trace**

- No runtime behavior is changed. The authority correction is stated as a
  candidate; root, repo, rule, and skill files are not edited.
- Claims inside the Anthropic Agent Skills post are not re-verified here;
  they are cited by direct URL and reading.
- No replay-harness fixture is added. The Phase 0 promise in the active
  change stays intact.

**Candidate only**

- The six principles, six process steps, and seven pattern types remain
  candidate pending review against `tasks 3b.8` (Design Principles),
  `3b.9` (Self-Check Checklist), `3b.15` (Pattern Catalog field-declaration
  SHOULD → SHALL promotion), `3b.16` (Skill rule-preamble opt-in vs required),
  and `3b.17` (`candidate-root-edit` row recheck) in the active change.
- This trace is the wiki-visible candidate; promotion to `wiki/methods/`
  or `wiki/adr/` would require the active change to close first.

## 10. External Provenance

Full URL list for every external source cited in this trace, in the active
change's `design.md`, and in the Pattern Catalog. Listed here so a reader
does not have to walk through the intake to find them. Verification status
refers to whether the source itself was fact-checked in-repo, not whether
its content was independently re-verified in this trace.

**Anthropic-normative (cited directly by this trace's Skill pattern)**

- `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills`
  — Anthropic Agent Skills engineering post, 2025-10. Source for
  progressive disclosure, dynamic loading, and the code-as-documentation
  pattern. Verification: cited by URL; claims inside the post are not
  independently re-verified here.
- `https://github.com/anthropics/skills` — anthropics/skills README.
  Source for the `SKILL.md` frontmatter contract: required `name` and
  `description`; optional `disable-model-invocation`, `user-invocable`,
  `allowed-tools`. Verification: cited by URL and direct reading.

**Fact-checked in `codex-global-agents-md` intake §3 (2026-04-29)**

- `https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/`
  — GitHub Blog, "how to write a great agents.md" 2,500+ repos study.
  Source for six core AGENTS areas: commands / testing / project structure
  / code style / git workflow / boundaries. Verification: intake §3 +
  §8 + §11 quantification audit; the post contains no line-count
  recommendation, so any "recommended line count" claim from this source
  is disallowed.
- `https://arxiv.org/html/2602.11988v1` — arXiv 2602.11988. Source for
  context-file cost: LLM-generated context files show average 20% / 23%
  inference cost increase on SWE-bench Lite / AGENTbench; developer-
  provided context files show at most 19%. Verification: intake §3 +
  §11.
- `https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b` —
  skyzyx instruction-budget gist, citing Humanlayer Kyle. Source for
  the 150–200 instruction budget guideline and "AGENTS.md as small as
  possible". Verification: intake §3 + §11.
- `https://github.com/danielrosehill/Agents.md-Templates` — danielrosehill
  community template index. Source for sample shape only; not a normative
  specification. Verification: intake §3 recorded 9 template entries
  across project-type / purpose-outline / stack-context / sysadmin
  directories.
- `https://raw.githubusercontent.com/openai/codex/main/AGENTS.md` —
  openai/codex current `AGENTS.md`. Source for short entry-card shape.
  Verification: intake §3 + §11; current raw size on 2026-04-29 is 40
  lines, which supersedes earlier recorded sizes.

**Inherited benchmark names without independent URL verification**

The active change's `design.md` `Benchmark Signals` section lists five
additional sources by name (OpenAI skills catalog, Claude skill guidance,
GitHub Copilot skills docs, Vercel agent-skills template, getsentry
agents-md guidance). These are stated as benchmark inputs rather than
imported policy. The present trace has corrected its earlier attributions
so that candidate principle 3 and candidate principle 5 no longer rely on
these unverified names; they now rely on the Anthropic-normative and
fact-checked sources above. If a later revision of the Pattern Catalog
restates a dependency on any of the five unverified names, it SHOULD first
add a URL and a verification note here.

**In-repo sources (not external, for completeness)**

- `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md` —
  originating intake; carries the fact-check history for every external
  URL above.
- `AGENTS.md` — repo entrance card; carries the
  "principle-skills complements, but does not replace" clause used as the
  authority anchor.
- `.codex/skills/clarify-before-acting/SKILL.md`,
  `.codex/skills/verify-before-claiming/SKILL.md`,
  `.codex/skills/openspec-propose/SKILL.md` — worked examples of the
  Skill pattern.
- `wiki/ops/disagreement-management-replay-harness.md` and
  `scripts/disagreement_replay_check.py` — canonical shape for the
  Harness pattern.

## 11. 2026-05-04 Patch Round: codex 7 Items Plus Archive-Readiness

### Trigger

A codex-side review flagged seven issues in the active change
`decide-root-governance-alignment`. The issues clustered around one root
cause: `candidate / under-review / accepted / spec-bound` were not isolated
as four separate states, so `spec.md` had started carrying `SHALL`
clauses whose review gates were still open in `tasks.md`.

### What changed in the design (applied 2026-05-04)

- **Pattern Catalog field declaration** in `spec.md` downgraded from `SHALL`
  to `SHOULD`; promotion to `SHALL` is gated on a new task `3b.15`. The
  corresponding `design.md` preamble was updated to say the SHOULD-to-SHALL
  promotion is itself a candidate.
- **Self-Check Checklist** adopts a three-state declaration rule —
  `applicable` / `not applicable` / `blocker` — so design-only or
  candidate-only changes are not trapped by checklist items that do not
  apply to them. `spec.md` scope was narrowed from "any task" to
  "any behavior-asset editing task".
- **Phase 0 permitted wiki changes** tightened to an exhaustive
  two-item list: the intake at `codex-global-agents-md-diagnosis-intake-
  2026-04-25.md` and the design-trace at `behavior-asset-governance-design-
  trace.md`. Earlier text said "one intake learning update" while the
  Quantified Review Criteria already allowed a trace file; that
  contradiction is resolved.
- **Design-trace lifecycle** language changed from
  "upon archive the content promotes" to "archive review decides whether
  to promote; promotion is never automatic". The trace either promotes,
  stays as a frozen candidate, or is retracted — the archive review
  makes the call.
- **Interaction Protocol §1** (skill rule-preamble) downgraded from
  "triggered skills SHALL load declared rules" to opt-in: a skill MAY
  declare rule dependencies; when it does, triggering SHALL load them.
  This avoids back-imposing a new required field on every existing
  `SKILL.md`. Task `3b.16` tracks whether the opt-in becomes a required
  Skill-pattern field later.
- **Issue Routing Table class** renamed from `edit-here` to
  `candidate-root-edit`. The old name was easy to misread as "edit inside
  this change", while the actual semantics is "after protocol acceptance,
  editable in the named layer, deferred to a successor change". Task
  `3b.17` does a line-by-line recheck of the renamed rows.
- **Archive Readiness Criteria** added as a new section in `design.md`,
  listing exactly which tasks and which `spec.md` invariants must hold
  before archive review is allowed. The previously open question "what
  evidence is required before archive readiness?" is retired.

### State after the patch

- `openspec validate decide-root-governance-alignment --strict` passed on
  2026-05-04 and was re-run successfully on 2026-05-05; the PostHog telemetry
  DNS failure observed in the command output is unrelated network noise, not
  a validation failure.
- `spec.md` contains no `SHALL` or `MUST` whose review gate is still open,
  after the Pattern Catalog downgrade.
- At the design-document level, Phase 0 file-edit scope is internally
  consistent: `design.md` Phase 0 list and Quantified Review Criteria name the
  same two wiki files plus the change artifacts. Working-tree diff consistency
  is a per-commit check and not a durable property of this trace; any commit
  covering the change must exclude files outside this scope at commit time.
- Tasks 3b.15 / 3b.16 / 3b.17 are the remaining candidate-pattern review
  gates; tasks 2.1–2.7 and 3.7 / 3a.5 / 3b.8 / 3b.9 remain the substantive
  review gates tracked by Archive Readiness Criteria.

### Discussion-round accounting

Design-side discussion counts for this trace are now: intake 5 revisions
(2026-04-25 → 2026-04-29), OpenSpec change 8 commits (from `1774680` through
`a98305e`) plus the 2026-05-04 working-tree patch captured above. Further
"new round of design" has diminishing returns; what remains is running the
review gates, not writing more design. This note is recorded here so a
future reader does not re-open the patch loop by mistake.

## 12. 2026-05-04 Public-Example Benchmarking

### Trigger

The user asked to look at public discussion on progressive governance and
harness models before closing this design. The research below is recorded
here, not in `design.md`, because these are benchmark signals, not accepted
sources. Only one item (§12.4) led to a design-level recommendation.

### 12.1 philschmid — agent harness 2026

`https://www.philschmid.de/agent-harness-2026` defines `agent harness` as
"the infrastructure that wraps around an AI model to manage long-running
tasks … an operating system layer". This is a **runtime wrapper** meaning,
not an evidence pack. The author's progressive argument is "stay
lightweight and modular; each new model generation will want a different
harness".

Usable signal: trajectory-log-as-training-feedback. The in-repo
`replay-harness.md` records RED/GREEN but not trajectory; if Phase 1
adds a trajectory field, that part has a public reference.

Not usable: the name collision (see §12.6) means this is the dominant
public meaning of "harness", different from the one used in this design.

### 12.2 calv.info — coding agents Feb 2026

`https://calv.info/agents-feb-2026` treats harness-ish governance as
evidence-driven and emphasises incremental automation:
"I don't think I would've had any success trying to start with this
process. But by building it over time and noticing little areas where I
could automate, it's significantly improved my workflow."

This is the public source that most closely matches the Phase 0 → Phase 3
plan in `design.md`. It is a vote of confidence for the current phased
rhythm; no design change needed.

### 12.3 GitHub spec-kit

`https://github.com/github/spec-kit/blob/main/spec-driven.md` uses a
three-command flow (`/speckit.specify` → `/speckit.plan` →
`/speckit.tasks`) with "Phase -1 Pre-Implementation Gates" enforced as
constitutional checks. Compliance is binary.

Relationship to this repo's design: **deliberately opposite direction.**
Principle 6 ("Candidate versus decided is visible") keeps `candidate`,
`proposed for review`, and `open question` as first-class states; spec-kit
collapses those into enforced gates. The design should not drift toward
spec-kit's enforcement model.

### 12.4 UK AISI Inspect AI

`https://inspect.aisi.org.uk/` is an LLM evaluation framework. Its public
surface documents Log Viewer, Log Files, and Eval Sets as evidence-review
tooling, which makes it closer to this repo's review-evidence harness
than to a runtime gate. Progressive adoption is supported by the same
surface: evaluations can start small and scale through reusable
components.

This is the closest public match to the harness definition in
`design.md` §Harness pattern. Usable signal: `.eval` log structure is
more disciplined than the current "markdown or JSON fixture" shape. A
Phase 1 decision could reasonably borrow a minimal frontmatter contract
from Inspect for fixture files. Flagged as a future-round consideration,
not applied in the current patch.

### 12.5 promptfoo red-team and CI/CD

`https://www.promptfoo.dev/docs/red-team` and
`https://promptfoo.dev/docs/integrations/ci-cd/` show eval suites running
either as one-off reports or as CI/CD gates. There is no documented
"shadow mode" that records without blocking. The jump from "eval exists"
to "eval blocks CI" is one step.

Relationship: the Phase 2 → Phase 3 boundary in this design
intentionally inserts "three real behaviour-asset changes must use the
manual shape before checker output connects to any gate". That buffer is
what promptfoo lacks. Do not remove the buffer.

### 12.6 Terminology caveat — "harness" collision

In the public 2026 discourse the default meaning of "agent harness" is
philschmid's runtime wrapper, not a design-review evidence pack. The
`design.md` §Harness pattern definition in this change is narrower and
local. A one-line terminology caveat is now present at the top of
`design.md` §Harness pattern (lines 359–361), distinguishing this
design's harness-as-evidence meaning from the dominant runtime-wrapper
meaning so a reader cross-referencing public posts is not misled. No
further action required here; this note is retained for traceability.

### Overall assessment

The design's harness-as-evidence model is aligned with Inspect AI and
calv.info, intentionally opposed to spec-kit's constitutional gates,
and uses a deliberately wider buffer than promptfoo before automation
kicks in. Relative to public examples, the design is slightly
conservative, and conservative in the right direction. No public
example argues the current Phase 0 → Phase 3 path is wrong; the only
two items worth carrying forward are (a) the Inspect-style fixture
structure for Phase 1 and (b) the terminology caveat against the
dominant public meaning of "harness".

## 13. 2026-05-05 Drift Convergence — Main-Line Lock

### Trigger

The 2026-05-04 patch round (§11) resolved seven codex-review items. Follow-up
review rounds on 2026-05-05 continued surfacing new copy-edit items in this
trace — open-task ID set, tense of durable claims in §11, frontmatter
metadata nits, working-tree pollution, §12.6 wording. Every round closed
with an internally consistent trace, then another round found new items.
The pattern itself is drift: the governance change is spending all its
energy refining the description of its own model instead of accepting it.
This section locks the main line so subsequent copy-edit rounds are
recognizable as drift rather than progress.

### State (2026-05-05)

- This trace is internally consistent; `openspec validate
  decide-root-governance-alignment --strict` passes.
- Archive-readiness review completed 2026-05-06; D1/D2/D3 adopted as
  "use / SHOULD / opt-in". See
  `openspec/changes/decide-root-governance-alignment/evaluation.md`
  §Archive-readiness Review Outcome.
- The governance model (six principles, four-layer catalog, six-step
  process, three evidence lanes) is sourced entirely from class A and
  class B references. Content is ready; only review decisions are pending.
- `openspec list --json` shows four in-progress changes, but only
  `decide-root-governance-alignment` has advanced (30/47) in the past two
  weeks. `phase1-repo-agents-compression` (0/10),
  `decide-no-repo-local-commit-hook` (0/7), and
  `close-agents-governance-candidate-materials` (0/8) stand at zero since
  2026-04-21.
- `~/.codex/AGENTS.md` remains at 281 lines. No behavior file has been
  edited by this change or the other three in-flight changes.
- This trace is `language: en` under the newly-added
  `wiki/language-policy.md` design-trace carve-out; a Chinese companion
  page `wiki/ops/behavior-asset-governance-zh.md` covers zh-CN intake.

### Main line

> Make three decisions → archive `decide-root-governance-alignment` →
> resolve the Phase 1 disambiguation → close or consolidate the other three
> in-flight changes → then open a new change that actually touches
> `~/.codex/AGENTS.md`.

### Three review decisions

| ID | Gate | Recommendation |
|---|---|---|
| D1 | Adopt the six principles + four-layer catalog + six-step process as the repo's governance model? | Adopt. Every principle anchored on class A or B sources. |
| D2 | Pattern Catalog five-field declaration: `SHOULD` or `SHALL` in `spec.md`? | Keep `SHOULD`. Promote only after three real pattern additions in the field verify the five-field shape is workable. |
| D3 | Skill rule-preamble: required field on every `SKILL.md` or opt-in? | Opt-in. Required would retroactively invalidate existing `SKILL.md` files. |

Accepting these three closes tasks 2.1–2.4, 3.7, 3a.5, 3b.8, 3b.9, 3b.15,
3b.16, 3b.17 in one sweep. Tasks 2.5–2.7, 4.1, 4.2, 5.5 are parked,
conditional, or final-gate and close mechanically afterward.

### Phase 1 disambiguation

"Phase 1" carries two incompatible meanings in repo history; archive review
must pick one and retract the other:

- **intake §12 phased recommendation**: Phase 1 = build a manual harness
  template; no behavior-file edits.
- **OpenSpec change `phase1-repo-agents-compression`**: Phase 1 = compress
  the repo `AGENTS.md` file.

Both cannot hold. The intake definition is the earlier one and is the one
this design-trace implicitly assumes. If archive review confirms the intake
definition, `phase1-repo-agents-compression` needs to be renamed or
re-scoped; if archive review confirms the change-name definition, the
intake phased recommendation needs a retraction note.

### Anti-drift rules (2026-05-05)

1. **No further copy-edit** of `design.md`, `spec.md`, or this trace for
   the remainder of `decide-root-governance-alignment`. Any additional
   "one more polish" belongs to drift, not progress. The only allowed edit
   to this trace from this point is the archive-readiness outcome under
   task 5.5.
2. **One governance design change in-progress at a time.** The current
   four-way parallel is itself a drift symptom — it mirrors the root
   `AGENTS.md` growth pattern this change was meant to address.
3. **Retracted figures stay retracted.** The "40-line" openai/codex
   observation was retracted to an observation, not a target, in intake
   §11. Any Phase 1 or Phase 2 discussion that reintroduces a target line
   count for root `AGENTS.md` without a new verified source is rejected.

### Status

This section is the last non-structural edit to this trace before archive
review. Subsequent edits that are not an archive-readiness update under
task 5.5 are drift by the rule above.

## 14. Language-policy Compliance

### Status (2026-05-05)

Covered by `wiki/language-policy.md` "design-trace 英文豁免" carve-out.
Frontmatter carries `policy_waiver: design-trace-english`. Chinese
companion page: `wiki/ops/behavior-asset-governance-zh.md`.

### Why this page is English

Upstream artifacts are English (`openspec/changes/.../design.md`,
`spec.md`, the bulk of external references). Drafting continued in
English and subsequent edit rounds focused on codex-review items,
frontmatter nits, and drift-convergence (§13), not on language policy.

### Why the carve-out is narrow

Carve-out applies only when all three conditions hold: `artifact_type:
design-trace`, `derived_from` majority-English, and a same-directory
Chinese companion page exists. It does not extend to method pages, ADRs,
sources, reports, intake summaries, `rules/`, or `skills/` — those
remain governed by `wiki/language-policy.md` main rules and
`openspec/specs/skill-authoring-contract/spec.md`.

### Why not translate instead

§13 forbids further copy-edit of this trace until the archive-readiness
outcome under task 5.5. A 655-line translate pass is exactly that kind
of copy-edit. The carve-out + companion-page pattern satisfies the
policy intent (Chinese reader has a first-class entry point) without
forcing a body rewrite that competes with D1/D2/D3 for attention.

### Future action

The carve-out can be revisited after the companion-page pattern sees
two or three real uses. If it turns out the companion pages consistently
duplicate the English trace, fold back into a single-language policy
with appendix. If they diverge usefully (Chinese reader workflow vs.
English design-trace), keep the carve-out as-is.

## 15. 2026-05-06 Post-Archive Successor Calibration

### Trigger

After `decide-root-governance-alignment` was archived, two successor changes
remained easy to confuse:

- `compress-root-agents-budget`
- `phase1-repo-agents-compression`

The later `agent-harness-article-learning.md` page also became the durable
source-of-record for external agent / harness / eval article learning. This
section records how those facts calibrate successor execution. It does not
reopen the governance design.

### New facts after §13

- `decide-root-governance-alignment` is archived at
  `openspec/changes/archive/2026-05-06-decide-root-governance-alignment/`.
- D1 / D2 / D3 were adopted in the archived change's `evaluation.md`
  §Archive-readiness Review Outcome.
- `wiki/ops/agent-harness-article-learning.md` is now the source-of-record
  for the external article learning pass. It records route, source grounding,
  admission gate, score detail, transfer candidates, and promotion boundaries.
- `compress-root-agents-budget` is the active root successor for
  `~/.codex/AGENTS.md` loaded-context governance.
- `phase1-repo-agents-compression` remains parked. Its own proposal says not
  to proceed while the name conflict and sequencing question remain open.

### What the article learning changes

The article learning does not change the adopted governance model. It
calibrates how successor changes use evidence:

- root `AGENTS.md` should be treated as a map, not a manual;
- line count is supporting evidence, not the success metric;
- loaded context, trigger-gated detail, source-of-record pointers, and
  recovery artifacts are the real target;
- external best-practice claims should cite the learning page or its evidence
  table rather than scattered chat history or raw URL lists;
- unsupported article takeaways remain candidate observations and do not become
  `AGENTS.md` text, spec `SHALL`, skill hard rules, or archive-ready claims.

### Successor split

| Change | Layer | Status | Rule |
|---|---|---|---|
| `compress-root-agents-budget` | root `~/.codex/AGENTS.md` | active successor | Continue first. Govern loaded context and drift, not line count alone. |
| `phase1-repo-agents-compression` | repo `AGENTS.md` | parked | Do not unpark until the root successor run completes and archive review decides rename / unpark / rescope. |

These two changes are not duplicates. They share the adopted governance model
but apply it to different layers. Running them in parallel would recreate the
multi-change drift pattern §13 warned against.

### Required successor correction

Future `compress-root-agents-budget` work should cite
`wiki/ops/agent-harness-article-learning.md` as the durable article-learning
source when using external harness / agent / eval material. It should not
spread the same evidence across chat memory, this trace, older governance pages,
or raw external URLs.

Future `phase1-repo-agents-compression` work should not start from its current
0/10 task list while parked. After the root successor completes, archive review
should decide whether to rename, unpark, or rescope the repo-level change.

### Anti-drift boundary

This section does not:

- edit §2-§14;
- reopen D1 / D2 / D3;
- add a Pattern Catalog entry;
- promote article learning into a spec `SHALL`;
- edit root `~/.codex/AGENTS.md` or repo `AGENTS.md`;
- unpark `phase1-repo-agents-compression`.

## §16 2026-05-06 Repo AGENTS Compression Re-entry

### Trigger

The root successor `compress-root-agents-budget` has completed and archived at
`openspec/changes/archive/2026-05-06-compress-root-agents-budget/`. The user
asked to return to `phase1-repo-agents-compression` under `openspec-explore`.

### Current focus

Explore whether `phase1-repo-agents-compression` should now be renamed,
unparked, or rescoped. The current change remains parked until that decision is
made explicitly.

### Current hypotheses

- Root compression produced a small measured edit, not a broad root rewrite.
- The repo-level problem is still legitimate, but the current change name still
collides with the older intake meaning of "Phase 1".
- The old 0/10 task list should not be executed as-is until the rename /
  unpark / rescope decision is made.

### Open questions

- Should the repo change be renamed away from `phase1-*` before any work?
- Is the target still "compression", or should it be reframed as repo AGENTS
  loaded-context governance?
- Which repo `AGENTS.md` sections are true repo-only hard stops, and which are
  proxies to ADR, OpenSpec specs, wiki ops pages, or skills?

### Next step

Read `phase1-repo-agents-compression` and the archived root-successor evidence,
then decide whether to rename, unpark, or rescope before implementation.

### Anti-drift boundary

This re-entry does not implement repo `AGENTS.md`, alter the parked change's
tasks, or change Pattern Catalog rules. It only records the exploration trigger
and the decision point opened by completion of the root successor.
