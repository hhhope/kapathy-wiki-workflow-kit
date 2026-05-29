# Design: Source-Visual Redraw For Account Onboarding H5

## Visual Direction

Use deterministic SVG assets with real Chinese text. The diagrams should feel
like technical training posters: dense enough to carry architecture, but not a
PPT screenshot dump. The H5 should be an annotated visual walkthrough, not a
card encyclopedia.

## Source-Backed Visual Assets

Create four standalone SVG assets:

1. `account-capability-map.svg`
   - Source: `账户体系能力地图` slide from `账户组技术规划与述职 _v6.pptx`.
   - Purpose: show account basic, accounting, clearing/settlement, balance,
     reconciliation/report/data, revenue/split capabilities.
   - Boundary: exclude credit and advance-funding clusters.

2. `account-system-architecture.svg`
   - Source: multi-channel architecture and 宝财通 architecture slides from
     `账户组技术现状分享.pptx`.
   - Purpose: show upstream entrances, product layer, service layer, account
     and clearing services, data layer, payment channels, and partner banks.

3. `account-core-chain.svg`
   - Source: account technical status, clearing/account materials, and the
     current H5 domain rewrite.
   - Purpose: show identity/account relation, transaction, split/withdraw/refund,
     accounting/balance, clearing/settlement, reconciliation/report/difference,
     and observability as one chain.

4. `nirvana-project-entry-map.svg`
   - Source: `inbox/nirvana/现状.png`, `最终方案.png`, `优化后图示.png`,
     `清算的内容.png`, and the split-account/core project report.
   - Purpose: show why Nirvana matters to the account group and where new
     graduates can enter real project work.

## H5 Structure Changes

- Keep the accepted chapter order.
- Replace the capability, architecture, core-chain, and active-project sections
  with image-first sections.
- Keep explanatory text short and adjacent to the diagram.
- Add a source-visual index near the top so reviewers can see which source
  visuals are represented.
- Preserve onboarding, AI collaboration, and growth-path sections, but visually
  reduce generic cards where they compete with architecture visuals.

## Gate Review Changes

The gate review must explicitly record:

- previous Visual Gate result is invalid;
- old screenshots show box-heavy layout and are failure evidence;
- new standalone asset paths;
- source-to-visual mapping;
- desktop and mobile screenshots after repair;
- sensitive-info grep results.

## Verification

Required verification:

- SVG parse check for each new asset.
- HTML parser check for the H5.
- Required-source visual grep for the H5 asset references.
- Sensitive-info grep on H5 and SVG assets.
- Excluded capability grep for `授信能力|垫资能力`.
- Desktop and mobile full-page screenshots with visual inspection.
- `git diff --check`.
- `openspec validate redraw-account-onboarding-h5-source-visuals --strict`.
