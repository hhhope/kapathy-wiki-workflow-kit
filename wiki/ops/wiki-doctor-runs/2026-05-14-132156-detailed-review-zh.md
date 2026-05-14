---
canonical_object: wiki-doctor-review
artifact_type: detailed-review
layer: ops
domain: wiki
ops_area: wiki-runtime
title: wiki-doctor / 中文详细复核单 2026-05-14 13:21:56 UTC
type: review-record
language: zh-CN
status: draft
created_at: 2026-05-14
derived_from:
  - scripts/build_wiki_content_adjudication.py
---

# wiki-doctor 中文详细复核单

## 怎么看这份文件

- 这是一份给人工复核用的诊断清单，不是自动修复结果。
- 已排除 `wiki/ops/wiki-doctor-runs/` 下已有的 doctor 记录，避免 doctor 诊断自己的输出。
- 每个 `detail_ref` 都对应 adjudication package 里的 `full_detail_set`。
- `Candidate frontmatter` 和 `Candidate relations` 都只是候选，不代表批准写入。
- “中文诊断建议”是下一步人工处理建议，不是自动 patch。

## 总览

- candidate_count: 153
- full_detail_count: 153
- review_focus_count: 144
- taxonomy_candidate_count: 0
- drift_trace_count: 71
- safe_to_apply_frontmatter_count: 9
- eval_passed: True
- eval_error_count: 0
- eval_warning_count: 112

## 风险原因分布

- agent_uncertain: 138（分类或判断仍不确定，需要人工确认）
- relation_weak_evidence: 112（关系候选证据不足，不能批量接受）
- openspec_required: 51（涉及治理/行为变化，可能需要 OpenSpec 承接）
- drift_risk: 35（包含 drift / retro / reanchor 等治理漂移信号）
- adr_risk: 34（涉及 ADR 稳定决策页，需要按 ADR 语义复核）

## Drift / Governance 风险分布

- openspec_required: 51（涉及治理/行为变化，可能需要 OpenSpec 承接）
- drift_risk: 35（包含 drift / retro / reanchor 等治理漂移信号）
- adr_risk: 34（涉及 ADR 稳定决策页，需要按 ADR 语义复核）

## 详细复核条目

### 1. detail-0001 - `wiki/ops/20260415100517-转写-yan的快速会议-纪要文本-1-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: unclassified
canonical_object: 20260415100517-转写-yan的快速会议-纪要文本-1
artifact_type: intake
ops_area: workflow-trace
classification_needed: true
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - reminders
```

证据:

- path: wiki/ops/20260415100517-转写-yan的快速会议-纪要文本-1-intake.md
- title: 20260415100517 转写 yan的快速会议 纪要文本 1
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- domain: `auto_accept_unclassified` - unclassified domain requires review before structural write
- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 2. detail-0002 - `wiki/ops/20260415100517-转写-yan的快速会议-逐字稿文本-1-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: unclassified
canonical_object: 20260415100517-转写-yan的快速会议-逐字稿文本-1
artifact_type: intake
ops_area: workflow-trace
classification_needed: true
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - reminders
```

证据:

- path: wiki/ops/20260415100517-转写-yan的快速会议-逐字稿文本-1-intake.md
- title: 20260415100517 转写 yan的快速会议 逐字稿文本 1
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- domain: `auto_accept_unclassified` - unclassified domain requires review before structural write
- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 3. detail-0003 - `wiki/ops/account-knowledge-base-structure-explore.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: account-knowledge-base-structure
artifact_type: explore
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - main-thread
  - public-report-quality-gate
  - reminders
```

证据:

- path: wiki/ops/account-knowledge-base-structure-explore.md
- title: account knowledge base structure explore
- matched domain keyword: wiki
- matched keywords: learning capture, readme, github
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 4. detail-0004 - `wiki/ops/account-knowledge-base-workbench.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: account-knowledge-base
artifact_type: ops-overview
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base-structure
  - behavior-replay-gate
  - learning-capture-routing
  - team-lore-candidates
  - wiki-runtime-auto-routing
derived_from:
  - wiki/ops/account-knowledge-base-structure-explore.md
  - wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md
  - PROJECT.md
  - wiki/index.md
  - wiki/role-boundaries.md
  - wiki/team-lore-candidates.md
```

证据:

- path: wiki/ops/account-knowledge-base-workbench.md
- title: 团队知识库构建路径
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 5. detail-0007 - `wiki/ops/agent-governance-gate-gap-explore-2026-04-18.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agent-governance-gate-gap
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - reminders
```

证据:

- path: wiki/ops/agent-governance-gate-gap-explore-2026-04-18.md
- title: Agent 治理 gate 缺口探索 2026-04-18
- matched domain keyword: wiki
- matched keywords: retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 6. detail-0008 - `wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agent-governance-gate-gap
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - explore-trace
  - main-thread
  - sample
  - sample-explore
```

证据:

- path: wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md
- title: Agent 治理 gate 缺口复盘 2026-04-18
- matched domain keyword: wiki
- matched keywords: retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 7. detail-0009 - `wiki/ops/agent-harness-article-learning-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: agent-harness-article-learning
artifact_type: intake
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - article-learning-capture
  - behavior-asset-governance
  - example-driven-capture
derived_from:
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://mp.weixin.qq.com/s/-nXD7gp75SHeZHHhTh3lNw
```

证据:

- path: wiki/ops/agent-harness-article-learning-intake.md
- title: agent-harness-article-learning / intake
- matched domain keyword: agent-harness
- matched keywords: reading notes
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 8. detail-0010 - `wiki/ops/agent-harness-article-learning.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: agent-harness-article-learning
artifact_type: reading-notes
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - article-learning-capture
  - behavior-asset-governance
  - codex-global-agents-md
  - example-driven-capture
  - learning-capture-routing
derived_from:
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://mp.weixin.qq.com/s/-nXD7gp75SHeZHHhTh3lNw
  - https://mp.weixin.qq.com/s/r__2l_u6oXwzWHyD3wu_ZQ
```

证据:

- path: wiki/ops/agent-harness-article-learning.md
- title: Agent Harness 文章精读
- matched domain keyword: agent-harness
- matched keywords: learning capture, reading notes
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 9. detail-0011 - `wiki/ops/agent-intent-routing-skill-drift-explore-2026-05-13.md`

- 风险原因: drift_risk
- 风险解释: 包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: none
canonical_object: agent-intent-routing-skill-drift
artifact_type: explore-trace
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - explore-trace
```

证据:

- path: wiki/ops/agent-intent-routing-skill-drift-explore-2026-05-13.md
- title: Agent Intent Routing Skill Drift Explore
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。

### 10. detail-0012 - `wiki/ops/agent-readable-wiki-artifact-grouping.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana
canonical_object: wiki-readable-views
artifact_type: artifact-grouping-view
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - agent-readable-wiki-frontmatter
  - agent-readable-wiki-frontmatter-before-graph-automation
  - agent-readable-wiki-graph-extraction-after-structure
  - agent-readable-wiki-naming-before-graph-growth
  - agent-readable-wiki-naming-model
  - agent-readable-wiki-relation-analysis-after-extraction
  - conversation-handoff
  - conversation-north-star-handoff
  - disagreement-management
  - disagreement-management-before-conclusion-promotion
  - disagreement-management-method
  - disagreement-management-replay-harness
  - disagreement-management-replay-validation
  - example-driven-capture-runtime-validation
  - example-driven-wiki-capture
  - explore-trace
  - github-analysis
  - gstack-lark-learning
  - karpathy-skills-learning
  - live-conversation-reanchor-gate
  - nirvana-weekly
  - sample
  - sample-disagreement
  - sample-explore
  - scope-drift
  - wiki-context-injection
  - wiki-frontmatter-model
  - wiki-graph-extraction
  - wiki-naming-model
  - wiki-relation-analysis
  - wiki-runtime-auto-routing
  - wiki-runtime-context
  - wiki-runtime-context-source-integration
  - wiki-self-directed-execution
  - wiki-semantic-scoring
derived_from:
  - wiki-naming-model
  - wiki-frontmatter-model
validates:
  - wiki-readable-views
```

证据:

- path: wiki/ops/agent-readable-wiki-artifact-grouping.md
- title: wiki-readable-views / artifact-grouping-view
- matched domain keyword: nirvana
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 11. detail-0013 - `wiki/ops/agent-readable-wiki-context-injection.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-context-injection
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-auto-routing
  - wiki-runtime-context-source-integration
formalizes:
  - wiki-context-injection
related_objects:
  - sample
  - wiki-runtime-auto-routing
  - wiki-runtime-context
  - wiki-runtime-context-source-integration
```

证据:

- path: wiki/ops/agent-readable-wiki-context-injection.md
- title: wiki-context-injection / method
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 12. detail-0014 - `wiki/ops/agent-readable-wiki-frontmatter.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agent-readable-wiki-frontmatter
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/agent-readable-wiki-frontmatter.md
- title: Agent-Readable Wiki Frontmatter
- matched domain keyword: wiki
- matched keywords: graph, frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 13. detail-0015 - `wiki/ops/agent-readable-wiki-graph-extraction.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-graph-extraction
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - sample
  - wiki-frontmatter-model
  - wiki-naming-model
  - wiki-relation-analysis
formalizes:
  - wiki-graph-extraction
```

