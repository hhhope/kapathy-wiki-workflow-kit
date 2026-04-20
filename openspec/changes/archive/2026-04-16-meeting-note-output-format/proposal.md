## Why

The current repository can classify and summarize meeting materials, but it does not yet enforce a high-quality, fixed output format for meeting notes. This caused the generated meeting-note output to be too loose, too short, and inconsistent with the user's expectation of a directly usable meeting-minutes document.

## What Changes

- Add a fixed meeting-note output format for source pages and external document output.
- Define required sections for meeting-note outputs, including basic meeting metadata, core agenda, decision-oriented body, risks, and action items.
- Add a repository-local meeting-note output skill draft that documents how to convert raw note / transcript material into the fixed format.
- Update the current meeting-note template and rewrite the current sample meeting note to match the new format.

## Capabilities

### New Capabilities
- `meeting-note-output-format`: Fixed structure for turning meeting materials into readable meeting-note outputs for wiki and Feishu delivery.

### Modified Capabilities
- `material-collaboration-defaults`: Meeting-note processing now requires a stronger output contract than generic readable summary text.

## Impact

- Adds OpenSpec artifacts under `openspec/changes/meeting-note-output-format/`.
- Updates repository guidance and templates for meeting-note output.
- Adds a repo-local skill draft and a reusable meeting-note format example.
- Changes the structure of meeting-note source pages and future Feishu meeting-note documents.
