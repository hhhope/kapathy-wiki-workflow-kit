# Stripe AI Payment PPT v6 Image-Model Redesign

Date: 2026-07-06

## Objective

Rework `stripe-ai-payment-sharing-template-deck-v5-template-mapped-2026-07-03.pptx` into a v6 review deck that is suitable for an internal 80-person presentation. The v6 scope is not another H5-to-PPT conversion. It is a presentation refinement pass with image-model-generated right-side visuals, tighter presenter-facing wording, and stronger template integration.

Target output:

- `wiki/reports/stripe-ai-payment-sharing-template-deck-v6-image-model-2026-07-06.pptx`
- image-model visual assets under `wiki/reports/assets/stripe-ai-payment-sharing-h5/ppt-v6-image-model-visuals-2026-07-06/`
- prompt package / visual task map under `wiki/ops/stripe-ai-payment-sharing-ppt-v6-image-model-plan-2026-07-06.md`
- gate review under `wiki/ops/stripe-ai-payment-sharing-ppt-v6-gate-review-2026-07-06.md`

## Current Problem Summary

The v5 deck fixed the previous hard failures: no template placeholder text, all 32 H3/evidence sections are present, and no generic repeated three-box diagram is reused. But v5 is still not final presentation quality.

Observed issues:

1. Right-side images are too small in the final PPT composition.
2. Image labels are too small and too thin after being scaled into the slide.
3. The right-side visuals look like deterministic script diagrams, not the intended image-model strategy-board illustrations.
4. Body copy is still too close to H5 prose: long paragraph plus repeated bullets.
5. Many H5 section titles are retained as page titles without being rewritten into presentation claims.
6. Chapter divider pages act as separators, not as clear talk-track transitions.
7. Evidence-boundary pages are visually repetitive.
8. The blue Mandao template and warm-paper diagrams need a unifying integration layer.

## Accepted Direction

The user confirmed approach 2: a chapter-by-chapter review and refinement path.

The user then specified the v6 implementation direction:

- regenerate the entire right-side visual system through image-model output;
- keep the PPT content coverage from v5;
- prepare a plan and then start execution.

Because `$superpowers:brainstorming` is active, this design document is the design gate before implementation. OpenSpec stays read-only until this written spec is reviewed.

## Reader And Job-To-Be-Done

Reader: internal presentation audience of around 80 people.

Reader job:

- understand why Stripe is a useful AI-payment-era case;
- stop framing AI payment as just a new entrance or button;
- understand the core claim: payment competition moves toward financial transaction language, relationship design, and operating complexity;
- take away a practical judgment card for evaluating AI + industry opportunities.

Non-goals:

- prove Stripe will win;
- weaken PayPal, Adyen, Visa, Mastercard, or other competitors;
- make a source-heavy public research report;
- turn the PPT into a dense H5 article;
- fabricate metrics, market share, dates, or organization facts.

## Output Shape

V6 keeps the broad deck structure but upgrades the presentation behavior.

Expected deck shape:

1. Cover.
2. Optional agenda / route page if it improves listener orientation.
3. Chapter divider pages for chapters 1-9.
4. One page per H3/evidence section, preserving the 32-section coverage.
5. Closing page.

Body slide structure:

- title: one presentation claim, not only the H5 heading;
- left side: one sentence takeaway + up to three short supporting bullets;
- right side: one large image-model finished visual, carrying its own readable Chinese labels/dates/numbers when the visual needs them;
- footer/page mark: retained but unobtrusive;
- no long body paragraphs copied directly from H5.

## Visual Design Direction

Mode: image_model for the complete right-side finished visual, including Chinese labels, dates, numbers, and evidence-boundary text when the page needs them. Do not default to deterministic PPT overlay for precise text.

Visual source roles:

- Content source: `wiki/reports/stripe-ai-payment-sharing-h5.html` and the v5 slide text/readback.
- Style source: `wiki/reports/assets/stripe-ai-payment-sharing-h5/handdrawn-hybrid-2026-07-02/`, `handdrawn-ai-2026-07-02/`, and the style language described in `image-generation-prompts-2026-07-02.md`.
- Template source: `C:/Users/yan/Desktop/account-group-onboarding-h5/附件二：漫道集团PPT模板V1.pptx`.
- Executor: image generation for new right-side visuals, followed by PPT composition and screenshot QA.

Visual style:

- editorial hand-drawn strategy-board illustration;
- warm off-white paper texture;
- charcoal ink lines;
- muted teal, coral, amber, and blue-gray accents;
- refined internal strategy memo tone;
- no cartoon mascot, no sci-fi glow, no fake dashboard UI, no dense microtext;
- no invented logos, metrics, dates, or percentages;
- enough quiet areas around the model-rendered labels so the visual remains readable after insertion into PPT.

Template integration:

- Right-side image area must be larger than v5.
- Add a consistent integration shell: subtle blue title chip, thin blue-gray border, or shared corner accent so the warm-paper image does not feel pasted onto a corporate slide.
- Keep Mandao cover/chapter/closing pages, but rewrite chapter copy into talk-track transitions.
- Avoid mixing three unrelated surfaces: pure white body page, blue corporate footer, and isolated beige image card. The image container should visually mediate between blue template and warm illustration.

## Image Model Policy

Critical text policy:

- Image model should render the complete right-side finished visual, including readable Chinese labels when the page needs text.
- Exact dates, numbers, evidence boundaries, company/product names, and Chinese labels should be attempted directly in the image-model output.
- Each image is a candidate until image-text QA passes by visual inspection/readback.
- If model text is garbled, cramped, or wrong, the repair path is regenerate or image-model/local image repair first. Deterministic PPT overlay is only an emergency fallback after repeated model-text failure and must be explicitly called out.

