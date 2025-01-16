"""
PyPassword Generator

This script generates a secure password based on user input. The user can specify
the number of letters, symbols, and numbers they want in the password. The script
provides two levels of password generation:
1. Easy Level: Sequential password generation without shuffling.
2. Hard Level: Randomly shuffled password for enhanced security.
"""

import random

# Define character pools for the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Gather user input for password composition
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# ------------------------
# Easy Level: Sequential password generation
# ------------------------
easy_password = ""

# Add random letters
for _ in range(nr_letters):
    easy_password += random.choice(letters)

# Add random symbols
for _ in range(nr_symbols):
    easy_password += random.choice(symbols)

# Add random numbers
for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

# Display the easy-level password
print(f"\nEasy Password: {easy_password}")

# ------------------------
# Hard Level: Shuffled password generation
# ------------------------
# Create a list of random characters
password_list = []

# Add random letters to the list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Display the password list before shuffling
print(f"\nPassword List (Before Shuffling): {password_list}")

# Shuffle the password list
random.shuffle(password_list)

# Display the password list after shuffling
print(f"Password List (After Shuffling): {password_list}")

# Combine the shuffled list into a final password string
hard_password = "".join(password_list)

# Display the hard-level password
print(f"\nYour Password: {hard_password}")
