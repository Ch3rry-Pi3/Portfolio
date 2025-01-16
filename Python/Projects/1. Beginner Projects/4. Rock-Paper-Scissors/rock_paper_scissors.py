"""
Rock, Paper, Scissors Game

This is a simple text-based game where the player competes against the computer
by choosing Rock, Paper, or Scissors. The winner is determined based on the 
classic rules of the game:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
"""

import random

# ASCII art for the game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List to store game images for easy access
game_images = [rock, paper, scissors]

# Get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Check if the user's choice is valid
if user_choice >= 0 and user_choice <= 2:
    # Display the user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Generate the computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the game outcome
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
else:
    # Handle invalid input
    print("You typed an invalid number. You lose!")
