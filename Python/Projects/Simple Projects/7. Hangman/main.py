"""
Hangman Game

This is a Python implementation of the classic Hangman game.
Players must guess letters to uncover the hidden word before running out of lives.
"""

import random
from hangman_words import word_list
from hangman_art import stages, logo

# Initialise lives and print the game logo
lives = 6
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
# Uncomment the next line to display the chosen word for testing/debugging purposes
# print(f"Chosen word: {chosen_word}")

# Create a placeholder for the word to guess
word_length = len(chosen_word)
placeholder = "_" * word_length
print("Word to guess: " + placeholder)

# Initialise game variables
game_over = False
correct_letters = []

# Main game loop
while not game_over:
    print(f"\n************************ {lives}/6 LIVES LEFT ************************")
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    # Update the display with the guessed letter
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"******************** IT WAS {chosen_word}! YOU LOSE ********************")

    # Check for a win condition
    if "_" not in display:
        game_over = True
        print("************************ YOU WIN ************************")

    # Display the hangman stage
    print(stages[lives])
