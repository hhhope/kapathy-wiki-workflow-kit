---
title: anthropic claude code cowork baofu payment ppt rewrite
canonical_object: anthropic-claude-code-cowork-baofu-payment-ppt
artifact_type: reader-facing-ppt-draft
layer: sources
domain: product-engineering-collaboration
source_type: ppt-rewrite-draft
created: 2026-06-09
status: review-draft
source_files:
  - /mnt/c/Users/yan/Desktop/1/Claude Code研发调研报告.pptx
source_references:
  - https://mp.weixin.qq.com/s/Cz3fyYoqNdsSUFFtJdij7A
  - https://www.anthropic.com/company
  - https://www.anthropic.com/product/claude-code
  - https://www.anthropic.com/product/claude-cowork
  - https://www.anthropic.com/news/anthropics-responsible-scaling-policy
  - https://openai.com/index/harness-engineering/
  - https://seed.bytedance.com/en/models
ai_generated: true
---

# 从 Claude Code 到 Claude Cowork：Anthropic 如何把强模型推进真实工作场

## Article Intent Contract

| Field | Decision |
|---|---|
| Target reader | 宝付管理层、产品、研发、风控、运营、清结算、合规和数据团队 |
| Reader job | 通过 Anthropic 的产品演进，理解 AI 对支付公司组织协作、流程边界和岗位能力的影响 |
| Core question | Anthropic 为什么从 Claude 走到 Claude Code，再走到 Claude Cowork？这条路径对宝付意味着什么？ |
| Main claim | Anthropic 的关键路径不是工具功能堆叠，而是让强模型在可控边界内进入真实工作场。宝付要学习的不是某个工具，而是“受控 agent + 真实流程 + 审批评测”的组织方法。 |
| Evidence role | 李想访谈提供分析因子；Anthropic 官方材料提供主证据；OpenAI 和 Seed 只做同行共识旁证；宝付启发属于基于支付业务的本地推演。 |
| Non-claims | 不声称 Anthropic 的目标只是企业工具；不声称宝付应直接照搬 Claude Code / Claude Cowork；不使用未核验的泄露路线图或未来版本时间线。 |
| Visual rule | 高密度结构页使用图片模型生成位图视觉；不使用 SVG。 |

## 术语约定

PPT 内尽量减少中英文混写。保留英文的只有公司名、产品名和行业通用核心词：

- Anthropic
- Claude
- Claude Code
- Claude Cowork
- OpenAI
- Seed
- agent
- chatbot
- harness
- MCP
- ASL

其他表达统一中文化：

- 不写“chat 窗口”，写 `chatbot` 或“对话界面”。
- 不写“Agent 化”，写“让 agent 进入流程”。
- 不写“上下文工程”作为大标题，写“工作环境、规则和反馈系统”。
- 不写“AI 操作系统”作为结论，除非只作为类比。

## 建议 PPT 结构

### 01 封面

**标题**

从 Claude Code 到 Claude Cowork：Anthropic 如何把强模型推进真实工作场

**副标题**

以李想访谈为引子，通过公开信源和同行共识，反推宝付的 AI 落地路径

**页面主句**

我们不是复盘一个工具，而是借 Anthropic 的产品演进，看强模型如何被安全、可控地放进真实组织。

**视觉建议**

使用图片模型生成一张横向封面：左侧是研究员/工程师正在指挥多个半透明工作任务流，右侧是支付公司的风控、清结算、商户接入、客诉流程以光线连成工作网络。风格克制、企业研究报告感，不要科幻过度，不要 SVG。

### 02 为什么这份报告要重写

**页面主句**

原 PPT 的问题不是资料不够，而是主线不对：它把 Claude Code 当功能清单讲，少了 Anthropic 如何改变组织协作的故事。

**正文要点**

- 当前 PPT 已有好材料：Claude Code、内部团队使用、记忆、权限、harness、反馈、宝付落地。
- 但这些材料还没有被组织到一条历史线里。
- 本次重写只回答一个问题：Anthropic 为什么一步步把 Claude 从模型能力推进到真实工作场？
- 宝付要看的不是 Anthropic 有哪些功能，而是哪些组织方法可以迁移到支付业务。

### 03 分析因子：李想访谈给了一个看 AI 公司的方法

**页面主句**

李想访谈的价值，不是“人体比喻”本身，而是提醒我们：AI 公司要按“构建一个能工作的智能体”来理解。

**正文要点**

