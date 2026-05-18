---
title: public-report skill gate wording / explore
layer: ops
type: intake
language: zh-CN
source_path: chat://openspec-explore/public-report-skill-gate-wording/2026-05-11
source_type: conversation
audience: self
knowledge_level: working
domain: report-workflow
ops_area: workflow-trace
canonical_object: public-report-skill-gate-wording
artifact_type: explore
period: active
confidence: medium
status: active
updated_at: 2026-05-11
ai_generated: true
related_sources:
  - .codex/skills/public-report-quality-gate/SKILL.md
  - openspec/changes/enforce-public-report-article-flow-gate/
related_focus_threads: []
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# public-report skill gate wording / explore

## 触发问题

用户指出 `public-report-quality-gate` 新增的 article-flow 门禁使用了
“卡片墙、表格格子、dashboard 面板、奇怪配色块、prompt/Hybrid 脚本残留”
这类表达，其中部分措辞主观、定制化、不可稳定回放。

## 当前关注点

- skill hard rule 应该写成通用、可观察、可复核的触发条件。
- 单次输出事故不能直接原样沉淀成 repo 默认规则。
- 视觉/版式门禁应区分“用户或参考明确选择的输出形态”和“agent 擅自替换的形态”。
- 回放证据应证明未来 agent 能识别同类漂移，而不是只记住这次页面的词。

## 当前假设

- 需要保留“参考形态不能被擅自替换”的门禁方向。
- 需要去掉主观词和过窄枚举，改成以 reference contract、observable divergence、
  prohibited leakage 和 explicit user override 为核心的表述。
- 若要改正式 skill，应退出 explore，走 OpenSpec/TDD/skill evaluation。

## 暂未决定

- 当前已提交 change 是追加修正一个 follow-up change，还是回滚后重做。
- 门禁名称是否继续叫 `Article Flow Layout Gate`，还是改成更通用的
  `Reference Output Shape Gate`。
- 是否需要把“prompt/Hybrid 脚本残留”移到独立的 public-text leakage gate。

## 下一步

- 先在 explore 中确认问题归因和通用表述标准。
- 若确认要改，创建或选择新的 OpenSpec change。
- 按 skill TDD 做 RED baseline、GREEN wording、pressure replay，再提交。
