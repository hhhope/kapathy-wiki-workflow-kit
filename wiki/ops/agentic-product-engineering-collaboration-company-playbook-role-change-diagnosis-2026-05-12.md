---
title: agentic-product-engineering-collaboration company playbook role-change diagnosis
canonical_object: agentic-product-engineering-collaboration
artifact_type: office_hours_design
layer: ops
domain: product-engineering-collaboration
ops_area: workflow-trace
status: draft
created: 2026-05-12
target: wiki/reports/agentic-product-engineering-collaboration-company-playbook.html
source_paths:
  - wiki/reports/agentic-product-engineering-collaboration-company-playbook.html
  - wiki/ops/agentic-product-engineering-collaboration-company-playbook-report-gate-review.md
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md
---

# Company Playbook Role-Change Diagnosis

## Problem Statement

The current company playbook answers "what collaboration model does each company
represent", but it does not yet answer the reader's next question: "what changes
for the actual people in product, engineering, design, QA, project management,
and leadership?"

The missing layer is not a generic role checklist. It is a company-by-company
role-change reading extracted from the evidence already collected.

The sharp question is:

> When execution gets delegated to agents, which human responsibility moves
> upstream, and what new artifact does each role have to produce or review?

## Demand Evidence

User correction:

- The company playbook does not make role changes clear enough.
- Example confusion: "产品在干啥，都可以写代码了吗？"
- The fix must come from the pulled data, not a generic AI-role opinion.

Local evidence:

- The H5 currently has company strategy and evidence sections, but each company
  section ends at "我们学到" rather than "role implications".
- The source map already names role-change axes: human role, organization
  design, governance, cross-functional adoption, evidence/eval, and readiness.
- The article evidence matrix already says the "人怎么变" chapter should explain
  that responsibility moves to goals, judgment, taste, acceptance, risk, system
  design, and end-to-end ownership.
- The podcast/video layer records where role language becomes explicit: PM
  collapse, coder-to-manager, designer-to-prototyper, field engineer as
  codebase navigator, manager as agent orchestrator.

## Status Quo

The current page has four strong company frames:

- OpenAI: agent-first engineering operating system.
- Anthropic: human-AI collaborative workspace.
- Stripe: agent-readable commerce protocol.
- Block: AI-native organization system plus workforce-risk warning.

But the page compresses people-model evidence into company labels:

- OpenAI tells us the repo, issue tracker, CI, review, and observability become
  agent work surfaces, but not enough about what PM, engineer, EM, QA, or
  platform owner now do differently.
- Anthropic names product, security, marketing, design, and legal use cases, but
  does not explain whether this means non-engineers "write code" or whether they
  now produce runnable artifacts with human judgment.
- Stripe names EM and designer job signals, but the role implication is buried:
  product/design/engineering are designing a three-party protocol across
  merchants, consumers, agents, and payment rails.
- Block names adoption metrics, champions, rules, skills, CI, and layoffs, but
  does not separate healthy role upgrade from management headcount narrative.

## Target Reader And Narrowest Wedge

Target reader:

- Product, engineering, QA, project management, design, and management readers
  asking what this means for their own job.

Narrowest wedge:

- Add one new evidence-led section to the company playbook:
  "职位到底怎么变".

This section should not say "everyone writes code". It should say:

- Product becomes the owner of intent, acceptance, taste, and runnable
  exploration artifacts.
- Engineering becomes the designer of harness, architecture, constraints,
  review, and failure writeback, not only the typist of implementation.
- Design becomes closer to prototype-and-test loops, not only static handoff.
- QA/test becomes the owner of evidence matrices, evals, replay, and risk-based
  acceptance, not only end-stage bug finding.
- Project/ops becomes the owner of queue health, dependency clarity, review
  packets, and writeback, not only meeting minutes and status chasing.
- Management becomes responsible for incentives, trust boundaries, metrics, and
  headcount narrative, not just AI adoption rate.

## Role-Change Reading By Company

### OpenAI

Evidence in current materials:

- Harness Engineering: humans steer, agents execute; repo knowledge, tests,
  guardrails, and feedback loops become the production system.
- Symphony: issue tracker becomes control plane; tasks get agent workspaces;
  humans review outcomes.
