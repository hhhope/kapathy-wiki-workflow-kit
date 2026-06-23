# Stripe 公司演进与 AI 时代支付变革 H5 设计稿

## 路由状态

Route: brainstorm -> superpowers spec; OpenSpec 在本设计稿审核通过前保持只读。

本稿是重新锚定后的中文审核稿。它不再把内部分析概念写成标题，也不再按“材料模块”堆页面。它把 Stripe 当作一个支付行业样本做商业分析：**这家公司如何选择战略楔子，如何扩张能力边界，哪些选择造成了今天的位置，AI 时代又可能在哪些已有金融能力之上继续创新。**

## 这篇 H5 到底要回答什么

主问题：

> Stripe 的公司发展路径，如何解释 AI 时代支付行业的生存之道？

更具体地说：

> 预授权、发卡、联名权益、token、钱包、用量计费、风控、KYC/KYB、争议处理和清结算，属于支付行业既有能力。AI 时代的分析重点，是这些能力之上形成了哪些新的控制点：商业对象的机器可读化、授权边界的规则化、预算执行的自动化、风控触发的实时化、责任证据的可审计化。Stripe 的研究价值在于：它过去十五年持续把金融复杂性沉淀为 API、对象模型、文档、测试环境和风控规则，因此更有可能把这些底层能力升级为 Agent 可操作的交易基础设施。

金融对象先分为两条主线：

1. **交易关系线**：一笔交易关系如何发生、被确认、被授权、被履约并完成责任闭环。分析对象包括商品与服务表达、价格与权益、授权边界、履约状态、分账清结算、争议处理和责任归属。
2. **信用关系线**：一笔信用关系如何被授予、使用、定价、监控并回收。分析对象包括授信主体、数据依据、额度、期限、价格、还款来源、风险预警、逾期处置和合规边界。

Stripe 的公司路径要同时放入这两条线。Payments、Checkout、Connect、Billing、Tax、Radar、Link、Agentic Commerce、MCP/skills、MPP/x402 解释交易关系如何被接口化；Capital、BNPL 支付方式、Issuing、Financial Connections、Identity、Radar、Capital underwriting 和 ML 风控解释信用关系如何被数据化、规则化和自动化回收。

拆成五个商业分析问题：

1. **路径问题**：Stripe 在 2010-2026 每个阶段解决的核心商业问题是什么？
2. **战略问题**：哪些长期战略选择造就了 Stripe 的能力结构？
3. **变化问题**：AI 时代之后，支付行业会在已有能力之上创新哪些新的控制点？
4. **竞争问题**：Stripe、Visa、Mastercard、Google/OpenAI、PayPal/Adyen/Checkout.com、钱包和稳定币公司分别在争夺哪一层入口？
5. **启发问题**：我们如何用 Stripe 的路径理解 AI 支付基础设施，而不是只看产品发布？

这篇 H5 的主轴是时间。时间不是装饰，而是分析方法：只有把产品、并购、市场指标、技术接口、JD 和来源放回时间线上，才能看出哪些是战略选择，哪些是结果，哪些只是当期噪音。

## 商业分析口径

每个阶段统一用八个字段分析，避免写成流水账：

| 字段 | 要回答的问题 |
|---|---|
| 战略押注 | Stripe 当时押了什么方向？ |
| 目标客户 | 谁的痛点最先被解决？ |
| 商业模式影响 | 这一步如何扩大处理规模、收入机会或客户粘性？ |
| 能力沉淀 | 这阶段留下了什么可复用能力？ |
| 技术选择 | 哪些 API、对象、文档、工具或协议支撑这个战略？ |
| 并购/补位 | 哪些能力不是自然长出来的，需要收购或合作补齐？ |
| 指标证据 | 哪些数据说明这一步真的扩大了位置？ |
| AI 时代复用 | 这阶段能力在 AI 时代被怎样重新调用？ |

这才是页面应该呈现的“体系”。不是证据分类体系，而是公司战略演进体系。

## 当前漂移复盘：为什么 H5 没按详设做

本详设后续实现不能只当素材库使用。前几轮 H5 漂移的核心问题不是“少几个词”，而是实现没有把详设当成章节验收结构。

已能确认的漂移至少有四次：

1. **研究逻辑漂移**：早期 H5 把市场、并购、技术、AI 事件做成材料模块，像 source bucket，不像商业分析。对应修复是 `2026-06-22-stripe-h5-research-logic-redesign.md`。
2. **范围漂移**：后续实现进入 `refine-stripe-h5-visual-atlas`，实际做的是视觉 atlas、首屏、来源 handle 和节点密度；但当时应验收的是本详设的第 4-6 章论证顺序。结果是关键词出现了，章节因果没有出现。
3. **局部话术漂移**：`polish` 和 `professionalize` 两轮主要修标题、口语化、词云、引用样式和截图问题，但没有重新执行“详设章节 -> H5 章节”的逐项映射。
4. **结尾结构漂移**：最新 H5 末尾仍停在“战略复利、竞争位置、引用、信号分层、全面看”，没有把用户确认的新判断落成 `12 未来判断` 和 `13 我们能学什么`。

直接原因：

- Superpowers 详设被当作参考材料，而不是 reader-facing acceptance checklist。
- OpenSpec change 之间边界相邻，执行时选择了视觉/语言修复 change，却没有检查它是否拥有本详设的章节验收范围。
- 验证偏向 grep、HTML parse 和截图 smoke；这些只能证明页面存在，不证明论证顺序正确。
- H5 文件过大，后续 patch 倾向局部补卡片，绕过了反向大纲检查。

后续实现前必须先做一次反向大纲：

| 详设章节 | H5 必须出现的读者路径 | 验收方式 |
|---|---|---|
| 4 哪些战略造就 Stripe | 战略选择 -> 能力沉淀 -> 后续产品/并购 -> AI 时代复用 | 章节截图 + 文字结构检查 |
| 5 为什么坚持做难事 | 碎片化金融规则 -> 领域对象/API -> 商业分发和迁移成本 | 章节截图 + 关键论证检查 |
| 6 AI 支付重组 | 行业判断 -> 基础设施压力 -> 交易/信用线 -> 权益凭据 -> 工具化 -> 协议责任 -> 回到 Stripe 路径 | 章节截图 + 流程图读回 |
| 12 未来判断 | 历史规律 -> 当前阶段 -> L1-L4 折线 -> 未来五年 -> 金融结果阈值 | 折线图截图 + 阶段读回 |
| 13 我们能学什么 | AI 降低实现成本但抬高金融设计成本 -> 金融关系设计才是可复用框架 | 结尾截图 + 结论读回 |

验收原则：

> 关键词覆盖不等于结构覆盖。截图不只看“有没有”，还要读回“读者会不会按正确顺序理解”。

## 推荐标题

主标题：

> Stripe 公司演进与 AI 时代支付变革

副标题：

> 2010-2026 年，Stripe 的主线不是产品线扩张，而是把交易关系和信用关系拆成可编程对象：谁参与、交易如何确认、资金如何流转、信用如何授予、风险如何回收。AI 时代的变化，是这些对象开始被 Agent、模型和自动化系统读取、组合和执行。

备用标题：

- `Stripe 的发展路径与 AI 时代变革`
- `从 Stripe 看 AI 时代金融基础设施的演进`
- `Stripe 2010-2026：公司路径、支付能力重组与 AI 交易变化`

明确不用：

- `Stripe：从支付 API 到 AI 交易控制面`
- `证据坐标`
- `能力迁移地图`
- `核心判断`
- `原有能力底座`
- `市场位置计算面板`

## 首屏应该怎么说

首屏不讲抽象概念，先交代研究对象、时间范围和结论方向。

推荐文案：

> 本页从 2010 到 2026 追踪 Stripe 如何从支付 API 走向嵌入式支付与嵌入式金融基础设施。早期 Stripe 把在线收款嵌入开发者产品；Connect 把支付、分账、商户 onboarding 和合规嵌入平台、marketplace 与 SaaS；Treasury、Issuing、Capital、Financial Connections 把账户、卡、授信和资金管理嵌入平台经营。AI 时代的变化，是交易关系和信用关系继续被嵌入 Agent、模型和自动化工作流。

改写后的首屏判断：

> Stripe 的公司路径可以读成嵌入位置的迁移：从嵌入网站和 App 的收款接口，到嵌入平台经营系统的支付和金融服务，再到嵌入 AI 入口和 Agent workflow 的交易与信用执行层。AI 后的核心问题，是 Agent 在什么授权、预算、商品对象、授信和风控规则下完成交易，而不是支付按钮是否更智能。

