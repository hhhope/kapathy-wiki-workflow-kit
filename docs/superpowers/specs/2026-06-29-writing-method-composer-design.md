# Writing Method Composer Design

## Route Status

Route: brainstorm -> superpowers spec; OpenSpec remains read-only until this
brainstorming spec is reviewed and accepted.

This design is a Superpowers brainstorming artifact. It is not authoritative
OpenSpec lifecycle state and does not implement the skill.

## Problem

The repository already has `learning-capture`, `public-report-quality-gate`,
`khazix-writer`, visual skills, and many PM/business analysis skills. They are
useful, but they do not provide a stable pre-writing method layer.

The current failure mode is:

- a user gives a link, company, topic, or draft;
- the agent starts learning or summarizing before asking what the output is
  supposed to do;
- learning methods, evidence search, and writing structure are chosen
  opportunistically;
- PM frameworks such as JTBD, SWOT, Five Forces, battlecards, market sizing,
  AB analysis, and cohort analysis become loose labels instead of proof tools;
- reader-facing drafts then become either source summaries or jargon-heavy
  reports rather than a deliberately composed article, H5, sharing script, PPT,
  or long-form analysis.

The 2026-06-24 learning workflow matrix defined L0-L3 learning levels and
research methods. It intentionally left public-writing transformation as a
downstream layer. The missing piece is now clear: for article-class work, the
writing method must be selected before learning execution, because the intended
article shape determines what must be learned, searched, validated, and
expressed.

## Design Goal

Add a repo-local skill named `writing-method-composer` as the single normal
entry controller for article-class methodology composition.

It should force this sequence:

```text
user intent
  -> classify writing/output intent
  -> build Writing Method Contract
  -> validate contract
  -> route learning/search/writing/visual/report skills
```

The goal is not to write the final article. The goal is to decide, in a
repeatable and checkable way, what kind of article or sharing artifact is being
made, what mainline it has, which proof modules it needs, which analysis
frameworks each module uses, which expression patterns each module uses, and
what L0-L3 learning/evidence workflow is required.

## Pattern Basis

The design follows two existing repo patterns.

`visual-agent` is the model for intent-based routing:

- one user-facing controller;
- fixed route block;
- mode selection before production;
- source-role mapping;
- low-level tools treated as executors, not parent workflows.

`wiki-medical-agent` is the model for hard control:

- classify intent first;
- resolve state before action;
- validate allowed action;
- return a structured payload;
- only confirmed decision surfaces can execute.

For writing, the equivalent is:

- classify writing intent first;
- build a Writing Method Contract before learning or drafting;
- validate the contract with a checker;
- treat proposed methods as non-executable until the contract is accepted or
  structurally complete;
- route downstream skills as workers, not as competing entry points.

## Approved Architecture

Use one skill with multiple registries, not three competing skills.

```text
.codex/skills/writing-method-composer/
  SKILL.md
  references/
    writing-methodology-registry.md
    analysis-framework-registry.md
    expression-pattern-registry.md
    collaboration-mode-registry.md
    contract-schema.md
    capability-ownership.md
    pressure-scenarios.md
  evaluation.md
```

Potential implementation scripts:

```text
scripts/check_writing_method_contract.py
scripts/eval_writing_method_boundaries.py
tests/test_writing_method_contract.py
tests/test_writing_method_boundaries.py
```

`SKILL.md` stays compact. It owns trigger conditions, hard stops, route block,
and loading pointers. Heavy writing methods, framework definitions, examples,
and pressure cases live in references.

## Runtime Route Block

Every normal run should expose a compact route block:

```text
- Using writing-method-composer
- Intent
- Target Artifact
- Reader Decision
- Mainline
- Proof Modules
- Analysis Frameworks
- Expression Frameworks
- Evidence Needs
- L0-L3 Learning Route
- Allowed Action
- Blocked Action
- Next Action
```

If the user only gives a link or topic and the target artifact is unclear, the
allowed action is clarification or a thin pre-contract. It must not jump
straight to summary, durable learning capture, public report writing, H5
production, or skill edits.

## Writing Method Contract

The contract is the hard intermediate artifact. A normal article-class task
must produce it before downstream research or drafting.

Minimum shape:

