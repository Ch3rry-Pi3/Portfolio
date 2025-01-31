# 🚀 **LeetCode 338: Counting Bits**

## 📌 **Overview**

This project solves **LeetCode Problem 338: Counting Bits**. The task is to generate an array where each index `i` contains the **number of 1 bits** (also known as the Hamming Weight) in the binary representation of `i`.

### **Problem Statement**

Given an integer `n`, return an array `ans` of length `n + 1` where:

- `ans[i]` is the number of **1's** in the binary representation of `i`.

🔹 **Constraints:**

- `0 <= n <= 10⁵`
- The solution must run in **O(n)** time complexity.

## 🎯 **Example Walkthrough**

### **Example 1**

```python
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0 (0 ones)
1 --> 1 (1 one)
2 --> 10 (1 one)
```

### **Example 2**

```python
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 -->  0   (0 ones)
1 -->  1   (1 one)
2 --> 10   (1 one)
3 --> 11   (2 ones)
4 --> 100  (1 one)
5 --> 101  (2 ones)
```

## 🚀 **Understanding the Problem**

### **Key Observations**

✔ Every number has a unique **binary representation**.
✔ We need to **count the number of 1 bits** efficiently.
✔ A naive approach would iterate through numbers and count `1`s in their binary form (**O(n log n)**).
✔ A **dynamic programming (DP) approach** allows us to solve it in **O(n)**.

## 📝 **Step-by-Step Approach**

### **1️⃣ Dynamic Programming (DP) Approach**

- **Initialise a DP array**: `dp = [0] * (n + 1)` to store the count of 1s for each number.
- **Track the highest power of 2** encountered using `offset`.
- **Use the recurrence relation**:
  ```
  dp[i] = 1 + dp[i - offset]
  ```
  - This means: the number of `1`s in `i` is **1 + number of 1s in \*\*\*\*****`i - offset`**.
- \*\*Update \*\***`offset`** when `i` reaches a new power of 2.

## **Implementation**

```python
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Computes the number of `1` bits for each number from 0 to `n`.

        :param n: Integer representing the upper limit
        :return: List containing the count of 1 bits for each number in range [0, n]
        """
        dp = [0] * (n + 1)      # Initialise DP array
        offset = 1              # Tracks most significant power of 2

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i              # Update offset at power of 2
            
            dp[i] = 1 + dp[i - offset]  # DP formula

        return dp
```

## ⏳ **Time Complexity Analysis**

| Approach                                                               | Time Complexity  | Space Complexity |
| ---------------------------------------------------------------------- | ---------------- | ---------------- |
| **Brute Force (********`bin(i).count('1')`********)**                  | **O(n log n)** ❌ | **O(n)** ✅       |
| **Dynamic Programming (********`dp[i] = 1 + dp[i - offset]`********)** | **O(n)** ✅       | **O(n)** ✅       |

✔ **The DP approach runs in ********`O(n)`********, making it optimal for large values of ********`n`********.**
✔ **Only ********`O(n)`******** extra space is required for the DP array.**

## 🏗 **Project Structure**

```
338. Counting Bits/
├── counting_bits.py    # Efficient O(n) DP solution
├── README.md           # Detailed explanation & walkthrough
```

**🚀 Master Dynamic Programming and Bitwise Tricks for Optimal Performance!**

