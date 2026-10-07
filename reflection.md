# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
/**
When I first ran app.py, the app rendered without crashing, but playing the game immediately revealed broken mechanics. The most confusing issue was that the hints were inverted: guessing higher than the target prompted me to guess higher rather than lower. Furthermore, the difficulty selectors did not enforce the intended boundaries for Normal (1–50) and Hard (1–100), and the guess box accepted negative numbers without warning. Finally, submitting the exact correct number still penalized my score, meaning a player lost points even when winning.
**/

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|          Input         |      Expected Behavior       |              Actual Behavior              | Console Output / Error|
|------------------------|------------------------------|-------------------------------------------|-----------------------|
| Guess: 20 (Secret: 19) | Go LOWER! should be hint     | Go HIGHER! shown hint                     |          None         |
| Difficulty: Normal     | Range: 1 to 50               | Range: 1 to 100                           |          None         |
| Guess: 25 (Secret: 25) | Victory detected and         | Victory detected, but score decremented   |          None         |
                           score preserved                due to unconditional penalty                                  
| Guess: -5              | expected out-of-bounds error | Negative number was accepted as a valid |                         |
                          and attemt should be preserved| guess and deducted an attempt.                     
                          



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI correctly identified that the comparison operators (> vs <) were swapped inside check_guess()
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

One suggestion I did not accept as written was in check_guess: the AI suggested adding g = int(guess) to convert the guess before comparing it to the secret. I rejected this because input validation is already the job of parse_guess, which checks that the raw input is a number and returns it as an int before check_guess is ever called I verified it by runnning streamlit run app.py and testing manually.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was truly resolved only after confirming both the isolated logic in unit tests and the live behavior across edge cases in the browser using streamlit run app.py.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Whenever a user interacts with any widget in Streamlit—such as clicking a button or changing an input—Streamlit reruns the entire Python script from line 1 to the end. Because the script executes fresh on each interaction, standard local variables reset to their default values and lose their data instantly. st.session_state acts as a persistent memory dictionary that survives these continuous reruns. Without storing the secret number, guess count, and score in st.session_state, the game would forget the player's progress the moment they clicked submit.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
In future projects, I want to keep the habit of isolating core game and business logic into separate helper functions before touching the UI layer. Next time I work with an AI assistant, I will provide stricter constraints and function signatures upfront so it does not propose bloated or over-engineered solutions. Working through these glitches reinforced that AI is excellent at spotting inverted comparisons, but the developer must remain the architect who decides whether a fix cleanly fits the codebase.

- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI-generated code frequently appears clean and functional while hiding subtle logical flaws, like overenginnnering of checking input and convering to string or unhandled edge cases. I now treat AI renerated code as an unverified initial draft that demands strict human review and boundary testing rather than a ready-to-merge solution.

