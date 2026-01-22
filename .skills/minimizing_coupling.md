# Skill: Minimize Coupling

## Purpose
Keep code easy to understand and safe to change by limiting unnecessary dependencies.

## When to consult
- Adding an import statement
- Considering whether to create a shared abstraction
- Integrating with external libraries or frameworks

## Instructions

### Dependency direction
Dependencies should flow **inward** toward domain logic, never outward.

```
# ❌ Domain depends on framework
class User:
    def save(self):
        db.session.add(self)  # SQLAlchemy leaked into domain

# ✅ Domain is framework-agnostic
class User:
    pass  # Pure domain object

# Repository handles persistence separately
class UserRepository:
    def save(self, user: User):
        db.session.add(UserModel.from_domain(user))
```

### Decision heuristic: Should I add this import?

1. Is this import from the same module/package? → **Yes, add it**
2. Is this a stdlib import (typing, dataclasses, datetime)? → **Yes, add it**
3. Is this import for domain logic depending on infrastructure? → **No, invert the dependency**
4. Will this create a circular dependency? → **No, refactor first**
5. Is there a simpler way without this dependency? → **Prefer the simpler way**

### Abstractions
Only introduce an abstraction when:
- It removes **duplication** (3+ similar implementations)
- It creates a **clear boundary** (e.g., repository pattern for persistence)
- It makes code **easier to read** (not just "more flexible")

If none apply, prefer concrete code over abstraction.

## Failure modes to watch
- Importing a large library for one small function (copy the function instead)
- Premature abstractions ("we might need this later")
- God modules that everything imports from
