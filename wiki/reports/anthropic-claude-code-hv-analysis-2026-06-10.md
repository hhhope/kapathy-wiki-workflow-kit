---
layer: reports
domain: agentic-collaboration
title: "从 Claude Code 到 Claude Cowork：Anthropic 如何把强模型推进真实工作环境"
status: draft
created: 2026-06-10
source_type: research-report
---

# 从 Claude Code 到 Claude Cowork：Anthropic 如何把强模型推进真实工作环境

> 研究时间：2026-06-10 | 研究对象类型：产品 / 公司路径 | 方法：横纵分析法 | 稿件状态：内部调研稿

## 一句话定义

Claude Code 不是一个普通编程工具，而是 Anthropic 用来验证「强模型如何进入真实工作环境」的旗舰项目；Claude Cowork 则说明，这条路径正在从研发现场外溢到更广的知识工作现场。

这份报告不做三家公司横评，也不改 PPT。它只回答一个问题：

**Anthropic 为什么会从 Claude 走到 Claude Code，再走到 Claude Cowork？这条历史线暴露了它对未来 AI 组织协作方式的什么判断？**

## 核心判断

Anthropic 的公开使命不是做聊天产品，也不是做办公软件。它把自己定义为 AI safety and research company，目标是构建可靠、可解释、可引导的 AI 系统。Dario Amodei 在《Machines of Loving Grace》里也没有把未来强 AI 描述成一个更好用的问答界面，而是描述为能使用文本、音频、视频、鼠标键盘、互联网等接口，能像聪明员工一样接收长任务并自主推进的系统。

用这个尺度看 Claude Code，它的重要性不在「会写代码」。代码只是第一个足够适合强模型行动化的真实工作场。

研发现场有几个天然优势：文件可读，工具可调用，测试可运行，版本可追溯，错误可复现，结果可审查。这让 Anthropic 能在一个相对可控的环境里，把 Claude 从「能回答」推向「能行动」。

所以 Claude Code 是一次组织实验：当模型进入真实工作链路后，人、模型、文件、工具、权限、测试、评审、记忆之间应该怎样重新分工。

Claude Cowork 的出现，是这条实验线的第二个信号。Anthropic 官方说明里提到，Marketing、Data 等非技术团队开始绕过普通对话界面去使用 Claude Code，因为它能处理复杂、多步骤任务，例如建工具、挖数据。Cowork 正是把这种行动能力做成更适合知识工作者的产品形态。

我的判断是：Anthropic 的产品演进不是从「聊天」走向「办公」，而是从「强模型」走向「受控行动」。Claude Code 和 Claude Cowork 是这条路径上两个可观察的大事件。

## 研究方法：李想访谈是因子，不是结论

李想和罗永浩访谈里最有价值的部分，不是「人体器官」这个比喻本身，而是它提供了一个观察 AI 公司的方法。

传统公司可以按职能理解：研发、产品、销售、运营、财务、人力。AI 公司不能只这么看。更有效的看法是：它有没有在构建一个能工作的智能体，这个智能体有哪些器官，哪些器官还缺，哪些器官已经变成产品。

按这个方法看 Anthropic：

| 观察层 | Anthropic 对应物 | 说明 |
|---|---|---|
| 大脑 | Claude / frontier model | 理解、推理、规划、生成能力 |
| 手脚 | Claude Code / Claude Cowork | 进入真实环境执行任务 |
| 感官 | 代码库、文件、本地应用、企业数据、连接器 | 让模型看到真实工作对象 |
| 记忆 | CLAUDE.md、auto memory、项目知识 | 让经验跨会话保留 |
| 神经系统 | hooks、subagents、settings、MCP、workflow | 让任务触发、分工、权限和工具调用可组织 |
| 免疫系统 | RSP / ASL、权限、人工确认、评测、安全研究 | 控制模型行动风险 |

这个框架不是为了写漂亮类比，而是为了避免报告滑成产品功能清单。每个新产品和新机制，都要问它补的是哪一个器官，它改变了哪条协作链路。

## 纵向分析：Claude Code 的历史线

### 1. Anthropic 的起点不是产品，而是强 AI 的安全部署问题

