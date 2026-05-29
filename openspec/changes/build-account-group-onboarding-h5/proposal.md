# Build Account Group Onboarding H5

## Why

The repository needs an internal H5 training draft that turns the account-group
planning, current-state, clearing/account-system, onboarding, and AI
collaboration materials into a coherent newcomer-facing learning path.

The current sources are scattered across PPT/PDF/wiki/Feishu materials. A new
graduate needs one readable entry point that explains what the account group
owns, which active project areas they may join, how the team uses AI
collaboration, and what they can do and gain during onboarding.

## What Changes

- Add a standalone static H5 draft at
  `wiki/reports/account-group-onboarding-h5.html`.
- Add a repo-visible public-output gate review record at
  `wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`.
- Update `wiki/reports/index.md` to list the new H5 after verification.
- Preserve source-to-screen evidence mapping and sensitive-information
  boundaries for the reader-facing draft.

## Non-Goals

- No Feishu sync or publication claim.
- No backend, build pipeline, login, or live API integration.
- No raw internal account, VPN, test URL, personal contact, credential, or
  Feishu-token exposure in the reader-facing H5.
- No change to repository runtime behavior, skill routing, or governance rules.

## Impact

- Adds one reader-facing internal H5 draft.
- Adds one report-quality gate review note tied to the draft.
- Adds one reports index entry.
