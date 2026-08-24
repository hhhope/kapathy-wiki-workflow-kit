## Why

The BaoCaiTong 2.0 and 3.0 collection and split-settlement proposal currently exists only as two dense screenshots. Product and engineering reviewers need a readable, traceable H5 that separates account relationships, fund flows, business rules, implementation impact, and unresolved decisions without inventing unreadable source text.

## What Changes

- Persist the two source screenshots and create a structured source summary with fact IDs and confidence labels.
- Add a standalone offline H5 for BaoCaiTong 2.0 to 3.0 joint product/engineering review.
- Redraw both account and fund flows with deterministic local HTML/CSS/SVG semantics.
- Add version comparison, seven change areas, business rules, owner filters, risk/open-question cards, and a review-decision surface.
- Add local build and contract tests plus desktop/mobile visual acceptance evidence.
- Add a public-report gate-review record; do not publish or sync to Feishu.

## Capabilities

### New Capabilities

- `baocaitong-review-h5`: Source-traceable, responsive, offline BaoCaiTong 2.0/3.0 review H5 behavior and verification contract.

### Modified Capabilities

None.

## Impact

- Adds files under `wiki/sources`, `wiki/reports`, `wiki/ops`, `scripts`, and `tests`.
- Uses only Python standard library, HTML, CSS, and native JavaScript.
- Adds no remote dependency, backend, API, credential, production identifier, Feishu write, or publication step.