首屏要让读者立刻知道：

- 这是 Stripe 公司路径研究。
- 核心视角是 2010-2026 的时间变化。
- 主线是嵌入式支付到嵌入式金融，再到 Agent 嵌入式交易与信用。
- 1000 条来源是底层材料，不是主叙事。

首屏主图：

- 不做孤立指标卡，改成一张增长折线图。
- 主线：Stripe processed volume，展示 2023 $1T、2024 约 $1.4T、2025 $1.9T。
- 副线：Stripe GDP-equivalent framing，展示 2023 1.0%、2025 1.6%。
- 标注：2026 Sessions 发布 288 项产品和功能，作为 AI 时代产品扩张节点，不和交易量混成同一指标。
- 来源队列：1000 concrete URL rows 放在图下注释或来源热力入口，明确是 triage queue，不是 1000 条已读结论。

同业基准：

- 首屏或首屏下方要有 peer benchmark 入口，不能只看 Stripe 自己增长。
- 同业不强行放进同一条曲线。用两个视图更清楚：
  - `处理规模/TPV 量级视图`：Stripe、PayPal、Adyen、Worldpay/Global Payments 等可比口径。
  - `增长指数视图`：把各家公司同一年归一为 100，看增长斜率，而不是混淆收入、TPV 和净收入。
- take-rate、revenue / TPV、processed volume / net revenue 的公式放展开面板，主图只表达规模、增长和相对量级。

## BVP 例子怎么用

BVP `State of the Cloud 2024` 给我们的不是标题，也不是配色，而是“年度状态报告”的结构：

- 一个清楚的大主题。
- 几个能解释主题的趋势。
- 每个趋势配数据点和影响。
- 视觉图表服务判断，而不是展示材料数量。

本文的改造：

- BVP 的主题是 AI Cloud。
- 本文主题是 Stripe 公司演进与 AI 时代变革。
- BVP 的趋势卡，在这里变成“阶段战略卡 + AI 后变化专题”。
- BVP 的 notable data points，在这里变成处理规模、估值、并购、产品发布、API/docs、合作事件、JD 信号和来源热力图。

## 页面结构

### 1. 公司演进总览：2010-2026

作用：

用一张主时间线建立全篇。读者先看到公司怎么走，而不是看到证据怎么分。

五个阶段：

| 阶段 | 时间 | 核心商业问题 | 战略押注 | 结果 |
|---|---|---|---|---|
| 支付 API 起点 | 2010-2014 | 新互联网业务收款接入复杂 | API-first、开发者体验、文档和测试 | Stripe 拿到开发者入口 |
| 商户经营系统 | 2015-2019 | 平台、SaaS、订阅和线下场景变复杂 | Connect、Billing、Radar、Terminal、Atlas | Stripe 从支付入口进入商户经营层 |
| 金融运营平台 | 2020-2022 | 全球化、税务、账户、风控、资金和合规压力上升 | Treasury、Capital、Identity、Tax、Issuing，以及区域/税务/对账/硬件补位 | Stripe 扩成更完整的金融运营栈 |
| AI 客户压力 | 2023-2024 | AI 公司高增长、高用量、全球化、风险和成本波动 | Revenue suite、usage billing、global tax、risk、agent tooling、Bridge | 原有收入和风控能力被 AI 客户重新放大 |
| AI 时代支付能力重组 | 2025-2026 | Agent 交易、权益/凭据重组、稳定币、钱包、机器支付和实时风控进入主线 | Bridge、Privy、Metronome、Issuing/Link wallets、MCP/skills、MPP、x402、Radar token theft | Stripe 把原有支付、发卡、计费、风控和开发者能力接入 AI 时代新交易形态 |

视觉：

- 横向年份主轴。
- 每个阶段有一句战略判断。
- 每个阶段附 3-5 个关键事件或指标。
- AI 阶段作为最新阶段，但必须显示它依赖前面阶段。

### 2. 阶段战略卡：每个阶段都按同一口径展开

作用：

避免写成公司百科。每个阶段都用同一商业分析框架。

每张阶段卡包含：

- 战略押注
- 目标客户
- 商业模式影响
- 能力沉淀
- 技术选择
- 并购/补位
- 指标证据
- AI 时代复用

示例：2010-2014 支付 API 起点

- 战略押注：把在线收款从银行/支付机构接入问题，改成开发者 API 接入问题。
- 目标客户：互联网创业公司、开发者团队、需要快速上线收款的新业务。
- 商业模式影响：用低摩擦接入扩大商户获取，处理规模随客户增长累积。
- 能力沉淀：API、SDK、文档、测试卡、Dashboard、webhook。
- 技术选择：把金融动作封装成可调用接口。
- 并购/补位：早期不是并购驱动。
- 指标证据：早期公开份额不足，使用官方历史材料、客户扩散和开发者采用作为代理。
- AI 时代复用：agent docs、MCP、llms.txt、sandbox 和 toolkit 仍然继承 developer-first 分发逻辑。

### 3. 主时间轴：五条线并读

作用：

这是 H5 的核心交互。拖动年份时，读者同时看到商业战略、市场位置、并购、技术和 AI 变化。

五条线：

1. 公司战略线：Stripe 在这个阶段解决什么商业问题。
2. 市场位置线：处理规模、估值、客户规模、同业参照。
3. 并购补位线：哪些能力通过收购或合作补齐。
4. 技术产品线：API、docs、对象模型、风控、计费、协议。
5. AI 支付重组线：2023 之后 AI 客户、Agent 交易、权益/联名卡、usage billing、MCP/skills、stablecoin、machine payment、风险对象如何出现。

交互：

- 年份可拖拽。
- 点击年份显示五条线同屏信息。
- 节点颜色固定：战略、市场、并购、技术、AI。
- 点击节点打开详情抽屉：事实、商业意义、来源强度。

这一章回答：

> 这些事件如何共同解释 Stripe 的变迁？

### 4. 哪些战略造就了 Stripe

作用：

把“战略因果”讲清楚。不是列产品，而是解释长期选择如何造成今天的位置。

六个战略选择：

1. **开发者入口战略**
   Stripe 用 API、SDK、文档和测试体验进入市场。它不是先做大销售组织，而是把支付接入变成开发者体验。这造就了后续 docs、agent toolkit、MCP、llms.txt、sandbox 的分发基础。

2. **平台商户战略**
   Connect 让 Stripe 服务 marketplace、platform 和 SaaS，而不只是单个商户。平台客户带来更复杂的账户、分账、风控和合规问题，也让 Stripe 更深入商户经营层。

3. **收入运营战略**
   Billing、Revenue suite、Tax、Invoicing 让 Stripe 从收单扩到收入管理。AI 公司的 token、event、usage、outcome 计费需求，让这条战略线在 2023 之后变得更关键。

4. **风险基础设施战略**
   Radar、Identity、KYC/KYB、Capital underwriting、AI Security JD 和 token theft protection 说明风险不是支付之后的售后问题，而是交易系统基础能力。

5. **全球化和本地化补位战略**
   Paystack、TaxJar、Recko、BBPOS 等动作不是并购新闻，而是补全球化、本地支付、税务、对账和线下场景的缺口。

6. **发卡、钱包和权益入口战略**
   Issuing、virtual cards、spending controls、card personalization、tokens、Link wallets 和 Privy 说明 Stripe 不只处理商户收款，也在构建买方凭据、平台权益和受限授权能力。AI 时代的联名卡、权益卡、任务级受限支付凭据和钱包，会重新使用这些能力。

7. **新金融轨道接入战略**
   Bridge、Privy、Metronome、Tempo、MPP、x402 表明 Stripe 正在把稳定币、钱包、用量计费和机器支付接入自己的主线。

这一章必须用图表示因果：

> 战略选择 -> 能力沉淀 -> 后续产品/并购 -> AI 时代复用。

### 5. Stripe 为什么坚持做难事：API、规范和领域模型

作用：

回答一个更深的问题：Stripe 为什么长期做行业里最难、最慢、最不讨巧的事情，包括 API 抽象、对象模型、文档、测试环境、协议、风控规则、税务和合规边界。

这不是工程洁癖，而是商业战略。

核心解释：

