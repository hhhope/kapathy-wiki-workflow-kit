## ADDED Requirements

### Requirement: Repository SHALL support a small migration pilot for legacy evolution-bearing pages

The repository SHALL support a narrow migration pilot that applies the naming and
frontmatter models to an existing legacy page family.

#### Scenario: Pilot family is selected

- **WHEN** the repository chooses a pilot family for migration
- **THEN** the pilot SHALL stay limited to a small, coherent object family

### Requirement: Repository SHALL preserve local navigation during the migration pilot

The repository SHALL update affected local links and indexes within the pilot scope.

#### Scenario: Pilot pages are renamed or restructured

- **WHEN** pilot pages are renamed or restructured
- **THEN** affected local navigation inside the pilot scope SHALL be updated to remain valid

### Requirement: Repository SHALL verify extraction still works after the migration pilot

The repository SHALL confirm that graph extraction still recognizes migrated pages
after the pilot is applied.

#### Scenario: Pilot migration is complete

- **WHEN** the pilot migration is complete
- **THEN** the repository SHALL re-run graph extraction and confirm the migrated pages still appear as expected
