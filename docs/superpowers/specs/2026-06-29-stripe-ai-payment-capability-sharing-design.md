# Stripe AI Payment Capability Sharing Design

## Route

Route: `$superpowers:brainstorming` -> `writing-method-composer` -> public report
gate -> visual route.

This is a design spec for a future H5/share draft. It is not an H5
implementation, Feishu draft, or review-ready public artifact.

Confirmed user decisions:

- Target audience: about 80 people.
- Target direction: use Stripe to explain how we should understand payment and
  financial capability building in the AI era.
- Rejected direction: a Stripe company biography or a generic "Stripe is strong"
  case study.
- Core repair: LinkedIn and JD must stay as evidence. LinkedIn maps current
  people capability. JD maps capability-building intent.

## Writing Method Contract

```yaml
target_artifact:
  kind: h5_share
  audience: "80-person internal sharing audience"
  delivery_surface: h5
reader_decision:
  reader_needs_to_understand_or_decide: >
    AI-era payment competition is not mainly about adding an AI checkout
    feature. It is about building financial transaction capabilities that can
    make authorization, risk, settlement, responsibility, and audit executable
    by software.
  non_goals:
    - "Do not make Stripe a hero biography."
    - "Do not claim Stripe will certainly win AI payments."
    - "Do not turn source quantity into the story."
mainline:
  question: "How should we understand payment and financial capability building in the AI era through Stripe?"
  thesis: >
    AI payment is not about letting an Agent click a payment button. It is about
    turning financial rules, authorization, risk controls, settlement, and
    responsibility boundaries into a transaction control plane that software can
    call, limit, audit, and settle. Stripe matters because its long company path
    accumulated many of those capabilities before the AI wave made them more
    visible.
  reader_takeaway: >
    AI lowers feature implementation cost, but raises the cost of financial
    design: rules, responsibility, risk, audit, and cross-party settlement.
  primary_frameworks:
    - company_evolution_case
    - trend_report
    - capability_gap_analysis
proof_modules:
  - module_id: "sample_selection"
    article_position: "body"
    proof_task: "Explain why Stripe is a valid sample for observing AI-era payment infrastructure."
    analysis_frameworks:
      - source_layering
      - process_tracing
    expression_frameworks:
      - layered_reveal
      - contrast_table
    required_evidence:
      - Stripe product/docs/newsroom
      - public company scale claims
      - AI payment and agent commerce product signals
    l_level: "L2"
    proof_boundary: "Proves Stripe is a useful observation sample, not a guaranteed winner."
  - module_id: "ai_payment_capability_framework"
    article_position: "turning_point"
    proof_task: "Define the five capability layers needed for AI-era payment."
    analysis_frameworks:
      - capability_gap_analysis
      - source_layering
    expression_frameworks:
      - layered_reveal
      - contrast_table
    required_evidence:
      - transaction intent examples
      - authorization and identity examples
      - risk and settlement examples
      - responsibility and audit examples
    l_level: "L3"
    proof_boundary: "Framework for analysis, not an audited market taxonomy."
  - module_id: "stripe_capability_accumulation"
    article_position: "body"
    proof_task: "Show that Stripe's AI-era positioning extends from accumulated payment infrastructure capabilities."
    analysis_frameworks:
      - process_tracing
      - source_layering
    expression_frameworks:
      - timeline
      - layered_reveal
    required_evidence:
      - dated product launches
      - company scale milestones
      - acquisitions or capability gap closures
      - AI/agent/stablecoin payment moves
    l_level: "L3"
    proof_boundary: "Shows capability accumulation; does not prove causal inevitability."
  - module_id: "people_capability_map"
    article_position: "evidence_panel"
    proof_task: "Map what kind of people and expertise Stripe has assembled around this capability stack."
    analysis_frameworks:
      - people_background_mapping
      - source_layering
    expression_frameworks:
      - contrast_table
    required_evidence:
      - LinkedIn current employee backgrounds
      - role clusters
      - prior company and domain experience
    l_level: "L2"
    proof_boundary: "Supports capability profile; does not independently prove strategy success."
  - module_id: "hiring_intent"
    article_position: "evidence_panel"
    proof_task: "Show what capabilities Stripe is still building or reinforcing."
    analysis_frameworks:
      - capability_gap_analysis
      - source_layering
    expression_frameworks:
      - contrast_table
    required_evidence:
      - Stripe JD pages
      - team names
      - role requirements
      - location or seniority patterns
    l_level: "L2"
    proof_boundary: "Indicates capability investment intent; not proof of shipped product outcome."
source_roles:
  content_sources:
    - "Existing repo Stripe H5 specs and H5 report"
  evidence_sources:
    - "Stripe first-party docs, newsroom, annual letters, product pages"
    - "LinkedIn people profiles and role clusters"
    - "Stripe job descriptions"
    - "Secondary media and analyst material with source boundaries"
  style_references:
    - "WeChat RICE/KANO skill article as method-expression reference only"
  excluded_sources:
    - "Unsupported claims that only prove source volume"
collaboration_mode:
  id: "h5_share_contract_visual_route"
  stages:
    - contract
    - public_report_gate
    - visual_route
    - source_learning
    - draft_or_asset_plan
quality_gates:
  required_checkers:
    - "Section objective review"
    - "Evidence role review"
    - "Visual mode review"
  downstream_gates:
    - public-report-quality-gate
    - visual-agent
```