> 支付和金融基础设施行业的问题不是“有没有支付能力”，而是每个国家、支付方式、商户类型、风险场景、税务规则和结算轨道都高度碎片化。Stripe 的长期策略，是把这些碎片化规则抽象成稳定的领域对象和开发者接口，让新业务可以用同一套模型接入复杂金融世界。

它一直在做的难事：

| 难事 | 表面动作 | 商业意义 |
|---|---|---|
| 统一领域模型 | PaymentIntent、Checkout Session、Customer、Subscription、Invoice、Account、Balance、Payout 等对象 | 把复杂金融动作变成可复用的业务对象 |
| API 和文档标准化 | API-first、SDK、docs、test mode、webhook、preview API | 降低接入成本，让开发者把 Stripe 当默认入口 |
| 商户经营抽象 | Connect、Billing、Radar、Tax、Terminal、Treasury | 从单笔支付扩到商户经营系统 |
| 风险和合规内嵌 | Radar、Identity、KYC/KYB、AI Security、token theft protection | 把风险从人工流程变成交易基础能力 |
| 发卡和权益入口 | Issuing、virtual cards、personalization designs、tokens、spending controls、Link wallets | 把卡、权益、凭据、预算和授权做成可编程能力 |
| 新轨道接入 | Bridge、Privy、Metronome、MPP、x402、stablecoin、wallet | 把新金融轨道纳入同一套商业基础设施 |

为什么这能形成壁垒：

- **开发者默认选择**：谁定义了更好用的 API 和对象模型，谁就更容易成为新业务的第一接入点。
- **迁移成本**：一旦商户把支付、订阅、税务、风控、分账、账务和结算都接进同一套对象，替换成本远高于替换单个支付通道。
- **复合能力**：竞争对手可以复制一个功能，但很难同时复制支付、发卡、计费、税务、风控、全球化、本地支付、钱包和稳定币的组合。
- **行业抽象层**：Stripe 不是只和 PSP 比费率，它试图把自己放在更高的抽象层，成为开发者和商户理解金融复杂性的接口。
- **新场景复用**：AI 时代出现联名权益、Agent 钱包、MCP payment tools、usage billing、machine payment、stablecoin 时，Stripe 可以在已有能力上继续定义入口、授权、执行、风险和结算控制点，而不是从零开始。

这一章要回答：

> Stripe 的正确性不是“产品多”，而是它长期把行业复杂性标准化，并把标准化能力变成商业分发和锁定机制。

### 6. AI 时代支付行业重组：从权益入口到工具化支付

作用：

这一章不再泛泛写“AI 后变化”。它要回答支付行业在 AI 时代到底发生了什么，以及 Stripe 为什么能接住这件事。

总判断：

> 支付行业已有预授权、发卡、联名权益、钱包、token、订阅、风控、授信、争议和清结算。AI 时代的创新不在于重新发明这些金融能力，而在于把它们升级成 Agent 可以理解、可以调用、可以被限制、可以被审计、可以被追责的交易系统。

更准确的判断：

> 没有 AI，嵌入式支付、嵌入式金融、对象模型、计费、风控、合规和清结算也应该继续演进。AI 改变的是成本结构：coding、集成、测试和定制化实现成本下降，但金融产品的设计、评估、解释、审计和责任归因成本上升。主体仍然是人、组织、商户、平台、监管和网络规则共同定义的金融关系。谁能把复杂交易关系和信用关系设计成低摩擦、可组合、可评估、可审计、可合规的对象和流程，谁就更容易成为平台、SaaS、AI 应用和 Agent workflow 的默认金融接口。

这一节不把 AI 写成生存主体。支付和金融关系本来就高度碎片化，行业需要有人把复杂规则做成对象、接口、计费、授权、风控、清结算和合规边界。AI 之后，客户自己拼支付场景的技术门槛下降，但金融设计、责任边界、监管适配、异常处理和生态整合仍然集中在专业支付公司手里。

创新发生在五个上层控制点：

| 创新控制点 | 原有能力 | AI 时代新增变量 |
|---|---|---|
| 入口 | checkout、支付页、钱包入口 | AI 对话、搜索、Copilot、agent marketplace 成为商品发现和交易入口 |
| 权限 | 持卡人授权、预授权、商户规则 | 预算、商户、品类、时间、审批、撤销和责任被转化为可执行规则 |
| 商业对象 | 商品页、价格表、订阅方案、API 资源 | 商品、价格、库存、权益、订阅、token 用量和 API 资源进入机器可读表达 |
| 执行 | 人工接入、网页操作、API 调用 | Agent 通过 MCP、skills、API、sandbox、protocol 调用支付和商户系统 |
| 责任 | 支付结果、订单记录、争议材料 | 授权证据、风控信号、争议材料、清结算状态和审计轨迹进入交易过程 |

这一章先给出 Stripe 必须做基础设施的判断，再把支付行业拆成交易关系线和信用关系线，最后解释权益入口、工具化支付、协议化授权和信用风控这些创新控制点。

#### 6.0 为什么 Stripe 一定要做基础设施

Stripe 做基础设施的动因，在于 AI 时代会把支付价值拆到不同控制点：

| 谁在争夺控制点 | 可能拿走什么 | Stripe 不做基建的结果 |
|---|---|---|
| OpenAI / Google / Microsoft 等 AI 入口 | 用户意图、商品发现、购买入口、推荐分发 | Stripe 退回幕后处理通道，只拿支付处理价值 |
| Visa / Mastercard 等网络 | token、发卡规则、争议、授权和网络级信任 | Stripe 的授权和风险能力被卡网络上收 |
| 钱包 / 超级 App / 平台 | 用户凭据、权益、会员关系、默认支付方式 | Stripe 失去买方关系和权益分发位置 |
| 稳定币 / x402 / 新协议 | 机器支付、跨境结算、微支付、API 资源购买 | Stripe 的结算轨道被新协议绕开 |
| 商户 SaaS / PSP 同行 | 商户运营、税务、计费、风控、对账 | Stripe 被压回费率竞争 |

所以 Stripe 必须把自己从“支付处理商”推进到“交易基础设施商”。它要把支付行业已有能力做成一套可被 AI 入口调用、可被商户运营承接、可被金融系统审计的基础设施：

- 向上接 AI 入口：Agentic Commerce、Copilot Checkout、OpenAI/Google/Microsoft/Meta 合作。
- 向开发者接工具：MCP、skills、llms.txt、plain-text docs、sandbox、agent toolkit。
- 向商户接经营对象：catalog feed、Checkout、Billing、Tax、Radar、Connect、Revenue suite。
- 向买方接授权和凭据：Link wallets、Issuing、virtual cards、spending controls、tokens、Privy。
- 向资金轨道接结算：Bridge、stablecoin、Tempo、MPP、x402、machine payments。

这一节的判断：

> Stripe 做基建，是为了保住并扩大“交易规则层”的位置。AI 入口可以拿走用户意图，卡网络可以拿走凭据规则，稳定币协议可以拿走结算路径，商户 SaaS 可以拿走经营关系。Stripe 只有把 API、对象模型、钱包、计费、风控、发卡和结算连成基础设施，才不会在 AI 交易链路里被压缩成普通支付通道。

#### 6.1 两条金融主线：交易关系和信用关系

这一节是 AI 支付分析的底座。支付行业不是只有扣款和清算，更底层的是两类金融关系：

| 主线 | 本质问题 | 传统形态 | AI 时代新问题 | Stripe 对应能力 |
|---|---|---|---|---|
| 交易关系线 | 交易关系如何发生、确认、授权、履约、结算和追责 | C2B 支付、B2B 付款、平台分账、订阅、发票、线下收单、钱包 | Agent 如何读取商业对象、执行授权任务、遵守预算和商户规则、留下责任证据 | Payments、Checkout、Connect、Billing、Tax、Radar、Link、Agentic Commerce、MCP/skills、MPP/x402 |
| 信用关系线 | 价值先发生，资金以后支付或偿还 | 信用卡、赊账、BNPL、消费分期、商户贷款、现金垫款、营运资金 | Agent 或平台如何获得受限信用额度，如何按交易数据动态授信，如何实时控额、还款和处置风险 | Capital、BNPL payment methods、Issuing、Financial Connections、Identity、Radar、Capital underwriting、ML platform |

交易关系线回答交易如何发生和履约。信用关系线回答信用如何授予和回收。两条线经常绑定在一起：BNPL 把消费信用嵌入 checkout；信用卡和联名卡把支付、授信、权益和争议处理绑定在同一张凭据上；Stripe Capital 把商户经营现金流、销售历史和还款机制接回 Stripe 交易系统。

