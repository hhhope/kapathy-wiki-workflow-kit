# Realign Stripe H5 Around Financial Transaction Design Language

## Why

The latest approved Superpowers design changes the Stripe sharing mainline.
The H5 should no longer center on "AI payment as a transaction control plane"
or "trusted execution layer." The user's confirmed thesis is sharper:

> AI lowers coding and integration cost. The scarce capability is the ability
> to design a complex financial domain into clear objects, interfaces,
> permission boundaries, risk rules, settlement relationships, and dispute
> evidence. Stripe moves quickly into AI payment because it has long done the
> hardest correct work in payments: reducing fragmented financial complexity
> into a usable domain design language.

Existing Stripe H5 changes were completed under earlier OpenSpec scopes. This
new direction is out of scope for those completed changes, so it needs a fresh
active change before implementation.

## What Changes

- Realign `wiki/reports/stripe-ai-company-evolution-h5.html` around the
  financial transaction design-language thesis.
- Rebuild the opening and core chapters so chapters 2/3/4 explain:
  - why Stripe is the observation sample;
  - what financial transaction design language means;
  - how Stripe accumulated that language through hard domain work.
- Preserve LinkedIn as people-capability mapping and JD as capability-building
  intent.
- Update the Stripe report gate review with the new article intent, section
  drift review, visual gate notes, verification evidence, and non-publication
  boundary.
- Verify the H5 with static checks, HTML parse, desktop screenshot, and mobile
  screenshot when browser tooling is available.

## Non-Goals

- No Feishu sync, publication, or review-ready claim.
- No claim that Stripe will certainly win AI payments.
- No claim that all queued Stripe sources have been read.
- No new source collection, crawler, backend, package dependency, or build
  system.
- No unrelated rewrite of other reports, repo workflow rules, skills, or
  OpenSpec archive state.

## Impact

This change affects one Stripe H5 draft, its report gate review, and this
OpenSpec change ledger. It keeps the output as an internal local H5 draft for
user review.
