# 📌 LeetCode 1143: Longest Common Subsequence

## 📝 Overview
This project solves **LeetCode Problem 1143: Longest Common Subsequence**.
The goal is to find the **length of the longest common subsequence** shared between two input strings.

### **Problem Statement**
Given two strings `text1` and `text2`, return the **length of their longest common subsequence**.
A **subsequence** of a string is a sequence of characters that appears in the same relative order but not necessarily contiguous.

🔹 **Constraints:**
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist only of lowercase English letters.

## 🎯 Example Walkthrough

### **Example 1**
```python
Input: text1 = "abcde", text2 = "ace"
Output: 3
```
**Explanation:**
- The longest common subsequence is **"ace"**, which appears in both strings in order.
- Its length is `3`, so we return `3`.

### **Example 2**
```python
Input: text1 = "abc", text2 = "abc"
Output: 3
```
**Explanation:**
- The longest common subsequence is **"abc"** (the entire string).
- Its length is `3`.

### **Example 3**
```python
Input: text1 = "abc", text2 = "def"
Output: 0
```
**Explanation:**
- There is no common subsequence, so the result is `0`.

## 🚀 Understanding the Approach
### **1️⃣ Key Observations**
✔ The **order of characters must be maintained** but they do **not need to be contiguous**.
✔ If the last characters of both strings match, the LCS is **1 + LCS of the remaining substrings**.
✔ Otherwise, we take the **maximum LCS found** by either:
  - Ignoring the last character of `text1`.
  - Ignoring the last character of `text2`.
✔ This is a classic **dynamic programming** problem.

## 📝 Step-by-Step Algorithm
### **1️⃣ Initialize a DP Table**
- Create a **2D DP table** of size `(len(text1) + 1) x (len(text2) + 1)`, filled with `0`s.
- The extra row and column represent an empty string case.

### **2️⃣ Iterate Through Both Strings Backward**
- Start from the **end** of both strings.
- If `text1[i] == text2[j]`, we extend the LCS by `1 + dp[i+1][j+1]`.
- Otherwise, we take the **maximum** of `dp[i+1][j]` and `dp[i][j+1]`.

### **3️⃣ Return dp[0][0]**
- The **top-left** cell (`dp[0][0]`) contains the final answer.

## 🔍 Example Walkthrough with Code Execution

### **Input: text1 = "abcde", text2 = "ace"**
#### **Step 1: Initialize DP Table**
```
  a  c  e
 0  0  0  0
 0  0  0  0
 0  0  0  0
 0  0  0  0
 0  0  0  0
 0  0  0  0
```

#### **Step 2: Fill DP Table Backward**
| `text1` | `text2` | Match? | Action |
|---------|---------|--------|--------|
| `e` vs `e` | ✅ Yes | `dp[i][j] = 1 + dp[i+1][j+1]` |
| `d` vs `e` | ❌ No  | `dp[i][j] = max(dp[i+1][j], dp[i][j+1])` |
| `c` vs `c` | ✅ Yes | `dp[i][j] = 1 + dp[i+1][j+1]` |
| `b` vs `c` | ❌ No  | `dp[i][j] = max(dp[i+1][j], dp[i][j+1])` |
| `a` vs `a` | ✅ Yes | `dp[i][j] = 1 + dp[i+1][j+1]` |

At the end, `dp[0][0] = 3`, meaning the longest common subsequence is `"ace"`.

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Dynamic Programming (Bottom-Up)** | **O(m * n)** ✅ | **O(m * n)** ✅ |

- **We iterate through every cell** in the DP table, making it **O(m * n)**.
- **Space complexity is also O(m * n)**, but can be optimized to **O(min(m, n))** using a rolling array.

## **🏗 Project Structure**
```
1143. Longest Common Subsequence/
├── longest_common_subsequence.py   # Python implementation of the solution
├── README.md                       # Detailed explanation & walkthrough
```

✨ **Master dynamic programming with this classic problem!** 🚀