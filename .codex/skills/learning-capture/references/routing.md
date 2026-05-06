# Learning Capture Routing

Use this reference when intent or source kind is not obvious.

## Intent Gate

| User Intent | Learning Capture? | Route |
|---|---|---|
| Deep-read, `精读`, learn capability, or learn what is useful | yes | classify source kind |
| Bare article, repo, README, or example link inside an active learning / governance / method-calibration thread | yes | classify source kind |
| Source provided immediately after the user asks how learning should work | yes | classify source kind |
| Write to wiki from source learning | yes | classify source kind |
| Score whether a source deserves deep reading | yes | classify source kind |
| Decide what to reuse, adapt, reject, or formalize | yes | classify source kind |
| Turn external-source learning into SOP, template, skill candidate, or workflow decision | yes | classify source kind |
| Latest news or fact lookup | no | answer normally, browsing if needed |
| Raw article / WeChat body fetch only | no | use source-specific reader |
| Bare link with no local reuse context and no learning thread | no | ask or handle as ordinary lookup/fetch |
| Short abstract with no local reuse intent | no | answer normally |
| Generic code review | no | use review workflow |

## Source Kind Gate

| Source Kind | Signal | Module Route |
|---|---|---|
| Article-shaped | article, blog, paper, newsletter, WeChat post, article collection | `article.md` |
| Repo/README-shaped | GitHub/GitLab repo URL, README URL, repo docs, project structure | `repo-readme.md` |
| Example-shaped | output example, writing style, visual structure, workflow shape, method example | `example-reference.md` |
| Mixed | article discusses a repo, repo README supports an article, or example carries a method | start with the directly available source, then route to the second module only when the user asks for that evidence |

## Mixed-Source Rules

- An article about a repo is article-shaped until the repo or README is read.
- A repo README used only for writing structure may be example-shaped.
- A WeChat article used only for raw body extraction should not trigger learning
  capture.
- A secondary interpretation can frame learning, but promotion needs primary
  source or local evidence.

## Output Contract

Every learning result should say:

- source kind
- selected module
- what was learned
- local usefulness
- adoption boundary
- next repository target, if any
