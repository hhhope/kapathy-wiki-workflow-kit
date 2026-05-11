---
title: agentic-collaboration / company playbook page explore
canonical_object: agentic-product-engineering-collaboration
artifact_type: explore_trace
status: exploring
source_path: chat://openspec-explore/agentic-company-playbook-page/2026-05-11
updated: 2026-05-11
---

# Agentic Collaboration Company Playbook Page Explore

## Trigger

The user invoked `openspec-explore` and asked whether to add a separate
newspaper-format page based on current data that compares collaboration modes
from OpenAI, Anthropic, and one payment-domain company, then turns the finding
into a Chinese hand-drawn knowledge image using image-model or hybrid mode rather
than H5/SVG.

## Exploration Questions

- Should this be a separate page or part of the existing
  `agentic-product-engineering-collaboration-newspaper.html`?
- Which payment-domain company is the strongest comparable case based on
  available source evidence?
- What should the page say to existing company staff: "what do current company
  people do?" and "what should we do?"
- What visual asset should be generated later, and which mode should be used?

## Boundary

This is exploration only. Do not edit the existing newspaper HTML or generate
visual assets from this trace. If the direction is accepted, implementation
should happen after an explicit proceed signal or an OpenSpec change path.

## Findings

### Page boundary

This should be a separate newspaper-format page, not another section inserted
directly into `agentic-product-engineering-collaboration-newspaper.html`.

Reason: the current newspaper already covers the whole industry thesis:
industry debate, internal collaboration dumbbell, operating system, role
actions, evidence use, and local principles. The requested page is narrower: a
company-sample playbook that answers how current company staff should work and
what "we" should do next.

### Company sample selection

Recommended samples:

- OpenAI: issue/task control-plane collaboration. Use Codex, Harness
  Engineering, and Symphony to show "humans steer, agents execute" and issue
  trackers becoming agent orchestration surfaces.
- Anthropic: cross-functional work-surface collaboration. Use Claude Code team
  examples to show engineering, design, data, legal, and marketing people
  turning described problems into executable work.
- Stripe: payment-domain agentic transaction collaboration. Prefer Stripe over
  PayPal for this page because Stripe has current first-party evidence around
  Agentic Commerce Protocol, Instant Checkout, Shared Payment Token, MCP, fraud,
  checkout, fulfillment, and agent-readable business systems. PayPal remains
  useful as an organization/OPD anecdote, but it is not the strongest current
  payment-agent collaboration case.
- Block: payment/fintech organization restructuring plus engineering
  AI-readiness. Add Block because recent layoffs and Jack Dorsey's public
  language make it the strongest "boss says the company should now be smaller
  and intelligence-native" counterweight. Block should not replace Stripe:
  Stripe explains agentic transaction infrastructure; Block explains the
  organizational bet, employee pressure, repo readiness, AI Champions, automated
  PRs, and the risk of using AI productivity as a workforce-cutting narrative.

### Suggested page thesis

The page should say:

> Agentic collaboration is not one pattern. OpenAI shows how work enters an
> agent queue; Anthropic shows how every function can become a builder when
> problems are described well; Stripe shows what happens when agents cross into
> payment and commerce; Block shows the harder organizational question: once AI
> raises throughput, who remains, what work is still human, and how do you avoid
> turning "AI-native" into a blunt layoff story?

### Recommended page shape

Use the existing newspaper grammar, but make the page narrower:

1. Masthead: `三家公司告诉我们：Agent 协作不是工具接入，而是作业系统重排`.
2. Lead judgment: current company people must move from "doing tasks" to
   "defining executable work, reviewing evidence, and maintaining writeback".
3. Four company columns:
   - OpenAI: issue tracker / task board -> agent workspace -> PR/review -> repo
     knowledge.
   - Anthropic: anyone who can describe a problem can build or inspect a working
     artifact, but review remains human.
   - Stripe: agents can transact only when product, price, checkout, trust,
     payment authorization, fraud, and fulfillment are structured and auditable.
   - Block: smaller/flatter AI-assisted organization, but the page must hold two
     truths together: their engineering system shows real AI-readiness work; the
     layoff story also shows morale, judgment, customer support, and human-loop
     risk.
4. Local playbook:
   - Product/PM writes executable intent.
   - Engineering/TL builds harness, permission, tests, rollback, and review
     packets.
   - Design/research turns experience judgment into examples, states, and
     edge-case checks.
   - QA/data/ops convert recurring failures into evals and source-of-truth
     records.
   - Managers watch throughput, review load, risk, and writeback quality.
5. Closing principle:
   - "我们不是先让 Agent 多做事，而是先让工作能被 Agent 正确接走、被人审回来、被系统写回去。"

### Visual mode

The requested image should be one standalone Chinese hand-drawn knowledge image,
prefer image-model or hybrid mode. Do not use H5/SVG as the first route.

Recommended visual:

- Title: `三种 Agent 协作模式，落到我们怎么做`
- Layout: horizontal 16:9 teaching card or vertical compact one-page
  infographic.
- Structure:
  - Left: OpenAI = control plane / task queue.
  - Middle: Anthropic = cross-functional builder surface.
  - Right: Stripe = agentic transaction infrastructure.
  - Far right or bottom contrast: Block = AI-native org bet + layoff warning.
  - Bottom: Our action loop = intent -> context -> agent run -> review packet ->
    eval/writeback -> human responsibility.
- Mode: hybrid if exact Chinese wording matters; image model if visual quality
  is the main priority and text can be reviewed after generation.

## Source Notes

Current public sources inspected during exploration:

- OpenAI, `How OpenAI uses Codex`
- OpenAI, `Harness engineering: leveraging Codex in an agent-first world`
- OpenAI, `An open-source spec for Codex orchestration: Symphony`
- Anthropic / Claude, `How Anthropic teams use Claude Code`
- Stripe, `Stripe powers Instant Checkout in ChatGPT and releases Agentic
  Commerce Protocol codeveloped with OpenAI`
- Stripe, `What is agentic commerce? A guide to getting started`
- Block Engineering, `AI-Assisted Development at Block`
- The Register / Guardian / AP-syndicated coverage of Block's February-March
  2026 AI-linked layoffs and Jack Dorsey's shareholder-letter language
