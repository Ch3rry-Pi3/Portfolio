# 🃏 **Blackjack Game** ♣️♥️

## Overview  
The **Blackjack Game** is a Python implementation of the classic card game. In this game, you compete against the computer to get a hand value as close to **21** as possible without exceeding it. The program handles the card dealing, score calculation, and game logic, creating a fun and interactive experience! 🎉  

This project helps you:  
1. 🧠 Practice Python programming with loops, conditionals, and functions.  
2. 🃏 Build a dynamic card game with simple yet engaging logic.  
3. ✨ Enhance problem-solving skills while creating a fun project.  

## How It Works  

1. **The Goal**:  
   - Get as close to **21** as possible without going over.  
   - A score of exactly **21** with the first two cards is a **Blackjack**.  

2. **Game Rules**:  
   - Cards are worth their face value, face cards are worth **10**, and Aces are worth **1** or **11**, depending on the hand value.  
   - The computer must draw cards until its total is at least **17**.  

3. **Win/Lose Conditions**:  
   - If your total exceeds **21**, you lose.  
   - If the computer’s total exceeds **21**, you win.  
   - The highest total under **21** wins.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python blackjack.py
   ```  

## Example Gameplay  

### Start of the Game:  
```plaintext
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/                 

Do you want to play a game of Blackjack? Type 'y' or 'n': y
```

### User's Turn:  
```plaintext
Your cards: [10, 7], current score: 17
Computer's first card: 6
Type 'y' to get another card, type 'n' to pass: n
```

### Computer's Turn and Final Results:  
```plaintext
Your final hand: [10, 7], final score: 17
Computer's final hand: [6, 9, 5], final score: 20
You lose 😤
```

## Key Features  

1. **♠️ Card Dealing**:  
   - Randomly deals cards from a simulated deck.  

2. **📊 Score Calculation**:  
   - Calculates scores dynamically, including handling Aces as **1** or **11**.  

3. **🎮 Game Logic**:  
   - User can draw cards or pass.  
   - Computer follows rules to draw cards until it reaches a total of at least **17**.  

4. **✨ Interactive Gameplay**:  
   - Provides real-time updates on card hands and scores.  
   - Displays results with fun emojis and messages!  

## File Details  

### `blackjack.py`  
The main program file that:  
- Handles user and computer turns.  
- Calculates scores and determines the winner.  

### `art.py`  
Contains the ASCII art logo for the game, displayed at startup. 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
blackjack/
├── blackjack.py    # The main program logic
├── art.py          # Contains the ASCII art logo
```

## Additional Notes  

- 🃏 Modify the deck in `deal_card()` to include more cards or customise the game.  
- 🛠️ Experiment with new rules or add features like betting for more complexity.  
- 🎉 A fun project to practice Python programming while building a classic game!  

**✨ Have fun playing Blackjack, and may the best hand win!** 🃏🎉♠️♥️  