- 传统公司按职能分工：产品、研发、测试、运营、数据、合规。
- AI 公司更像在构建一个能工作的“个人”：需要理解、记忆、工具、执行、反馈、边界。
- 这不是修辞，而是组织边界的变化：模型团队、推理基础设施、agent 产品、安全评测、数据连接、企业流程要围绕一个行动闭环协作。
- 用这个因子看 Anthropic，Claude 不是孤立产品，而是一条能力外化路径。

**证据**

- 本地材料：`wiki/sources/agentic-product-engineering-collaboration-lixiang-luoyonghao-ai-agent-reading-2026-05-18.md`
- 访谈原文源：`https://mp.weixin.qq.com/s/Cz3fyYoqNdsSUFFtJdij7A`

### 04 研究方法：主线、子弹、共识和判断

**页面主句**

本报告不做三家公司横评，而是用公开信源把 Anthropic 的故事讲透。

**正文要点**

- 主线：Anthropic 从 Claude 到 Claude Code，再到 Claude Cowork。
- 子弹：Anthropic 官方使命、产品说明、内部使用案例、Responsible Scaling Policy。
- 共识：OpenAI 的 harness engineering 和 Seed 的能力版图说明头部公司都在把模型能力接入真实工作系统。
- 判断：宝付要建设的不是问答工具，而是受控 agent 参与核心流程的工作体系。

**视觉建议**

图片模型生成“研究链路图”：李想访谈作为放大镜，指向 Anthropic 时间线；OpenAI 和 Seed 作为两侧证据弹药库；终点落到宝付支付流程。不要使用组织架构树。

### 05 Anthropic 的公开使命：不是工具公司叙事

**页面主句**

Anthropic 对自己的定位是 AI 安全与研究公司，目标是构建可靠、可解释、可引导的 AI 系统。

**正文要点**

- 这决定了 Claude Code 和 Claude Cowork 不能只按“效率工具”理解。
- 它们是强模型进入真实任务环境时的产品化实验。
- Anthropic 的关键矛盾是：模型越强，越需要行动能力；行动能力越强，越需要边界、评测和人类控制。

**证据**

- Anthropic company page: `https://www.anthropic.com/company`
- 关键信息：Anthropic 是 AI safety and research company；构建 reliable, interpretable, steerable AI systems。

### 06 第一阶段：Claude 是大脑，但还没有稳定进入工作场

**页面主句**

Claude 解决的是理解和推理能力，但仅有大脑还不能完成真实组织里的复杂工作。

**正文要点**

- chatbot 适合问答、解释、草拟、分析。
- 真实工作需要读取本地文件、理解项目结构、调用工具、执行命令、产出结果、接受审批。
- 从 Claude 到 Claude Code 的跃迁，本质是从“回答问题”走向“完成任务”。

**改写当前 PPT**

- 使用现有第 2、3 页材料。
- 删除“2026 AI 进化更有意义”这类空泛判断。
- 改成“为什么真实工作场比对话界面更关键”。

### 07 第二阶段：Claude Code 让模型进入研发现场

**页面主句**

Claude Code 的核心不是代码补全，而是让 Claude 进入代码库、终端、测试和版本管理。

**正文要点**

- 它能读代码库、跨文件修改、运行测试、处理 CI 失败、提交代码。
- 这让模型第一次从“建议者”变成“执行者”。
- 工程师的工作也随之变化：不再只是逐行实现，而是定义目标、架构、约束、验收标准和风险边界。

**证据**

- Claude Code 官方页：`https://www.anthropic.com/product/claude-code`
- 官方表述包括：reads your codebase、makes changes across files、runs tests、delivers committed code。

**改写当前 PPT**

- 现有第 6 页“从工具到团队”保留，但要写成研发协作变化。
- 现有第 7 页“Prompt -> Context -> Harness”保留，但不要当概念史讲，要落到研发现场的规则、测试、权限、反馈。

### 08 第三阶段：Anthropic 内部扩散，说明 Claude Code 不只是研发工具

**页面主句**

真正重要的证据不是 Claude Code 会写代码，而是 Anthropic 内部多个非工程团队也开始用它完成复杂工作。

**正文要点**

- 数据、产品、安全、营销、设计、法律等团队的使用，说明 agent 能把专业判断转成可运行、可验证的 artifact。
- 非技术团队不是“变成工程师”，而是从需求传递方变成更靠近执行和验证的一方。
- 这改变了组织协作：过去靠文档交接，现在更多靠目标、资料、边界、执行结果和评审闭环。

**证据**

- 当前 PPT 第 4 页已有 Anthropic 内部团队使用案例，应作为重点页。
- 需要最终引用 Anthropic 官方团队使用文章或 Claude 页面相关案例，避免只引用二手描述。

