# 🚀 **LeetCode 139: Word Break**

## 📌 **Overview**
This project solves **LeetCode Problem 139: Word Break**.  
The goal is to determine if a string `s` **can be segmented into words** from a given dictionary.

### **Problem Statement**
Given a **string** `s` and a **dictionary** `wordDict`, return:
- `True` if `s` can be segmented into a **space-separated sequence** of words from `wordDict`.
- `False` otherwise.

🔹 **Constraints:**
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` consists only of **lowercase English letters**.
- Each word in `wordDict` is **unique**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
```
#### **Explanation:**
- We can split `"leetcode"` as **"leet" + "code"**.
- Both words exist in `wordDict`.

### **Example 2**
```python
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
```
#### **Explanation:**
- We can split `"applepenapple"` as **"apple" + "pen" + "apple"**.
- Words can be **reused multiple times**.

### **Example 3**
```python
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
```
#### **Explanation:**
- There is **no valid segmentation** using `wordDict`.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **A word can be used multiple times** in segmentation.  
✔ **Order matters** – we must form `s` in sequence.  
✔ **A dynamic programming approach efficiently solves the problem.**  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `s = "applepenapple"` and `wordDict = ["apple", "pen"]` to see how we use **dynamic programming**.

#### **Step 1️⃣: Define a DP Array**
We create an **array `dp`** where:
- `dp[i] = True` means `s[0:i]` can be **formed using `wordDict`**.
- Initialize `dp[len(s)] = True` (**Base case: an empty substring is always valid**).

```
s = "applepenapple"
dp = [False, False, False, False, False, False, False, False, False, False, False, False, True]
```

#### **Step 2️⃣: Traverse Backward and Check Words**
| Index | Substring Checked | Found in `wordDict`? | `dp` Update |
|--------|------------------|--------------------|------------|
| `10`  | `"apple"`        | ✅ Yes  | `dp[10] = dp[15] = True` |
| `5`   | `"pen"`          | ✅ Yes  | `dp[5] = dp[10] = True` |
| `0`   | `"apple"`        | ✅ Yes  | `dp[0] = dp[5] = True` |

At the end, `dp[0] = True`, so we **return `True`**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialise a DP Array**
- Create `dp = [False] * (len(s) + 1)`, where `dp[i]` stores **whether `s[i:]` can be segmented**.
- Set `dp[len(s)] = True` (**Base case: empty string is always valid**).

### **2️⃣ Iterate Backward Through `s`**
- For each `i` from `len(s)-1` to `0`:
  - Check if any word in `wordDict` **matches `s[i:i+len(w)]`**.
  - If a word matches, update `dp[i] = dp[i + len(w)]`.

### **3️⃣ Return `dp[0]`**
- If `dp[0] = True`, `s` can be segmented; otherwise, it **cannot**.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Word Break' problem.

    The function `wordBreak` determines if a given string `s` can be segmented 
    into words found in a given dictionary using dynamic programming.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into words from `wordDict`.

        :param s: Input string.
        :param wordDict: List of valid words.
        :return: True if `s` can be segmented using words from `wordDict`, otherwise False.
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True                           # Base case: An empty substring is always a valid segmentation

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]          # If the suffix is valid, mark dp[i] as True
                if dp[i]:                           # If we found a valid segmentation, no need to check further
                    break

        return dp[0]                                # The result is stored at the beginning of the DP array
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Dynamic Programming (`O(n * m)`)** | **O(n * m)** ✅ | **O(n)** ✅ |

- **Each position `i` in `s` is checked against all words in `wordDict` (`O(n * m)`).**
- **The `dp` array uses `O(n)` space.**

## 🏗 **Project Structure**
```
139. Word Break/
├── word_break.py    # Python implementation of the solution
├── README.md        # Detailed explanation & walkthrough
```

✨ **Master dynamic programming with an efficient `O(n * m)` approach!** 🚀  