Anthropic 官网对自己的描述很直接：它是 AI safety and research company，构建 reliable、interpretable、steerable 的 AI systems。公司团队公开分为 Research、Policy、Product、Operations，这个划分本身就说明，Anthropic 不是把安全、政策和产品分开叙事，而是把它们放在同一条部署链路里。

RSP（Responsible Scaling Policy）也是这条线的一部分。2023 年版本提出 AI Safety Levels，用模型能力和风险等级绑定安全、安保、运营要求。2026 年 v3.0 后，具体政策有调整，也受到外界质疑，但它仍然暴露了 Anthropic 的基本问题意识：模型能力越强，行动能力越高，部署越不能只靠产品增长逻辑。

这决定了 Claude Code 的解读方式。

如果把 Claude Code 当成「更强的代码助手」，会低估它。如果把它放回 Anthropic 的使命线里，它更像一个实验场：强模型怎样进入真实工作环境，怎样被限制、被观察、被评估、被人接管。

### 2. 为什么第一个突破口是研发现场

Claude Code 官方产品页给出的定义很清楚：它能读代码库、跨文件修改、运行测试，并交付已提交代码。它还强调自己不是 autocomplete，而是 project-level 的 agentic coding system。

这句话背后有两个关键点。

第一个点，代码场景天然有反馈。

模型写错一段话，很多时候只能靠人判断。模型写错一段代码，测试、编译、运行、日志、CI 都能给反馈。研发现场里存在大量可执行、可复现、可回滚的检查机制。对一个想研究强模型行动能力的公司来说，这是最好的试验环境。

第二个点，研发现场天然有边界。

代码库、权限、分支、PR、review、CI、release，本来就是一套边界系统。Claude Code 进入的不是空地，而是一个已经被工程行业打磨几十年的受控行动环境。Anthropic 选择终端和代码库，不只是因为程序员爱用命令行，而是因为这里最容易把「行动」变成可追踪的行动。

所以 Claude Code 的真正问题不是「AI 能不能写代码」，而是「一个强模型在现实工作环境里，怎样安全地看、改、验证、交付」。

### 3. 内部扩散：从工程工具变成组织协作样本

Anthropic 的《How Anthropic teams use Claude Code》是目前最重要的公开材料之一。它不是讲产品功能，而是讲公司内部团队怎么用。

文章里提到的团队包括 Infrastructure、Product Engineering、Product Design、Security Engineering、Growth Marketing、Legal 等。数据科学家用它理解代码库和数据 pipeline；产品工程用它快速定位要看的文件；设计团队用它写测试和自动化 PR 评论；营销团队用它批量生成广告变体；法律团队甚至做了内部 phone tree 原型。

这些例子最容易被误读成「非技术岗位也会写代码了」。这句话太浅，也容易错。

更准确的说法是：Claude Code 让非工程岗位能更早地产出可运行、可检查、可讨论的 artifact。这个 artifact 可能是脚本、原型、数据分析、自动化流程、文档处理器，也可能只是一个能让工程师继续接手的工作样本。

专业判断没有消失。工程责任没有消失。产品、设计、法律、营销也没有变成工程部门。改变的是协作链路：过去他们只能把想法写成需求、文档、表格或会议纪要，现在他们可以把一部分想法提前变成可执行对象。

这就是组织边界的变化。

旧边界是岗位边界：谁写需求，谁写代码，谁测试，谁上线。新边界是行动边界：哪些工作可以交给 agent 执行，哪些必须由人判断，哪些需要系统评估，哪些要进入权限控制。

### 4. Claude Cowork：研发现场之外的第二次外化

Claude Cowork 官方页写得很直接：它处理任务，给它一个目标，它会在你的电脑、本地文件和应用里工作，然后返回完成的交付物。页面还解释了它为什么出现：Anthropic 观察到非技术团队开始绕过 Claude 的对话界面去用 Claude Code，因为 Claude Code 更适合复杂、多步骤工作。

这段材料非常关键。

它说明 Cowork 不是随手做出来的「低代码版 Claude Code」。它是一个内部行为模式被产品化的结果。Anthropic 先在研发现场验证了模型的行动能力，再看到这种行动能力被非技术团队借用，于是把它从终端和代码库迁移到桌面、文件夹、日常应用和知识工作。

