---
layer: ops
domain: ai-workflow
ops_area: report-quality
canonical_object: stripe-ai-company-evolution
artifact_type: report-gate-review
title: "stripe-ai-company-evolution / report gate review"
status: draft
created: 2026-06-22
---

# Stripe AI Company Evolution / Report Gate Review

## Review Target

| Field | Value |
|---|---|
| Target title | 从 Stripe 看 AI 之后的金融基础设施 |
| Destination | `wiki/reports/stripe-ai-company-evolution-h5.html` |
| Scope | 首版高密度调研 H5 + source pack，聚焦公司发展路径、AI 后变化、发展规律、后续形态、金融领域 AI 可能性 |
| Non-scope | 最终 PPT、Feishu 同步、对外发布稿、1000 篇材料池完成声明 |

## Article Intent Contract

| Field | Value |
|---|---|
| Reader | 内部读者，需要快速理解 Stripe 为什么值得从 AI/金融基础设施角度研究 |
| Reader decision or action | 判断 1000-source queue 中哪些来源应继续晋级到 PPT、长 H5 或专题研究 |
| Main line | 采用 BVP-style trend report：先给出 AI 交易基础设施 thesis，再用五个趋势、三维时间轴、市场位置 lane、并购能力缺口、AI 交易链和证据坐标回答 Stripe 如何重新定位 |
| Non-goals | 不做投资建议；不把官方产品声明当独立效果证明；不推导中国监管落地结论 |
| User-owned judgments | 最终叙事强度、PPT 取舍、是否进入金融 AI 产品方案 |
| Agent-allowed work | 公开来源收集、证据矩阵、H5 初稿、后续阅读队列 |

## Reference Structure Map

| Reference | Reused element | Boundary |
|---|---|---|
| `https://www.bvp.com/atlas/state-of-the-cloud-2024` | 一个强主题、trend area、key takeaway、notable data points、implication 的报告组织方式 | 不复制 BVP 视觉品牌；只复用趋势报告的叙事骨架 |
| `inbox/Anthropic研发调研报告.pptx` | 公司演进、核心模块、内部实践、工程范式、启示的层次 | 不复刻具体 Anthropic 结论 |
| `wiki/reports/lixiang-luoyonghao-ai-agent-reading-board.html` | 脊柱 + 温度/强度地图 + 详情展开 | Stripe 不是访谈，不做“原文逐段”伪装 |
| `wiki/ops/anthropic-claude-code-khazix-article-report-gate-review-2026-06-10.md` | 事实矩阵、学习使用边界、非发布边界 | 本稿是调研板，不套公众号口吻 |

## Fact Verification Matrix

