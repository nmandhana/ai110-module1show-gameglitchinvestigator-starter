import logic_utils

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = logic_utils.check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    # and the player must be told to go LOWER (this was the inverted-hint bug)
    outcome, message = logic_utils.check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    # and the player must be told to go HIGHER
    outcome, message = logic_utils.check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_easy_range():
    # Easy mode should use the full 1 to 100 range
    assert logic_utils.get_range_for_difficulty("Easy") == (1, 100)

def test_normal_range():
    # Normal mode should use 1 to 50 (this was the swapped-range bug)
    assert logic_utils.get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    # Hard mode should use 1 to 20
    assert logic_utils.get_range_for_difficulty("Hard") == (1, 20)

def test_unknown_difficulty_falls_back_to_default_range():
    # Any unrecognized difficulty should fall back to 1 to 100
    assert logic_utils.get_range_for_difficulty("Impossible") == (1, 100)

def test_win_on_first_attempt_awards_90_points():
    # Winning on attempt 1 should pay 100 - 10*1 = 90 (this was the off-by-one bug)
    assert logic_utils.update_score(0, "Win", 1) == 90

def test_win_on_late_attempt_awards_minimum_10_points():
    # The win bonus should never drop below 10, no matter how many attempts
    assert logic_utils.update_score(0, "Win", 12) == 10

def test_too_high_always_loses_5_points():
    # A "Too High" guess must lose 5 points even on even attempts
    # (this was the glitch that rewarded wrong guesses with +5)
    assert logic_utils.update_score(50, "Too High", 2) == 45
    assert logic_utils.update_score(50, "Too High", 3) == 45

def test_too_low_loses_5_points():
    # A "Too Low" guess loses 5 points
    assert logic_utils.update_score(50, "Too Low", 1) == 45

def test_other_outcome_preserves_score():
    # Any other outcome (e.g. invalid input) should leave the score unchanged
    assert logic_utils.update_score(50, "Invalid", 1) == 50

def test_parse_guess_valid_integer():
    # A plain integer string should parse successfully
    assert logic_utils.parse_guess("42") == (True, 42, None)

def test_parse_guess_decimal_truncates_to_int():
    # A decimal string is accepted and truncated to an int
    assert logic_utils.parse_guess("7.9") == (True, 7, None)

def test_parse_guess_empty_string_is_rejected():
    # Empty input should fail with a prompt to enter a guess
    assert logic_utils.parse_guess("") == (False, None, "Enter a guess.")

def test_parse_guess_none_is_rejected():
    # None input should fail with a prompt to enter a guess
    assert logic_utils.parse_guess(None) == (False, None, "Enter a guess.")

def test_parse_guess_non_number_is_rejected():
    # Non-numeric input should fail with a clear error message
    assert logic_utils.parse_guess("abc") == (False, None, "That is not a number.")