证据:

- path: wiki/ops/agent-readable-wiki-graph-extraction.md
- title: Agent-Readable Wiki Graph Extraction
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 14. detail-0016 - `wiki/ops/agent-readable-wiki-naming-model.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agent-readable-wiki-naming-model
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - conversation-handoff
  - disagreement-management
  - sample
  - wiki-naming-model
```

证据:

- path: wiki/ops/agent-readable-wiki-naming-model.md
- title: Agent-Readable Wiki Naming Model
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 15. detail-0017 - `wiki/ops/agent-readable-wiki-relation-analysis.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-relation-analysis
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
formalizes:
  - wiki-relation-analysis
related_objects:
  - sample
```

证据:

- path: wiki/ops/agent-readable-wiki-relation-analysis.md
- title: wiki-relation-analysis / method
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 16. detail-0018 - `wiki/ops/agent-readable-wiki-relation-reading-view.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-readable-views
artifact_type: relation-reading-view
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-readable-wiki-frontmatter
  - agent-readable-wiki-frontmatter-before-graph-automation
  - agent-readable-wiki-naming-before-graph-growth
  - agent-readable-wiki-naming-model
  - conversation-handoff
  - conversation-north-star-handoff
  - disagreement-management
  - disagreement-management-before-conclusion-promotion
  - disagreement-management-method
  - example-driven-wiki-capture
  - github-analysis
  - sample
  - wiki-frontmatter-model
  - wiki-graph-extraction
  - wiki-naming-model
  - wiki-relation-analysis
  - wiki-semantic-scoring
derived_from:
  - wiki-graph-extraction
  - wiki-relation-analysis
validates:
  - wiki-readable-views
```

证据:

- path: wiki/ops/agent-readable-wiki-relation-reading-view.md
- title: wiki-readable-views / relation-reading-view
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 17. detail-0019 - `wiki/ops/agent-readable-wiki-runtime-auto-routing.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-runtime-auto-routing
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-context-source-integration
  - wiki-runtime-context
formalizes:
  - wiki-runtime-auto-routing
related_objects:
  - sample
  - wiki-runtime-context
  - wiki-runtime-context-source-integration
```

证据:

- path: wiki/ops/agent-readable-wiki-runtime-auto-routing.md
- title: wiki-runtime-auto-routing / method
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 18. detail-0020 - `wiki/ops/agent-readable-wiki-runtime-context-source-integration.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-runtime-context-source-integration
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-context
  - wiki-utilization-layer
formalizes:
  - wiki-runtime-context-source-integration
related_objects:
  - sample
  - wiki-runtime-context
  - wiki-utilization-layer
```

证据:

- path: wiki/ops/agent-readable-wiki-runtime-context-source-integration.md
- title: wiki-runtime-context-source-integration / method
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 19. detail-0021 - `wiki/ops/agent-readable-wiki-runtime-context.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-runtime-context
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
formalizes:
  - wiki-runtime-context
related_objects:
  - sample
```

证据:

- path: wiki/ops/agent-readable-wiki-runtime-context.md
- title: wiki-runtime-context / method
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 20. detail-0022 - `wiki/ops/agent-readable-wiki-self-directed-execution.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-self-directed-execution
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki-context-injection
  - wiki-runtime-auto-routing
formalizes:
  - wiki-self-directed-execution
related_objects:
  - sample
  - wiki-context-injection
  - wiki-runtime-auto-routing
```

证据:

- path: wiki/ops/agent-readable-wiki-self-directed-execution.md
- title: wiki-self-directed-execution / method
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 21. detail-0024 - `wiki/ops/agent-readable-wiki-utilization-layer.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-utilization-layer
artifact_type: method
ops_area: wiki-runtime
```

候选关系:

```yaml
formalizes:
  - wiki-utilization-layer
related_objects:
  - sample
```

证据:

- path: wiki/ops/agent-readable-wiki-utilization-layer.md
- title: wiki-utilization-layer / method
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 22. detail-0025 - `wiki/ops/agentic-collaboration-company-playbook-page-explore-2026-05-11.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agentic-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: explore_trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - sample
```

证据:

- path: wiki/ops/agentic-collaboration-company-playbook-page-explore-2026-05-11.md
- title: Agentic Collaboration Company Playbook Page Explore
- matched domain keyword: agentic-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 23. detail-0026 - `wiki/ops/agentic-company-playbook-quality-failure-root-cause-explore-2026-05-11.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: explore_trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - behavior-replay-gate
  - public-report-quality-gate
```

证据:

- path: wiki/ops/agentic-company-playbook-quality-failure-root-cause-explore-2026-05-11.md
- title: Agentic Company Playbook Quality Failure Root Cause Explore
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 24. detail-0027 - `wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: article-evidence-matrix
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md
  - wiki/reports/agentic-product-engineering-collaboration-management-report.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-article-evidence-matrix-2026-05-11.md
- title: Article Evidence Matrix
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 25. detail-0028 - `wiki/ops/agentic-product-engineering-collaboration-company-playbook-report-gate-review.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agentic-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: report_gate_review
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - sample
  - visual-output-routing
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-company-playbook-report-gate-review.md
- title: Company Playbook Report Gate Review
- matched domain keyword: agentic-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 26. detail-0029 - `wiki/ops/agentic-product-engineering-collaboration-company-playbook-role-change-diagnosis-2026-05-12.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: office_hours_design
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-company-playbook-role-change-diagnosis-2026-05-12.md
- title: Company Playbook Role-Change Diagnosis
- matched domain keyword: product-engineering-collaboration
- matched keywords: moc

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 27. detail-0030 - `wiki/ops/agentic-product-engineering-collaboration-image-model-visual-qa-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: visual-qa
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/agentic-visual-assets-v2/00-total-infographic.png
  - wiki/reports/agentic-visual-assets-image-model/00-total-infographic-image-model.png
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-image-model-visual-qa-2026-05-11.md
- title: Image-Model Visual QA
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 28. detail-0031 - `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agentic-collaboration
canonical_object: agentic-product-engineering-collaboration-our-operating-system
artifact_type: report-gate-review
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agentic-product-engineering-collaboration
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-our-operating-system-report-gate-review.md
- title: Report Gate Review
- matched domain keyword: agentic-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 29. detail-0032 - `wiki/ops/agentic-product-engineering-collaboration-our-operating-system-role-change-design-2026-05-12.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: office_hours_design
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agentic-product-engineering-collaboration-our-operating-system
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-our-operating-system-role-change-design-2026-05-12.md
- title: Our Operating System Role-Change Design
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 30. detail-0033 - `wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: report-gate-review
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/reports/agentic-product-engineering-collaboration-management-report.md
  - wiki/reports/agentic-product-engineering-collaboration-newspaper.html
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
- title: agentic-product-engineering-collaboration / report-gate-review
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 31. detail-0034 - `wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: agentic-product-engineering-collaboration
artifact_type: ops-handoff
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/sources/agentic-product-engineering-collaboration-source-map-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-broad-scan-2026-05-11.md
  - wiki/sources/agentic-product-engineering-collaboration-public-timeline-2026-01-to-2026-05.md
  - wiki/sources/agentic-product-engineering-collaboration-podcast-video-discussions-2026-05-11.md
  - wiki/reports/agentic-product-engineering-collaboration-management-report.md
  - wiki/reports/agentic-product-engineering-collaboration-newspaper.html
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/assets/account-wiki-runtime-card.png
  - wiki/reports/assets/account-wiki-validation-card.png
  - wiki/reports/agentic-visual-assets/
related_objects:
  - account-knowledge-base
  - account-knowledge-base-structure
  - agent-harness-article-learning
  - team-knowledge-base-overview
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
- title: Agentic Product Engineering Collaboration / Session Handoff
- matched domain keyword: agent-harness
- matched keywords: wiki-runtime, graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 32. detail-0035 - `wiki/ops/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md`

- 风险原因: agent_uncertain, openspec_required
- 风险解释: 分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: source-hardening-evidence
ops_area: agent-governance
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-source-hardening-300-leads-2026-05-12.md
- title: Agentic Product Engineering Collaboration / 300 Source Leads Hardening Evidence
- matched domain keyword: product-engineering-collaboration
- matched keywords: governance

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 33. detail-0036 - `wiki/ops/agentic-product-engineering-collaboration-split-execution-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: ops-execution-plan
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/reports/assets/
  - wiki/reports/agentic-visual-assets/
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-split-execution-2026-05-11.md
- title: Agentic Product Engineering Collaboration / Split Execution
- matched domain keyword: product-engineering-collaboration
- matched keywords: wiki-runtime, graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 34. detail-0037 - `wiki/ops/agentic-product-engineering-collaboration-visual-production-brief-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: visual-production-brief
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/reports/assets/account-wiki-onepager.png
  - wiki/reports/assets/account-wiki-runtime-card.png
  - wiki/reports/assets/account-wiki-validation-card.png
  - wiki/reports/agentic-visual-assets/
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-visual-production-brief-2026-05-11.md
- title: Visual Production Brief
- matched domain keyword: product-engineering-collaboration
- matched keywords: wiki-runtime, graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 35. detail-0038 - `wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: agentic-product-engineering-collaboration
artifact_type: workflow-gate
ops_area: wiki-runtime
```

