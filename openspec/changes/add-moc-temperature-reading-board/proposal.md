# Proposal: add MOC temperature reading board

## Why

The current Obsidian MOC projection can generate relation pages directly from
frontmatter graph edges. That is mechanically correct, but it lets low-value
relation types such as `derived_from` and `related_objects` become standalone
MOC pages without proving reading value.

The repository needs a value-first admission layer before MOC projection. MOC
should reveal useful wiki relationships and clues, not raw edge dumps.

## What Changes

- Add a relation temperature reading-board layer that converts graph edges into
  bounded clue windows.
- Keep Python responsible for structural feature packages only.
- Require explicit AI or human review judgments for semantic temperature.
- Gate relation MOC pages behind admitted high-temperature clue windows.
- Surface admitted, blocked, and review-needed counts in MOC dry-run and
  medical-agent MOC preview.
- Keep MOC preview and medical-agent review read-only.

## Impact

- Affects `scripts/wiki_moc_temperature.py`, `scripts/wiki_moc_projection.py`,
  `scripts/build_wiki_moc_projection.py`, and `scripts/wiki_medical_agent.py`.
- Updates MOC projection tests and medical-agent preview tests.
- Existing domain and object MOC pages remain available.
- Relation MOC pages are no longer created from raw relation types by default.
