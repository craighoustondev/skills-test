# Skill: Responsibility Boundaries

## Purpose
Guide modular code with clear, single responsibilities per module.

## When to consult
- Adding new features or functionality
- Extending existing classes or modules
- Deciding where new code should live
- A file exceeds 200 lines

## Instructions

### The single question test
Before adding code to an existing module, ask:

*"Can I describe what this module does in one sentence without using 'and'?"*

- If yes → the responsibility is clear
- If no → consider splitting

### Decision tree: Where should new code live?

```
New feature/behaviour needed
    │
    ├─ Does it fit an existing module's single responsibility?
    │   ├─ Yes → Add it there
    │   └─ No ↓
    │
    ├─ Is it a new responsibility?
    │   ├─ Yes → Create a new module
    │   └─ No, it's shared logic ↓
    │
    └─ Is it used by 3+ modules?
        ├─ Yes → Create a shared module named by its responsibility (e.g., `date_calculations.py`, not `utils.py`)
        └─ No → Duplicate it (duplication is cheaper than wrong abstraction)
```

### Size thresholds (guidelines, not rules)
| Metric | Review threshold | Action |
|--------|------------------|--------|
| File length | > 200 lines | Consider splitting by responsibility |
| Function length | > 30 lines | Extract sub-functions |
| Class methods | > 10 methods | May have multiple responsibilities |
| Parameters | > 4 parameters | Consider a parameter object or splitting |

### Example: Splitting by responsibility

```python
# ❌ user.py with mixed responsibilities (300 lines)
class User:
    def __init__(self, name, email): ...
    def validate_email(self): ...      # validation
    def send_welcome_email(self): ...  # notification
    def hash_password(self): ...       # security
    def save(self): ...                # persistence

# ✅ Split by responsibility
# users/user.py - core entity
class User:
    def __init__(self, name, email): ...

# users/registration.py - registration workflow
def register_user(name, email, password): ...

# users/notifications.py - user notifications
def send_welcome_email(user): ...
```

## Failure modes to watch
- Adding "just one more method" to an already large class
- Comments like "# TODO: refactor this" that never get addressed
