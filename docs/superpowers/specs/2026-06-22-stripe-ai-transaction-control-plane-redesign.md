# Stripe AI 交易控制面 H5 重设计

## 路由状态

Route: brainstorm -> superpowers spec; OpenSpec 在本设计稿审核通过前保持只读。

本稿替换上一版失败的 `证据坐标` 修复方向。它是设计审核稿，不授权直接改 H5。

## 我们到底在做什么

这篇 H5 不是 Stripe 资料库，也不是把 1000 条 URL 摆出来证明“材料很多”。

我们要做的是一篇可阅读、可交互、可继续扩展成 PPT 或长报告的研究型 H5。它要回答一个问题：

> AI 时代，Stripe 认为交易系统正在变成什么？Stripe 把自己放在这个新系统里的什么位置？我们从它的公司路径、技术选择、并购、市场规模和招聘信号里能学到什么？

这篇 H5 要检验的核心判断是：

> AI 不是只让支付更智能，而是把交易从人的 checkout 流程，改成一套机器可发现、可读取、可计量、可授权、可结算、可风控的交易控制面。Stripe 的产品、并购、开发者接口、市场规模和招聘信号，都应该放到这些交易控制点上理解。

换句话说，我们不是在写“Stripe 很厉害”。我们是在研究：

- AI 到底改写了交易系统的哪些环节。
- Stripe 在哪些环节放了能力。
- 这些能力是自己长出来的，还是靠并购补的。
- 这些动作有没有市场规模支撑。
- 1000 条来源如何支持、限制或推迟这些判断。
- 我们如何把 Stripe 的路径抽象成金融 AI 基础设施的分析框架。

## 为什么当前稿失败

当前稿不是完全没材料，问题在于设计逻辑错了。

主要失败点：

- 把 `证据` 做成了读者主框架。读者看到的是证据坐标、证据节点、证据库存，而不是 Stripe 的战略位置。
- 市场面板、时间轴、AI 链路、能力图、词云、来源库存是并列模块。它们各讲各的，没有共同回答一个问题。
- BVP 参考只学到了 trend card 的表面格式，没有学到它“强主题 + 趋势 + 数据点 + implication”的报告结构。
- 1000-source queue 只是被展示成数量，读者看不出这些来源如何改变文章判断。
- 词云虽然可点击，但没有实际阅读价值。它没有过滤时间轴，没有展示信号密度，也没有把来源分类变成洞察。
- 并购被做成能力卡片，但没有叠回交易系统，看不出 Bridge、Privy、Metronome 分别补了哪个交易环节。
- 视觉增强停留在卡片、条形图、列表，没有形成一个能承载全文的主图。

下一版必须先解决“关系”，再解决“文案”。

## BVP 例子怎么用到 Stripe

参考页面：`https://www.bvp.com/atlas/state-of-the-cloud-2024`

BVP 页值得借鉴的不是视觉品牌，而是报告组织方式：

- 先给一个强主题。
- 再给少数几个趋势。
- 每个趋势有清楚的变化、数据点和影响。
- 图表服务趋势，不是把资料铺满。
- 读者可以跳转浏览，也可以顺着主线读完。

我们要借的：

- 一个主判断。
- 一组趋势块。
- 每个趋势固定结构：变化、Stripe 动作、关键数据/事件、影响、来源。
- 大图先行，细节后置。
- 数据点服务判断，而不是让数据点自己堆出来。

我们不要借的：

- BVP 的视觉风格、配色、插画和品牌感。
- VC 式预测口吻。
- 用宏大趋势替代事实证明。
- 直接照搬 AI Cloud 的趋势标签。

Stripe 的改造方式：

- BVP 的研究对象是 `AI Cloud`。
- 本文的研究对象是 `AI 交易控制面`。
- BVP 的五个趋势，在本文中变成交易系统的六个控制点。
- BVP 的 notable data points，在本文中变成 Stripe 的交易规模、并购、API/docs、合作发布、JD 信号和来源密度。

## 读者可见主标题和主判断

工作标题：

> Stripe：从支付 API 到 AI 交易控制面

首屏主判断：

