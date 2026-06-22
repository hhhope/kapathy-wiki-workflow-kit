<callout emoji="💡" background-color="light-blue" border-color="blue">
这套 Codex 项目规范包，核心解决的是“首次接入 Codex 时，不知道 AGENTS.md / rules / skills / agent 模板怎么组织，最后每个项目各写一份、规则重复、边界不清、也不好复用”的问题。
</callout>

## 一句话结论

我们把 Codex 在项目里的能力拆成五层：

| 层级 | 放什么 | 解决什么问题 |
|------|--------|--------------|
| `AGENTS.md` | 项目门禁、启动顺序、规则入口索引 | 防止一上来就跳过健康检查、REQ/lore、git 状态核验 |
| `rules/` | 长期常驻工程规则 | 把 Git / 安全 / 测试 / Python / Web 规范沉下来，避免 AGENTS.md 里写一大坨重复条款 |
| `agents/` | planner / code-reviewer / security-reviewer / python-reviewer 角色模板 | 用户明确要求开子代理时，有统一职责边界和输出格式 |
| `skills/` | 场景化 reference card，例如 DB migration、Jira 对齐 | 不是流程说明书，而是“已知道要做什么后，直接查参数、约束、错误排查”的 cheatsheet |
| `governance-install` | 对话式安装入口 | 用户直接说一句“帮我装到 Codex / Cursor”，AI 就按平台执行 |

---

## 这次落地了哪些能力

### 1）项目门禁和上下文恢复

- 进入仓库后先读 `AGENTS.md`
- 再读 `rules/common/development-workflow.md`、`rules/common/git-workflow.md`
- 再读 `PROJECT.md`、active REQ、`logs/`、当前 `git status`
- 中断恢复后必须重新核对 `git status --short` 和 `git log -1 --oneline`
- 未重新核验前，不允许口头宣称“已提交 / 已干净 / 已同步”

### 你如何驾驭这套 AI 编码体系

<image token="IW04blXkiokWj6xcZeWcfaOZnTf" width="1800" height="1460" align="center"/>

这张图用于说明控制关系、阶段方法、验证入口和路线图：

| 层 | 你要看什么 | 在体系里扮演什么角色 |
|----|------------|----------------------|
| 你 / 决策者 | 目标、边界、是否继续、是否接受结果 | 方向盘，决定 AI 做什么、不做什么 |
| `AGENTS.md` + `PROJECT.md` | 健康检查、git truth、路由、完成门槛 | 控制层，决定 AI 是否能进入下一步 |
| `rules/` | Git / 安全 / 测试 / Python / Web 等常驻约束 | 长期边界，防止 AI 为了省事绕规则 |
| `skills/` + `agents/` | lore、graphify、database-migrations、feishu-doc-writing 等方法卡 | 场景化能力层，告诉 AI 这类任务该怎么做 |
| `OpenSpec` / `Lore` / `Graphify` | 过程、规则事实、代码结构 | 规划与知识层，决定先读什么、先信什么 |
| CLI / tests / git / `lark-cli` | 执行、验证、同步 | 执行层，把决策变成可验证产物 |

如果只画“默认时序”，读者会以为这是几个命令的先后顺序；真正重要的是：

- 你在上层给目标和许可
- `AGENTS.md` / `rules` / `skills` 约束 AI 的动作空间
- `OpenSpec` / `Lore` / `Graphify` 分别提供过程真相、稳定知识、结构证据
- CLI 和测试只负责执行与验证，不负责定义真相

### 这套体系在代码生命周期里怎么协作

| 阶段 | 默认主入口 | 产出什么 |
|------|------------|----------|
| `start` | `AGENTS.md`、`PROJECT.md`、git truth | 确认能不能开工，先读什么 |
| `route` | OpenSpec / Lore / Graphify | 确认当前 change、规则边界、代码入口 |
| `implement` | 代码实现 + 对应 skill | 修改代码、文档、模板、配置 |
| `verify` | TDD、tests、routing checks、benchmark、readback | 确认不是“看起来差不多”，而是真通过 |
| `absorb` | `logs/`、weekly review、team-lore | 把一次性的任务事实沉成 durable memory |
| `publish` | Feishu share / wiki / rollout note | 把对外可读的说明和结果同步出去 |

### 需求评审 agent kit 新增了什么

这次把 `req-agent-kit/req-agent` 从“安装一组需求脚本”升级成了一个完整的需求评审入口。它的定位不是替产品经理做决定，而是在开发前把需求材料拆成可审查、可追溯、可阻断的状态。

