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
