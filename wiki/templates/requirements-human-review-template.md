---
title: <Requirement Human Review Title>
type: requirements-human-review
language: zh-CN
audience: product-review
knowledge_level: working
layer: examples
domain: report-workflow
classification_needed: false
status: draft
case_slug: <case-slug>
source_case: <requirements-case-file.md>
created_at: YYYY-MM-DD
ai_generated: true
---

# <需求名称>需求分析

## Case 身份

| 字段 | 内容 |
| --- | --- |
| case_slug | `<case-slug>` |
| source_case | `<requirements-case-file.md>` |
| 来源材料 | `<source-path-or-chat-reference>` |
| 当前状态 | `<checker-status>` |
| checker 结果 | `<requirements-ready / blocked / detailed-design-gate>` |

## 一句话结论

说明需求是否可进入人工评审、是否可 handoff、详细设计是否 blocked。

## 源材料复核

| 原始材料点 | 复核判断 | 当前文档位置/映射 |
| --- | --- | --- |
| `<source-point>` | `<covered / corrected / gap / out-of-scope>` | `<US/AC/section>` |

## 领域判断

| 判断项 | 结论 | 理由 |
| --- | --- | --- |
| 主域 | `<domain>` | `<reason>` |
| 关联域 | `<domain>` | `<reason>` |
| 明确排除域 | `<domain>` | `<reason>` |

## 范围边界

### 首版范围

- `<in-scope-item>`

### 不在首版范围

- `<out-of-scope-item>`

### 存量/一次性事项

- `<one-time-boundary>`

## 角色与责任

| 角色 | 关注点 | 责任边界 |
| --- | --- | --- |
| `<role>` | `<concern>` | `<boundary>` |

## 用户故事

| ID | 角色 | 用户故事 | 业务价值 | 对应验收 | 来源依据 |
| --- | --- | --- | --- | --- | --- |
| US-001 | `<role>` | `<as a role, I want...>` | `<benefit>` | AC-001 | `<source>` |

## 用户故事与场景复核结论

- 用户故事是否充分：
- 场景覆盖是否充分：
- 必须同步机器 case 的需求事实：
- 仅作为人工评审提示的问题：

## 场景覆盖矩阵

| 场景 ID | 场景 | 触发条件 | 期望结果 | 关联用户故事 | 验收映射/判断 |
| --- | --- | --- | --- | --- | --- |
| S-001 | `<scenario>` | `<trigger>` | `<expected-result>` | US-001 | AC-001 |

## 规则/状态矩阵

| 状态/规则 | 进入条件 | 退出条件 | 页面/后台展示 | 后台操作 | 是否阻断流程 | 复核判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `<state>` | `<enter>` | `<exit>` | `<display>` | `<operation>` | `<yes/no>` | `<judgment>` |

## 验收范围

### 首版必须验收

| ID | 验收点 | 可观察结果 | 来源依据 |
| --- | --- | --- | --- |
| AC-001 | `<acceptance-name>` | `<observable-result>` | `<source>` |

### 反向边界验收

| ID | 验收点 | 可观察结果 | 来源依据 |
| --- | --- | --- | --- |
| AC-XXX | `<negative-boundary>` | `<observable-result>` | `<source>` |

### 不在首版验收

- `<not-in-first-release>`

## 缺口分类

| 缺口 | 分类 | 是否必须同步机器 case | 处理方式 |
| --- | --- | --- | --- |
| `<gap>` | `demand_fact / review_prompt / design_gate_gap` | `<yes/no>` | `<action>` |

## 详细设计门禁

| 门禁 | 当前状态 | 缺失材料 | 是否阻断详细设计 |
| --- | --- | --- | --- |
| current_state_material_package | `<status>` | `<material>` | `<yes/no>` |
| business_rule_position_table | `<status>` | `<material>` | `<yes/no>` |
| system_boundary_contract_table | `<status>` | `<material>` | `<yes/no>` |

## 同步证明

| 项目 | 结果 | 证据 |
| --- | --- | --- |
| Human Review demand facts 已同步机器 case | `<yes/no>` | `<US/AC/domain/scope references>` |
| checker 已运行 | `<yes/no>` | `<command/result>` |
| frontmatter 预检已运行 | `<yes/no>` | `<command/result>` |

## Agent 使用方式

### 事实源顺序

1. 机器事实源：`<source_case>`
2. 人读评审视图：本文档
3. 需求 taxonomy：`requirements/config/requirements-taxonomy.yaml`
4. checker：`scripts/check_requirements_case.py`

### 允许动作

- 根据人工评审意见同步更新机器 case 和本文档。
- 将已确认的 `demand_fact` 写回机器 case。
- 在同步后运行 checker。

### 禁止动作

- 不要把本文档当作机器事实源。
- 不要只改本文档而不改机器 case。
- 不要在详细设计门禁未通过时生成 API、DDL、状态机或工程拆解。

## 下一步

- `<next-action>`
