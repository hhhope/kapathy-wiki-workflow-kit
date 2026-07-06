# Stripe PPT v6 Polish: PPT Method And Chapter 1 Design

Date: 2026-07-06
Status: design review
Scope: brainstorming design only; no PPT implementation in this step

## Problem

The current v6 deck is content-complete but not presentation-ready. It preserves the H5 sections, but many pages still read like H5 paragraphs placed on slides with a right-side image. The user rejected two drift patterns:

1. Renaming chapter or subsection anchors as the main solution.
2. Treating a generated image on the right as a complete visual strategy.

The deck needs a company-share / business-analysis PPT method: keep structural anchors, add spoken claims, use visual evidence deliberately, and vary page roles.

## External Reference Learning

This design uses external learning recorded in `wiki/sources/ppt-making-method-learning-2026-07-06.md`:

- Assertion-Evidence: each slide should carry a clear assertion supported by visual evidence.
- Presentation Zen: remove text that does not help the audience understand the point.
- Duarte: presentations need narrative movement, not flat section listing.
- PPTAgent / DeepSlide / PPT-Eval direction: analyze references and templates before implementation; evaluate fidelity, layout, coherence, and delivery quality.
- Mary Meeker / KPCB Internet Trends 2014 is the selected concrete business-analysis deck reference: use it for headline + evidence + so-what logic, not for its dense visual style.

## Non-Negotiable Anchors

- Keep chapter titles and H5 subsection titles as structural anchors.
- Do not rename the section map to make slides sound clever.
- Do not compress or remove first-chapter subsections.
- Do not regenerate images in this pass.
- Do not put internal design labels such as "本页判断" on slides.

## Slide Writing Model

Each content slide should have two layers:

1. Structural anchor: the original H5 subsection title, visible but not dominant.
2. Business headline: a natural claim sentence that the speaker can say aloud.

Then the slide uses visual evidence and minimal support text:

- 0-3 short support points.
- A visual that proves or clarifies the headline.
- Optional small source / boundary line only when needed.

The slide should not use this pattern:

- long paragraph from H5
- bullet summary that repeats the paragraph
- separate takeaway that repeats both

## Page Roles

Use role-based layouts rather than one repeated left-text/right-image template.

- Chapter transition page: keep chapter title; add what this chapter proves and what problem it opens.
- Opening assertion page: balanced claim + evidence visual.
- Service explanation page: balanced claim + decomposition visual.
- Core turn page: large visual; text only frames the conflict.
- Evidence boundary page: explicit proof boundary; visual should feel like a review / evidence card.

## Chapter 1 Design

Chapter title anchor remains: `入口只是烟雾弹`.

Chapter 1 purpose:

AI may change payment entry points, but it does not automatically solve the business question of why payment companies can still charge. The value moves from visible entry points to underlying transaction relationships: participants, authorization, responsibility, funds, and evidence.

Narrative flow:

1. Entrance is visible but not sufficient.
2. Fees are shorthand for complex services.
3. AI lowers integration cost but leaves relationship questions unresolved.
4. The chapter only defines the problem boundary; it does not prove winners or losers.

### Chapter 1 Transition Page

Visible anchor:

`Chapter 1｜入口只是烟雾弹`

On-slide headline:

`AI 会改变付款从哪里开始，但不会改变支付公司为什么还能收费。`

Support text, max three short lines:

- 入口会变
- 关系未解
- 价值在底层

Visual treatment:

Use the template's chapter page, but remove long article-style lead. This page should set up the problem rather than summarize an article section.

### 1-1 AI 支付不是多一个入口

Visible anchor:

`1-1 AI 支付不是多一个入口`

On-slide headline:

`入口解释交易从哪里开始，底层关系决定支付价值。`

Support text:

- Agent 改变触发方式
- 交易关系仍要定义
- 责任、资金、证据才是底层问题

Visual evidence:

Use the existing iceberg image. It should be large enough for the audience to see the contrast between entry and underlying transaction relationship. Add a subtle blue container or frame to integrate the warm image with the blue corporate template.

Layout role:

Opening assertion page, balanced text and visual.

### 1-2 费率背后买的是什么

Visible anchor:

`1-2 费率背后买的是什么`

On-slide headline:

`费率只是表面数字，商户买的是少出错、少扯皮、少自建。`

Support text:

- 转化率影响真实成本
- 拒付和欺诈需要系统处理
- 对账、分账、税务决定长期成本

Visual evidence:

Use the existing receipt / service ledger image. Treat it as a service ledger, not as a decorative receipt. Add a small blue label or frame if needed, but do not add internal design terms.

Layout role:

Service explanation page, balanced text and visual.

### 1-3 AI 让接入变便宜，但关系不会自动清楚

Visible anchor:

`1-3 AI 让接入变便宜，但关系不会自动清楚`

On-slide headline:

`接入成本下降，不等于交易关系清楚。`

Support text:

Use short question chips instead of normal bullets:

- 谁授权？
- 谁担责？
- 钱到哪？
- 证据在哪？

Visual evidence:

Use the existing cost-down / relationship-unresolved image, but make this the largest visual in Chapter 1. The audience should see this as the chapter's main turn: integration gets cheaper, relationship complexity remains.

Layout role:

Core turn page, large visual dominant.

### 1-4 这一章只证明问题，不证明胜负

Visible anchor:

`1-4 这一章只证明问题，不证明胜负`

On-slide headline:

`到这里为止，我们只划清问题边界，不判断谁已经赢。`

Support text:

- 基础支付会被比较
- 服务深度决定溢价
- 公开材料不足以推出胜负

Visual evidence:

Use the existing proof boundary image. The page should feel like an evidence review card: what can be proven, what cannot be proven, and what needs more evidence.

Layout role:

Evidence boundary page, balanced but with stronger boundary styling than ordinary content pages.

## Visual Standards For Chapter 1 Polish

- The original subsection title stays visible, preferably as a smaller eyebrow / anchor line.
- The business headline is larger and more prominent than the subsection title.
- Body text should be short enough to read at projection distance.
- 1-3 must be visibly larger and more important than 1-1, 1-2, and 1-4.
- Existing images are reused; image regeneration is out of scope.
- Warm image assets need a consistent container treatment to reduce conflict with the blue template.

## Acceptance Criteria For The Chapter 1 Prototype

- Chapter and subsection anchors are unchanged.
- No slide contains the label `本页判断` or other internal design terms.
- No H5 paragraph is pasted as a body block.
- Every first-chapter slide has a spoken business headline.
- 1-3 reads as the core turn page.
- Screenshot review confirms that the slide can be understood quickly without the speaker reading paragraphs aloud.

## Open Questions

- Whether to create a Chapter 1 prototype deck before applying the method to the rest of the deck.
- Whether the route page should be added before or after Chapter 1 is prototyped.
