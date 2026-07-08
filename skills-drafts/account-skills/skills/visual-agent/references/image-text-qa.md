# Image Text QA

Use this reference when a generated or edited image contains readable text.

## Critical Text

Check text that can make the artifact wrong if it drifts:

- names, titles, and brand/product names
- addresses, phone numbers, IDs, and URLs
- prices, dates, quantities, percentages, table values, and units
- policy clauses, eligibility rules, warnings, and legal/compliance text

## Check Flow

1. Treat the generated image as a candidate draft.
2. Inspect or crop text-heavy regions before final delivery.
3. Compare critical text against the source or user-provided wording.
4. Classify issues: wrong, missing, garbled, blurry, cramped, or visibly patched.
5. Tell the user when style is usable but text is not ready.
6. Pick the smallest viable repair.
7. Re-check the repaired crop and the full image before claiming completion.

OCR may help locate or confirm text, but it is not final proof. A crop can pass
OCR while still looking visually patched, cramped, or inconsistent.

## Repair Choice

| Issue shape | Prefer |
|---|---|
| broad text unreliability | regenerate or switch to hybrid |
| one bounded wrong area | local edit |
| wrong word or short phrase | phrase redraw |
| full line is unreliable | line redraw |
| exact public-facing text required | deterministic overlay or hybrid |

## Chinese Poster / Marketing Long Image

For Chinese posters, rental cards, one-page ads, and marketing long images,
check these before saying the image is ready:

- headline and offer
- address and contact phone
- price, area, rent period, and table numbers
- eligibility rules, restrictions, and warm reminders
- section labels and any callout badges

If a user points out a specific wrong word, first identify whether it is a
missing character, wrong character, garbled character, spacing problem, or patch
artifact. Do not jump to a whole-line patch unless the whole line is unreliable.
## User Review Block

When a critical field cannot be confirmed, show the user a compact block before
final delivery:

```text
待确认文字：<field>
当前观察：<what looks wrong, blurry, suspicious, or unverified>
已有证据：<crop/OCR/source/user text/manual inspection>
建议处理：<regenerate/local edit/phrase redraw/line redraw/overlay>
需要你确认：<exact question or source text needed>
```

Do not say the image is ready while `待确认文字` contains unresolved address,
phone, price, date, table, or policy text.
