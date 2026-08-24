## Context

Two user-provided screenshots contain the BaoCaiTong 2.0/3.0 account relationships, fund paths, rules, implementation changes, and unresolved issues. They are dense and partially low-resolution. The approved reader is a joint product and engineering review group. The approved narrative and screen plan are recorded in `docs/superpowers/specs/2026-08-24-baocaitong-2-3-h5-design.md`; the implementation slices are recorded in `docs/superpowers/plans/2026-08-24-baocaitong-2-3-h5.md` and are used only as execution detail.

## Goals / Non-Goals

**Goals:**

- Persist the source images and assign traceable fact IDs with confidence labels.
- Generate a standalone responsive H5 with deterministic 2.0/3.0 account and fund-flow diagrams.
- Preserve full linear content without JavaScript while adding accessible progressive enhancement.
- Verify source mapping, static contracts, local-resource safety, desktop layout, and mobile layout.

**Non-Goals:**

- No Feishu sync, publication, backend, live data, remote dependency, or production integration.
- No invented business rule or claim when screenshot text is unreadable or conflicting.
- No replacement of the original screenshots; they remain source evidence.

## Decisions

1. **Persist source before rendering.** Copy the temporary screenshots into `wiki/sources/assets/baocaitong-2-3/` and create a structured source summary. This prevents the final artifact from depending on temporary paths.
2. **Use one JSON fact source plus a deterministic Python builder.** This keeps source mapping auditable and renders all core content into static HTML. A hand-authored monolithic HTML alternative was rejected because it would mix facts, layout, and interaction.
3. **Use local HTML/CSS/SVG and native JavaScript.** This supports offline review without CDN or package additions. Image-model diagrams were rejected because exact Chinese labels and fund-flow semantics are load-bearing.
4. **Use progressive enhancement.** Native HTML and `details` preserve reading without JavaScript; JavaScript adds compare modes, filters, navigation state, and progress.
5. **Keep report review separate from publication.** A gate-review record captures intent, source mapping, judgment ownership, drift review, visual QA, and residual risk. It does not authorize Feishu or external delivery.

## Risks / Trade-offs

- [Low-resolution source text] → Mark uncertain fields `待原文确认` and keep the source coordinate in the fact record.
- [Conflicting statements across screenshots] → Render the conflict as an open question rather than choosing silently.
- [Complex flow on mobile] → Stack version flows and preserve readable labels instead of scaling down the desktop canvas.
- [Generated HTML drift from JSON] → Rebuild before tests and assert required fact IDs in the generated artifact or gate record.
- [Dirty shared worktree] → Stage and commit only exact task paths; do not alter unrelated changes.

## Migration Plan

1. Add new source, content, build, test, report, and gate-review artifacts without overwriting an existing report.
2. Verify the generated H5 locally at desktop and mobile widths.
3. Roll back by removing only the new change-owned paths; no shared runtime or schema is modified.

## Open Questions

Business fields that cannot be read with confidence remain open in the H5 and gate review. They do not block producing an internal review draft, but they block a final business-approved claim.
