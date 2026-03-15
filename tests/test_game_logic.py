from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug fix tests: parse_guess input validation ---

def test_negative_number_rejected():
    # Negative numbers should not be accepted (e.g., -10 is out of 1-100 range)
    ok, value, err = parse_guess("-10")
    assert ok == False
    assert value is None
    assert err is not None

def test_zero_rejected():
    # 0 is below the valid range of 1-100
    ok, value, err = parse_guess("0")
    assert ok == False
    assert value is None
    assert err is not None

def test_above_100_rejected():
    # Numbers above 100 should not be accepted
    ok, value, err = parse_guess("101")
    assert ok == False
    assert value is None
    assert err is not None

def test_decimal_number_rejected():
    # Decimal inputs like 3.7 should not be accepted
    ok, value, err = parse_guess("3.7")
    assert ok == False
    assert value is None
    assert err is not None

def test_decimal_whole_rejected():
    # Even "5.0" should be rejected since it contains a decimal point
    ok, value, err = parse_guess("5.0")
    assert ok == False
    assert value is None
    assert err is not None

def test_valid_guess_accepted():
    # A normal in-range integer should be accepted
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

def test_boundary_low_accepted():
    # 1 is the lowest valid guess
    ok, value, err = parse_guess("1")
    assert ok == True
    assert value == 1

def test_boundary_high_accepted():
    # 100 is the highest valid guess
    ok, value, err = parse_guess("100")
    assert ok == True
    assert value == 100


# --- Bug fix tests: check_guess feedback direction ---

def test_high_guess_returns_too_high():
    # Guessing 21 when secret is 5 — should be Too High (go lower), not Too Low
    result = check_guess(21, 5)
    assert result == "Too High"

def test_low_guess_returns_too_low():
    # Guessing 3 when secret is 7 — should be Too Low (go higher)
    result = check_guess(3, 7)
    assert result == "Too Low"

def test_negative_guess_vs_positive_secret():
    # Guessing -10 when secret is 7 — should be Too Low (go higher), not Too High
    # (This bug was caused by string comparison on even attempts)
    result = check_guess(-10, 7)
    assert result == "Too Low"
