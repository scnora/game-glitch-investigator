# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


--sarai --
When I was putting a guess, lets say 21, it told me to go higher even tho the secret is 5 

When i put in a negative number, it tells me to go lower even tho the number is positive and bigger. 
ex. secret is 7 and I guessed -10, it told me to go lower 

new game button doesnt work 

leading zeros would be considered a lower number
however if the secret is 35 and i guess 035, it counts as correct.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
--SARAI--
I used Claude Code to help me with this project

The AI suggested I changed the conditional statements for the hints that were printed after each guess which was right. The original code was printing opposite conditions. 

The AI told me that it fixed negative numbers but when I tested it again, it wasn't working like i wanted. yes it was giving the right hints but i didnt want negative numbers to be accepted because the range is from 1 to 100. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
--SARAI--
I would run an example trial and input values that I was trying to fix and take note of what was outputted each time. I would also take note of what was being added each round into the Developer Debug Info

When checking for negative numbers, I was given the secret to be 14. I inputted -24 and it outputed for me to go lower. After I saw this, I asked Claude to make sure that negative numbers are accounted for corrected. Then I realised that the range is from 1 to 100 so I told it to ignore negative numbers and the next time the secret was 40 and i inputted -40 and it came out correct. I retold Claude and inspected the fixes to make sure the code was how I intended. 


## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--SARAI--
The secret number kept changing in the original app because it was refreshing the guess each time the guess button was clicked. 

Think of it as playdough, everytime it runs, we have a target shape we want to make but are given clues about the shape each round. The problem is everytime a new round started, Streamlit "reruns" would act like a hammer and would crush the playdough and you'd start over again. 

I changed the buttons functionality and make it so that the guess button wouldn't trigger a Streamlit rerun 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
