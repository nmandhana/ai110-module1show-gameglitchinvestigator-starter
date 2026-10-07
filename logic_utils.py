def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 100
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 20
    return 1, 100


#FIX: Refactor parse_guess from app.py into logic_utils
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Fix inverted hint bug and refactor check_guess into logic_utils
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess < secret:
            return "Too Low", "📈 Go HIGHER!"
        else:
            return "Too High", "📉 Go LOWER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g < secret:
            return "Too Low", "📈 Go HIGHER!"
        return "Too High", "📉 Go LOWER!"


#FIX: Fix wrong-guess bonus and win off-by-one, refactor update_score into logic_utils
def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    Win: add a bonus of 100 - 10 per attempt used (minimum 10).
    Too High / Too Low: lose 5 points.
    Anything else (e.g. invalid input): score is preserved.
    """
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
