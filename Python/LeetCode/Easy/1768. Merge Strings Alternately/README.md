# 🔤 **LeetCode 1768: Merge Strings Alternately**  

## 📌 **Overview**  
This project solves **LeetCode Problem 1768: Merge Strings Alternately**.  
The task is to merge two strings by alternating characters from each string, starting with the first string. If one string is longer than the other, the remaining characters are appended to the end of the merged string.  

### **Problem Statement**  
Given two strings, `word1` and `word2`, return a new string that merges them **alternately**.  
- Start with the **first character of `word1`**, then take the **first character of `word2`**, then the **second character of `word1`**, and so on.  
- If one string is **longer** than the other, append the extra characters **at the end**.  

🔹 **Constraints:**  
- `1 <= len(word1), len(word2) <= 100`  
- `word1` and `word2` contain only **lowercase** English letters.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```
#### **Step-by-Step Breakdown**  
| `word1` | a  | b  | c  |
|---------|----|----|----|
| `word2` | p  | q  | r  |
| **Merged** | a  | p  | b  | q  | c  | r  |

✅ Both strings are **equal in length**, so the characters are interwoven **perfectly**.

### **Example 2**  
```python
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```
#### **Step-by-Step Breakdown**  
| `word1` | a  | b  | -  | -  |
|---------|----|----|----|----|
| `word2` | p  | q  | r  | s  |
| **Merged** | a  | p  | b  | q  | r  | s  |

✅ `word2` is **longer**, so `"rs"` is **appended at the end**.

### **Example 3**  
```python
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```
#### **Step-by-Step Breakdown**  
| `word1` | a  | b  | c  | d  |
|---------|----|----|----|----|
| `word2` | p  | q  | -  | -  |
| **Merged** | a  | p  | b  | q  | c  | d  |

✅ `word1` is **longer**, so `"cd"` is **appended at the end**.

## 🚀 **Understanding the Solution**  
### **Key Observations**
✔ **Use two pointers (`i` and `j`)** to track positions in both words.  
✔ **Append characters alternately** until one string is fully used.  
✔ **If one string is longer**, append the remaining characters **at the end**.  

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialise Variables**  
- `i` and `j` as **pointers** for `word1` and `word2`.  
- `result` as an **empty list** to store characters.

### **2️⃣ Iterate While Both Strings Have Characters**  
- Append `word1[i]` to `result`.  
- Append `word2[j]` to `result`.  
- Increment `i` and `j` **to move to the next characters**.

### **3️⃣ Append Remaining Characters**  
- If `word1` has remaining characters, append `word1[i:]`.  
- If `word2` has remaining characters, append `word2[j:]`.

## 💡 **Python Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of merging two strings alternately.
    
    Given two strings, `word1` and `word2`, the function merges them by alternating 
    characters from each string. If one string is longer, the remaining characters 
    are appended to the end of the merged string.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately, starting with word1.

        :param word1: First string
        :param word2: Second string
        :return: Merged string
        """
        i, j = 0, 0  # Pointers for word1 and word2
        result = []  # List to store merged characters

        # Merge characters from both strings alternately
        while i < len(word1) and j < len(word2):
            result.append(word1[i])  # Append from word1
            result.append(word2[j])  # Append from word2
            i += 1
            j += 1

        # Append remaining characters from the longer string
        result.append(word1[i:])  # Remaining part of word1
        result.append(word2[j:])  # Remaining part of word2

        return "".join(result)  # Convert list to string


def main():
    """
    Demonstrates testing the mergeAlternately function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        ("abc", "pqr"),   # Expected: "apbqcr"
        ("ab", "pqrs"),   # Expected: "apbqrs"
        ("abcd", "pq"),   # Expected: "apbqcd"
    ]

    for word1, word2 in test_cases:
        print(f"Input: word1 = {word1}, word2 = {word2}")
        result = solver.mergeAlternately(word1, word2)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach  | Time Complexity | Space Complexity |
|-----------|---------------|------------------|
| **Merging with Two Pointers** | **O(n + m)** ✅ | **O(n + m)** ✅ |

🔹 **Explanation:**  
- We iterate **through both strings once**, so **O(n + m)** time complexity.  
- We store the result in a **list**, so **O(n + m)** space complexity.  

## 🏗 **Project Structure**
```
1768. Merge Strings Alternately/
├── merge_strings.py   # Python implementation of the solution
├── README.md          # Detailed explanation & walkthrough
```

## 🎯 **Why This Works Well**
✅ Uses **two pointers** for efficiency.  
✅ Handles **unequal length strings** correctly.  
✅ **Simple and intuitive** solution with optimal time complexity.  

**✨ Merge strings the smart way! 🚀**  

I hope you love it! Let me know if you want any refinements. 💙