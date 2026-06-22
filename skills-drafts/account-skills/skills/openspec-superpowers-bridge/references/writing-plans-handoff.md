# writing-plans 交接契约

## 输入（唯一 OpenSpec 入口）

`openspec/changes/.../<change>/planning-brief-for-superpowers.md`

禁止在 writing-plans 阶段直接拼凑原始 `spec.md`，除非尚未生成 brief（应先跑桥接 skill）。

## 从 brief 映射到 writing-plans 文档头

| brief 章节 | writing-plans 字段 |
|------------|-------------------|
| §1 Proposal（Why / Goal） | **Goal** |
| §2 Scope | **Architecture** 范围；non-goals |
| §3 Decisions | **Architecture** |
| §4 R* / S* | 每个 R* → `### Task N`；每个 S* → 测试/验证步 |
| §5 OpenSpec T* | 分解为多个 2–5 分钟 TDD 步，禁止整段复制 |
| §6 Traceability | 计划末尾 R* ↔ Task N 自检 |

## 计划输出

- 路径：`docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`
- 文首 **Related OpenSpec**：change 目录 + brief 路径 + `proposal.md` 链接

## writing-plans 完成之后 → 实现（非 apply）

1. brief §9 + writing-plans self-review。
2. 向用户选择执行方式（subagent-driven / inline）。
3. **必须**进入 Superpowers 实现链：
   - `superpowers:test-driven-development`
   - `superpowers:executing-plans` 或 `superpowers:subagent-driven-development`
4. **禁止**使用 `/opsx:apply` 作为实现驱动。
5. 实现进度：勾选 **本计划文件** 的 checkbox；OpenSpec `tasks.md` 仅在里程碑完成时**可选**同步。

## 常见误解

| 误解 | 正确 |
|------|------|
| OpenSpec task = 一个 coding 步骤 | 一个 T* → 多个 TDD 微步 + 多次 commit |
| tasks.md 勾选 = 日常进度 | 计划 checkbox = 日常进度 |
| apply 与 TDD 二选一都行 | 本工作流 **只用 TDD 链** |
| 读完 proposal 就够 | 还须 brief 中扁平化 R*/S* 与验收边界 |
