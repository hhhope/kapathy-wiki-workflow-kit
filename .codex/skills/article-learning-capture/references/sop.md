# Article Learning SOP

Use this SOP after `article-learning-capture` triggers.

## 1. Source Intake

Record:

- original URL
- title
- author or publisher, if available
- publication date, if available
- access date
- source type: article / blog / paper / WeChat / article collection
- retrieval method: browser, `weixin-reader`, pasted text, screenshot, local PDF
- source class: primary source / secondary interpretation / structure
  reference / low-relevance/general-interest
- source artifact type: extracted markdown / source map / bounded excerpts /
  retrieval failure note

For `mp.weixin.qq.com` links, try `weixin-reader` when body text is needed. If it
fails, ask for pasted text or screenshots.

Preserve source grounding before scoring or deep reading:

- Use an extracted markdown snapshot when the source is available and copyright
  boundaries allow local storage.
- Use a source map with section headings and bounded excerpts when the full
  source cannot be stored.
- Use a retrieval-failure note when the original cannot be accessed; ask for
  pasted text or screenshots before interpreting the article.
- Do not treat another model's summary as the source artifact.

## 2. Score Before Deep Reading

Apply `scorecard.md`.

- 75 or higher: deep-read and write durable wiki notes.
- 60-74: brief-read and keep a candidate note.
- Below 60: record source and skip reason.

Do not deep-read low-scoring material by default.

## 3. Reading Draft

The reading draft is for understanding the article, not extracting rules.

Capture:

- problem the article is solving
- method, architecture, or process
- evidence type: experiment, benchmark, case study, product experience, logs,
  research result, opinion
- assumptions and context
- what the article does not prove
- structured translation notes or paraphrased reading notes

Copyright boundary:

- short excerpts only when needed
- prefer paraphrase
- no full verbatim article text
- no full verbatim translation
- no full verbatim translation draft as the durable wiki output

## 4. Transfer Extraction

Only extract points that might affect this repo, agent workflow, output methods,
or behavior-asset candidates.

For each point, record:

- source
- claim
- evidence
- local usefulness
- adoption boundary
- status: accepted / candidate / rejected

These are metadata for transfer candidates. They are not the article summary.

## 5. Wiki Routing

Default routing:

- `wiki/ops`: workflow, governance, operating behavior, agent practice
- `wiki/examples`: output-shape, writing style, visual grammar, reusable format
- `wiki/team-lore-candidates.md`: only after a project-local record exists and
  the learning appears cross-project reusable
- OpenSpec change: when the learning becomes a scoped repository behavior or
  asset change

Keep `intake` as a directory and topic entry. Put deep notes in a
`reading-notes` page or equivalent section.

## 6. Promotion Decision

Before promoting any takeaway into `AGENTS.md`, `rules/`, `skills/`, specs, or
archive-ready claims, require one accepted evidence shape:

- external-document excerpt with URL and exact section or line reference
- local RED/GREEN demo or fixture with command/manual replay
- git-like project comparison with repository, commit or path, and observable
  structure or behavior difference

Unsupported learning remains a candidate observation.