候选关系:

```yaml
derived_from:
  - wiki/ops/agentic-product-engineering-collaboration-session-handoff-2026-05-11.md
  - wiki/ops/agentic-product-engineering-collaboration-report-gate-review.md
  - wiki/ops/agentic-product-engineering-collaboration-split-execution-2026-05-11.md
```

证据:

- path: wiki/ops/agentic-product-engineering-collaboration-workflow-gate-2026-05-11.md
- title: Workflow Gate
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 36. detail-0039 - `wiki/ops/agents-governance-281-compression-retro-2026-05-06.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
  - behavior-asset-governance
  - codex-global-agents-md
  - root-governance-alignment
derived_from:
  - openspec/changes/archive/2026-05-06-decide-root-governance-alignment/
  - openspec/changes/compress-codex-agents-md/
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/behavior-asset-governance-design-trace.md
  - wiki/language-policy.md
```

证据:

- path: wiki/ops/agents-governance-281-compression-retro-2026-05-06.md
- title: agents-governance 281 行压缩复盘
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 37. detail-0040 - `wiki/ops/agents-governance-drift-distill-2026-04-21.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: distill
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - agents-governance-drift-distill-calibration
  - archive-review-before-archive
  - conversation-handoff
  - conversation-north-star-handoff
  - disagreement-management
  - openspec-explore-trigger-drift
  - retire-draft-skills-as-runtime-surface
  - sample
  - skill-evaluation-evidence
  - wiki-naming-model
  - wiki-readable-views
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
  - wiki/ops/agents-governance-remediation-explore-2026-04-21.md
  - wiki/ops/openspec-explore-trigger-drift-retro.md
```

证据:

- path: wiki/ops/agents-governance-drift-distill-2026-04-21.md
- title: AGENTS.md 治理漂移二次蒸馏 2026-04-21
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 38. detail-0041 - `wiki/ops/agents-governance-drift-distill-calibration-retro.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift-distill-calibration
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
  - conversation-handoff
  - disagreement-management
  - openspec-explore-trigger-drift
derived_from:
  - wiki/ops/agents-governance-drift-distill-2026-04-21.md
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
  - wiki/ops/openspec-explore-trigger-drift-retro.md
```

证据:

- path: wiki/ops/agents-governance-drift-distill-calibration-retro.md
- title: agents-governance-drift-distill-calibration / retro
- matched domain keyword: wiki
- matched keywords: drift, retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 39. detail-0042 - `wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift-distill-calibration
artifact_type: replay-validation
ops_area: workflow-trace
```

候选关系:

```yaml
derived_from:
  - wiki/ops/agents-governance-drift-distill-calibration-retro.md
  - wiki/ops/distill-calibration-replay-harness.md
validates:
  - disagreement-management-method
related_objects:
  - agents-governance-drift
  - disagreement-management
  - disagreement-management-method
```

证据:

- path: wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md
- title: agents-governance-drift-distill-calibration / replay-validation
- matched domain keyword: wiki
- matched keywords: drift, retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 40. detail-0043 - `wiki/ops/agents-governance-drift-explore.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - conversation-handoff
  - disagreement-management
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-remediation-explore-2026-04-21.md
```

证据:

- path: wiki/ops/agents-governance-drift-explore.md
- title: agents-governance-drift / explore
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 41. detail-0044 - `wiki/ops/agents-governance-drift-playbook-2026-04-21.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: playbook
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift-distill-calibration
  - archive-review-before-archive
  - conversation-handoff
  - disagreement-management
  - retire-draft-skills-as-runtime-surface
derived_from:
  - wiki/ops/agents-governance-drift-distill-2026-04-21.md
```

证据:

- path: wiki/ops/agents-governance-drift-playbook-2026-04-21.md
- title: AGENTS.md 治理漂移候选实施 playbook 2026-04-21
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 42. detail-0045 - `wiki/ops/agents-governance-drift-retro.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - codex-handoff-rules
  - conversation-handoff
  - disagreement-management
  - explore-trace
  - karpathy-skills-learning
  - local-skill-pressure-tests
  - principle-skills-layer
  - sample
  - sample-codex-handoff
  - scope-drift
  - skill-evaluation-evidence
derived_from:
  - wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md
  - wiki/ops/karpathy-skills-learning-retro-2026-04-16.md
  - wiki/ops/scope-drift-retro.md
```

证据:

- path: wiki/ops/agents-governance-drift-retro.md
- title: AGENTS.md 治理漂移复盘 2026-04-21
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 43. detail-0046 - `wiki/ops/agents-governance-remediation-explore-2026-04-21.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - local-skill-pressure-tests
  - skill-evaluation-evidence
  - wiki-readable-views
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
```

证据:

- path: wiki/ops/agents-governance-remediation-explore-2026-04-21.md
- title: AGENTS.md 治理漂移整改方向探索 2026-04-21
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 44. detail-0047 - `wiki/ops/ai-chat-一键安装-skill-探索-2026-04-17.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: ai-workflow
canonical_object: ai-chat-workflow-installer
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - reminders
```

证据:

- path: wiki/ops/ai-chat-一键安装-skill-探索-2026-04-17.md
- title: AI Chat 一键安装 Skill 探索
- existing domain frontmatter
- matched keywords: trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 45. detail-0048 - `wiki/ops/behavior-asset-governance-design-trace.md`

- 风险原因: agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: behavior-asset-governance
artifact_type: design-trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-harness-article-learning
  - agents-governance-drift
  - codex-global-agents-md
  - compress-root-agents-budget
  - disagreement-management
  - disagreement-management-replay-harness
  - phase1-repo-agents-compression
  - repo-agents-loaded-context
  - root-governance-alignment
  - sample
  - skill-authoring-contract
derived_from:
  - openspec/changes/decide-root-governance-alignment/design.md
  - openspec/changes/decide-root-governance-alignment/specs/root-governance-alignment/spec.md
  - openspec/changes/archive/2026-05-06-decide-root-governance-alignment/evaluation.md
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/agent-harness-article-learning.md
  - openspec/changes/compress-root-agents-budget/proposal.md
  - openspec/changes/phase1-repo-agents-compression/proposal.md
  - AGENTS.md
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  - https://github.com/anthropics/skills
  - https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
  - https://arxiv.org/html/2602.11988v1
  - https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b
  - https://github.com/danielrosehill/Agents.md-Templates
  - https://raw.githubusercontent.com/openai/codex/main/AGENTS.md
  - https://www.philschmid.de/agent-harness-2026
  - https://calv.info/agents-feb-2026
  - https://github.com/github/spec-kit/blob/main/spec-driven.md
  - https://inspect.aisi.org.uk/
  - https://www.promptfoo.dev/docs/red-team
  - https://promptfoo.dev/docs/integrations/ci-cd/
```

证据:

- path: wiki/ops/behavior-asset-governance-design-trace.md
- title: behavior-asset-governance / design-trace
- matched domain keyword: agent-harness
- matched keywords: frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 46. detail-0049 - `wiki/ops/behavior-asset-governance-zh.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: behavior-asset-governance
artifact_type: summary
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agent-harness-article-learning
  - agents-governance-drift
  - codex-global-agents-md
  - root-governance-alignment
derived_from:
  - wiki/ops/behavior-asset-governance-design-trace.md
  - openspec/changes/decide-root-governance-alignment/design.md
  - wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
  - wiki/ops/agents-governance-281-compression-retro-2026-05-06.md
  - https://openai.com/index/harness-engineering/
  - https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
  - https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - https://www.anthropic.com/research/diff-tool
  - https://www.anthropic.com/engineering/managed-agents
  - https://www.anthropic.com/engineering/harness-design-long-running-apps
  - https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
```

证据:

- path: wiki/ops/behavior-asset-governance-zh.md
- title: 行为资产治理 · 中文摘要
- matched domain keyword: agent-harness
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 47. detail-0051 - `wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md`

- 风险原因: drift_risk
- 风险解释: 包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: brainstorming-drift-wiki-trace
artifact_type: retro
ops_area: agent-governance
```

候选关系:

```yaml
related_objects:
  - live-conversation-reanchor-gate
  - openspec-explore-wiki-trace
  - retros-stay-separate-from-adrs
  - wiki-react-decision-trace
  - wiki-runtime-layer-contract
derived_from:
  - chat://2026-05-14/wiki-runtime-brainstorming-drift
  - openspec/changes/add-brainstorming-drift-wiki-trace/design.md
```

证据:

- path: wiki/ops/brainstorming-drift-wiki-trace-retro-2026-05-14.md
- title: brainstorming-drift-wiki-trace / retro
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。

### 48. detail-0052 - `wiki/ops/check-to-wiki-routing-explore.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: check-to-wiki-routing
artifact_type: intake
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - conversation-handoff
  - example-driven-capture
  - example-driven-wiki-capture
  - material-collaboration-defaults
  - meeting-note
```

证据:

- path: wiki/ops/check-to-wiki-routing-explore.md
- title: check-to-wiki-routing / intake
- matched domain keyword: wiki
- matched keywords: readme
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 49. detail-0053 - `wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: codex-global-agents-md
artifact_type: intake
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-governance-gate-gap
  - agents-governance-drift
  - root-governance-alignment
  - sample
