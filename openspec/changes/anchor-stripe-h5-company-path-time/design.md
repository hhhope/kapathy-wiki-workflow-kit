# Design: Anchor Company Path In Time

## Company Path

The section should be titled:

`2010-2026：五次战略位置迁移`

Each stage should visibly include:

- time range
- strategic choice
- capability accumulated
- resulting position

The cards should not read as product inventory. They should explain the causal
move that created the next position.

## Timeline Section

Replace:

`关键转折：Stripe 每次把自己嵌到更深的位置`

with a more concrete title such as:

`选择如何变成能力：Stripe 的阶段转折`

Replace the support paragraph with:

`这条线回答两个问题：Stripe 每一阶段选择服务谁，因此必须补出什么能力。开发者入口带来 API 和文档；平台客户逼出 Connect、分账和风控；资金账户把发卡、融资、税务和身份接进来；AI 公司放大用量计费和全球收入运营；Agent commerce 继续复用钱包、凭据、协议支付和风险证据。`

## Verification

- Static grep for rejected abstract heading and previous support paragraph.
- HTML parser.
- `git diff --check`.
- OpenSpec strict validation.
- Desktop/mobile screenshot readback focused on the company path and timeline
  title.