| Claim / data | Source | Verification result | Boundary |
|---|---|---|---|
| 2025 Stripe businesses generated $1.9T, about 1.6% global GDP, up 34% from 2024 | https://stripe.com/annual-updates/2025 and PDF lines 3-4 | Verified from official annual letter | Official self-report |
| Stripe powers more than 5M businesses directly or via platforms | 2025 annual letter PDF lines 4-5 | Verified | Official self-report |
| Stripe acquired Privy and Metronome; Metronome powers usage-based billing for OpenAI, Anthropic, Confluent, NVIDIA | 2025 annual letter PDF lines 12-16 | Verified | Official self-report |
| More than 100,000 claimable sandboxes created from AI coding tools | 2025 annual letter PDF lines 73-77 | Verified | Official self-report |
| 2025 acceleration is framed by Stripe as an LLM-enabled inflection | 2025 annual letter PDF lines 83-87 | Verified | Stripe hypothesis |
| Sessions 2026 announced 288 products/features for AI economic infrastructure | https://stripe.com/en-jp/newsroom/news/sessions-2026 lines 284-290 | Verified | Availability varies |
| Link wallets for agents use one-time-use cards per task and approval | Sessions 2026 lines 298-300 | Verified | Product claim; not tested |
| Streaming payments combine Metronome and Tempo for token-level micropayments | Sessions 2026 lines 302-305 | Verified | Product claim; not tested |
| Radar token theft blocked 3.3M risky sign-ups across eight AI businesses in one month | Sessions 2026 lines 307-309 | Verified | Vendor metric |
| Copilot Checkout uses Stripe and Agentic Commerce Protocol; SPT avoids exposing buyer credentials | https://stripe.com/en-jp/newsroom/news/microsoft-copilot-and-stripe lines 284-292 | Verified | Official partner release |
| AWS WAF + Stripe supports HTTP 402 and Machine Payments Protocol for AI traffic monetization | https://stripe.com/en-jp/newsroom/news/aws-waf-and-stripe lines 284-289 | Verified | AWS side still pending |
| Stripe docs expose agent-first tools: MCP, skills, CLI, llms.txt, Markdown docs | https://docs.stripe.com/agents.md lines 0-4 | Verified | Direct docs |
| `stripe/ai` contains agent toolkit, AI SDK, token-meter, MCP server notes | https://github.com/stripe/ai lines 279-299 | Verified | GitHub page snapshot |
| ACS seller integration uses product/inventory/pricing feeds, including 15-minute inventory and pricing refresh expectations | https://docs.stripe.com/agentic-commerce/for-sellers lines 5-7 | Verified | Direct docs; US availability noted |
| ACS feed upload uses `ProductCatalogImport` and `Stripe-Version: 2026-05-27.preview` | https://docs.stripe.com/agentic-commerce/for-sellers lines 8-13 | Verified | Preview API; not production-tested |
| ACS fulfillment can use `checkout.session.completed`, expanded CheckoutSession retrieval, and `Stripe-Version: 2025-12-15.preview` | https://docs.stripe.com/agentic-commerce/for-sellers lines 22-26 | Verified | Preview/private-preview fields included |
| ACS order approval hooks have a four-second timeout and require idempotency because agents may retry | https://docs.stripe.com/agentic-commerce/for-sellers lines 31-37 | Verified | Direct docs |
| Machine payments let agents pay for resources programmatically, including API calls/services, with charges as low as 0.01 USDC | https://docs.stripe.com/payments/machine lines 0-3 | Verified | Direct docs |
| Machine payments support Base/x402/USDC, Solana/MPP/USDC, Tempo/MPP/USDC, and Stripe card networks/MPP | https://docs.stripe.com/payments/machine lines 4-6 | Verified | Direct docs; availability varies |
| MPP returns HTTP 402 payment details, client authorizes payment, retries, pays, and gets resource access | https://docs.stripe.com/payments/machine/mpp lines 0-1 | Verified | Direct docs |
| MPP docs require `2026-03-04.preview` for crypto PaymentIntents | https://docs.stripe.com/payments/machine/mpp lines 11-13 | Verified | Preview API |
| x402 Stripe docs also use HTTP 402 and require `2026-03-04.preview` for crypto PaymentIntents | https://docs.stripe.com/payments/machine/x402 lines 0-8 | Verified | Direct docs |
| PyPI lists `stripe-agent-toolkit` 0.7.0, released Feb 12 2026, supporting OpenAI Agent SDK, LangChain, and CrewAI | https://pypi.org/project/stripe-agent-toolkit/ lines 23-31 and 81-119 | Verified | Registry snapshot |
| PyPI release history shows `stripe-agent-toolkit` existed by Nov 14 2024 and has releases through Feb 12 2026 | https://pypi.org/project/stripe-agent-toolkit/ lines 175-220 | Verified | Registry snapshot |
| `stripe-samples/machine-payments` demonstrates MPP and x402, with TypeScript/Python sample directories, Stripe Discord, and GitHub Issues as support routes | https://github.com/stripe-samples/machine-payments lines 255-305 | Verified | GitHub snapshot |
| Main timeline now merges company operating path, market position, acquisitions, technology events, and commercial/technical mutual influence | H5 timeline model and source addendum | Verified structurally | Narrative structure evidence; each factual claim still needs source boundary |
| Timeline now carries valuation/liquidity markers: $95B in 2021, $50B in 2023, $91.5B in 2025 | Axios/FT links added to source pack | Verified as secondary coverage | Private-company valuation/tender context, not public market cap |
| Timeline now carries processed-volume markers: $1T in 2023, around $1.4T in 2024, $1.9T in 2025 | Stripe annual updates plus secondary coverage | Verified with boundary | 2024 figure remains secondary/proxy; 2025 is official self-report |
| Market position is now handled as a scale/market evidence lane inside the trend report, not as a standalone calculation panel | H5 market-position section and three-dimensional timeline | Verified structurally | Public-ready version should promote direct PayPal 10-K and Adyen shareholder-letter tables |
| Stripe GDP-equivalent share increased from 1.0% in 2023 to 1.6% in 2025 under Stripe's own framing | Stripe 2023 and 2025 annual letters | Verified from official annual-letter pages | GDP ratio is not a payments-market share denominator |
| PayPal and Adyen are used as take-rate mechanics: revenue / TPV or net revenue / processed volume | PayPal secondary financial summary, Adyen IR entry, MarketWatch Q1 Adyen coverage | Partial-pass | Comparison only; different accounting models; not Stripe revenue proof |
| H5 now folds market-position evidence into the three-dimensional timeline: processed volume, valuation/liquidity events, and share-gain proxy wording | Stripe annual updates, Axios/FT/IBD, secondary compiled sources | Verified with boundary | Not a precise market-share estimate |
| H5 now folds acquisition/event evidence into the main timeline and AI timeline: Paystack, TaxJar/Recko, OpenChannel/BBPOS, Lemon Squeezy, Bridge, Privy, Metronome | Annual letter, Axios TaxJar, secondary compiled acquisition routes | Partial-pass | Original deal announcements still need promotion before public-ready use |
| AI transaction section is now led by a six-step chain from demand discovery to risk movement, with the draggable timeline as supporting evidence | H5 AI transaction-chain section | Verified structurally | Interaction state still needs console-event QA before review-ready |
| Capability map is now framed as evidence coordinates, not an independent proof or standalone conclusion | H5 evidence-coordinate section | Verified wording | Map node details still depend on source-promotion strength |

