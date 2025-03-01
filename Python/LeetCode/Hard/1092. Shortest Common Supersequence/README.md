# 📌 **LeetCode 1092: Shortest Common Supersequence**

## 📝 **Problem Statement**
Given two strings **str1** and **str2**, return **the shortest string** that has both **str1** and **str2** as **subsequences**.  
If multiple valid answers exist, return **any of them**.

### 🔹 **Definitions**
- A **subsequence** of a string is obtained by deleting some (possibly zero) characters **without reordering** the remaining characters.

## 🏆 **Examples & Explanation**

### **Example 1**
```python
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
```
✅ **Explanation:**  
- "abac" is a subsequence of "cabac" (remove the first 'c').  
- "cab" is a subsequence of "cabac" (remove "ac").  
- The answer provided is the shortest possible string satisfying these conditions.

### **Example 2**
```python
Input: str1 = "aaaaaaaa", str2 = "aaaaaaa"
Output: "aaaaaaaa"
```
✅ **Explanation:**  
- Both strings are nearly identical. The **shortest common supersequence** is simply **"aaaaaaaa"**.

### **Example 3**
```python
Input: str1 = "geek", str2 = "eke"
Output: "geeke"
```
✅ **Explanation:**  
- "geek" is a subsequence of "geeke" (remove one 'e').  
- "eke" is a subsequence of "geeke" (remove 'g').

## 💡 **Approach & Algorithm**

### **🔹 Key Idea: Dynamic Programming**
1. **Construct a DP Table**  
   - `dp[i][j]` stores **length of the shortest common supersequence** for `str1[:i]` and `str2[:j]`.
   - If characters match, inherit diagonal value `+1`.
   - Otherwise, take the **minimum** of the previous row or column `+1`.

2. **Backtracking to Construct the Supersequence**
   - Start from `dp[len(str1)][len(str2)]`.
   - Move diagonally if characters match.
   - Otherwise, move in the direction of the smaller value.

📌 **Why This Works?**  
- **Bottom-up DP ensures optimal length calculation.**  
- **Backtracking reconstructs the actual sequence efficiently.**  

## ⏳ **Time & Space Complexity**

| Operation | Complexity |
|-----------|------------|
| **Building DP Table** | **O(m × n)** |
| **Backtracking for Supersequence** | **O(m + n)** |
| **Overall Complexity** | **O(m × n)** |

🚀 **Efficient for input sizes up to `1000 × 1000`**.

## 💻 **Implementation (Python)**
```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Finds the shortest string that has both str1 and str2 as subsequences.

        :param str1: First input string.
        :param str2: Second input string.
        :return: Shortest common supersequence string.
        """
        str1_length = len(str1)
        str2_length = len(str2)

        # Initialise DP table
        dp = [[0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)]

        # Base cases
        for row in range(str1_length + 1):
            dp[row][0] = row
        for col in range(str2_length + 1):
            dp[0][col] = col

        # Fill DP table
        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        # Backtracking to construct the shortest common supersequence
        super_sequence = []
        row, col = str1_length, str2_length

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                super_sequence.append(str2[col - 1])
                col -= 1

        # Append remaining characters
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1

        return "".join(super_sequence[::-1])
```

## 📂 **Project Structure**
```
shortest_common_supersequence/
├── shortest_common_supersequence.py  # Python solution
├── README.md                          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**
✔ **Uses Dynamic Programming** for efficient `O(m × n)` computation.  
✔ **Reconstructs the supersequence using backtracking**.  
✔ **Handles multiple valid outputs** by constructing one valid solution.  

🔥 **Mastering this problem improves understanding of DP-based string operations!** 🔥  