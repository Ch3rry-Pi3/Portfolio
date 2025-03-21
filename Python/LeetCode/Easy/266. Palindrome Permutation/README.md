# 📝 **LeetCode 266: Palindrome Permutation**  

## 📌 **Problem Overview**  

Given a string **s**, return `True` if a **permutation** of the string could form a **palindrome**, otherwise return `False`.  

A **palindrome** is a string that reads the same **forward** and **backward**.  

## ✅ **Example 1**  

```python
Input: s = "code"
Output: False
```

### **Explanation:**  
- The characters cannot be rearranged to form a palindrome.  
- Example permutations: `"cdeo"`, `"ecod"`, `"doce"` (none are palindromes).  

## ✅ **Example 2**  

```python
Input: s = "aab"
Output: True
```

### **Explanation:**  
- The string can be rearranged as `"aba"`, which is a **palindrome**.  

## ✅ **Example 3**  

```python
Input: s = "carerac"
Output: True
```

### **Explanation:**  
- The string can be rearranged as `"racecar"`, which is a **palindrome**.  

## 🛠 **Approach & Intuition**  

### 🔹 **Character Frequency Counting**  
1. **Count occurrences** of each character in the string.  
2. **A string can be rearranged into a palindrome if:**  
   - At most **one** character has an **odd frequency**.  
   - All other characters must appear an **even number** of times.  
3. **Return `True`** if the odd character count is **≤ 1**, otherwise return `False`.  

📌 **Why does this work?**  
- A palindrome with an **even length** must have all characters appearing an **even** number of times.  
- A palindrome with an **odd length** can have **one character** with an **odd** frequency (it will be the middle character).  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Determines whether any permutation of the given string can form a palindrome.

        :param s: The input string consisting of lowercase English letters.
        :return: True if a permutation of the string can form a palindrome, otherwise False.
        """
        char_count = [0] * 128  # ASCII table size to track character frequencies
        
        # Count occurrences of each character
        for ch in s:
            char_count[ord(ch)] += 1
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in char_count if count % 2 == 1)
        
        # A palindrome can have at most one character with an odd frequency
        return odd_count <= 1

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Character Frequency Counting** | **O(n)** ✅ |
| **Odd Count Calculation** | **O(1)** ✅ |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The **frequency array** ensures efficient character tracking.  
- The solution runs in **linear time O(n)**, making it scalable.  

## 📂 **Project Structure**  

```
palindrome_permutation/
├── palindrome_permutation.py  # Python solution
├── README.md                  # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Simple character frequency counting** efficiently checks for palindrome permutations.  
✔ **Runs in O(n) time complexity**, making it **scalable**.  
✔ **Works for all lowercase English letter strings** due to ASCII-based tracking.  

🚀 **Master this technique for solving similar problems!** 🔥  