> AI 不只是让支付更智能，而是把交易拆成机器可以发现、读取、计量、授权、结算和风控的系统。Stripe 的路径，是把支付、账单、风控、钱包、稳定币、协议和开发者工具接到这些控制点上。

页面里避免使用这些作为读者标题：

- `证据坐标`
- `核心判断`
- `原有能力底座`
- `市场位置计算面板`
- `能力迁移地图`
- 反复出现的 `不是...而是...`
- `proof tag`、`evidence lane`、`source queue` 这类生产过程标签

证据仍然存在，但它应该放在来源抽屉、source chips、图表脚注和附录里，不再站到页面最前面。

## 页面结构

### 1. 首屏：先把研究问题讲清楚

作用：

让读者一进来就知道这篇 H5 在证明什么。

首屏内容：

- 标题：`Stripe：从支付 API 到 AI 交易控制面`
- 副标题：AI 改写的是整个交易系统，不只是 checkout。
- 四个关键指标：
  - `$1.9T`：Stripe 2025 年处理规模。
  - `1.6%`：Stripe 自披露的 GDP 等价口径。
  - `288`：Sessions 2026 发布的产品和功能数量。
  - `1000`：具体 URL 来源队列，但标注为 triage queue，不等于 1000 条结论。

视觉：

- 首屏不再是普通 hero 图加卡片。
- 首屏应该露出一张主系统图。
- 六个交易控制点在第一屏就能看到。
- Stripe 的产品、并购、API、协议和 JD 信号以标记形式挂在图上。

### 2. 主图：AI 交易控制面

作用：

承载整篇文章的关系。后面的时间轴、市场图、并购图、来源热力图都回到这张图。

横向六个控制点：

1. 交易入口
2. 商品表达
3. 计费与计量
4. 买方授权
5. 结算轨道
6. 风险控制

每个控制点展示五件事：

- 原来的交易对象是什么。
- AI 时代变成什么。
- Stripe 放了什么能力。
- 哪类来源支持这个判断。
- 还有什么证明边界。

初始映射：

| 控制点 | 原交易对象 | AI 后交易对象 | Stripe 信号 |
|---|---|---|---|
| 交易入口 | 网站、App、商户 checkout 流量 | Copilot、Gemini、ChatGPT、agent surface | Copilot Checkout、Agentic Commerce Suite |
| 商品表达 | 商品页、SKU、checkout 参数 | catalog feed、inventory feed、pricing feed、order approval | ProductCatalogImport、15-minute inventory/pricing refresh、Checkout Session fulfillment |
| 计费与计量 | 订阅、账单、发票 | token、event、usage、outcome | Billing、Revenue suite、Metronome、streaming payments |
| 买方授权 | 输入卡号、保存支付凭据 | wallet、one-time token、approval hook、Shared Payment Token | Link wallets for agents、SPT、Privy |
| 结算轨道 | card rails、银行 payout | stablecoin、MPP、x402、machine payment | Bridge、Tempo、machine payments docs |
| 风险控制 | 盗卡、拒付、支付欺诈 | token theft、fake signup、prompt/tool misuse、resource abuse | Radar token theft、AI Security JD、seller approval hook |

交互要求：

- 点击某个控制点，下方所有板块按该控制点过滤。
- hover/click 时出现来源 chips 和来源强度。
- 颜色代表控制点，不代表笼统的证据类别。

### 3. 趋势块：用 BVP 的结构讲六个控制点

作用：

用统一语法解释每个控制点，而不是每段都换一套说法。

每个趋势块固定五栏：

- `变化`：交易系统哪里变了。
- `Stripe 动作`：Stripe 在这个位置放了什么能力。
- `关键数据/事件`：3-5 个硬标记。
- `影响`：这说明 Stripe 的位置发生了什么变化。
- `来源`：已晋级来源和证明边界。

示例：交易入口

- 变化：交易入口从商户网站进入 AI surface。
- Stripe 动作：Copilot Checkout 和 Agentic Commerce Suite 把 Stripe 放进 agent-driven discovery 和 purchase flow。
- 关键数据/事件：Microsoft Copilot Checkout、Agentic Commerce Protocol、Shared Payment Token、Sessions 2026 中 Google/Gemini 相关发布。
- 影响：Stripe 不只是处理 checkout，它在争夺 agent、商户和买方凭据之间的交易接口。