| 关注点 | 现在怎么处理 |
|--------|--------------|
| 需求识别 | `req-agent` 先判断用户是在做 intake、分析、范围确认、验收、ready check，还是 OpenSpec handoff |
| taxonomy | `requirements/config/requirements-taxonomy.yaml` 是需求领域词表，和 wiki frontmatter taxonomy 分开；它按 DDD 模型解构当前支付生态：支付生态 8 个核心 subdomain，Agent 服务相邻生态 5 个 subdomain |
| 需求分析 | `req-domain-analysis` 先做 DDD `domain_model`，再识别 context 重叠、协作边界和 domain coverage obligations，最后交给 scope、stories、acceptance |
| AGI 协作 | AGI 负责结构化评审、证据整理和候选判断；人提供业务材料、当前状态、规则口径、系统边界和 waiver 决策 |
| 质量门 | readiness 拆成 `domain_model_gate`、`domain_coverage_gate`、`requirement_delivery_gate`、`detailed_design_gate` |
| 停止条件 | OpenSpec draft 只是 handoff，不代表批准实现；详设和实现还要等 current-state material、business rule position、system boundary contract 过 gate 或显式 waiver |

这个 kit 的关键价值，是把“AI 看完需求直接开写”的冲动挡在前面：先识别需求，再做领域分析，再补 stories / acceptance / coverage，最后才允许进入 OpenSpec 草案。

taxonomy 的主线是“分类 -> 建模 -> 标准 -> 讨论 -> 复利”：分类只是行为，建模才是目的；标准让讨论有共同对象，讨论沉淀后才会变成下一次需求分析的复利。

`req-agent-kit/req-agent/README.md` 已改成中文说明，并补了 taxonomy / DDD / 支付生态解构 / 需求分析流程的 ASCII 图示，便于直接作为 kit 入口文档阅读。

### 我们一起构建了什么

我们现在构建出来的不是一个单点工具，而是一套 `Account Harness`：

- 用 `OpenSpec` 管大任务的 proposal / design / tasks
- 用 `OpenSpec + TDD` 把设计和验证接到同一条 change 线上，而不是先写设计、最后再补验证
- 用 `Lore` 管原则、边界、pitfall、weekly review 吸收
- 用 `Graphify` 管代码结构检索，降低全仓硬读的 token 成本
- 用 `AGENTS.md`、`rules/`、`skills/` 管 AI 的行为边界
- 用 `lark-cli` 和飞书文档把对外表达纳入同一个工作周期

这里有两个关键来源也应该说清楚：

- `OpenSpec + TDD`：我们不是把 TDD 放在实现末尾，而是把它前移成 change 的一部分，让 `proposal / design / tasks / eval` 能互相约束
- `raw wiki` 思路：Lore 不追求一上来就写成漂亮长文，而是更接近可检索、可吸收、可演化的原始工程记忆，再通过 page contract 和 weekly review 慢慢变稳定

### 这轮暂时完成了什么

| 已完成 | 当前状态 |
|--------|----------|
| OpenSpec 过程层 | 已落到 change / proposal / design / tasks |
| Lore 检索页模型 | 已做 retrieval-first page contract 和 rollout slice |
| Graphify 结构证据层 | 已接入 update/query 使用方式和 benchmark 案例 |
| Feishu 同步门槛 | 已进 `PROJECT.md` completion gate |
| 文档发布门槛 | 已要求读者友好、表格优先、远程 readback、图文一致性 |

### 这轮产出了什么

| 产物 | 用途 |
|------|------|
| `codex-integration-kit` | 可迁移的治理包 |
| `req-agent-kit` | 需求评审 agent kit，用 taxonomy、worker skills、checker scripts 把需求材料转成可审查状态 |
| `skills/*` | 场景化 reference card |
| `rules/*` + `AGENTS.md` | 常驻约束和启动门禁 |
| OpenSpec / eval docs | 设计、TDD、验证证据 |
| team-lore rollout slice | 可检索的 durable memory 结构 |
| 飞书四篇文档 | 总览、运行态、安装与迁移、验证与案例 |

### 未来可以继续往哪里加硬

| 方向 | 目标 |
|------|------|
| `pre-push` / CI 校验 | 把一部分规则从“文档约束”升级成“硬拦截” |
| query 分类自动化 | 让 Lore / Graphify / OpenSpec 路由更少依赖人工判断 |
| Lore + Graphify 联动评测 | 不只看 recall，也看结构证据对真实排查的帮助 |
| 发布后 lint | 自动检查飞书标题、表格、图文关系、readback 是否齐全 |

### 面向 AICoding L1-L4 的路线图

这套体系的下一阶段，是把研发生命周期按阶段接到更稳定的 AI 协作方式上。

