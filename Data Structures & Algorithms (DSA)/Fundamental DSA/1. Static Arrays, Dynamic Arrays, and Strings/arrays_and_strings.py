"""
1. Static Arrays, Dynamic Arrays, and Strings

This script demonstrates fundamental operations on Python lists (dynamic arrays) 
and strings, along with their time complexity in Big O notation.

Operations Covered:
- List operations: append, pop, insert, modify, access, check existence, and length retrieval.
- String operations: concatenation, checking existence, accessing positions, and length retrieval.

Time Complexity Notation:
- O(1) - Constant time
- O(n) - Linear time
"""

# Initialise a dynamic array
A = [1, 2, 3]
print("Initial List:", A)

# Append - Insert element at end of array - Average: O(1)
A.append(5)
print("\nAfter Append:", A)

# Pop - Deleting element at end of array - O(1)
A.pop()
print("\nAfter Pop:", A)

# Insert (not at end of array) - O(n)
A.insert(2, 5)
print("\nAfter Insert at index 2:", A)

# Modify an element - O(1)
A[0] = 7
print("\nAfter Modifying first element:", A)

# Accessing element given index i - O(1)
print("\nElement at index 2:", A[2])

# Checking if array has an element - O(n)
if 7 in A:
    print("\nElement 7 exists in list")

# Checking length - O(1)
print("\nLength of List:", len(A))

# String Operations
s = 'hello'
print("\nInitial String:", s)

# Append to end of string (concatenation) - O(n)
b = s + 'z'
print("\nAfter Concatenation:", b)

# Check if something is in string - O(n)
if 'f' in s:
    print("\nCharacter 'f' exists in string")

# Access positions - O(1)
print("\nCharacter at index 2:", s[2])

# Check length of string - O(1)
print("\nLength of String:", len(s))
