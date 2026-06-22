# Python Security Rules

## FastAPI Boundaries

- Request bodies and query parameters must be type-validated; do not pass user input directly into SQL, file paths, or shell commands.
- API errors returned to the frontend should contain only necessary business information; detailed exceptions belong in server-side logs.
- For new routes, verify the current user, team scope, role permissions, and read-only constraints for shared objects.

## SQL Safety

- Use parameterized MySQL queries or a safe query builder; do not compose user input with f-strings.
- If dynamic table names, field names, or sort fields are unavoidable, map them through a whitelist.
- Cross-team reads must include explicit team constraints, and shared-read paths must preserve `source_team` vs `executor_team` semantics.

## External Processes and File Paths

- Do not compose shell commands from user input. If a command is required, prefer argument-array execution.
- File paths must be constrained to an allowed root and reject `..` traversal.
- Do not persist or echo plaintext secret fields in raw/log/config files.
