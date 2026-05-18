---
title: ~/.codex/AGENTS.md 全局文件诊断
type: intake
canonical_object: codex-global-agents-md
artifact_type: intake
language: zh-CN
audience: self
domain: wiki
layer: ops
ops_area: agent-governance
period: evergreen
confidence: high
status: active
updated_at: 2026-04-29
ai_generated: true
source_path: /home/yan/.codex/AGENTS.md
source_type: global-agent-config
related_objects:
  - agents-governance-drift
  - agent-governance-gate-gap
derived_from:
  - https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
  - https://arxiv.org/html/2602.11988v1
  - https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b
  - https://github.com/danielrosehill/Agents.md-Templates
  - https://raw.githubusercontent.com/openai/codex/main/AGENTS.md
notes_scope: 对 ~/.codex/AGENTS.md（281 行，1909 words，用户全局 Codex 配置）的一次诊断 + 外部参考对标。非 repo AGENTS.md 诊断；与 agents-governance-drift 同根但作用对象不同。2026-04-29 经过来源核验后修订；所有外部查询结论必须带 URL，所有量化结论必须带本地命令或外部来源。
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
- 它与已核验 AGENTS.md 外部参考之间的差距；未重新定位 URL 的来源不再作为具体论据使用

---

## 3. 外部参考源摘要（2026-04-29 重新核验）

| 参考 | 核心信号 | URL / 验证 |
|------|---------|-----------|
| GitHub Blog "2500 repos 研究" | 文章声称分析 2,500+ 个 `agents.md` 文件；明确列出 6 个 core areas：commands / testing / project structure / code style / git workflow / boundaries；本轮未在文中找到任何推荐行数数字 | https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/ |
| arXiv 2602.11988 | HTML 摘要声称 context files 通常降低任务成功率并增加 20%+ inference cost；正文表述 LLM-generated context files 在 SWE-bench Lite / AGENTbench 上平均 cost increase 为 20% / 23%；developer-provided context files at most 19% cost increase | https://arxiv.org/html/2602.11988v1 |
| skyzyx gist | 引 Humanlayer Kyle 的 instruction budget：frontier thinking LLMs can follow about 150-200 instructions with reasonable consistency；作者建议 `AGENTS.md` should be as small as possible | https://gist.github.com/skyzyx/c91d9be9e5050c85e81ccbcca022ff6b |
| danielrosehill 模板仓库 | Template Index 当前列出 9 个模板入口，分布在 project-type、purpose-outline、stack-context、sysadmin 等目录；这是社区样例，不是规范来源 | https://github.com/danielrosehill/Agents.md-Templates |
| openai/codex raw `AGENTS.md` | 2026-04-29 Web 打开显示 Total lines: 40；因此 2026-04-27 的“213 行”记录已过期，不能继续作为当前量化基准 | https://raw.githubusercontent.com/openai/codex/main/AGENTS.md |
| `~/.claude/CLAUDE.md`（同机对照物） | 跨 agent 不对称见 4.4 节（实列 5 处，非"9 处"）；属于 local comparison，不是外部查询 | local |

**修订记录（2026-04-27）：**
- 删除原"GitHub 2500-repo 优秀示例约 60 行"——伪引用，GitHub 官方博客全文无任何行数数字
- 修正原"4 类模板"为"9 个/5 类"
- 修正原"两份全局文件存在 9 处跨 agent 不对称"为 5 处（与 4.4 节对齐）
- 2026-04-29 再修订：撤回未在当前来源中定位到的 `mean=641 / min=24 / max=2003 / section mean=9.7` 量化断言；撤回 openai/codex `213 行` 作为当前基准，改用当前 raw 显示的 40 行。

---

## 4. 当前诊断 hypothesis

### 4.1 量化基准（2026-04-29 重新核验）