## Recommended Frame

Use the capability reconstruction frame.

Do not make the structure:

> Stripe company history -> Stripe products -> Stripe AI products -> lessons.

Use this structure instead:

> AI changes financial transaction capability requirements -> Stripe is a useful
> sample -> Stripe's history proves the capability stack was accumulated over
> time -> people and hiring evidence show the organizational capability behind
> the stack -> lessons for our own financial capability design.

The headline argument:

> Stripe is the case. AI-era payment capability building is the subject.

## Chapter Map

### 1. AI Payment Is Often Misread

Reader job: break the shallow frame.

Core claim:

> The important question is not whether an Agent can click pay. The important
> question is whether software can initiate transactions inside bounded,
> auditable, risk-controlled financial rules.

Visual shape:

- left: human clicks checkout
- right: software acts inside rules
- middle: authorization, limits, risk, settlement, audit

### 2. Why Stripe Is the Sample

Reader job: understand why Stripe is a valid observation object, not just a
famous company.

Core claim:

> Stripe is worth studying not because it launched AI features, but because it
> has long occupied critical transaction-chain positions: developer access,
> merchant operations, platform split payment, subscription billing, risk,
> identity, settlement, stablecoin, and now Agent-facing transaction entry.

Talk track:

1. Start with the common misunderstanding: AI payment sounds like an Agent
   paying on behalf of a user.
2. Reframe the sample question: which company already touches the rules,
   identity, money movement, and responsibility boundaries behind payment?
3. Place Stripe across the transaction chain, from developer integration to
   merchant operations and AI-era transaction entry.
4. State the evidence boundary: this makes Stripe a high-quality sample, not a
   guaranteed winner.

Visual shape:

```text
developer access
  -> merchant operations
  -> platform split payment
  -> subscription / usage billing
  -> risk / identity
  -> settlement / stablecoin
  -> agent transaction entry
```

Chapter acceptance:

- The chapter must answer "why this sample" before "what Stripe did."
- It must not read like a company introduction.
- It must include a proof boundary.

### 3. The Five-Layer AI Payment Capability Framework

Reader job: get the reusable method.

Core claim:

> AI payment is a shift from direct human operation to software agents executing
> transactions inside rules. That requires five layers of financial capability.

Five layers:

| Layer | Question It Answers | What To Explain |
|---|---|---|
| Transaction intent | What is the buyer trying to accomplish? | Search, compare, order, renew, replenish, procure, or trigger a task. |
| Authorization and identity | Who allowed the action, for whom, and within what boundary? | User, company, platform, sub-account, one-time approval, standing approval, budget. |
| Rules and risk | Under what conditions can the transaction proceed or be blocked? | Limits, fraud, misuse, compliance, refund, dispute, policy exceptions. |
| Money movement and settlement | Where does money come from, where does it go, and how is it reconciled? | Funding source, split payment, merchant settlement, cross-border, stablecoin, reconciliation. |
| Responsibility and audit | Who is accountable when something goes wrong? | User, merchant, platform, Agent provider, payment provider, logs, evidence, recovery path. |

Reusable formula:

```text
AI payment capability = intent + authorization + rules + money movement + responsibility
```

Talk track:

1. Define the difference between "payment action" and "transaction capability."
2. Walk through the five layers in order.
3. For each layer, name the failure mode if it is missing.
4. Only after the framework is clear, bring Stripe back as the company that has
   accumulated pieces of the stack.

Visual shape:

- A five-layer control-plane diagram.
- Each layer has one question, one failure mode, and one Stripe evidence handle.

Chapter acceptance:

- This chapter must be understandable without Stripe product names.
- It must become the audience's reusable framework.
- It must not collapse into a Stripe product catalog.

### 4. How Stripe Accumulated the Five Layers

Reader job: see that the AI-era position is accumulated, not improvised.

Core claim:

> Stripe's AI payment position is not a sudden AI feature. It extends from a
> long accumulation of programmable payment, merchant, risk, billing, settlement,
> and developer-interface capabilities.

Use a capability timeline instead of a flat history.

| Era | What Stripe Solved | Capability Accumulated | AI-Era Reuse |
|---|---|---|---|
| Developer payment access | Make online payment easier to integrate. | API, SDK, docs, dashboard, webhook, test mode. | Agents and developers still need programmable transaction interfaces. |
| Platform and merchant operations | Support platforms, marketplaces, subscriptions, and offline/online operations. | Connect, Billing, Radar, Terminal, merchant operating model. | Agent commerce still needs merchant controls, split payment, billing, and risk rules. |
| Financial operations stack | Expand into tax, identity, issuing, treasury, capital, reconciliation, and global operations. | Wider transaction lifecycle and financial operations layer. | AI transactions need more than checkout: identity, risk, reconciliation, funding, and accountability. |
| AI customer and usage pressure | Serve high-growth AI customers with usage, global revenue, risk, and billing complexity. | Usage/event billing, revenue operations, risk tooling. | AI-native business models pressure pricing, usage, fraud, and cash-flow systems. |
| Agent, wallet, stablecoin, and machine payment | Move toward new transaction entry and settlement surfaces. | Agent commerce, wallet abstraction, stablecoin orchestration, machine-readable payment protocols. | The five-layer framework becomes visible as a transaction control plane. |

