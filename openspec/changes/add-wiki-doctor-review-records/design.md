# Design: wiki-doctor review records

## Architecture

Keep adjudication package construction in `scripts/wiki_content_adjudication.py`.
Add `scripts/wiki_doctor_review_records.py` for review-record rendering and
write safety. Wire `scripts/build_wiki_content_adjudication.py` to the new
module with explicit CLI flags.

## Data Flow

```text
build_adjudication_package(root)
  -> optional limit applied by CLI
  -> stdout JSON
  -> optional write_review_record(package, root, output_dir)
  -> wiki/ops/wiki-doctor-runs/YYYY-MM-DD-HHMMSS-review.md
```

## Review Record Contract

The Markdown record includes:

- scan scope and generated time
- summary counts
- taxonomy candidates as candidates only
- drift trace summary
- eval result summary
- proof boundary
- next review actions

## Boundaries

The review record is diagnosis evidence only. It does not apply structure,
approve taxonomy, write MOC pages, mark OpenSpec tasks complete, or execute
queued work.

## Large-File Boundary

`scripts/wiki_content_adjudication.py` is already above the Python large-file
threshold. This change adds a new helper module instead of adding rendering and
filesystem responsibilities to that file.