### 4. 三维时间轴：这些控制点何时形成

作用：

时间轴不是主论点，而是历史证明层。它回答：Stripe 是怎样一步步从支付 API 扩到 AI 交易控制面的。

三维结构：

- x 轴：时间，从 2010 到 2026。
- y 轴：信号轨道。
- 第三维：这个节点加强了哪个交易控制点。

信号轨道：

- 公司规模和经营路径。
- 市场位置、估值和流动性事件。
- 并购和能力缺口。
- 产品与 API。
- AI 协议和合作发布。
- 组织、JD 和风险信号。

交互要求：

- 年份可拖拽。
- 节点颜色按六个控制点统一。
- 每条轨道有清楚图标或标签。
- 每个节点打开详情抽屉。
- 详情抽屉只讲三件事：发生了什么、为什么重要、来源强度。

关键年份锚点：

- 2010-2014：API、SDK、文档、测试环境形成可编程支付入口。
- 2015-2019：Connect、Billing、Radar、Terminal 和平台/SaaS 客户让 Stripe 进入商户经营层。
- 2020-2022：Treasury、Capital、Identity、Tax、Issuing，以及 Paystack、TaxJar、Recko、OpenChannel、BBPOS，补深金融运营能力。
- 2023：$1T 处理规模和 AI 客户压力，让 billing、tax、risk 变得更关键。
- 2024：usage billing、stablecoin、agent tooling 和 Bridge 进入主叙事。
- 2025：$1.9T、1.6% GDP 等价口径、5M+ businesses、Bridge/Privy/Metronome、claimable sandboxes。
- 2026：Copilot Checkout、Sessions 2026、Link wallets for agents、streaming payments、Radar token theft、HTTP 402、MPP、x402。

### 5. 市场位置图：Stripe 是否有资格进入系统级讨论

作用：

回答一个很具体的问题：Stripe 的规模是否足以支撑“AI 交易基础设施候选者”这个讨论。

读者可见判断：

> Stripe 披露的处理规模已经足够大，可以把它作为 AI 交易基础设施候选者来分析。但页面不能把它写成已经拥有可审计的全球支付市场份额。

主视觉：

- 处理规模增长线或阶梯面积图：`$1T -> ~$1.4T -> $1.9T`
- GDP 等价口径变化：`1.0% -> 1.6%`
- 同业参照条形图：PayPal、Adyen、Worldpay/Global Payments，能比的才比。
- take-rate 敏感性放抽屉，不做主画面。

规则：

- 不再出现 `两公司 TPV 参照` 这种读者看不懂的标签。
- 不把巨大收入敏感性区间放在主画面吓人。
- 主画面讲增长和相对量级。
- 公式和口径放在可展开抽屉里。
- 每个数字标清楚：官方自披露、二级报道、同业机制参考。

### 6. 并购覆盖图：并购补了哪个控制点

作用：

并购不是大事件列表，而是能力缺口修补图。

它应该叠在主图上，而不是单独成为 M&A 列表。

映射关系：

| 动作 | 对应控制点 | 补的缺口 |
|---|---|---|
| Paystack | 结算 / 本地收单 | 区域支付覆盖 |
| TaxJar / Recko | 商户运营 | 税务、财务自动化、对账 |
| BBPOS / Terminal | 交易入口 / 支付场景 | 线下和 omnichannel |
| Lemon Squeezy | 商品与商户运营 | merchant-of-record、数字商品销售 |
| Bridge | 结算轨道 | 稳定币编排 |
| Privy | 买方授权 | 钱包抽象 |
| Metronome | 计费与计量 | usage、event、token、outcome rating |

交互：

- 有 `Acquisitions` 图层开关。
- 打开后，并购能力在主图对应控制点亮起。
- 点击并购节点显示：时间、来源强度、补了什么缺口、为什么和 AI 交易有关。

### 7. 来源热力图：替代词云

作用：

让 1000 条来源的工作方式可见，但不假装 1000 条都已经读完、都能支撑正文。

替代当前词云，改成矩阵：

- 行：来源类型
  - official annual/newsroom
  - docs/API/changelog
  - jobs/JD
  - GitHub/code/community
  - partner/media/protocol
  - research/risk