这条路径很像一个能力的迁徙：

Claude 证明模型能理解。

Claude Code 证明模型能在受控工程环境里行动。

Claude Cowork 证明这种行动模式正在寻找更通用的工作环境。

这不是「聊天界面升级」。恰恰相反，Cowork 的出现说明普通对话界面不够了。强模型要承担真实任务，就不能永远停留在一问一答里。它需要进入文件、应用、工具链、权限和交付物。

### 5. 记忆、权限、hooks、subagents：不是功能堆叠，而是行动系统的基础设施

Claude Code 文档里有几类机制值得放在一起看。

CLAUDE.md 和 auto memory 解决的是记忆问题。官方文档说，每个 Claude Code session 都从新的 context window 开始，所以需要 CLAUDE.md 和 auto memory 承载跨会话知识。CLAUDE.md 是人写的规则和项目上下文，auto memory 是 Claude 根据纠正和偏好自动记下的学习。

settings 和 permissions 解决的是组织边界问题。配置分 managed、user、project、local 等 scope。managed scope 用于组织级安全政策和合规要求，project scope 用于团队共享配置。这不是普通软件设置，而是把「谁能规定什么」写进产品结构。

subagents 解决的是分工问题。官方文档强调 subagents 有自己的 context window、system prompt、工具访问和独立权限，用于专门任务和上下文管理。这让复杂工作从一个 agent 一口气做到底，变成不同角色分担探索、计划、实现、验证。

hooks 解决的是生命周期控制问题。它们能在 Claude Code 的不同事件点自动执行命令、HTTP endpoint 或提示逻辑，包括工具调用前后、权限请求、任务创建完成、子 agent 启停、文件变化等。换成组织语言，hooks 是行动系统的神经反射。

这些机制合起来，才是 Claude Code 作为旗舰项目的深层价值。Anthropic 不是只在提升模型，而是在补齐模型进入组织工作所需的环境部件：记忆、权限、分工、触发、审计、反馈。

## 横向分析：同行共识只用于验证，不抢主线

### OpenAI：同样把重点放在 agent 可读的工作环境

OpenAI 的 Harness Engineering 文章是最强旁证。它讲的不是某个模型，而是一个 agent-first codebase 如何组织。

OpenAI 的核心经验是：repo 里的知识要成为 system of record，AGENTS.md 不该是一千页手册，而该像目录；真正重要的是结构化文档、测试、脚本、计划、质量记录、评审反馈都能被 agent 读取和验证。文章还强调，当 agent throughput 提升后，人类工程师的工作层级会变化：人优先处理用户反馈、验收标准、结果验证，以及当 agent 失败时补齐工具、文档和 guardrails。

这与 Anthropic 的路径高度相似。区别在于，OpenAI 说的是 Codex 如何改变工程组织，Anthropic 的公开材料更明显地展示了 Claude Code 如何从工程部门扩散到设计、营销、法律、安全等职能。

OpenAI 证明的是行业共识：强模型要真正工作，组织必须把知识、规则、反馈、测试和评审变成 agent 可读、可执行、可验证的环境。

### Seed：能力版图显示「器官化」趋势，但不能当组织图

ByteDance Seed 官方模型页列出 Foundation Models、GenMedia、AI for Science、Robotics 等方向，也列出 LLM、Infrastructures、Vision、Speech、Multimodal Interaction & World Model、AI for Science、Robotics、Responsible AI 等团队方向。

Seed Infrastructures 页面把团队职责写为分布式训练、强化学习框架、高性能推理、异构硬件编译等。

这能支持一个谨慎判断：头部 AI 公司公开能力版图正在从传统职能语言转向能力模块语言。大脑、感官、身体、基础设施、免疫系统这类观察框架，不是凭空套上去的。

但边界也要清楚：这些页面不是字节内部组织架构图，不能把它们写成「字节就是按人体结构设组织」。它只能作为外部共识信号，说明李想访谈里的观察并非孤例。

## 横纵交汇洞察

### 洞察一：Claude Code 的历史地位，不在 coding，而在 action

如果只看产品名，Claude Code 是 coding tool。如果看历史线，它更像 Anthropic 的 action lab。

