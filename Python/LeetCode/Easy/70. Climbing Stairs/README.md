# 🏆 LeetCode 70: Climbing Stairs

## 📌 Overview
This project solves **LeetCode Problem 70: Climbing Stairs**.

The problem is modeled as a **Fibonacci-like sequence**, where each step can be reached by taking either **one step** or **two steps** from a previous step. The task is to determine the number of distinct ways to climb `n` steps.

---

## 🎯 Problem Statement
Given an integer `n`, representing the number of steps, return the number of **distinct ways** to climb to the top.

🔹 **Constraints:**
- `1 <= n <= 45`

---

## 🚀 Intuition & Approach
### **Understanding the Problem with a Decision Tree**
Each step has **two decisions**:
- Take **1 step** → Move to `n - 1`
- Take **2 steps** → Move to `n - 2`

For example, starting from step `0`:
```
Step 0:
 - Take 1 Step -> Step 1
 - Take 2 Steps -> Step 2
```
Each branch continues similarly. However, this recursive approach **recomputes the same subproblems multiple times**, leading to an exponential `O(2^n)` time complexity.

### **Optimised Approach: Dynamic Programming**
Instead of recomputing values, we use **memoisation** or **bottom-up DP**:
- **Store results** in memory and build up from base cases.
- The number of ways to reach `n` is the sum of ways to reach `n-1` and `n-2`:
  
  **`dp[n] = dp[n-1] + dp[n-2]`**

#### **Why This Works? (Step-by-Step Breakdown)**
Consider `n = 5`. We initialise `one` and `two`:
- `one` represents ways to reach `n-1`.
- `two` represents ways to reach `n-2`.

We **iterate backwards** from `n-1` down to `1`, updating values dynamically:

| Step | `one` (ways to n-1) | `two` (ways to n-2) | New `one` (ways to n) |
|------|---------------------|---------------------|-----------------|
| 5    | 1                   | 1                   | `1 + 1 = 2`       |
| 4    | 2                   | 1                   | `2 + 1 = 3`       |
| 3    | 3                   | 2                   | `3 + 2 = 5`       |
| 2    | 5                   | 3                   | `5 + 3 = 8`       |
| 1    | 8                   | 5                   | `8 + 5 = 13`      |

Final result: `dp[5] = 8`, meaning there are **8 distinct ways** to climb 5 steps.

#### **Optimised Space Complexity**
We only need **two variables (`one` and `two`)** instead of an array, reducing space complexity to **O(1)**.

---

## 💡 Code Implementation
```python
from typing import List

class Solution:
    """
    This class provides a solution for the Climbing Stairs problem.
    """
    def climbStairs(self, n: int) -> int:
        """
        Computes the number of distinct ways to climb 'n' stairs.

        :param n: The total number of steps.
        :return: The number of unique ways to climb to the top.
        """
        # Base cases: Only one way to reach step 0 or step 1
        one, two = 1, 1

        # Iterating from the second-to-last step down to the first step
        for _ in range(n - 1):
            temp = one
            one = one + two         # Update step count based on previous two steps
            two = temp              # Shift values forward
        
        return one

def main():
    """
    Runs test cases for the climbStairs function.
    """
    solver = Solution()
    
    test_cases = [
        2,          # Expected: 2
        3,          # Expected: 3
        4,          # Expected: 5
        5,          # Expected: 8
        6           # Expected: 13
    ]

    for n in test_cases:
        print(f"Input: n = {n}")
        result = solver.climbStairs(n)
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main()
```

---

## ⏳ **Time & Space Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Recursive (Brute-force)** | **O(2^n)** 🚫 | **O(n)** 🚫 |
| **Memoisation (Top-down DP)** | **O(n)** ✅ | **O(n)** ✅ |
| **Iterative DP (Bottom-up)** | **O(n)** ✅ | **O(1)** ✅ |

🔹 **Best Solution**: Iterative DP with `O(n)` time and `O(1)` space.

---

## **🏗 Project Structure**
```
climbing_stairs/
├── climbing_stairs.py  # Python implementation of the solution
├── README.md           # Detailed explanation & walkthrough
```

✨ **Master recursion and dynamic programming with this intuitive approach!** 🚀

