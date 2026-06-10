---
layer: ops
domain: agentic-collaboration
ops_area: report-quality
canonical_object: anthropic-claude-code-khazix-article
artifact_type: report-gate-review
title: "anthropic-claude-code-khazix-article / report gate review"
status: draft
created: 2026-06-10
---

# Anthropic Claude Code Khazix Article / Report Gate Review

## Review Target

| Field | Value |
|---|---|
| Target title | 我发现 Anthropic 真正厉害的不是 Claude Code |
| Destination | `wiki/reports/anthropic-claude-code-khazix-article-2026-06-10.md` and `.html` |
| Scope | Khazix-style public article based on the existing Anthropic / Claude Code research, with additional fact verification and data support |
| Non-scope | PPT rewrite, Baofu application chapter, Feishu sync, publish-ready claim |

## Article Intent Contract

| Field | Value |
|---|---|
| Reader | Public-account readers interested in AI company/product evolution |
| Reader decision or action | Understand why Claude Code should be read as an action-system experiment, not only a coding tool |
| Main line | Anthropic is using Claude Code and Claude Cowork to move Claude from language capability into controlled action inside real work environments |
| Non-goals | Do not overclaim internal org chart; do not make OpenAI/Seed equal protagonists; do not write Baofu landing advice |
| User-owned judgments | Final publish stance, final title, final voice intensity |
| Agent-allowed work | Rewrite, source verification, data selection, H5 packaging, self-check |

## Fact Verification Matrix

| Claim / Data | Source | Verification Result | Boundary |
|---|---|---|---|
| Anthropic describes itself as an AI safety and research company building reliable, interpretable, steerable AI systems | https://www.anthropic.com/company | Verified from official company page | Company positioning, not independent assessment |
| Claude Code launched as limited research preview on 2025-02-24 with Claude 3.7 Sonnet | https://www.anthropic.com/news/claude-3-7-sonnet | Verified, lines 11-18 and 35-42 | Official announcement |
| Claude Code became generally available on 2025-05-22 with Claude 4 | https://www.anthropic.com/news/claude-4 | Verified, lines 20-24 and 43-48 | Official announcement |
| Claude Code reads codebase, changes files, runs tests, and delivers committed code | https://www.anthropic.com/product/claude-code | Verified, lines 10-13 | Product claim |
| Stripe deployed Claude Code across 1,370 engineers; one team did a 10,000-line migration in four days vs ten engineer-weeks | https://www.anthropic.com/product/claude-code | Verified, lines 54-57 | Vendor customer case |
| Ramp cut incident investigation time by 80% | https://www.anthropic.com/product/claude-code | Verified, lines 57-60 | Vendor customer case |
| Wiz migrated a 50,000-line Python library to Go in roughly 20 active hours vs estimated 2-3 months | https://www.anthropic.com/product/claude-code | Verified, lines 61-64 | Vendor customer case |
| Rakuten reduced new feature delivery time from 24 working days to 5 | https://www.anthropic.com/product/claude-code | Verified, lines 64-67 | Vendor customer case |
| Anthropic internal teams used Claude Code across infrastructure, product, design, security, marketing, legal | https://claude.com/blog/how-anthropic-teams-use-claude-code | Verified, lines 236-289 and 301-314 | Official internal examples |
| Growth Marketing generated up to 100 ad variations and reduced hours of copy-pasting to half a second per batch | https://claude.com/blog/how-anthropic-teams-use-claude-code | Verified, lines 304-309 | Official internal example |
| Claude Cowork was built because non-technical teams bypassed chat for Claude Code to handle complex multi-step work | https://www.anthropic.com/product/claude-cowork | Verified, lines 22-29 and 59-61 | Product positioning |
| RSP v3 includes risk reports every 3-6 months and external review under certain circumstances | https://www.anthropic.com/news/responsible-scaling-policy-v3 | Verified, lines 76-81 | Safety governance source |
| OpenAI Harness Engineering argues repo knowledge should be a map/system of record, not a 1,000-page manual | https://openai.com/index/harness-engineering/ | Verified, lines 80-91 and 223-225 | Peer comparison only |
| Seed official page lists LLM, Infrastructures, Vision, Speech, Multimodal Interaction & World Model, AI for Science, Robotics, Responsible AI | https://seed.bytedance.com/en/models | Verified, lines 62-64 and 81-97 | Capability map, not org chart |

## Learning Use Map

| Learning artifact | Used output element | Boundary |
|---|---|---|
| `wiki/reports/anthropic-claude-code-hv-analysis-2026-06-10.md` | Main argument and source list | Converted from report voice to public-account prose |
| `wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md` | Organ/person analysis lens | Treated as lens, not proof |
| `wiki/ops/agentic-product-engineering-collaboration-company-playbook-role-change-diagnosis-2026-05-12.md` | Role-boundary caution | Avoided "everyone becomes coder" claim |

## Khazix Four-Layer Self-Check

### L1 Hard Rules

| Check | Result |
|---|---|
| Banned phrases | Pass. No true hits for banned phrases. `最后` appears as an ordinary Chinese word, not the prohibited "首先/其次/最后" structure. |
| Punctuation ban | Pass for article body: full-width colon 0, half-width colon 0, em dash 0, double quotes 0. |
| Structural cliche | Pass. No textbook opening, no bullet-list body. |
| Specific tool/product names | Pass. Uses concrete names: Claude Code, Claude Cowork, OpenAI, Codex, Seed. |

### L2 Style

| Check | Result |
|---|---|
| Opening | Pass. Starts from the live research process, not macro narrative. |
| Rhythm | Pass. Uses short paragraphs and line breaks. |
| Oral expression | Pass. Includes "事情是这样的", "坦率的讲", "说真的", "你想想看", "大时代啊，朋友们" and self-limiting statements. |
| English mixing | Pass with boundary. English is mostly reserved for official product names and necessary terms; explanatory prose is Chinese-first. |

### L3 Content Quality

| Check | Result |
|---|---|
| Data support | Pass. Added dated launches, customer metrics, internal-team examples, and RSP cadence. |
| Knowledge output | Pass. Technical concepts are explained through organization/workflow language. |
| Cultural/structural lift | Pass. Uses Li Xiang's body-organ frame and company-as-work-environment frame. |
| Opposing side | Pass. Explicitly says vendor cases are not independent audit proof. |

### L4 Human Feel

Draft quality: acceptable for user review, not claimed final public publish.

Known residual issue: article still contains product names and some technical terms because exact source alignment requires them. This is intentional, not casual code-switching.

## Hard Gate Results

| Gate | Result |
|---|---|
| Learning use | pass |
| Reference structure | pass |
| Split | pass: article + H5 + gate review |
| Voice | pass for draft |
| Narrative | pass |
| Paragraph drift | pass |
| Judgment ownership | pass: major inferences stated as "I think" / "my judgment" |
| Visual | pass: H5 uses reading layout and fact-check panel, no decorative diagrams |
| Publish | not applicable: no Feishu sync or publish-ready claim |

## Decision

Use as a revised public-account article draft. Do not claim final publish-ready until the user reviews voice, title, and stance strength.

## Residual Risks

- Anthropic customer metrics are vendor-published case claims, not independent audits.
- Claude Cowork product claims are official positioning and need real-user validation before stronger adoption claims.
- Khazix voice is approximated from the skill; final publish voice still benefits from user edit.
