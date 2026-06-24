# Learning Workflow Matrix Design

## Route Status

Route: brainstorm -> superpowers spec; OpenSpec remains read-only until this
brainstorming spec is reviewed and accepted.

## Problem

The repository already has `learning-capture`, but that skill mostly answers:

- whether an external source should be treated as learning;
- what evidence object it is: article, repo/README, or example;
- whether a source reaches a score threshold for durable capture;
- where a learning artifact should be routed.

It does not define a complete learning workflow:

- how to choose learning depth;
- how to distinguish technical, business, company-case, trend, output-shape,
  and governance learning;
- how much evidence is needed for each depth;
- which research methods apply;
- when a large source queue is useful;
- when learning is ready for a reader-facing article, H5, or PPT;
- when to stop, continue, split, or formalize the result.

The Stripe research thread exposed the gap. A 1000-source queue, long company
timeline, product/API evidence, market position, acquisitions, protocol signals,
and a reader-facing H5 cannot be processed as ordinary learning. The workflow
must support research-grade object reconstruction.

## Design Goal

Define a learning matrix that gives the agent a stable way to decide:

1. learning level;
2. learning type;
3. required evidence strength;
4. research methods;
5. output format;
6. public-writing transformation path;
7. validation and replay requirements.

The design should not create a monolithic skill. It should produce a modular
architecture that can later be implemented through OpenSpec.

## Architecture Decision

Use:

```text
Learning Agent Controller
  + modular references / workers
  + structured output contract
  + Python checker / replay
  + optional research-case state later
```

Do not put the entire learning workflow into one large `learning-capture/SKILL.md`.

### Pattern Basis

The design combines these industry patterns:

| Pattern | Use | Local Role |
|---|---|---|
| Skill + supporting files | Reusable rules, examples, scripts, templates, references | Keep `SKILL.md` short; move heavy method detail to references/scripts |
| Controller / Router + workers | Multi-stage work without default durable state | `learning-capture` stays the user-facing controller |
| Schema + guardrails + checker | Stable, replayable, verifiable outputs | Use YAML/JSON blocks and Python checkers for L2/L3 artifacts |
| Tool/script-backed skill | Deterministic parsing, validation, extraction, replay | Scripts check structure, fields, source status, and replay coverage |
| State machine / graph | Long-running, resumable research cases | Optional later for repeated L3 case-state needs |
| Multi-agent team | Planner/reviewer/executor role split | Not first-version default; only when role boundaries are clear |

First version should not use a full state machine or function-calling runtime.
The current environment is Codex + repo markdown + OpenSpec, not a persistent
agent server. State-machine support can be introduced later for long-running
L3 cases.

## Learning Levels

Learning level determines data strength, depth, output shape, and validation.

| Level | Name | Goal | Input Strength | Method Strength | Output | Stop Condition |
|---|---|---|---|---|---|---|
| L0 | 快速判断 | Decide whether a source is worth continuing | 1-3 accessible sources; README/abstract/entry page is enough | source class and relevance judgment | short conclusion, continue/skip, next step | enough to answer whether to continue |
| L1 | 普通学习 | Extract reusable points | 3-8 core sources or one complete material package | grounding, reuse/modify/reject, boundary | what was learned, transferable practices, non-transfer boundary | reusable point and boundary are clear |
| L2 | 深度学习 | Support a technical, product, or business judgment | multiple evidence types; at least two-way cross-validation | input decomposition, cross-validation, evidence sufficiency, selected framework | input inventory, method used, value judgment, output map, transfer boundary | load-bearing claims have evidence strength |
| L3 | 研究级学习 | Reconstruct an object and produce research-grade judgment | preset evidence pool, P0/P1 reading, source queue when needed | case study, process tracing, cross-validation, evidence sufficiency, data saturation, due-diligence source layering | object reconstruction, causal chain, evidence matrix, method layer, value judgment, output transformation plan | new P0/P1 sources no longer change the main judgment, and residual gaps have proof boundaries |

Default behavior:

- If the user does not specify depth, start at L1.
- If the user asks to reuse, adapt, or assess local value, upgrade to at least L2 when the object is non-trivial.
- If the source affects OpenSpec, skills, AGENTS, agent behavior, H5, PPT, Feishu review, or a public report, use at least L2.
- If the task involves company path, industry trend, future judgment, long timeline, multi-source evidence pool, or 1000-source queue, use L3.
- If token or space is insufficient, do not compress L3 into L1. State the split plan.

## Learning Types

Learning type determines the analysis method. The same level can behave
differently depending on type.

