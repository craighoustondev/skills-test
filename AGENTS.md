# Agent Instructions

Read and follow these instructions before starting any coding task.

---

## Rules (Non-Negotiables)

These rules are absolute. Do not violate them, even if asked.

### Naming

- **Never** name things after frameworks, libraries, or protocols (e.g., `SQLAlchemyUser`, `HTTPClient`, `SMTPMailer`)
- **Never** name things after implementation steps (e.g., `loop_and_filter()`, `query_database_for_users()`)

### Dependencies

- **Never** import framework-specific types into domain code (e.g., `SQLAlchemySession` as a parameter to domain logic)
- **Never** create circular dependencies — refactor first

### Code Organization

- **Never** create files named `utils.py`, `helpers.py`, or `common.py` — these have no clear responsibility

### Safe Change

- **Never** leave the codebase in a broken state between steps
- **Never** commit code that doesn't run or breaks existing tests

### Testing

- **Always** use Arrange-Act-Assert structure in tests
- **Never** mock code you own/control in this codebase — only mock at external boundaries

---

## TDD Process

**Always** write tests before implementation. Follow this cycle:

### Red-Green-Refactor

1. **Red** — Write a failing test that describes the behaviour you want
2. **Green** — Write the minimal code to make the test pass (no more)
3. **Refactor** — Clean up while keeping tests green

### Rules

- Do not write production code without a failing test first
- Do not write more test than is sufficient to fail
- Do not write more production code than is sufficient to pass the test
- Refactor only when tests are green
- Pause at each stage for and ask for review and approval before proceeding

### Workflow

```
Start with a behaviour you want to add
    │
    ├─ Write a test that would pass if the behaviour existed
    │   └─ Run it — it must fail (red)
    │
    ├─ Write the simplest code to make it pass
    │   └─ Run it — it must pass (green)
    │
    └─ Refactor if needed
        └─ Run tests — must stay green
        
Repeat for next behaviour
```