- Codex Core Agents JD: sandbox, orchestration, stateful workflows, memory,
  production fleet, CI/CD, safety, and developer platform.

Role implication:

- Product does not become "a coder" by default. Product must write sharper work
  objects: intent, acceptance criteria, non-goals, constraints, and review
  questions that an agent can execute against.
- Engineering moves from code author to execution-system designer: repo
  structure, testability, observability, state, safety policy, and review loops.
- Engineering manager / tech lead becomes closer to an agent-fleet manager:
  task splitting, queue control, failed-run recovery, CI/rebase/conflict
  handling, and quality gates.
- QA moves upstream into eval and verification design. "Build passed" is not
  enough; the question is whether the agent could prove the outcome.
- Project management moves from status collector to control-plane operator:
  issues, handoff states, review packets, blocked tasks, retry loops, and
  ownership boundaries.

What not to say:

- Do not say OpenAI proves everyone can code.
- Say OpenAI proves engineering systems must become agent-readable and
  reviewable before parallel agent work is useful.

### Anthropic

Evidence in current materials:

- How teams use Claude Code: data infra, product, security, marketing, design,
  and legal all have internal workflow examples.
- Claude Code best practices: explore first, plan, verify, context management,
  permissions, MCP, and subagents.
- Claude Code PM JD: PM plus engineering experience, working with research,
  engineering, and cross-functional teams to translate model progress into
  product capability.
- Public timeline and podcast layer: PM work moves into markdown workflows,
  context libraries, research automation, and lightweight personal operating
  systems; design moves toward coded prototype playgrounds.

Role implication:

- Product can produce more executable artifacts than before: prototype scripts,
  research synthesis, spec drafts, edge-case lists, experiment plans, and
  validation harnesses. That is not the same as owning production code.
- The core PM skill shifts from "write requirements" to "frame the problem,
  explore alternatives, preserve context, judge output, and decide what should
  ship".
- Design shifts from static mockup handoff to rapid prototype/test loops, where
  AI helps build the thing to inspect.
- Legal, marketing, and security do not become engineers. They use agentic
  tools to turn their domain workflow into runnable artifacts, then retain
  professional judgment.
- Engineering still matters because permissions, context, verification, and
  production boundaries decide whether cross-functional artifacts are safe.

What not to say:

- Do not say "产品都可以写代码了".
- Say "产品能把一部分想法变成可运行、可验证、可讨论的 artifact, 但生产责任和专业判断没有消失".

### Stripe

Evidence in current materials:

- Instant Checkout, ACP, and Shared Payment Token move transactions from human
  web UI into agent, user, merchant, and payment-network responsibility chains.
- Agentic Commerce EM JD names new API primitives, dashboard surfaces, money
  movement, and Stripe primitives integration.
- Agentic Commerce Designer JD names merchants, agents, and consumers as three
  surfaces.
- Stripe eval evidence says payment workflows require production-realistic
  integration tests. Mostly correct is failure.

Role implication:

- Product's job is protocol framing: who is the actor, what is authorized, what
  can be refused, what can be rolled back, and what must be auditable.
- Engineering's job is API primitives, identity/payment context, risk controls,
  integration surfaces, and production-realistic evals.
- Design's job is no longer only the merchant dashboard or checkout UI. It must
  design consumer, merchant, and agent surfaces together, including visibility,
  confirmation, refusal, and recovery states.
- QA/risk/compliance become central because agentic commerce crosses money,
  identity, merchant promises, tax, fulfillment, and returns.
- Project management must coordinate cross-party dependencies rather than only
  internal feature delivery.

What not to say:

- Do not say Stripe is a coding-productivity story.
- Say Stripe proves high-stakes workflows need protocol, authorization,
  auditability, and rollback before agent experience.

### Block

Evidence in current materials:

- Block Engineering: 95% of engineers regularly use AI; 50 Engineering AI
  Champions spend 30% of time on enablement; AI-authored code +69%, reported
  time savings +37%, automated PRs +21x.
- Block repo readiness: AGENTS.md, HOWTOAI.md, agent skills, AI rules, usage
  tracking, CI/CD analysis, incident/postmortem support.
