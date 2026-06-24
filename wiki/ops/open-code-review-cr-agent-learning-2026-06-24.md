---
layer: ops
domain: agent-harness
ops_area: learning-capture
canonical_object: open-code-review-cr-agent-learning
artifact_type: repo-learning
status: active
created_at: 2026-06-24
updated_at: 2026-06-24
source_reference: https://github.com/alibaba/open-code-review
---

# Open Code Review 对 cr-agent 的学习记录

## 触发

用户询问 `https://github.com/alibaba/open-code-review` 是否使用 LangGraph，
以及它对本地 `cr-agent` 有什么帮助。

## Repo Admission

| 字段 | 结果 |
|---|---|
| Source access | 通过：读取 README、`go.mod`、`package.json`、源码包目录和关键 Go 文件 |
| Source class | official repo / implementation reference |
| Source artifact type | GitHub repo + README + source tree |
| Local objective | 判断技术栈，并评估对本地 CR agent 的可迁移价值 |
| Adaptation boundary | 只记录 candidate learning；不直接改 `cr-agent`、OpenSpec 或运行时规则 |

## Score

| 维度 | 分数 | 说明 |
|---|---:|---|
| Source access and provenance | 20/20 | 官方 GitHub repo，读取到 README、go.mod、package.json 和源码树 |
| Evidence or method density | 25/25 | 有 CLI、Go agent、diff、tool、rule、template、viewer、CI/skill/plugin 集成 |
| Local capability gain | 20/25 | 对 CR 工程化有明显启发，但本地 cr-agent 已有生命周期/gate 分层 |
| Transfer path | 13/15 | 可转为 CR evidence executor、preview/diff adapter、issue 定位能力候选 |
| Verification path | 12/15 | 可通过源码路径、命令、输出 JSON、规则匹配和 replay 对照验证 |
| Total | 90/100 | deep-read |

## 技术栈判断

Open Code Review 不是 LangGraph 项目。

依据：

- `go.mod` 显示主模块是 Go 1.25，依赖 `anthropic-sdk-go`、`openai-go/v3`、
  `tiktoken-go`、OpenTelemetry、Charm TUI 组件等。
- `package.json` 只是 npm 分发层，`ocr` 命令指向 `bin/ocr.js`，安装时拉取
  平台二进制。
- 核心代码在 `internal/agent`、`internal/diff`、`internal/tool`、
  `internal/config/rules`、`internal/config/template`、`internal/session`。
- 未发现 LangGraph / Python graph runtime 依赖；其“agent”是 Go 编排的
  LLM tool-use loop。

## 核心设计

README 的主线是 `Deterministic Engineering × Agent Hybrid`：

- 确定性工程层负责文件选择、过滤、规则匹配、diff 解析、分片并发、行号定位、
  session 持久化、viewer、遥测。
- Agent 层负责动态判断、读取上下文、搜索代码、跨文件确认、产出 review
  comments。
- 工具集是 code review 专用，不是通用 agent 工具箱：`file_read`、
  `file_find`、`file_read_diff`、`code_search`、`code_comment`、`task_done`。
- 每个文件作为子任务并发执行，大 diff 触发 plan phase，小 diff 可跳过 plan。
- 评论定位不是完全信任模型，而是用 `existing_code` 通过 diff hunk / 文件内容再定位。

## 对本地 cr-agent 的帮助

本地 `cr-agent` 当前优势是生命周期和 gate 边界清楚：

- `cr-intake` 归一化 CR 类型、范围、证据；
- `cr-diff` 产出 deterministic diff evidence；
- `cr-scope` 和 `cr-technical-review` 做范围与技术维度；
- `cr-evidence` 处理 Jira/test/UAT/rollback/impact；
- `cr-gate` 产出 allow / conditional / blocked；
- `cr-report` 只渲染中文报告，不重算 gate。

Open Code Review 对我们的补强点主要是工程化 executor，而不是替换现有
`cr-agent` 控制器：

1. `preview` 作为 review 前置能力：先输出哪些文件会 review、哪些被排除、
   排除原因、变更行数。
2. path rule / file type rule：把不同文件类型的 review 规则确定性匹配出来，
   减少 prompt 里泛泛而谈。
3. per-file 子任务并发：大 CR 不让一个模型上下文吞完整 diff。
4. dedicated toolset：CR agent 应有固定工具，不应暴露泛用 shell/grep 决策。
5. line relocation：模型给出的 `existing_code` 应被 deterministic resolver
   再定位，减少行号漂移。
6. session JSONL / viewer：保留每个文件的 LLM request/response/tool-call 轨迹，
   便于 CR 复盘和 replay。
7. review filter phase：对模型 comments 再做一次过滤，降低误报。
8. JSON output / agent audience：为上层 agent 提供稳定机器输出，而不是只给人类 UI。

## 代码质量能力

Open Code Review 有代码质量相关能力，而且是它最直接可复用的部分之一。
它不是只做 diff 工程化，也内置了一组按文件类型匹配的 review rules。

内置通用维度：

- correctness：逻辑正确性、边界条件、异常处理、并发线程安全；
- security：SQL injection、XSS、敏感信息、权限校验；
- performance：N+1 查询、循环内查询、大数据无分页、资源释放；
- maintainability：命名、可读性、架构风格、重复代码；
- test coverage：关键路径和边界条件测试覆盖。

语言 / 文件类型专项：

- Java：拼写、死代码、if 条件、边界检查、布尔表达式、NPE、switch
  fall-through、数据库循环查询、N+1、分页、线程安全；
- TypeScript / JavaScript / React：重复代码、注释、硬编码、`var`、
  `==`、`any`、空值检查、嵌套三元、Hooks、useEffect cleanup、render
  side effect、innerHTML / eval / sensitive data；
- MyBatis mapper / DAO XML：SQL 条件、JOIN 条件、动态 SQL、语法错误、
  全表扫描、大查询无分页、重复子查询、`${}` 注入风险；
- package / build / yaml / workflow / Rust / C / C++ 等也有独立规则文档。

这里对 `cr-agent` 的转化方式应该是：

- 把 OCR 的 code-quality output 接到 `cr-technical-review`；
- 每条 finding 进入 `cr-issues`，带 path、line、evidence、severity、rule
  category；
- 代码质量问题不能直接改写 `cr-gate`，除非命中本地 gate 的阻断条件，例如
  critical security、生产风险、缺少验证证据；
- 对低置信度、纯风格、上下文不足的问题，要保持 candidate / conditional，
  不要污染 release CR 结论。

## 不直接复用的部分

- 不把它当 LangGraph 或状态机框架学习。
- 不用它替代本地 `cr-gate` 的 release / branch / evidence 决策。
- 不直接采用它的 priority 规则为本地 gate 结论。
- 不把 OCR 的 code-quality review 扩展成我们的 release CR 完整语义。
- 不在没有 OpenSpec change 的情况下修改 `cr-agent` skill。

## Candidate Transfer

候选后续 change：

- 给 `cr-agent` 增加一个 `cr-ocr-executor` 或 `cr-code-review-executor`
  子能力，输入为 `cr-diff` 的 deterministic evidence，输出为 normalized
  `cr-issues`。
- 在 `cr-diff` 后增加 preview/coverage surface：文件是否 review、排除原因、
  文件类型、命中的规则。
- 为代码质量类 findings 增加 line relocation：issue 必须有 path、line 或
  定位失败原因。
- 对 OCR 输出只作为 `cr-technical-review` 的 evidence，不允许绕过
  `cr-issues` 和 `cr-gate`。

## Status

Candidate learning captured. No repo behavior change has been made from this
source.
