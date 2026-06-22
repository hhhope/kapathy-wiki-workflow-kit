---
name: cr-dated-output
description: 执行代码评审（CR）并按中文统一模板输出，包含门禁结论、评分卡、技术债、TODO，写入 cr/YYYY-MM-DD.md。用户提到 CR、代码评审、review、代码走查时使用。
tags:
  - CR
  - 代码评审
  - 门禁
  - Obsidian
related:
  - [[checkpoints/common|通用检查点]]
  - [[checkpoints/exception|Exception 检查点]]
  - [[checkpoints/api-migration|接口迁移检查点]]
---

> [!tip] 本 skill 输出 Obsidian 兼容格式
> 生成的 CR 文档支持双链、标签、嵌入等 Obsidian 特性，方便在 Obsidian 中建立知识关联。

# 强制约束

## CR Agent Role

When `cr-agent` is available, this skill is the first `cr-technical-review` and
`cr-report` provider. It does not own CR lifecycle state, branch governance, or
final gate decisions. Technical findings must be normalized into the CR issue
registry before the final gate is claimed.

**禁止直接写文件**。所有CR操作必须通过 `Skill` 工具调用本skill执行，不得手动创建或编辑CR文件。

**信息缺失时必须澄清**。当检查过程中发现上下文不足，无法判断是否符合规范时，必须向用户确认，不得凭猜测执行。

---

## 检查点扩展机制

cr-dated-output 采用插件式检查点，框架固定，各领域检查点独立维护。

## 目录结构

```
cr-dated-output/
├── SKILL.md
└── checkpoints/
    ├── [[checkpoints/common|common.md]]              # 通用检查点（6维度）
    ├── [[checkpoints/exception|exception.md]]       # Exception 领域检查点
    └── [[checkpoints/api-migration|api-migration.md]] # 接口迁移检查点
```

> [!info] 检查点扩展机制
> cr-dated-output 采用插件式检查点，框架固定，各领域检查点独立维护。新增领域只需在 `checkpoints/` 目录添加 `{领域}.md` 文件即可自动识别。

## 执行流程

1. **确定 Project 标识**
2. **创建输出目录**
3. **扫描代码变更范围**
4. **自动匹配检查点**
   - 读取代码变更的文件路径
   - 根据触发条件匹配检查点文件（如 exception/**/*.java → exception.md）
   - 加载匹配的检查点配置
5. **执行检查**
   - 通用检查点（always）
   - 领域检查点（按匹配触发）
6. **输出报告**

## 检查点文件格式

```markdown
# {领域名} 检查点

触发条件：{匹配规则，如 exception/**/*.java}

## 检查点

| ID | 检查项 | 规则 | 严重级别 |
|----|--------|------|----------|
| E001 | 检查项名 | 规则描述 | 高/中/低 |
```

## 添加新检查点

1. 在 `cr-checkpoints/` 创建 `{领域}.md`
2. 定义触发条件和检查点表格
3. cr-dated-output 自动识别

---

# 代码评审落盘模板（中文统一）

当用户提出 **代码评审（CR）** 时：

1. **确定 Project 标识**
   - 从当前工作目录或 git remote 获取项目名
   - 如 account-asl、order-bc 等

2. **创建输出目录**
   - 确保项目根目录存在 `cr/`（不存在则创建）
   - 子目录按 project 分离：`cr/{project}/`

3. **按 Project + 日期命名文件**
   - 文件名使用 `cr/{project}/YYYY-MM-DD.md`（如 `cr/account-asl/2026-03-16.md`）
   - 同 Project 同日多次 CR 时自动追加分隔段

3. **执行评审并给出门禁结论**
   - 从正确性、稳定性、安全性、可测试性、可维护性、可观测性六个维度评审。
   - 按严重级别统计：严重 / 高 / 中 / 低。
   - 按门禁规则决策：
     - 任一严重问题 => 不允许发布（打回重做）
     - 高风险问题 >= 2 => 不允许发布（打回重做）
     - 高风险问题 = 1 且缺回归证据 => 不允许发布（打回重做）
     - 核心变更覆盖率 < 80% => 不得评为“允许发布”
     - 中风险问题 > 5 => 至少“有条件发布”
   - 结论统一为中文：`允许发布` / `有条件发布` / `不允许发布（打回重做）`