- 列：六个交易控制点
- 时间筛选：2010-2022、2023、2024、2025、2026

每个格子展示：

- queued 数量。
- read/classified 数量。
- promoted 数量。
- 代表来源。
- 为什么进入正文，或为什么暂时不能进入正文。

已知库存要展示：

- 1000 条 concrete URL rows。
- 487 条 docs/API/changelog。
- 292 条 jobs/JD，其中 260 条是职位详情页。
- 160 条 GitHub/code/community routes。
- promoted source count 单独显示，不能和 queue 数量混在一起。

这个板块回答：

> 这些来源如何塑造本文判断？

它不回答：

> 我们收集了多少 URL？

### 8. 我们能学什么

作用：

把 Stripe 分析抽象成我们自己的分析框架。

不要写成“Stripe 很先进”。要写成方法：

- 看 AI 金融基础设施，不只看产品名，要看交易对象是否被改写。
- 基础设施优势来自多个控制点的连接能力。
- 并购只有在补上控制面缺口时才是战略信号。
- docs、API、sandbox、SDK、MCP、llms.txt、sample repo 在 agent 时代也是分发面。
- 市场规模重要，因为没有足够交易量，控制面判断很虚。
- JD 信号只有绑定到具体控制点和具体日期时才有意义。

## 视觉风格

这页应该像 strategy atlas，不像 dashboard dump。

视觉规则：

- 只有一张主导图：AI 交易控制面。
- 少用独立卡片。
- 每个图表必须有明确任务。
- 颜色始终映射六个控制点。
- 来源细节放在抽屉、chips、脚注里。
- 不做装饰性词云。
- 不做卡片套卡片。
- 不把生产过程写进读者正文。
- 移动端保留主图逻辑，可以横向滚动或堆叠，但不能变回普通列表。

建议控制点配色：

- 交易入口：blue
- 商品表达：teal
- 计费与计量：amber
- 买方授权：violet
- 结算轨道：green
- 风险控制：red

## 来源与边界模型

H5 可以展示来源强度，但来源强度不能变成页面主框架。

来源状态：

- queued：已经收集具体 URL。
- read：已经打开、确认日期、摘要。
- classified：已经归入控制点和信号轨道。
- promoted：可以支撑页面可见判断。

读者可见来源标签：

- official self-report
- direct docs/API
- partner release
- job signal
- secondary report
- community/code route
- research/risk lens

边界写法：

- Stripe annual figures 是官方自披露，不是独立审计。
- GDP 等价口径不是全球支付市场份额。
- 2024 processed volume 如果没有更强来源，仍是 secondary/proxy。
- 二级来源整理出的并购时间线不能当作 public-ready M&A diligence。
- x402/MPP 安全研究是风险视角，不是 Stripe-specific failure claim。

## 验收标准

- 首屏明确提出 AI 交易控制面判断。
- 主图先解释交易变化和 Stripe 能力的关系，再出现来源库存。
- BVP 影响体现在结构上：主判断、趋势块、数据点、影响、可跳转章节。
- 时间轴是历史证明层，采用时间 x 信号轨道 x 控制点，不是平铺事件表。
- 市场位置用增长和相对规模图呈现，公式放抽屉。
- 并购显示在它修补的控制点上。
- 词云被来源热力图或信号矩阵替代。
- 1000 条来源被表达成 triage / promotion 系统，不写成 1000 条结论。
- 读者标题不使用 `证据坐标`、`能力迁移地图`、`核心判断` 等内部标签。
- 每个视觉组件都能用一句话说清它的任务。
- H5 仍是内部草稿，必须等 screenshot QA、interaction QA、source integrity check 和 report gate review 通过后，才能说 review-ready。

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

一致性检查：全文主对象是 AI 交易控制面。证据是支撑层，不是读者主框架。

范围检查：这是一个 H5 重设计，范围限定在 Stripe H5、gate review notes 和必要视觉资产，不扩到其它报告。

歧义检查：后续实现不能从当前 `证据坐标` 模块继续修补，必须围绕主控制面重建页面，再把时间轴、市场图、并购覆盖图和来源热力图接上去。
