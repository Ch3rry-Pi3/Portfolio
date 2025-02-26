# 📌 Static Arrays, Dynamic Arrays, and Strings

## 📖 Overview

This guide provides an introduction to **static arrays**, **dynamic arrays**, and **strings** in programming. It covers their fundamental operations, along with their respective time complexities in Big O notation.

- **Static Arrays**: Fixed-size collections of elements stored in contiguous memory locations.
- **Dynamic Arrays**: Resizable arrays that allow efficient insertion and deletion of elements.
- **Strings**: Immutable sequences of characters, commonly used in text processing.

## 📊 Time Complexity Table

The table below summarises the time complexities of common operations performed on arrays (both static and dynamic) and strings.

| Operation                 | Array/List | String (Immutable) |
|---------------------------|------------|-------------------|
| **Appending to end**       | O(1) (amortised) | O(n) |
| **Popping from end**       | O(1)        | O(n) |
| **Insertion, not from end** | O(n)        | O(n) |
| **Deletion, not from end**  | O(n)        | O(n) |
| **Modifying an element**    | O(1)        | ❌ (Immutable) |
| **Random access**          | O(1)        | O(1) |
| **Checking if element exists** | O(n)    | O(n) |

## 📝 Code Examples

### 📌 Dynamic Array (Python List)

```python
# Initialize a dynamic array
A = [1, 2, 3]
print("Initial List:", A)

# Append operation (O(1) on average)
A.append(5)
print("After Append:", A)

# Pop operation (O(1))
A.pop()
print("After Pop:", A)

# Insert at a specific position (O(n))
A.insert(1, 10)
print("After Insert at index 1:", A)

# Access an element (O(1))
print("Element at index 2:", A[2])

# Check if element exists (O(n))
if 10 in A:
    print("10 exists in the list")

# Get length of array (O(1))
print("Length of List:", len(A))
```

### 📌 String Operations in Python

```python
# Define a string
s = "hello"
print("Initial String:", s)

# String concatenation (O(n))
s = s + " world"
print("After Concatenation:", s)

# Checking if character exists (O(n))
if 'e' in s:
    print("Character 'e' exists in the string")

# Accessing a character by index (O(1))
print("Character at index 2:", s[2])

# Get length of string (O(1))
print("Length of String:", len(s))
```

## 🎯 Key Takeaways

✅ **Dynamic Arrays offer flexibility** compared to static arrays but come with overhead for resizing.
✅ **Strings are immutable** in many languages, requiring full reallocation for modifications.
✅ **Random access in arrays and strings** is efficient, but insertions and deletions (except at the end) can be costly.

## 📜 License

This project is open-source and available under the **MIT License**.

## 🤝 Contributions

We welcome contributions! Feel free to:

- Open issues for bug reports or feature requests 🐛  
- Submit pull requests for improvements 🔥  
- Share feedback to enhance this guide 💡  

🚀 **Happy Learning!**