```yaml
target_artifact:
  kind: longform_article | deep_report | h5_share | ppt_script | speech | method_article | case_analysis | other
  audience: ""
  delivery_surface: chat | markdown | wiki | h5 | ppt | feishu | public_repo
reader_decision:
  reader_needs_to_understand_or_decide: ""
  non_goals: []
mainline:
  question: ""
  thesis: ""
  reader_takeaway: ""
  primary_frameworks: []
proof_modules:
  - module_id: ""
    article_position: opening | body | turning_point | evidence_panel | conclusion | appendix
    proof_task: ""
    analysis_frameworks: []
    expression_frameworks: []
    required_evidence: []
    l_level: L0 | L1 | L2 | L3
    proof_boundary: ""
source_roles:
  content_sources: []
  evidence_sources: []
  style_references: []
  excluded_sources: []
collaboration_mode:
  id: ""
  stages: []
quality_gates:
  required_checkers: []
  downstream_gates: []
```

Core rule:

```text
mainline -> proof modules -> analysis frameworks -> expression frameworks -> evidence needs -> L0-L3 learning route
```

Do not start from a pile of frameworks. The article has one mainline. Complex
work may use one or two primary frameworks, but only with clear hierarchy.
Proof modules can use multiple analysis and expression frameworks, but each
framework must have a named proof task.

## Registries

Registries are the extension mechanism. New frameworks are added to registries,
not as new skills by default.

### Writing Methodology Registry

Owns article and output methodology, such as:

- topic explanation;
- trend report;
- company evolution case;
- capability gap analysis;
- method-sharing article;
- investigative longform;
- product/experience analysis;
- speech or sharing script;
- H5/share structure;
- PPT narrative structure.

Each entry should define:

```yaml
id: ""
use_when: ""
mainline_shape: ""
typical_proof_modules: []
required_reader_decision: ""
failure_modes: []
```

### Analysis Framework Registry

Owns thinking and proof frameworks. These are not article types.

Examples:

- JTBD;
- customer journey;
- business model canvas;
- lean canvas;
- Five Forces;
- SWOT;
- PESTLE;
- competitive battlecard;
- market sizing;
- pricing / monetization;
- AB validation;
- cohort analysis;
- case study;
- process tracing;
- triangulation;
- source layering;
- people background mapping;
- artifact analysis.

Each entry should define:

```yaml
id: jtbd
type: analysis_framework
use_when: ""
proves: ""
required_evidence: []
article_use: proof_module
delegates_to_skill: job-stories
failure_modes: []
```

The registry may delegate to existing PM/business skills, but it must not copy
their full method bodies. Existing skills remain specialized workers.

### Expression Pattern Registry

Owns how a proof module is made understandable.

Examples:

- concrete event opening;
- role or reader situation entry;
- timeline;
- contrast table;
- layered reveal;
- reverse argument;
- not-A-but-B framing;
- visual explainer;
- callback;
- conclusion elevation.

Each entry should define:

```yaml
id: concrete_event_opening
type: expression_pattern
use_when: ""
helps_reader: ""
best_for: []
failure_modes: []
```

### Collaboration Mode Registry

Owns staged cooperation patterns, not writing theory.

Examples:

- clarify -> contract -> research -> outline review -> draft -> gate;
- link intake -> ask target -> L0/L1 scan -> contract;
- complex report -> contract -> P0/P1 source plan -> evidence matrix ->
  outline -> public gate;
- share/H5 -> contract -> proof modules -> visual role map -> public report
  gate -> visual-agent.

Each entry should define:

```yaml
id: research_outline_review_draft
type: collaboration_mode
use_when: ""
stages: []
blocked_if: []
```

## L0-L3 Integration

L0-L3 remain the learning depth interface from the 2026-06-24 learning workflow
matrix. `writing-method-composer` does not replace `learning-capture`; it
decides which learning route is needed for each proof module.

Examples:

- A short opinion paragraph may need L0/L1 only.
- A reusable article based on several materials usually needs L1/L2.
- A business analysis article with claims about market size, competitive
  position, or company capability needs L2.
- A Stripe-style company evolution, industry shift, or future judgment report
  needs L3 for the load-bearing modules.

The contract should map each proof module to L0-L3 and required evidence. This
prevents learning from becoming unbounded source collection.

## Capability Ownership

`writing-method-composer` owns:

- writing intent classification for article-class work;
- target artifact and reader-decision clarification;
- Writing Method Contract composition;
- registry selection for writing methodology, analysis frameworks, expression
  patterns, and collaboration mode;
- structural validation requirements for the contract;
- route decisions to downstream skills.

It does not own:

- final prose style execution for `khazix-writer`;
- learning capture, source scoring, source queues, or L0-L3 method definitions
  for `learning-capture`;
- reader-facing publish/review gates for `public-report-quality-gate`;
- visual medium selection or image/H5 production for `visual-agent` and child
  visual workers;
