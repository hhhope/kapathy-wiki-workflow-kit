# Design: Stripe H5 Evidence Coordinate Language Repair

## Reader-Facing Grammar

Use one visible naming system:

- `证据坐标 01｜规模与市场位置`
- `证据坐标 02｜时间轴：公司、市场、并购、技术、AI`
- `证据坐标 03｜能力缺口：并购补位`
- `证据坐标 04｜AI 交易链路`
- `证据坐标 05｜信号索引：技术、商业、金融、风险`
- `证据坐标 06｜能力迁移`
- `证据坐标 07｜证据库存与边界`

Avoid rhetorical or chatty headings. Headings should name the coordinate and
the evidence job.

## Signal Cloud

The signal cloud must be interactive:

- each term is a button, not static text
- clicking a term updates a detail panel
- detail panel shows category, what it proves, source count or source route,
  and evidence boundary
- category filter buttons should support technology, business, finance, risk,
  organization, and all

## Source Inventory

The H5 must not imply 22 evidence nodes are the full source base. It should show
the 1000-source queue as grouped inventory:

- 1000 concrete URLs
- 487 docs/API/changelog
- 292 jobs/JD
- 160 GitHub/code/community
- 45 official/partner/media/protocol/regulatory/research/community routes
- 17 verified/promoted rows

The page should explain that 22 coordinate nodes are high-level proof nodes, not
the full source count.

## Verification

- rejected heading grep returns no hits
- HTML parses
- signal buttons exist and are wired to data
- screenshots refreshed
- gate review records the follow-up repair
