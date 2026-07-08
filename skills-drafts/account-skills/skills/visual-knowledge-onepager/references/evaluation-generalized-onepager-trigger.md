# Evaluation: generalized visual one-pager trigger

Date: 2026-05-07

## Pressure Scenarios

| Scenario | Expected routing |
|---|---|
| "把 learning-capture / agent / wiki / OpenSpec 的治理目标做成 H5" | Load this skill as a visual knowledge one-pager task, not material processing. |
| "把一篇文章做成一图流 HTML" | Load this skill and use the HTML one-pager branch. |
| "做小红书爆款干货多图" | Load this skill and use the carousel branch. |
| "画系统架构图" | Do not use this skill first; prefer an architecture diagram skill. |
| "做项目周报甘特 H5" | Do not use this skill first; prefer the project weekly report skill. |

## RED Baseline

Command:

```bash
test "$(sed -n '2p' skills/visual-knowledge-onepager/SKILL.md)" = "name: visual-knowledge-onepager"
sed -n '3p' skills/visual-knowledge-onepager/SKILL.md | rg "governance idea|abstract framework|dense visual one-pager|screenshot-friendly single-file HTML"
```

Result before change: both checks failed.

Observed failure:

- The old local source directory name was channel-specific, so the identity was
  easy to mistake for one platform style.
- The description mentioned HTML and infographic output, but the primary trigger surface was still Xiaohongshu-specific.

## GREEN Result

Expected after change:

- Metadata name is `visual-knowledge-onepager`.
- Description includes generic triggers for concepts, governance ideas, learning notes, abstract frameworks, dense one-pagers, H5, long infographics, retro-grid cards, Xiaohongshu-style carousel, and screenshot-friendly single-file HTML.
- Xiaohongshu remains as one output style rather than the skill identity.
- The 3-input intake requirement applies only to carousel outputs, not H5 / HTML / one-pager requests.
- HTML visual modes route abstract governance metaphors to `handdrawn-teaching` unless a dense grid is requested.

## Residual Risks

- The account-skills package uses `skills/visual-knowledge-onepager` as the
  local directory, so skill discovery and metadata now use the same generalized
  name.
- This is local pressure-test evidence, not proof that every runtime skill index will refresh immediately.
