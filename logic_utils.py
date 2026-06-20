# COLLAB: I asked AI (agent mode) to refactor the core logic functions out of app.py into this module
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    # FIXED: swapped Normal/Hard ranges so Hard is the widest (hardest), not narrower than Normal
    # COLLAB: AI flagged that Hard was narrower than Normal; I decided to swap them and AI applied it
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str, low=1, high=100):
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

    # FIXED: added range check so out-of-range numbers (e.g. negatives) are rejected instead of accepted as valid guesses
    # COLLAB: I described the negative-number bug; AI located the missing check and wrote the fix
    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    try:
        # FIXED: swapped the hint messages so a too-high guess says "Go LOWER" and a too-low guess says "Go HIGHER"
        # COLLAB: I spotted the reversed hints while playing; AI confirmed the cause and swapped the messages
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        # FIXED: swapped hints here too so too-high says "Go LOWER" and too-low says "Go HIGHER"
        # COLLAB: AI found this fallback path still had the old reversed hints and fixed it to match
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


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
