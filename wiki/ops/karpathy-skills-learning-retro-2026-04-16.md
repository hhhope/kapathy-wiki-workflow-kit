# Karpathy Skills 学习复盘 2026-04-16

## 观察对象

- 外部仓库：`forrestchang/andrej-karpathy-skills`
- 入口设计：一个全局 `CLAUDE.md` + 一个极薄的 `skills/karpathy-guidelines/SKILL.md`
- 目标：用最少规则压制最常见的 LLM 编码错误

参考：

- `https://github.com/forrestchang/andrej-karpathy-skills`
- `https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md`
- `https://github.com/forrestchang/andrej-karpathy-skills/blob/main/EXAMPLES.md`

## 这个仓库最突出的特点

### 1. 原则极少，但打得很准

它没有铺很多流程，而是把常见失误压缩成 4 条：

- Think Before Coding
- Simplicity First
- Surgical Changes
- Goal-Driven Execution

这 4 条几乎都直接对应模型最常犯的错：

- 自作主张补假设
- 过度设计
- 顺手改无关内容
- 没有验证闭环

优点不是“全”，而是“短、硬、记得住”。

### 2. 它在赌一件事：高频原则比长流程更容易真正生效

它的 `CLAUDE.md` 只有几十行，但每一条都很像“行为刹车片”。

这类规则的优势是：

- 高频触发
- token 负担小
- 更容易被模型持续记住
- 不依赖复杂路由

它本质上是一个“全局认知校正器”，不是一个复杂 workflow 系统。

### 3. 它把示例和主规则分层了

主规则很短，例子放到 `EXAMPLES.md`。这个分层值得学：

- 主规则负责约束
- 示例负责校准
- 规则本体不被例子撑胖

### 4. 它非常重视 anti-pattern，而不只是 best practice

这点很强。它不是只说“应该怎样”，还明确展示：

- 模型通常会怎么错
- 这种错为什么看起来“像是合理工程实践”
- 但为什么在当前时机会变坏

这种写法对模型约束比纯正面规范更有效。

## 我们现有体系哪里更强

### 1. 我们的治理边界更完整

相较这个外部仓库，我们已经有更成熟的分层：

- 全局 `~/.codex/AGENTS.md`：健康检查、git 真值源、OpenSpec 边界
- repo `AGENTS.md`：项目默认 workflow
- `.codex/skills/`：项目级正式 skill
- `~/.codex/agents/*.md`：显式角色模板

也就是说，我们不是只有“行为原则”，还有：

- 发布机制
- discoverability 约束
- archive review
- 项目级 skill / draft / agent template 边界

这层是外部仓库没有覆盖的。

### 2. 我们更适合复杂仓库和多流程材料处理

这个 repo 的材料流转、飞书同步、source/ops/report 分层、OpenSpec 生命周期，都不是一份短 `CLAUDE.md` 能兜住的。

外部仓库适合：

- 通用 coding agent
- 少流程、高通用性场景

我们当前体系适合：

- 多层规则
- 多输出 contract
- 项目内强约束协作

### 3. 我们已经在 agent 与 skill 分工上走得更清楚

现在的边界已经比较健康：

- workflow 复用交给 skill
- 角色视角交给 agent
- repo 默认行为由 `AGENTS.md` 和 OpenSpec 固化

这是我们最近补出来的强项，不能为了追求“简单”再退回成混用机制。

## 最值得学的地方

### 1. 给高频通用行为再压一层“短原则卡”

我们现在规则很强，但有些地方偏“治理完备”，不够“瞬时可记忆”。

最值得吸收的是这种表达方式：

- 用极少数高频原则覆盖大部分错误
- 一条原则只打一个失误面
- 让规则先变成刹车，再变成流程

对我们最有价值的，不是把他们整套搬进来，而是补一层更短的“高频行为原则卡”。

### 2. 把 anti-pattern 当成一等公民

我们现在已经有不少正向规则，但“模型常见错法样例库”还不够系统。

这仓库的写法提醒了一点：

- 模型不是只需要知道正确答案
- 模型还需要知道“哪些看起来专业、其实是错时机的做法”

尤其适合补到：

- skill reference
- governance retro
- agent reviewer 模板

### 3. 让主规则更短，把例子外置

这个思路适合我们优化 skill 仓库：

- `SKILL.md` 保持触发条件、关键约束、边界
- 长示例、反例、演化样例放 `references/`
- 避免主 skill 变成厚重手册

## 不该照搬的地方

### 1. 不能退化成“只有一个全局文件”

我们的场景不是通用 coding-only 仓库。

如果把很多 repo-specific workflow 重新压回一个总文件，会丢失：

- 项目级 discoverability
- 可发布路径
- 场景 skill 路由
- repo contract 的局部性

所以该学的是“表达密度”，不是“收缩成单文件架构”。

### 2. 不能用通用原则替代 workflow contract

像会议纪要、材料处理、OpenSpec archive review 这类事情，必须有明确 contract。

短原则能防错，但不能替代：

- 结构化输出模板
- 触发边界
- 交付顺序
- 发布与归档规则

### 3. 不能让 agent 模板重新承担默认路由职责

外部仓库更偏全局行为调教，我们这边已经明确：

- agent template 是显式角色
- skill 才是 workflow 复用面

这条边界不应该回退。

## 对我们 AGENTS.md 和技能仓库的具体启发

### 对 AGENTS.md

可以继续加强的，不是再加更多长条款，而是补一层更短的高频原则，例如：

- 不替用户脑补关键歧义
- 不为未来需求提前设计
- 不顺手改无关代码或文档
- 没有验证就不算完成

这层最好是“总开关式原则”，不是替代现有规则。

### 对 skill 仓库

可以演进成两层：

- `workflow skills`
  负责具体场景，如 meeting-note、material-collaboration
- `principle skills`
  负责高频认知校正，如 simplicity、surgical-changes、clarify-before-act

我们目前 workflow skill 已经比之前健康，但 principle skill 还偏少。

### 对 agent 模板

我们现在的 agent 模板方向是对的，但还能更克制：

- planner/reviewer 继续聚焦角色职责
- 不在 agent 里重复 repo workflow
- 多把高频 anti-pattern 前置成 reviewer 观察点

## 当前结论

一句话总结：

`andrej-karpathy-skills` 强在“用极少原则矫正常见错误”，我们强在“把复杂 repo workflow 做成可发布、可路由、可归档的治理系统”。下一步最值得学的不是变成它，而是在我们现有体系上补一层更短、更硬、更 anti-pattern oriented 的通用原则层。

## 可继续跟进的方向

- 是否为全局或项目级治理补一张“高频行为原则卡”
- 是否把常见 anti-pattern 样例沉成独立 reference 页面
- 是否把 `principle skill` 和 `workflow skill` 明确分层
