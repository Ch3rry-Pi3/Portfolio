# 🔢 **LeetCode 873: Length of Longest Fibonacci Subsequence**  

## 📌 **Problem Overview**  

A sequence \( x_1, x_2, ..., x_n \) is **Fibonacci-like** if:  

- \( n \geq 3 \)  
- \( x_i + x_{i+1} = x_{i+2} \) for all \( i \geq 1 \)  

Given a **strictly increasing array** `arr` of **positive integers**, return the **length of the longest Fibonacci-like subsequence** of `arr`.  

If one does not exist, return **0**.  

📌 **Note:**  
A **subsequence** is derived from another sequence by **deleting any number of elements** (including none) without changing the order of the remaining elements.  

## 📝 **Examples**  

### **Example 1**  
```python
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
```
✅ **Explanation:**  
The **longest subsequence** that is Fibonacci-like: **[1,2,3,5,8]**.  

### **Example 2**  
```python
Input: arr = [1,3,7,11,12,14,18]
Output: 3
```
✅ **Explanation:**  
The **longest subsequence** that is Fibonacci-like: **[1,11,12]**, **[3,11,14]**, or **[7,11,18]**.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Dynamic Programming with Two Pointers**  
1. **Use a 2D DP table** `dp[prev][curr]` where:  
   - `prev` is the **index of the second-last number** in the sequence.  
   - `curr` is the **index of the last number** in the sequence.  
   - `dp[prev][curr]` stores the **length of the Fibonacci-like sequence** ending at `arr[prev]` and `arr[curr]`.  
2. **Use Two Pointers to Find Valid Pairs**  
   - For each `curr`, find **pairs (start, end)** such that `arr[start] + arr[end] = arr[curr]`.  
   - Update `dp[end][curr] = dp[start][end] + 1`.  
3. **Track Maximum Length**  
   - The longest sequence found is stored in `max_len`.  
   - If no sequence is found, return **0**.  

📌 **Why does this work?**  
- **Finding valid pairs takes O(n²)** using two pointers.  
- **Updating DP is efficient** and avoids unnecessary calculations.  

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    This class provides a solution to find the longest Fibonacci-like subsequence.
    """

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Computes the length of the longest Fibonacci-like subsequence in arr.

        :param arr: List[int] - The input list of strictly increasing positive integers.
        :return: int - The length of the longest Fibonacci-like subsequence.
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        for curr in range(2, n):
            start, end = 0, curr - 1

            while start < end:
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    # Found a valid Fibonacci-like subsequence
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(dp[end][curr], max_len)
                    end -= 1
                    start += 1

        return max_len + 2 if max_len else 0
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Finding valid Fibonacci-like pairs** | **O(n²)** |
| **Updating DP table** | **O(1) per pair** |
| **Overall Complexity** | **O(n²)** ✅ |

🔹 **Why is this optimal?**  
- The **brute-force approach (O(2ⁿ)) is impractical**.  
- **Using DP with two pointers reduces redundant checks**.  

## 📂 **Project Structure**  

```
longest_fibonacci_subsequence/
├── longest_fibonacci_subsequence.py  # Python solution
├── README.md                          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Efficient O(n²) approach** using **Dynamic Programming**.  
✔ **Uses two-pointers** to efficiently check Fibonacci conditions.  
✔ **Handles large inputs efficiently** due to optimised lookups.  

🚀 **Master this technique for Fibonacci-style subsequence problems!**  
