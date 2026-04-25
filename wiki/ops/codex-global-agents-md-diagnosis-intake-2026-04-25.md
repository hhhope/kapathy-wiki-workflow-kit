---
title: ~/.codex/AGENTS.md 全局文件诊断
type: intake
canonical_object: codex-global-agents-md
artifact_type: intake
language: zh-CN
audience: self
domain: personal-ops
period: evergreen
confidence: high
status: active
updated_at: 2026-04-25
ai_generated: true
source_path: /home/yan/.codex/AGENTS.md
source_type: global-agent-config
related_objects:
  - agents-governance-drift
  - agent-governance-gate-gap
derived_from: []
notes_scope: 对 ~/.codex/AGENTS.md（281 行，用户全局 Codex 配置）的一次诊断 + 外部参考对标。非 repo AGENTS.md 诊断；与 agents-governance-drift 同根但作用对象不同。仅记录，不作决定。
---

# ~/.codex/AGENTS.md 全局文件诊断

## 0. 本文件定位

- 对象：`/home/yan/.codex/AGENTS.md`（用户全局 Codex 配置，当前 281 行）
- 不是：repo 根 `AGENTS.md`（那份由 repo Phase 0 / Phase 1 治理管）
- 场合：本次对话中 yan 让我"看下根目录 agents.md"——先理解成 repo 根，后确认是 home 根（`~/.codex/`）
- 性质：一次性诊断记录 + 外部参考对照。仅作 `intake` 落盘；不改文件，不起 OpenSpec change，不作决定

本次仅捕获：trigger 问题、当前 focus、当前 hypothesis、open questions、next step。

---

## 1. Trigger 问题

> "帮我看下根目录的 agents.md 有什么问题"

（home 根，非 repo 根）

## 2. Current focus

- `~/.codex/AGENTS.md` 是否还在可维护状态
- 它与 `~/.claude/CLAUDE.md` 的跨 agent 一致性
- 它与 official `agents.md` spec / GitHub 2500-repo 研究 / skyzyx "instruction budget" 的差距

---

## 3. 外部参考源摘要（验证过）

| 参考 | 核心信号 |
|------|---------|
| official `agents.md` spec | 设计对象是 repo 级；precedence 近者赢；常见 section = project overview / build-test / code style / testing / security / commits |
| GitHub "2500 repo 研究" | 优秀示例约 60 行；必备 section = executable commands / project structure / 代码示例 / git workflow / 三层边界 |
| skyzyx gist | LLM 能稳定遵守约 150–200 条指令；头号陷阱 = accretion over time；推荐 progressive disclosure |
| danielrosehill 模板仓库 | 4 类模板全是 repo-level，**社区无 global 模板** |
| openai/codex 自身 AGENTS.md | 213 行，纯 Rust 技术约定，无 meta-workflow |
| `~/.claude/CLAUDE.md`（同机对照物） | 两份全局文件存在 9 处跨 agent 不对称 |

---

## 4. 当前诊断 hypothesis

### 4.1 量化基准

| 指标 | 现状 | 外部参考 | 判断 |
|------|------|---------|------|
| 行数 | 281 | 优秀示例 ~60；预算 ~150–200；openai repo 213 | 超预算 40–360% |
| 核心内容 | 个人 workflow 偏好 | 可执行技术约定 | 类型错位 |
| git 纪律重复段 | 3 处 | canonical 单源 | 反模式 |
| 含 repo-specific policy | 是（OpenSpec archive-review 细节） | spec "近者赢" 禁止 | 违反 precedence |
| 3 周变化 | +22% 行数 | accretion 是头号坑 | 正在堆积 |
| 生态形态 | personal global | 社区模板无此类 | 罕见形态 |

### 4.2 Critical 问题（实际矛盾）

- **C1** team-lore 路径 + 数据模型双重分叉：Codex 侧 `/mnt/d/team-lore/wiki`（目录）vs Claude 侧 `~/team-lore/LORE.md`（flat 文件）。跨 agent 各走各路
- **C2** 全局文件装了 repo policy（line 115–127 OpenSpec boundary 含 archive-review 细节）。自违反 line 280 的 "repo semantics 归 repo" 声明
- **C3** 硬编码 WSL 绝对路径（`/mnt/d/team-lore/wiki`）

