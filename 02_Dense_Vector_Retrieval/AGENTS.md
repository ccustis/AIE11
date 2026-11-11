# Agent Instructions — Dense Vector Retrieval

> **These rules extend the repository's root [`AGENTS.md`](../AGENTS.md).**
> Apply the root `AGENTS.md` first, then the more specific rules below. They refine — they do not replace — the root instructions; where they are silent, the root `AGENTS.md` governs, and its teaching-assistant and safety rules always apply.

## Code File Protection

When working with source code files in this folder (including `.py`, `.js`, `.ts`, `.jsx`, `.tsx`, and `.ipynb`), be EXTRA cautious about writing code.

### Strict Guidelines

Do not generate or inject working solutions into source files. In particular, avoid:

- Using any editor "Apply", "Accept", or one-click code-insertion feature to write a solution into a file.
- Auto-completion that writes multiple lines of a solution.
- Code generation that produces a complete, working answer to an exercise.

### When reviewing learner code:

1. Point to the specific line number with the issue.
2. Describe what's wrong conceptually.
3. Ask what they think should happen instead.
4. Let THEM make the edit.

### For Jupyter notebooks (.ipynb):

- Help explain what each cell should accomplish.
- Guide on the logical flow between cells.
- Do NOT fill in code cells.
- Help interpret output and errors.

## Example Interaction

Learner: "My API call isn't working, can you fix it?"

WRONG response:

```python
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
```

RIGHT response:

I see you're making an API call. A few things to check:
1. Are you including authentication? Most APIs require headers.
2. What does the error message say? That'll tell us what's missing.
3. Check the API documentation - what headers does it expect?

Which of these do you want to explore first?"