| Level | 当前目标 | 人机关系 | 代表能力 | 当前状态 |
|------|----------|----------|----------|----------|
| `L1` | AI 辅助查阅和局部执行 | 人主导，AI 做局部补全和查询 | 文档生成、局部改写、命令执行、基本检索 | 已稳定 |
| `L2` | AI 按约束完成单次任务 | 人定目标与边界，AI 能按 gate 执行 | `AGENTS.md`、rules、skills、OpenSpec、Lore、Graphify 联动 | 已基本完成 |
| `L3` | AI 进入可验证的阶段化协作 | 人定义阶段目标，AI 在需求/设计/研发/CR/验收中扮演固定角色 | 脑暴、SDD、TDD、前置 CR、验收驱动验证 | 现在要推进 |
| `L4` | AI 驱动的工程协作面 | 人负责方向和例外处理，AI 负责大部分日常推进与知识沉淀 | 自动路由、自动 lint、阶段指标、知识持续吸收、项目透视面板 | 远期目标 |

这四级不是抽象成熟度模型，而是我们当前体系的升级顺序：

- `L1` 解决“AI 能不能帮我做”
- `L2` 解决“AI 会不会乱做”
- `L3` 解决“AI 能不能按研发阶段协作，并且每个阶段都有验证”
- `L4` 解决“AI 能不能成为持续运行的工程协作面，而不是一次性助手”

### 对应研发生命周期的协作方式

| 阶段 | 推荐工作方式 | 主要载体 | AI 在做什么 |
|------|--------------|----------|-------------|
| 需求阶段 | `brainstorm first` | Feishu / PRD / Jira / 会议纪要 | 帮你拆问题、列方案、比边界，不直接跳实现 |
| 设计阶段 | `SDD first` | OpenSpec `proposal/design`、详设文档 | 把方案收敛成结构、接口、边界、风险和验收思路 |
| 研发阶段 | `implementation under SDD` | 代码、skills、Graphify、Lore | 依据设计实施，最小上下文读代码，减少盲搜 |
| CR 阶段 | `CR shift-left` | reviewer agent、rules、diff | 在提交前就做结构/安全/边界 review，不把 CR 全压到最后 |
| 验收阶段 | `TDD inside OpenSpec` | tests、benchmark、routing checks、raw data proof、eval docs | 让验证从 change 内部发生，而不是上线前临时补 |
| 沉淀阶段 | `absorb continuously` | logs、weekly review、Lore、Feishu share | 把有效事实、pitfall、路线和结果沉成可复用知识 |

### Lore 为什么不是“精装修 wiki”起步

我们在 Lore 上吸收了一部分 `raw wiki` 思想：先保留高信号的工程事实，再逐步结构化，而不是一开始就把知识写成大段说明文。

| 思路 | 我们怎么吸收 | 带来的好处 |
|------|--------------|-----------|
| `raw wiki` | 先记录真实事实、路径、边界、坑，再逐步整理 | 降低知识沉淀门槛，不容易因为“写得不够漂亮”而什么都不记 |
| retrieval-first page model | 用 `Scope / Applies When / Not For / Top Facts / Load Next` 收敛页面 | 提高 agent 命中率和首屏可读性 |
| weekly review absorption | 让散的事实经过 review 再升级为 durable memory | 保持 wiki 可演化，而不是一次性定稿 |
| Feishu-facing rewrite | 当内容要面向人读时，再通过 `feishu-doc-writing` 做渐进式整理 | 把“工程原始记忆”和“对外说明文档”分层处理 |

### 这条路线为什么是合理的

| 现在已有什么 | 能往上接什么 |
|--------------|-------------|
| `git truth`、commit discipline、branch discipline | 把阶段状态、改动分布和产出做成更可靠的工程记录 |
| OpenSpec proposal / design / tasks + evals | 支撑 `需求 -> 设计 -> 实施 -> 验收` 的阶段化切换 |
| Lore durable memory + raw wiki absorption | 支撑跨项目经验复用和 review 吸收 |
| Graphify code topology | 支撑大仓库低 token 成本的代码检索和结构透视 |
| Feishu sync gate | 支撑对外知识和对内实施保持同周期一致 |

### 我们可以继续加什么能力

| 方向 | 具体能力 | 价值 |
|------|----------|------|
| Git 透视 | 代码量、目录演化、模块热点、改动分布、功能覆盖映射 | 让 roadmap 和工程现实对齐，而不是只凭感觉 |
| 功能透视 | 从 OpenSpec、Lore、Graphify、git history 反推出功能地图 | 帮助新人上手、架构 review、影响面判断 |
| CR 前置 | 在开发中就做 reviewer pass，而不是等最后统一爆炸 | 降低返工和 late-stage surprises |
| 验收加硬 | 把 TDD、benchmark、routing checks、readback 接进统一 gate | 让“完成”从主观判断变成可验证状态 |
| 知识库加速 | 自动把 logs / review / benchmark 结果转成 Lore 草案 | 降低知识沉淀的额外成本 |
| 协作看板 | 需求、设计、实施、验证、发布的阶段状态面板 | 让 L3/L4 升级有统一可见面 |

### 推荐的推进顺序

