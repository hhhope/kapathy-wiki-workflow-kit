# AI Chat Workflow Installer

这页定义项目级 AI workflow 的跨运行面安装模型。它不是某一个平台专用说明，也不是一个“万能 skill 文件”，而是仓库内的统一真源说明。

## 目标

- 把当前仓库里的治理、workflow skill 和 wiki 组织方式，整理成可安装的统一模型
- 支持至少三类目标运行面：Codex、Cursor、Claude
- 保留跨平台共享语义，同时承认平台入口差异
- 给分享、交接和后续自动化提供稳定基线

## 非目标

- 不承诺三端使用字节级相同的文件
- 不把仓库 workflow 降级成一个大 prompt
- 不把 repo-local skills 当成唯一可移植产物
- 不在没有平台适配的情况下宣称“已经一键安装”

## 三层模型

```text
canonical workflow source
    ├─ governance boundary
    ├─ workflow units
    ├─ adapter mapping rules
    └─ validation checklist
            ↓
       installer workflow
            ├─ codex adapter output
            ├─ cursor adapter output
            ├─ claude adapter output
            └─ share artifact
```

## Canonical Workflow Source

这是安装器的唯一语义真源，负责定义：

- 治理边界
- workflow 单元
- 适配规则
- 验证要求

### 1. 治理边界

核心输入来自：

- `AGENTS.md`
- `wiki/adr/`
- `openspec/`

这层决定：

- 什么属于 repo 默认行为
- 什么变化必须先走 OpenSpec
- 什么是稳定决策，什么只是当前 change 范围

### 2. Workflow Units

核心输入来自：

- `.codex/skills/material-collaboration-defaults/SKILL.md`
- `.codex/skills/meeting-note-output/SKILL.md`
- `.codex/skills/clarify-before-acting/SKILL.md`
- `.codex/skills/simplicity-first/SKILL.md`
- `.codex/skills/surgical-changes/SKILL.md`
- `.codex/skills/verify-before-claiming/SKILL.md`
- `wiki/ai-workflow.md`

这层决定：

- 哪些 workflow 可以复用
- 哪些原则是高频纠偏
- workflow 如何连接到 wiki 的 source / ops / report 结构

### 3. Adapter Mapping Rules

这层决定：

- 哪些语义必须跨平台保留
- 哪些内容需要按平台改写承载面
- 哪些能力在某个平台只能降级表达

### 4. Validation Checklist

这层决定：

- 安装后如何检查入口文件是否存在
- 是否能看见 repo workflow 的核心边界
- 是否能识别三端都必须保留的 cross-platform invariants

## Canonical Inputs Vs Adapter Outputs

| Category | Canonical Input | Adapter Output |
|----------|-----------------|----------------|
| Governance | `AGENTS.md`, `wiki/adr/`, `openspec/` | 平台可消费的治理入口 |
| Workflow units | repo-local `SKILL.md` and linked wiki guidance | 平台可消费的 workflow routing / command / rule text |
| Examples and reports | `wiki/` pages | 分享文档、演示文案、安装说明 |
| Validation | change verification and checklists | 安装后检查步骤 |

规则：

- canonical input 只在仓库里维护
- adapter output 可以重排、裁剪、转写
- adapter output 不能悄悄引入 canonical source 里没有的新行为

## Platform Adapters

### Codex Adapter

主承载面：

- `AGENTS.md`
- repo-local `.codex/skills/`

要求：

- 保留 repo 默认治理边界
- 说明 repo-local workflow skill 如何被路由
- 明确 OpenSpec、ADR、wiki 的角色分层

最小输出形态：

- repo instruction entry
- workflow skill availability note
- installation verification checklist

### Cursor Adapter

主承载面：

- `.cursor/rules/`
- 必要时引用 `AGENTS.md` 的兼容入口

要求：

- 把治理和 workflow 语义拆成 Cursor 可消费的规则面
- 不能假装 Cursor 原生理解 repo-local Codex skill 目录
- 需要显式声明哪些能力是映射结果，哪些不是原生能力

最小输出形态：

- rules file set
- rule-to-workflow mapping note
- installation verification checklist

### Claude Adapter

主承载面：

- `CLAUDE.md`
- command / memory entry surfaces

要求：

- 把 repo workflow 语义转成 Claude 可用的记忆和命令结构
- 不能简单复制 Codex skill 目录作为 Claude 运行时
- 要明确哪些 workflow 通过命令触发，哪些通过长期记忆触发

最小输出形态：

- Claude memory entry
- workflow command mapping note
- installation verification checklist

## Cross-Platform Invariants

所有 adapter 都必须保留：

- repo 有一套高于单次 prompt 的治理边界
- workflow 默认行为来自仓库真源，而不是聊天历史
- OpenSpec 负责 change 生命周期，不被安装器绕开
- 稳定决策进入 `wiki/adr/`
- workflow skill 和 principle skill 是可复用能力层，不等于全部运行时入口
- 分享物必须讲清差异和边界，不能把三端包装成完全一致

## One-Click Installation Flow

```text
select repository
    ↓
read canonical workflow source
    ↓
select target runtimes
    ↓
render adapter outputs
    ↓
write target files
    ↓
run install verification
    ↓
generate share artifact
```

### Expected Inputs

- repo path
- target runtimes
- desired installation mode
- optional share output request

### Installation Boundary

workflow content 负责回答“要安装什么语义”。

platform mechanics 负责回答“目标平台怎么落文件、命令、规则入口”。

两者必须分离：

- workflow content 不直接依赖某个平台的目录约定
- platform mechanics 不得更改 canonical workflow 语义

## Validation Checklist

每个目标至少验证：

1. 目标入口文件已经生成
2. 仓库治理边界被明确表达
3. workflow 单元能被目标平台识别到合适入口
4. OpenSpec / ADR / wiki 分层没有丢失
5. adapter 没有宣称自己原生支持仓库并不存在的能力

## Failure Handling

当某个平台无法承接完整 workflow surface 时：

- 保留 canonical source 不变
- 在 adapter 中显式标注降级部分
- 生成安装失败或降级说明
- 不得把缺失能力静默视为“已经安装成功”

## Share Boundary

飞书分享物属于安装器的正式输出之一，但不是 canonical source 本身。

它负责：

- 说明为什么要做
- 解释三端差异
- 说明边界和非目标
- 帮助团队理解怎么安装和怎么验证

它不负责：

- 取代 repo 真源
- 取代 OpenSpec change
- 作为运行时规则主文件
