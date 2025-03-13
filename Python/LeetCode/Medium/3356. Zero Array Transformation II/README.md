# 🟢 **LeetCode 3356: Zero Array Transformation II**  

## 📌 **Problem Overview**  

Given an integer array **nums** of length **n** and a list of queries **queries**, where each query is represented as `[l, r, val]`:  

- Each query **decrements** elements in `nums` within the range `[l, r]` by **at most `val`**.  
- The decrement **amount** can be chosen **independently** for each element.  
- A **Zero Array** is an array where all elements are **zero**.  

Your task is to **find the minimum number of queries `k` required to transform `nums` into a Zero Array**.  
If it's **impossible** to do so, return **`-1`**.

## ✅ **Example 1**  

```python
Input: nums = [2, 0, 2], queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
Output: 2
```

### **Explanation:**  
- Query **1** `[0, 2, 1]`:  
  - Decrease `nums[0]` by `1` → `nums = [1, 0, 2]`  
  - Decrease `nums[2]` by `1` → `nums = [1, 0, 1]`  
- Query **2** `[0, 2, 1]`:  
  - Decrease `nums[0]` by `1` → `nums = [0, 0, 1]`  
  - Decrease `nums[2]` by `1` → `nums = [0, 0, 0]` ✅  

Minimum queries needed: **`2`**.

## ✅ **Example 2**  

```python
Input: nums = [4, 3, 2], queries = [[1, 3, 2], [0, 2, 1]]
Output: -1
```

### **Explanation:**  
- Query **1** `[1, 3, 2]`:  
  - Decrease `nums[1]` by `2` → `nums = [4, 1, 2]`  
  - Decrease `nums[2]` by `2` → `nums = [4, 1, 0]`  
- Query **2** `[0, 2, 1]`:  
  - Decrease `nums[0]` by `1` → `nums = [3, 1, 0]`  
  - Decrease `nums[1]` by `1` → `nums = [3, 0, 0]`  

At this point, `nums` **is not a Zero Array** and no more queries are available. ❌  
Thus, the answer is **`-1`**.

## 🔥 **Intuition & Approach**  

### 🚀 **Key Observations**  
1. **Queries must be applied sequentially.**  
   - We cannot "look ahead" or reorder queries for optimization.  

2. **We must find the minimum `k` queries to reach a Zero Array.**  
   - If `k` queries are not enough, return `-1`.  

3. **Some queries might be redundant.**  
   - If a number is already `0`, applying further queries to it is unnecessary.  

## 🛠 **Optimised Approach: Difference Array + Prefix Sum**  

### 🔹 **Why use a Difference Array?**  
A **difference array** allows **efficient range updates** without iterating over subarrays multiple times.  

### 🔹 **How does the algorithm work?**  
1. **Use a difference array** to keep track of the effect of queries.  
2. **Iterate through `nums`** to check if we can bring each element to `0`.  
3. **Apply queries sequentially** while keeping track of how many are needed.  
4. **If a query does not exist that helps reduce `nums[i]` to `0`, return `-1`.**  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Finds the minimum number of queries required to transform nums into a Zero Array.

        :param nums: List[int] - The input array of integers.
        :param queries: List[List[int]] - A list of queries, where each query is [l, r, val].
        :return: The minimum number of queries required to make nums a Zero Array, or -1 if impossible.
        """
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Process queries while the current index of nums is not zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # If all queries are exhausted and nums is not a Zero Array, return -1
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Apply range update using a difference array technique
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update the running prefix sum at the current index
            total_sum += difference_array[index]

        return k
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating through `nums`** | **O(n)** ✅ |
| **Processing queries** | **O(k)** ✅ |
| **Using a difference array** | **O(1) per update** ✅ |
| **Overall Complexity** | **O(n + k)** ✅ |

## 📂 **Project Structure**  

```
3356. Zero Array Transformation II/
├── zero_array_transformation.py  # Python solution
├── README.md                     # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses a difference array** for efficient updates.  
✔ **Ensures minimal queries are used** to form a Zero Array.  
✔ **Handles edge cases where `nums` cannot be reduced to zero.**  
✔ **Runs in O(n + k) time complexity**, making it **highly efficient**.  

🚀 **Master this technique for handling range updates efficiently!** 🔥  
