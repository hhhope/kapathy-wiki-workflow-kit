# Proposal: Redraw Account Onboarding H5 Source Visuals

## Why

The current account-group onboarding H5 still fails its real reader job. It
turned source architecture diagrams, capability maps, Nirvana diagrams, and
latest project-report evidence into generic CSS boxes. The result does not look
like account-group technical material and the prior gate review incorrectly
claimed visual quality passed.

This change treats the current H5 as a failed visual draft and rebuilds the
core visual evidence around redrawn, source-backed diagrams.

## What Changes

- Add standalone source-backed SVG visual assets for the onboarding H5.
- Redraw the account capability map instead of presenting it as card clusters.
- Redraw the system architecture based on the multi-channel and 宝财通
  architecture slides.
- Redraw the core funds/account chain as a lane diagram, not a wrapped card
  flow.
- Add a Nirvana/latest-project visual section that shows the current-state
  problem, target architecture, clearing/account-service relation, and current
  project entry points.
- Replace or demote the box-heavy H5 sections by embedding the new visuals and
  using text only as annotation.
- Update the gate review to mark the previous visual gate as failed and record
  the new visual evidence.

## Out of Scope

- Feishu sync or image insertion.
- Changing the already-completed
  `rewrite-account-group-onboarding-h5-domain-depth` task ledger.
- Exposing credentials, internal URLs, Feishu links, personal contacts, QR
  codes, or access instructions.
- Reintroducing `授信能力` or `垫资能力` as account-group capabilities.

## Impact

- `wiki/reports/account-group-onboarding-h5.html` will be visually refactored
  in place.
- New local assets will live under
  `wiki/reports/assets/account-group-onboarding-h5/`.
- The gate review becomes a failure-and-repair record, not a false pass.
