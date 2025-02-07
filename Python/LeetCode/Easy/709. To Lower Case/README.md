# 🔡 **LeetCode 709: To Lower Case**

## 📌 **Overview**
This project solves **LeetCode Problem 709: To Lower Case**.  
The goal is to convert **all uppercase letters** in a string **to lowercase** without using built-in string methods like `.lower()`.

### **Problem Statement**
Given a **string** `s`, return the **same string** but with **all uppercase letters converted to lowercase**.

🔹 **Constraints:**
- `1 <= s.length <= 100`
- `s` consists of **printable ASCII characters**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "Hello"
Output: "hello"
```
#### **Explanation:**
- `'H' → 'h'`
- `'e'` remains unchanged.
- `'l'` remains unchanged.
- `'l'` remains unchanged.
- `'o'` remains unchanged.

✅ **Final Output: `"hello"`**

### **Example 2**
```python
Input: s = "here"
Output: "here"
```
#### **Explanation:**
- No uppercase letters → String remains unchanged.
✅ **Final Output: `"here"`**

### **Example 3**
```python
Input: s = "LOVELY"
Output: "lovely"
```
#### **Explanation:**
- `'L' → 'l'`
- `'O' → 'o'`
- `'V' → 'v'`
- `'E' → 'e'`
- `'L' → 'l'`
- `'Y' → 'y'`

✅ **Final Output: `"lovely"`**

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ **Every uppercase letter** (`A-Z`) has an ASCII value **32 less than its lowercase counterpart** (`a-z`).  
✔ Instead of using `.lower()`, we can manually **add `32` to each uppercase letter’s ASCII value** using `chr(ord(x) + 32)`.  
✔ Other characters (lowercase letters, numbers, special symbols) **remain unchanged**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Check if a Character is Uppercase**
- If `x` is between `'A'` (`65`) and `'Z'` (`90`), it is uppercase.

### **2️⃣ Convert Uppercase to Lowercase**
- Use `chr(ord(x) + 32)` to **shift the character to its lowercase equivalent**.

### **3️⃣ Construct the Result**
- Use **list comprehension** to apply the transformation.
- **Join the list into a string** and return the result.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'To Lower Case' problem.

    The function `toLowerCase` converts all uppercase letters in a string to lowercase 
    without using the built-in `lower()` function.
    """

    def toLowerCase(self, s: str) -> str:
        """
        Converts all uppercase letters in the given string to lowercase.

        :param s: Input string containing uppercase and lowercase letters.
        :return: Lowercase version of the input string.
        """
        is_upper = lambda x: 'A' <= x <= 'Z'        # Checks if a character is uppercase
        to_lower = lambda x: chr(ord(x) + 32)       # Converts an uppercase letter to lowercase

        # Convert uppercase letters while keeping other characters unchanged
        return ''.join([to_lower(x) if is_upper(x) else x for x in s])

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **ASCII-based (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each character is processed once**, making it **O(n)**.
- **A new string is created**, making **O(n) space complexity**.

## 🏗 **Project Structure**
```
709. To Lower Case/
├── to_lower_case.py    # Python implementation of the solution
├── README.md           # Detailed explanation & walkthrough
```

✨ **Master string manipulation with an efficient `O(n)` approach!** 🚀  