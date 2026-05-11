---
artifact_type: source-map
title: agentic-product-engineering-collaboration / source-map
canonical_object: agentic-product-engineering-collaboration
source_type: external-article-collection
created: 2026-05-11
---

# Agentic Product Engineering Collaboration / Source Map

## Research Goal

Build a management-facing view of how AI agents are changing product and
engineering collaboration across the software delivery lifecycle.

Primary decision target: support a 30-60 day pilot for agent-assisted product
engineering workflows.

## Source Set

| Class | Company / Source | Article | Why It Matters |
|---|---|---|---|
| AI lab | OpenAI | [An open-source spec for Codex orchestration: Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/) | Turns issue tracker / Linear into the control plane for coding agents. Shows the shift from managing sessions to managing deliverables. |
| AI lab | OpenAI | [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) | Defines the deeper operating model: humans steer, agents execute; repository knowledge, tests, and guardrails become the actual production system. |
| AI lab | Anthropic | [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | Shows cross-functional adoption: engineering, product, design, data, legal, and marketing using agentic coding as a work surface. |
| Payment / fintech | Block | [AI-Assisted Development at Block](https://engineering.block.xyz/blog/ai-assisted-development-at-block) | Shows enterprise-scale repo readiness: AGENTS.md, HOWTOAI.md, reusable skills, AI code review, CI integration, and shared recipes. |
| Cloud | AWS | [Amazon Q Developer](https://aws.amazon.com/q/developer/) | Positions agentic capabilities across implementation, documentation, testing, reviewing, refactoring, modernization, cloud operations, and data/AI work. |
| Cloud | AWS | [Frontier agents](https://aws.amazon.com/ai/frontier-agents/) | Frames persistent agents as team extensions for software development, security, operations, and Kiro autonomous development. |
| Traditional software / dev platform | GitHub | [GitHub Copilot: Meet the new coding agent](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/) | Embeds the coding agent directly into GitHub issues, branches, PRs, Actions, logs, and repository policies. |
| Traditional software / work management | Atlassian | [Rovo Dev in Jira](https://www.atlassian.com/blog/company-news/rovo-dev-in-jira) | Connects backlog, plan, code, and PR through Jira/Rovo. Useful for the product-management control-plane pattern. |
| Traditional software / IDE platform | JetBrains | [JetBrains Central](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/) | Explicitly names agentic software development as a distributed system of agents, environments, workflows, governance, cost, and intent alignment. |

## Initial Source Classification

| Source | Source Class | Reusable Capability Type | Local Use |
|---|---|---|---|
| OpenAI Symphony | Primary source | structure, boundary, evidence | Ticket/issue as agent control plane; agent orchestration loop. |
| OpenAI Harness Engineering | Primary source | structure, evidence, boundary | Repo as harness; human time as scarce resource; judgment vs execution split. |
| Anthropic Claude Code teams | Primary source / case study | content, structure, boundary | Cross-functional adoption and non-engineer build path. |
| Block AI-assisted development | Primary source / engineering case | structure, governance, evidence | Repo readiness, champions, skills, measurement, shared recipes. |
| AWS Q / Frontier agents | Primary source / product framing | content, boundary | Cloud vendor view of full SDLC, operations, security, and persistent agents. |
| GitHub Copilot coding agent | Primary source / product workflow | structure, governance | Issue-to-PR workflow, branch protection, PR review, GitHub Actions runtime. |
| Atlassian Rovo/Jira | Primary source / product workflow | structure, content | Backlog-to-code, Jira as planning and agent orchestration surface. |
| JetBrains Central | Primary source / platform strategy | structure, governance, boundary | Control/execution plane, observability, cost attribution, semantic context. |

## Emerging Patterns

1. The unit of work is moving from prompt/session to issue, ticket, PR, spec, or
   workflow object.
2. Agent work needs a control plane: Jira, Linear, GitHub Issues, repository
   plans, or an IDE/platform orchestration layer.
3. Product, design, and other non-engineering roles can initiate more work, but
   this increases the need for acceptance criteria, review packets, and
   judgment boundaries.
4. Engineering leadership shifts from "who writes code" to "who designs the
   harness, guardrails, repo knowledge, tests, and review system."
5. The mature companies converge on governance: permissions, auditability,
   cost attribution, branch protections, CI gates, sandboxing, and observability.

## Skip / Caution

- Vendor metrics are useful signals, not neutral benchmarks.
- Product marketing pages are treated as evidence of vendor strategy, not proof
  that every customer achieves the claimed workflow.
- The final report should avoid claiming that agent-first workflows generalize
  without similar investment in tests, repo knowledge, guardrails, and review.