**页面写法**

不要写“大家都能写代码”。写：

> 当 agent 能进入真实工作环境，专业岗位可以更早地产生可运行、可验证、可讨论的 artifact；生产责任、权限边界和专业判断仍由人承担。

### 09 关键大事件：Claude Cowork 的诞生

**页面主句**

Claude Cowork 的出现说明：Claude Code 验证的不是“写代码”，而是“把复杂工作交给 agent 执行”的模式。

**正文要点**

- Anthropic 官方说明：非技术团队如 Marketing 和 Data 曾绕过 Claude 的对话界面，转向 Claude Code，因为它能处理复杂、多步骤工作。
- Claude Cowork 是把这种能力简化后，放到非技术知识工作者的日常工作场。
- 它能围绕目标处理本地文件、应用和多来源信息，返回完成品。
- 这是从研发现场向知识工作现场的扩展。

**证据**

- Claude Cowork 官方页：`https://www.anthropic.com/product/claude-cowork`
- 官方信息包括：give it a goal、works on your computer、local files、applications、return a finished deliverable。

**注意**

不要把 Cowork 写成“办公软件”。它更像 Anthropic 在验证：强模型如何在更广泛的现实工作中承担执行循环。

### 10 从历史看未来：Anthropic 的路径不是功能堆叠

**页面主句**

Claude、Claude Code、Claude Cowork 不是三个孤立产品，而是一条能力外化路径。

**正文结构**

| 阶段 | 能力变化 | 组织含义 |
|---|---|---|
| Claude | 理解、推理、生成 | 模型具备大脑能力 |
| Claude Code | 读代码、改文件、跑测试、提交结果 | 进入研发生产环境 |
| 内部扩散 | 非工程团队用 agent 完成复杂任务 | 专业岗位靠近执行和验证 |
| Claude Cowork | 处理文件、应用、多来源资料并交付结果 | agent 进入知识工作现场 |
| 安全边界 | 权限、审批、评测、ASL、RSP | 行动能力必须被治理 |

**视觉建议**

图片模型生成“能力外化时间线”：不是普通横轴时间线，而是一个人逐步长出大脑、手、眼睛、神经、免疫系统的隐喻图。文字保持少量，重点用视觉表达能力演进。

### 11 安全不是附属模块，而是行动能力的前提

**页面主句**

agent 越能行动，安全越不能放在最后；Anthropic 的路线是能力推进和安全边界同步建设。

**正文要点**

- Claude Code 默认要求用户批准文件修改和命令执行。
- Claude Cowork 强调人类监督，重要决策仍由用户负责。
- Responsible Scaling Policy 使用 ASL 思路：能力提升必须匹配对应安全措施。
- 对高风险行业来说，这一点比效率提升更重要。

**证据**

- Claude Code 官方页：agent safety、权限和人工控制。
- Claude Cowork 官方页：human oversight、trust、access、control。
- Anthropic Responsible Scaling Policy：`https://www.anthropic.com/news/anthropics-responsible-scaling-policy`

**改写当前 PPT**

- 第 14 页不要写 `constitution.md` 作为 Claude Code 机制，证据不稳。
- 第 17、18、21 页可以保留，但改成“权限、测试、评测、反馈系统”。

### 12 同行共识一：OpenAI 也在讲 harness

**页面主句**

OpenAI 的 harness engineering 证明，同类头部公司也在把重点从“模型回答”转向“模型在环境中可靠执行”。

**正文要点**

- 人负责方向、目标、判断和验收。
- agent 负责执行、迭代、修复和提交。
- 真正的生产力来自工作环境：代码库知识、测试、权限、反馈、评审。
- 这不是 Anthropic 的孤例。

**证据**

- OpenAI Harness Engineering：`https://openai.com/index/harness-engineering/`

**定位**

这页只做共识验证，不展开 OpenAI 组织架构。

### 13 同行共识二：Seed 显示能力按模块展开

**页面主句**

Seed 的公开能力版图说明，AI 公司越来越按模型、基础设施、多模态、世界模型、机器人、安全责任等能力模块展开。

**正文要点**

- 这与李想访谈的分析因子相呼应：AI 公司不是简单职能拼装，而是在围绕智能体能力建设组织。
- Seed 只能作为能力版图证据，不能写成字节官方组织架构结论。
- 对本报告的作用是：证明 Anthropic 的路径属于行业共识，而不是单家公司偶然选择。

**证据**

