# Build Ad Platform Operational Prototype

## Why

The existing Growth Cockpit H5 explored a customer-facing demo, but the corrected
requirement is an actually operable advertising delivery system prototype. The
new prototype must cover the requested architecture, module-level PRD flows, and
local-state operations across the full advertising platform.

## What Changes

- Add a standalone operational backstage prototype at `wiki/reports/ad-platform-operational-prototype.html`.
- Add contract tests for module coverage, stateful interaction hooks, architecture and sequence surfaces, and drift prevention.
- Add a repo-visible report gate review that records the intent correction and proof boundary.

## Non-Goals

- No real backend, login, payment, invoice, media API, SDK network call, or attribution API call.
- No Feishu sync or production readiness claim.
- No deletion of the existing Growth Cockpit H5 unless requested separately.

## Impact

- Adds one prototype HTML artifact.
- Adds one test file.
- Adds one ops gate review artifact.
- Leaves existing completed Growth Cockpit artifacts intact as exploratory output.
