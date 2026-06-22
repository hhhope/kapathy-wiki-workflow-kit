# Java Security Rules

## API Boundaries

- Request bodies, query parameters, headers, and path variables must be validated and normalized before they reach business logic.
- Default string-boundary rule: trim leading and trailing whitespace before authorization, lookup, deduplication, or persistence decisions.
- Length limits are required for externally supplied string inputs. Do not let unbounded fields flow into logs, SQL, caches, message queues, or remote clients.
- New endpoints must verify the current user, tenant or team scope, role permissions, and read-only constraints before mutating shared data.
- API errors returned to clients should expose only necessary business information; detailed exception data belongs in server-side logs.

## SQL and Persistence Safety

- Use parameterized queries, MyBatis placeholders, JPA parameters, or a safe query builder; never concatenate user input into SQL.
- If dynamic table names, column names, or sort fields are unavoidable, map them through a strict whitelist.
- Repository queries that cross tenant or team boundaries must include explicit scope constraints; do not rely on caller discipline alone.
- Do not persist raw request payloads or free-form exception strings when they may contain secrets, tokens, or personal data.

## Logging and Sensitive Data

- Do not log plaintext passwords, tokens, cookies, authorization headers, bank-card data, or secret configuration values.
- For validation failures, log the rejected field and rule when useful, but avoid echoing full sensitive payloads.
- Use structured logging fields where possible so filtering and redaction stay reliable.

## External Calls and Files

- Do not compose shell commands from user input. If process execution is required, prefer argument-array APIs and strict allowlists.
- External HTTP or RPC calls must define timeouts and avoid forwarding unchecked user input directly into downstream requests.
- File paths must stay within an allowed root and reject traversal patterns such as `..`.
- Deserialization of uploaded or remote content must use trusted libraries and explicit target types; avoid permissive polymorphic deserialization defaults.
