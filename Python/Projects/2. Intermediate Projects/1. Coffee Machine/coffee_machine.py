"""
Coffee Machine Program

This program simulates a simple coffee vending machine. It allows users to:
- Select a drink (espresso, latte, or cappuccino).
- Insert coins to pay for the drink.
- Receive change if necessary.
- Track resource levels and generate reports.
- Turn off the machine when needed.
"""

# Coffee Menu and Machine Resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Global Variables for Profit and Available Resources
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """
    Checks if there are enough ingredients to make the selected drink.

    Parameters:
        order_ingredients (dict): The ingredients required for the drink.

    Returns:
        bool: True if there are sufficient resources, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Processes the coins inserted by the user and calculates the total amount.

    Returns:
        float: The total amount of money inserted.
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Checks if the transaction is successful by comparing inserted money with drink cost.

    Parameters:
        money_received (float): The amount of money inserted.
        drink_cost (float): The cost of the selected drink.

    Returns:
        bool: True if payment is successful, False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Prepares the selected coffee by deducting the required ingredients from resources.

    Parameters:
        drink_name (str): The name of the selected drink.
        order_ingredients (dict): The required ingredients for the drink.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Main Coffee Machine Loop
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please choose a valid drink.")
