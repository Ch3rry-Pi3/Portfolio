"""
Calculator Application

This program provides a simple calculator that can perform basic operations:
addition, subtraction, multiplication, and division. Users can continue 
calculating with the result or start a new calculation.
"""

import art


# Define basic arithmetic operations
def add(n1, n2):
    """Returns the sum of n1 and n2."""
    return n1 + n2


def subtract(n1, n2):
    """Returns the difference when n2 is subtracted from n1."""
    return n1 - n2


def multiply(n1, n2):
    """Returns the product of n1 and n2."""
    return n1 * n2


def divide(n1, n2):
    """Returns the quotient when n1 is divided by n2."""
    return n1 / n2


# Dictionary to map operators to their respective functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """
    Main calculator function. Allows users to:
    - Perform a calculation.
    - Continue calculating with the current result.
    - Start a new calculation.
    """
    print(art.logo)

    # Begin calculation with the first number
    num1 = float(input("What is the first number?: "))
    should_accumulate = True

    while should_accumulate:
        # Display available operations
        for symbol in operations:
            print(symbol)

        # Get the operation and the next number
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        # Perform the calculation
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue or start a new calculation
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)  # Simulate clearing the screen
            calculator()  # Restart the calculator


# Run the calculator
calculator()
