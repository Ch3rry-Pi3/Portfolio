"""
Number Guessing Game

This is a simple Python game where the player guesses a randomly selected number
between 1 and 100. The player can choose between two difficulty levels: Easy and Hard.
"""

from random import randint
from art import logo

# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """
    Compares the user's guess to the actual answer.
    Prints feedback and reduces the number of turns if the guess is incorrect.

    Parameters:
        user_guess (int): The player's guessed number.
        actual_answer (int): The correct number to guess.
        turns (int): Remaining attempts.

    Returns:
        int: Updated number of turns remaining.
    """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    """
    Sets the game difficulty level by selecting the number of attempts.

    Returns:
        int: Number of attempts based on the chosen difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """
    Main function to play the Number Guessing Game.
    Handles the game flow, including setting the difficulty, managing guesses,
    and providing feedback.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")  # Debug message (optional)

    # Set the number of turns based on the chosen difficulty
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        
        # Check the guess and update remaining turns
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


# Start the game
game()
