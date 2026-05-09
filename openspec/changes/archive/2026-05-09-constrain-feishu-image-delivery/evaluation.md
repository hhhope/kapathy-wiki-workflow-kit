## RED Baseline 2026-05-09

| Scenario | Current Evidence | RED Result |
|---|---|---|
| User says "图片我自己添加，正文同步飞书" | `SKILL.md` asks at Feishu sync fork-points, but does not state text-only sync as the default when images are user-managed. | FAIL |
| User asks for a Feishu draft with generated chapter images | Existing wording can still combine Feishu text sync and image insertion after a broad approval. | FAIL |
| Feishu image token and read-back exist after insertion | Existing skill body requires read-back before success claims but does not explicitly say image-token read-back is not client-usability proof. | FAIL |
| Client freeze is reported for image-bearing Feishu docs | Repair change records the finding, but reusable pressure scenarios do not yet block further image insertion. | FAIL |

## GREEN Result

| Scenario | GREEN Evidence | Result |
|---|---|---|
| User says "图片我自己添加，正文同步飞书" | `SKILL.md` now says to generate required report visuals as local assets, keep Feishu sync text-only, and preserve local asset paths when the user will add images manually. | PASS |
| User approves Feishu sync without image insertion | `spec.md` requires the Feishu operation to be treated as text-only unless image insertion is explicitly approved. | PASS |
| User explicitly asks the agent to insert Feishu images | `SKILL.md`, `gate-review-artifact.md`, and `spec.md` require stating the known client-freeze risk and recording explicit image-insertion approval. | PASS |
| Feishu image token and read-back exist after insertion | `SKILL.md`, `gate-review-artifact.md`, `pressure-scenarios.md`, and `spec.md` now treat image tokens and read-back logs as audit evidence only, not proof of client usability. | PASS |
| Client freeze is reported for image-bearing Feishu docs | `pressure-scenarios.md` and `spec.md` require stopping further image-included writes and switching to text-only sync, local asset paths, or a separately approved client-safe route. | PASS |

Proof boundary: the GREEN result above proves wording and pressure-scenario
coverage only. It does not yet prove that a fresh runtime invocation will load
`public-report-quality-gate` and choose text-only Feishu sync when the user says
they will add images manually.

## Static Checks

| Check | Result |
|---|---|
| Static wording check | PASS — `rg` found local asset, text-only, client-freeze, image-token, Visual Asset Boundary, and Feishu Image Delivery Replay wording in skill/reference/spec files. |
| Skill body compactness | PASS — `SKILL.md` is 89 lines; longer delivery replay detail lives in references. |
| OpenSpec strict validation | PASS — `openspec validate constrain-feishu-image-delivery --strict` returned `Change 'constrain-feishu-image-delivery' is valid`; PostHog DNS flush errors ignored. |

## Runtime Replay

| Check | Evidence | Result |
|---|---|---|
| Fresh replay artifact exists | `runtime-replay.md` records the input shape, loaded skill files, expected route, observed route, and proof boundary. | PASS |
| Manual image scenario routes correctly | Replay input says images are generated locally and the user will add them manually; observed route keeps Feishu sync text-only and blocks image insertion. | PASS |
| No accidental external action | Replay did not call Feishu or generate new images. | PASS |

## Residual Risks

- This is current-session runtime replay evidence, not multi-session rollout
  proof.
- The change blocks default Feishu image insertion; it does not solve Feishu
  client freezes or remove existing image blocks.
- If a future workflow needs agent-managed Feishu images, it needs a separate
  client-safe image workflow with explicit acceptance evidence.
