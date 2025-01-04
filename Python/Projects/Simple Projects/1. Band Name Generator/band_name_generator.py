"""
Band Name Generator

This script generates a potential band name based on user input.
The user is prompted to enter the city they grew up in and the name of a pet.
The program then combines these inputs to suggest a band name.
"""

# Welcome message
print("Welcome to the Band Name Generator!")

# Prompt the user for the city they grew up in
city = input("Which city did you grow up in? ")

# Prompt the user for the name of a pet
pet = input("What is the name of a pet? ")

# Generate and display the band name
band_name = city + " " + pet
print("Your band name could be: " + band_name)
