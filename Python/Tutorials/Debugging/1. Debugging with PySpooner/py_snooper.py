"""
Debugging with PySpooner

This script demonstrates how to use PySnooper for debugging Python functions. 
PySnooper is a lightweight debugging tool that logs function calls, variable changes, 
and execution steps, making it easier to trace code execution.

In this example, we define a function `add_sub` that takes two numbers as input 
and returns their sum and difference. The `@pysnooper.snoop()` decorator is 
used to log all operations within the function.
"""

import pysnooper

@pysnooper.snoop()          # Enables PySnooper to log debugging details for this function
def add_sub(a, b):
    """
    Computes the sum and difference of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        tuple: A tuple containing the sum and the difference of the two numbers.
    """

    add = a + b         # Compute the sum of a and b
    sub = a - b         # Compute the difference of a and b

    return add, sub         # Return both results as a tuple

# Call the function with example inputs
add_sub(9, 5)