这个分法决定 AI 时代支付的分析口径：

- **交易关系**：Agent 代表谁，执行什么交易，依据什么授权，履约状态如何确认，责任证据如何保存。
- **信用关系**：信用建立在身份、交易历史、现金流、商户经营数据、风控和还款控制之上；这些正是 Stripe 长期沉淀的数据和系统位置。
- **赊和贷款是交易时间结构的变化**。价值交付先于资金偿付，系统必须同时处理定价、期限、额度、还款来源、逾期、欺诈和监管。

Stripe 相关证据要这样组织：

| 证据对象 | 支撑哪条主线 | 该怎么解读 |
|---|---|---|
| Stripe Capital | 信用关系线 | 资格与 Stripe 上的交易量和历史相关，还款从每日销售中自动扣取，说明 Stripe 可以把交易流变成授信和还款控制面 |
| Capital underwriting JD | 信用关系线 | 招聘信号显示 Capital underwriting 使用 Stripe 内外的 business activity 和 ML model 定制融资 offer，说明信用评估已经是机器学习和业务活动数据问题 |
| BNPL payment methods | 信用关系线 + 交易关系线 | Affirm、Klarna、Afterpay/Clearpay 等 pay-later 方式把消费信用嵌进 checkout，本质是结账时的授信和分期决策 |
| Financial Connections | 信用关系线 | 银行账户和金融数据连接用于补足账户、现金流和还款能力判断，是信用风控的数据接口之一 |
| Identity / Radar | 两条线共同基础 | 身份验证、欺诈识别和风险控制既服务交易通过率，也服务授信、额度、逾期和争议责任 |
| Issuing / spending controls | 信用关系线 + 权益入口 | 发卡、额度、MCC/商户/地域/时间控制和实时授权，是把信用、预算和权益做成可编程凭据 |

本 H5 不能把信用线压缩成一个词。信用线要作为独立章节进入时间轴：2015-2019 看平台和风控如何沉淀信用数据；2020-2022 看 Capital、Treasury、Identity、Issuing 进入金融运营平台；2023-2026 看 AI 客户、Agent 任务、用量计费和钱包凭据如何把“动态授信、受限信用、信用风控”推到前台。

#### 6.2 权益化入口：联名卡、权益卡和 tokenized credential

要补上的核心点：

联名卡和权益卡属于核心入口案例。它们说明支付从来不只是扣款，还会把身份、权益、额度、返佣、风控、品牌关系和消费场景绑定到一张卡或一个凭据上。AI 时代的“AI 联名卡”“Agent 钱包”“平台内支付 token”，延续的是同一套商业逻辑：把支付凭据变成某个入口的权益和控制层。

读者要看到的映射：

| 传统金融机制 | AI 时代对应形态 | 需要解释的商业含义 |
|---|---|---|
| 联名卡 / 权益卡 | AI 应用绑定卡、平台权益卡、Agent 可用凭据 | 入口方用权益和分润绑定支付关系 |
| 预授权 | Agent 预算、单次任务授权、购物条件授权 | 用户不是每次点击付款，而是提前定义边界 |
| tokenized card-on-file | Agentic Token、Shared Payment Token、数字钱包 token | 不把原始卡号暴露给 Agent 或商户 |
| virtual card / commercial card | 任务级受限支付凭据、企业采购虚拟卡、一次性卡 | 把支付责任限制在场景、金额、商户和时间内 |
| spending controls | 预算、MCC、地域、商户白名单、审批流 | 支付公司把“人类意图”转成机器可执行规则 |
| rewards / offers | 个性化 bundle、平台权益、AI 推荐返佣 | 入口从搜索/广告转向 Agent 推荐与交易分发 |

应放入的案例：

- Visa 把 Visa 网络接入 ChatGPT，核心在于卡网络把持卡人授权、消费限额、商户限制、审批和争议处理带进 AI 入口。
- Mastercard Agent Pay 使用 tokenization / Agentic Token 思路，把 AI 发起的支付请求变成可追踪、带权限规则的支付凭据。
- Stripe Issuing 不是 AI 新产品，但它已经具备发卡、虚拟卡、卡面/卡函个性化、实时授权、spending controls、digital wallet token 等机制；这些机制解释了“权益类/联名卡/任务级受限支付凭据”为什么属于同一条凭据和授权主线。
- Stripe Link wallets for agents 和 Privy 钱包能力，应被解释为买方授权和钱包抽象，不只是“又一个钱包产品”。

这一层回答：

> AI 时代的支付入口，仍然绕不开“谁持有支付关系、谁定义权益、谁承担授权和争议责任”。联名卡/权益卡/Agent 钱包是一条线，不是三个孤立产品。

#### 6.3 工具化支付：MCP、skills、sandbox 和支付 API 给 Agent 用

要补上的核心点：

MCP 支付属于能力调用层变化。它改变的是支付能力被调用的方式：过去开发者读文档、写代码、调用 API；现在 Agent 通过 MCP server、skills、CLI、plain-text docs、llms.txt、sandbox 和工具描述来发现能力、组合参数、创建资源、测试交易。

Stripe 的对应动作：

| Agent 调用层 | Stripe 对应材料 | 商业含义 |
|---|---|---|
| MCP server | `mcp.stripe.com`、`docs.stripe.com/mcp` | 让 MCP-compatible client 直接搜索文档、交互 Stripe 资源 |
| Agent skills | `docs.stripe.com/skills`、skills catalog | 把最佳实践包装成 Agent 可安装指令 |
| Agent-first docs | plain-text docs、`llms.txt` | 把文档从人类阅读优化到机器读取 |
| sandbox / CLI | no-login sandbox、Stripe CLI | 降低 Agent 自动创建测试环境的摩擦 |
| agent toolkit | Stripe AI / agent toolkit | 把支付、计费、客户对象、产品对象接进 AI 应用开发 |

这一层回答：

> AI 时代支付公司的关键能力之一，是让自己的金融对象被 Agent 正确调用。谁的 API、docs、sandbox、skills 和 MCP 工具更机器可读，谁更容易成为 Agent 开发栈里的默认支付接口。

#### 6.4 协议化授权：AP2、ACP、MPP、x402 和机器支付

要补上的核心点：

当 Agent 真正替用户或企业花钱时，支付问题不只是“能不能扣款”，而是授权、真实性、责任、争议、清算和风控如何落地。Google AP2、OpenAI/Stripe ACP、Stripe MPP、x402、Visa Intelligent Commerce、Mastercard Agent Pay 都在争夺这个层。

协议层要解释的对象：

| 协议/机制 | 解决的问题 | 与 Stripe 路径的关系 |
|---|---|---|
| AP2 | 用 mandate / verifiable credential 证明用户授权、真实意图和责任边界 | 说明支付行业正在把“人类点击购买”改成“可审计授权链” |
| ACP / Instant Checkout | 把 AI 对话里的商品发现和购买接到商户订单与支付流程 | Stripe 进入 AI commerce surface |
| MPP / HTTP 402 | 让 API、内容、数据、服务可以被机器按价格/许可购买 | Stripe 把收款 API 延伸到机器可购买资源 |
| x402 | 把 HTTP 402 和稳定币/链上支付接到机器支付 | Bridge、stablecoin 和 machine payment 的新轨道 |
| Visa / Mastercard agentic payment | 把卡网络的 token、授权、争议、风控带进 Agent 交易 | 卡组织不是普通竞品，而是在定义网络规则层 |

这一层回答：

> MCP 解决“Agent 怎么调用工具”，AP2/ACP/MPP/x402 解决“Agent 调用后怎么形成可追责交易”。支付公司的 AI 机会不只在收单费率，而在谁能定义授权、凭据、责任和结算接口。

#### 6.5 回到 Stripe：为什么这些变化能接回公司路径

分七类变化：

