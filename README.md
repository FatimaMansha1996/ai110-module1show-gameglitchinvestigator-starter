# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Game's purpose:** A Streamlit number-guessing game. You pick a difficulty (Easy, Normal, Hard), the game picks a secret number in that range, and you guess using "Go HIGHER"/"Go LOWER" hints until you win or run out of attempts.

**Bugs I found:**
1. It showed "Attempts left: 7" before any guess, even though Settings said 8.
2. Out-of-range numbers (like negatives) were accepted as valid guesses.
3. The hints were reversed — too-high said "Go HIGHER," too-low said "Go LOWER."
4. The range check used 1–100 for every difficulty instead of the chosen one (Normal should be 1–50).

**Fixes I applied:**
1. Started the attempts counter at 0 instead of 1.
2. Added a range check in `parse_guess` to reject out-of-range numbers.
3. Swapped the hint messages in `check_guess` so they point the right way.
4. Fixed the difficulty ranges, passed the real range into `parse_guess`, updated the UI, and moved the logic into `logic_utils.py`.

**Tests I wrote:** I added pytest tests in `tests/test_game_logic.py` that target each bug — checking the hints point the right way (e.g. a guess of 60 vs 50 returns "Too High"), that out-of-range numbers are rejected (including per-difficulty, like 75 on Normal), and that each difficulty returns the correct range. All 14 tests pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The game opens on **Normal** difficulty by default, showing "Guess a number between 1 and 50" and "Attempts left: 8."
2. Player guesses **25** → "Too Low" with the hint "📈 Go HIGHER!"; attempts left drops to 7.
3. Player guesses **40** → "Too High" with the hint "📉 Go LOWER!"; attempts left drops to 6.
4. Player guesses **-5** → rejected with "Enter a number between 1 and 50" instead of being treated as a real guess.
5. Player guesses **33** → "🎉 Correct!", balloons appear, the secret (33) is revealed, and the final score is shown.
6. The score updates after each guess, and the game ends once the correct number is found.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts =============================
platform win32 -- Python 3.13.3, pytest-9.1.0, pluggy-1.6.0
configfile: pytest.ini
collected 14 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  7%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 14%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 21%]
tests/test_game_logic.py::test_too_high_guess_hint_says_go_lower PASSED  [ 28%]
tests/test_game_logic.py::test_too_low_guess_hint_says_go_higher PASSED  [ 35%]
tests/test_game_logic.py::test_negative_number_is_rejected PASSED        [ 42%]
tests/test_game_logic.py::test_number_above_range_is_rejected PASSED     [ 50%]
tests/test_game_logic.py::test_in_range_number_is_accepted PASSED        [ 57%]
tests/test_game_logic.py::test_normal_range_rejects_above_50 PASSED      [ 64%]
tests/test_game_logic.py::test_easy_range PASSED                         [ 71%]
tests/test_game_logic.py::test_normal_range PASSED                       [ 78%]
tests/test_game_logic.py::test_hard_range_is_widest PASSED               [ 85%]
tests/test_game_logic.py::test_string_secret_too_high_says_go_lower PASSED [ 92%]
tests/test_game_logic.py::test_string_secret_too_low_says_go_higher PASSED [100%]

============================= 14 passed in 0.03s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