| 优先级 | 先做什么 | 原因 |
|--------|----------|------|
| `P1` | 把 `L2 -> L3` 的阶段协作固定下来 | 现在约束和工具已经够，缺的是阶段方法的统一 |
| `P2` | 把 CR 前置和验收 gate 再加硬 | 返工主要发生在这里，收益最高 |
| `P3` | 做 git / Graphify / OpenSpec / Lore 的联合透视 | 为功能地图、知识库和协作面板提供基础数据 |
| `P4` | 做更自动化的 L4 协作层 | 这一步必须建立在前面阶段定义稳定之后 |

### 延伸阅读

| 如果你要继续看 | 去哪里 |
|---|---|
| `L1-L4` 路线图完整版 | [AICoding L1-L4 路线图（更新至 2026-04-13）](https://my.feishu.cn/docx/XRj1dtTYDoxRF8xbdd6ckJUMnhd) |
| `需求 -> SDD -> 研发 -> CR -> 验收 -> 沉淀` 协作卡 | [AICoding 生命周期协作卡（更新至 2026-04-13）](https://my.feishu.cn/docx/TG7CdVjSNo3BOtxbAYdcWukznNh) |

### 2）长期常驻规则拆分

| 文件 | 重点约束 |
|------|----------|
| `rules/common/development-workflow.md` | health check、REQ/lore 匹配、大文件门禁、长步骤报备 |
| `rules/common/git-workflow.md` | 禁止从记忆判断 git 状态、禁止 main 上直接做 feature work、提交前后必须核对 HEAD/worktree |
| `rules/common/security.md` | auth/team scope、参数化 SQL、timeout、禁止日志/文档里泄密 |
| `rules/common/testing.md` | 后端/前端/DB/409/同步通知链路怎么验 |
| `rules/python/patterns.md` | FastAPI/Python 模块拆分、类型、异常、重任务边界 |
| `rules/python/security.md` | SQL 注入、路径逃逸、权限边界、日志泄密 |
| `rules/java/patterns.md` | Java 8+ 兼容的 Controller/Service/Repository 分层、DTO 校验、字符串归一化、接口参数长度约束 |
| `rules/java/security.md` | Java 接口边界校验、SQL 参数化、租户/团队范围、敏感日志与反序列化约束 |
| `rules/web/patterns.md` | Vue 3 状态/交互/API 调用、200 行以上优先拆分 |
| `rules/web/design-quality.md` | 看板和配置页的视觉一致性、按钮语言统一、避免模板感 UI |

补充约束：

- 对 `AGENTS.md`、`rules/*`、`skills/*` 这类行为资产，语义性修改必须带可追溯验证证据
- 这类验证不能只存在聊天记录里，至少要落到仓库内的 `docs/`、`evals/` 或 `logs/`

### 3）Agent 模板只保留“能力边界 + 输出格式”

| Agent | 用途 |
|-------|------|
| `planner` | 大需求拆 Phase、排依赖、列风险和验证方式 |
| `code-reviewer` | 按 CRITICAL/HIGH/MEDIUM/LOW 输出高置信 review findings |
| `security-reviewer` | 专盯 API/Auth/SQL/team scope/secret/logging 风险 |
| `python-reviewer` | 专盯 Python/FastAPI/MySQL diff 的异常、类型、阻塞调用、SQL 写法 |

默认不自动开子代理；只有用户明确说“开 planner / reviewer 子代理”时才使用这些模板。

### 4）Skill 改成 reference card，不写成长流程

我们参考了 `skill-creator` 的写法，把 skill 做成“查表 + 错误索引”：

- `description` 用三段式：触发词 + 隐含触发 + 排除条件
- 顶部先写 `Do Not`，拦高代价错误
- 核心用 `Intent Routing` 查表：意图 → 产物/工具 → 必填字段/必查项
- 再补 `Error / Risk Index`：症状 → 根因 → 修复方式

当前保留的三个 skill：

| Skill | 解决什么 |
|-------|----------|
| `skills/database-migrations/SKILL.md` | 新增表/字段、物理重命名、历史数据导入、回滚和验证 SQL |
| `skills/jira-integration/SKILL.md` | 业务-研发对齐后，从 Jira ticket / 会议结论抽需求、验收标准、测试场景、Jira 回写评论 |
| `skills/governance-install/SKILL.md` | 识别用户是要装到 Codex 还是 Cursor，并直接执行 dry-run / apply，而不是先让用户跳去看 shell 文档 |
| `skills/feishu-doc-writing/SKILL.md` | 飞书分享稿、知识总览页、治理说明文档的渐进式编排、拆文和上下文联动更新 |

最近又补了一条很实用的约束：

- 不要因为“新信息也很重要”就继续给主页新增一级章节
- 先判断这条信息有没有改变页面的职责
- 没改变，就并入现有章节或下沉到对应子页
- 尤其是 overview 页，不要一路漂成 install/how-to 页

`verification-loop` 已删掉，因为这部分和 AGENTS + testing rules + 我们现有收尾习惯高度重复，单独留 skill 收益不大。

这三张 skill 在 kit 里都应视为 starter card，接入新环境前需要先本地化命名、路径、字段和权限边界，不能直接当成仓库事实来源。

---

## 现在这套约束“怎么生效”

### 已经生效的部分

- Codex 进入项目后，会通过 `AGENTS.md` 看到规则索引和上下文恢复顺序
- rules / agents / skills 的职责边界已经拆开，不再把所有条款堆在一个 AGENTS.md 里
- skill 文档结构已经按 reference card 思路整理，便于快速查表

### 还不是硬拦截的部分

目前这些约束主要是“Codex 按文档主动遵守”，不是 git hook / CI 那种强制阻断。

如果要做到“违反规则就直接挡提交/挡修改”，下一步需要再补 git hooks 或校验脚本，把这些规则接到 pre-commit / pre-push / CI。

---

## Lore / Graphify 现在怎么分工

最近补清的一点是：不要把 OpenSpec、Lore、Graphify 混成同一层。

### 1）OpenSpec 是过程层，不是知识层

OpenSpec 回答的是：

- 当前 change 是什么
- proposal / design / tasks 到哪一步
- 过程状态和执行边界是什么

它解决的是“这次变更现在在做什么”，不是“稳定知识是什么”。

### 2）Lore + Graphify 是知识层，但职责不同

| 组件 | 负责什么 |
|------|----------|
| `Lore` | 规则、边界、pitfall、principle、stable facts |
| `Graphify` | 代码入口、邻接节点、桥接点、结构路径 |

一句话说：

- Lore 负责回答“这是什么问题、适用什么规则、先装哪些稳定事实”
- Graphify 负责回答“它在代码里哪里、和谁相连”

### 3）默认路由规则

| 问题类型 | 默认去哪里 |
|----------|------------|
| 过程问题 | `OpenSpec` |
| 规则/边界问题 | `Lore` |
| 代码结构问题 | `Graphify` |
| 混合问题 | `Lore first -> Graphify second` |

混合问题的典型例子：

- Lore 里某条原则，在代码里最可能落在哪些入口
- 某个 pitfall 对应的实现，最相关的模块或桥点是什么

这里的重点不是“永远先查哪边”，而是：

- 不要让 Graphify 取代 Lore 的 durable truth
- 也不要让 Lore 假装给出代码拓扑图

### 4）当前验证结论

这轮已经补过可追溯验证：

- Lore 压测：
  - retrieval recall = `1.0`
  - noise = `0.0`
  - startup budget `P50 = 4`，`P90 = 6`
- blind weekly review：
  - decision accuracy = `1.0`
  - destination type accuracy = `1.0`
- multi-session weekly review：
  - absorption = `1.0`
  - `absorbed_to_completion = 0.8`
- knowledge-plane routing：
  - process → OpenSpec
  - Lore rule/boundary → Lore
  - code topology → Graphify
  - mixed question → Lore then Graphify

这意味着现在的 Lore wiki 还能用，而且仍然是主干；Graphify 是补结构证据，不是替代物。

### 5）Graphify 具体怎么用

如果只说“Graphify 是代码结构证据层”，还是太抽象。实际用法要记三件事：

#### 先建图，再提问

```bash
graphify update .
graphify query "你的问题"
```

- `graphify update .`：重建当前仓库的代码图
- `graphify query "..."`：基于图回答结构问题，而不是重新扫全仓库

#### 什么情况下用 `update`

这些情况要先跑一次：

- 代码结构刚变过
- 新增了模块/脚本/入口
- 你怀疑当前图已经过期

一句话：**仓库结构变了，就先 `update`。**

#### 什么情况下用 `query`

这些情况优先用：

- 想找入口文件
- 想看某个能力连到哪些节点
- 想找桥接点、邻接点、可能的调用路径

一句话：**你要问结构问题，就用 `query`。**

#### Lore 和 Graphify 组合时怎么走

现在不是 Lore 被 Graphify 替代，而是两者组合：

1. 先用 Lore 定场景
   - 这是什么问题
   - 命中哪条 principle / pitfall / project context
   - 边界是什么
2. 再用 Graphify 找代码证据
   - 入口在哪
   - 相邻节点有哪些
   - 哪条路径最值得先读

也就是说：

- **规则、边界、经验 → 先看 Lore**
- **入口、连接、结构路径 → 再看 Graphify**

#### 一个最小例子

如果用户问：

> “platform-admin team scope 这条规则现在代码里最可能落在哪？”

正确顺序不是只跑 `graphify query`，而是：

1. 先从 Lore 命中相关 principle / pitfall，确认这是 team-scope boundary 问题
2. 再跑：

```bash
graphify query "platform-admin team scope 相关入口、桥接点、相邻节点有哪些？"
```

这样输出才不会漂成“代码图很完整，但没有规则语境”。

---

## 安装入口

现在有两种安装入口：

### 0）Codex 原生插件市场安装（CR Agent）

`account-skills` 现在提供 Claude/Codex 共用的插件市场入口：

```bash
codex plugin marketplace add /mnt/d/skills/account-skills
codex plugin add account-cr-agent@account-skills
```

仓库发布到 GitHub 后，可替换为：

```bash
codex plugin marketplace add your-org/account-skills
codex plugin add account-cr-agent@account-skills
```

`account-cr-agent` 是独立 CR Agent 插件包，只包含 `cr-agent`、CR worker
skills 和 `release-diff-cr` 证据提供者；不把 `channel-integration`、
`ddl-review`、`code-review`、`api-inventory` 等其他账号技能混进安装范围。

### 1）对话式安装（推荐）

用户直接说：

- `帮我把这套规范装到 Codex`
- `给当前项目装 Cursor 规则`
- `先预览最小版`
- `装团队版`

AI 应直接识别：

- 平台：`Codex` / `Cursor`
- 模式：`dry-run` / `apply`
- 范围：`minimal` / `team`

然后直接执行，不需要用户切去 shell 或 `/plan`。

补充：如果安装请求还包括共享 Lore Wiki，不应只回 README，而要继续保持 AI chat 安装路径：

- Codex / Cursor 配置由 `governance-install` 处理
- 共享 wiki repo 的初始化 / 迁移由 `lore-bootstrap` 处理
- Lore Wiki 路径必须显式确认；当前环境默认推荐 `/mnt/d/team-lore`
- 安装结果里必须回报：`selected install path`、`repo root`、`wiki root`

### 2）一键安装脚本（Codex shell 入口）

仓库里新增了：

```bash
scripts/install-codex-governance.sh
```

### 解决什么

Codex 新项目首次安装时，最麻烦的是这些文件不知道怎么铺：

- 根目录要不要放 `AGENTS.md`
- `rules/`、`agents/`、`skills/` 应该怎么分层
- 老项目如果已经有同名文件，怎么避免直接覆盖
- 想先预览安装结果，怎么做 dry-run

这个脚本就是把当前仓库这套规范包复制到目标 Codex home，并自动备份目标目录已有的同名文件。
现在默认安装目标是 `~/.codex`；全局基线安装为 `~/.codex/AGENTS.md`，repo 模板安装为 `~/.codex/AGENTS.repo-template.md`，`rules/`、`agents/`、`skills/` 会逐文件合并进去。

### Cursor 直接安装产物

如果目标是 Cursor，不应该只给 README 说明，还应该直接落这些文件：

- `.cursor/rules/codex-governance.mdc`
- `.cursor/mcp.json`
- `.cursorrules.example`

### 用法

```bash
# 默认安装到 ~/.codex
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh

# 安装到指定 Codex home
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh --target ~/.codex

# 只预览，不实际写文件
bash /path/to/account-skills/codex-integration-kit/scripts/install-codex-governance.sh --target ~/.codex --dry-run
```

### 安装行为

| 项目 | 行为 |
|------|------|
| 全局基线 | 安装为 `~/.codex/AGENTS.md` |
| repo 模板 | 安装为 `~/.codex/AGENTS.repo-template.md` |
| `rules/` | 逐文件复制到 `~/.codex/rules/`，目标同名文件先备份 |
| `agents/` | 逐文件复制到 `~/.codex/agents/`，目标同名文件先备份 |
| `skills/` | 逐文件复制到 `~/.codex/skills/`，目标同名文件先备份 |
| dry-run | 只打印将要复制/备份的路径，不写文件 |

### 本地安装验证

本轮已经做过一次本地安装验证，不直接污染真实 `~/.codex`：

- dry-run 目标：`/tmp/codex-kit-verify`
- 实际安装目标：`/tmp/codex-kit-verify`
- 已确认产物：
  - `AGENTS.md`
  - `AGENTS.repo-template.md`
  - `rules/common/*`
  - `rules/python/*`
  - `rules/java/*`
  - `rules/web/*`
  - `agents/*.md`
  - `skills/database-migrations/SKILL.md`
  - `skills/jira-integration/SKILL.md`

安装验证过程中还发现并修复了一个实际问题：

- `scripts/install-codex-governance.sh` 原先带 CRLF 换行，bash 会报 `set: pipefail\r: invalid option name`
- 已改为正常 LF，之后 dry-run 和实际安装均通过

---


## req-agent 需求工作流安装包

本仓库现在包含 `installers/req-agent/`，用于把 `req-agent` 需求分析工作流安装到其他仓库。

核心安装命令：

```bash
npm install -g /path/to/account-skills/installers/req-agent
req-agent-install /path/to/target-repo --mode codex-repo --update-agents --verify
```

发布到 npm 后可使用：

```bash
npm install -g @account-skills/req-agent-installer
```

安装内容包括 `.codex/skills/req-*`、requirements helper scripts、`requirements/config/requirements-taxonomy.yaml`、验证测试、OpenSpec 审计文档和 `docs/req-agent/AGENTS_SNIPPET.md`。`req-agent` 是普通用户入口；`req-intake`、`req-scope`、`req-stories`、`req-acceptance`、`req-handoff` 只作为 worker/debug skill 使用。

---

## cr-agent 代码评审工作流

本仓库现在也补了 `cr-agent` 代码评审入口，用来把原来分散的 `code-review` 和 `release-diff-cr` 串成一个 CR 生命周期。

它解决的不是“多一个报告模板”，而是把 CR 拆成可阻断的工作流：

| 环节 | 负责什么 |
|------|----------|
| `cr-agent` | 普通用户入口，先判断 CR 类型，再路由 worker |
| `cr-intake` | 归一化仓库、CR 类型、比较范围、Jira/测试/准生产/回滚等材料 |
| `cr-branch-governance` | 检查 release/merge/hotfix 的基线、分支范围、主干直提、UAT 覆盖 |
| `cr-diff` | 复用 `release-diff-cr` 产出确定性 diff 证据，但不做最终门禁 |
| `cr-scope` | 从 diff 触发技术审查维度，例如证书、`keyType`、加解密、DB、安全、配置 |
| `cr-technical-review` | 做技术 CR，覆盖鲁棒性、安全性、结构、技术债、兼容性等问题 |
| `cr-evidence` | 检查 Jira、测试、准生产、回滚、影响方确认等交付证据 |
| `cr-issues` | 统一登记所有 CR findings，避免报告和门禁各算各的 |
| `cr-gate` | 只根据 issue registry 和证据输出 `allow` / `conditional` / `blocked` |
| `cr-report` | 只负责中文报告渲染，不重新计算门禁 |
| `cr-replay` | 用历史事故形状做行为回放，确认下次能触发同类阻断 |

CR Agent 的报告现在有两个硬边界：

- 如果被审仓库已有 `CR/` 目录，报告、gate 结论、issue registry 和 TODO 必须落到仓库既有 CR 记录位置，不能只停留在聊天里。
- 技术审查不能只报第一个阻塞点；技术债、坏味道 / Sonar 类问题、安全风险、业务风险、测试证据缺口、UAT/回滚/原始报文证据缺口都要进入 `cr-issues` 或报告证据区。
- 技术质量评分不能只给分，必须给扣分依据，并关联 CR-ID、文件/命令证据或明确说明不适用；缺少评分依据时，report/gate/full CR 不能算完成。
- 可维护性不能只看格式和命名，要覆盖变更规模、owner、模块边界、复杂度、重复、死代码、耦合、配置/profile 隔离、回滚/拆分性、测试、文档和 runbook。
- 可观测性不能只看是否有日志，要覆盖 logs / metrics / traces、dashboard、实时告警、报表或批处理告警、SLI/SLO 或业务 KPI、correlation id、脱敏、告警 owner、阈值、路由和 runbook。

这里的关键边界是：

- `release-diff-cr` 是 `cr-diff` 的证据 provider，不是完整 CR 生命周期控制器
- `code-review` 是 `cr-technical-review` 和 `cr-report` 的第一版 provider，不拥有最终 gate
- release CR 必须用“上一版线上主线版本 -> 本次生产目标”来比较，不能拿 feature branch diff 冒充 release gate
- 主干直提、生产 commit 未被准生产/UAT 证据覆盖、阻塞级 CR 扫描问题，都必须进入 `cr-issues` 并驱动 `cr-gate`
- Sonar / 安全扫描如果没有实际执行，只能登记为证据缺口，不能把静态阅读包装成扫描结论
- 涉及 release、支付、清算、MQ、调度、报表、数据路由、外部集成或生产运维路径的高风险变更，如果没有可观测性证据和告警闭环，`cr-gate` 必须阻塞。
- 参考外部实践时只吸收可执行约束：GitHub required checks / code owners / code scanning alerts 对应门禁、owner 和告警追踪；OpenTelemetry 的 traces/metrics/logs 对应遥测信号；SRE 的 dashboard、黄金信号和 SLO 告警原则对应运行态观测和告警质量。

这次也修复了一个真实门禁缺口：`release-diff-cr` 已经能识别阻塞级 CR 扫描问题时，最终 `risk.gate_conclusion` 也必须同步为“阻塞上线”，`--fail-on blocker` 必须返回失败退出码。

`mandao-customer` 的证书 `keyType` 事故被沉成 replay fixture：静态 diff 能识别 `keyType` 变化、主干直提、证据缺口这些 CR 风险；但不能单独证明具体下游老前置解密事故，仍需要业务兼容性和验证证据。

---

## 当前验证结论

- `AGENTS.md` 能索引到所有新增 rules / agents / skills
- 三个 skill 都已经具备清晰的触发与边界说明
- 模板中的上下文恢复顺序、git truth-source 约束、skill reference-card 结构已经对齐
- starter skill 已经标明“本地化后再接入治理”，避免把外部示例直接当仓库事实
- 行为资产的 TDD / 评估验证现在要求落到仓库文件里可追溯，不能只留在聊天记录
- 安装脚本已完成 `/tmp/codex-kit-verify` 的 dry-run + 实际安装验证
- 对话式安装已补齐 Codex 与 Cursor 两侧的落地产物与追溯记录
- Lore Wiki 已拆出独立 `lore-bootstrap` skill，安装/迁移不再混进运行态 `lore`
- Lore Wiki 安装现在把“路径选择”视为安装合同的一部分，而不是隐式实现细节
- `lore-bootstrap` fixture 验证已覆盖：fresh install、existing repo bootstrap、legacy migration，以及默认路径显式输出
- 当前环境的推荐共享 wiki 路径为 `/mnt/d/team-lore/wiki`，不再默认写入 `~/team-lore`
- Lore / Graphify 的边界已经补齐：OpenSpec 是过程层，Lore + Graphify 是知识层
- Graphify 的 Codex 集成已落到：
  - `AGENTS.md`
  - `.codex/hooks.json`
- 知识层路由验收已经明确：
  - 过程问题不应错误命中 wiki 或 graph
  - 规则/边界问题由 Lore 承担
  - 代码结构问题由 Graphify 承担
  - 混合问题按 `Lore first -> Graphify second`
- CR agent 已补成独立入口和 worker 包，`release-diff-cr` / `code-review` 被标注为 provider，不再混同为生命周期控制器
- release-diff 阻塞门禁已补测试：阻塞级 CR 扫描问题会把 `gate_conclusion` 同步为“阻塞上线”，`--fail-on blocker` 返回失败退出码
- CR replay 已覆盖 `mandao-customer` 证书 `keyType` 场景，并明确静态 diff 的证明边界

### 飞书同步门槛

从现在开始，下面这些改动不应再被视为“只改仓库”：

- `codex-integration-kit/**`
- `skills/**`
- governance 规则
- 安装流程
- Lore / Graphify 用法与边界

这些都应视为 Feishu-facing share 的工作面。

也就是说：

- **如果这些内容发生 material change，而 `docs/feishu-codex-governance-share.md` 没同步，这次工作就不应算 complete。**

为了不再只靠记忆，这个仓库已经补了 repo-local 执行门槛：

- 校验脚本：`codex-integration-kit/scripts/check-feishu-sync.sh`
- 可选 hook：`.githooks/pre-commit`
- 启用方式：`git config core.hooksPath .githooks`

这个门槛只对当前仓库生效，不会污染全局 `~/.codex`。

另外，这次也把“飞书文档怎么写”沉成了一张全局可安装 skill：

- `skills/feishu-doc-writing/SKILL.md`

它专门约束这些高频失败：

- 知识密度过高时不拆文档
- 更新一个文档却不联动上下文相关页
- 已经继续写了但还留着 TODO / 未完成提示
- 行文只求完整，不考虑人读时的渐进体验
- 一个文档改成新 framing 了，其他子文档和图还停留在旧 framing
- 页面像“聊天记录整理稿”，不像稳定文档
- 明显适合做比较 / 指标 / 路径说明的内容却没有改成表格
- 飞书已经更新，但没有回读远程结果确认标题、版式和图文是否真的生效

同时补了一条很关键的路由边界：

- 如果用户只是要“写一篇飞书分享稿”，可以只用 `feishu-doc-writing`
- 如果用户要“创建/更新真实飞书文档”，必须同时配合 `lark-doc`
- 也就是：
  - `feishu-doc-writing` 管内容结构和行文质量
  - `lark-doc` 管真实文档的 CLI 读写

如果还需要图，不应临时手搓：

- 高信息密度总结图 / 一图流 / 长图 HTML → 配 `xiaohongshu-retro-grid-content`
- 可编辑的分层图 / 架构图 / 流程图 → 配 `lark-whiteboard`

现在这张 skill 还补了一个更硬的发布门槛：

- 先检查第一页是否便宜
- 再把 list-shaped 内容尽量转成表格
- 再确认图是否真的在帮助理解，而不是重复文字
- 最后回读远程 Feishu 文档，确认最终可见结果和本地意图一致

---

## 建议下一步

1. 先拿这份规范包给一个新项目做首次安装试跑
2. 再决定哪些 rules 需要上升成 git hooks / CI 的硬拦截
3. 如果团队要正式推广，再补一版“最小安装包”和“可选增强包”的安装策略
