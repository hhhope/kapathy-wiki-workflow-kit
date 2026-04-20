# AI Chat 一键安装工作流方案

## 一、要解决的问题

当前仓库已经有一套能跑起来的 AI workflow，但它分散在不同层里：

- `AGENTS.md`：治理边界、执行约束、OpenSpec 规则
- `.codex/skills/`：项目级 workflow skill 和 principle skill
- `wiki/`：长期知识、操作说明、样例链路

这些内容在仓库内可用，但还没有被整理成一个可复制、可分享、可安装到不同 AI chat 环境的统一方案。

## 二、为什么不能只做一个 skill

因为三端的运行面不同：

- Codex 更适合使用 repo instruction 入口和本地 skill 目录
- Cursor 更偏向规则文件入口
- Claude 更偏向 memory / command 入口

所以这件事不能被讲成“一份 skill 文件原样装到三端”。如果这样做：

- 运行时能力会被误导
- 后续维护会漂移
- 团队会误以为三端支持完全对齐

## 三、我们的方案

我们把它定义成：

`AI Chat Workflow Installer`

这不是单一 skill，而是一个安装器工作流。

它有三层：

### 1. Canonical workflow source

仓库内部唯一真源，定义：

- 治理边界
- workflow 单元
- 适配规则
- 验证要求

### 2. Platform adapters

针对不同 AI chat 输出适配结果：

- Codex adapter
- Cursor adapter
- Claude adapter

### 3. Share artifact

生成一份对外可讲、可复用的说明材料，用于飞书分享、培训和交接。

## 四、三端映射

### Codex

主入口：

- `AGENTS.md`
- repo-local `.codex/skills/`

要保留的重点：

- repo 默认治理边界
- workflow skill 路由
- OpenSpec / ADR / wiki 分层

### Cursor

主入口：

- `.cursor/rules/`

兼容入口：

- 必要时可引用 `AGENTS.md`

要保留的重点：

- 把 workflow 语义转成 rules 可消费形态
- 明确哪些能力是映射出来的，不是假装原生支持

### Claude

主入口：

- `CLAUDE.md`
- command / memory entry

要保留的重点：

- 把 workflow 语义转成 Claude 可执行的长期记忆和命令结构
- 不直接复制 Codex 的 skill 目录

## 五、为什么这套方案更稳

- 仓库是唯一真源，不靠聊天历史维持规则
- 多端适配可控，避免维护三份独立说明
- 分享、培训、onboarding 有统一说法
- 后续如果增加新的 AI chat 平台，只要加 adapter，不必重写全部 workflow

## 六、边界和非目标

这套方案不是：

- 一个万能 prompt 包
- 一个 raw skill 文件直接复制到所有平台
- 一个跳过 OpenSpec 和 repo 治理边界的捷径

这套方案的边界是：

- 真源在仓库里
- 安装器只负责映射和落地
- 分享文档只负责解释，不取代运行时规则

## 七、安装后怎么验证

至少检查五件事：

1. 目标平台入口文件是否真的生成
2. repo 默认治理边界是否还在
3. workflow 单元是否能被目标平台识别
4. OpenSpec / ADR / wiki 分层是否被保留
5. 是否有任何被静默降级却还被说成“安装成功”的地方

## 八、下一步

- 定义 canonical source 的正式结构
- 产出 Codex / Cursor / Claude 三端 adapter
- 增加安装后验证清单
- 再根据需要补真正的一键安装命令或安装 skill
