# Chinese CR Report Template

Use this as the default human-facing report structure. Keep the report concise
enough for a reviewer to decide in the first screen, while preserving audit
evidence later in the document.

```markdown
# 代码评审报告 — {project} {YYYY-MM-DD}

## 最终结论（是否可发布）
- 一句话结论：**{代码合入/保留结论；发布/开关结论；下一步。}**
- 结论矩阵：

| 决策项 | 结论 | 原因 |
|---|---|---|
| 代码合入状态 | {可合入/可保留/阻塞} | {一句话原因} |
| 生产开关 / 发布动作 | {允许/阻塞/暂缓} | {证据是否闭环} |
| 宣称发布完成 | {允许/阻塞/暂缓} | {测试、UAT、回滚、监控是否满足} |
| 后续联调 / 预发验证 | {允许/不允许} | {边界条件} |

- 严重级别统计：严重={n}，高={n}，中={n}，低={n}，信息={n}
- 关键判断：{本次 CR 的真正风险类型，避免读者误解结论边界。}

## 必须补齐的阻塞项
| 阻塞项 | 责任人 | 最晚完成时间 | 完成标准 |
|---|---|---|---|
| {阻塞项 1} | {owner} | {时间点} | {可验证完成标准} |

## 变更基本信息
- 项目：{project}
- 评审类型：{merge_cr/release_cr/hotfix_cr/db_cr/config_cr}
- 评审分支：`{source_ref}`
- 目标分支：`{target_ref}`
- 评审范围：`{base}..{head}`
- 评审人：Codex / Account CR Agent
- 最新提交（HEAD）：`{head_sha} {subject}`
- HEAD 提交人：{name} `<{email}>`
- 变更规模：{diffstat}
- 非合并提交数：{n}
- merge-base：`{merge_base}` / {特殊说明}

本次变更集中在：
- {业务变化 1}
- {业务变化 2}
- {技术变化 1}
- {测试/文档边界说明}

## 评分卡（100分）
### 技术质量评分
- 正确性/业务逻辑（30）：{score}
- 稳定性/异常处理（20）：{score}
- 安全性/合规（15）：{score}
- 可测试性/验证证据（15）：{score}
- 可维护性（10）：{score}
- 可观测性（10）：{score}
- 总分：{score}

#### 技术质量评分扣分依据
每个技术质量分项都必须说明扣分依据；不能只给分。扣分依据必须关联 CR-ID、文件/命令证据，或说明该维度不适用。

| 评分项 | 得分 | 扣分依据 | 对应证据 / CR-ID |
|---|---:|---|---|
| 正确性/业务逻辑（30） | {score} | {业务语义、状态、边界、兼容性扣分说明} | {CR-ID / evidence} |
| 稳定性/异常处理（20） | {score} | {异常、重试、幂等、并发、降级、部分失败扣分说明} | {CR-ID / evidence} |
| 安全性/合规（15） | {score} | {鉴权、敏感信息、密钥、注入、合规扣分说明} | {CR-ID / evidence} |
| 可测试性/验证证据（15） | {score} | {单测、集成、UAT、回归、覆盖率、失败路径证据扣分说明} | {CR-ID / evidence} |
| 可维护性（10） | {score} | {变更规模、owner、模块边界、复杂度 / 重复 / 死代码 / 耦合、配置/profile 隔离、回滚/拆分性、文档/runbook 扣分说明} | {CR-ID / evidence} |
| 可观测性（10） | {score} | {logs / metrics / traces、dashboard、实时告警 / 报表或批处理告警、SLI/SLO 或业务 KPI、correlation id、脱敏、owner、threshold、routing、runbook 扣分说明} | {CR-ID / evidence} |

### CR 执行审计评分
- 范围和基线可信度（20）：{score}
- diff 证据完整性（15）：{score}
- 触发维度覆盖（15）：{score}
- 技术审查深度（20）：{score}
- 交付证据审查（15）：{score}
- gate / issue trace 一致性（15）：{score}
- 总分：{score}

## CR 执行审计
| Worker / Skill | 是否适用 | 是否执行 | 产出证据 | 缺口 / 风险 |
|---|---|---|---|---|
| cr-intake | {Y/N} | {Y/N} | {CR type, range, output mode} | {缺口} |
| cr-branch-governance | {Y/N} | {Y/N} | {branch, baseline, merge-base, trust checks} | {缺口} |
| cr-diff | {Y/N} | {Y/N} | {commit list, files, numstat, high-risk paths} | {缺口} |
| cr-scope | {Y/N} | {Y/N} | {triggered dimensions and reviewers} | {缺口} |
| cr-technical-review | {Y/N} | {Y/N} | {findings by dimension} | {缺口} |
| cr-evidence | {Y/N} | {Y/N} | {test/UAT/rollback/config evidence} | {缺口} |
| cr-issues | {Y/N} | {Y/N} | {normalized CR IDs and statuses} | {缺口} |
| cr-gate | {Y/N} | {Y/N} | {allow/conditional/blocked and reasons} | {缺口} |
| cr-report | Y | Y | {report path} | {template/reference gaps} |

## 分支治理结果
- 远端刷新：{成功/失败及原因}
- 分支关系：{ahead/behind/已合入/不能使用三点 diff 的原因}
- 静态合并检查：{结果}
- whitespace 检查：{结果}
- 工作区边界：{是否干净；如不干净，说明本报告是否只基于提交对象}
- 风险：{分支治理风险}

## 技术审查结果
### 高优先级问题（严重/高）
1) [高][{project}-CR-{YYYYMMDD}-001][{类别}] {标题}
   - 证据：
     - `{file}:{line}` {证据描述}
   - 影响：{业务/资金/安全/稳定性影响}
   - 必须动作：{必须修复或必须补证的动作}
   - 阻塞发布：Y

### 中优先级问题
2) [中][{project}-CR-{YYYYMMDD}-002][{类别}] {标题}
   - 证据：`{file}:{line}` {证据描述}
   - 影响：{影响}
   - 必须动作：{动作}
   - 阻塞发布：{Y/N，说明阻塞的是代码合入、生产开关还是发布完成}

### 低优先级问题 / 坏味道 / Sonar 类问题
3) [低][{project}-CR-{YYYYMMDD}-003][{类别}] {标题}
   - 证据：`{file}:{line}` {证据描述}
   - 影响：{影响}
   - 建议动作：{动作}
   - 阻塞发布：N

### 信息项 / 证据缺口
4) [信息][{project}-CR-{YYYYMMDD}-004][{类别}] {标题}
   - 命令/证据：`{command}` / `{artifact}`
   - 结果：{结果}
   - 影响：{证明边界}

## 技术债登记（重点）
| 债务编号 | 类型 | 影响/风险 | 工作量 | 责任人 | 截止日期 | 优先级 | 阻塞 |
|---|---|---|---|---|---|---|---|
| {project}-TD-{YYYYMMDD}-001 | {类型} | {风险} | {S/M/L} | {owner} | {date} | {P0/P1/P2} | {Y/N} |

## TODO 跟踪
| TODO 编号 | 来源 | 行动项 | 责任人 | 截止日期 | 工时 | 优先级 | 状态 | 阻塞 |
|---|---|---|---|---|---|---|---|---|
| {project}-TODO-{YYYYMMDD}-001 | CR-001 | {可执行动作} | {owner} | {date} | {estimate} | {P0/P1/P2} | 待处理 | {Y/N} |

## 测试证据
- 单元测试：{通过/缺失/未执行及原因}
- 集成测试：{通过/缺失/未执行及原因}
- UAT/预发：{通过/缺失/未执行及原因}
- Sonar：{通过/失败/未执行及原因}
- 安全扫描：{通过/失败/未执行及原因}
- 本地命令：
  - `{command}`：{result}

## 发布风险与回滚
- 风险等级：{低/中/高}
- 关键风险点：
  - {风险 1}
  - {风险 2}
- 回滚方案要求：
  - {回滚动作 1}
  - {回滚动作 2}
  - {补偿/清理/重放/核对要求}

## 处置项
- 发布/开关前必须完成（阻塞）：
  - {阻塞处置 1}
  - {阻塞处置 2}
- 可延期（需 owner/日期）：
  - {延期项 1}
  - {延期项 2}

## 附录：Issue Registry（可选）
Only include this appendix when a raw registry helps auditability. Do not put it
before the final conclusion.
```
