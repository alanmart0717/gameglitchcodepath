# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game was inconsistent, the out of attempts message would appear when I had one attempt left. However, it still allowed me to submit my last attempt, but regardless it was misleading. Additionally, I noticed that the ranges in correspondance to each game mode were not accurate. Also, the secret number was way below or above the ranges indicated for easy, normal, and hard.

---

## 2. How did you use AI as a teammate?

1) I used Claude
2) Claude suggested that the mismatched ranges was due to the fact that it explicitly stated "pick a number between 1 and 100". Given this feedback I manually changed the it to retrieve the low and high values for the corresponding game mode. 
3) Claude suggeseted that my Attempts left counter had to do with the fact that the state attempt was initialized at 1. However, changing it did not reflect the correct output. With some more context rich prompts, I checked the submit if statement, asked it to describe the logic to me. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would often use py.test or retest the game myself
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the switching of game modes to ensure the ranges and secret number were updating in real time. I was able to identify which specific functions or lines the code might be faulty, narrowing my search for the error. 
- Did AI help you design or understand any tests? How?
  Yes, when it came to figuring out how to accurately represent the attempts left, Claude suggested a change, but I only ever implemented it after i understood what was wrong. Additionally, if I did allow it to change on its own, I often reverted back changes if other sections of code were being edited. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- Answer: Streamlit reruns are like while loops, iterating again and again upon each user interaction. Session state are handy dandy counters, and allow you to save variables upon reruns. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - Answer: continuing to use context rich prompts, and being as specific as possible. 
- What is one thing you would do differently next time you work with AI on a coding task?
- Answer: Not jumping the gun on a specific change and being more thorough with what Im asking it to do
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- Answer: Claude is very effective, however often makes errors without the proper guidance. I learned that its always better to check code intention yourself, and utilizing AI to guide you to solving a specific issue given the proper context, rather than just saying "fix it"
