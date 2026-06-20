from logic_utils import check_guess, parse_guess, get_range_for_difficulty


# check_guess returns a tuple: (outcome, message)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # CHANGED: unpack the (outcome, message) tuple and compare the outcome
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: hints were reversed ---
# A too-high guess must tell the player to go LOWER, and a too-low guess
# must tell them to go HIGHER. Before the fix these were swapped.

def test_too_high_guess_hint_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()


def test_too_low_guess_hint_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


# --- Bug 2: out-of-range numbers were accepted as valid guesses ---
# parse_guess returns (ok, value, error_message). Numbers outside the
# allowed range (e.g. negatives) must be rejected.

def test_negative_number_is_rejected():
    ok, value, error = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert error is not None


def test_number_above_range_is_rejected():
    ok, _, error = parse_guess("150", 1, 100)
    assert ok is False
    assert error is not None


def test_in_range_number_is_accepted():
    ok, value, error = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert error is None


# --- Bug 3: difficulty ranges were wrong (Hard was narrower than Normal) ---
# After the fix: Easy 1-20, Normal 1-50, Hard 1-100.

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range_is_widest():
    assert get_range_for_difficulty("Hard") == (1, 100)