derived_from:
  - https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
  - https://arxiv.org/html/2602.11988v1
  - https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b
  - https://github.com/danielrosehill/Agents.md-Templates
  - https://raw.githubusercontent.com/openai/codex/main/AGENTS.md
```

证据:

- path: wiki/ops/codex-global-agents-md-diagnosis-intake-2026-04-25.md
- title: ~/.codex/AGENTS.md 全局文件诊断
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 50. detail-0054 - `wiki/ops/codex-handoff-rules.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: codex-handoff-rules
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/codex-handoff-rules.md
- title: Codex Handoff 规则
- matched domain keyword: wiki
- default ops fallback requires review

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 51. detail-0055 - `wiki/ops/completion-bridge-drift-explore-2026-05-12.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: completion-bridge-drift
artifact_type: explore-trace
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - add-product-status-contract
  - conversation-handoff
  - explore-trace
  - openspec-explore-trigger-drift
  - product-status-contract
  - reminders
```

证据:

- path: wiki/ops/completion-bridge-drift-explore-2026-05-12.md
- title: completion-bridge-drift / explore
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 52. detail-0056 - `wiki/ops/conversation-handoff-mode.md`

- 风险原因: agent_uncertain, drift_risk
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: conversation-handoff
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
formalizes:
  - conversation-handoff
```

证据:

- path: wiki/ops/conversation-handoff-mode.md
- title: conversation-handoff / method
- matched domain keyword: wiki
- matched keywords: retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 53. detail-0057 - `wiki/ops/disagreement-management-method.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: disagreement-management
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - disagreement-management-method
```

证据:

- path: wiki/ops/disagreement-management-method.md
- title: 分歧管理方法
- matched domain keyword: wiki
- matched keywords: drift, retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 54. detail-0058 - `wiki/ops/disagreement-management-replay-harness.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: disagreement-management-replay-harness
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - disagreement-management
```

证据:

- path: wiki/ops/disagreement-management-replay-harness.md
- title: 分歧管理 Replay Harness
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 55. detail-0059 - `wiki/ops/disagreement-management-replay-validation-2026-04-20.md`

- 风险原因: agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: disagreement-management-replay-validation
artifact_type: method
ops_area: agent-governance
```

候选关系:

```yaml
related_objects:
  - disagreement-management
```

证据:

- path: wiki/ops/disagreement-management-replay-validation-2026-04-20.md
- title: 分歧管理 Replay 验证 2026-04-20
- matched domain keyword: wiki
- matched keywords: governance, adr
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 56. detail-0060 - `wiki/ops/distill-calibration-replay-harness.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: agents-governance-drift-distill-calibration
artifact_type: replay-harness
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
```

证据:

- path: wiki/ops/distill-calibration-replay-harness.md
- title: Distill Calibration Replay Harness
- matched domain keyword: wiki
- matched keywords: drift, retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 57. detail-0061 - `wiki/ops/evolver-self-evolving-harness-reading-notes.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: evolver-self-evolving-harness
artifact_type: reading-notes
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - agent-harness-article-learning
  - public-report-quality-gate
  - team-knowledge-base-overview
derived_from:
  - https://mp.weixin.qq.com/s/L8H0Kl0ecXOk7yTwpI7RTA
```

证据:

- path: wiki/ops/evolver-self-evolving-harness-reading-notes.md
- title: Evolver Self-Evolving Harness / Reading Notes
- existing domain frontmatter
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 58. detail-0062 - `wiki/ops/example-driven-capture-runtime-validation-2026-04-18.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: example-driven-capture-runtime-validation
artifact_type: method
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - example-driven-wiki-capture
  - gstack-lark-learning
  - main-thread
```

证据:

- path: wiki/ops/example-driven-capture-runtime-validation-2026-04-18.md
- title: 例子驱动留痕运行时验证 2026-04-18
- matched domain keyword: wiki
- matched keywords: readme, github
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 59. detail-0063 - `wiki/ops/example-driven-wiki-capture.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: example-driven-wiki-capture
artifact_type: method
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - behavior-asset-governance
  - root-governance-alignment
```

证据:

- path: wiki/ops/example-driven-wiki-capture.md
- title: 例子驱动的 Wiki 留痕
- matched domain keyword: wiki
- matched keywords: readme
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 60. detail-0064 - `wiki/ops/feishu-image-client-freeze-explore-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: public-report-output
canonical_object: feishu-image-client-freeze
artifact_type: explore
ops_area: report-quality
```

候选关系:

```yaml
related_objects:
  - account-wiki-public-draft-repair
  - reminders
  - team-knowledge-base-overview
```

证据:

- path: wiki/ops/feishu-image-client-freeze-explore-2026-05-09.md
- title: Feishu image client freeze explore
- existing domain frontmatter
- matched keywords: report gate, public report
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 61. detail-0065 - `wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: unclassified
canonical_object: go-engineering-security-rule
artifact_type: source-learning
ops_area: learning-capture
classification_needed: true
```

候选关系:

```yaml
derived_from:
  - https://mp.weixin.qq.com/s/3hQC4BYmU1-h_WfbOmXOhg
  - https://mp.weixin.qq.com/s/8SoRM1Q_nR_JtXuQhLMafg
  - https://mp.weixin.qq.com/s/NpDiSiiG_PFX15vYheEsqw
  - https://mp.weixin.qq.com/s/SxnMbThrsgB3Q6hTZRX69Q
  - https://mp.weixin.qq.com/s/KcKm8BNBYV91zlbxTIz9yw
  - https://mp.weixin.qq.com/s/pJSibD0QYrbhSqcy4V4EMQ
  - https://mp.weixin.qq.com/s/sWnXjrWpTjYO9ZGTaOIlJQ
  - https://go.dev/doc/modules/layout
  - https://go.dev/wiki/CodeReviewComments
  - https://google.github.io/styleguide/go/guide
  - https://github.com/uber-go/guide
  - https://github.com/golang-standards/project-layout
```

证据:

- path: wiki/ops/go-engineering-security-rule-source-learning-2026-05-13.md
- title: Go Engineering Security Rule / Source Learning
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- domain: `auto_accept_unclassified` - unclassified domain requires review before structural write

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 62. detail-0066 - `wiki/ops/gstack-lark-learning-retro-2026-04-18.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: gstack-lark-learning
artifact_type: retro
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - main-thread
```

证据:

- path: wiki/ops/gstack-lark-learning-retro-2026-04-18.md
- title: gstack 与 larksuite CLI 学习复盘 2026-04-18
- matched domain keyword: wiki
- matched keywords: readme, github
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 63. detail-0067 - `wiki/ops/harness-engineering-overview-reading-notes.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: harness-engineering-overview
artifact_type: reading-notes
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - evolver-self-evolving-harness
  - public-report-quality-gate
  - team-knowledge-base-overview
derived_from:
  - https://mp.weixin.qq.com/s/x2BZgM1boc_TmdosO78XVA
```

证据:

- path: wiki/ops/harness-engineering-overview-reading-notes.md
- title: Harness Engineering Overview / Reading Notes
- existing domain frontmatter
- matched keywords: reading notes, github
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 64. detail-0068 - `wiki/ops/hermes-self-evolution-gap-explore-2026-04-16.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: hermes-self-evolution-gap
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - reminders
```

证据:

- path: wiki/ops/hermes-self-evolution-gap-explore-2026-04-16.md
- title: Hermes 自进化缺口探索 2026-04-16
- matched domain keyword: wiki
- matched keywords: trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 65. detail-0069 - `wiki/ops/intelligence-native-organization-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: intelligence-native-organization
artifact_type: intake
ops_area: report-quality
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
  - behavior-asset-governance
  - root-governance-alignment
derived_from:
  - https://block.xyz/inside/from-hierarchy-to-intelligence
  - https://sequoiacap.com/article/from-hierarchy-to-intelligence/
  - https://investors.block.xyz/governance/leadership/default.aspx
  - https://www.pbs.org/newshour/amp/economy/ai-is-key-driver-behind-layoffs-at-fintech-company-block-ceo-says
  - https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w
```

证据:

- path: wiki/ops/intelligence-native-organization-intake.md
- title: intelligence-native-organization / intake
- matched domain keyword: wiki
- matched keywords: h5
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 66. detail-0071 - `wiki/ops/karpathy-skills-learning-retro-2026-04-16.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: karpathy-skills-learning
artifact_type: retro
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - meeting-note
```

证据:

- path: wiki/ops/karpathy-skills-learning-retro-2026-04-16.md
- title: Karpathy Skills 学习复盘 2026-04-16
- matched domain keyword: wiki
- matched keywords: github
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 67. detail-0073 - `wiki/ops/learning-source-routing-gap-explore-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: learning-source-routing-gap
artifact_type: explore-trace
ops_area: learning-capture
```

候选关系:

```yaml
related_objects:
  - example-driven-capture
  - example-driven-wiki-capture
  - explore-trace
  - learning-capture-routing
  - learning-note
  - obsidian-wiki-reference-gap-review
derived_from:
  - wiki/index.md
  - wiki/ops/learning-capture-routing.md
  - wiki/ops/example-driven-wiki-capture.md
  - .codex/skills/learning-capture/SKILL.md
  - .codex/skills/readme-learning-capture/SKILL.md
```