代码场景有文件、有工具、有测试、有版本、有审查，适合让强模型练习行动。Claude Code 在这个场景里跑通了读、改、测、交付、反馈。然后这套能力被内部非技术团队借用，最后沉淀成 Claude Cowork。

这说明 Anthropic 的真实问题不是「怎样让模型更会写代码」，而是「怎样让模型承担越来越长、越来越复杂、越来越贴近真实世界的任务，同时还能被人监督和组织控制」。

### 洞察二：Anthropic 的安全叙事不是产品外壳，而是行动化的必要条件

当模型只回答问题，安全主要体现在输出内容上。当模型能改文件、跑命令、访问数据、控制应用，安全就变成行动边界问题。

所以 RSP、ASL、permissions、managed settings、human approval、hooks、subagents、evaluation，这些东西不能分开看。它们共同回答一个问题：模型越像一个能工作的个体，组织越需要明确它能看什么、能做什么、何时停下、谁来批准、如何复盘。

这也是 Anthropic 与普通应用公司不一样的地方。它不是在给产品加安全功能，而是在为「强模型进入现实任务」设计行动约束。

### 洞察三：组织变化不是「所有人都会写代码」，而是「专业人更早接近可执行物」

Claude Code 内部案例最容易被传播成一句话：非技术团队也能构建东西。

这句话没有错，但不够深。

真正的变化是，专业人员的输出形态变了。产品不只写需求，可以做可跑原型；设计不只交静态稿，可以做可验证交互；法律不只写意见，可以做内部查询和分流工具；营销不只提创意，可以批量生成、测试、比较方案。

这不是岗位合并，而是交付物提前。

过去组织里的很多工作要经过多轮翻译：想法翻译成需求，需求翻译成设计，设计翻译成代码，代码再翻译成测试和上线证据。Agent 进入后，一部分翻译链条会缩短。人仍然负责判断、责任和品味，但人的判断对象会从「文字描述」更多变成「可执行 artifact」。

### 洞察四：Cowork 是 Claude Code 的外溢，不是旁支

如果报告只讲 Claude Code，会漏掉 Anthropic 路径里最关键的转折。Cowork 说明 Anthropic 已经看到：行动能力不应被锁在研发现场。

研发现场只是第一个训练场。知识工作现场才是更大的外部世界。

但这不等于 Anthropic 要做一个普通企业办公套件。更准确的判断是：Anthropic 正在寻找强模型进入现实组织的通用接口。今天这个接口可能是终端、代码库、桌面、本地文件、应用连接器；明天可能是更长任务、更复杂权限、更深企业系统。

Claude Cowork 的价值不在「给非技术用户一个简单界面」，而在它把 Claude Code 里验证过的行动模式带到了更大的任务空间。

## 未来推演

### 最可能剧本：Claude Code 成为 Anthropic 的行动能力样板

Claude Code 会继续在研发场景里深化：更多 IDE / web / desktop / mobile 入口，更多并行 agent，更多权限配置，更多企业级治理。它不一定永远是营收最大的产品，但很可能长期承担 Anthropic 的样板角色：证明 Claude 不只会说，还能在真实环境里完成工作。

Claude Cowork 会沿着文件、桌面、企业应用、数据连接器继续扩展。它会吸收 Claude Code 的机制，但降低技术门槛。

这个剧本下，Anthropic 的产品线看起来会越来越像「Claude 在不同工作环境中的行动入口」。

### 最危险剧本：行动能力增长快于边界系统成熟

Claude Code 和 Cowork 的风险也来自同一个地方：它们越有用，越会被放进更多真实系统。

如果权限、审计、评估、组织配置跟不上，模型行动能力会把旧流程里的模糊地带放大。错误不再只是一个回答错了，而可能是文件被改错、数据被误读、流程被误触发、责任归属说不清。

Anthropic 的安全叙事在这里会遇到最硬的考验。外界不会只听它怎么讲 RSP，而会看这些行动产品在真实企业环境里如何处理越权、误操作、提示注入、数据泄露、责任归属和复盘。

### 最乐观剧本：Anthropic 找到强模型进入组织的标准形态

