# 🐍 **Debugging with PySnooper**

## 📌 **Overview**
[PySnooper](https://github.com/cool-RR/PySnooper) is a **lightweight debugging tool** for Python that provides detailed logging of function execution. It tracks **variable changes**, **execution flow**, and **function calls** without modifying the original code.

This guide explains how to install PySnooper and use it to debug a simple function.

## 🔧 **Installation**
To install PySnooper, use the following command:

```bash
pip install pysnooper
```

## 🚀 **Example: Debugging a Function**
The following Python script demonstrates **PySnooper in action** by debugging a function that calculates the sum and difference of two numbers.

### **Python Script: `debugging_with_pysnooper.py`**
```python
"""
debugging_with_pysnooper.py

This script demonstrates how to use PySnooper for debugging Python functions.
PySnooper logs function calls, variable changes, and execution steps.

In this example, we define a function `add_sub` that takes two numbers as input 
and returns their sum and difference. The `@pysnooper.snoop()` decorator 
is used to log all operations within the function.
"""

import pysnooper

@pysnooper.snoop()      # Enables PySnooper to log debugging details for this function
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
```

## 🖥 **PySnooper Output Example**
When running the script, PySnooper logs the **execution flow** of the function:

```
Starting var:.. a = 9
Starting var:.. b = 5
10:57:05.662179 call        16 def add_sub(a, b):
10:57:05.662179 line        28     add = a + b         # Compute the sum of a and b
New var:....... add = 14
10:57:05.662179 line        29     sub = a - b         # Compute the difference of a and b
New var:....... sub = 4
10:57:05.662179 line        31     return add, sub         # Return both results as a tuple
10:57:05.662179 return      31     return add, sub         # Return both results as a tuple
Return value:.. (14, 4)
```

## 🔥 **Why Use PySnooper?**
✅ **Automatic tracing** without modifying function logic  
✅ **Shows variable changes** step by step  
✅ **Great for debugging complex functions**  

## 🚀 **Try It Yourself!**
- Install PySnooper with `pip install pysnooper`
- Copy and run the **`debugging_with_pysnooper.py`** script
- Observe the **detailed function execution logs**

**Happy debugging!** 🛠🐍