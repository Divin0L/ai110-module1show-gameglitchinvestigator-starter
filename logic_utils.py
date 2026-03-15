# CHANGED: moved get_range_for_difficulty here from app.py so all game logic
# lives in one place and app.py only handles UI.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


# CHANGED: moved parse_guess here from app.py for the same reason.
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


# CHANGED: check_guess now returns only the outcome string ("Win", "Too High",
# "Too Low") so tests can assert directly on the return value.
# Previously returned a tuple (outcome, message) which broke the test assertions.
# Both arguments are kept as ints — no str() casting — so comparisons are
# always numeric and correct.
def check_guess(guess: int, secret: int) -> str:
    """
    Compare guess to secret and return the outcome as a string.

    Returns: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


# Hint messages shown in the UI, keyed by outcome from check_guess.
# FIXED: hints were backwards — "Too High" means the guess is above the secret
# so the player needs to go LOWER, and "Too Low" means go HIGHER.
HINT_MESSAGES = {
    "Win": "🎉 Correct!",
    "Too High": "📉 Go LOWER!",
    "Too Low": "📈 Go HIGHER!",
}


# CHANGED: moved update_score here from app.py for the same reason.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
