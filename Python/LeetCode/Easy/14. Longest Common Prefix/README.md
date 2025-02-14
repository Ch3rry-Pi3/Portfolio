# 🌟 **LeetCode 14: Longest Common Prefix**  

## 📌 **Problem Statement**  
Given an array of strings, find the **longest common prefix** shared among all the strings.  
If there is no common prefix, return an empty string `""`.  

### 🔹 **Constraints**  
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists only of **lowercase English letters**.

## 🎯 **Understanding the Problem**  

### ✅ **Example 1**  
#### **Input:**  
```python
strs = ["flower", "flow", "flight"]
```
#### **Output:**  
```python
"fl"
```
#### **Explanation:**  
The first two letters `fl` are common in all words.

### ✅ **Example 2**  
#### **Input:**  
```python
strs = ["dog", "racecar", "car"]
```
#### **Output:**  
```python
""
```
#### **Explanation:**  
There is no common prefix among all words, so we return an empty string.

### ✅ **Example 3**  
#### **Input:**  
```python
strs = ["interspecies", "interstellar", "interstate"]
```
#### **Output:**  
```python
"inters"
```
#### **Explanation:**  
All words share the common prefix `"inters"`.

## 💡 **Intuition & Approach**  

### 🔹 **Observations**
1. The longest possible prefix cannot be longer than the **shortest word** in the list.
2. If a mismatch occurs at index `i`, the common prefix **must be** from `0` to `i-1`.
3. The best approach is **character-by-character comparison** across all words.

### 🔄 **Efficient Strategy:**
- Identify the **shortest word length** to limit comparisons.
- Iterate **character by character**:
  - If a mismatch is found, return the prefix up to that point.
- If we check all characters, return the complete prefix.

## 🚀 **Optimised Python Solution**  

```python
from typing import List

class Solution:
    """
    A class to find the longest common prefix among an array of strings.
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix in a list of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. If there is no common prefix, returns an empty string.
        """
        # Edge case: If the list is empty, return an empty string
        if not strs:
            return ""

        # Find the minimum length of all strings in the list
        min_length = min(len(s) for s in strs)

        # Iterate character by character up to the minimum length found
        for i in range(min_length):
            # Compare the character at position 'i' across all strings
            if any(s[i] != strs[0][i] for s in strs):
                return strs[0][:i]

        # If we complete the loop, return the full prefix up to 'min_length'
        return strs[0][:min_length]
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Find min length** | `min(len(s) for s in strs)` | **O(N)** |
| **Iterate characters** | `for i in range(min_length)` | **O(M)** (M is min word length) |
| **Compare characters** | `if s[i] != strs[0][i]` | **O(N)** per character |
| **Total Complexity** | **O(N * M)** |

💡 **Where:**  
- `N` is the number of words.  
- `M` is the length of the shortest word.

## 🔥 **Why This Approach?**
✔ **Efficient character-based scanning** instead of full sorting.  
✔ **No extra space usage**—constant space `O(1)`.  
✔ **Handles edge cases** like single-word lists and empty strings.  

## 🎯 **Key Takeaways**
- The longest common prefix is limited by the **shortest word**.
- Comparing **character by character** is **better** than sorting all words.
- The function efficiently **exits early** upon detecting a mismatch.

🚀 **With this approach, you can efficiently find the longest common prefix in any list of words!** 🎯