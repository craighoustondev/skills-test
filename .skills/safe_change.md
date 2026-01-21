# Skill: Safe Change & Incremental Implementation

## Purpose
Implement changes incrementally, verifying each step before proceeding.

## When to consult
- Planning how to implement a multi-step task
- A task involves changes across 3+ files
- Estimated changes exceed 100 lines
- Uncertainty about the right approach

## Instructions

### Complexity triggers: When to pause and plan

Before diving into implementation, check:

| Condition | Action |
|-----------|--------|
| Task touches 5+ files | Outline the plan and confirm approach first |
| Task involves 3+ distinct changes | List the steps before starting |
| Changes exceed 100 lines | Break into smaller logical units |
| Design decision is ambiguous | Ask for clarification rather than guess |

### Breaking down work

Each step in a multi-step task should be:

1. **Independently verifiable** — can confirm it works before moving on
2. **Independently reversible** — easy to undo if the approach is wrong
3. **Leaves codebase working** — no broken intermediate states

### Example: Breaking down a feature

Task: *"Add email verification for new users"*

```
# ❌ One large change
- Implement everything at once, hope it works

# ✅ Incremental steps (verify each before proceeding)
1. Add `email_verified` field to User → verify: field exists, defaults correct
2. Add verification token generation → verify: tokens generate correctly
3. Add endpoint to request verification → verify: endpoint responds
4. Add endpoint to confirm verification → verify: verification works end-to-end
5. Add UI for verification flow → verify: user can complete flow
```

### Decision heuristic: Should I break this up?

- Does this task do more than one thing? → **Break it up**
- Am I changing unrelated parts of the codebase? → **Break it up**
- If step 3 fails, will I lose work from steps 1-2? → **Commit incrementally**
- Am I unsure if my approach is right? → **Pause and ask**

### Commit strategy

When suggesting commits:

| Guideline | Rationale |
|-----------|-----------|
| One logical change per commit | Easy to review, easy to revert |
| Commit message explains *why* | Future readers need context |
| Don't bundle unrelated changes | Even if done in the same session |
| Commit working states only | No "WIP" commits that break things |

### Verification checkpoints

After each logical unit of work:
- [ ] Code runs without errors
- [ ] Existing tests still pass
- [ ] New behaviour works as expected
- [ ] Ready to build the next step on top

### When to ask vs. proceed

```
Am I confident this is the right approach?
    ├─ Yes → Proceed
    └─ No ↓

Is the decision easily reversible?
    ├─ Yes → Proceed, but note the assumption
    └─ No ↓

Could the wrong choice waste significant effort?
    ├─ Yes → Ask for clarification
    └─ No → Make a reasonable choice and note it
```

## Failure modes to watch
- Making all changes at once, then debugging a tangled mess
- Proceeding with uncertainty when asking would take 10 seconds
- Bundling "one more quick fix" into an unrelated change
- Leaving the codebase in a broken state between steps