Talk track:

1. Do not narrate year by year.
2. Narrate by capability accumulation.
3. For every era, answer: what was the business problem, what reusable ability
   remained, and how AI reuses it.
4. End by returning to Chapter 3: the five-layer framework is not theoretical;
   Stripe's path provides a concrete case.

Visual shape:

```text
time axis: 2010 -> 2026
capability axis:
  developer access
  platform / merchant operations
  billing / revenue operations
  risk / identity / compliance
  money movement / settlement
  agent / wallet / machine payment
```

Chapter acceptance:

- The chapter must prove accumulation, not recite chronology.
- Each Stripe event must carry a proof tag.
- It must explain why AI-era moves depend on prior capabilities.

### 5. People Capability Map

Reader job: see the organizational capability behind the infrastructure.

Core claim:

> This kind of financial infrastructure is not built by one AI feature team. It
> requires a capability mix across platform engineering, financial operations,
> risk, compliance, data, product, enterprise sales, stablecoin, and AI tooling.

LinkedIn evidence role:

- Map current employee backgrounds and role clusters.
- Look for prior companies, domain expertise, seniority, and cross-functional
  mixes.
- Show what kind of people Stripe has assembled around the capability stack.

Boundary:

- LinkedIn supports a people-capability profile.
- It does not independently prove strategic success or product outcome.

### 6. Hiring Intent And Capability Gaps

Reader job: see what Stripe is still building.

Core claim:

> JD evidence shows where capability investment is continuing: what roles are
> being added, which teams are named, and what requirements are emphasized.

JD evidence role:

- Map role titles, teams, requirements, locations, seniority, and repeated
  capability language.
- Compare JD signals to the five-layer framework.
- Use JD as capability-building intent, not as proof of shipped outcome.

LinkedIn + JD relation:

```text
LinkedIn: what kind of people Stripe already has
JD: what kind of capability Stripe is still adding
```

### 7. Future Judgment

Reader job: understand the forward-looking conclusion without overclaim.

Core claim:

> Agent payment will pass through the rules layer before it passes through the
> financial results layer. The winners will not simply make the best AI demo;
> they will make authorization, limits, risk, settlement, and accountability
> machine-readable and operationally reliable.

Evidence boundary:

- Treat future claims as structured judgment, not source fact.
- Attach each future claim to the five-layer framework.

### 8. What We Learn

Reader job: apply the lesson beyond Stripe.

Core claim:

> AI reduces implementation friction, but raises financial design cost. In
> financial systems, the durable work is relationship design: who can do what,
> with whose money, under which rules, with what evidence, and who is
> responsible afterward.

End with a callback to the opening misunderstanding:

> The question was never "can an Agent pay?" The real question is whether the
> financial system can make the Agent's action bounded, auditable, reversible,
> and settleable.

## Visual System

Recommended output mode: H5/HTML, with deterministic diagrams and expandable
evidence panels.

Required visuals:

1. Transaction-chain sample map for Chapter 2.
2. Five-layer AI payment capability framework for Chapter 3.
3. Capability accumulation timeline for Chapter 4.
4. People capability map for Chapter 5.
5. JD capability gap table for Chapter 6.

Visual boundary:

- Do not add decorative images.
- Each visual must carry one proof task.
- Evidence handles can be expandable, but load-bearing claims need visible
  citation routes before review-ready or share-ready status.

## Source And Evidence Plan

| Source Type | Role | Use Boundary |
|---|---|---|
| Stripe first-party docs/product/newsroom | Product and capability evidence | Strong for shipped surface; weak for independent outcome claims. |
| Annual letters/company scale claims | Scale and narrative evidence | Use with date and source boundary. |
| LinkedIn | Current people capability map | Analyze backgrounds and capability clusters, not generic talent flow. |
| JD | Hiring intent and capability-building direction | Shows investment pressure, not shipped results. |
| Secondary media/analysts | Context and interpretation | Must be separated from first-party proof. |
| WeChat RICE/KANO skill article | Expression-method reference | Useful for method operationalization only; not Stripe evidence. |

## Review Checklist

- Does the draft make AI-era payment capability building the subject and Stripe
  the case?
- Does Chapter 2 answer "why Stripe" before describing Stripe?
- Does Chapter 3 stand as a reusable framework without product-name dependency?
- Does Chapter 4 prove capability accumulation rather than recite history?
- Are LinkedIn and JD preserved as separate evidence modules?
- Are proof boundaries visible for sample selection, people evidence, hiring
  evidence, and future judgment?
- Does every visual carry a proof task?

## Next Step

After user review, create the implementation plan or H5 rewrite plan. Do not
edit the H5 directly from this design without the next gate approval.