| Type | Typical Question | Core Methods | High-Quality Industry References | Local Samples / Replay |
|---|---|---|---|---|
| Technical | How does it work? What is reusable? | architecture decomposition, execution-chain tracing, interface/data-flow analysis, capability mapping | LangGraph docs, OpenTelemetry docs, Kubernetes design docs, PostgreSQL docs, OpenAI/Anthropic engineering docs, high-quality OSS architecture docs | OpenCodeReview learning, cr-agent migration candidates |
| Business | Why does this strategy matter? Where is the value? | value-chain analysis, business model decomposition, unit economics, competitive position, customer segmentation | BVP State of the Cloud, a16z reports, Stripe annual letters, Adyen annual reports, PayPal 10-K, selected consulting reports | Stripe source pack, Stripe report gate review |
| Company Case | How did this company evolve? | Case Study Research, Process Tracing, cross-validation, evidence sufficiency | Stripe annual letters, Amazon shareholder letters, Shopify Editions, NVIDIA/Apple/Microsoft annual reports, HBR/business-school case style | Stripe H5 reanchor, Stripe drift retro |
| Industry Trend | Where is this trend going? | trend layering, time constants, scenario analysis, key-variable analysis, counterexample analysis | Gartner/Forrester market guides, CB Insights, State of AI Report, BVP cloud reports, regulatory/central-bank/international-organization reports | AI payment / agent commerce chapters, future judgment chapter |
| Output Expression | Why does this article/H5/PPT work? | structure mapping, reader-job analysis, narrative skeleton, visual-evidence relation, paragraph rhythm | BVP Atlas, Stripe annual update pages, Apple keynote/product pages, FT visual explainers, NYT visual stories, The Pudding visual essays | Stripe H5 redesign drift, public-report gate reviews |
| Governance / Agent Workflow | Should this behavior be formalized? | failure replay, promotion boundary, prior-art scan, OpenSpec formalization, pressure tests | OpenAI docs/Cookbook, Anthropic Claude Code docs, LangGraph docs, MCP docs, mature OSS contributor guides | learning-capture-routing, visual-agent drift, openspec-router replay |

High-quality industry references are not local wiki artifacts. Local artifacts
are replay samples, pressure tests, or implementation evidence.

## Research Method Layer

These methods become default candidates for L2/L3, and required considerations
for L3.

### Case Study Research / 案例研究

Use when the object is a company, product system, tool, organization, or
workflow worth deep reconstruction. Stripe is a company-path case. OpenCodeReview
is a tool/engineering case.

### Process Tracing / 过程追踪

Use to reconstruct time and causality:

```text
what happened
  -> why it happened
  -> what capability accumulated
  -> how later events reused that capability
```

### Triangulation / 交叉验证

Use different evidence types to validate a key judgment. A load-bearing claim
should ideally have:

```text
primary / official source
  + behavior or product evidence
  + external reference or boundary evidence
```

Cross-validation dimensions:

- source: official, financial, docs, media, peer, analyst;
- type: metric, product release, API doc, acquisition, hiring, customer case;
- time: early path, middle accumulation, current stage;
- actor: self-claim, peer action, partner, protocol, regulator;
- positive/negative: support, boundary, counterexample, missing evidence.

### Evidence Sufficiency / 证据充分性

Every load-bearing claim must be labeled:

- promoted: enough evidence for visible output;
- candidate: plausible but not enough for visible claim;
- route-only: useful source lead only;
- proof-boundary: important but not sufficiently proven;
- rejected: not supported or too risky.

### Data Saturation / 资料饱和

Use when deciding whether research is enough. A module is saturated when new
P0/P1 sources no longer change the main judgment and mostly add detail. If new
sources still change the main line, do not claim saturation.

### Due Diligence Source Layering / 尽调式材料分层

Separate:

- official first-party material;
- audited or financial data;
- product/API docs;
- partner material;
- customer cases;
- media reports;
- analyst writing;
- community interpretation;
- speculative material.

Do not let lower-confidence layers carry stronger claims than they can support.

## Research Reconstruction Method

For L3, the agent should reconstruct the object instead of summarizing sources.

```text
research object
  -> required background data
  -> time span
  -> evidence roles
  -> source queue
  -> P0/P1 reading
  -> reconstruction model
  -> evidence matrix
  -> value judgment
  -> output transformation
```

Stripe example:

- object: Stripe company evolution and AI-era financial infrastructure;
- time span: 2010-2026, with future judgment to 2031;
- evidence roles: company scale, product/API evolution, acquisition gaps,
  technical interfaces, transaction-chain shifts, credit relationship shifts,
  partner/protocol signals, peer/network moves, regulatory/accountability
  boundary;
- source queue: 1000 candidate rows;
- promoted evidence: official annual letters, product docs, API docs, partner
  releases, selected financial/market sources;
- output: H5 / report / future-learning chapters.

The 1000-source queue is not a content brag. It is an evidence-pool mechanism.

## Output Contracts

### L1 Minimum Output

- source kind;
- what was learned;
- reusable point;
- non-transfer / non-promotion boundary.

### L2 Minimum Output

