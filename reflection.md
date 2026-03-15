# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The game when I started this had a bunch of bugs and logic errors that did not work. The correct number was constantly reset after every click, the hints were always telling the user to guess higher, the new game button did not work even though the app would direct the user to retry with a new game. These bugs all came together and made it a sloppy app alltogether 

---

## 2. How did you use AI as a teammate?
The Ai tools i used on this project were both copilor and Claude and i prompted it to help me figure out many aspects of this project that i sadly struggled with from opening the file to code fixes. The ai suggestions i used were correct but because at the start i tried to stray away from using AI too much i sometimes ignored its suggestions only to later come back to it and use it. When i found out the logic error that was affecting the correct answer being constantly affected claude suggested that i had to set a spesific function to stop the issue. Intrestingly enough the fix it had suggested had already been implemented but this led to it finding bugs in another area of the code that it suggested fixing which was changing the conversion of the correct number into a string and making that an integer. This one example while it dosent really show how ai was incorrect or misleading shows how ai had intresting ideas and implementations with the code it produced. 


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For debugging i tested the app myself by playing the game and identifying the changes that were made and if the features i wanted were really implemented. One that i ran was when i wanted to fix the new game and after i commited a code that claude had wrote i tested it by running the app and playing once and then clicking the button again 

## 4. What did you learn about Streamlit and state?

Streamlits session state essentially makes sure that an variable stored in the app dosent get refreshed when a button or feature is clicked in the app. Streamilit automatically refreshes everything from top to bottom when something is changed so session state stops that. Reruns on the other hand makes only that varaible that is stored refreshed when that spesific feature is interacted with. 


## 5. Looking ahead: your developer habits
one habit that i want to learn is definatly to searh things up that i dont know and put more effort into learning things. Because here this was the first time i had ever even touched git and i spent a while just learning how to even do commits and i still got more of git to learn. One thing i want to do differently next time is start trusting AI more that would have saved me a lot of time .Thi project made me more open minded about using AI in my code.