最乐观的情况是，Claude Code 与 Claude Cowork 逐渐沉淀出一种标准组织形态：每个任务有目标，有上下文，有权限，有工具，有验证，有审计，有人类决策点，有失败回写。

这会把很多公司的协作方式从「人把信息传给人」改成「工作对象自己携带上下文、约束和验收」。不是人被替代，而是组织里的低效翻译层被压缩。

如果这条路走通，Anthropic 的护城河不只是模型能力，而是它对「强模型如何被组织使用」的系统理解。

## 对现有材料的事实清洗建议

原材料里有几类表述需要谨慎处理：

| 原说法 | 建议处理 |
|---|---|
| “Anthropic 从聊天助手升级为自主工作者” | 改成“Anthropic 正在把强模型推进真实工作环境”，避免低估其 frontier AI / safety 目标 |
| “Claude Code 放弃 RAG” | 降级为局部技术选择；可以说代码场景更依赖实时工具检索和代码库探索，不要写成全公司路线 |
| “constitution.md 是 Claude Code 最高行为准则” | 删除。官方文档核心是 CLAUDE.md、settings、permissions、hooks 等，不应编造 constitution.md 文件机制 |
| “Computer Use 是 Claude Code 最具突破特性之一” | 谨慎区分 Claude Code、computer use、desktop / browser 能力，不要混写 |
| “Agent Teams / Workflow / Auto Memory 的发布时间线” | 逐条验官方 changelog 后再写；未验源的版本时间不进正式报告 |
| “数字生命体 / 数字员工团队” | 少用或不用。容易变成口号，无法承载证据 |

## 结论

Claude Code 的重要性，不是它让程序员快了多少，也不是它把非技术人员变成工程师。

它真正暴露的是 Anthropic 的路线：让强模型从语言能力走向行动能力，再把行动能力放进真实组织环境，同时用记忆、权限、评估、分工、人工确认和安全政策来控制风险。

Claude Code 是这条路线的第一个高密度样本。Claude Cowork 是第二个信号：行动能力正在从研发现场走向知识工作现场。

OpenAI 的 Harness Engineering 和 Seed 的能力版图说明，这不是 Anthropic 单点创意，而是头部 AI 公司共同面对的问题：模型越来越强之后，真正稀缺的不是「再多一个功能」，而是能让模型可靠行动的组织环境。

李想访谈提供的因子在这里闭合了。AI 公司不能只按部门看，要按一个能工作的智能体来看。Anthropic 正在做的事情，就是不断给 Claude 补器官：大脑之后是手脚，手脚之后是记忆、权限、评估和边界。

这条路径还没有完成。正因为没有完成，Claude Code 和 Claude Cowork 才值得持续跟踪。

## 信息来源

- Anthropic Company: https://www.anthropic.com/company
- Claude Code product page: https://www.anthropic.com/product/claude-code
- How Anthropic teams use Claude Code: https://claude.com/blog/how-anthropic-teams-use-claude-code
- Claude Cowork product page: https://www.anthropic.com/product/claude-cowork
- Claude Code memory docs: https://code.claude.com/docs/en/memory
- Claude Code settings docs: https://code.claude.com/docs/en/settings
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Claude Code hooks docs: https://code.claude.com/docs/en/hooks
- Anthropic Responsible Scaling Policy: https://www.anthropic.com/news/anthropics-responsible-scaling-policy
- Anthropic Responsible Scaling Policy v3: https://www.anthropic.com/news/responsible-scaling-policy-v3
- Dario Amodei, Machines of Loving Grace: https://darioamodei.com/essay/machines-of-loving-grace
- OpenAI Harness Engineering: https://openai.com/index/harness-engineering/
- ByteDance Seed Models: https://seed.bytedance.com/en/models
- ByteDance Seed Infrastructures: https://seed.bytedance.com/en/direction/infrastructures
- Repo-local 李想/罗永浩访谈学习记录: `wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md`

## 方法论说明

本报告使用横纵分析法：纵轴追踪 Anthropic 从 Claude 到 Claude Code 再到 Claude Cowork 的事件链；横轴只选 OpenAI 与 Seed 作为同阶段共识验证；交汇处输出对 Anthropic 路径的判断。
