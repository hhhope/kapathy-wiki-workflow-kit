---
layer: ops
domain: ai-workflow
ops_area: agent-governance
canonical_object: skill-runtime-governance-root-install
artifact_type: retro
title: skill-runtime-governance root 安装记录 / 复盘
type: retro
language: zh-CN
status: active
created_at: 2026-05-24
updated_at: 2026-05-24
ai_generated: true
derived_from:
  - docs/superpowers/specs/2026-05-24-skill-runtime-governance-design.md
  - docs/superpowers/plans/2026-05-24-skill-runtime-governance.md
related_objects:
  - skill-runtime-governance-scope-drift
  - behavior-replay-gate
  - skill-authoring-contract
notes_scope: 记录 root skill-runtime-governance 的本机安装和局部 RED/GREEN 证据边界；不声明 root AGENTS 路由或多端 rollout。
---

# skill-runtime-governance root 安装记录 / 复盘

## 已安装文件

- `/home/yan/.codex/skills/skill-runtime-governance/SKILL.md`
- `/home/yan/.codex/skills/skill-runtime-governance/evaluation.md`

## 证据

- RED baseline：记录在 root evaluation 文件中。
- GREEN replay：记录在 root evaluation 文件中。
- 残余风险：记录在 root evaluation 文件中。
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/skill-runtime-governance-root-install-2026-05-24.md` 没有返回 blocker。
- `python3 scripts/check_wiki_frontmatter.py` 退出码为 0。
- `python3 scripts/check_behavior_assets.py` 退出码为 1，指向一个既有且无关的 evaluation 文件：
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md`.

## RED 边界

提示式 RED 探针全部返回 `PASS`，但这些 prompt 太显式，因为它们已经命名了期望的评估面。
因此失败的 RED 证据来自这个 skill 存在之前的现场事故：

- English-first 行为资产指导泄漏进 `wiki/ops` 记录。
- `$writing-skills` 被当成评估路由问题的中心。
- `skill-runtime-governance` 被缩回 `$superpowers:brainstorming`，随后又被缩成“用户质疑”触发器。
- 对话继续沿着可见技术链条推进，直到用户打断并重新锚定范围。

## GREEN 边界

安装 root skill 后，对全部十个场景运行了 GREEN replay。replay 在行动前选择固定分诊字段，并路由到期望的评估面。

这仍然只是本地压力证据。它不证明自动加载、root `AGENTS.md` 路由，或多客户端 rollout。

## 边界

这页只记录本机 root skill 安装证据。它不声明：

- root `AGENTS.md` 路由已经完成；
- 每个未来事故都会自动发现这个 skill；
- 已经修改 plugin/cache skill；
- 已经具备多客户端或多会话 rollout 证明；
- 仓库行为资产检查器全量干净；这次观察到的非零结果与新 root skill 文件无关。
