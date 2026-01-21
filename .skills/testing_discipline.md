# Skill: Testing Discipline

## Purpose
Maintain confidence in code through clear, behaviour-focused tests.

## When to consult
- Writing or modifying tests
- Deciding what to test
- Choosing whether to use mocks
- Tests break after refactoring (sign of implementation coupling)

## Instructions

### Test behaviour, not implementation

A good test should **not need to change** if you refactor the implementation.

```python
# ❌ Tests implementation (will break if we change how verification works)
def test_verify_email_sets_flag_and_clears_token():
    user = User("alice", "alice@example.com")
    user._verification_token = "abc123"
    
    user.verify_email("abc123")
    
    assert user.email_verified == True
    assert user._verification_token is None  # Testing internal state

# ✅ Tests behaviour (survives refactoring)
def test_verified_user_can_access_protected_features():
    user = create_user("alice@example.com")
    verify_user(user)
    
    result = access_protected_feature(user)
    
    assert result.is_allowed
```

### Arrange-Act-Assert structure

Every test should have three distinct sections:

```python
def test_new_user_email_is_not_verified():
    # Arrange - set up preconditions
    user = User(name="Alice", email="alice@example.com")
    
    # Act - perform the action being tested
    is_verified = user.email_verified
    
    # Assert - verify the outcome
    assert is_verified == False
```

### Test naming

Name tests as **behaviour specifications**:

| ❌ Implementation-focused | ✅ Behaviour-focused |
|---------------------------|----------------------|
| `test_hash_password` | `test_password_is_stored_securely` |
| `test_send_email_calls_smtp` | `test_user_receives_welcome_message` |
| `test_validate_returns_false` | `test_invalid_email_is_rejected` |

### Mocking strategy

**Mock at boundaries, not internally.**

```python
# ❌ Mocking internal code
def test_registration(mock_validator, mock_hasher, mock_repo):
    # Tightly coupled to implementation details
    mock_validator.return_value = True
    mock_hasher.return_value = "hashed"
    register_user("alice@example.com", "password")
    mock_repo.save.assert_called_once()

# ✅ Mocking only external boundary
def test_registration_sends_welcome_email(mock_email_service):
    register_user("alice@example.com", "password")
    
    mock_email_service.send.assert_called_with(
        to="alice@example.com",
        template="welcome"
    )
```

### Decision tree: Should I mock this?

```
Is it an external service (DB, API, email, filesystem)?
    ├─ Yes → Mock it at the boundary
    └─ No ↓

Is it slow (> 100ms)?
    ├─ Yes → Consider mocking or using a faster alternative
    └─ No ↓

Is it code I control in this codebase?
    ├─ Yes → Don't mock it, test through it
    └─ No → Mock it
```

### What to test

| Always test | Sometimes test | Rarely test |
|-------------|----------------|-------------|
| Public behaviour | Edge cases | Private methods |
| Business rules | Error messages | Framework code |
| State transitions | Performance | Logging |
| Boundary conditions | Integration points | Getters/setters |

## Failure modes to watch
- Tests that mirror the implementation step-by-step
- Mocking code you own (usually means design needs work)
- `test_it_works()` or `test_function_name()` (unclear what behaviour is expected)
- Tests that pass when the feature is broken
- Skipping tests because "it's too hard to test" (design smell)
