# Design: wiki-doctor skill rename

## Naming

Use `wiki-doctor` for the user-facing skill name.

Rationale:

- short enough for daily use
- implies diagnosis and risk review
- does not imply automatic writes
- avoids exposing the internal term `adjudication`

## Compatibility

The underlying runtime remains:

- `scripts/build_wiki_content_adjudication.py`
- `scripts/wiki_content_adjudication.py`

The skill rename is a surface change only.

## Boundary

`wiki-doctor` remains review-only:

- no frontmatter writes
- no taxonomy mutation
- no MOC writes
- no OpenSpec lifecycle changes
- no queued work execution
