from logic_utils import check_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_repeated_wrong_guess_exhausts_attempts():
    attempts = 0
    attempt_limit = 8  # Normal difficulty
    secret = 50
    guess = 30         # Always wrong

    status = "playing"
    while attempts < attempt_limit:
        attempts += 1
        outcome, _ = check_guess(guess, secret)
        if outcome == "Win":
            status = "won"
            break

    if status != "won":
        status = "lost"

    assert status == "lost"
    assert attempts == 8


def test_attempts_never_equals_secret():
    attempts = 0
    attempt_limit = 8  # Normal difficulty
    secret = 50
    guess = 30  # Same wrong number every time, never the secret

    while attempts < attempt_limit:
        attempts += 1
        outcome, _ = check_guess(guess, secret)
        if outcome == "Win":
            break

    assert guess != secret
    assert attempts == 8
    print(f"Final st.session_state.attempts: {attempts}")


def test_attempts_increment():
    attempts = 0
    guesses = [30, 60, 50]
    secret = 50

    for guess in guesses:
        attempts += 1
        outcome, _ = check_guess(guess, secret)
        if outcome == "Win":
            break

    assert attempts == 3