| 指标 | 现状 | 外部参考 | 判断 |
|------|------|---------|------|
| 行数 / 字数 | 281 lines / 1909 words（`wc -l -w /home/yan/.codex/AGENTS.md`） | openai/codex raw `AGENTS.md` 当前 40 lines；skyzyx 建议 small as possible；GitHub Blog 未给推荐行数 | 当前文件明显长于一个当前官方项目样例；结论只支持“偏长且需分层”，不支持单靠行数判定必须删除 |
| 核心内容 | 个人 workflow 偏好 | 可执行技术约定 | 类型错位 |
| 含 repo-specific policy | 是（OpenSpec archive-review 细节，line 115–127） | local line 280 自称 repo-specific semantics 归 repo | 与文件自身边界冲突 |
| 24 天行数变化 | 223 lines / 1264 words（2026-04-03 backup）→ 281 lines / 1909 words（2026-04-27/29 current）= +58 lines / +645 words，约 +26% lines / +51% words | local `wc -l -w` | 正在堆积 |
| 生态形态 | personal global | danielrosehill 模板索引当前 9 个入口均是项目、栈、目的或系统管理样例 | 在该样例集里没有 personal-global 模板 |

**已删除项（伪引用 / 失实陈述）：**
- ~~"git 纪律重复段 3 处" / "各出现 2 次"~~：全文 grep 实测 `commit immediately` 只出现 1 次（line 165），`before push verify` 0 次，`interruption` 4 次但集中在一段。字串重复不成立；若需保留 S3，应改为"语义重复"论证而非字串计数
- ~~"超预算 40-360%"~~：基于伪基线 60 行得出，已删
- ~~"3 周 +22%"~~：实测 24 天 +26%，已更正
- ~~"arXiv 字数 mean=641 / min=24 / max=2003 / section mean=9.7"~~：2026-04-29 未在当前 HTML 来源中定位到，撤回为未验证。
- ~~"openai/codex repo 213 行"~~：2026-04-29 当前 raw 打开显示 Total lines: 40，旧数字只能视为过期记录，不能作为当前基准。

**修订记录（2026-04-29）：** 原表中"优秀示例 ~60 行"为伪基线（GitHub 官方博客无此数字），已删除；arXiv 只保留当前来源可定位的 cost 结论，不再承载未定位到的字数统计。

### 4.2 Critical 问题（实际矛盾）

- **C1** team-lore 路径 + 数据模型双重分叉：Codex 侧 `/mnt/d/team-lore/wiki`（目录）vs Claude 侧 `~/team-lore/LORE.md`（flat 文件）。跨 agent 各走各路
- **C2** 全局文件装了 repo policy（line 115–127 OpenSpec boundary 含 archive-review 细节）。自违反 line 280 的 "repo semantics 归 repo" 声明
- **C3** 硬编码 WSL 绝对路径（`/mnt/d/team-lore/wiki`）

### 4.3 Substantive 问题（设计张力）

- **S1** REQ identification 在 OpenSpec 为 default 的前提下成死代码
- **S2** "active OpenSpec change"（line 61）vs "approved OpenSpec change"（line 108）前后不一
- **S3** ~~三段 git 纪律互相覆盖无主次：`commit immediately` / `before push verify` / `after interruption recheck` 各出现 2 次~~（**2026-04-27 撤回字串重复陈述**：grep 实测仅 line 165 有一次 `commit immediately`，其他短语零次或单次。若 S3 仍成立，应基于"语义重复"重新论证而非字串计数）
- **S4** Rule precedence 只管 `rules/*`，不覆盖 `agents/*`
- **S5** Lore 导航模型跨 agent 分叉：Codex 走 wiki index→overview→domain；Claude 走 flat grep

### 4.4 Cross-agent asymmetry（Claude 对照暴露）

