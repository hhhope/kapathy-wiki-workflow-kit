# Language Hardening Results — first-load interpretation

Date: 2026-04-14
Change: `harden-team-lore-language-and-routing`

## RED — Before draft hardening

Observed failures from `check-language-hardening.py`:

- all three target draft pages were absent
- there was no `Summary` section carrying mixed-language first-load guidance
- the required operating sections for this follow-up (`Summary`, `Applies When`, `Top Facts`, `Load Next`) did not yet expose mixed-language support

Why this was RED:

- aliases alone can improve routing, but they do not prove that the first screen is understandable under mixed-language startup
- the follow-up needed concrete page surfaces to verify, not a prose claim that “we could add summaries later”

## GREEN — After draft hardening

The follow-up draft slice now adds:

- a bilingual `Summary` to each target page
- mixed-language `Applies When`
- mixed-language `Top Facts`
- mixed-language `Load Next`

Selected pages:

- `drafts/wiki/index.md`
- `drafts/projects/account-skills/overview.md`
- `drafts/pitfalls/behavior-assets-without-evidence.md`

## Verification

`check-language-hardening.py` now passes for the selected slice:

- each target page exists
- each target page exposes all required sections
- each required section contains both Chinese and English support
- passing pages:
  - `drafts/wiki/index.md`
  - `drafts/projects/account-skills/overview.md`
  - `drafts/pitfalls/behavior-assets-without-evidence.md`

## Limits

- this proves a stronger first-load contract for the selected pages, not full bilingual completion of `team-lore`
- long-form body text is still not mirrored end-to-end
- broader historical backfill remains outside this follow-up