| AI 后变化 | Stripe 做了什么 | 为什么符合长期战略 |
|---|---|---|
| AI 客户成为高强度客户 | 强化 Revenue suite、global tax、usage billing，并收购 Metronome | 延续收入运营战略，把订阅/发票扩到 token、event、usage、outcome |
| 交易入口进入 AI surface | Copilot Checkout、Agentic Commerce Suite、OpenAI/Google/Microsoft/Meta partner launches | 延续开发者和平台入口战略，让 Stripe 进入新的购买入口 |
| 商品表达机器可读 | ProductCatalogImport、seller docs、preview API、inventory/pricing feed | 延续领域模型战略，把商品、库存、价格、订单审批做成对象和接口 |
| 权益和凭据被重组 | Issuing、virtual cards、personalization designs、tokens、spending controls、Link wallets for agents、Privy、Shared Payment Token | 延续发卡/钱包/凭据抽象，把“卡 + 权益 + 授权”迁移到 Agent 可控模型 |
| 信用和赊账被数据化 | Capital、BNPL payment methods、Financial Connections、Identity、Capital underwriting、ML platform | 延续交易数据和风险基础设施战略，把商户现金流、消费分期、额度、还款和风控接进同一条交易链 |
| 支付能力被工具化 | MCP server、agent skills、plain-text docs、llms.txt、sandbox、agent toolkit | 延续 API-first 和开发者体验战略，把 Stripe 从人类开发者入口迁移到 Agent 开发入口 |
| 结算轨道扩张 | Bridge、Tempo、MPP、x402、stablecoin/machine payment docs | 延续新金融轨道接入战略，把稳定币和机器支付接入主栈 |
| 风险对象变实时 | Radar token theft、approval hook、AI Security JD、risk roles | 延续风险基础设施战略，把风险前移到注册、授权、工具调用和资源访问 |

收束判断：

> AI 没有推翻 Stripe 原有能力，而是验证了这些能力的可迁移性。Stripe 过去做的难事，包括领域模型、API、文档、发卡、计费、风控、钱包、稳定币和全球化，在 AI 客户和 Agent 交易中被重新定价。

### 7. 市场位置与增长

作用：

回答 Stripe 是否已经有足够规模进入系统级基础设施讨论。

主图：

- 处理规模：2023 $1T，2024 约 $1.4T，2025 $1.9T。
- GDP 等价口径：2023 1.0%，2025 1.6%。
- 估值/流动性：2021 $95B，2023 $50B，2025 $91.5B tender valuation。
- 同业参照：PayPal、Adyen、Worldpay/Global Payments、Block/Square、Checkout.com、Shopify Payments，只在口径可比处使用。

分析口径：

- 这里不是要硬算“全球支付市场份额”。
- 这里要说明 Stripe 的处理规模、增长速度、同业量级和能力覆盖，是否足够支持“公司战略正确性”的判断。
- take-rate、revenue sensitivity、同业 TPV 参照放在展开面板，不占主叙事。

同业视角必须分层，并把 AI 支付入口补进去：

- 卡组织 / 清算网络：Visa、Mastercard。它们掌握网络规则和卡组织清算，不是 Stripe 的同一类公司。
- 政策/监管/央行类基础设施：它们决定边界，不是商业竞争对手。
- PSP / gateway / acquirer / processor：Adyen、Worldpay、Checkout.com、Global Payments 等，是支付处理和企业商户竞争层。
- 钱包和超级 App：PayPal、Block/Square、Apple Pay、Shopify Payments 等，是商户、消费者和生态入口竞争层。
- AI 入口和协议层：OpenAI、Google、Microsoft、Anthropic/Claude ecosystem、AP2、ACP、MCP/A2A。它们可能不直接做清结算，但会争夺商品发现、意图捕获和 Agent 工具入口。
- 发卡/权益/凭据层：Visa Intelligent Commerce、Mastercard Agent Pay、Stripe Issuing、虚拟卡、tokenized credential、联名权益和平台卡。它们争夺的是“用户授权和支付关系”。
- 新金融轨道：stablecoin、crypto wallet、machine payment、agent commerce protocol 相关公司，是 AI 时代新增竞争层。

这一章回答：

> Stripe 不是在同一个平面上和所有公司竞争。它的策略是从支付处理层往开发者接口、商户经营、发卡/授权、收入运营、风险和新金融轨道上移，把竞争从费率变成系统能力。AI 时代的关键问题，是 Stripe 能否在 OpenAI/Google 这类入口、Visa/Mastercard 这类网络、Adyen/PayPal 这类支付同行、以及稳定币/钱包新轨道之间，保住自己的接口层位置。

### 8. 并购与能力补位

作用：

把并购从“大事件列表”改成战略补位图。

展示方式：

- 放在时间轴上。
- 同时提供能力补位视图。
- 每个节点显示：时间、补的缺口、对应战略、AI 时代是否重新变重要、来源强度。

初始映射：

| 并购/动作 | 补的能力 | 对应战略 | AI 时代意义 |
|---|---|---|---|
| Paystack | 区域支付和本地收单 | 全球化和本地化补位 | 支撑更多地区的新业务收款 |
| TaxJar / Recko | 税务、财务自动化、对账 | 收入运营和商户后台 | AI 公司全球化和税务复杂度上升 |
| BBPOS / Terminal | 线下支付和硬件入口 | 商户经营系统 | omnichannel 交易入口 |
| Lemon Squeezy | MOR、数字商品销售 | 软件和开发者产品销售 | AI 工具和数字产品销售路径 |
| Bridge | 稳定币编排和跨境结算 | 新金融轨道 | stablecoin settlement 进入主线 |
| Privy | 钱包抽象 | 买方/应用授权基础设施 | agent/app wallet 基础设施 |
| Metronome | usage/event/token 计费 | 收入运营 | AI 产品实时收入模型 |
| Issuing / card personalization / tokens | 发卡、权益、数字钱包 token、实时授权 | 发卡和权益入口 | 任务级受限支付凭据、联名权益、受限凭据和预算控制 |

### 9. 技术事件时间线

作用：

技术不是独立炫技章节，而是解释商业战略如何落成系统能力。

技术线必须回答：

- 这个技术选择服务哪个商业阶段？
- 它降低了谁的摩擦？
- 它如何扩大 Stripe 的能力边界？
- 它在 AI 时代是否被重新调用？

技术节点类型：

- API / SDK / docs / test mode
- PaymentIntent / Checkout Session / webhook
- Connect / Billing / Radar / Terminal
- Tax / Treasury / Issuing / Identity
- docs for agents、MCP、llms.txt、agent toolkit
- Issuing、virtual cards、personalization designs、tokens、spending controls、real-time authorizations
- ProductCatalogImport、preview API、seller docs
- MPP、x402、HTTP 402、machine payments
- Radar token theft、AI Security、risk jobs

### 10. 战略正确性验证图

作用：

用户问的“能力迁移地图”或“证据坐标”不应该只是图名。它真正要证明的是：Stripe 为什么能做到现在这个规模，这些战略选择是否被市场和产品结果验证。

建议改名：

- `战略正确性验证图`
- `战略复利图`
- `从战略选择到规模结果`

图的结构：

| 战略选择 | 能力沉淀 | 验证指标 | AI 时代复用 |
|---|---|---|---|
| 开发者入口 | API、SDK、docs、test mode、webhook | 开发者采用、客户扩散、文档/API source density | agents.md、MCP、llms.txt、agent toolkit、sandbox |
| 平台商户 | Connect、account model、分账、平台风控 | 平台/SaaS/marketplace 客户、处理规模增长 | agent commerce、merchant control、catalog integration |
| 收入运营 | Billing、Tax、Revenue suite、Invoicing | usage billing、global tax、AI 客户需求 | Metronome、streaming payments、token/event billing |
| 风险基础设施 | Radar、Identity、KYC/KYB、review、risk graph | Radar token theft、risk JD、fraud/risk roles | fake signup、token theft、tool misuse、approval hook |
| 发卡和权益入口 | Issuing、virtual cards、personalization designs、tokens、spending controls、real-time authorization | 发卡 API、卡面/卡函个性化、digital wallet token、授权控制 | AI 联名卡、任务级受限支付凭据、权益化支付入口、受限凭据 |
| 信用和赊账 | Capital、BNPL payment methods、Financial Connections、Capital underwriting、ML risk | Stripe Capital、Capital underwriting JD、BNPL docs、Financial Connections docs | Agent 受限信用、消费分期、商户营运资金、动态授信、实时还款和风险控制 |
| 全球化补位 | Paystack、TaxJar、Recko、BBPOS、本地支付 | 国际客户、新市场、税务/对账能力 | AI 公司 global-by-default |
| 新金融轨道 | Bridge、Privy、Tempo、MPP、x402 | stablecoin/wallet/machine payment product signals | machine payment、agent wallet、stablecoin settlement |

这一章回答：

> 不是“Stripe 做了很多事”，而是哪些选择形成了复利，并在 AI 时代继续有效。

### 11. 1000 条来源如何进入判断

作用：

解释研究材料如何支撑 H5，而不是展示链接数量。

