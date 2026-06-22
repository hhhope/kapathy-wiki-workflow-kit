# Web Patterns

## Stack Boundary

- The frontend stack is Vue 3 + Vite. Prefer the existing component/page structure and do not transplant React/Next templates.
- Do not add new frontend UI dependencies unless the user explicitly agrees and the benefit is material.

## State and Interaction

- Cross-page state such as login session, team scope, and platform-admin view selection should be centralized in one shared state source instead of reimplemented per page.
- After list-page create/update/delete/toggle actions, the UI must refresh to the latest data and latest `version`.
- 409 conflicts, 401/403 authorization failures, and network errors need readable user-facing messages; do not expose raw technical exceptions directly.

## API Calls

- Before consuming a new field, verify field names and payload structure from a real API response.
- Write-action buttons need loading state, duplicate-click prevention, and success/failure feedback.
- Short actions such as database connection tests should prefer inline button feedback over modal alerts.

## Large-File Splitting

- If a Vue / JS file exceeds 200 lines, prioritize extracting composables, child components, config models, or utility functions.
- Do not heavily rewrite template, script, styles, and API wiring in one patch. Close work in stages: skeleton -> data/interaction wiring -> style/detail refinement.
