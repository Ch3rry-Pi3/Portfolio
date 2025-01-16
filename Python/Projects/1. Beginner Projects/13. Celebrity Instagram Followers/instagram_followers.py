"""
Celebrity Instagram Followers

This game compares the Instagram followers of two accounts. 
The player guesses which account has more followers and tries to achieve the highest score possible.
"""

# Imports
import random
from art import logo, vs
from game_data import data


def format_data(account):
    """
    Formats the account data into a printable string.

    Parameters:
        account (dict): A dictionary containing account details (name, description, country).

    Returns:
        str: Formatted string describing the account.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """
    Checks if the user's guess is correct.

    Parameters:
        user_guess (str): The user's guess ('a' or 'b').
        a_followers (int): Follower count of account A.
        b_followers (int): Follower count of account B.

    Returns:
        bool: True if the user's guess is correct, False otherwise.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Main game logic
def play_game():
    """
    Runs the Higher or Lower game. Handles game flow, including:
    - Generating accounts to compare.
    - Taking user input.
    - Keeping track of the score.
    - Ending the game when the user guesses incorrectly.
    """
    print(logo)
    score = 0
    game_should_continue = True

    # Generate the first account for comparison
    account_b = random.choice(data)

    while game_should_continue:
        # Set account A to the previous account B and generate a new account B
        account_a = account_b
        account_b = random.choice(data)

        # Ensure the accounts are not the same
        while account_a == account_b:
            account_b = random.choice(data)

        # Display the accounts to the player
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get the user's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen
        print("\n" * 20)
        print(logo)

        # Get the follower counts for each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if the user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Provide feedback and update the score
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False


# Start the game
if __name__ == "__main__":
    play_game()
