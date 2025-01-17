"""
Coffee Machine Program (OOP Version)

This program simulates a coffee vending machine using Object-Oriented Programming (OOP).
It allows users to:
- Select a drink (espresso, latte, or cappuccino).
- Check if resources are sufficient.
- Process payments.
- Serve coffee.
- View reports for machine resources and earnings.

The system is structured into four classes:
1. `MenuItem` (menu.py) – Represents an individual drink.
2. `Menu` (menu.py) – Manages the list of available drinks.
3. `CoffeeMaker` (coffee_maker.py) – Handles resource management and coffee preparation.
4. `MoneyMachine` (money_machine.py) – Processes payments and tracks profit.
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialise system components
menu = Menu()  # Manages available drinks
coffee_maker = CoffeeMaker()  # Handles machine operations
money_machine = MoneyMachine()  # Manages transactions

# Main program loop
is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        print("Shutting down the coffee machine. Have a great day! ☕️")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_choice = menu.find_drink(choice)

        if coffee_choice:
            if coffee_maker.is_resource_sufficient(coffee_choice) and money_machine.make_payment(coffee_choice.cost):
                coffee_maker.make_coffee(coffee_choice)
