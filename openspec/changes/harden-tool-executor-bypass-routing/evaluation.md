# Evaluation: tool executor bypass routing

## Pressure Scenarios

### Positive scenario: H5 visual request mentions image model

- input or situation shape: user names a reader-facing H5/report and asks for
  section visuals while mentioning image-model output.
- trigger condition: the deliverable is reader-facing and no article-level
  visual package or per-image script exists yet.
- expected route: `public-report-quality-gate -> knowledge-article-visual ->
  infographic-onepager -> imagegen`.
- repo-visible artifact:
  `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`,
  `.codex/skills/public-report-quality-gate/SKILL.md`,
  `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`,
  and
  `wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md`.
- expected output: parent gate preserve evidence first, article visual planning
  and per-image scripting next, then bitmap generation only as the final
  executor.
- promotion or non-promotion boundary: this proves repo-visible routing
  evidence for the public report gate; it does not promote a root `AGENTS.md`
  keyword-list patch or make `imagegen` a workflow owner.
- proof boundary: validates behavior-asset wording and replay coverage, not
  automatic runtime dispatch in every future client.

### Positive scenario: Feishu sync follows report drafting

- input or situation shape: user asks to sync a reader-facing report or review
  draft to Feishu.
- trigger condition: the report has a public/readership boundary and Feishu is
  the destination executor.
- expected route: public report gate owns draft readiness, judgment ownership,
  publish/sync approval, and post-write read-back evidence before `lark-doc`
  runs.
- repo-visible artifact:
  `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`
  and `.codex/skills/public-report-quality-gate/SKILL.md`.
- expected output: `lark-doc` remains an executor after the parent gate is
  preserved; Feishu writing does not replace readiness or evidence checks.
- promotion or non-promotion boundary: this preserves the existing public gate
  and does not add a separate Feishu route table.
- proof boundary: validates replay expectations, not Feishu API success or
  client rendering quality.

### Positive scenario: Research lookup follows source-learning work

- input or situation shape: user asks for source-backed public report research
  or lookup.
- trigger condition: browser/search is needed, but source selection, citation
  boundary, and evidence classification still belong to the parent workflow.
- expected route: the source/public-report workflow owns evidence decisions;
  browser and search are executors.
- repo-visible artifact:
  `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`
  and pressure scenarios in
  `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`.
- expected output: source evidence is selected, classified, and bounded before
  lookup results are treated as report evidence.
- promotion or non-promotion boundary: search/browser availability is not
  promoted into authority over public report evidence.
- proof boundary: validates routing and evidence-boundary expectations, not the
  accuracy of any future web result.

### Negative / should-not-trigger scenario: Private source capture

- input or situation shape: user asks only to capture raw meeting notes or
  private source material into `wiki/sources`.
- trigger condition: no reader-facing report, H5/share draft, Feishu review
  draft, or public artifact is requested.
- expected route: material/source capture can proceed through the source
  workflow; the public report gate should-not-trigger.
- repo-visible artifact: repo routing rules in `AGENTS.md` and existing
  high-frequency skill boundaries.
- expected output: source material is captured without public scorecard,
  publish gate, or visual production requirements.
- promotion or non-promotion boundary: no public-report behavior is promoted
  from a private capture task.
- proof boundary: validates non-trigger language, not source quality.

## RED Baseline

Before the change, the 2026-05-18 H5 visual incident demonstrated direct
executor routing. A request for H5 visual work mentioned image-model output, and
the route could jump directly to `imagegen` without preserving the parent gate,
inspecting existing visuals, creating an article-level visual plan, or scripting
each visual through `infographic-onepager`.

Two adjacent RED baselines were also possible:

- Feishu sync could route directly to `lark-doc`, treating the destination tool
  as workflow authority instead of an executor after report readiness,
  judgment ownership, sync approval, and post-write read-back.
- Research lookup could route directly to browser/search, treating retrieved
  results as sufficient report evidence before source selection, citation
  boundary, and evidence classification.

## GREEN Result

The corrected route preserves the public report gate as the parent gate for
delivery-sensitive reader-facing outputs. Visual work delegates in order:

`public-report-quality-gate -> knowledge-article-visual -> infographic-onepager -> imagegen`

The GREEN replay language keeps low-level tools as executors:

- `imagegen` runs only after the visual route, grammar, and per-image scripts
  exist.
- `lark-doc` runs only after the publish/sync and read-back boundaries are
  satisfied.
- browser/search runs only under the workflow that owns source selection,
  citation boundary, and evidence classification.

Parent gate preservation evidence appears in the OpenSpec spec, the public
report gate anti-pattern, the pressure scenarios, and the 2026-05-18 drift ops
trace.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`,
  `openspec/changes/harden-tool-executor-bypass-routing/proposal.md`,
  `openspec/changes/harden-tool-executor-bypass-routing/design.md`,
  `openspec/changes/harden-tool-executor-bypass-routing/specs/public-report-quality-gate/spec.md`,
  `.codex/skills/public-report-quality-gate/SKILL.md`,
  `.codex/skills/public-report-quality-gate/references/pressure-scenarios.md`,
  `wiki/ops/agentic-product-engineering-collaboration-tool-executor-bypass-drift-2026-05-18.md`,
  `wiki/config/behavior-asset-evaluation.yaml`, and common development/git
  rules.
- Owns: the public report gate's local anti-pattern evidence for Tool Executor
  Bypass in reader-facing report, H5, Feishu, and source-research routes.
- References: repo `AGENTS.md` for Agent Intent Routing and High-Frequency
  Skills, the existing public-report-quality-gate parent role, existing
  pressure scenarios, the visual-output-routing/tool-executor-bypass ops trace,
  and behavior asset evaluation requirements.
- Rejects: a root `AGENTS.md` keyword-list patch, a second generic route table,
  making `imagegen`, `lark-doc`, browser, or search the route owner, and
  duplicating generic git/testing/file-size rules already owned by common or
  global guidance.

## Residual Risks

- Behavior asset proof does not guarantee all future clients auto-load the
  skill or dispatch through the corrected route.
- Current H5 assets still need visual QA before any review-ready or share-ready
  claim.
- Direct image-model Chinese text may still require deterministic hybrid
  overlay.
- Existing pressure scenarios are markdown replay evidence, not executable
  dispatch tests.
- Share zip regeneration is out of scope unless explicitly asked.