证据:

- path: wiki/ops/learning-source-routing-gap-explore-2026-05-09.md
- title: learning-source-routing-gap / explore-trace
- matched domain keyword: wiki
- matched keywords: learning capture, readme
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 68. detail-0074 - `wiki/ops/live-conversation-reanchor-gate-replay-harness.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: live-conversation-reanchor-gate
artifact_type: replay-harness
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - disagreement-management
  - live-conversation-reanchor-gate-replay
validates:
  - live-conversation-reanchor-gate
```

证据:

- path: wiki/ops/live-conversation-reanchor-gate-replay-harness.md
- title: live-conversation-reanchor-gate / replay-harness
- matched domain keyword: wiki
- matched keywords: drift, reanchor
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 69. detail-0075 - `wiki/ops/live-conversation-reanchor-gate-retro.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: live-conversation-reanchor-gate
artifact_type: retro
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - disagreement-management
derived_from:
  - disagreement-management
```

证据:

- path: wiki/ops/live-conversation-reanchor-gate-retro.md
- title: live-conversation-reanchor-gate / retro
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 70. detail-0076 - `wiki/ops/llm-wiki-core-product-contract.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: llm-wiki-core-product-contract
artifact_type: product-contract
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - explore-trace
  - learning-source-routing-gap
  - obsidian-wiki-reference-gap-review
  - product-capability-and-graph-gap
  - report-wiki-product-plan
derived_from:
  - PROJECT.md
  - wiki/ops/report-wiki-product-plan-2026-05-09.md
  - wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
  - wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
  - /home/yan/.gstack/projects/clearing-account-meeting-lore/yan-feat-refine-openspec-explore-trace-model-design-20260509-114904-llm-wiki-core-value.md
```

证据:

- path: wiki/ops/llm-wiki-core-product-contract.md
- title: LLM Wiki core product contract
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 71. detail-0077 - `wiki/ops/main-thread.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: main-thread
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - project-management-weekly-loop
  - reminders
```

证据:

- path: wiki/ops/main-thread.md
- title: 主线面板
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 72. detail-0078 - `wiki/ops/multi-system-branch-spec-explore-2026-05-12.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: multi-system-branch-spec
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - product-status-contract
  - reminders
```

证据:

- path: wiki/ops/multi-system-branch-spec-explore-2026-05-12.md
- title: multi-system branch spec explore
- existing domain frontmatter
- matched keywords: trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 73. detail-0079 - `wiki/ops/nirvana-preview-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana
canonical_object: nirvana-preview
artifact_type: intake
ops_area: source-intake
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - nirvana-weekly
  - reminders
```

证据:

- path: wiki/ops/nirvana-preview-intake.md
- title: preview
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 74. detail-0080 - `wiki/ops/nirvana-weekly-intake-2026-04-13.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana-project
canonical_object: nirvana-weekly
artifact_type: intake
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - nirvana-weekly-reminder
  - project-management-weekly-loop
  - reminders
```

证据:

- path: wiki/ops/nirvana-weekly-intake-2026-04-13.md
- title: 涅槃项目周推进 intake 2026-04-13
- existing domain frontmatter
- matched keywords: drift
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 75. detail-0081 - `wiki/ops/nirvana-weekly-reminder-2026-04-13.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana-project
canonical_object: nirvana-weekly-reminder
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - nirvana-weekly
```

证据:

- path: wiki/ops/nirvana-weekly-reminder-2026-04-13.md
- title: 涅槃项目本周跟进提醒 2026-04-13
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 76. detail-0082 - `wiki/ops/nirvana-协议支付涅槃需求文档-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana
canonical_object: nirvana-协议支付涅槃需求文档
artifact_type: intake
ops_area: source-intake
```

候选关系:

```yaml
related_objects:
  - nirvana-涅槃产品上架梳理
  - reminders
```

证据:

- path: wiki/ops/nirvana-协议支付涅槃需求文档-intake.md
- title: 协议支付涅槃需求文档
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 77. detail-0083 - `wiki/ops/nirvana-涅槃产品上架梳理-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana
canonical_object: nirvana-涅槃产品上架梳理
artifact_type: intake
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - reminders
```

证据:

- path: wiki/ops/nirvana-涅槃产品上架梳理-intake.md
- title: 涅槃产品上架梳理
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 78. detail-0084 - `wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: obsidian-wiki-reference-gap-review
artifact_type: learning-note
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - account-knowledge-base-workbench
  - agent-readable-wiki
  - learning-capture-routing
  - learning-note
  - main-thread
  - sample
derived_from:
  - https://github.com/Ar9av/obsidian-wiki
validates:
  - readme-learning-capture
```

证据:

- path: wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
- title: obsidian-wiki project gap review / learning-note
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 79. detail-0085 - `wiki/ops/openspec-explore-trigger-drift-retro.md`

- 风险原因: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: openspec-explore-trigger-drift
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
  - conversation-handoff
  - disagreement-management
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
```

证据:

- path: wiki/ops/openspec-explore-trigger-drift-retro.md
- title: openspec-explore-trigger-drift / retro
- matched domain keyword: wiki
- matched keywords: drift, retro, trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 80. detail-0086 - `wiki/ops/product-alignment-drift-explore-2026-05-09.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: product-alignment-drift
artifact_type: explore-trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - explore-trace
  - learning-source-routing-gap
  - obsidian-wiki-reference-gap-review
  - product-capability-and-graph-gap
  - product-status-contract
  - report-wiki-product-plan
  - scorecard-calibration-gap
derived_from:
  - wiki/ops/report-wiki-product-plan-2026-05-09.md
  - wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
  - wiki/ops/scorecard-calibration-gap-explore-2026-05-09.md
  - wiki/ops/learning-source-routing-gap-explore-2026-05-09.md
  - wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
```

证据:

- path: wiki/ops/product-alignment-drift-explore-2026-05-09.md
- title: product-alignment-drift / explore-trace
- matched domain keyword: wiki
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 81. detail-0087 - `wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: product-capability-and-graph-gap
artifact_type: explore-trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - agent-readable-wiki
  - explore-trace
  - obsidian-wiki-reference-gap-review
derived_from:
  - PROJECT.md
  - wiki/index.md
  - wiki/ops/account-knowledge-base-workbench.md
  - wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
```

证据:

- path: wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
- title: product-capability-and-graph-gap / explore-trace
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 82. detail-0088 - `wiki/ops/project-management-weekly-loop.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: project-management-weekly-loop
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - reminders
```

证据:

- path: wiki/ops/project-management-weekly-loop.md
- title: 项目管理周推进循环
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 83. detail-0089 - `wiki/ops/public-report-skill-gate-wording-explore-2026-05-11.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: report-workflow
canonical_object: public-report-skill-gate-wording
artifact_type: explore
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - public-report-quality-gate
  - reminders
```

证据:

- path: wiki/ops/public-report-skill-gate-wording-explore-2026-05-11.md
- title: public-report skill gate wording / explore
- existing domain frontmatter
- matched keywords: trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 84. detail-0090 - `wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md`

- 风险原因: drift_risk
- 风险解释: 包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: readme-capability-map-boundary
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - brainstorming-drift-wiki-trace
  - obsidian-moc-projection
  - wiki-runtime-layer-boundary
derived_from:
  - chat://2026-05-14/readme-capability-map-drift
  - openspec/changes/document-readme-capability-map-boundary/design.md
```

证据:

- path: wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md
- title: README Capability Map Boundary / Drift Retro
- existing domain frontmatter
- existing ops_area frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。

### 85. detail-0091 - `wiki/ops/reference-driven-output-calibration-retro.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: reference-driven-output-calibration
artifact_type: retro
ops_area: report-quality
```

候选关系:

```yaml
related_objects:
  - disagreement-management
  - example-driven-capture
  - intelligence-native-organization
  - weixin-reference-wiki-capture
  - xiaohongshu-retro-grid-content
derived_from:
  - wiki/ops/intelligence-native-organization-intake.md
  - wiki/ops/intelligence-native-organization-h5.html
  - wiki/ops/intelligence-native-organization-handdrawn-h5.html
  - https://mp.weixin.qq.com/s/b_uLQlu-yTyHncFybc8g2w
```

证据:

- path: wiki/ops/reference-driven-output-calibration-retro.md
- title: reference-driven-output-calibration / retro
- matched domain keyword: wiki
- matched keywords: h5
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 86. detail-0092 - `wiki/ops/reminders.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: nirvana
canonical_object: reminders
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - nirvana-weekly
  - nirvana-weekly-reminder
  - project-management-weekly-loop
```

证据:

- path: wiki/ops/reminders.md
- title: 提醒面板
- matched domain keyword: nirvana
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 87. detail-0093 - `wiki/ops/report-wiki-product-plan-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: report-wiki-product-plan
artifact_type: product-plan
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - obsidian-wiki-reference-gap-review
  - product-capability-and-graph-gap
  - wiki-status-dashboard
derived_from:
  - PROJECT.md
  - wiki/ops/account-knowledge-base-workbench.md
  - wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
  - wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
