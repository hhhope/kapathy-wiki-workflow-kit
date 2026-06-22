# Stripe 公司演进与 AI 时代变革 H5 设计稿

## 路由状态

Route: brainstorm -> superpowers spec; OpenSpec 在本设计稿审核通过前保持只读。

本稿是重新锚定后的中文审核稿。它不再把内部分析概念写成标题，也不再按“材料模块”堆页面。它把 Stripe 当作一个公司案例做商业分析：**这家公司如何选择战略楔子，如何扩张能力边界，哪些选择造成了今天的位置，AI 时代又如何重新放大或改写这些能力。**

## 这篇 H5 到底要回答什么

主问题：

> Stripe 如何从一个支付 API 公司，演进为可以承接 AI 时代新交易需求的金融基础设施公司？

拆成四个商业分析问题：

1. **路径问题**：Stripe 在 2010-2026 每个阶段解决的核心商业问题是什么？
2. **战略问题**：哪些长期战略选择造就了 Stripe 的能力结构？
3. **变化问题**：AI 时代之后，客户需求、交易入口、计费、结算、风险发生了什么变化？
4. **启发问题**：我们如何用 Stripe 的路径理解 AI 金融基础设施，而不是只看产品发布？

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

## 推荐标题

主标题：

> Stripe 公司演进：从支付 API 到 AI 时代金融基础设施

副标题：

> 2010-2026 年，Stripe 的关键变化不是产品越来越多，而是它不断把商户收款、平台分账、订阅计费、风控、税务、钱包、稳定币和机器支付接进同一条交易基础设施路径。AI 时代让这条路径被重新放大。

备用标题：

- `Stripe 的发展路径与 AI 时代变革`
- `从 Stripe 看 AI 时代金融基础设施的演进`
- `Stripe 2010-2026：战略选择、能力扩张与 AI 交易变化`

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

> 这页从 2010 到 2026 追踪 Stripe 的公司演进。Stripe 先用 API-first 降低在线收款接入门槛，再把能力扩到平台分账、订阅计费、风控、税务、金融账户和全球化运营。AI 时代之后，AI 公司和 Agent 交易把原有能力重新推到前台：用量计费、商品数据、钱包授权、稳定币结算、机器支付和实时风控成为新的增长线索。

首屏要让读者立刻知道：

- 这是 Stripe 公司路径研究。
- 核心视角是 2010-2026 的时间变化。
- AI 时代不是凭空新增章节，而是前面战略积累的再解释。
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
| AI 时代金融基础设施 | 2025-2026 | Agent 交易、稳定币、钱包、机器支付和实时风控进入主线 | Bridge、Privy、Metronome、Link wallets、MPP、x402、Radar token theft | Stripe 把原有交易能力接入 AI 时代新交易形态 |

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
5. AI 变化线：2023 之后 AI 客户、Agent 交易、usage billing、stablecoin、machine payment、风险对象如何出现。

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

6. **新金融轨道接入战略**
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
| 新轨道接入 | Bridge、Privy、Metronome、MPP、x402、stablecoin、wallet | 把新金融轨道纳入同一套商业基础设施 |

为什么这能形成壁垒：

- **开发者默认选择**：谁定义了更好用的 API 和对象模型，谁就更容易成为新业务的第一接入点。
- **迁移成本**：一旦商户把支付、订阅、税务、风控、分账、账务和结算都接进同一套对象，替换成本远高于替换单个支付通道。
- **复合能力**：竞争对手可以复制一个功能，但很难同时复制支付、计费、税务、风控、全球化、本地支付、钱包和稳定币的组合。
- **行业抽象层**：Stripe 不是只和 PSP 比费率，它试图把自己放在更高的抽象层，成为开发者和商户理解金融复杂性的接口。
- **新场景复用**：AI 时代出现 Agent、usage billing、machine payment、stablecoin 时，Stripe 可以把旧能力重新组合，而不是从零开始。

这一章要回答：

> Stripe 的正确性不是“产品多”，而是它长期把行业复杂性标准化，并把标准化能力变成商业分发和锁定机制。

### 6. AI 时代后的变化：做了什么，以及为什么

总：

> AI 之后，Stripe 做的不是给支付加 AI 功能，而是把过去积累的 API、领域模型、计费、风控、钱包、稳定币和开发者工具，放到 AI 公司和 Agent 交易的新需求里。重点不是“它发布了什么”，而是这些动作如何延续它过去十五年的战略。

分六类变化：