- **A1** Branch naming 只在 Claude 侧定义（component/feature/bugfix/cr 四类）；Codex 侧要求建分支但无命名规则
- **A2** Technical checkpoints 不对称：Claude 2 条集中；Codex 散在 line 110、line 157、line 246 三处（2026-04-27 修正：原记 "1 条集中 + 1 条散在" 漏数 line 246）
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
  - 本轮已核验来源中的 minimal / specific / boundary / command-first 信号
  - skyzyx progressive disclosure（主文件最小 + domain 细节搬独立文件）
  - 本 repo `wiki/ops/agents-governance-drift-distill-2026-04-21.md` 的 v3.1 候选框架（**candidate，非共识**）
- **不动的也记**：若选择"识相不改"，也把本 intake 的结论作为 "2026-04-25 状态快照"，避免下次重复走诊断流程

---

## 7. GitHub AGENTS.md 书写方式参考

### 7.1 本轮补充来源

本轮追加的是"AGENTS.md 应该怎么写"的样例学习，不是 hook 配置学习。参考对象：

| 来源 | 可复用信号 | URL / 验证 |
|------|------------|-----------|
| OpenAI Codex repo `AGENTS.md` | 2026-04-29 当前 raw 只有 40 行；可作为“短入口卡片存在”的样例，但旧的 213 行结构解读已过期 | https://raw.githubusercontent.com/openai/codex/main/AGENTS.md |

### 7.2 抽取出的书写原则

下面是基于已核验来源和本地文件诊断得到的候选原则，不是外部来源逐字规定：

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

- **已验证（2026-04-29 重新核验）**：本地文件现状（`wc -l -w /home/yan/.codex/AGENTS.md` = 281 lines / 1909 words）+ 备份（223 lines / 1264 words）+ GitHub Blog 2,500+ repos 与 6 core areas + arXiv 20% / 23% / at most 19% cost signals + skyzyx 150-200 instructions 引用 + danielrosehill 9 template entries + openai/codex raw 当前 Total lines: 40 + Codex Proceed signal 9 词 / Claude 4 词 + line 引用全部对位
- **未验证**：上述问题对实际 Codex session 行为的量化影响（需单独压测）
- **已撤回的伪陈述**：
  - "GitHub 2500-repo 优秀示例约 60 行" — GitHub 官方博客全文无此数字
  - "超预算 40-360%" — 基于伪基线推论
  - "git 纪律 3 处重复 / 各 2 次" — grep 实测对不上
  - "3 周 +22%" — 实测 24 天 +26%
  - "9 处跨 agent 不对称" — intake 自身只列 5 处，已与 4.4 对齐
  - "openai/codex AGENTS.md 当前 213 行" — 2026-04-29 当前 raw 显示 40 行，旧数字已过期
  - "arXiv mean=641 / min=24 / max=2003 / section mean=9.7" — 当前 HTML 来源未定位到，撤回为未验证

本 intake 不主张任何特定整改路径。

---

## 9. 2026-04-27 openspec-explore 复查

### Trigger

用户要求用 `$openspec-explore` 复查 `codex-global-agents-md-diagnosis-intake-2026-04-25` 有什么问题。

### Current focus

- 区分 `~/.codex/AGENTS.md` 本体问题与本 intake 记录问题
- 判断本 intake 是否已经足够支持下一步动作
- 不在本轮修改 `~/.codex/AGENTS.md`

### Confirmed facts

- 当前 `~/.codex/AGENTS.md` 仍为 281 行。
- 本 intake 对 C1/C2/C3、S1-S5、A1-A5 的诊断仍能从当前文件中找到对应信号。
- 本 intake 明确声明自己是 `intake`，不作决定，不自动演进成 retro / ADR / spec。

### Current hypotheses

- 这份 intake 的主要问题不是诊断太少，而是缺少 action 分层：可直接修的小问题、需要跨 agent 对齐的问题、需要职责边界决策的问题混在一起。
- `C2`（global 文件装 repo policy）应是最高优先级，因为它直接违反当前文件自己的全局 / repo 边界声明。
- `C1/C3/A1/A2` 更像低风险收口项；如果不动结构，至少可以先形成一个独立 small-fix list。
- `S1/S3` 需要先决定 global 文件是否做 progressive disclosure，否则容易继续把压缩变成新一轮堆积。