- Block careers: current 0 open jobs as a hiring boundary, not causal proof.
- Guardian reporting: layoffs and worker reaction create a workforce-trust risk.

Role implication:

- Engineering shifts through enablement systems: champions, playbooks, skills,
  shared recipes, CI feedback, and service-level context. This is organizational
  infrastructure, not personal prompt hacking.
- Tech leads and managers own adoption quality, not just adoption rate. Usage
  metrics can become theater if they are not tied to verification, incidents,
  review quality, and writeback.
- QA and incident roles gain leverage when postmortems, CI failures, and review
  signals become agent-readable.
- Leadership must separate "AI-readiness" from "smaller team" messaging. If the
  organization ties every AI improvement to layoffs, trust drops and teams hide
  real risks.

What not to say:

- Do not say Block proves AI should reduce people.
- Say Block proves company-wide AI enablement needs explicit guardrails,
  champions, skills, metrics, and a trust boundary around workforce policy.

## Premises

1. The reader's confusion is real: the current H5 answers company strategy but
   not role-level consequences.
2. "Can product write code?" is the wrong first question. The better question is
   "what artifact can product now create, inspect, and be accountable for?"
3. The role-change section should be sourced from the existing data, not invented
   as a generic product/engineering playbook.
4. The safest wording is responsibility redistribution, not role collapse:
   boundaries thin, but accountability does not vanish.

## Approaches Considered

### Approach A: Minimal Patch

Summary: Add a short "职位到底怎么变" section after the four company analysis.

Effort: S

Risk: Low

Pros:

- Fastest to make the H5 answer the user's current complaint.
- Keeps the existing company structure intact.
- Low risk of new visual or layout drift.

Cons:

- The four company sections still carry most of the evidence, so role insight
  may feel appended.
- The reader has to connect company evidence to roles after reading the section.

Reuses:

- Current H5 sections.
- Source map role axes.
- Article evidence matrix "人怎么变".

### Approach B: Company Sections With Role Implications

Summary: Add a role implication block inside each company section, immediately
after evidence labels.

Effort: M

Risk: Medium

Pros:

- Best evidence fit. Each role claim sits next to the company evidence that
  supports it.
- Avoids a generic role checklist.
- Makes OpenAI, Anthropic, Stripe, and Block visibly different.

Cons:

- Longer H5 section. Needs tight writing.
- Requires careful source-boundary wording so secondary podcast/role language is
  not overstated.

Reuses:

- Current company article prose.
- Existing evidence labels.
- Source map and timeline role-language entries.

### Approach C: Role-First Rewrite

Summary: Reframe the page around roles first, then use four companies as
evidence examples under each role.

Effort: L

Risk: High

Pros:

- Directly answers "产品在干啥".
- Stronger if the final audience is internal team role training.

Cons:

- It would abandon the current company-playbook premise.
- It risks becoming the generic role-action playbook that the earlier gate
  explicitly rejected.

Reuses:

- The broader evidence matrix, but less of the current H5 structure.

## Recommendation

Choose Approach B.

Reason: the user asked to see role changes through the company evidence, not to
receive a detached role checklist. The clean fix is to add a sourced
"role implications" block inside each company section, then close with one
cross-company role map.

## Success Criteria

- A product reader can answer: "Am I expected to write production code?" The
  answer should be "no by default; you are expected to create clearer executable
  context, prototypes, validation artifacts, and acceptance criteria."
- An engineering reader can answer: "What changes if agents write more code?"
  The answer should be "you own harness, architecture, tests, review,
  observability, and failure writeback more intensely."
- A QA reader can answer: "Where do I enter earlier?" The answer should be
  "evidence matrix, evals, replay, risk-based acceptance, and incident learning."
- A management reader can answer: "What should we measure?" The answer should be
  "verification quality, rework reduction, incident reduction, writeback, and
  owner clarity, not raw AI usage."
- Every role claim should map to a company source, source-map note, timeline
  entry, or evidence-matrix row.

## The Assignment

Before editing the H5, confirm the stance:

> We will not write "AI makes every role a coder." We will write "AI moves each
> role closer to executable artifacts, reviewable evidence, and sharper
> accountability."

If that stance is accepted, update the H5 using Approach B and refresh the share
package.
