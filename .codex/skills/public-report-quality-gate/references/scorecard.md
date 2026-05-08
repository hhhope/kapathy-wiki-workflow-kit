# Public Report Quality Scorecard

Use this before creating/updating Feishu documents, H5/share drafts, or other
reader-facing reports.

## Hard Gates

Any hard-fail blocks publishing, Feishu sync, or a "ready for review" claim.

| Gate | Hard-fail signal |
|---|---|
| Reference Structure Gate | A reference artifact exists, but the draft does not map its overall structure, page split, reader path, visual logic, and writing standard before drafting. |
| Split Gate | One draft carries multiple reader jobs such as overview, runtime, migration, validation, and roadmap without an explicit split decision. |
| Voice Gate | Chat residue, slogan simplification, loose narrator, weak section openings, internal ops leakage, or tone mismatch remains in reader-facing text. |
| Narrative Gate | The core story changes, such as turning an evolution path into a static responsibility split. |
| Visual Gate | Diagrams are decorative, duplicated text, or fail to say what relationship or decision they carry. |
| Publish Gate | Review status, source boundary, residual risks, or non-goals are missing before sync/publish. |

## Voice Gate Detail

| Check | Fail Condition |
|---|---|
| Chat residue | Phrases such as "这页是", "我们现在", "下一步去哪", or "一句话记忆" remain as chat/worklog framing instead of report prose. |
| Slogan simplification | A slogan replaces a definition, causal chain, maturity path, or argument. |
| Loose narrator | The draft sounds like an agent explaining what it did rather than a report serving a reader. |
| Weak section opening | A section starts by announcing its topic instead of giving a judgment, reader benefit, or necessary context. |
| Internal ops leakage | Repo paths, OpenSpec mechanics, gates, traces, or agent workflow appear without translation into reader-facing context. |
| Tone mismatch | The requested output is public/executive/shareable, but the tone remains scratch note, chat recap, or wiki draft. |

## Scorecard

Only score after all hard gates pass.

| Dimension | Points | Full-credit standard |
|---|---:|---|
| Reference fidelity | 20 | Reuses the reference's organization, reader journey, visual logic, and writing standard while changing content appropriately. |
| Core narrative | 20 | The main story remains stable from title through diagrams and section conclusions. |
| Progressive split | 15 | Long material is split into overview and follow-up pages, or the single-page choice is justified. |
| Reader path | 15 | The reader knows who the material is for, what decision it supports, what to read first, and where to go next. |
| Visual information design | 15 | Each diagram carries structure, sequence, contrast, or decision logic that prose alone cannot scan quickly. |
| Report voice | 10 | Language is formal, concise, reader-facing, and free of chat residue. |
| Evidence boundary | 5 | Source/reference/local truth boundaries are explicit without overwhelming the reader. |

## Thresholds

| Score | Meaning | Action |
|---:|---|---|
| 90-100 | Strong | May proceed to review/sync after final verification. |
| 80-89 | Acceptable | May proceed, but record residual risks. |
| 70-79 | Draft only | Do not sync/publish; revise first. |
| Below 70 | Failed | Re-plan structure before rewriting. |

Hard-gate failure overrides the numeric score.