### 4.3 Substantive 问题（设计张力）

- **S1** REQ identification 在 OpenSpec 为 default 的前提下成死代码
- **S2** "active OpenSpec change"（line 61）vs "approved OpenSpec change"（line 108）前后不一
- **S3** 三段 git 纪律互相覆盖无主次：`commit immediately` / `before push verify` / `after interruption recheck` 各出现 2 次
- **S4** Rule precedence 只管 `rules/*`，不覆盖 `agents/*`
- **S5** Lore 导航模型跨 agent 分叉：Codex 走 wiki index→overview→domain；Claude 走 flat grep

### 4.4 Cross-agent asymmetry（Claude 对照暴露）

- **A1** Branch naming 只在 Claude 侧定义（component/feature/bugfix/cr 四类）；Codex 侧要求建分支但无命名规则
- **A2** Technical checkpoints 不对称：Claude 2 条集中；Codex 1 条集中 + 1 条散在 line 157
- **A3** Health check 严格度不对称：Claude git dirty → 硬停问用户；Codex git dirty → 软 advise 继续
- **A4** Proceed signal 触发词不对称：Claude 4 个；Codex 9 个（含中文扩展）
- **A5** Graphify skill 入口仅 Claude 侧有

### 4.5 Minor

- M1 `AGENTS.md.bak-20260403-193625` 备份残留
- M2 `task-related` vs `local junk` 无定义
- M3 Large-file guardrails 只覆盖 Python + Vue/JS/TS
- M4 `Paths` 独占一节但只有 1 条
- M5 Self-check 漏读类 / UI 类

---

## 5. Open questions

1. team-lore 统一形态：选 `wiki/`（结构化）还是 `LORE.md`（flat 好 grep）？选定后两份全局文件同步改
2. archive-review 细节：从全局文件剥离后，是否在每个需要此规则的 repo AGENTS.md 里都已覆盖？
3. Codex 的 Proceed signal 比 Claude 宽（9 vs 4），是**故意给 Codex 更宽容**，还是漂移？
4. Graphify 是 Claude-only 还是应扩到 Codex？
5. Branch naming 是否可以直接从 Claude 侧复制到 Codex 侧，还是需要 agent-specific 区分？
6. 本次诊断与 repo 级 `agents-governance-drift` 是否需要关联：它们都是"AGENTS.md 治理"语义，但作用域不同（repo vs global）。是否共享 canonical object？当前暂记为 related，非同一 object

---

## 6. Next step

- **本文件作用**：作为一次性 intake trace。不自动演进成 retro / ADR / spec
- **若后续处理**：应当走独立路径，不混入 repo Phase 0 / Phase 1
  - 小范围修正（C1 / C3 / A1 / A2）可直接改文件，无需 OpenSpec
  - 结构性重整（C2 / S1 / S3）需要决定"全局文件职责边界"——这是 personal-ops 层决定，repo 不强制
- **候选参考**：若真启动重整，可参考
  - official `agents.md` spec 的 precedence model
  - skyzyx progressive disclosure（主文件最小 + domain 细节搬独立文件）
  - 本 repo `wiki/ops/agents-governance-drift-distill-2026-04-21.md` 的 v3.1 候选框架（**candidate，非共识**）
- **不动的也记**：若选择"识相不改"，也把本 intake 的结论作为 "2026-04-25 状态快照"，避免下次重复走诊断流程

---

## 7. GitHub AGENTS.md 书写方式参考

### 7.1 本轮补充来源

本轮追加的是"AGENTS.md 应该怎么写"的样例学习，不是 hook 配置学习。参考对象：

