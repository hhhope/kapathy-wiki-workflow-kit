---
tags: [lore/pitfall]
pitfall: behavior-assets-without-evidence
---

# Pitfall — behavior-assets-without-evidence

## Scope
Failure pattern where AGENTS, skills, rules, or install guidance change agent behavior without traceable RED/GREEN evidence.

## Summary
- 这是行为资产漂移类 pitfall：文字看起来对，但没有 baseline 和 after-check，agent 行为会悄悄变差。This pitfall covers behavior-asset drift: wording looks coherent, but without baseline and after-check evidence the agent behavior silently regresses.

## Aliases
- 无证据行为资产改动
- 规则改了但没验证
- skill change without evidence
- governance drift without proof

## Applies When
- 你在改 `AGENTS.md`、`rules/*`、`skills/*`、安装说明或路由约束。Use this page when changing `AGENTS.md`, `rules/*`, `skills/*`, install guidance, or routing rules.
- 你能描述设计，但拿不出 RED baseline 或 before/after eval。Use it when the design sounds coherent but RED baseline or before/after evidence is missing.

## Trigger signals
- A skill, AGENTS file, or rule is rewritten and the author cannot show a RED baseline.
- Installation guidance exists only as prose with no runnable validation path.
- A new workflow is declared complete before fixture or command-level checks run.

## Top Facts
- 行为资产不是普通 prose；它们会改变 agent 的触发、顺序和禁令。Behavior assets are not ordinary prose; they change agent triggers, workflow order, and prohibitions.
- 如果 evidence 只在聊天里，不在 repo 里，这类变更仍然不算 durable。If evidence exists only in chat and not in-repo, the change still fails the durable-memory bar.
- 安装流、路由规则和 skill 触发条件最容易“看起来合理但未验证”。Install flows, routing rules, and skill triggers are the easiest places to over-claim without proof.

## Top Checks
- Confirm whether there is a visible failing baseline or absence-of-proof case for the old wording.
- Confirm whether before/after evidence is staged with the behavior asset change instead of described only in prose.
- Confirm whether there is at least one runnable command, fixture, or walkthrough that exercises the claimed behavior.

## Failure mode
Behavior assets look coherent in text but are not proven in execution. The agent can drift, skip gates, or misroute work while maintainers still believe the system is covered.

## Avoidance
- Require `writing-skills` plus `test-driven-development` for semantic `skills/*` changes.
- Keep baseline/eval artifacts in-repo and stage them with the behavior change.
- Add a minimal command surface whenever install or lifecycle claims need verification.

## Not For
- 这页不适用于纯解释性文档排版优化。This page does not apply to pure explanatory-document polish that does not change agent behavior.

## Watchpoints
- 漂亮的设计文档也可能是行为回归，只要没有可执行证据。A polished design doc can still be a behavior regression if no executable evidence exists.
- 安装工作流最容易被过度宣称，因为人会线性阅读，agent 需要命令级证明。Install workflows are easy to over-claim because humans read linearly while agents need command-level proof.

## Load Next
- 治理安装或 Lore 接入行为：[[projects/account-skills/domains/codex-governance-installation]]。For governance-install or Lore bootstrap behavior: [[projects/account-skills/domains/codex-governance-installation]].
- 稳定规则：[[principles/evidence-before-rollout]]。For the stable rule behind this pitfall: [[principles/evidence-before-rollout]].

## Seen in
- [[projects/account-skills/domains/codex-governance-installation]]

## Related principles
- [[principles/evidence-before-rollout]]

## Notes
Keep the first validation questions visible before the longer process rationale. If the page starts with prose and hides the checks, it has drifted away from the operating contract.
