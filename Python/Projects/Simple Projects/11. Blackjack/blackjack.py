"""
Blackjack Game

This program simulates a simple game of Blackjack between the user and the computer.
Players draw cards to get as close to a score of 21 as possible without going over.
The program handles card dealing, score calculation, and game logic.
"""

import random
from art import logo


def deal_card():
    """
    Returns a random card from the deck.
    Cards include numbers 2-10, face cards (represented as 10), and Aces (represented as 11).
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Calculates the score of a given hand of cards.
    - Aces (11) are converted to 1 if the score exceeds 21.
    - A score of 21 with 2 cards is considered a Blackjack (score = 0).
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """
    Compares the user's score (u_score) with the computer's score (c_score).
    Returns the result as a string.
    """
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    Main function to play a game of Blackjack.
    Handles the game flow, including user and computer turns, score calculations, 
    and determining the winner.
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to both the user and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    # Final scores and results
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)  # Simulate clearing the screen
    play_game()