| AI 后变化 | Stripe 做了什么 | 为什么符合长期战略 |
|---|---|---|
| AI 客户成为高强度客户 | 强化 Revenue suite、global tax、usage billing，并收购 Metronome | 延续收入运营战略，把订阅/发票扩到 token、event、usage、outcome |
| 交易入口进入 AI surface | Copilot Checkout、Agentic Commerce Suite、partner launches | 延续开发者和平台入口战略，让 Stripe 进入新的购买入口 |
| 商品表达机器可读 | ProductCatalogImport、seller docs、preview API、inventory/pricing feed | 延续领域模型战略，把商品、库存、价格、订单审批做成对象和接口 |
| 买方授权和钱包变化 | Link wallets for agents、Privy、Shared Payment Token | 延续账户/凭据抽象，把人的支付凭据迁移到 agent 可控的授权模型 |
| 结算轨道扩张 | Bridge、Tempo、MPP、x402、stablecoin/machine payment docs | 延续新金融轨道接入战略，把稳定币和机器支付接入主栈 |
| 风险对象变实时 | Radar token theft、approval hook、AI Security JD、risk roles | 延续风险基础设施战略，把风险前移到注册、授权、工具调用和资源访问 |

总：

> AI 没有推翻 Stripe 原有能力，而是验证了这些能力的可迁移性。Stripe 过去做的难事，包括领域模型、API、文档、计费、风控和全球化，在 AI 客户和 Agent 交易中被重新定价。

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

同业视角必须分层：

- 卡组织 / 清算网络：Visa、Mastercard。它们掌握网络规则和卡组织清算，不是 Stripe 的同一类公司。
- 政策/监管/央行类基础设施：它们决定边界，不是商业竞争对手。
- PSP / gateway / acquirer / processor：Adyen、Worldpay、Checkout.com、Global Payments 等，是支付处理和企业商户竞争层。
- 钱包和超级 App：PayPal、Block/Square、Apple Pay、Shopify Payments 等，是商户、消费者和生态入口竞争层。
- 新金融轨道：stablecoin、crypto wallet、machine payment、agent commerce protocol 相关公司，是 AI 时代新增竞争层。

这一章回答：

> Stripe 不是在同一个平面上和所有公司竞争。它的策略是从支付处理层往开发者接口、商户经营、收入运营、风险和新金融轨道上移，把竞争从费率变成系统能力。

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

### 12. 我们能学什么

作用：

把 Stripe 的路径变成可复用的商业分析框架。

结论方向：

- 基础设施公司的战略价值，不在于产品名多，而在于能否把复杂业务动作做成可复用接口。
- Stripe 的核心不是“做支付”，而是把混乱的行业流程抽象成领域模型、API、文档、规则和可复用对象。
- 看 AI 金融机会，要从交易对象和交易流程变化入手，而不是从 AI 功能清单入手。
- 看公司战略，要把并购、产品、API、JD、市场指标放回时间线。
- AI 时代的变化，经常不是全新能力，而是旧能力在新客户、新入口、新计费和新风险下被重新组合。
- 市场位置分析不能停在“没有公开份额”，要用处理规模、增长、同业参照和采用信号构建判断边界。

## 视觉设计要求

这页应该像公司演进 atlas，不像 dashboard dump。

主视觉结构：

1. 2010-2026 公司演进总时间线。
2. 公司战略 / 市场位置 / 并购补位 / 技术产品 / AI 变化五线并读。
3. AI 后变化专题图。
4. 同业基准和战略正确性验证图。
5. 来源热力图。

视觉规则：

- 时间轴是主角。
- 图表要服务商业问题。
- 不再使用词云证明研究深度。
- 不再用内部分析概念做页面标题。
- 颜色固定对应：战略、市场、并购、技术、AI、来源状态。
- 首屏增长指标必须优先用折线/阶梯面积图表达，不用孤立指标卡堆叠。
- 同业数据必须分口径呈现，不能把 TPV、收入、净收入、估值混在一张无解释图里。
- 移动端也保留时间主轴，不能退化成普通卡片堆叠。

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

## 验收标准

- 标题回到 Stripe 公司发展路径与 AI 时代变革。
- 首屏明确 2010-2026 时间跨度。
- 页面主图是公司演进时间线，不是抽象概念图。
- 每个阶段都按战略押注、目标客户、商业模式影响、能力沉淀、技术选择、并购补位、指标证据、AI 时代复用来分析。
- 主时间轴支持拖拽，并能并读公司战略、市场位置、并购补位、技术产品、AI 变化五条线。
- AI 后变化采用总分总，并解释 Stripe 做了什么、为什么这么做、如何延续长期战略。
- 市场位置有折线增长图、同业参照和口径分层，不再只写口径声明。
- 页面解释行业竞争格局：卡组织、监管/政策基础设施、PSP/acquirer/gateway、钱包/生态入口、新金融轨道分别处在哪一层。
- 页面解释 Stripe 如何通过 API、领域模型、文档、对象和规则，把竞争从费率竞争上移到系统能力竞争。
- 并购以时间和能力补位组织，不是列表。
- 技术事件有独立视角，并说明商业战略与技术选择的相互影响。
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
