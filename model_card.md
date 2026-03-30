# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0** 

Mood Matcher

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is meant to find and suggest songs similar to a users taste, anything they would probably like.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system first creates a user profile based on a user's likes and dislikes. From the data set of songs, it gives each song a score based on the user's profile, and compiles them in a list sorted by that score. The top songs in that list are then recommended to the user.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

We're using a fairly small dataset with 21 songs, however there's a wide variety in all categories listed.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works very well at finding songs that are extremely close to the vibe of the user profile, including artists, genre, and mood.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The scoring system heavily favors songs with exact matches for the genre, mood, and artists to the user profiles. This happens because these categories are the most valuable in the scoring system, and also look for exact matches rather than similar matches. If a user's profile is limited, then many of the suggestions will be repeated and all have the same genres/moods instead of including a true variety that the user might like. 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The only surprising results were from the third profile that liked every genre and mood. This edge case profile shows how the system can be tricked if the user either likes or dislikes everything, giving every song a super high/low score that isn't accurate to the recommendation. In reality, this profile would technically be accurate if someone really did like/dislike everything.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
