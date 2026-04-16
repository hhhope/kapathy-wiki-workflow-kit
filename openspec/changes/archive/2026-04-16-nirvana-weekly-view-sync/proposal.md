## Why

The current Nirvana weekly records already capture the spreadsheet-based weekly PM summary, but two important inputs are still missing from the weekly archive:

- the user's newly clarified weekly alignment facts from email/chat
- the `preview .html` project view, which carries gantt, capability-map, and technical-construction context

If these are not synchronized into the weekly records, the weekly archive will lose key execution judgment and the HTML view will remain an orphaned artifact that changes over time without a preserved weekly trace.

## What Changes

- Update the existing Nirvana weekly source/intake/reminder records with the newly provided alignment facts.
- Add a dedicated source page for the weekly HTML preview view.
- Link that HTML view into the existing weekly records so the week retains both spreadsheet and visual context.
- Make the weekly archive expectation explicit: each week's HTML view should be preserved as its own source instead of being silently overwritten.

## Capabilities

### New Capabilities

- `nirvana-weekly-html-archive`: The weekly PM archive can preserve a week-specific HTML project view as a source record.

### Modified Capabilities

- `nirvana-weekly-pm-intake`: Weekly records now absorb direct user clarifications and associated HTML project views.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/nirvana-weekly-view-sync/`.
- Adds a new weekly HTML source page under `wiki/sources/`.
- Updates the existing Nirvana weekly source, intake, and reminder pages.
