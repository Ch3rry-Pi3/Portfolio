# 🪓 **Hangman Game** 🎉

## Overview  
The **Hangman Game** is a Python implementation of the classic word-guessing game. The player must guess the letters in a hidden word within a limited number of attempts. The game provides visual feedback of the hangman figure as the player loses lives, adding a fun and challenging element to the gameplay!

This project helps you:
1. 🧠 Practice Python fundamentals such as loops, conditional statements, and lists.  
2. 🎮 Build an interactive game for both fun and learning.  
3. ✨ Work with external Python files for modular coding.  

## Folder Structure  

Ensure the following files are in the same directory to run the game successfully:  

```
hangman/
├── main.py            # The main game logic
├── hangman_art.py     # ASCII art for the hangman stages and logo
├── hangman_words.py   # A list of words for the game
```

## How to Play  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the game with the following command:  
   ```bash
   python main.py
   ```
4. Follow the on-screen instructions to guess the word. You’ll need to:  
   - Enter one letter at a time.  
   - Avoid repeating incorrect guesses.  

5. The game ends when you either:  
   - 🎉 Successfully guess the word (You win!).  
   - 💀 Run out of lives (You lose!).  

## Key Features  

1. **🖼️ Visual Feedback**:  
   - ASCII art displays the hangman’s progression as you lose lives.  

2. **📜 Extensive Word List**:  
   - Includes a diverse set of challenging words for endless fun.  

3. **🔀 Random Word Selection**:  
   - Each game starts with a randomly chosen word.  

4. **🛠️ Modular Design**:  
   - Organized code across multiple Python files for better readability and maintainability.  

5. **⚡ Replayability**:  
   - Play as many rounds as you want with new words each time!  

## Example Gameplay  

### Game Start:  
```plaintext
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
Word to guess: _______
************************ 6/6 LIVES LEFT ************************
Guess a letter:
```

### Incorrect Guess:  
```plaintext
You guessed 'x', that's not in the word. You lose a life.
************************ 5/6 LIVES LEFT ************************
  +---+
  |   |
  O   |
      |
      |
      |
=========
Word to guess: _______
```

### Win Example:  
```plaintext
Word to guess: python
************************ YOU WIN ************************
```

### Lose Example:  
```plaintext
You guessed 'z', that's not in the word. You lose a life.
******************** IT WAS python! YOU LOSE ********************
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## File Details  

### `main.py`  
This file contains the main game logic. It handles:  
- Word selection from `hangman_words.py`.  
- Player input and validation.  
- Lives tracking and win/lose conditions.  
- Visual feedback using ASCII art from `hangman_art.py`.  

### `hangman_art.py`  
This file contains:  
- **`stages`**: ASCII art for the hangman figure, which updates as lives are lost.  
- **`logo`**: A creative logo displayed at the start of the game.  

### `hangman_words.py`  
This file contains:  
- **`word_list`**: A diverse and challenging set of words for the game.  

## Additional Notes  

- 🛠️ Customize the word list in `hangman_words.py` to add or remove words.  
- 🎨 Modify the ASCII art in `hangman_art.py` to personalize the game visuals.  
- 🧠 A great project to practice modular programming and improve problem-solving skills!  

**🎉 Have fun playing Hangman, and may the odds be in your favor!** 💀📖🎮  