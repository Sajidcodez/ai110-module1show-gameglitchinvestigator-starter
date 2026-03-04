from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# --- Existing starter tests (fixed to match tuple return) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- New tests targeting our bug fixes ---

#FIX: Test that hints point the correct direction after swapping them
def test_too_high_hint_says_lower():
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, "When guess is too high, hint should say LOWER"

def test_too_low_hint_says_higher():
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, "When guess is too low, hint should say HIGHER"

#FIX: Test that Hard difficulty range is larger than Normal
def test_hard_range_is_harder_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, "Hard range should be larger than Normal"

#FIX: Test that difficulty ranges return correct values
def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 200

#FIX: Test parse_guess handles valid and invalid input
def test_parse_valid_number():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False and value is None

def test_parse_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False and "not a number" in err
