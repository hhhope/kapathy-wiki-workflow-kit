## Why

The user has now provided the first real weekly project-management input under `inbox/nirvana/`. To make the wiki act like an operational agent workspace, this material must be turned into durable structured pages instead of remaining only as raw spreadsheets.

The first weekly PM intake should establish the working pattern:

- keep the weekly report as a source record
- create an ops intake record that summarizes the weekly PM judgment
- surface follow-up actions and risks as a reminder

## What Changes

- Create a weekly source page for the Nirvana 2026-04-13 project weekly report.
- Create an ops intake page for the same weekly PM material.
- Create a reminder page that captures the current follow-up actions and risks.
- Link the new pages from the relevant source and ops indexes.

## Capabilities

### New Capabilities

- `nirvana-weekly-pm-intake`: The repository can ingest a real weekly PM input from `inbox/nirvana/` into source, intake, and reminder layers.

### Modified Capabilities

- `weekly-project-management-loop`: The loop is exercised with a real Nirvana weekly report instead of policy-only pages.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/nirvana-weekly-pm-intake/`.
- Adds new pages under `wiki/sources/` and `wiki/ops/`.
- Updates source and ops navigation pages so the new records are discoverable.