- `Input Inventory`;
- `Method Used`;
- `Output Map`;
- `Value Judgment`;
- `Transfer Boundary`.

### L3 Minimum Output

- `Input Inventory`;
- `Research Reconstruction Model`;
- `Evidence Matrix`;
- `Method Layer`;
- `Value Judgment`;
- `Data Saturation / Proof Boundary`;
- `Output Transformation Plan`.

L2/L3 outputs should include a structured YAML or JSON block so scripts can
validate required fields.

## Public Writing Transformation

Reader-facing outputs are not learning notes with polished prose. They require
an additional transformation layer:

```text
research learning
  -> Article Intent Contract
  -> Reader Path
  -> Thesis
  -> Section Structure
  -> Evidence Placement
  -> Visual Role
  -> Claim Strength Control
  -> Citation Surface
  -> Section Drift Review
```

Public-writing methods:

| Method | Purpose |
|---|---|
| Article Intent Contract | Define reader, reader decision, main line, non-goals, user-owned judgments |
| Reader Path | Define the order in which the reader should understand the argument |
| Thesis First | Start from the main judgment, not from source buckets |
| Evidence Placement | Every chart, metric, quote, and visual serves a named judgment |
| Claim Strength Control | Distinguish assertion, candidate, boundary, and speculation |
| Citation Surface | Reader-visible evidence for load-bearing claims |
| Section Drift Review | Verify section objectives and paragraph claims against the intent contract |

For newspaper-style H5/share/public drafts, internal source maps are not enough.
The reader-facing artifact needs a citation route for load-bearing claims,
figures, company examples, and visual panels.

## Runtime Flow

```text
learning request
  -> classify whether this is learning
  -> classify level
  -> classify type
  -> decide whether object reconstruction is needed
  -> select methods
  -> declare input/output plan for L2/L3
  -> execute learning
  -> write learning artifact or output transformation plan
  -> validate structure for L2/L3
```

When entering L2/L3, state:

- learning level;
- learning type;
- required inputs;
- methods to use;
- expected outputs;
- whether the task needs splitting.

When the material exceeds one reliable turn:

```text
This is not a normal summary. I will first create:
1. input decomposition
2. P0/P1 source ordering
3. output plan
Then I will continue with the main analysis.
```

## Stop / Continue Rules

| Situation | Required Behavior |
|---|---|
| Current evidence answers the immediate question but not a stronger claim | Output current conclusion and proof boundary |
| New sources still change the main judgment | Do not claim saturation; continue or split |
| New sources mostly add detail | Mark local saturation for that module |
| Claim affects behavior assets | Do not promote directly; route to OpenSpec / proposal |
| Public output lacks reader-visible citation surface | Do not claim review-ready or publish-ready |

## Module Layout For Future Implementation

Keep `learning-capture` as the controller/router. Add modular references:

- `references/levels.md`
- `references/research-methods.md`
- `references/evidence-strength.md`
- `references/source-queue.md`
- `references/output-contract.md`
- `references/public-writing-method.md`
- `references/pressure-scenarios.md`

Potential later scripts:

- `scripts/check_learning_record.py`
- `scripts/check_source_queue.py`
- `scripts/check_claim_evidence_links.py`
- `scripts/eval_learning_replay.py`

Python scripts should verify structure, required fields, evidence links, source
status, and proof-boundary presence. They should not decide whether the core
business or technical judgment is correct.

## Non-Goals

- Do not implement the workflow in this brainstorming step.
- Do not edit `learning-capture`, `AGENTS.md`, or OpenSpec specs from this
  document alone.
- Do not introduce a full state machine in the first implementation.
- Do not introduce function calling runtime as a dependency for this repository.
- Do not make every learning request heavy; L0/L1 must remain light.
- Do not treat local wiki artifacts as industry benchmark materials.

## Acceptance Criteria For Future Implementation

- `learning-capture` remains compact and routes rather than containing the full
  matrix.
- The level/type matrix is stored in references.
- L2/L3 outputs have a structured output contract.
- A checker can identify missing required L2/L3 fields.
- Stripe-style L3 learning has source queue, evidence role, promoted evidence,
  and proof-boundary concepts.
- OCR-style technical learning routes differently from Stripe-style company
  reconstruction.
- Public-writing transformation is separate from learning capture.
- Replay scenarios cover OCR, Stripe, public article/H5, and governance/agent
  workflow learning.

## Open Questions

- Should L3 research case state remain a Markdown artifact first, or should it
  be represented as JSON/CSV from the start?
- Should `learning-output-transform` become a separate skill later, or remain a
  reference under `learning-capture`?
- How much source-queue tooling is needed before the next Stripe-like research
  case?

## Self-Review Notes

- No implementation is included.
- Scope is a single learning workflow design.
- The architecture separates controller, references, scripts, and optional
  state.
- Public-writing transformation is included because the user explicitly asked
  to consider external drafts and article-writing methodology.
