"""
Tip Calculator

This script calculates the amount each person should pay when splitting a bill, 
including a chosen percentage tip. It ensures a user-friendly experience 
and rounds the final amount to the nearest dollar.
"""

# Welcome message
print("Welcome to the Tip Calculator!")

# Prompt the user for the total bill amount
bill = float(input("What was the total bill? $"))

# Prompt the user for the desired tip percentage
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15% "))

# Prompt the user for the number of people splitting the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip as a percentage
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill amount including the tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill / people

# Round the final amount to the nearest dollar
final_amount = round(bill_per_person)

# Display the final amount each person should pay
print(f"Each person should pay: ${final_amount}")
