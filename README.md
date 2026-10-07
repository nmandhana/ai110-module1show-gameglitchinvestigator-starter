# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**
  The app is a Streamlit number-guessing game: the player picks a difficulty (which sets the number range and attempt limit), then tries to guess a secret number within the allowed attempts. Hints ("Go HIGHER" / "Go LOWER") guide each guess, and a score rewards winning quickly and penalizes wrong guesses.

- [x] **Detail which bugs you found.**
  1. **Inverted hints** — guessing too high told the player to go HIGHER, and vice versa.
  2. **Wrong difficulty mapping** — Normal/Hard did not use their intended ranges and attempt limits.
  3. **Scoring glitches in `update_score`** — a "Too High" guess on an even attempt *added* 5 points instead of subtracting, and the win bonus had an off-by-one (winning on attempt 1 paid 80 instead of 90).
  4. **Invalid input burned an attempt** — typing "abc" consumed an attempt even though no guess was made.
  5. **New Game didn't restart** — after winning or losing, New Game left the old score/status/history, so the game stayed stuck on the game-over screen.
  6. **Attempts off-by-one** — the counter started at 1 on first load, so the first game showed one fewer attempt than allowed.

- [x] **Explain what fixes you applied.**
  - Fixed the swapped comparison in `check_guess` so hints point the right way.
  - Corrected the difficulty-to-range/attempts mapping and made the UI use it dynamically.
  - Rewrote `update_score`: every wrong guess loses 5 points, the win bonus is `100 − 10 × attempt_number` (minimum 10), and any other outcome preserves the score.
  - Moved the attempts increment after input validation, so invalid input preserves both score and attempts.
  - Made New Game reset score, status, and history along with the secret and attempts.
  - Initialized attempts to 0 (guesses used), matching the New Game reset.
  - Refactored all game logic (`parse_guess`, `check_guess`, `get_range_for_difficulty`, `update_score`) out of `app.py` into `logic_utils.py` and covered it with pytest tests.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` and open the app in the browser. In the sidebar, pick a difficulty — the caption shows the matching range and attempt limit (e.g., Normal is 1–50 with 6 attempts), and the banner shows the full attempts remaining.
2. Expand **Developer Debug Info** to see the secret number, current score, and attempts — useful for verifying each fix live.
3. Type something invalid like `abc` and click **Submit Guess**. The app shows "That is not a number." and the debug panel confirms the score and attempts are untouched.
4. Make a wrong guess. The hint now points the correct way ("Go LOWER" when you guessed too high), the score drops by 5, and one attempt is used — on every wrong guess, odd or even.
5. Guess the secret number. Balloons appear, and the win bonus is added (90 points on a first-attempt win, decreasing by 10 per attempt used, never below 10).
6. Click **New Game 🔁**. The score, attempts, history, and status all reset, and a fresh secret is drawn — the game is fully playable again even after a win or loss.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/
============================= test session starts ==============================
collected 17 items

tests/test_game_logic.py .................                               [100%]

============================== 17 passed in 0.01s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
