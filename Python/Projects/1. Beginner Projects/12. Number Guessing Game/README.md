# 🔢 **Number Guessing Game** 🎯

## Overview  
The **Number Guessing Game** is a fun Python game where players try to guess a randomly chosen number between **1 and 100**. Players can select a difficulty level to adjust the number of attempts. The game provides helpful feedback ("Too high" or "Too low") to guide players to the correct answer. Can you guess the number before running out of attempts? 🤔  

This project helps you:
1. 🧠 Practice Python programming concepts like loops, functions, and conditionals.  
2. 🎮 Build an interactive and enjoyable game.  
3. ✨ Enhance problem-solving skills while having fun!  

## How It Works  

1. **The Goal**:  
   - Guess the random number between **1 and 100**.  

2. **Game Rules**:  
   - Choose between two difficulty levels:  
     - **Easy**: 10 attempts.  
     - **Hard**: 5 attempts.  
   - Use the feedback provided ("Too high" or "Too low") to refine your guesses.  

3. **Win/Lose Conditions**:  
   - Win by guessing the correct number.  
   - Lose if you run out of attempts.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python guessing_game.py
   ```  

## Example Gameplay  

### Start of the Game:  
```plaintext
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is 42
```

### User Guesses:  
```plaintext
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.

You have 9 attempts remaining to guess the number.
Make a guess: 30
Too low.
Guess again.

You have 8 attempts remaining to guess the number.
Make a guess: 42
You got it! The answer was 42
```

### Running Out of Guesses:  
```plaintext
You have 1 attempt remaining to guess the number.
Make a guess: 70
Too high.
You've run out of guesses, you lose.
```

## Key Features  

1. **🎯 Randomised Number**:  
   - Generates a random number between **1 and 100** for every new game.  

2. **📊 Difficulty Levels**:  
   - Choose between **Easy** (10 attempts) or **Hard** (5 attempts).  

3. **✨ User Feedback**:  
   - Provides hints ("Too high" or "Too low") to guide players.  

4. **🔄 Replayability**:  
   - Start a new game immediately after finishing one.  

## File Details  

### `guessing_game.py`  
The main program file that:  
- Handles the game flow, including difficulty selection, guessing logic, and feedback.  
- Tracks and updates the number of remaining attempts.  

### `art.py`  
Contains the ASCII art logo displayed at the start of the game. 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
number_guessing_game/
├── guessing_game.py    # The main program logic
├── art.py              # Contains the ASCII art logo
```

## Additional Notes  

- 🛠️ Customise the range of numbers in the `randint()` function for a different challenge.  
- 🎉 A great project to practice Python basics and build a fun, interactive game!  

**🎯 Good luck guessing the number, and may the odds be in your favor!** 🔢✨🎉  