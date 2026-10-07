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
