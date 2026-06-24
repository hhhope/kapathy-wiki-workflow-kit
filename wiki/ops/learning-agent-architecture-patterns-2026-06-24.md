---
layer: ops
domain: agent-harness
ops_area: learning-capture
canonical_object: learning-agent-architecture-patterns
artifact_type: repo-learning
status: active
created_at: 2026-06-24
updated_at: 2026-06-24
source_type: conversation
source_path: "chat://superpowers-brainstorming/learning-workflow-matrix/2026-06-24"
---

# Learning Agent Architecture Patterns

## Trigger

在讨论学习流程分级时，用户追问大型 skill 是否应该放在一个 skill 内，是否应
参考 `medical-agent` 或 `cr-agent`，以及行业内是否只有
`Controller / Router + workers` 和 `State machine / graph` 两种模式。

## Learning Point

行业主流不是把“大 skill”越写越大，而是采用组合式结构：

```text
short runtime entry
  -> supporting references / templates / scripts
  -> controller or router
  -> worker modules
  -> structured output contract
  -> checker / replay
  -> optional state machine for long-running cases
```

本仓库的学习流程应采用：

```text
Learning Agent Controller
  + modular references / workers
  + structured output contract
  + Python checker / replay
  + optional research-case state later
```

## Industry Pattern Map

| Pattern | Use | Local Interpretation |
|---|---|---|
| Skill + supporting files | Reusable procedures, rules, templates, examples, scripts, references | Keep `SKILL.md` short; move large learning levels, methods, source queues, output contracts, and writing methods into references/scripts/templates |
| Controller / Router + workers | Multi-step work where state does not need to be durable by default | Use `learning-capture` as the user-facing controller; route to bounded modules |
| State machine / graph | Long-running, resumable, stateful work with explicit transitions and human review | Optional later for L3 research cases such as Stripe-style source queues |
| Multi-agent team | Planner/reviewer/executor roles or parallel specialist work | Not first-version default; useful only after clear role boundaries exist |
| Schema + guardrails + checker | Stable, replayable, verifiable outputs | Use YAML/JSON blocks and Python checkers for L2/L3 learning records |
| Tool/script-backed skill | Deterministic parsing, validation, extraction, scoring, replay | Scripts verify structure and gaps; LLM keeps judgment and synthesis |

## External References

- Anthropic Claude Code Skills: skills may include `SKILL.md`, scripts,
  templates, examples, and reference docs; complex skills should keep trigger
  context compact and place heavy detail in supporting files.
  <https://docs.anthropic.com/en/docs/claude-code/skills>
- OpenAI Agents SDK: uses agents, handoffs / agents-as-tools, guardrails,
  sessions, tracing, Python-first tools, and Pydantic validation to structure
  complex workflows.
  <https://openai.github.io/openai-agents-python/>
- LangGraph: emphasizes durable execution, stateful agents, persistence,
  memory, and human-in-the-loop for long-running workflows.
  <https://docs.langchain.com/oss/python/langgraph/overview>
- Microsoft AutoGen AgentChat: emphasizes agent teams, group chat, selector
  teams, swarm, and graph workflows for multi-agent collaboration.
  <https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html>

## Local Architecture Decision Candidate

Do not put the full learning workflow into one large `learning-capture/SKILL.md`.

Use `learning-capture` as a controller/router:

- classify whether the task is learning;
- classify learning level: L0, L1, L2, L3;
- classify learning type: technical, business, company case, industry trend,
  output expression, governance / agent workflow;
- decide whether the task needs object reconstruction;
- route to a module or report that the task needs a split.

Move complex rules into modules / references:

- `levels.md`
- `research-methods.md`
- `evidence-strength.md`
- `source-queue.md`
- `output-contract.md`
- `public-writing-method.md`
- `pressure-scenarios.md`

Use script-backed validation for verifiable structure:

- L2/L3 records should contain structured YAML/JSON blocks.
- Python checkers should verify required fields, evidence IDs, source status,
  proof boundaries, and replay coverage.
- Python should not decide whether the business or technical judgment is
  correct; it only checks whether the reasoning artifact is structurally
  complete.

Keep state machine optional:

- First version should not use LangGraph or a full state machine.
- Add research-case state only when L3 cases repeatedly need resume, source
  queue progress, saturation tracking, human review, and output iteration.

## Proposed Local Shape

```text
learning-capture / controller
  -> learning-intake-levels
  -> learning-type-method-router
  -> learning-evidence
  -> learning-source-queue
  -> learning-output-transform
  -> learning-public-writing
  -> learning-replay-checker
```

## Reuse Boundary

This is candidate learning, not a behavior change.

- Do not edit `AGENTS.md` from this note alone.
- Do not change `learning-capture` without an OpenSpec change.
- Do not claim future runtime behavior until replay evidence exists.
- Use this note as input to the ongoing Superpowers brainstorming design.
