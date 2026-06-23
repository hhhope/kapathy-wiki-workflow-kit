# Design: Stripe H5 Visual Language Polish

## Repair Targets

### First-Screen Volume Visual

Use a scale snapshot rather than a sloped line chart. The visual should show:

- 2023 official volume: `$1.0T`
- 2024 secondary-reported volume: `~$1.4T`
- 2025 official volume: `$1.9T`
- a visible growth arrow or callout showing the movement

The chart should not imply more precision than the source supports.

### Relationship Rails

Replace taxonomy labels with reader language:

- transaction relationship: "一笔生意怎么发生、授权、交付、结算、追责"
- credit relationship: "价值先给出去，后面怎么授信、定价、还钱、控风险"

Keep the underlying transaction / credit distinction, but present it as
business language.

### Five Position Migration

Use a connected path visual:

1. payment API
2. embedded payments
3. embedded finance
4. AI customer pressure
5. Agent workflow

The path should make the movement visible before the reader reads each detail.

### Market Section

Use a reader-facing headline and prose:

- title: `Stripe 到了多大体量`
- first paragraph: "先看 Stripe 自己的处理规模，再用同一年口径找参照。这样能看清量级，不把不同财务口径硬混成市场份额。"

Move caveats into short footnotes / boundary notes.

### Company Timeline Section

Replace process-language headings and instructions:

- avoid `并读`
- avoid opening with `拖动年份看`
- use a business-analysis claim such as `关键转折：Stripe 每次把自己嵌到更深的位置`
- make the timeline module visually stronger with a clear section badge,
  two-column heading treatment, and concise reader-facing premise

### Strategy Section

The strategy section can keep the title `哪些战略造就了 Stripe`, but the visual
should read like a strategic sequence / compounding chain, not a generic
mechanical matrix. Replace labels such as `壁垒读法` with a reader-facing
conclusion, for example:

> 这些选择最后变成难替代的位置：开发者先接入，平台把经营数据带进来，计费、风控、发卡、钱包和结算继续叠加，替换 Stripe 就不再只是换一个支付通道。

### AI Payment Restructuring Section

Remove generic AI phrasing such as "Agent can understand/call/limit/audit".
The section should say the concrete business problem:

> AI 入口把购物、订阅、API 调用和资金动作前移到对话、搜索和自动化工作流里。支付公司的问题不是让 AI 付款，而是把授权、预算、商户规则、授信、争议和清结算放回可执行的金融关系里。

Restyle the section as a control-point map:

- who captures the control point
- what value may be captured
- what Stripe must connect back into its infrastructure

Keep transaction and credit lines, but make the labels readable and concrete.

### Source Quote Section

Use one source-card grammar for every quote:

- source id
- source type
- business claim
- short original quote
- what it supports
- what it does not prove

The section title should not read like an internal instruction. Use a report
heading such as `关键判断必须能回到来源`.

### Signal Matrix

The signal section should not look like a decorative word cloud. Keep the
interactive filtering, but render signals as a categorized evidence matrix with
consistent cells:

- category label
- signal term
- source route / evidence route
- active state

The visible heading should say what the reader can do with the section, not
describe it as a generic technology/business/finance/risk/organization word
cloud.

## Verification

- Static grep checks for rejected phrases.
- HTML parser.
- `git diff --check`.
- OpenSpec strict validation.
- Desktop and mobile screenshots with visual readback focused on first screen
  migration path, company timeline heading, source-card styling, and signal
  matrix styling.