```

证据:

- path: wiki/ops/report-wiki-product-plan-2026-05-09.md
- title: report-wiki product plan / 2026-05-09
- matched domain keyword: wiki
- matched keywords: graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 88. detail-0094 - `wiki/ops/root-capability-extraction-retro.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: root-capability-extraction
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - learning-capture-routing
  - meeting-note
  - principle-skills-layer
  - repo-agents-loaded-context
  - root-governance-alignment
derived_from:
  - openspec/specs/principle-skills-layer/spec.md
  - openspec/specs/repo-agents-loaded-context/spec.md
  - openspec/specs/root-governance-alignment/spec.md
  - wiki/ops/learning-capture-routing.md
```

证据:

- path: wiki/ops/root-capability-extraction-retro.md
- title: root-capability-extraction / retro
- matched domain keyword: wiki
- matched keywords: retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 89. detail-0095 - `wiki/ops/sample-codex-handoff.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample-codex-handoff
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - reminders
  - sample
  - sample-reminder
```

证据:

- path: wiki/ops/sample-codex-handoff.md
- title: 实现 inbox 到 source 草稿生成
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 90. detail-0096 - `wiki/ops/sample-disagreement-retro.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample-disagreement
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - sample
```

证据:

- path: wiki/ops/sample-disagreement-retro.md
- title: 分歧管理 retro 示例
- matched domain keyword: wiki
- matched keywords: retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 91. detail-0097 - `wiki/ops/sample-explore-trace.md`

- 风险原因: agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample-explore
artifact_type: trace
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - explore-trace
  - main-thread
  - reminders
  - sample
```

证据:

- path: wiki/ops/sample-explore-trace.md
- title: OpenSpec 探索留痕样例
- matched domain keyword: wiki
- matched keywords: trace
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 92. detail-0098 - `wiki/ops/sample-focus-thread.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample-focus-thread
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - reminders
  - sample
  - sample-reminder
```

证据:

- path: wiki/ops/sample-focus-thread.md
- title: 个人操作系统 MVP
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 93. detail-0099 - `wiki/ops/sample-handoff-topic.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: conversation-handoff
artifact_type: sample
ops_area: workflow-trace
```

候选关系:

```yaml
derived_from:
  - chat://handoff-mode/sample-north-star
validates:
  - conversation-handoff
related_objects:
  - agent-governance-gate-gap
  - main-thread
  - reminders
  - sample
```

证据:

- path: wiki/ops/sample-handoff-topic.md
- title: conversation-handoff / sample
- matched domain keyword: wiki
- matched keywords: retro
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 94. detail-0100 - `wiki/ops/sample-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample
artifact_type: intake
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - main-thread
  - reminders
```

证据:

- path: wiki/ops/sample-intake.md
- title: 研发任务派发想法记录
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 95. detail-0101 - `wiki/ops/sample-reminder.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: sample-reminder
artifact_type: method
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - sample
  - sample-focus-thread
```

证据:

- path: wiki/ops/sample-reminder.md
- title: 设计 Codex 任务升级规则
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 96. detail-0102 - `wiki/ops/scope-drift-retro.md`

- 风险原因: agent_uncertain, drift_risk
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: scope-drift
artifact_type: retro
ops_area: workflow-trace
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/scope-drift-retro.md
- title: Scope Drift 复盘
- matched domain keyword: wiki
- matched keywords: drift, retro

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 97. detail-0103 - `wiki/ops/scorecard-calibration-gap-explore-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: scorecard-calibration-gap
artifact_type: explore-trace
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agent-harness-article-learning
  - article-learning-capture
  - behavior-replay-gate
  - explore-trace
  - learning-capture-routing
  - product-capability-and-graph-gap
  - public-report-quality-gate
  - sample
  - team-knowledge-base-overview
derived_from:
  - .codex/skills/article-learning-capture/references/scorecard.md
  - .codex/skills/readme-learning-capture/references/scorecard.md
  - .codex/skills/public-report-quality-gate/references/scorecard.md
  - wiki/ops/agent-harness-article-learning.md
  - wiki/ops/team-knowledge-base-overview-report-gate-review.md
```

证据:

- path: wiki/ops/scorecard-calibration-gap-explore-2026-05-09.md
- title: scorecard-calibration-gap / explore-trace
- matched domain keyword: agent-harness
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 98. detail-0104 - `wiki/ops/superpowers-brainstorming-skill-visibility-explore-2026-05-14.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: superpowers-brainstorming-skill-visibility
artifact_type: explore
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/superpowers-brainstorming-skill-visibility-explore-2026-05-14.md
- title: superpowers-brainstorming-skill-visibility / explore
- matched domain keyword: wiki
- matched keywords: frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 99. detail-0105 - `wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: team-knowledge-base-overview
artifact_type: runtime-replay
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - public-report-quality-gate
  - public-report-reviewer
derived_from:
  - wiki/reports/team-knowledge-base-overview.md
  - .codex/skills/public-report-quality-gate/SKILL.md
  - .codex/skills/public-report-quality-gate/references/scorecard.md
  - .codex/skills/public-report-quality-gate/references/gate-review-artifact.md
  - .codex/agents/public-report-reviewer.md
validates:
  - openspec/changes/add-public-report-paragraph-drift-gate
```

证据:

- path: wiki/ops/team-knowledge-base-overview-paragraph-drift-runtime-replay-2026-05-11.md
- title: team-knowledge-base-overview / paragraph-drift-runtime-replay
- matched domain keyword: wiki
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 100. detail-0106 - `wiki/ops/team-knowledge-base-overview-report-gate-review.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: agent-harness
canonical_object: account-knowledge-base
artifact_type: report-gate-review
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - account-knowledge-base
  - account-knowledge-base-structure
  - agent-harness-article-learning
  - agent-readable-wiki-frontmatter
  - evolver-self-evolving-harness
  - harness-engineering-overview
  - karpathy-llm-wiki
  - public-report-quality-gate
  - reference-driven-output-calibration
  - team-knowledge-base-overview
  - wiki-graph-extraction
derived_from:
  - .codex/skills/public-report-quality-gate/SKILL.md
  - .codex/skills/public-report-quality-gate/references/scorecard.md
  - .codex/skills/public-report-quality-gate/references/report-group-templates.md
  - wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md
  - wiki/ops/account-knowledge-base-structure-explore.md
validates:
  - wiki/ops/account-knowledge-base-workbench.md
```

证据:

- path: wiki/ops/team-knowledge-base-overview-report-gate-review.md
- title: account-knowledge-base / overview-report-gate-review
- matched domain keyword: agent-harness
- matched keywords: wiki-runtime, graph, frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 101. detail-0107 - `wiki/ops/visual-output-routing-drift-explore-2026-05-11.md`

- 风险原因: agent_uncertain, drift_risk, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: product-engineering-collaboration
canonical_object: visual-output-routing-drift
artifact_type: intake
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - agentic-product-engineering-collaboration
  - article-learning-capture
  - public-report-quality-gate
  - visual-output-routing
```

证据:

- path: wiki/ops/visual-output-routing-drift-explore-2026-05-11.md
- title: Visual Output Routing Drift / Explore
- matched domain keyword: product-engineering-collaboration
- matched keywords: graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 102. detail-0108 - `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: visual-output-routing
artifact_type: explore_trace
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md
- title: Visual Output Routing Fix Recheck
- matched domain keyword: wiki
- matched keywords: graph

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 103. detail-0109 - `wiki/ops/visual-output-routing-residual-fallback-repair-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: visual-output-routing
artifact_type: skill_fix_evidence
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/visual-output-routing-residual-fallback-repair-2026-05-11.md
- title: Visual Output Routing Residual Fallback Repair
- matched domain keyword: wiki
- matched keywords: graph

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 104. detail-0110 - `wiki/ops/visual-output-routing-skill-fix-evidence-2026-05-11.md`

- 风险原因: agent_uncertain
- 风险解释: 分类或判断仍不确定，需要人工确认
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: visual-output-routing
artifact_type: skill_fix_evidence
ops_area: wiki-runtime
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/visual-output-routing-skill-fix-evidence-2026-05-11.md
- title: Visual Output Routing Skill Fix Evidence
- matched domain keyword: wiki
- matched keywords: graph

不自动应用的原因:

- 无

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 105. detail-0114 - `wiki/ops/wiki-readable-views-validation-harness.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-readable-views-validation
artifact_type: replay-harness
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - sample
  - wiki-readable-views
validates:
  - wiki-readable-views
```

证据:

- path: wiki/ops/wiki-readable-views-validation-harness.md
- title: wiki-readable-views-validation / replay-harness
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 106. detail-0115 - `wiki/ops/wiki-runtime-command-surface-explore-2026-05-09.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-runtime-command-surface
artifact_type: explore
ops_area: wiki-runtime
```

候选关系:

```yaml
related_objects:
  - llm-wiki-core-product-contract
  - wiki-runtime-slash-command-surface
  - wiki-status-slash-command
```

证据:

- path: wiki/ops/wiki-runtime-command-surface-explore-2026-05-09.md
- title: Wiki Runtime Command Surface Explore
- matched domain keyword: wiki
- matched keywords: wiki-runtime, graph
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 107. detail-0118 - `wiki/ops/wiki-status-slash-command-reanchor.md`