| 来源 | 可复用信号 |
|------|------------|
| OpenAI Codex repo `AGENTS.md` | 以工程约定、模块边界、测试命令、API 规则为主；不把治理历史写成入口规则 |
| OpenAI Cookbook `AGENTS.md` | 典型结构是项目结构、构建测试、命名风格、提交/PR、发布元数据和 review 要点 |
| openclaw `AGENTS.md` | 明确受限路径、测试门槛、发布/安全 workflow 技能入口；规则多为可执行动作 |
| Codex 官方 AGENTS.md spec | AGENTS.md 是目录树作用域内的工作提示；更深层文件优先，直接 user/developer/system 指令更高优先级 |

### 7.2 抽取出的书写原则

- AGENTS.md 更适合作为 **operating card**，不是治理论文或历史演进记录。
- 优先写可执行信息：项目结构、常用命令、测试要求、命名约定、提交要求、受限路径、必须更新的元数据。
- 少写抽象判断词；把"保持边界清晰"改成"遇到 X 时读 Y / 停止 / 询问 / 跑 Z 命令"。
- 不把二级规则全文搬入 AGENTS.md；入口文件只放硬边界和路由，细节交给 `rules/*`、repo `AGENTS.md`、wiki、ADR 或 OpenSpec。
- 对用户级 `~/.codex/AGENTS.md`，更应避免塞入 repo-specific policy；全局层只保留跨仓库稳定成立的行为边界。

### 7.3 对当前 `~/.codex/AGENTS.md` 的候选改写骨架

候选骨架仅作后续重整参考，尚未形成决策：

1. `Identity & Scope`
   - 声明这是 yan 的 personal global rules。
   - 说明 repo `AGENTS.md` / `PROJECT.md` 负责 repo-specific semantics。

2. `Start Checklist`
   - substantial project work 才要求找 `PROJECT.md`。
   - large coding work 才要求完整 worktree / OpenSpec / lore 流程。

3. `Git Safety`
   - 不从记忆声明 clean / synced / committed。
   - feature work 不在 `main` 上继续。
   - stage only task-related files。
   - hidden tool dirs 默认 local junk，除非任务明确要求。

4. `Behavior Assets`
   - `AGENTS.md`、`rules/*`、`skills/*` 都是 behavior assets。
   - 语义修改必须先加载 `~/.codex/rules/common/development-workflow.md`，并留下 baseline / after evidence。

5. `Rule Routing`
   - implementation -> `rules/common/development-workflow.md`
   - git boundary -> `rules/common/git-workflow.md`
   - security/API/external call -> `rules/common/security.md`
   - testing -> `rules/common/testing.md`
   - Python -> `rules/python/*`
   - frontend -> `rules/web/*`

6. `Hard Stops`
   - substantial project work 找不到 `PROJECT.md`。
   - large scoped work 的 REQ / OpenSpec 映射不清。
   - dirty worktree 中 task-related 与 local junk 未分类。
   - destructive git / file operation 未获得明确请求。

### 7.4 与 hooks 的关系

- AGENTS.md 负责"应该如何工作"的入口规则。
- Codex hooks 适合承接可自动判断的提醒或拦截，如 `git push origin main`、`git reset --hard`、dirty worktree、Stop 前未 commit。
- hooks 当前不能完全替代 AGENTS.md：工具覆盖仍有限，尤其不能把文件写入、所有 shell 形态、WebSearch 等都视为已被完整强制拦截。

### 7.5 本节状态

- 这是 external example learning capture。
- 不是 ADR，不改变当前全局文件。
- 后续若实际改 `~/.codex/AGENTS.md`，应先决定 global 文件职责边界，再按 behavior asset gate 做 before/after evaluation。

---

## 8. 本诊断的 proof boundary

- **已验证**：文件现状 + 外部参考源 + GitHub AGENTS.md 样例 + Claude 对照物 + 引用链文件存在性
- **未验证**：上述问题对实际 Codex session 行为的量化影响（需单独压测）
- **候选 vs 事实**：所有"优化方向"为候选，未达任何共识；行数基准 60 / 150–200 / 213 为外部参考数值，不是本 repo 已定的目标

本 intake 不主张任何特定整改路径。
