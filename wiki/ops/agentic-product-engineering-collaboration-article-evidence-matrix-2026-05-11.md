---
artifact_type: article-evidence-matrix
title: agentic-product-engineering-collaboration / article evidence matrix
canonical_object: agentic-product-engineering-collaboration
layer: ops
domain: product-engineering-collaboration
ops_area: source-intake
created: 2026-05-11
status: draft
derived_from:
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md
  - wiki/reports/agentic-product-engineering-collaboration-management-report.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
---

# Article Evidence Matrix

## Main Line

The next article should move from "AI coding tool comparison" to "product and
engineering operating-system migration".

Core claim: AI Agent did not create a middle layer from nothing. It turns part
of the existing PM/TL/QA/Ops/meeting/Jira/document/script/RPA middle work into
a callable, reviewable, replayable, writeback system loop.

## Chapter Matrix

| Chapter | Core Claim | Evidence Can Carry | Boundary | Hard References Needed |
|---|---|---|---|---|
| 行业在争什么 | Debate moved from model/IDE strength to whether Agent can enter real work objects, be governed, be verified, shift responsibility upward, and use clear organization context. | 95-entry public timeline; 60-lead source-hardening extension; OpenAI Symphony; GitHub Copilot coding agent; Atlassian Rovo/Jira; Google Jules; JetBrains Central; Stack Overflow, DORA, GitLab, Thoughtworks, METR, OWASP, Replit incident as risk counterweights. | Say `截至 2026-05-12 的公开来源池显示`, not `全网`. Vendor pages show strategy, not customer proof. 312 unique URLs are source leads, not 312 deeply read independent sources. | Monthly count methodology; concrete Stack Overflow/DORA/GitLab/METR data points; authoritative Replit incident source; transcripts for Sherwin Wu, Boris Cherny, Karpathy, Marc Brooker, Simon Last; select 60-80 load-bearing sources before publication. |
| 公司的位置更像哑铃 | Company collaboration can be observed as a dumbbell: execution automation on one side, organization governance on the other, bridged by spec/eval/review/owner/writeback. | Execution: OpenAI Symphony, GitHub issue-to-PR, Atlassian backlog-to-code, Google Jules, Cursor, Sourcegraph, AWS Q. Governance: Block AGENTS/HOWTOAI/skills/CI/review, GitHub branch protection, JetBrains control/execution plane, Coder self-hosted agents. Organization: Amazon, Shopify, Duolingo, Coinbase, Klarna, Microsoft Frontier Firm, McKinsey. | Dumbbell is a candidate observation frame, not an accepted industry term. Middle layer is not gone; middle work is systematized and responsibility rises. Workforce-policy cases do not equal mature agent operating systems. | Primary memos/posts for Shopify, Duolingo, Coinbase, Fiverr; JetBrains, Coder, Block source passages; Microsoft/McKinsey definitions of human-agent operating model. |
| 作业系统变了 | Product-engineering work shifts from people passing context to work objects carrying context: ticket/spec/PR/eval/wiki/CI/logs/review packet become readable, executable, verifiable, writeback objects. | OpenAI Harness Engineering; OpenAI Symphony; GitHub Copilot coding agent; Stripe eval; Block; Anthropic best practices; AgentKit. | Do not claim Agent has taken over full SDLC. Tools alone do not migrate an operating system. Agent-readable docs are necessary, not sufficient. | Paragraph-level references from OpenAI Harness/Symphony, GitHub Copilot coding agent, Stripe eval, Block AGENTS/HOWTOAI/skills, Anthropic workflow/eval/permission materials. |
| Agent 循环 | Agent value is not adding a new middle layer. It organizes scattered middle execution work into a reviewable loop: target -> executable context -> agent queue -> review packet -> replay trail -> system writeback. | OpenAI Codex agent loop; Symphony task/workspace/review packet; Warp Open Agentic Development; Block skills/Actionable CI/testing pyramid; Anthropic Managed Agents. | Do not describe the loop as full automation. Human review, permissions, failure gates, and rollback remain. Review packet is a concept surface, not a standard product object everywhere. | OpenAI Codex agent loop source; Warp virtuous loop source; Anthropic Managed Agents long-horizon/sandbox/credential isolation; Block Actionable CI/testing pyramid/skills details. |
| 人怎么变 | People are not simply replaced; responsibility moves to goals, judgment, taste, acceptance, risk, system design, and end-to-end ownership. | Keith Rabois/barrels; Karpathy vibe coding vs agentic engineering; Addy Osmani on managing coding agents; Cat Wu/Anthropic product team; Notion design Claude Code; Figma/Codex; Stack Overflow, Practical AI, Thoughtworks caution. | OPD/barrel is a candidate lens, not a local talent model yet. Do not say PM/design/engineering collapse into one role; say boundaries thin and responsibilities redistribute. Podcast summaries require transcripts before hard quoting. | Keith Rabois original interview/transcript; Karpathy transcript; Boris Cherny, Cat Wu, Sherwin Wu, Brian Scanlan, Simon Last, Marc Brooker transcripts or notes; local role examples. |

## Recommended Article Order

1. Open with `行业在争什么`, using the time-series and dispute axes.
2. Move to `公司的位置更像哑铃`, framing execution and governance as two ends.
3. Explain `作业系统变了`, naming the work objects.
4. Draw `Agent 循环`, making the middle execution layer reviewable.
5. Close with `人怎么变`, then only a bounded pilot decision.

## Evidence Rules

- Primary company posts can support practice claims.
- Research/survey sources can support adoption, risk, trust, and instability
  patterns.
- Operator interviews can support role language after transcript capture.
- WeChat, media summaries, podcast pages, and indexes are route signals unless
  their upstream source is captured.
- Do not use `全网`, `行业定论`, `必然`, or `已经完成转型`.
