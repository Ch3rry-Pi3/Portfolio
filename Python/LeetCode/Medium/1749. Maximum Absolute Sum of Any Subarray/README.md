# 🔢 **LeetCode 1749: Maximum Absolute Sum of Any Subarray**  

## 📌 **Problem Overview**  

You are given an integer array `nums`.  

The **absolute sum** of a subarray `[nums[i], nums[i+1], ..., nums[j]]` is calculated as:  

\[
\text{abs}(nums[i] + nums[i+1] + ... + nums[j])
\]

Return **the maximum absolute sum of any (possibly empty) subarray** of `nums`.  

📌 **Note:**  
- The absolute value of `x`, denoted as `abs(x)`, is defined as:  
  - If `x` is **negative**, then `abs(x) = -x`.  
  - If `x` is **non-negative**, then `abs(x) = x`.  

## 📝 **Examples**  

### **Example 1**  
```python
Input: nums = [-3,2,3,-4]
Output: 5
```
✅ **Explanation:**  
- The **subarray** `[2,3]` has an **absolute sum** of `abs(2+3) = abs(5) = 5`.  

### **Example 2**  
```python
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
```
✅ **Explanation:**  
- The **subarray** `[-5,1,-4]` has an **absolute sum** of `abs(-5+1-4) = abs(-8) = 8`.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Kadane’s Algorithm with Two Passes**  
1. **Maximum Subarray Sum (Kadane's Algorithm)**  
   - Find the **maximum sum subarray** (to track positive gains).  
2. **Minimum Subarray Sum (Kadane’s Algorithm)**  
   - Find the **minimum sum subarray** (to track negative dips).  
3. **Return the maximum of** `abs(max_sum)` and `abs(min_sum)`.  

📌 **Why does this work?**  
- The **Kadane’s algorithm** efficiently finds **max/min subarrays** in **O(n) time**.  
- Instead of checking all subarrays (which takes **O(n²)**), **we update running sums dynamically**.  

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    This class provides a solution to find the maximum absolute sum of any subarray.
    """

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Computes the maximum absolute sum of any subarray in the given list.

        :param nums: List[int] - The input array of integers.
        :return: int - The maximum absolute sum of any subarray.
        """
        max_sum = min_sum = max_absolute = 0

        for num in nums:
            # Track running sums for max and min subarrays
            max_sum = max(0, max_sum + num)
            min_sum = min(0, min_sum + num)

            # Update the maximum absolute sum
            max_absolute = max(max_absolute, abs(max_sum), abs(min_sum))

        return max_absolute
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Finding max subarray sum** | **O(n)** |
| **Finding min subarray sum** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The algorithm **visits each element once**.  
- Uses **constant extra space** (`O(1)`).  
- **Faster than brute force O(n²) methods**.  

## 📂 **Project Structure**  

```
maximum_absolute_sum/
├── maximum_absolute_sum.py  # Python solution
├── README.md                # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Efficient O(n) approach** using **Kadane’s Algorithm**.  
✔ **Tracks both max and min subarrays** to find absolute max.  
✔ **Handles positive and negative subarrays dynamically**.  

🚀 **Master this trick for max/min subarray problems!**  