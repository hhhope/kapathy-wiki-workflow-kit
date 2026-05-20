# wiki-medical-agent Specification Delta

## ADDED Requirements

### Requirement: MOC surgery preview SHALL include read-only temperature prediagnosis

When `moc_surgery_preview` is allowed, the medical agent SHALL include a bounded
read-only prediagnosis section that interprets MOC temperature evidence without
expanding write authority.

#### Scenario: User asks for MOC temperature clues

- **GIVEN** exactly one active medical case exists
- **WHEN** the user asks the medical agent to inspect MOC temperature clues
- **THEN** the medical agent SHALL return intent `moc_surgery_preview`
- **AND** it SHALL include `prediagnosis.kind: moc_temperature`
- **AND** it SHALL include script result summary, interpreted live intent,
  blocked mechanical relation families, review-needed clues, orphan relation
  MOC pages, confirmation points, and write boundary
- **AND** it SHALL NOT write `wiki/moc`.

#### Scenario: Mechanical relation families are blocked by default

- **GIVEN** temperature admission contains `derived_from` and `related_objects`
  as blocked relations
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL mark those relation families as mechanical
  and blocked by default
- **AND** it SHALL NOT mark them as admitted.

#### Scenario: Review-needed clue windows are summarized

- **GIVEN** temperature admission contains many `clue_windows`
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL include bounded clue candidates
- **AND** it SHALL NOT dump the full `clue_windows` array into the
  prediagnosis section.

#### Scenario: Orphan relation MOC pages are surgery candidates only

- **GIVEN** surgery preview contains orphan relation MOC sample items
- **WHEN** MOC prediagnosis is built
- **THEN** the prediagnosis SHALL surface those pages as surgery candidates
- **AND** it SHALL NOT clean them up.