4. **生成评分卡（100分）**
   - 正确性/业务逻辑：30
   - 稳定性/异常处理：20
   - 安全性/合规：15
   - 可测试性/验证证据：15
   - 可维护性：10
   - 可观测性：10
   - 评分建议：
     - `>= 85`：允许发布候选
     - `70-84`：有条件发布候选
     - `< 70`：不允许发布候选

5. **写入结构化报告到 `cr/{project}/YYYY-MM-DD.md`**
   - 必须使用下方中文模板。
   - 同 Project 同日重复评审时默认追加分隔段；若用户要求覆盖则覆盖。
   - 报告正文、标题、字段名必须中文（代码标识符除外）。

6. **同步 TODO 台账**
   - 将本次未关闭 TODO 同步到 `cr/{project}/TODO_BACKLOG.md`。
   - 每个 TODO-ID = {project}-{日期}-{序号}，如 account-asl-20260316-001
   - 包含：责任人、截止日期、预计工时、优先级

7. **自动匹配检查点**
   - 扫描代码变更的文件路径
   - 根据触发条件自动匹配检查点文件
   - 从 `cr-checkpoints/` 目录读取对应的检查点配置
   - 匹配规则：
     - `exception/**/*.java` → 加载 `exception.md`
     - 接口迁移相关 → 加载 `api-migration.md`
     - 其他 → 只用 `common.md`

8. **向用户确认**
   - 明确告知已写入 `cr/{project}/YYYY-MM-DD.md`
   - 询问时间需求：预计修复时间、优先级

## 报告模板（强制）

> 标签：`#CR` `#代码评审` `#门禁`

```markdown
---
title: 代码评审报告 — {project} YYYY-MM-DD
tags: [CR, 代码评审, {project}]
related:
  - [[checkpoints/common|通用检查点]]
---

# 代码评审报告 — {project} YYYY-MM-DD

> [!tip] 本报告可关联到 [[README|项目 CR 索引页]]

## 变更基本信息
- 项目：{project}
- 评审范围：
- 评审人：
- 分支：
- 最新提交（HEAD）：
- HEAD 提交人：
- HEAD 提交文件数：
- 最新非合并提交：
- 非合并提交人：
- 非合并提交文件数：

## 最终结论（是否可发布）
- 结论：允许发布 | 有条件发布 | 不允许发布（打回重做）
- 严重级别统计：严重=X，高=Y，中=Z，低=W
- 结论依据：

## 评分卡（100分）
- 正确性/业务逻辑（30）：
- 稳定性/异常处理（20）：
- 安全性/合规（15）：
- 可测试性/验证证据（15）：
- 可维护性（10）：
- 可观测性（10）：
- 总分：

## 高优先级问题（严重/高）
1) [严重级别] 问题标题（中文）
   - 现象：
   - 原因：
   - 影响：
   - 修复建议：
   - 预计工时：
   - 优先级：P0 | P1 | P2

## 本次新增逻辑问题
1) [严重级别] 问题标题（中文）
   - 现象：
   - 原因：
   - 影响：
   - 修复建议：
   - 预计工时：
   - 优先级：P0 | P1 | P2

## 技术债登记（重点）
1) 债务编号：{project}-TD-YYYYMMDD-XXX
   - 类型：架构 | 代码 | 测试 | 运维 | 文档
   - 影响/风险：
   - 工作量：S(0.5d) | M(1-2d) | L(3d+)
   - 责任人：
   - 截止日期：
   - 优先级：P0 | P1 | P2
   - 是否阻塞发布：Y | N

## TODO 跟踪

> [!todo] TODO 统一写入 [[TODO_BACKLOG|TODO 台账]]
> 所有 TODO 需同步写入 `cr/{project}/TODO_BACKLOG.md`，便于追踪和管理。

1) TODO 编号：`{project}-TODO-YYYYMMDD-XXX`
   - 来源：问题编号 | 债务编号
   - 行动项：
   - 责任人：
   - 截止日期：
   - 预计工时：
   - 优先级：P0 | P1 | P2
   - 状态：待处理 | 进行中 | 已完成
   - 是否阻塞发布：Y | N

## 测试证据
- 单元测试：
- 集成测试：
- 回归测试：
- 证据缺口：

## 发布风险与回滚
- 风险等级：低 | 中 | 高
- 关键风险点：
- 回滚方案：

## 处置项
- 合并前必须完成（阻塞）：
- 可延期（需 owner/日期）：
```

不得省略必填章节。若证据缺失，统一标记为“缺失”。
