# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

## Bug number 1 ##
 When I first launched the game on Normal difficulty, the Settings sidebar said "Attempts allowed: 8," but the main game panel immediately displayed "Attempts left: 7" before I had made a single guess. This is wrong because the player loses an attempt before the game even begins. I expected the game to start by showing all 8 attempts available, matching the total shown in Settings, and to only count down to "attempts left" after each guess is actually submitted.


 ## Bug number 2 ##

When playing the game, the instructions clearly state to guess a number between 1 and 100, but when I entered a negative number, the game accepted it as a valid guess and responded with the hint "Go LOWER!" — telling me to guess an even smaller number, which makes no sense since the value was already below the allowed range. This is wrong because a negative number is outside the valid range and should never be treated as a real guess or given a directional hint. I expected the game to reject any input below 1 (or above 100) and show a clear error message telling the player they are not allowed to enter a negative or out-of-range number, and to ask them to enter a number between 1 and 100 instead.


## Bug number 3 ##
 While playing, I used the Developer Debug Info to confirm the secret number was 33, then tested the hints directly. When I entered a number lower than 33, the game told me to "Go LOWER!", and when I entered a number higher than 33, it told me to " Go HIGHER!" the exact opposite of what should happen. This is wrong because the hints are inverted: a guess below the secret should tell the player to go higher, and a guess above the secret should tell them to go lower. I expected the game to point me toward the correct number, so that guessing too low says "Go HIGHER" and guessing too high says "Go LOWER," allowing the hints to actually help narrow down the secret instead of leading the player in the wrong direction.
 
## Bug Reproduction Logs ##

| Input Used      | Expected Behavior     | Actual Behavior        | Console Error / Output |
| --------------- | --------------------- | ---------------------- | ---------------------- |
| New game        | "Attempts left: 8"    | "Attempts left: 7"     | None                   |
| `-5`            | Error message shown   | Hint "Go LOWER!" shown | None                   |
| Guess below 33  | Hint "Go HIGHER"      | Hint "Go LOWER"        | None                   |
| Guess above 33  | Hint "Go LOWER"       | Hint "Go HIGHER"       | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Chatgpt and Claude both. But i used Claude more than Chatgpt. I used it like a pair-programming partner: I described the bugs I saw while playing, and i also told the AI the function that needs to be fixed. It helped trace them to the exact lines. I always checked its work myself by replaying the game and running pytest.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When the hints were backwards, I asked AI to tell me what's wrong in the function check_guess; I also gave the speific line number to ask what is wrong here. The AI said the messages in `check_guess` were swapped and fixed them so "Too High" returns "Go LOWER." I verified it by using the Debug Info to see the secret, guessing above and below it, and confirming the arrows were right — plus a pytest test that passed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For the negative-number bug, the AI added a range check that defaulted to 1–100. It looked fixed, but on Normal difficulty (1–50) I typed a number over 100 and still got "enter a number between 1 and 100." That showed the fix was incomplete, so we updated `app.py` to pass the real range. It taught me an AI fix can look done and still miss a case.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

First, I looked at the code myself to understand where the bug might be. Then I asked the AI to write a pytest test specifically targeting that bug, so I could confirm whether it was actually fixed. I ran the test in the terminal to make sure it passed, and finally I verified the fix by playing the game and checking the behavior was correct.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One of the tests I ran was for the backwards-hints bug. I wrote a pytest that checked if guessing 60 when the secret was 50 actually returned "Too High." While I was at it, running all the tests together taught me something I hadn't realized about my own code — the starter test kept failing, and when I looked closer it was because `check_guess` doesn't just return a word like "Win," it actually returns two things together: the outcome and the hint message. So my test had to pull those apart instead of comparing to a single word. Once I fixed that, everything passed, and it felt good to see the green checkmarks confirm the hints were finally pointing the right way.

- Did AI help you design or understand any tests? How?

Yes, the AI helped with the tests. I told it which bug I'd just fixed, and it wrote pytest cases targeting that exact bug — like checking that guessing 60 against a secret of 50 returns "Too High." It also helped me understand why my tests were failing at first, by explaining that `check_guess` returns two values instead of one. So it helped me both write the tests and understand what they were telling me.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit re-runs your whole script from top to bottom every time you click something, so normal variables reset each time. Session state is the one box that survives those reruns — it's where you keep things you want to remember, like the secret number, score, and attempts. Without it, the game would forget everything on every click.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I want to keep using the AI in agent mode, but with the AI showing me each edit before it changes the file directly. That way I can verify it's only changing exactly what I asked for, and if it touches anything else, I can reject it and rewrite my prompt with more detail.



- What is one thing you would do differently next time you work with AI on a coding task?

Next time I'd test the AI's fixes more carefully in edge cases and will give more clear instructions, because it removed the pre-existing pytests from the file when i asked to create new pytests for the bugs I fixed.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It taught me that AI code can look correct and still be wrong, so I can't just trust it. I need to test AI's work very carefully by covering each test that i can do manually, because sometimes a small bug is still there even if you think AI has already fixed it.