### Open questions

1. 这次是只要诊断结论，还是要把它推进成一个可执行整改 change？
2. `~/.codex/AGENTS.md` 的整改是否允许直接修改个人全局文件，还是需要先在本 repo 内生成方案再人工迁移？
3. Codex / Claude 全局规则是否需要追求对称，还是只对齐共同边界、保留 agent-specific 差异？

### Next step

- 如果只是诊断：本轮停在口头结论即可。
- 如果要推进整改：先把问题分成 `quick fixes`、`cross-agent alignment`、`global-boundary decision` 三组，再决定是否创建 OpenSpec change 或个人全局整改清单。

---

## 10. 2026-04-27 everything-claude-code AGENTS.md 参考

### Source

- `https://github.com/affaan-m/everything-claude-code/blob/main/AGENTS.md`
- 观察对象是 `everything-claude-code` 的 repo-level `AGENTS.md`，不是 personal global AGENTS 模板。

### What can be reused

- 它像一张 operating card：先声明项目对象，再列核心原则、agent/skill 路由、安全、测试、工作流、目录结构和成功指标。
- `Workflow Surface Policy` 值得参考：明确 `skills/` 是 canonical workflow surface，`commands/` 是兼容层。这与本 repo 当前“技能正式层 vs draft/command 层”的治理问题同构。
- “知识落点”规则值得参考：个人临时信息、团队项目知识、任务已产出文档、无明确落点时询问，四类边界清晰。
- 相比当前 `~/.codex/AGENTS.md`，它更少讲历史和治理争议，更强调执行入口，这支持“global AGENTS 应压成入口卡片”的候选方向。

### What should be adapted

- 它的 agent-first 路由只适合实际拥有 48 个 specialized agents 的 ECC 仓库；不能搬到 Codex 全局层，因为本机 Codex sub-agent 使用受显式授权约束。
- 它的 `80%+ coverage`、all test types required、TDD mandatory 适合产品仓库目标，不适合个人全局规则直接硬编码。
- 它的 `Always create new objects, never mutate existing ones` 是过宽技术偏好；若放入全局 AGENTS，会误伤 Python/Vue/配置文件等正常更新场景。
- 它的 `200-400 lines typical, 800 max` 与当前全局 guardrail 阈值不同；可作为参考数值，不能直接替换。

### What is rejected

- 不把 `Available Agents` 大表复制进 `~/.codex/AGENTS.md`。全局入口不应枚举不存在或未授权的 agent。
- 不把 `Agent-First` 当成默认。当前规则仍应保持“只有用户明确要求 sub-agent 时才 spawn”。
- 不把 repo-level success metrics 改成 personal global hard gate。

### Repo target

- 目标仍是 `codex-global-agents-md` 这个 intake。
- 若后续改 `~/.codex/AGENTS.md`，该参考只支持两个候选原则：
  1. 主文件做 operating card，而不是治理历史全文。
  2. workflow surface / knowledge routing / hard stops 可以独立成高密度段落。

### Residual risks

- 该文件来自 Claude Code 插件仓库，不是 OpenAI 官方 `AGENTS.md` spec；只能作为样例，不是规范来源。
- raw 文件当前呈现为单行 markdown，说明格式本身对机器可读性不理想；不能拿它证明“短文件就一定好读”。

---

## 11. 2026-04-29 量化数据核验

### Trigger

复查发现 intake 多处量化断言无来源；用户要求"明确量化的数据要验证清楚给出来源"。

### 方法

逐条对 intake 中所有数字断言做 fact-check：本地 grep / wc / 备份 diff + WebFetch 原始来源。规则是：外部查询结论必须带 URL；本地量化结论必须带命令；找不到来源的断言只能保留为撤回项或未验证项。

### 核验结果