## Hard Gate Results

| Gate | Result |
|---|---|
| Reader intent | pass for internal draft |
| Reference structure | pass: BVP-style trend report shape selected and mapped |
| Learning/source use | partial-pass: verified source pack created, 1000-row concrete-source queue added, JD signal scan promoted, and expanded H5 system map / merged company-market-acquisition-tech timeline / AI timeline added; not all rows are read materials |
| Split strategy | pass: H5 for reading, source pack for material density |
| Voice | pass for internal research draft |
| Visual | partial-pass: standalone H5 structure rewritten and fresh desktop/mobile screenshots generated; console event check still not covered |
| Judgment ownership | pass: official claims are labeled as official/vendor claims |
| Publish | not applicable: no Feishu sync or public release |

## Residual Risks

- The previous 155-source pack was materially below the user's requested 1000-source ceiling. The queue has now been corrected to `wiki/sources/stripe-ai-company-evolution-1000-source-queue-2026-06-22.csv` with 1000 concrete URL rows and no `SEARCH:` placeholders, but most rows are still candidate URLs rather than read materials.
- Recruitment coverage now includes 292 Stripe jobs/JD URLs, including 260 concrete job-description pages. A focused JD scan has been added to the source pack and H5, but historical JD change claims still need archived snapshots or dated job-board mirrors.
- Several official claims are product-positioning or vendor metrics; they need partner/customer corroboration before stronger public claims.
- API/version-change section now has concrete ACS/MPP/x402 preview headers and object routes, but is not yet fully mined from Stripe changelog or package diffs.
- H5 has expanded desktop/mobile screenshots after the timeline restructure, but should still receive console-event QA and deeper interaction QA before review-ready.
- Community signals are still route-level for Discord, HN, Reddit, GitHub issues/PRs; next pass should sample actual discussions and classify friction.
- Company-path and big-event sections are now expanded, but older pre-2023 company-path milestones still need tighter official date sourcing before a public-ready version.
- Timeline now includes company/technology dual tracks and evidence metrics, but several valuation/acquisition details are secondary-source markers and must not be upgraded to investment-grade claims without independent checks.
- Market position is now visualized through calculated lenses: processed-volume growth, Stripe GDP-equivalent share, a small visible-TPV peer sample, and take-rate sensitivity. Do not turn these into global payment-market share without audited numerator and denominator.
- PayPal/Adyen take-rate comparisons are useful mechanics but remain partial until direct 10-K/shareholder-letter table extraction replaces secondary summaries.
- Acquisition/event evidence now appears inside the timelines, but Paystack/Recko/OpenChannel/BBPOS/Lemon Squeezy/Bridge/Privy deal rows still need direct original-source promotion for a public-ready version.
- A live re-anchor corrected the page style from abstract thesis language to research-control-surface language. Future edits should preserve this: source organization first, staged judgments second.
- A follow-up structure pass corrected the relationship between modules: the main timeline is the company/market/acquisition/technology sequence, the AI timeline is the transaction-chain sequence, and the comprehensive view is the capability-positioning layer.
- Main timeline and AI timeline interactions are browser-rendered and screenshot-checked at initial state; drag/click state changes still need console-event QA before review-ready.
- 2026-06-22 A-direction rewrite replaced the rejected visible chapter grammar with a BVP-style trend report, a three-dimensional evidence timeline, a capability-gap acquisition map, and an AI transaction-chain section. This improves structure but still requires fresh screenshot QA and interaction checks.
- 2026-06-22 follow-up repaired the remaining conversational headings into a unified `证据坐标` system, made the signal cloud clickable with 52 signal terms, and surfaced the 1000-source queue as grouped inventory rather than implying 22 proof nodes are the evidence limit.
- 2026-06-22 reader-language repair removed remaining process-language from visible H5 copy: hero, section descriptions, trend cards, timeline labels, signal detail labels, synthesis copy, and evidence inventory now use report-language instead of conversation/process wording.
- 2026-06-22 Atlas refinement replaced the rejected `证据坐标` reader surface with `Stripe Evolution Atlas`: first-screen time spine, processed-volume line, transaction/credit rails, embedded-finance path, AI five-layer payment restructuring, standalone credit flow, competition-position grid, strategy-validation grid, and source-id quote cards.
- 2026-06-23 drift repair records that the Atlas refinement still used the wrong acceptance boundary: it improved visual density and source handling, but did not preserve the Superpowers redesign's chapter 4-6 reader path. The repair is now owned by `openspec/changes/realign-stripe-h5-redesign-sections/` and tracked in `wiki/ops/stripe-h5-redesign-drift-retro-2026-06-23.md`.
- 2026-06-23 H5 section realignment added a visible `哪些战略造就了 Stripe` chapter with strategic choice -> capability accumulation -> later product / acquisition -> AI-era reuse rows.
- 2026-06-23 H5 section realignment added a visible `Stripe 为什么坚持做难事：API、规范和领域模型` chapter explaining domain models, API/docs/test mode, merchant operating abstraction, embedded risk/compliance, issuing/entitlement entry, and new rails as business strategy.
- 2026-06-23 H5 section realignment rebuilt the AI-era payment chapter around the redesign's 6.0-6.5 structure: infrastructure pressure, transaction / credit relationship lines, entitlement / credential entry, MCP tooling, protocol accountability, and return to Stripe's company path.
- 2026-06-23 visual-language drift cause: the prior repair treated the redesign spec as a section-presence checklist and did not hold the output to reader-facing copy and screenshot-visible visual standards. Static checks removed some rejected labels, but did not catch awkward report prose such as `并读`, `拖动年份看`, `壁垒读法`, generic AI phrasing, or decorative signal/quote styling. Screenshot review also looked too shallowly at initial layout instead of checking the exact sections the user later flagged.
- 2026-06-23 visual-language repair: `openspec/changes/polish-stripe-h5-visual-language/` now owns the follow-up. The H5 replaced the first-screen processed-volume line with a scale snapshot, rewrote transaction/credit rails into plain business language, converted the five-step company path into a connected visual, rewrote market/timeline/strategy/AI section copy, converted the AI chapter to a control-point map, normalized source quote cards, and replaced the decorative signal cloud with a categorized signal matrix.
- 2026-06-23 remaining boundary: the broad capability map in the lower interactive area remains long and dense. This repair deliberately focused on the user-flagged H5 sections and did not attempt a full redesign of the entire bottom map.
- 2026-06-23 professional-report repair cause: the previous visual-language repair still used friendly explainer copy and card-like modules where the user expected consulting-report visual grammar. The transaction/credit rail explained the idea in prose instead of carrying it as an operating model; the AI section still described "AI" as the subject rather than market-structure control points; the citation and signal sections still looked like source-management widgets.
- 2026-06-23 professional-report repair: `openspec/changes/professionalize-stripe-h5-report-visuals/` replaces the first-screen transaction/credit cards with two operating rails, changes evidence-pool and volume-copy wording, rewrites the timeline premise, rewrites the AI section around demand distribution / credentials / merchant systems / settlement rails / risk and credit, simplifies quote cards into gray quote blocks, and converts the signal area into grouped evidence lanes.
- 2026-06-23 company-path chronology repair cause: the previous repair kept `公司路径` and the timeline as separate mental models. The company-path module described five positions without visible dates, while the timeline heading preserved an abstract phrase the agent incorrectly judged as acceptable because the user had partially reacted positively to it. This left the reader without a clear answer to how each strategic choice, in a specific time period, accumulated into today's position.
- 2026-06-23 company-path chronology repair: `openspec/changes/anchor-stripe-h5-company-path-time/` anchors the path as `2010-2026：五次战略位置迁移`, adds visible year ranges to every path stage, rewrites cards around `战略选择 / 能力沉淀 / 成就位置`, and replaces the abstract timeline heading with `选择如何变成能力：Stripe 的阶段转折`.

