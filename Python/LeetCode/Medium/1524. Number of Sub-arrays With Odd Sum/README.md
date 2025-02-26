# 🔢 **LeetCode 1524: Number of Sub-arrays With Odd Sum**  

## 📌 **Problem Overview**  

Given an array of integers **arr**, return the **number of subarrays** that have an **odd sum**.  

Since the result can be **very large**, return the answer **modulo** \(10^9 + 7\).  

## 📝 **Example 1**  

```python
Input: arr = [1, 3, 5]  
Output: 4
```

✅ **Explanation:**  
- All possible subarrays: `[[1], [1,3], [1,3,5], [3], [3,5], [5]]`
- Their sums: `[1, 4, 9, 3, 8, 5]`
- Odd sums: `[1, 9, 3, 5]`
- **Total odd subarrays = 4**  

## 📝 **Example 2**  

```python
Input: arr = [2, 4, 6]  
Output: 0
```

✅ **Explanation:**  
- All subarrays have an **even sum**, so the result is **0**.  

## 📝 **Example 3**  

```python
Input: arr = [1,2,3,4,5,6,7]  
Output: 16
```

✅ **Explanation:**  
- There are **16** subarrays with an **odd sum**.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Using Dynamic Programming**  
Instead of generating **all subarrays** (which would be **O(n²)**), we can **track odd/even sums efficiently** using DP:

1. Convert **each number** to `0` (even) or `1` (odd).
2. Maintain **two DP arrays**:  
   - **dp_even[i]** → Number of subarrays **ending at i** with an **even sum**.  
   - **dp_odd[i]** → Number of subarrays **ending at i** with an **odd sum**.  
3. If `arr[i]` is:
   - **Odd (`1`)** → It **flips** even to odd & vice versa.
   - **Even (`0`)** → It **extends** the current sequence without flipping.  
4. **Summing up all `dp_odd[i]` values** gives the final count.  

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    This class provides a solution for counting subarrays with an odd sum.
    """

    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Returns the number of subarrays with an odd sum.

        :param arr: List[int] - The input array of integers.
        :return: int - The count of subarrays with an odd sum modulo 10^9 + 7.
        """
        MOD = int(1e9 + 7)  # Modulo value to prevent integer overflow
        n = len(arr)

        # Convert each element to 0 (even) or 1 (odd)
        arr = [num % 2 for num in arr]

        # dp_even[i]: Number of subarrays with an even sum ending at index i
        # dp_odd[i]: Number of subarrays with an odd sum ending at index i
        dp_even, dp_odd = [0] * n, [0] * n

        # Initialise the last element
        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            dp_odd[n - 1] = 1

        # Traverse the array in reverse to calculate dp values
        for i in range(n - 2, -1, -1):
            if arr[i] == 1:
                # Odd element contributes to odd subarrays
                dp_odd[i] = (1 + dp_even[i + 1]) % MOD
                # Even element continues the pattern
                dp_even[i] = dp_odd[i + 1]
            else:
                # Even element contributes to even subarrays
                dp_even[i] = (1 + dp_even[i + 1]) % MOD
                # Odd element continues the pattern
                dp_odd[i] = dp_odd[i + 1]

        # Sum all the odd subarrays and return the result
        return sum(dp_odd) % MOD

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating over array (O(n))** | **O(n)** |
| **Summing up odd subarrays** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- **We traverse the array only once** → **O(n)** complexity.  
- **No need to store all subarrays** → **Efficient space usage**.  

## 📂 **Project Structure**  

```
subarrays_odd_sum/
├── subarrays_odd_sum.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Avoids brute force O(n²) approach** using **efficient DP**.  
✔ **Uses modulo `10^9 + 7`** to prevent overflow.  
✔ **Simple yet effective approach** with clear logic.  

🚀 **Master this technique for future DP problems!** 🔥  