| 断言 | 验证 | 结论 |
|------|------|------|
| `~/.codex/AGENTS.md` 281 行 | `wc -l` | ✅ 成立 |
| openai/codex AGENTS.md 213 行 | 2026-04-29 重新打开 raw，当前 Total lines: 40 | ❌ 旧数字过期，不能作为当前基准 |
| skyzyx "150-200 条指令" | WebFetch gist | ✅ 成立（原文引 Humanlayer Kyle） |
| line 61 / 108 / 115-127 / 157 / 280 引用对位 | sed -n | ✅ 全部成立 |
| C2 OpenSpec archive-review 装在全局 | line 117/120/125/127 实有 | ✅ 成立 |
| C3 硬编码 `/mnt/d/team-lore/wiki` | line 14 | ✅ 成立 |
| Codex Proceed signal 9 词 | line 103-104 = 4+5 | ✅ 成立 |
| M1 备份残留 | ls | ✅ 成立 |
| **GitHub "2500-repo 研究 优秀示例约 60 行"** | WebFetch 原文 | ❌ **伪引用**——博客全文无任何行数数字 |
| **"超预算 40-360%"** | 基于上一项推论 | ❌ **基础垮了**，已删 |
| **"3 周 +22%"** | 备份 2026-04-03 = 223 行 → 现 281 行 | ⚠️ **24 天 +26%**，已更正 |
| **"git 纪律 3 处重复，各 2 次"** | grep 实测 | ❌ **失实**——`commit immediately` 仅 1 次 |
| **"9 处跨 agent 不对称"** | intake 仅列 A1-A5 | ❌ **自相矛盾**，已对齐为 5 处 |
| **"4 类模板"** | WebFetch | ⚠️ 实为 9 个/5 类，已更正 |
| arXiv 2602.11988 实证（20%+ cost increase；20% / 23% cost increase；developer context at most 19%） | WebFetch | ✅ 成立 |
| arXiv 2602.11988 字数 mean=641 / min=24 / max=2003 / section mean=9.7 | 2026-04-29 当前 HTML 未定位到 | ❌ 撤回为未验证，不再作为量化基准 |

### 修订

第 3 节（外部参考）+ 第 4.1 节（量化基准）+ S3 + A2 + 第 8 节（proof boundary）+ frontmatter（`updated_at: 2026-04-29`、`derived_from` 保留可核验 URL）已同步更新。

### 残留风险

- official `agents.md` spec、OpenAI Cookbook、openclaw 在本轮未独立 fact-check，相关旧表述已从证据表中移除
- `S3` git 纪律重复的"语义重复"判断尚未重做；当前只确认了原"字串重复"陈述失实，不等于 S3 整体撤销，待重新论证
- 本核验只覆盖了 intake 的量化数据，未覆盖 intake 的结构性 / 哲学性判断（C2 / S1 / S5 等仍为候选诊断，未达共识）

---

## 12. 2026-04-29 root governance alignment design conclusion

### Trigger

围绕 `decide-root-governance-alignment` 的设计修补中，用户追问：

- `harness` 到底是什么
- 设计稿到底要改成什么样子
- 为什么学习完没有结论、wiki 也没有落
- git 学习完的结论是什么

### Why the previous wiki landing failed

这次没有及时落 wiki，不是因为没有规则，而是因为三层约束互相拉扯：

1. repo-local `openspec-explore` skill 本体强调 `stance, not workflow`，容易让执行者把它理解成只切换思考姿态。
2. repo `AGENTS.md` 和 ADR-0009 又要求每次 `openspec-explore` 在 `wiki/ops/` 留 trace。
3. 当前 active change 同时写了 `wiki-gated`：不能把 root governance 设计直接升级成 wiki method page 或 ADR。

正确拆分应是：

- wiki 可以落学习结论和校准材料
- OpenSpec 继续承接正式设计和任务状态
- ADR 或 method page 必须等稳定决策后再晋升

本节就是补上这次应落的学习结论，不把它包装成最终治理决定。

### Current design conclusion

