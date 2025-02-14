# 🔤 **LeetCode 2351: First Letter to Appear Twice**

## 📌 **Problem Statement**
Given a string `s` consisting only of **lowercase English letters**, return **the first letter to appear twice**.

### 🔹 **Constraints**
- The input string `s` will **always** contain **at least one** letter that appears twice.

### 📜 **Note**
A letter **`a`** appears twice before another letter **`b`** **if the second occurrence** of `a` appears **before** the second occurrence of `b`.

## 🏆 **Examples & Explanation**

### **Example 1**
#### **Input:**
```python
s = "abccbaacz"
```
#### **Output:**
```python
"c"
```
#### **Explanation:**
| Letter | Index Positions |
|---------|---------------|
| `'a'` | Appears at indices **0, 5, 6** |
| `'b'` | Appears at indices **1, 4** |
| `'c'` | Appears at indices **2, 3, 7** |
| `'z'` | Appears at index **8** |

- The first letter to **repeat twice** is **`'c'`** because its second occurrence (index `3`) appears before any other letter's second occurrence.

### **Example 2**
#### **Input:**
```python
s = "abcdd"
```
#### **Output:**
```python
"d"
```
#### **Explanation:**
- The only letter that appears twice is **`'d'`**, so we return `"d"`.

## 🛠 **Approach**
The problem can be solved efficiently using a **set** to track letters that have already been seen.

### **🔹 Optimised Approach (Using a Set)**
1. **Initialise an empty set** called `seen_letters` to store characters encountered so far.
2. **Iterate through each character** in `s`:
   - If the character is **already in the set**, return it immediately.
   - Otherwise, **add it to the set** and continue.
3. Since the problem guarantees that at least one letter appears twice, **we will always return a result**.

---

## 🚀 **Python Solution**
```python
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        """
        Finds the first letter in the given string `s` that appears twice.

        Args:
            s (str): Input string containing only lowercase English letters.

        Returns:
            str: The first letter that appears twice.
        """

        seen_letters = set()

        for char in s:
            if char in seen_letters:
                return char
            seen_letters.add(char)

        return ""  # This case won't occur as per the problem statement.
```

## ⏳ **Complexity Analysis**
| Operation | Time Complexity | Space Complexity |
|-----------|---------------|----------------|
| **Iterating through `s`** | **O(N)** | **O(1)** (only 26 letters in English alphabet) |
| **Checking membership in `set()`** | **O(1) (average case)** | **O(1)** |
| **Adding elements to `set()`** | **O(1) (average case)** | **O(1)** |

### 🔹 **Why This Approach?**
✅ **Uses a set for O(1) lookups**, making it much faster than a list-based approach.  
✅ **Iterates through `s` only once** (O(N) time complexity).  
✅ **Minimal space usage** (only storing at most 26 letters).  

## 🎯 **Key Takeaways**
✔ **Use a set for efficient membership checks.**  
✔ **Early exit when a repeated letter is found.**  
✔ **Guaranteed to find an answer, since at least one letter repeats.**  

🚀 **This solution ensures optimal performance and simplicity!**  
