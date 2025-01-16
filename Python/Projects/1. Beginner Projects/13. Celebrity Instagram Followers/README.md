# 📸 **Celebrity Instagram Followers** 🎉  

## Overview  
The **Celebrity Instagram Followers** game is a fun Python challenge where players guess which celebrity or entity has more Instagram followers. Compete against yourself to get the highest score possible by correctly identifying the more-followed account! 🌟  

This project helps you:  
1. 🧠 Practice Python programming with functions, loops, and conditionals.  
2. 🎮 Build a fun, interactive game based on real-world data.  
3. ✨ Improve problem-solving skills while enjoying a social media-inspired game.  

## How It Works  

1. **The Goal**:  
   - Compare two celebrities/entities and guess who has more Instagram followers.  

2. **Game Rules**:  
   - You will be shown two accounts: `A` and `B`.  
   - Use the information provided (name, description, and country) to guess which account has more followers.  

3. **Win/Lose Conditions**:  
   - Earn a point for each correct guess.  
   - The game continues until you make an incorrect guess.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python instagram_followers.py
   ```  

## Example Gameplay  

### Game Start:  
```plaintext
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Ariana Grande, a Musician and actress, from United States.
Who has more followers? Type 'A' or 'B': a
```

### Correct Guess:  
```plaintext
You're right! Current score: 1

Compare A: Ariana Grande, a Musician and actress, from United States.
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Kylie Jenner, a Reality TV personality and businesswoman and Self-Made Billionaire, from United States.
Who has more followers? Type 'A' or 'B': b
```

### Incorrect Guess:  
```plaintext
Sorry, that's wrong. Final score: 2.
```

## Key Features  

1. **📊 Real-World Data**:  
   - Includes actual Instagram follower counts for celebrities, athletes, musicians, and more.  

2. **🔄 Replayable Gameplay**:  
   - Test your knowledge and aim for a higher score in every round.  

3. **🎨 Visual Design**:  
   - Displays a logo and clear comparison between the two accounts for a polished experience.  

4. **✨ Feedback System**:  
   - Provides immediate feedback on your guesses and keeps track of your score.  

## File Details  

### `instagram_followers.py`  
The main program file that:  
- Randomly selects accounts for comparison.  
- Handles user input, score tracking, and game logic.  

### `game_data.py`  
Contains a list of dictionaries with real-world data about celebrity Instagram accounts:  
- **`name`**: The celebrity or entity's name.  
- **`follower_count`**: Their Instagram follower count (in millions).  
- **`description`**: A brief description of their profession.  
- **`country`**: Their country of origin.  

### `art.py`  
Contains ASCII art for the game logo and visual separator (`vs`). 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
celebrity_instagram_followers/
├── instagram_followers.py   # Main program logic
├── game_data.py             # Contains account data
├── art.py                   # Contains ASCII art for the logo and separator
```

## Additional Notes  

- 🛠️ Expand the game by adding more data entries to `game_data.py`.  
- 🎉 Challenge your friends to see who can get the highest score!  
- ✨ A great project to practice Python fundamentals while building something fun and creative.  

**🌟 Have fun playing Celebrity Instagram Followers, and may the best guesser win!** 📸🎯🎉  