## Verification Evidence

| Check | Result | Evidence |
|---|---|---|
| HTML parser | pass | `python3 -m html.parser wiki/reports/stripe-ai-company-evolution-h5.html` |
| Diff whitespace | pass | `git diff --check -- wiki/sources/stripe-ai-company-evolution-research-2026-06-22.md wiki/ops/stripe-ai-company-evolution-report-gate-review-2026-06-22.md wiki/reports/stripe-ai-company-evolution-h5.html` |
| Desktop screenshot | pass after A-direction rewrite | `wiki/reports/assets/stripe-ai-company-evolution/desktop.png` full-page screenshot shows the BVP-style trend cards, market-position lane, three-dimensional timeline, acquisition gap map, AI transaction chain, evidence coordinate map, and source cards without obvious overlap. |
| Mobile screenshot | pass after A-direction rewrite | `wiki/reports/assets/stripe-ai-company-evolution/mobile.png` full-page screenshot shows the same structure in a readable single-column layout with no obvious overlap. |
| Chinese rendering | fixed | Initial screenshots showed missing CJK glyphs; H5 now imports Noto Sans SC and screenshots render Chinese correctly. |
| Frontmatter precheck | inconclusive for target, blocked globally by legacy pages | `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target ...` returned existing unrelated legacy blockers and `target.entry_count: 0`; target pages include required fields from repair hints. |
| Console event check | blocked | `node -e require('playwright')...` failed with `MODULE_NOT_FOUND`; CLI screenshot still worked. |
| 1000-source queue row count | pass for concrete-source queue, not for read-material completion | `wiki/sources/stripe-ai-company-evolution-1000-source-queue-2026-06-22.csv` has 1000 data rows, 0 empty URL fields, 0 duplicate URL fields, and 0 `SEARCH:` placeholder rows. |
| Recruitment/JD coverage | pass for current-source queue and focused scan, partial for historical change evidence | CSV includes 292 `jobs-jd` rows: 260 concrete Stripe job-description pages and 32 Stripe jobs search pages. Focused read opened AI Security, AI Conversation Platform, Developer Productivity AI, ML Platform, Capital Underwriting, Crypto/Stablecoins, Privy, Stablecoin Audit/Reporting, and Radar/Fraud/Risk roles. Historical JD change analysis still needs archive or dated mirror evidence. |
| H5 source reference integrity | pass | Inline source key/reference check found 24 source keys, 66 H5 refs, and 0 missing referenced source keys after timeline expansion. |
| H5 source reference integrity after market-calculation repair | pass | Inline source key/reference check found 30 source keys, 81 H5 refs, and 0 missing referenced source keys. |
| Market-position visual repair | pass for structure | H5 now treats market position as a supporting scale/market lane and removes the rejected standalone calculation-panel framing. |
| H5 source reference integrity after A-direction rewrite | pass | Inline source key/reference check found 30 source keys, 81 H5 refs, and 0 missing referenced source keys. |
| OpenSpec strict validation | pass | `openspec validate rewrite-stripe-ai-company-evolution-h5 --strict` returned valid; only telemetry flush reported a network error after local validation. |
| Evidence-coordinate heading repair | pass | Rejected-heading grep returned no hits for the conversational headings flagged by the user. |
| Signal index interaction structure | pass | Static JS check found 52 unique signal terms, `signalDetail`, and the 1000-source inventory block. |
| Follow-up desktop/mobile screenshot | pass | Refreshed full-page screenshots show unified evidence-coordinate headings, clickable signal index region, and grouped source inventory with no obvious overlap. |
| Reader-language cleanup | pass | Static check over H5 visible templates excluding raw `signalTerms` data found no hits for rejected process terms such as `不是`, `不能`, `proof`, `Evidence lane`, `Proof tag`, `来源路由`, or `证据边界`. |
| CSV field correction | pass | Queue check uses `url_or_query`, not `url`: 1000 rows, 0 empty `url_or_query`, 0 duplicate `url_or_query`, 0 `SEARCH:` placeholders, 292 `jobs-jd` rows. |
| Live re-anchor trace | pass | `wiki/ops/stripe-ai-company-evolution-h5-reanchor-2026-06-22.md` records the user's correction: source organization, unified style, and evidence-bound wording. |
| Atlas refinement static checks | pass | `python3 -c "HTMLParser().feed(...)"` returned `html_parse_ok 119287`; `git diff --check -- wiki/reports/stripe-ai-company-evolution-h5.html openspec/changes/refine-stripe-h5-visual-atlas/* wiki/ops/stripe-ai-company-evolution-report-gate-review-2026-06-22.md` returned clean. |
| Rejected visible-label check after Atlas refinement | pass | H5-only grep found no hits for `证据坐标`, `能力迁移`, `核心判断`, `原有能力底座`, `市场位置计算面板`, `AI 交易基础设施`, `AI 交易链路`, `结论坐标`, `chain thesis`, `学法`, `Agent 任务卡`, or `总分总`. |
| Atlas desktop/mobile smoke screenshots | pass | `playwright screenshot file:///mnt/d/cloud/account-meeting-lore/wiki/reports/stripe-ai-company-evolution-h5.html /tmp/stripe-atlas-desktop.png --viewport-size=1440,1200` and the matching mobile command with `390,1200` both completed; visual readback showed the first-screen title, line chart, time spine, relationship rails, and metric cards without obvious overlap. |
| 2026-06-23 chapter-structure grep | pass | H5 grep found `哪些战略造就了 Stripe`, `Stripe 为什么坚持做难事：API、规范和领域模型`, `6.0 infrastructure pressure`, `6.1 交易 / 信用关系`, `6.2 权益 / 凭据入口`, `6.3 工具化支付`, `6.4 协议化授权`, and `6.5 回到 Stripe 路径`. |
| 2026-06-23 rejected visible-label check | pass | H5-only grep found no hits for `证据坐标`, `能力迁移`, `核心判断`, `原有能力底座`, `市场位置计算面板`, `AI 交易控制面`, or `transaction control plane`. |
| 2026-06-23 HTML parser | pass | `python3 -m html.parser wiki/reports/stripe-ai-company-evolution-h5.html` completed successfully after chapter realignment. |
| 2026-06-23 frontmatter precheck | partial / blocked by legacy pages | Target precheck for `wiki/ops/stripe-h5-redesign-drift-retro-2026-06-23.md` returned target repair hints, but whole-repo precheck remains blocked by unrelated legacy pages under `wiki/reports/shanghai-payment-*` and script producer warnings. |
| 2026-06-23 desktop/mobile visual smoke | pass with limitation | Refreshed screenshots at `wiki/reports/assets/stripe-ai-company-evolution/desktop-realign-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/mobile-realign-2026-06-23.png`, and `wiki/reports/assets/stripe-ai-company-evolution/fullpage-realign-2026-06-23.png`. Visual readback showed first-screen and full-page structure without obvious overlap, clipping, or blank blocks. Console-event QA remains uncovered in this environment. |
| 2026-06-23 OpenSpec strict validation | pass | `openspec validate realign-stripe-h5-redesign-sections --strict` returned `Change 'realign-stripe-h5-redesign-sections' is valid`; PostHog telemetry flush failed because network access to `edge.openspec.dev` was unavailable. |
| 2026-06-23 visual-language rejected phrase check | pass | H5 grep found no hits for the flagged phrases: `处理规模曲线`, `先看处理规模增长`, `同年同业参照`, `并读`, `拖动年份看`, `壁垒读法`, `可以理解、调用、限制、审计和追责`, `AI 时代的创新不在于重新发明`, `交易关系与信用关系被重新设计`, `GPT-era`, `AI 客户先改变收入系统压力`, `压力集中压到`, `信号矩阵：技术、商业、金融、风险和组织`, `原文引用：关键判断必须能回到来源`, `AI 客户压力`, `AI 客户收入`, `词云`, and `战略正确性`. |
| 2026-06-23 visual-language HTML / diff checks | pass | `python3 -m html.parser wiki/reports/stripe-ai-company-evolution-h5.html` and `git diff --check -- wiki/reports/stripe-ai-company-evolution-h5.html` both completed successfully after the visual-language repair. |
| 2026-06-23 visual-language screenshots | pass with limitation | Refreshed screenshots at `wiki/reports/assets/stripe-ai-company-evolution/polish-desktop-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/polish-mobile-2026-06-23.png`, and `wiki/reports/assets/stripe-ai-company-evolution/polish-full-desktop-2026-06-23.png`. Visual readback confirmed first-screen scale snapshot, mobile stacking, and full-page continuity. Python element screenshots for AI/source/signal sections were attempted but blocked by Chromium sandbox shutdown; CLI screenshots remained available. |
| 2026-06-23 professional-report rejected phrase check | pass | H5 grep found no hits for the newly flagged wording: `一笔生意怎么发生`, `价值先给出去`, `不把 1000`, `queue`, `处理规模从 1 万亿`, `这条时间轴不是事件列表`, `证据维度`, `AI 入口把`, `不被压回后台`, `用户意图可能被`, `关键判断必须能回到来源`, `证据矩阵：五类信号`, `word-cloud`, `谁在拿`, `可能拿走`, or `Stripe 要接住`. |
| 2026-06-23 professional-report screenshots | pass | Refreshed screenshots at `wiki/reports/assets/stripe-ai-company-evolution/professional-desktop-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/professional-mobile-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/professional-mobile-tall-2026-06-23.png`, and `wiki/reports/assets/stripe-ai-company-evolution/professional-full-desktop-2026-06-23.png`. Visual readback confirmed the first-screen operating rails, mobile 3-column rail stages, AI market-structure section, gray quote blocks, and grouped signal lanes. |
| 2026-06-23 company-path chronology rejected phrase check | pass | H5 grep found no hits for the rejected abstract path/timeline wording: `公司路径：五次位置迁移`, `关键转折：Stripe 每次把自己嵌到更深的位置`, or `每一阶段都对应一次位置上移`. |
| 2026-06-23 company-path chronology screenshots | pass | Refreshed screenshots at `wiki/reports/assets/stripe-ai-company-evolution/company-path-time-desktop-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/company-path-time-mobile-2026-06-23.png`, `wiki/reports/assets/stripe-ai-company-evolution/company-path-time-tall-desktop-2026-06-23.png`, and `wiki/reports/assets/stripe-ai-company-evolution/company-path-time-full-2026-06-23.png`. Visual readback confirmed visible year ranges in the path section and the new `战略选择 / 能力沉淀 / 成就位置` structure. |
| 2026-06-23 strategy topology and future chapters | pass | Static grep found `战略拓扑时间图`, `主干递进`, `横向补位`, `AI 复用`, `并购补位：按年份和能力层看`, `未来五年：Agent 支付先过规则关`, `2026 / L2.5`, L1-L4 labels, and `我们能学什么：金融创新最终比的是关系设计`; rejected visible phrase grep returned no hits for `并购 / 能力补位 lane`, `壁垒读法`, `证据维度`, `AI 公司把用量计费`, `这页从时间维度看`, or `Agent 工作流：商品发现`. |
| 2026-06-23 strategy topology visual screenshots | pass | Playwright screenshots were captured for desktop first screen, full desktop, full mobile, `#acquisition-scatter`, `#strategy-topology`, `#future-judgment`, and mobile `#strategy-topology`. Visual readback confirmed the acquisition timeline/scatter, strategy topology, Chapter 12 maturity line chart, and Chapter 13 learning board render without blank regions or obvious overlap. A CSS class collision with existing `.rail` was found in screenshot readback and repaired by renaming the new class to `.newrail`. |

