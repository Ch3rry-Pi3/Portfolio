# 🎉 **LeetCode 1415: The k-th Lexicographical Happy String of Length n**  

## 📌 **Problem Overview**  
A **happy string** is defined as:  
- A string consisting **only** of the characters **'a', 'b', and 'c'**.  
- No **two adjacent characters** are the same.  

Given two integers `n` and `k`, the task is to generate all **happy strings** of length `n` in **lexicographical order**, then return the **k-th** string.  
If `k` is **larger** than the number of happy strings possible, return an **empty string** (`""`).  

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: n = 1, k = 3  
Output: "c"  
```
✅ The **happy strings** of length `1` are:  
- `["a", "b", "c"]`  
- The **3rd** string is `"c"`.

### **Example 2**  
```python
Input: n = 1, k = 4  
Output: ""  
```
✅ There are only **3** happy strings of length `1`, so there **is no** 4th string.  
Hence, the function returns **""**.

### **Example 3**  
```python
Input: n = 3, k = 9  
Output: "cab"  
```
✅ The **happy strings** of length `3` in lexicographical order:  
```python
["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]
```
The **9th** string is `"cab"`.

## 🚀 **Approach Explanation**  

### **1️⃣ Observing the Pattern**  
For a given `n`, the total number of happy strings is:  

\[
3 \times 2^{(n-1)}
\]

- Each string starts with `'a'`, `'b'`, or `'c'`.
- Each subsequent character **alternates** to avoid consecutive duplicates.

### **2️⃣ Efficiently Finding the k-th Happy String**  
Instead of **generating all** happy strings, we can **construct the k-th one directly**:  
- The **first character** is determined based on `k` and **divides the range** into three parts.  
- The remaining characters are chosen **bitwise**, ensuring valid alternation.

## 📝 **Python Solution**  
```python
from typing import List

class Solution:
    """
    This class provides an optimised solution for generating the k-th lexicographical
    happy string of length n.
    """

    def getHappyString(self, n: int, k: int) -> str:
        """
        Returns the k-th lexicographically smallest happy string of length n.
        
        :param n: Length of the happy string.
        :param k: The k-th string to return in lexicographical order.
        :return: The k-th happy string, or an empty string if k is too large.
        """

        # Calculate total possible happy strings of length n
        total = 3 * (1 << (n - 1))

        # If k exceeds total number of happy strings, return an empty string
        if k > total:
            return ""

        # Initialise result list with 'a' characters
        result = ["a"] * n

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        # Determine starting indices for strings beginning with 'a', 'b', and 'c'
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        # Assign the first character based on k's position
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        # Generate the rest of the happy string
        for char_index in range(1, n):
            midpoint = 1 << (n - char_index - 1)

            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Bitwise Calculation** | Determining the first character | **O(1)** |
| **String Construction** | Iterating over `n` to determine characters | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Avoids generating all happy strings** → saves **time & space**.  
✔ **Uses bitwise operations** for efficient **partitioning**.  
✔ **Lexicographically smallest string** is built directly.  

## 📂 **Project Structure**  
```
happy_strings/
├── happy_strings.py  # Python solution
├── README.md         # Explanation & approach
```

✨ **Master lexicographical ordering with this bitwise optimised approach!** 🚀