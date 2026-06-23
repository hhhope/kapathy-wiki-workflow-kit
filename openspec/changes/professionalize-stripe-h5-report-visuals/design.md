# Design: Professional Stripe H5 Report Visuals

## Direction

Use a consulting / business-report visual language:

- fewer explanatory paragraphs
- clearer visual encoding
- source boundaries carried as footnotes or small labels
- titles that make business claims only when the visible section supports them
- no internal workflow language, no chat-language caveats, no decorative word
  clouds

## Target Repairs

### Transaction And Credit Rail

Replace the current friendly explanation with professional wording:

- transaction rail: `交易链路：需求、报价、授权、履约、清结算、争议`
- credit rail: `信用链路：准入、额度、定价、回收、逾期、复评`

The visual should look like an operating model, not two text cards. Use rows,
stage cells, and a compact thesis column.

### Evidence Pool Copy

Replace `不把 1000 条 queue 写成 1000 条结论` with a professional label such as:

`1000 条候选来源，结论仅引用已晋级证据`

### Volume Headline

Avoid unsupported headline wording. Use a source-aware headline:

`Stripe 官方处理规模：2023 $1.0T，2025 $1.9T`

Treat the 2024 figure as a trend bridge in the visual, not in the title.

### Timeline Premise

Keep the heading:

`关键转折：Stripe 每次把自己嵌到更深的位置`

Rewrite the support copy as business analysis:

`每一阶段都对应一次位置上移：从开发接入，到平台经营，到资金账户，再到 AI 公司收入运营和自动化交易。读这条线，是为了看商业压力如何沉淀成 API、账户、计费、风控、钱包和结算能力。`

### Evidence Encoding

Replace `证据维度` with `视觉编码` or `证据类型`. The timeline/detail should make
the encoding visible via legend strips, bars, or lane labels so the reader does
not need to click just to understand the chart grammar.

### AI Payment Restructuring

Avoid phrasing such as `AI 入口把...前移` or `Stripe 做基础设施，是为了...`.
Use market-structure language:

`AI 应用不会替代支付系统本身，但会改变交易发起和分发的位置。新的竞争集中在五个环节：需求分发、支付凭据、商户系统、结算轨道、风险与信用。Stripe 的应对不是“让 AI 付款”，而是把这些环节重新接回自己的商户、钱包、计费、风控和结算能力。`

### Source Quote Section

The quote section should answer: "these citations protect which claims?" Use a
short framing title and gray quote blocks. Avoid making the section look like a
source-management dashboard.

### Signal Section

Replace the word-cloud-like signal matrix with grouped bars/lanes:

- technology interface
- commercial motion
- financial rails
- risk controls
- organization signal

Each lane should show representative signals as dense but consistent rows.

## Verification

- H5 rejected-phrase grep.
- HTML parser.
- `git diff --check`.
- OpenSpec strict validation.
- Desktop and mobile screenshots with visual readback focused on first-screen
  rails, timeline, AI section, source quote section, and signal section.