- Seed Models：`https://seed.bytedance.com/en/models`

### 14 对宝付的第一层启发：别从工具开始，从流程开始

**页面主句**

宝付不能把 AI 落地理解成采购工具，而要先选择能被 agent 参与、又能被人审计的流程。

**正文要点**

- 支付公司的核心不是内容生产，而是资金、商户、交易、风控、清结算、合规和客户信任。
- agent 可以承担资料整理、比对、分析、生成、复核辅助。
- 但资金动作、风险处置、合规上报、生产变更必须保留审批、日志和回放。
- 所以宝付的 AI 路线应是“受控执行”，不是“全自动替代”。

### 15 宝付场景一：商户接入

**页面主句**

商户接入适合先做 agent，因为它资料多、规则多、跨部门多，但最终决策必须由人负责。

**旧流程**

销售收资料，产品确认方案，风控评估风险，合规看资质，技术评估接口，运营跟进上线。

**agent 参与后的流程**

- 读取商户资料、合同、行业信息、官网和历史案例。
- 对照准入规则，生成资料缺口和风险摘要。
- 形成接入方案草稿、接口需求、待确认问题和审批包。
- 人完成风险判断、商务判断、合规判断和最终审批。

**落地边界**

- agent 不直接批准商户。
- agent 不绕过 KYC、尽调、风控和合规流程。
- 所有依据必须可追溯到原始材料。

### 16 宝付场景二：风控与反洗钱

**页面主句**

风控 agent 的价值不是替代规则，而是把分散证据组织成可解释、可复核的风险判断包。

**agent 参与后的流程**

- 围绕异常商户、异常交易或异常行业模式拉取证据。
- 汇总交易特征、历史规则、相似案例、处置记录、外部风险信号。
- 生成风险画像、疑点列表、建议动作和证据索引。
- 风控人员决定是否冻结、限额、拒付、报送或人工复核。

**落地边界**

- 不能让 agent 单独完成冻结、处罚、报送。
- 模型输出不能作为唯一证据。
- 每个结论必须绑定交易数据、规则、案例或制度条款。

### 17 宝付场景三：清结算与对账

**页面主句**

清结算和对账是 Claude Cowork 类能力最适合迁移的场景：多文件、多系统、多步骤、重复但高风险。

**agent 参与后的流程**

- 读取支付流水、清算文件、通道账单、银行回盘、差错记录。
- 识别金额、笔数、时间、通道、手续费和状态差异。
- 生成差异定位、处理建议、需人工确认事项和工单草稿。
- 人完成差错认定、资金调整和通道沟通。

**落地边界**

- agent 不直接改账。
- agent 不直接发起资金调账。
- agent 只生成证据包、建议和工单。

### 18 宝付场景四：客诉、调单、拒付

**页面主句**

争议处理的瓶颈常常不是判断，而是材料追溯；agent 可以把证据组织速度提升一个数量级。

**agent 参与后的流程**

- 汇总交易记录、商户协议、用户沟通、通道规则、调单时限、拒付原因。
- 生成争议处理包：事实时间线、证据清单、责任初判、缺失材料、建议话术。
- 客服、运营、商户管理、合规共同评审。

**落地边界**

- 不让 agent 直接对外承诺赔付、免责或处罚。
- 高敏感客诉必须人工复核。
- 所有对外口径保留审批记录。

### 19 宝付场景五：研发与运维

**页面主句**

研发与运维是宝付最接近 Claude Code 的场景，可以先从低风险代码库、测试、日志和文档开始。

**agent 参与后的流程**

- 读取需求、代码、接口文档、测试用例和历史缺陷。
- 生成变更方案、影响范围、测试建议和回滚预案。
- 在隔离环境内修改代码、跑测试、整理 MR 描述。
- 运维侧辅助分析日志、告警、变更记录和故障复盘。

**落地边界**

- 禁止 agent 直接操作生产。
- 禁止无审批变更数据库和资金相关逻辑。
- 先在只读分析、测试生成、文档更新、非核心脚本上试点。

### 20 宝付需要建设的不是“AI 工具箱”，而是受控工作场

**页面主句**

如果没有工作环境、权限、知识、评测和审批，agent 只会变成更贵的问答框。

**能力组件**

| 组件 | 对宝付意味着什么 |
|---|---|
| 工作入口 | 工单、需求、商户接入单、风险事件、对账差异、客诉单 |
| 知识上下文 | 制度、接口文档、商户资料、通道规则、历史案例、代码库 |
| 工具权限 | 只读查询、文件读取、测试环境、工单创建、报告生成 |
| 审批边界 | 风控处置、资金调整、生产发布、对外回复必须人工批准 |
| 评测机制 | 准确率、可追溯率、漏判率、复核耗时、风险事件回放 |
| 反馈沉淀 | 每次人工修改、拒绝、补充证据都回写到流程知识里 |