展示方式：

- 来源热力图：时间阶段 x 来源类型。
- 第二视图：战略主题 x 来源类型。
- 每个格子展示 queued、read/classified、promoted 数量。
- 点击格子显示代表来源、进入正文原因、未进入正文原因。

来源类型：

- 官方年信 / 新闻稿
- docs / API / changelog
- 招聘 / JD
- GitHub / code / community
- partner / media / protocol
- research / risk

已知库存：

- 1000 条具体 URL。
- 487 条 docs/API/changelog。
- 292 条 jobs/JD，其中 260 条职位详情页。
- 160 条 GitHub/code/community routes。

这一章回答：

> 我们如何从 1000 条材料里形成分层判断？

### 12. 未来五年：Agent 支付会先过规则关，再过金融结果关

作用：

用历史发展规律判断当下所处阶段和未来五年的演进，而不是把 AP2、MPP、x402、MCP、Agent wallet 写成已经成熟的市场结果。

核心判断：

> Agentic payment 不是 Agent 获得金融主体地位，而是人、组织、商户、平台、网络和监管定义的金融规则，开始被软件读取、调用、限制、审计和清结算。AP2、MPP、x402 这类机制的意义，不是让 Agent 自主“想买就买”，而是把授权、预算、凭据、资源访问、争议和结算规则做成机器可执行协议。

#### 12.1 当前阶段：2026 大约在 L2.5

2026 年不能写成“Agent 金融已经成熟”。更准确的位置是：

| 层级 | 阶段名 | 说明 | 2026 判断 |
|---|---|---|---|
| L1 | 信息辅助 | AI 搜索、比较、摘要、推荐商品或服务 | 已成熟 |
| L2 | 任务执行 | AI 填表、准备订单、调用工具、生成 checkout，仍由人确认 | 正在规模化 |
| L3 | 受限交易 | 预算、商户、品类、时间、审批、凭据和撤销规则可以被系统执行 | 刚进入产品化 |
| L4 | 可审计金融执行 | 跨系统采购、结算、信用、机器支付、争议证据和审计轨迹连续成立 | 试点 / 协议阶段 |

本页可把当前点标成 `2026 / L2.5`：Agent 已经能执行任务和调用工具，但金融执行仍需要受限授权、凭据、争议、责任和监管框架补齐。

#### 12.2 四条成熟度曲线

这一章必须用折线图表达，不再使用卡片墙。图形要求：

- X 轴：2024、2025、2026、2027、2028、2029、2030、2031。
- Y 轴：L1、L2、L3、L4。
- 折叠或分层显示四条曲线：
  - 技术接入成熟度：API、MCP、skills、sandbox、agent toolkit、catalog feed。
  - 授权 / 责任成熟度：mandate、token、凭据限制、审批、撤销、争议证据。
  - 法规 / 网络规则成熟度：卡组织规则、消费者保护、稳定币、数据授权、跨平台责任。
  - 商业结果成熟度：转化率、收入、现金流、风险成本、信用条件、争议成本。

这张图的读法：

- 技术接入最快，2026 已经接近 L3。
- 授权 / 责任慢一拍，因为它要处理用户同意、预算、凭据、撤销和争议。
- 法规 / 网络规则更慢，因为它需要卡组织、监管、稳定币、消费者保护和跨平台责任边界形成共识。
- 商业结果最关键。只有当 AI/Agent 能持续带来更高转化、更低交易摩擦、更好现金流控制、更低风险成本或更优信用条件时，才算进入真正商业拐点。

#### 12.3 历史时间常数

历史类比不能写成“完全一样”，只能用来判断金融基础设施变化的时间常数：

| 类型 | 历史参照 | 大致时间常数 | 对 Agent 支付的启发 |
|---|---|---|---|
| 狭窄等价规则 | Check 21 这类既有工具电子化 | 1-2 年 | 如果只是把旧凭据或旧授权搬到新接口，推进较快 |
| 支付账户 / 数据开放 | PSD2、Open Banking、SCA | 3-5 年 | 当涉及账户权限、第三方接入、强认证和责任边界，时间明显拉长 |
| 货币 / 稳定币 / 钱包 | MiCA、稳定币监管、数字身份钱包 | 5-10 年 | 当涉及储值、结算、身份、跨境和消费者保护，制度成熟慢于产品发布 |
| 跨平台自动化金融执行 | Agent 授权、机器支付、动态授信、自动采购 | 5-10 年或更长 | L4 不是技术 demo，而是授权、审计、争议、清结算和追责共同成熟 |

#### 12.4 未来五年判断

| 时间 | 阶段判断 | 主要变化 | Stripe 相关观察点 |
|---|---|---|---|
| 2026-2027 | L3 形成 | 受限支付、任务级凭据、预算、审批、商户白名单进入可用产品 | Link wallets、Issuing、spending controls、MCP、Agentic Commerce、ACP |
| 2027-2028 | L3 加深 | 商品、价格、库存、税务、退货、权益、订阅和 API 资源更机器可读 | catalog feed、Checkout、Billing、Tax、Radar、Revenue suite |
| 2028-2029 | L4 试点扩大 | API、内容、算力、数据、广告、库存采购等高频小额或 B2B 场景开始机器支付 | MPP、x402、Bridge、stablecoin、Metronome、Financial Connections |
| 2029-2031 | 早期制度化 | 授权证据、争议、清结算、动态授信、审计和责任归因开始形成行业规则 | 卡网络规则、监管适配、Capital / BNPL / Issuing / Radar 组合能力 |

#### 12.5 真正的商业拐点

不能把“AI 增效”直接写成奇点。更专业的表达是：

> AI/Agent 的商业拐点，不是用户少点几下按钮，而是金融结果开始变化：更高转化率、更低交易摩擦、更稳定现金流、更低欺诈和争议成本、更好的授信价格或更快的资金周转。只有当这些结果可评估、可解释、可审计，并且责任边界清楚，支付公司、平台和商户才会把 Agent 交易从试点推向默认流程。

这也是“无 App 交互”之外更重要的趋势：

- 搜索向履约迁移：用户不只要答案，而是要结果交付。
- 定价向 outcome 迁移：软件和服务更容易按完成结果、解决问题、用量、事件或金融结果计费。
- 分发向 Agent 生态迁移：谁能被 Agent 正确发现、调用、授权和结算，谁更接近交易入口。
- 授权向规则化迁移：预算、商户、品类、时间、审批和撤销成为机器可执行边界。
- 信用向动态化迁移：交易数据、现金流、身份、经营历史和还款表现可能影响额度、账期、费率和准入。

### 13. 我们能学什么

作用：

把 Stripe 的路径变成可复用的商业分析框架。第 12 章判断未来，第 13 章才收束方法论。

#### 13.1 主体是人和制度，AI 改变成本结构

单独讨论“AI 生存”没有意义。支付和金融行业的主体仍然是人、组织、商户、平台、监管、卡组织、银行和用户之间形成的关系。AI 降低的是 coding、集成、测试和定制化实现成本；没有降低，甚至会抬高金融产品的设计、评估、解释、审计和责任归因成本。交易关系和信用关系仍然需要被定义：谁参与、谁授权、谁履约、谁承担风险、谁负责争议、资金如何清结算、信用如何授予和回收。

#### 13.2 支付公司的 AI 融合不是模型转发

AI Hub 或平台转发模式，更接近批发商逻辑：聚合流量，转发模型能力，用规模换议价权，用计量和路由赚差价。支付公司的 AI 融合逻辑不同。支付公司不是只把 AI 接进来做转发，而是把 AI 放进支付和金融对象里：账期方案、订阅和用量计费、授信和额度、风控和争议、商户 onboarding、资金流和清结算。

#### 13.3 账期、Billing 和信用是新的想象空间

Stripe Billing、Revenue suite、Metronome、Capital 和 Financial Connections 指向同一个方向：支付公司可以不只处理付款，还可以帮客户设计收入确认、用量计费、账期、分期、授信、还款和风险控制。AI 让这些方案更容易被配置、解释、测试和自动运营。

对客户来说，价值不是“我能不能自己用 AI 写一个账单系统”，而是支付公司能否把账期方案、usage billing、税务、风控、授信、争议和清结算组合成可信的业务能力。这个方向有想象空间，但前提是产品设计必须穿过监管、会计、税务、数据安全、消费者保护和资金流规则。

#### 13.4 金融创新最终比的是关系设计