- 风险原因: agent_uncertain, drift_risk
- 风险解释: 分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, drift_risk
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: wiki-status-slash-command
artifact_type: reanchor
ops_area: workflow-trace
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/ops/wiki-status-slash-command-reanchor.md
- title: Wiki Status Slash Command Reanchor
- matched domain keyword: wiki
- matched keywords: drift, reanchor

不自动应用的原因:

- 无

中文诊断建议:

- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 108. detail-0119 - `wiki/ops/宝财通分账开通与迁移边界提醒-2026-04-16.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: unclassified
canonical_object: baocaitong-split-account-migration
artifact_type: reminder
ops_area: workflow-trace
classification_needed: true
```

候选关系:

```yaml
related_objects:
  - 文字转写-呼呼的快速会议-276823523
```

证据:

- path: wiki/ops/宝财通分账开通与迁移边界提醒-2026-04-16.md
- title: 宝财通分账开通与迁移边界提醒 2026-04-16
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- domain: `auto_accept_unclassified` - unclassified domain requires review before structural write
- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 109. detail-0120 - `wiki/ops/宝财通分账开通迁移场景对照表-2026-04-16.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: wiki
canonical_object: baocaitong-split-account-migration
artifact_type: scenario-matrix
ops_area: workflow-trace
```

候选关系:

```yaml
related_objects:
  - baocaitong-split-account-migration
  - 文字转写-呼呼的快速会议-276823523
derived_from:
  - wiki/ops/文字转写-呼呼的快速会议-276823523-intake.md
```

证据:

- path: wiki/ops/宝财通分账开通迁移场景对照表-2026-04-16.md
- title: 宝财通分账开通迁移场景对照表 2026-04-16
- matched domain keyword: wiki
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 110. detail-0121 - `wiki/ops/文字转写-呼呼的快速会议-276823523-intake.md`

- 风险原因: agent_uncertain, relation_weak_evidence
- 风险解释: 分类或判断仍不确定，需要人工确认；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: agent_uncertain, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: ops
domain: unclassified
canonical_object: 文字转写-呼呼的快速会议-276823523
artifact_type: intake
ops_area: workflow-trace
classification_needed: true
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - reminders
```

证据:

- path: wiki/ops/文字转写-呼呼的快速会议-276823523-intake.md
- title: 文字转写 呼呼的快速会议 276823523
- existing domain frontmatter
- default ops fallback requires review
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- domain: `auto_accept_unclassified` - unclassified domain requires review before structural write
- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 111. detail-0122 - `wiki/adr/0001-repository-default-workflow-changes-require-openspec.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: repository-default-workflow-changes-require-openspec
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0001-repository-default-workflow-changes-require-openspec.md
- title: ADR-0001 Repository-Default Workflow Changes Require OpenSpec
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 112. detail-0123 - `wiki/adr/0002-stable-decisions-live-in-wiki-adr.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: stable-decisions-live-in-wiki-adr
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0002-stable-decisions-live-in-wiki-adr.md
- title: ADR-0002 Stable Decisions Live In Wiki ADR
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 113. detail-0124 - `wiki/adr/0003-retros-stay-separate-from-adrs.md`

- 风险原因: adr_risk, agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: retros-stay-separate-from-adrs
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - scope-drift
```

证据:

- path: wiki/adr/0003-retros-stay-separate-from-adrs.md
- title: ADR-0003 Retros Stay Separate From ADRs
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 114. detail-0125 - `wiki/adr/0004-agent-self-evolution-over-skill-governance.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-self-evolution-over-skill-governance
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0004-agent-self-evolution-over-skill-governance.md
- title: ADR-0004 Agent Self-Evolution Over Skill Governance
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 115. detail-0126 - `wiki/adr/0005-incremental-refresh-over-full-reprocessing.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: incremental-refresh-over-full-reprocessing
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0005-incremental-refresh-over-full-reprocessing.md
- title: ADR-0005 Incremental Refresh Over Full Reprocessing
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 116. detail-0127 - `wiki/adr/0006-formal-project-local-skills-over-drafts.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: formal-project-local-skills-over-drafts
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - meeting-note
```

证据:

- path: wiki/adr/0006-formal-project-local-skills-over-drafts.md
- title: ADR-0006 Formal Project-Local Skills Over Draft Skill Docs
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 117. detail-0128 - `wiki/adr/0007-archive-review-before-archive.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: archive-review-before-archive
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0007-archive-review-before-archive.md
- title: ADR-0007 Archive Review Before Archive
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 118. detail-0129 - `wiki/adr/0008-human-governance-before-self-evolution-promotion.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: human-governance-before-self-evolution-promotion
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0008-human-governance-before-self-evolution-promotion.md
- title: ADR-0008 Human Governance Before Self-Evolution Promotion
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 119. detail-0130 - `wiki/adr/0009-explore-trace-before-openspec-explore.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: explore-trace-before-openspec-explore
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - explore-trace
```

证据:

- path: wiki/adr/0009-explore-trace-before-openspec-explore.md
- title: ADR-0009 Explore Trace Before OpenSpec Explore
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 120. detail-0131 - `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: shared-skill-authoring-contract-before-repo-local-overrides
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - skill-authoring-contract
```

证据:

- path: wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md
- title: ADR-0010 Shared Skill Authoring Contract Before Repo-Local Overrides
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 121. detail-0132 - `wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: canonical-ai-chat-installer-source-with-platform-adapters
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0011-canonical-ai-chat-installer-source-with-platform-adapters.md
- title: ADR-0011 Canonical AI Chat Installer Source With Platform Adapters
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 122. detail-0133 - `wiki/adr/0012-disagreement-management-before-conclusion-promotion.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: disagreement-management-before-conclusion-promotion
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - disagreement-management
```

证据:

- path: wiki/adr/0012-disagreement-management-before-conclusion-promotion.md
- title: ADR-0012 Disagreement Management Before Conclusion Promotion
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 123. detail-0134 - `wiki/adr/0013-agent-readable-wiki-naming-before-graph-growth.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-naming-before-graph-growth
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - conversation-handoff
  - disagreement-management
```

证据:

- path: wiki/adr/0013-agent-readable-wiki-naming-before-graph-growth.md
- title: ADR-0013 Agent-Readable Wiki Naming Before Graph Growth
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 124. detail-0135 - `wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-frontmatter-before-graph-automation
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - agent-readable-wiki-frontmatter
```

证据:

- path: wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md
- title: ADR-0014 Agent-Readable Wiki Frontmatter Before Graph Automation
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 125. detail-0136 - `wiki/adr/0015-agent-readable-wiki-graph-extraction-after-structure.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-graph-extraction-after-structure
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - wiki-graph-extraction
```

证据:

- path: wiki/adr/0015-agent-readable-wiki-graph-extraction-after-structure.md
- title: ADR-0015 Agent-Readable Wiki Graph Extraction After Structure
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 126. detail-0137 - `wiki/adr/0016-agent-readable-wiki-relation-analysis-after-extraction.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-relation-analysis-after-extraction
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - wiki-relation-analysis
```

证据:

- path: wiki/adr/0016-agent-readable-wiki-relation-analysis-after-extraction.md
- title: ADR-0016 Agent-Readable Wiki Relation Analysis After Extraction
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 127. detail-0138 - `wiki/adr/0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-semantic-scoring-after-relation-analysis
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - wiki-semantic-scoring
```

证据:

- path: wiki/adr/0017-agent-readable-wiki-semantic-scoring-after-relation-analysis.md
- title: ADR-0017 Agent-Readable Wiki Semantic Scoring After Relation Analysis
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 128. detail-0139 - `wiki/adr/0018-agent-readable-wiki-utilization-layer-after-semantic-scoring.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-utilization-layer-after-semantic-scoring
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - wiki-utilization-layer
```

证据:

- path: wiki/adr/0018-agent-readable-wiki-utilization-layer-after-semantic-scoring.md
- title: ADR-0018 Agent-Readable Wiki Utilization Layer After Semantic Scoring
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 129. detail-0140 - `wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: agent-readable-wiki-runtime-context-after-utilization
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - wiki-runtime-context
```

证据:

- path: wiki/adr/0019-agent-readable-wiki-runtime-context-after-utilization.md
- title: ADR-0019 Agent-Readable Wiki Runtime Context After Utilization
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 130. detail-0141 - `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-runtime-context-source-integration
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-context
formalizes:
  - wiki-runtime-context-source-integration
related_objects:
  - wiki-runtime-context
```

证据:

- path: wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md
- title: wiki-runtime-context-source-integration / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 131. detail-0142 - `wiki/adr/0021-agent-readable-wiki-runtime-auto-routing-after-source-integration.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-runtime-auto-routing
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-context-source-integration
formalizes:
  - wiki-runtime-auto-routing
related_objects:
  - wiki-runtime-context
  - wiki-runtime-context-source-integration
```

证据:

- path: wiki/adr/0021-agent-readable-wiki-runtime-auto-routing-after-source-integration.md
- title: wiki-runtime-auto-routing / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 132. detail-0143 - `wiki/adr/0022-agent-readable-wiki-context-injection-after-runtime-auto-routing.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-context-injection
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-auto-routing
formalizes:
  - wiki-context-injection