## 2026-06-29 Domain-Language Realignment

### Article Intent Contract Update

| Field | Value |
|---|---|
| Reader | 80 人内部分享读者，需要从 Stripe 案例理解 AI 时代支付/金融能力建设 |
| Reader decision or action | 看到 AI 降低 coding 和对接成本后，真正稀缺的是把复杂金融交易设计成清晰、稳定、可组合的领域语言 |
| Main line | Stripe 切入 AI 支付快，不是因为临时追 AI，而是过去十五年持续做支付行业难而正确的工作：把商户、价格、订单、订阅、分账、身份、权限、风控、资金、结算和争议收敛成对象、接口和规则 |
| Non-goals | 不做 Stripe 必胜判断；不把 LinkedIn/JD 当成产品成功证据；不做 Feishu 同步、公开发布或 review-ready claim |
| User-owned judgments | 主线词改为 `金融交易设计语言`；LinkedIn 看在职人员能力图；JD 看能力补位 |
| Agent-allowed work | 将批准的主线落到 H5 章节、视觉模块、证据边界和验证记录 |

### Section And Paragraph Drift Review

| Section | Objective | Result | Action |
|---|---|---|---|
| 首屏 | 把主线从 AI 支付入口/控制层改为 `coding 成本下降后，领域设计语言成为壁垒` | pass | 已重写 lead、time spine 和交易/信用关系入口 |
| Chapter 2 | 解释为什么 Stripe 是观察样本，而不是公司介绍 | pass | 新增 `为什么用 Stripe 做观察样本`，比较大模型、钱包/卡组织、商户 SaaS/PSP、Stripe |
| Chapter 3 | 给出金融交易设计语言公式和零售/供应链类比 | pass | 新增 `AI 支付需要一套金融交易设计语言`，拆成对象、接口、权限、规则、资金关系、责任证据 |
| Chapter 4 | 证明 Stripe 的速度来自长期做难事的能力累积 | pass | `哪些战略造就了 Stripe` 改为 `Stripe 是怎么把这套语言攒出来的`，拓扑图改为领域语言累积图 |
| LinkedIn | 保留为人员能力画像，而不是泛泛人才流向 | pass with boundary | 新增显式章节；目前是能力画像框架，不升级为战略成功证据 |
| JD | 保留为能力补位和投入方向 | pass with boundary | 新增显式章节；保留 AI Security / AI Conversation Platform / Stablecoins Audit 的组织信号边界 |