`harness` 在当前治理设计里只应定义为行为设计的回放证据包。

它包括：

- 一个说明验证对象、字段、通过标准、proof boundary 的 `replay-harness.md`
- 一个 markdown 或 JSON fixture，记录 RED baseline、GREEN expectation 和 residual risk
- active OpenSpec change 内的 `evaluation.md`，记录 before / after / residual risks

它不包括：

- hook
- CI gate
- runtime gate
- 自动合规系统
- 自动证明未来 agent 一定会执行

当前设计稿要表达的是 root/repo-aware 职责分离：

| Layer | Responsibility |
|---|---|
| root `AGENTS` | 跨 repo 入口路由、硬停止、git 真值、升级边界 |
| repo `AGENTS` | repo-local policy、OpenSpec 触发、wiki routing、项目级 stop conditions |
| `rules` | 常驻横切约束，如 git、安全、测试、行为资产修改门槛 |
| `skills` | 按需触发的行为合同，保持短小，细节放 references/scripts |
| OpenSpec | 行为资产变化的 lifecycle、scope、tasks、evaluation |
| harness | 人工回放证据，不做执行 gate |
| wiki / ADR / retro | 学习、复盘、稳定决策沉淀 |

### Quantified conclusion

当前结论不是“全局 AGENTS 必须立刻大删”，而是“偏长且类型错位，需要先分层”。下面的外部指标来源见第 3 节；本地指标来源为 `wc -l -w /home/yan/.codex/AGENTS.md /home/yan/.codex/AGENTS.md.bak-20260403-193625`：

| Metric | Current evidence | Conclusion |
|---|---:|---|
| `~/.codex/AGENTS.md` current size | 281 lines | 偏长，但不是单靠行数判死刑 |
| 2026-04-03 backup | 223 lines | 24 天增加 58 行 |
| Growth rate | about 26 percent | 有持续堆积趋势 |
| OpenAI Codex repo AGENTS reference | current raw Total lines: 40 | 当前个人全局文件明显长于这个当前官方项目样例 |
| arXiv 2602.11988 sample | 20%+ inference cost increase signal; detailed text cites 20% / 23% average cost increases for LLM-generated context files | 当前问题更像“内容是否必要、是否分层”，不只是长度 |
| current design repair root edits | 0 | 本轮不改变 runtime |
| current design repair skill edits | 0 | 本轮不重测 trigger 行为 |
| current design repair wiki method edits | 0 | 本轮只补 intake 学习结论 |

### Phased recommendation

建议渐进式推进：

1. Phase 0：只完成当前 OpenSpec 设计稿，接受或修改 root/repo-aware 职责模型。
2. Phase 1：如果接受，再做人工版 harness 模板，不写 checker。
3. Phase 2：只有模板被至少 3 个行为资产 change 使用后，再考虑结构 checker。
4. Phase 3：只有 checker 证明有用后，另起 OpenSpec 讨论是否进入 hook、CI 或 archive gate。

### Git learning conclusion

git 结论已经稳定，后续可以直接复用：

- 不能凭记忆说 `clean`、`committed`、`synced`。
- 任何这类判断前必须重新跑 `git status --short` 和 `git log -1 --oneline`。
- dirty worktree 下必须区分 `task-related` 和 `local junk`。
- hidden tool directories such as `.claude/`, `.idea/`, `.obsidian/` default to `local junk` unless the task explicitly targets them.
- non-hidden content directories such as `inbox/` still require task relevance classification; 当前 root governance 任务不应把它们纳入提交。
- 本次任务相关文件只应包括 active OpenSpec artifacts 和本 intake 页面。

### Next step

下一步不应直接改 root dotfiles。先审阅
`openspec/changes/decide-root-governance-alignment/design.md`：

- 是否接受 root/repo-aware 职责分离作为 review baseline
- 是否接受 `harness` v1 只作为人工证据模板
- 是否接受 Phase 1 先做模板、不做 checker
