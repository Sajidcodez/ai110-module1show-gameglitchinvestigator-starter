# 💭 Reflection: Game Glitch Investigator

It seems like a cool web version of the guessing number game. However, right away I noticed a couple bugs that if refined, can make this game a lot better and more interactive.

## 1. What was broken when you started?

- **Difficulty ranges are wrong:** I expected Hard mode to have a larger range than Normal, but Hard was 1-50 while Normal was 1-100, making Hard actually easier.
- **Hardcoded range message:** I expected the "Guess a number between X and Y" message to update when switching difficulty, but it always said "between 1 and 100" regardless of the selected level.
- **New Game reset broken:** I expected clicking New Game to fully reset the game (score, attempts, history, status), but it only reset attempts and generated a number from 1-100 ignoring the current difficulty. The only way to truly restart was refreshing the page.
- **Attempt counter off-by-one:** I expected the attempt count to start at 0 before any guess, but it started at 1, effectively costing the player one attempt.
- **Hints are backwards:** I expected "Too High" to say "Go LOWER" and "Too Low" to say "Go HIGHER," but the messages were swapped — guessing too high said "Go HIGHER," sending the player in the wrong direction.
- **TypeError crash on even attempts:** I expected the game to work on every guess, but on even-numbered attempts the code converted the secret number to a string, causing a TypeError crash when comparing an int guess to a string secret.
- **Score off-by-one on win:** I expected winning on attempt 1 to give 90 points, but the formula used `attempt_number + 1`, so it always gave 10 fewer points than expected.
- **Inconsistent "Too High" scoring:** I expected wrong guesses to consistently lose points, but "Too High" randomly gave +5 on even attempts and -5 on odd attempts, while "Too Low" always gave -5.
- **Secret doesn't regenerate on difficulty switch:** I expected switching difficulty to generate a new secret within the correct range, but the secret stayed the same (e.g., 98 on Easy mode with range 1-20).


---

## 2. How did you use AI as a teammate?

- I used copilot claude opus 4.6 to help me debug this game
- One example of an AI suggestion that was correct was when it helped me fix the guess a number between 1-100 issue where it was constantly displaying that regardless of the level so the fix was f"Guess a number between {low} and {high}. I verified the implementation was correct by playing the game again and changing the levels to make sure the numbers changed according to their range and displayed the correct numbers.
- One example of an AI suggestion that was misleading was when I asked it to help me with the attempts count fix, it changed the number of attempt counts for each level, but it misinterpreted what I had asked for, so I explicitly had to explain that I wanted the attempt count to start at 0 and not 1 because the original implementation is incorrect. 

---

## 3. Debugging and testing your fixes

- I decided a bug was fixed by both manually testing in the browser and running automated tests. If the game behaved as expected and all pytest tests passed, I considered the bug fixed.
- I manually tested each fix by playing the game in the browser after each change. For example, after fixing the difficulty range, I switched between Easy, Normal, and Hard and confirmed the displayed range text updated correctly. After fixing New Game, I clicked it and verified the score, attempts, and status all reset properly without needing to refresh the page.
- I also ran `py -m pytest tests/ -v` which executed 12 automated tests — all 12 passed. These tests verified that check_guess returns the correct hint direction, that difficulty ranges are correct (Hard > Normal), and that parse_guess handles valid numbers, empty strings, and non-numeric input properly.
- Yes, AI (Copilot) helped me generate 9 new pytest test cases in test_game_logic.py that specifically targeted the bugs I fixed, such as verifying that "Too High" hints contain "LOWER" and that the Hard range is larger than Normal. This saved me time writing tests from scratch and gave me confidence the fixes were correct.


---

## 4. What did you learn about Streamlit and state?

- The secret number kept changing in the original app because in the original new game button, when pressed it henerated random.randint(1,100) so regardless of the difficulty, it woud be something random within 1-100 that may or may not fall within the level range. 
- I would explain session reruns for streamlit as a web page that refreshes everytime I click anything, without session state, every variable reset to default but with st.session_state, it saves them.
- I fixed the new game button to use random.randint(low,high) instead of 1,100 and reset all session state fields. 

---

## 5. Looking ahead: your developer habits

- Playing the game first before even looking at any code help me see the bugs from user POV and I'd definitely reuse this habit for more projects going forward.
- One thing I would do differently next time when using AI is I would verify each AI suggestion more carefully before accepting it, since the AI sometimes misinterpreted what I was asking for (like the attempts fix). Next time I'd describe the exact bug and expected behavior upfront
- This project just further reinforced my belief that AI is absolutely capable and amazing building or developing apps in the right hands, meaning someone who knows how to prompt properly, specific about task, and provides as much contexts as possible. AI is not nearly as big of an issue as the prompt engineer themselves who can't properly articulate themselves.