### Hard Gate Results

| Gate | Result | Note |
|---|---|---|
| Narrative Gate | pass | 主线已统一为 `金融交易设计语言` |
| Paragraph Drift Gate | pass for changed sections | 2/3/4、LinkedIn、JD、未来判断、学习章节均按新主线修复 |
| Judgment Ownership Gate | pass | 新主线来自用户确认；LinkedIn/JD 证据边界明确 |
| Visual Gate | partial-pass | H5/HTML 可渲染结构已更新；还需桌面/移动截图读回后才能作为视觉完成证据 |
| Publish Gate | not applicable | 仍是内部本地 H5 草案，不做 review-ready、发布或 Feishu 同步声明 |

### Verification Evidence

| Check | Result | Evidence |
|---|---|---|
| Required thesis grep | pass | H5 grep found `金融交易设计语言`, `为什么用 Stripe 做观察样本`, `AI 支付需要一套金融交易设计语言`, `Stripe 是怎么把这套语言攒出来的`, `LinkedIn：Stripe 的人员能力画像`, and `JD：Stripe 还在补什么能力` |
| Rejected thesis grep | pass after repair | H5 grep no longer has reader-facing `可信交易执行层`, `控制平面`, `交易控制面`, `交易控制点`, or `交易规则层` as thesis language |
| HTML parser | pass | `python3 -m html.parser wiki/reports/stripe-ai-company-evolution-h5.html` |
| Diff whitespace | pass | `git diff --check -- wiki/reports/stripe-ai-company-evolution-h5.html` |
| Desktop screenshot | pass | `wiki/reports/assets/stripe-ai-company-evolution/domain-language-desktop-top-2026-06-29.png` and `wiki/reports/assets/stripe-ai-company-evolution/domain-language-desktop-2026-06-29.png`; visual readback confirmed the new H1, mainline, 2/3/4 section group, LinkedIn/JD modules, and full-page continuity without obvious overlap or blank regions. |
| Mobile screenshot | pass | `wiki/reports/assets/stripe-ai-company-evolution/domain-language-mobile-top-2026-06-29.png` and `wiki/reports/assets/stripe-ai-company-evolution/domain-language-mobile-2026-06-29.png`; visual readback confirmed the new H1 and first-screen content stack cleanly on narrow viewport. |
| OpenSpec strict validation | pass | `openspec validate realign-stripe-h5-domain-design-language --strict` returned `Change 'realign-stripe-h5-domain-design-language' is valid`; PostHog telemetry flush failed on network/DNS and is not part of local validation. |

### Residual Risks

- LinkedIn section is currently a people-capability-map framework. It requires
  promoted LinkedIn/person-profile evidence before stronger statements about
  actual employee composition.
- JD section uses existing JD scan categories and focused examples, but still
  proves capability investment intent only, not shipped product outcomes.
- Console-event QA for lower interactive timeline/filter controls remains
  uncovered; this local draft should not be claimed review-ready.

## Decision

Use as an internal first draft and research control surface. The latest section realignment now centers the user-confirmed `金融交易设计语言` thesis and repairs the 2/3/4 chapter group, LinkedIn, and JD evidence roles. This is still not a final PPT, Feishu sync, public publication, review-ready claim, or completed 1000-source read pack. The 1000-row CSV is a concrete-source triage queue; only read and promoted rows should become H5/PPT evidence.
