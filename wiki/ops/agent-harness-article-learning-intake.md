---
title: agent-harness-article-learning / intake
type: intake
canonical_object: agent-harness-article-learning
artifact_type: intake
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: candidate
updated_at: 2026-05-06
ai_generated: true
related_objects:
  - example-driven-capture
  - behavior-asset-governance
derived_from:
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
notes_scope: 记录 agent / harness / eval / managed agents 外部文章精读专题的打开语境。
  本页不是治理设计正文，不把文章结论直接升级成 AGENTS、skill、spec 或 repo policy。
---

# agent-harness-article-learning / intake

## Trigger Question

用户要求对一组 agent / harness / eval / managed agents 文章逐篇精读，并指出：

- 这是新开的学习专题，不是继续塞进既有 behavior-asset governance 框架；
- 当前动作是学习，不是治理；
- 所谓"有用"必须走已确认的证据约束。

## Current Focus

建立一个独立的文章学习容器，让每篇文章都能被精读、标注有用点、说明证据和本地边界。

## Current Hypotheses

1. 文章学习应先作为 `agent-harness-article-learning` 独立对象存在。
2. 与 `behavior-asset-governance` 的关系应是 `related_objects`，不是从属章节。
3. 每篇文章的"有用点"必须至少保留：
   - source
   - claim
   - evidence
   - local usefulness
   - adoption boundary
   - status: accepted / candidate / rejected
4. 文章学习页不能直接产生新 AGENTS、skill、spec 或 checklist；升级需要另走 OpenSpec 或明确的资产更新任务。

## Open Questions

- 最终是每篇文章一页，还是一个专题页内逐篇分节？
- 是否需要把已经误放在 `behavior-asset-governance-zh.md` 的证据表迁移到新专题页，还是先保留为历史校准痕迹？

## Next Step

先回答"为什么要新开"，确认边界后再进入逐篇精读落 wiki。