**视觉建议**

图片模型生成“支付公司受控工作场”一图：中间是 agent 工作台，周围连接商户接入、风控、清结算、客诉、研发运维五个流程；每个流程外层有权限、审批、日志、评测四道边界。位图风格，适合 PPT，不要 SVG。

### 21 宝付 90 天试点路线

**页面主句**

不要从全公司铺开开始，先用 90 天验证一个可控闭环。

**建议路线**

| 阶段 | 时间 | 目标 | 交付物 |
|---|---:|---|---|
| 第一阶段 | 0-30 天 | 选流程、建知识、定边界 | 选择 1 个试点流程；整理制度、样例、数据字段；定义禁止动作 |
| 第二阶段 | 31-60 天 | 建 agent 工作包 | 形成任务模板、证据包模板、人工复核表、评测指标 |
| 第三阶段 | 61-90 天 | 小范围运行 | 每周复盘正确率、节省时间、风险误差、人工修改点 |

**推荐试点优先级**

1. 对账差异分析：可控、重复、证据清晰。
2. 商户资料预审：业务价值高，但要控制权限。
3. 研发测试和日志分析：技术团队接受度高。

### 22 结论：宝付要学习 Anthropic 的不是产品，而是路径

**页面主句**

Anthropic 的路径告诉我们：强模型真正进入组织，不靠一次性部署，而靠一个个可控工作场。

**结论**

- Claude Code 说明：强模型进入真实环境后，可以承担执行循环。
- Claude Cowork 说明：这种执行能力会从研发扩散到知识工作。
- Responsible Scaling Policy 和 agent safety 说明：能力越强，边界越重要。
- 对宝付来说，AI 不是先替代岗位，而是先重构流程里的证据整理、任务执行、人工审批和反馈沉淀。

**最终判断**

宝付未来的 AI 能力，不应停留在“问答”和“写材料”，而应围绕支付核心流程建设一批受控 agent：能读制度、查证据、跑流程、生成交付物；但所有高风险动作由人审批、可审计、可回放。

## 当前 PPT 页面的处理建议

| 当前页 | 处理方式 | 理由 |
|---|---|---|
| 1 | 重写 | 标题和结构改为 Anthropic 路径研究 |
| 2 | 保留部分 | 用作 Anthropic 使命和 Claude 定位，不写空泛洞察 |
| 3 | 重写 | 改成“为什么真实工作场重要” |
| 4 | 强化 | 这是内部运营证据，应提前成为核心页 |
| 5 | 删除重做 | 未核验时间线风险高，只保留官方可证大事件 |
| 6 | 合并重写 | 从工具到团队，落到研发协作变化 |
| 7 | 保留重写 | 从概念变成工作环境、规则和反馈系统 |
| 8 | 删除或弱化 | 不讲“放弃 RAG”，改成“从检索到执行” |
| 9 | 删除或改总结 | “OS 无限可能”太虚 |
| 10 | 可保留为分节页 | 但章节名要改 |
| 11-13 | 保留重写 | 从记忆技术改成组织知识如何进入 agent 工作场 |
| 14 | 重写 | 不写未经证实的 `constitution.md` 机制 |
| 15 | 重写 | 避免混淆 Claude Code 和 Computer Use |
| 16 | 保留重写 | 多 agent 协作要服务组织流程 |
| 17-18 | 强化 | harness 和反馈循环是关键 |
| 19 | 可保留 | 改成阶段总结 |
| 20-21 | 保留并前移到宝付章节 | 知识库、能力图谱、质量门禁是宝付落地点 |
| 22-28 | 全部重写 | 改成宝付支付流程启发 |
| 29 | 视实际成果补充 | 需要具体成果，不要空页 |
| 30 | 保留 | Q&A |

## 需要继续核验的信源

1. Anthropic 官方 “How teams use Claude Code” 页面，作为内部扩散的核心证据。
2. Claude Code 官方文档中关于 memory、subagents、hooks、MCP、permissions 的具体机制。
3. OpenAI Harness Engineering 原文关键表述，作为共识旁证。
4. Seed 官方模型和团队方向页面，避免把能力版图写成组织架构。
5. 当前 PPT 第 5 页所有版本时间点，未核验前不进入最终稿。

