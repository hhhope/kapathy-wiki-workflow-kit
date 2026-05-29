# Proposal: Rewrite Account Group Onboarding H5 Domain Depth

## Why

The first account-group onboarding H5 draft has acceptable chapter order but
fails the reader job. It compresses account-group domain content into generic
cards, omits system architecture, and does not explain key engineering domains
such as account model, bank-account relation, accounting, balance,
clearing/settlement, reconciliation, reports, parent-child accounts, and
multi-account model with enough structure for fresh graduates.

## What Changes

- Rewrite the existing local H5 content while keeping the H5-first delivery
  form.
- Replace the thin capability summary with a real account-domain capability
  graph.
- Add a layered system architecture section based on the source architecture
  slides.
- Rewrite the core chain to include account model, bank-account relation,
  transaction, accounting, balance, clearing/settlement, reconciliation,
  reports, difference handling, and observability.
- Rewrite project and newcomer task sections so they map to real account-domain
  modules.
- Reconnect AI collaboration content to account-domain design, review,
  verification, and knowledge reuse.
- Update the public-output gate review with drift diagnosis, revised evidence
  map, verification evidence, and sensitive-info boundary.

## Out of Scope

- Feishu publishing or sync.
- Exposing credentials, personal contacts, internal test URLs, group QR codes,
  or access instructions.
- Treating `授信能力` or `垫资能力` as account-group capability groups.
- Reopening the completed `build-account-group-onboarding-h5` change.

## Impact

- The existing H5 file will be rewritten in place.
- The report index link remains valid unless the title changes.
- The gate review becomes the evidence surface for why the first draft failed
  and how the rewrite fixes it.