支付和金融行业的创新，往往不是单点技术突破，而是在既有法规和行业规则中形成新的可接受边界。Agent 钱包、任务级受限支付凭据、BNPL、商户融资、稳定币结算、机器支付和 MCP/API 调用，都要回答同一组问题：授权是否清楚、责任是否可追溯、风险是否可控、消费者或商户是否被保护、清结算和争议处理是否有规则。

所以本 H5 的最终结论应该收敛为：

> AI 时代的支付创新，不是把金融能力重新命名，也不是让 AI 直接替人付钱。真正的竞争在于：谁能围绕人、组织和制度关系，在法规、网络规则和商业共识之内，把交易关系和信用关系设计成更好用的对象模型、API、计费方案、授权规则、风控系统和生态组合。Stripe 的参考价值，是它长期把复杂金融关系产品化、接口化和嵌入式部署，这使它更有机会在 AI 时代继续成为新业务的第一接入点。

## 视觉设计要求

这页应该像公司演进 atlas，不像 dashboard dump。

### 视觉方案：Stripe Evolution Atlas

核心视觉隐喻：

> 一条时间脊柱，叠加三组坐标：嵌入位置、金融关系、证据强度。

这套视觉不是把资料做漂亮，而是让读者能同时看见三件事：

1. Stripe 的位置如何迁移：支付 API -> 嵌入式支付 -> 嵌入式金融 -> Agent/AI 工作流中的交易与信用执行。
2. 交易关系和信用关系如何被对象化、接口化、计费化、风控化和合规化。
3. 每个判断背后有哪些原文、指标、产品、并购、JD 或二级材料支撑。

### 视觉系统

页面使用克制的报告型视觉，不做科技感海报，不做装饰性大渐变，不做词云。

| 视觉元素 | 用途 | 规则 |
|---|---|---|
| 时间脊柱 | 2010-2026 公司演进主轴 | 全页贯穿；拖动年份时同步刷新阶段、指标、并购、技术、AI 事件 |
| 嵌入位置阶梯 | 表达 Stripe 从 API 到 embedded finance 再到 Agent workflow 的位置迁移 | 四级阶梯：API 接入、平台内支付、平台内金融、Agent 内交易/信用 |
| 双关系轨 | 表达交易关系线与信用关系线 | 两条并行轨道固定颜色，后续所有事件必须落到其中一条或两条 |
| 证据抽屉 | 展示原文依据条 | 每个节点点击打开：source_id、原文摘引、支撑判断、边界 |
| 小倍数图 | 对比市场指标、同业口径、阶段变化 | 不把 TPV、收入、估值混进一张图 |
| 能力补位带 | 展示并购和能力缺口 | 并购节点只显示“补什么缺口”，不做新闻列表 |

建议色彩：

| 类别 | 颜色用途 |
|---|---|
| 公司战略 | 深墨色主线 |
| 市场/指标 | 青蓝色 |
| 并购/补位 | 琥珀色 |
| 技术/对象模型 | 绿色 |
| AI/Agent | 紫灰色少量点缀 |
| 信用/风险 | 暗红色 |
| 来源强度 | 灰阶 + 实心/描边/虚线状态 |

避免单一蓝紫主题。整体背景使用浅灰白，不使用深蓝大屏、霓虹渐变、玻璃卡片、漂浮球、词云墙。

### 首屏视觉

首屏不是营销 hero，而是研究控制台。

结构：

1. 顶部标题区：`Stripe 公司演进与 AI 时代支付变革`。
2. 主图：2010-2026 时间脊柱横穿首屏，分四段显示嵌入位置迁移。
3. 左下：处理规模折线，显示 2023 $1T、2024 约 $1.4T、2025 $1.9T。
4. 右下：来源状态条，显示 promoted / classified / queued，不展示“1000 条结论”。
5. 时间脊柱下方：两条金融关系轨，`交易关系` 与 `信用关系`。

首屏必须让读者一眼看出：

- 这是公司路径，不是 AI 功能盘点。
- 主线是嵌入式支付到嵌入式金融，再到 Agent workflow。
- AI 改变的是成本结构和执行方式，金融关系的设计、评估和治理仍然是核心。

### 主时间轴视觉

主时间轴是全篇核心交互。

布局：

| 轨道 | 显示内容 | 交互 |
|---|---|---|
| 战略轨 | 阶段战略押注、目标客户、商业模式影响 | 点击显示阶段战略卡 |
| 市场轨 | 处理规模、GDP 等价口径、估值/流动性、同业参照 | 悬停显示口径和来源 |
| 并购轨 | Paystack、TaxJar、Recko、BBPOS、Bridge、Privy、Metronome 等 | 点击显示能力缺口和补位逻辑 |
| 技术轨 | API、Connect、Billing、Radar、Treasury、Issuing、MCP、x402 等 | 点击显示对象模型和商业影响 |
| AI/Agent 轨 | Agentic Commerce、Copilot Checkout、Link wallets、MCP/skills、MPP | 点击显示交易关系和信用关系变化 |
| 证据轨 | promoted / classified / queued 来源密度 | 点击打开原文依据抽屉 |

交互规则：

- 年份滑块可拖拽。
- 点击年份，六条轨道同步高亮。
- 点击事件节点，右侧打开证据抽屉。
- 节点大小代表影响范围，不代表证据强弱。
- 证据强弱用节点描边表达：实线为 promoted，虚线为 classified，浅描边为 queued。

### AI 支付重组专题视觉

这一章不能再做平铺卡片。使用五层系统图：

1. 底层：交易关系线与信用关系线。
2. 入口层：AI 对话、搜索、Copilot、agent marketplace。
3. 凭据/权益层：Link wallet、Issuing、virtual card、token、联名权益。
4. 工具/API 层：MCP、skills、agent toolkit、llms.txt、sandbox。
5. 协议/责任层：AP2、ACP、MPP、x402、授权证据、争议、清结算。

每层只回答一个问题：

| 层级 | 问题 |
|---|---|
| 交易/信用底层 | 这件事属于交易关系还是信用关系？ |
| 入口层 | 谁拿到用户意图和商品发现？ |
| 凭据/权益层 | 谁定义付款凭据、权益、预算和限制？ |
| 工具/API 层 | Agent 如何调用支付和商户系统？ |
| 协议/责任层 | 授权、审计、争议和清结算如何成立？ |

### 信用关系视觉

信用线必须单独可视化，不埋在风控里。

图形结构：

`交易数据 -> 授信判断 -> 额度/期限/价格 -> 使用场景 -> 还款来源 -> 逾期/争议/风控 -> 再评估`

Stripe 相关节点：

- Capital：商户融资和按销售还款。
- BNPL：checkout 中嵌入消费信用。
- Financial Connections：账户/现金流数据接口。
- Identity / Radar：身份、欺诈和风险信号。
- Issuing / spending controls：受限额度和可编程凭据。

视觉要求：

- 必须展示“授予”和“回收”两个方向。
- 必须把原文依据放进节点抽屉。
- 不把 Capital、BNPL、Financial Connections 写成同级产品清单，而是放进信用链路。

### 未来判断折线图

第 12 章必须用折线图或折叠折线图表达阶段判断，不再使用平铺卡片。

图形结构：

| 图层 | 展示内容 | 读者要看懂什么 |
|---|---|---|
| 时间轴 | 2024-2031 | 这不是产品发布表，而是金融基础设施成熟度判断 |
| 阶段轴 | L1 信息辅助、L2 任务执行、L3 受限交易、L4 可审计金融执行 | 当前不是 L4，不能把协议发布写成成熟市场 |
| 技术接入线 | API、MCP、skills、sandbox、catalog、agent toolkit | 技术接入最快成熟 |
| 授权 / 责任线 | token、mandate、spending controls、审批、撤销、争议证据 | 交易授权和追责慢于工具调用 |
| 法规 / 网络规则线 | 卡组织规则、稳定币监管、消费者保护、数据授权、跨平台责任 | 制度成熟慢于产品发布 |
| 商业结果线 | 转化率、收入、现金流、风险成本、信用条件、争议成本 | 真正拐点来自可衡量金融结果 |

视觉要求：

- 图上必须有 `2026 / L2.5` 当前阶段标记。
- AP2、MPP、x402 只能作为协议/规则层节点，不能画成已经成熟的 L4 市场结果。
- 历史参照用底部小条显示：1-2 年、3-5 年、5-10 年三类时间常数；参照只解释节奏，不证明 Agent 支付会照搬历史。
- 移动端不能退化成四张文字卡，至少保留一条横向时间轴和四条可切换曲线。