- PM/business framework bodies owned by existing PM skills;
- OpenSpec lifecycle state;
- skill implementation itself during brainstorming.

Description pollution is a failure. The new skill description must not say
that it is used for all H5s, reports, PPTs, public materials, learning, visuals,
or PM analysis. It is used when the task needs article-class methodology
composition before learning, drafting, or presentation.

## First Implementation Scope

First round should optimize article-class workflow only.

Expected touched files later, after OpenSpec approval:

- add `.codex/skills/writing-method-composer/*`;
- minimally update `.codex/skills/learning-capture/SKILL.md` so
  article/share/report output targets consume or require a Writing Method
  Contract before L2/L3 learning execution;
- minimally update
  `.codex/skills/learning-capture/references/article.md` to distinguish
  article-as-input-source from article-as-output-target;
- minimally update
  `.codex/skills/learning-capture/references/output-contract.md` to allow a
  `writing_method_contract_ref`;
- minimally update `.codex/skills/public-report-quality-gate/SKILL.md` so
  complex reader-facing article/H5/report work may require a Writing Method
  Contract while the public report gate remains the outer output gate;
- add checker, tests, and evaluation evidence.

Do not touch in the first round:

- `visual-agent`;
- `knowledge-article-visual`;
- `visual-knowledge-onepager`;
- `interview-deep-reading-board`;
- `material-collaboration-defaults`;
- `product-discovery-wiki-capture`;
- `khazix-writer`;
- PM/business skill descriptions;
- global `/home/yan/.codex/skills/khazix-writer`;
- OpenSpec artifacts from this brainstorming document alone.

Weak existing skills are not all repaired in this first round. They should be
listed as follow-up capability debt only when the new controller exposes a real
boundary conflict or missing worker behavior.

## Checker And Evaluation

Reference text alone is too weak. Enforcement requires four layers:

```text
references = method knowledge
contract = required runtime artifact
checker = machine structural validation
eval = replay evidence that future behavior should not drift
```

Minimum checker failures:

- missing target artifact;
- missing reader decision;
- missing mainline question or thesis;
- no proof modules;
- proof module without proof task;
- framework listed without a proof task;
- expression pattern listed without article position;
- L2/L3 module without evidence needs or proof boundary;
- source roles not separated;
- public/H5/report output without downstream public gate;
- visual output route without visual-agent as downstream controller;
- duplicate owner language in the new skill description.

Minimum replay scenarios:

- Bare link in a writing thread: asks target/intent before summary or learning.
- Company case article: uses case study/process tracing/source layering and L3
  only for load-bearing modules.
- Short article: stays light and does not force heavy research.
- H5/share draft: contract first, then public report gate and visual route.
- PM framework pile: rejects unused JTBD/SWOT/Five Forces/cohort stacking.
- People background module: requires public/official/career evidence and
  separates person-level evidence from organization capability claims.
- AB/cohort claim: requires data or experiment design, otherwise marks proof
  boundary.
- Duplicate capability check: fails if skill descriptions widen or worker
  capabilities are copied into the controller.

## Acceptance Criteria For Future Implementation

- `writing-method-composer` is a compact repo-local skill under `.codex/skills`.
- It has registry references for writing methodology, analysis frameworks,
  expression patterns, and collaboration modes.
- It produces a Writing Method Contract before article-class learning or
  drafting.
- L0-L3 learning depth is assigned per proof module.
- Existing PM/business skills are delegated to, not copied.
- `learning-capture` remains the learning controller.
- `public-report-quality-gate` remains the reader-facing output gate.
- Visual production still routes through `visual-agent`.
- Checker and tests catch missing contract structure and capability pollution.
- Evaluation records RED baseline, GREEN result, pressure scenarios, and
  residual risks.

## Non-Goals

- Do not implement the workflow in this brainstorming step.
- Do not make every writing task heavy.
- Do not create three separate skills for writing methodology, analysis
  frameworks, and expression frameworks.
- Do not move all writing quality rules into `learning-capture`.
- Do not replace `khazix-writer` style rules.
- Do not make registries a dumping ground for vague examples.
- Do not claim future runtime behavior without behavior replay evidence.

## Self-Review Notes

- No implementation is included.
- Scope is a single article-method controller design.
- The design explicitly preserves OpenSpec authority.
- The design separates controller, registries, contract, checker, evaluation,
  and downstream worker ownership.
- The design resolves the approved extension question: add new methods to
  registries first; promote to a separate skill only when it has independent
  trigger, input/output, checker, and no controller conflict.
