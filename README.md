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
  - A Streamlit-based number guessing game where the player picks a difficulty, guesses a secret number within a range, and receives hints after each attempt.
- [x] Detail which bugs you found.
  - Hard difficulty range (1-50) was easier than Normal (1-100)
  - "Guess a number between 1 and 100" was hardcoded regardless of difficulty
  - New Game button didn't reset score, status, or history, and generated numbers from 1-100 ignoring difficulty
  - Attempt counter started at 1 instead of 0
  - Hints were backwards ("Go HIGHER" when guess was too high)
  - TypeError crash on even attempts due to secret being converted to a string
  - Score off-by-one: winning formula used `attempt_number + 1` giving 10 fewer points
  - "Too High" scoring was inconsistent (+5 on even attempts, -5 on odd)
  - Switching difficulty didn't regenerate the secret number within the new range
- [x] Explain what fixes you applied.
  - Changed Hard range to 1-200
  - Used f-string with `{low}` and `{high}` for dynamic range display
  - New Game now resets all session state fields and uses `random.randint(low, high)`
  - Changed initial attempts to 0
  - Swapped hint messages so "Too High" says "Go LOWER" and vice versa
  - Removed buggy int-to-string conversion that caused TypeError on even attempts
  - Fixed score formula from `attempt_number + 1` to `attempt_number`
  - Made "Too High" scoring consistent (-5 always, matching "Too Low")
  - Added difficulty tracking so secret regenerates when switching levels
  - Changed Easy attempts from 6 to 10 for better gameplay balance
  - Refactored all game logic from app.py into logic_utils.py

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
