# Security Rules

## Baseline

- Do not hardcode passwords, tokens, API keys, webhooks, or database connection strings in code or docs.
- Do not return internal stack traces, raw SQL, secrets, or plaintext PII to the frontend or logs.
- Validate or whitelist all user input, request parameters, request bodies, file paths, and dynamic SQL fragments at the system boundary.

## API and Authorization

- For new or modified APIs, verify authentication, authorization, team scope, role boundaries, and cross-team sharing semantics.
- Write operations are restricted to team admins/owners by default; read-only member restrictions must be enforced by the backend, not only by hidden frontend buttons.
- Cross-team shared objects are read-only references: the source team owns maintenance, while target teams can use them but cannot edit or delete them.

## SQL and External Calls

- SQL queries must use parameterized execution; do not concatenate user input into query strings.
- External HTTP calls must set a timeout and return diagnosable errors without leaking secrets.
- For a new API or new field, inspect a real raw response first and verify field names and structure before writing business mapping logic.

## Dependencies and Logs

- Before adding a dependency, check maintenance status, license, and whether the dependency is necessary.
- Structured logs should include object type, object ID, team, action, version, and result, but must not record plaintext secrets.
