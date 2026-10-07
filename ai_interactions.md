# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I used Claude Code and asked it to fix `update_score` so that a wrong guess reduces the score and uses an attempt, a correct guess is never penalized, and invalid input preserves both score and attempts. Later I extended the task: refactor the remaining logic (`parse_guess`) into `logic_utils.py`, fix New Game not resetting after a win/loss, and fix the attempts counter starting at 1.

**What did the agent do?**

- Read `app.py` and `logic_utils.py`, identified three issues, and explained them before changing anything: the even-attempt +5 reward for "Too High" guesses, the off-by-one in the win bonus, and the attempts increment running before input validation.
- Implemented the corrected `update_score` in `logic_utils.py`, deleted the buggy copy in `app.py`, and updated the import.
- Moved the attempts increment inside the valid-input branch so invalid input costs nothing.
- Refactored `parse_guess` into `logic_utils.py`, made New Game reset score/status/history, and changed the attempts initializer from 1 to 0.
- Added 10 pytest tests across `update_score` and `parse_guess` and ran the suite (17 passed) plus a smoke check of the running Streamlit app after each change.
- Helped with Git: diagnosed why `git pull` showed nothing (local was *ahead* of origin, not behind) and pushed the commits.

**What did you have to verify or fix manually?**

- I chose the win semantics: the agent flagged that my wording ("preserve the score on a win") could mean no bonus at all, and recommended the bonus formula instead — I confirmed that interpretation before it edited.
- After committing, a stale editor buffer on my machine overwrote `logic_utils.py` and silently reverted `update_score` to the unimplemented stub. The agent caught the mismatch against the commit and restored the file, but it took my report that the editor looked wrong to surface it.
- I verified the fixes manually in the browser (invalid input, wrong guesses on even attempts, winning, New Game after a win) rather than trusting the unit tests alone.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Wrong guess on an even attempt (the alternating +5 glitch) | Asked Claude to fix update_score so wrong guesses reduce the score, then add tests | `test_too_high_always_loses_5_points` asserts −5 at attempt 2 **and** attempt 3 | Yes (after the fix; it fails against the original code) | Testing both parities is what locks out the `% 2 == 0` bonus from regressing |
| Win bonus floor on a very late win | Same session; Claude proposed boundary cases | `test_win_on_late_attempt_awards_minimum_10_points` (attempt 12 → +10) | Yes | The formula goes negative past attempt 9, so the floor needs its own test |
| Decimal input like "7.9" | Asked for parse_guess tests while refactoring it to logic_utils | `test_parse_guess_decimal_truncates_to_int` expects `(True, 7, None)` | Yes | Documents the current truncation behavior so a future change to it is a conscious decision |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
