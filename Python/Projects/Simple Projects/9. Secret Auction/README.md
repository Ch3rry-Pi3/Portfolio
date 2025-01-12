# 🔒 **Secret Auction Program** 💰  

## Overview  
The **Secret Auction Program** is a Python-based application that allows multiple users to place secret bids for an auction. Once all participants have submitted their bids, the program reveals the highest bidder and their bid amount. This program is perfect for managing friendly auctions or competitions where secrecy is key! 🕵️‍♂️✨  

This project helps you:  
1. 🧠 Practice Python fundamentals, including dictionaries and loops.  
2. ✨ Build an interactive and practical application.  
3. 🔒 Add a fun layer of secrecy to auctions.  

## How It Works  

1. **Collect Bids**:  
   - Each user enters their name and bid amount.  
   - The bids are stored securely in a dictionary.  

2. **Continue or Stop**:  
   - After each bid, the program asks if there are additional participants.  
   - If yes, the screen is "cleared" to keep bids secret.  
   - If no, the program announces the winner.  

3. **Determine the Winner**:  
   - The program evaluates all bids to find the highest one.  
   - The winner’s name and bid amount are displayed.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python main.py
   ```

## Example Gameplay  

### Program Start:  
```plaintext
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type 'yes' or 'no'.
yes
```

### Another Bidder:  
```plaintext
What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Bob with a bid of $200
```

## Key Features  

1. **💵 Secret Bidding**:  
   - Keeps all bids hidden until the end of the auction.  

2. **📊 Dynamic Winner Calculation**:  
   - Automatically determines the highest bid and winner.  

3. **🛠️ Modular Design**:  
   - Uses a separate function (`find_highest_bidder()`) for better readability and reusability.  

4. **🔄 Repeatability**:  
   - Allows multiple bidders to participate until everyone has placed their bids.  

5. **✨ Clean and Interactive**:  
   - Simulates a "screen clear" for added secrecy.  

## File Details  

### `main.py`  
The core program that:  
- Collects bids.  
- Stores bids in a dictionary.  
- Evaluates and announces the winner.  

### `art.py`  
Contains the ASCII art logo for the program, displayed at startup. 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
secret_auction/
├── secret_auction.py    # The main program logic
├── art.py               # Contains the ASCII art logo
```

## Additional Notes  

- 🛠️ Customise the ASCII art in `art.py` to add your own logo or flair.  
- 💡 Expand the program by adding features like minimum bid increments or bid validation.  
- 🎉 A great project for beginners to practice Python skills and create a fun, interactive tool!  

**🎉 Let the bidding begin! May the highest bidder win!** 💰✨🔒  