related_objects:
  - wiki-runtime-auto-routing
```

证据:

- path: wiki/adr/0022-agent-readable-wiki-context-injection-after-runtime-auto-routing.md
- title: wiki-context-injection / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 133. detail-0144 - `wiki/adr/0023-agent-readable-wiki-self-directed-execution-after-context-injection.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-self-directed-execution
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-context-injection
formalizes:
  - wiki-self-directed-execution
related_objects:
  - wiki-context-injection
```

证据:

- path: wiki/adr/0023-agent-readable-wiki-self-directed-execution-after-context-injection.md
- title: wiki-self-directed-execution / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 134. detail-0145 - `wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md`

- 风险原因: adr_risk, agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；包含 drift / retro / reanchor 等治理漂移信号；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, drift_risk, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: live-conversation-reanchor-gate
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - disagreement-management
formalizes:
  - live-conversation-reanchor-gate
related_objects:
  - disagreement-management
```

证据:

- path: wiki/adr/0024-live-conversation-reanchor-before-continued-implementation.md
- title: live-conversation-reanchor-gate / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 优先保留为 trace / retro 证据；除非人工确认要改变结构，否则不要把 drift 记录升级成规则或关系。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 135. detail-0146 - `wiki/adr/0025-readable-views-before-further-runtime-expansion.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-readable-views
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - live-conversation-reanchor-gate
formalizes:
  - wiki-readable-views
related_objects:
  - live-conversation-reanchor-gate
```

证据:

- path: wiki/adr/0025-readable-views-before-further-runtime-expansion.md
- title: wiki-readable-views / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 136. detail-0147 - `wiki/adr/0026-retire-draft-skills-as-runtime-surface.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: retire-draft-skills-as-runtime-surface
artifact_type: adr
```

候选关系:

```yaml
- 无
```

证据:

- path: wiki/adr/0026-retire-draft-skills-as-runtime-surface.md
- title: ADR-0026 Retire Draft Skills As Runtime Surface
- ADR pages use domain none

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。

### 137. detail-0148 - `wiki/adr/0027-repo-phase0-before-repo-agents-migration.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: repo-agents-governance-phase0
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - agents-governance-drift
formalizes:
  - repo-agents-governance-phase0
related_objects:
  - agents-governance-drift
```

证据:

- path: wiki/adr/0027-repo-phase0-before-repo-agents-migration.md
- title: repo-agents-governance-phase0 / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 138. detail-0149 - `wiki/adr/0028-root-agents-archive-review-generic-with-repo-detail.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: root-agents-archive-review-generic-with-repo-detail
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - root-governance-alignment
```

证据:

- path: wiki/adr/0028-root-agents-archive-review-generic-with-repo-detail.md
- title: ADR-0028 Root AGENTS Archive-Review Semantics Stay as Generic Top-Level Rules With Repo-Owned Detail
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 139. detail-0150 - `wiki/adr/0029-intake-retractions-legitimate-with-reopen-triggers.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: intake-retractions-legitimate-with-reopen-triggers
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - root-governance-alignment
```

证据:

- path: wiki/adr/0029-intake-retractions-legitimate-with-reopen-triggers.md
- title: ADR-0029 Intake Retractions Are Legitimate With Explicit Reopen Triggers
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 140. detail-0151 - `wiki/adr/0030-no-repo-local-commit-hook-default.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: no-repo-local-commit-hook-default
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - agents-governance-drift
  - repo-agents-governance-phase0
derived_from:
  - agents-governance-drift
formalizes:
  - no-repo-local-commit-hook-default
```

证据:

- path: wiki/adr/0030-no-repo-local-commit-hook-default.md
- title: no-repo-local-commit-hook-default / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 141. detail-0152 - `wiki/adr/0031-root-capability-extraction-boundary.md`

- 风险原因: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；分类或判断仍不确定，需要人工确认；涉及治理/行为变化，可能需要 OpenSpec 承接；关系候选证据不足，不能批量接受
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, agent_uncertain, openspec_required, relation_weak_evidence
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: root-capability-extraction
artifact_type: adr
```

候选关系:

```yaml
related_objects:
  - meeting-note
  - principle-skills-layer
  - repo-agents-loaded-context
  - root-governance-alignment
derived_from:
  - openspec/changes/archive/2026-05-07-decide-root-capability-extraction-boundary/
  - wiki/ops/root-capability-extraction-retro.md
formalizes:
  - root-capability-extraction
```

证据:

- path: wiki/adr/0031-root-capability-extraction-boundary.md
- title: root-capability-extraction / adr
- ADR pages use domain none
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- related_objects: `auto_accept_all_relations` - relation candidates need reviewed evidence

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。
- 需要人工确认分类；无法确认时保留 `unclassified` 或显式 uncertainty 字段。
- 逐条检查 suggested_relations 是否能从正文、frontmatter 或明确引用中证明；不要批量接受全部关系。

### 142. detail-0153 - `wiki/adr/0032-whole-wiki-frontmatter-gate-must-be-strict-and-scorecarded.md`

- 风险原因: adr_risk, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: whole-wiki-frontmatter-gate
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-frontmatter-model
  - stabilize-wiki-frontmatter-taxonomy
formalizes:
  - wiki-frontmatter-taxonomy-gate
related_objects:
  - visual-output-routing
  - wiki-frontmatter-model
  - wiki-runtime-context
  - wiki-runtime-context-source-integration
```

证据:

- path: wiki/adr/0032-whole-wiki-frontmatter-gate-must-be-strict-and-scorecarded.md
- title: ADR-0032 Whole Wiki Frontmatter Gate Must Be Strict And Scorecarded
- existing domain frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。

### 143. detail-0154 - `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`

- 风险原因: adr_risk, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: wiki-runtime-layer-boundary
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-layer-contract
  - wiki-react-decision-trace
  - brainstorming-drift-wiki-trace
formalizes:
  - wiki-runtime-layer-boundary
related_objects:
  - brainstorming-drift-wiki-trace
  - wiki-react-decision-trace
  - wiki-runtime-layer-contract
```

证据:

- path: wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md
- title: ADR-0033 Wiki React / Eval / Apply / OpenSpec 边界
- existing domain frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。

### 144. detail-0155 - `wiki/adr/0034-readme-capability-map-is-project-description.md`

- 风险原因: adr_risk, openspec_required
- 风险解释: 涉及 ADR 稳定决策页，需要按 ADR 语义复核；涉及治理/行为变化，可能需要 OpenSpec 承接
- 诊断状态: needs_user_confirmation
- 诊断原因: candidate has review risks: adr_risk, openspec_required
- 是否可直接应用 frontmatter: False
- package 建议动作: review_candidate_before_structure_write

候选 frontmatter:

```yaml
layer: adr
domain: none
canonical_object: readme-capability-map-boundary
artifact_type: adr
```

候选关系:

```yaml
derived_from:
  - wiki-runtime-layer-boundary
  - brainstorming-drift-wiki-trace
  - openspec/changes/document-readme-capability-map-boundary/design.md
formalizes:
  - readme-capability-map-boundary
related_objects:
  - brainstorming-drift-wiki-trace
  - wiki-runtime-layer-boundary
```

证据:

- path: wiki/adr/0034-readme-capability-map-is-project-description.md
- title: ADR-0034 README Capability Map Is Project Description
- existing domain frontmatter
- matched existing canonical objects in content/frontmatter

不自动应用的原因:

- 无

中文诊断建议:

- 先不要作为普通页面修复处理；判断这是否是治理或运行时行为变化，必要时新建或选择 OpenSpec。
- 按稳定决策页处理；先确认 ADR 的对象、决策边界和引用关系，再考虑 frontmatter。

## Eval Warnings

- detail-0001: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0002: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0003: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0004: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0007: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0008: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0009: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0010: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0012: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0013: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0015: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0016: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0017: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0018: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0019: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0020: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0021: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0022: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0024: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0025: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0026: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0028: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0031: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0032: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0034: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0039: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0040: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0041: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0042: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0043: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0044: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0045: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0046: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0047: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0048: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0049: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0052: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0053: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0055: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0057: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0058: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0059: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0060: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0061: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0062: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0063: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0064: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0066: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0067: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0068: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0069: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0071: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0073: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0074: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0075: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0076: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0077: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0078: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0079: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0080: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0081: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0082: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0083: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0084: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0085: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0086: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0087: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0088: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0089: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0091: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0092: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0093: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0094: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0095: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0096: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0097: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0098: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0099: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0100: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0101: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0103: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0105: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0106: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0107: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0114: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0115: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0119: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0120: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0121: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0124: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0127: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0130: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0131: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0133: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0134: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0135: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0136: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0137: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0138: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0139: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0140: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0141: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0142: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0143: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0144: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0145: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0146: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0148: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0149: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0150: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0151: relation candidate needs reviewed evidence（关系候选需要人工证据复核）
- detail-0152: relation candidate needs reviewed evidence（关系候选需要人工证据复核）

## Proof Boundary

- Content adjudication is deterministic review output only.
- It does not write frontmatter.
- It does not mutate taxonomy config.
- It does not prove hidden semantic truth.
- 本详细复核单仍然只是诊断记录，不是写入批准。