### 市场与同业视觉

市场部分使用三组小倍数图：

1. Stripe 自身规模：processed volume 折线 + GDP 等价份额。
2. 同业量级参照：PayPal、Adyen、Worldpay/Global Payments 等，按可比口径分图。
3. 能力覆盖雷达：支付处理、平台、账单、风控、发卡、信用、钱包、稳定币、Agent 工具。

禁用：

- 不用单句“没有公开市场份额”带过。
- 不把 Stripe revenue sensitivity 写成像事实收入。
- 不把 TPV、收入、净收入、估值混在一张图里。

### 证据引用视觉

每章都要有可见的证据条，不把来源藏到页面尾部。

证据条格式：

| 显示元素 | 内容 |
|---|---|
| source_id | S001 / S008 / S172 等 |
| 原文摘引 | 25 个英文词以内或对应长度中文 |
| 支撑判断 | 这条原文支撑本章哪句话 |
| 边界 | 自披露、preview、JD、二级报道、地区可用性 |

桌面端：

- 每章右侧固定一个 `Evidence rail`。
- 点击节点打开完整证据抽屉。

移动端：

- 证据条折叠到每节标题下方。
- 原文摘引默认显示 1 条，展开后显示全部。

### 移动端视觉

移动端不退化成普通长卡片。

规则：

- 时间轴改为横向滑动年份尺。
- 六条轨道改为可切换 tab，但年份状态共享。
- 每节保留一个主图，不用纯文字替代。
- 证据抽屉从右侧改为底部 sheet。
- 图表标签不使用小于 12px 的文字。

### 视觉验收

进入 H5 实现前，设计稿必须满足：

- 每章有一个主视觉，不存在纯文字章节。
- 每个主视觉说明承载的商业问题。
- 每个节点能回到 source_id。
- 首屏能同时看到时间、嵌入位置、规模指标和来源状态。
- AI 专题图能看出交易关系线和信用关系线。
- 第 12 章能看出 L1-L4、2026 / L2.5、四条成熟度曲线和未来五年路径。
- 第 13 章作为最终结论出现，不能被“战略复利”“竞争位置”“信号分层”替代。
- 市场指标用图表表达，不用段落解释代替。
- 移动端保留时间轴和证据抽屉。
- 不使用词云作为研究深度证明。
- 不用内部概念当页面标题。
- 截图验收必须读回章节顺序和读者路径，不能只确认页面非空或关键词存在。

## 来源与边界模型

来源状态：

- queued：已有具体 URL。
- read：已打开、确认日期、摘要。
- classified：已归入年份、来源类型、战略主题。
- promoted：可支撑页面可见判断。

页面需要标注：

- 官方自披露，不等于独立审计。
- GDP 等价口径，不等于全球支付市场份额。
- 二级报道和 compiled sources 不能直接当 public-ready diligence。
- JD 是组织信号，不是战略事实本身。
- GitHub/community 是采用和摩擦线索，不是市场份额证明。

## 章节原文引用规则

每个可见章节必须带一个“原文依据条”。它不是脚注装饰，而是进入正文的硬门槛。

原文依据条字段：

| 字段 | 要求 |
|---|---|
| source_id | 对应 source pack 的来源编号 |
| source_type | official annual / newsroom / docs / API / JD / partner / media |
| original_quote | 原文摘引，单条来源不超过 25 个英文词或对应长度中文摘引 |
| supports | 这句原文支撑本节哪一个判断 |
| boundary | 自披露、二级报道、地区可用性、产品 preview、JD 信号等限制 |

章节规则：

- 每个一级章节至少 2 条原文依据，其中至少 1 条来自官方年信、newsroom、docs、API 或 JD。
- 每个数据图必须把数据点映射到来源编号，不能只写“来源：Stripe”。
- 每个产品或机制名第一次出现时，必须能点开来源依据。
- 分析词可以使用，但必须标注为分析词。例如“任务级受限支付凭据”可以作为归纳词，但页面要同时展示 Stripe 原文：`a one-time-use card is issued per task`。
- 无法找到原文依据的词，不进入 reader-facing 正文，只能放在内部草稿或待核验队列。
- 每章末尾设置 `证据边界`，说明哪些是已核验事实，哪些是分析推断，哪些需要后续 provider/source follow-up。

首批必须前置的原文依据：

| 章节 | 原文摘引 | 来源 |
|---|---|---|
| 嵌入式金融主线 | `embedding financial services into your platform, including accounts, cards and financing` | S172 |
| Agent 受限支付凭据 | `a one-time-use card is issued per task` | S008 |
| Agent 受限支付凭据 | `you approve each payment` | S008 |
| Stripe Capital 信用线 | `eligibility is based on factors like your payment volume and history on Stripe` | S167 |
| Stripe Capital 回收线 | `Stripe deducts a fixed percentage of your sales` | S167 |

## 验收标准

- 标题回到 Stripe 公司发展路径与 AI 时代变革。
- 首屏明确 2010-2026 时间跨度。
- 页面主图是公司演进时间线，不是抽象概念图。
- 每个阶段都按战略押注、目标客户、商业模式影响、能力沉淀、技术选择、并购补位、指标证据、AI 时代复用来分析。
- 主时间轴支持拖拽，并能并读公司战略、市场位置、并购补位、技术产品、AI 变化五条线。
- AI 后变化先给行业判断，再拆成交易关系线、信用关系线、权益化入口、工具化支付、协议化授权，并解释支付行业如何把联名权益、预授权、发卡、token、钱包、赊账/信用付/贷款、MCP/skills、AP2/ACP/MPP/x402、风控和清结算升级给 Agent。
- 赊、信用付和贷款不能缺席。必须把 Stripe Capital、BNPL payment methods、Financial Connections、Identity、Radar、Capital underwriting JD 和 ML platform 放进一条“信用关系线”，解释它们如何把交易数据、现金流、额度、还款和风险连起来。
- 联名卡/权益卡不能缺席。必须把它与 Issuing、virtual card、personalization designs、tokens、spending controls、Link wallets、Visa/Mastercard agentic payment 案例放在同一条“权益化入口”线上。
- MCP 支付不能缺席。必须解释 MCP/skills 是“支付能力工具化”，并区分 MCP 解决调用、AP2/ACP/MPP/x402 解决可追责交易。
- 市场位置有折线增长图、同业参照和口径分层，不再只写口径声明。
- 页面解释行业竞争格局：卡组织、监管/政策基础设施、PSP/acquirer/gateway、钱包/生态入口、AI 入口和协议层、发卡/权益/凭据层、新金融轨道分别处在哪一层。
- 页面解释 Stripe 如何通过 API、领域模型、文档、对象和规则，把竞争从费率竞争上移到系统能力竞争。
- 并购以时间和能力补位组织，不是列表。
- 技术事件有独立视角，并说明商业战略与技术选择的相互影响。
- 每个可见章节都有原文依据条；没有原文引用的判断不能进入正文。
- 无来源产品化词不得出现；使用“任务级受限支付凭据”等分析词时，必须同步展示原文依据和来源边界。
- 有一张战略正确性验证图，说明战略选择如何转化为能力沉淀、指标结果和 AI 时代复用。
- 1000 条来源以热力图或矩阵表达，不再用词云。
- 页面不使用 `交易控制面` 作为读者标题或核心概念。
- H5 仍是内部草稿，必须经过 screenshot QA、interaction QA、source integrity check 和 report gate review 后才能说 review-ready。

## 下一步不做什么

本轮不做：

- 读完全部 1000 条来源。
- Feishu 同步。
- public investment conclusion。
- 声称可审计全球市场份额。
- Stripe H5 之外的报告风格改造。
- 未列入后续实现计划的新数据补充。

## 自审

占位符检查：无占位符。

一致性检查：全文主轴改为时间线和公司发展路径。每个阶段都有商业分析口径，AI 后变化作为最新阶段和专题展开，并解释 Stripe 长期做 API、规范、领域模型和复杂基础设施的商业原因。

范围检查：这是一个 H5 重设计，范围限定在 Stripe H5、gate review notes 和必要视觉资产，不扩到其它报告。

歧义检查：后续实现必须围绕 `公司演进时间线 + 阶段商业分析 + 行业竞争格局 + 战略正确性验证 + AI 时代变革专题` 重建页面。不能继续从当前 `证据坐标` 模块修补，也不能再把内部分析工具写成读者标题。
