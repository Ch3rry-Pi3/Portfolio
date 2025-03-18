# 🌟 **LeetCode 2401: Longest Nice Subarray**  

## 📌 **Problem Overview**  

Given an array **nums** consisting of **positive integers**, a subarray is considered **"nice"** if:  
- The **bitwise AND** of every pair of elements in different positions is **equal to 0**.  

Return the **length of the longest nice subarray**.  

## ✅ **Example 1**  

```python
Input: nums = [1, 3, 8, 48, 10]
Output: 3
```

### **Explanation:**  
The longest nice subarray is `[3, 8, 48]`, which satisfies the conditions:  
- **3 AND 8 = 0**  
- **3 AND 48 = 0**  
- **8 AND 48 = 0**  

Thus, the longest nice subarray has length **3**.

## ✅ **Example 2**  

```python
Input: nums = [3, 1, 5, 11, 13]
Output: 1
```

### **Explanation:**  
Each number in the array has **at least one bit in common** with another number, so **only individual elements** can be considered "nice."  
Thus, the longest nice subarray is **any single element**, and the answer is **1**.

## 🔎 **Intuition & Approach**  

### 🔹 **Understanding the "Nice" Condition**  
A **subarray** is "nice" if every **pair of elements** has a **bitwise AND = 0**.  
This means that **no two numbers** in the subarray **share a '1' bit** in the same position.

### 🔹 **Optimal Sliding Window Approach (Bitwise Operations)**  
Instead of checking **all possible subarrays**, we use a **sliding window** to efficiently find the longest valid subarray:

1. **Expand the window** by adding elements while maintaining the "nice" condition.  
2. **If the condition is violated**, shrink the window from the left until it is valid again.  
3. **Keep track of the maximum length** of any valid window.  

⏳ **Time Complexity:** **O(n)** → Each element is processed at most twice (once when added, once when removed).  
📌 **Space Complexity:** **O(1)** → Uses only a few integer variables.

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest 'nice' subarray.
        
        A subarray is 'nice' if the bitwise AND of every pair of elements
        in different positions is equal to 0.

        :param nums: List of positive integers.
        :return: Length of the longest nice subarray.
        """
        used_bits = 0           # Tracks bits used in current window
        window_start = 0        # Start position of current window
        max_length = 0          # Length of longest nice subarray found

        for window_end in range(len(nums)):
            # If current number shares bits with window, shrink window from left
            # until there's no bit conflict
            while used_bits & nums[window_end] != 0:
                used_bits ^= nums[window_start]  # Remove leftmost element's bits
                window_start += 1  # Shrink window from left

            # Add current number to the window
            used_bits |= nums[window_end]

            # Update max length if current window is longer
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

```

## ⏳ **Time Complexity Analysis**  

| Operation                 | Complexity  |
|---------------------------|------------|
| **Sliding Window Updates** | **O(n)** ✅ |
| **Bitwise Operations**      | **O(1)** ✅ |
| **Overall Complexity**      | **O(n)** ✅ |

### 🚀 **Why is this efficient?**
- **Each element is processed at most twice** (once when added, once when removed).  
- **Bitwise operations run in constant time O(1)**.  
- **No extra space is needed**, making it **memory-efficient**.  

## 📂 **Project Structure**  

```
2401. Longest Nice Subarray/
├── longest_nice_subarray.py  # Python solution
├── README.md              # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses an optimal sliding window technique** to efficiently check subarrays.  
✔ **Leverages bitwise operations** to quickly detect conflicts.  
✔ **Runs in O(n) time complexity**, making it **scalable** for large inputs.  

🚀 **Master this technique for solving similar bitwise and sliding window problems!** 🔥  