Delivery policy:

- Prefer repo-local image files.
- If the runtime image tool only returns chat artifacts without reliable file export, stop and produce a prompt package plus delivery-gap note; do not pretend local model-generated files exist.
- Do not claim image-model local asset delivery unless files exist and are inspectable.

## Visual Task Scope

V6 regenerates all 32 right-side visuals. Priority visuals receive richer treatment and bigger slide real estate:

High priority image-model pages:

- 1-3 AI lets integration get cheaper but relationships stay unclear.
- 2-2 player position matrix.
- 3-2 financial transaction language five-layer stack.
- 4-1 three strategic routes.
- 5-1 multiparty transaction graph.
- 6-1 capability radar.
- 6-2 260 JD sample profile.
- 7-4 137-day L3 A2A timeline.
- 8-3 five-question decision card.
- Evidence boundary.

All remaining pages also get regenerated images, but can use simpler image-model compositions if they pass style and readability gates.

## Wording Redesign Rules

Each content page should be rewritten from article prose into presentation talk-track language.

Rules:

1. Page title should be a claim or judgment.
2. Left-side takeaway should be one concise sentence.
3. Supporting bullets should be short enough to read while listening.
4. Avoid repeating the same sentence in paragraph and bullets.
5. Keep evidence boundaries visible when claims depend on partial evidence.
6. Preserve H5 coverage, but do not preserve H5 wording when it hurts presentation clarity.

Examples:

- v5: `1-3 AI 让接入变便宜，但关系不会自动清楚`
  v6 title candidate: `接入成本下降，不等于交易关系清楚`

- v5: `2-1 先看十五年增长：它不是突然被 AI 推上来`
  v6 title candidate: `Stripe 不是被 AI 临时推上牌桌`

- v5: `8-3 带走一张判断卡`
  v6 title candidate: `判断 AI 机会，先问五个关系问题`

## Chapter Page Rules

Each chapter page should answer one transition question:

- Chapter 1: What illusion are we removing?
- Chapter 2: Where is Stripe positioned before AI?
- Chapter 3: What is the real moat?
- Chapter 4: What strategic choice did Stripe make?
- Chapter 5: Why does complexity pull Stripe deeper?
- Chapter 6: What kind of organization is needed?
- Chapter 7: Why do old payment capabilities become expensive again?
- Chapter 8: What should we learn for ourselves?
- Chapter 9: What can and cannot be proven from current evidence?

Chapter copy should be one short transition line, not an H5 paragraph.

## Implementation Plan

### Phase 1 — v6 planning artifacts

- Create a v6 visual task map covering all 32 right-side visuals.
- For each visual, record: section, slide role, visual claim, image-model prompt, exact overlay labels, model-text risk, verification rule.
- Mark high-priority visuals that need richer image-model treatment.

### Phase 2 — image-model asset generation

- Generate the visual assets in batches, starting with the high-priority ten pages.
- Save or bridge generated assets into `ppt-v6-image-model-visuals-2026-07-06/`.
- Run image QA after each batch: style consistency, no garbled text, no unsupported numbers, enough whitespace, and readable main composition.
- If the image model cannot reliably emit exact text after repeated attempts, stop and report the specific failed fields before using any deterministic overlay fallback.

### Phase 3 — PPT text and layout rebuild

- Create `build_stripe_ai_payment_ppt_v6_image_model.ps1` or equivalent update script.
- Preserve the original template source and v5 as comparison artifacts.
- Add a route/agenda page if it improves listener orientation.
- Rewrite body slides into presentation titles, one takeaway, and short bullets.
- Enlarge the right-side visual area and add a consistent image container style.
- Replace all v5 right-side deterministic diagrams with v6 image-model assets.

### Phase 4 — verification

- Export the final PPT to screenshots.
- Inspect representative pages from every chapter and the high-priority pages.
- Confirm slide count and image count.
- Confirm all H3/evidence sections remain represented.
- Confirm no template guide text or placeholders remain.
- Confirm image-text QA for all critical text rendered inside the model-generated visuals.
- Write a v6 gate review artifact with pass/fail evidence and residual risks.

## Acceptance Criteria

V6 is acceptable only if all of the following pass:

1. All 32 H3/evidence content sections remain covered.
2. Right-side visuals are regenerated or replaced by image-model-driven visuals, not reused v5 script diagrams.
3. Critical text, dates, numbers, and evidence labels are rendered inside the model-generated visual and are readable and correct after image-text QA.
4. The PPT body text is presentation-oriented, not H5 paragraph copy.
5. Chapter pages have clear transition statements.
6. Template placeholders and guide text are absent from slide, layout, and master XML.
7. The final PPT exports to screenshots without error.
8. Representative screenshot review shows the deck looks like a coherent internal presentation.
9. A v6 gate review records evidence and residual risks.

## Open Questions / Decisions

Resolved:

- Use image-model route for the complete right-side visuals.
- Let the model render Chinese labels, dates, numbers, and evidence-boundary text directly when those elements belong in the visual.
- Preserve full content coverage.
- Do v6 as a refinement, not a full research rewrite.

Still needs review before implementation:

- Whether to add an agenda/route page.
- Whether evidence-boundary pages should stay as three pages or be compressed to a stronger one/two-page evidence matrix.

## Spec Self-Review

Placeholder scan: no TBD/TODO placeholders remain.

Internal consistency: the design keeps v5 content coverage while replacing the weak visual system and article-like wording.

Scope check: this is a single implementation project: v6 PPT refinement with regenerated right-side visuals, not a broader H5/report rewrite.

Ambiguity check: image model is the visual source for the complete right-side finished visuals, including exact text where needed; correctness is verified through image-text QA and screenshot QA.


