# Skill: Behaviour & User Focus

## Purpose
Ensure code reflects intended user behaviour, not internal implementation details.

## When to consult
- Naming new functions, classes, or modules
- Deciding how to organize code
- Reviewing existing names that feel unclear

## Instructions

### Naming
Name things by **what they achieve**, not **how they work**.

| ❌ Implementation-focused | ✅ Behaviour-focused |
|---------------------------|----------------------|
| `hash_password()` | `secure_password()` |
| `send_smtp_email()` | `notify_user()` |
| `query_database_for_users()` | `find_users()` |
| `run_validation_loop()` | `validate_order()` |
| `UserDBModel` | `User` |

### Decision heuristic
When naming, ask: *"If the implementation changed completely, would this name still make sense?"*

- If yes → good name
- If no → rename to describe the outcome

### Organization
Group code by **behaviour/capability**, not by technical layer.

```
# ❌ Organized by layer
models/user.py
services/user_service.py
validators/user_validator.py

# ✅ Organized by behaviour
users/user.py           # User entity and core behaviour
users/registration.py   # Registration workflow
users/verification.py   # Email verification workflow
```

## Failure modes to watch
- Splitting behaviour across layers instead of keeping it cohesive
- Names that feel awkward to say out loud when describing what code does