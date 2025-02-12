# 🎯 **LeetCode 724: Find Pivot Index**  

## 📌 **Problem Overview**  
Given an array of integers `nums`, the **pivot index** is the index where the sum of all numbers **strictly** to the left is equal to the sum of all numbers **strictly** to the right.

- If the index is at the left edge, the **left sum is 0** because there are no elements to the left.
- If the index is at the right edge, the **right sum is 0** because there are no elements to the right.
- **Return the leftmost pivot index** if it exists; otherwise, return `-1`.  

## 📊 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```python
nums = [1, 7, 3, 6, 5, 6]
```
#### **Output:**  
```python
3
```
#### **Explanation:**  
- Left sum of index `3` → `1 + 7 + 3 = 11`  
- Right sum of index `3` → `5 + 6 = 11`  
- Since both sums are equal, **pivot index = `3`** ✅  

### **Example 2**  
#### **Input:**  
```python
nums = [1, 2, 3]
```
#### **Output:**  
```python
-1
```
#### **Explanation:**  
- No index satisfies the pivot condition.  

### **Example 3**  
#### **Input:**  
```python
nums = [2, 1, -1]
```
#### **Output:**  
```python
0
```
#### **Explanation:**  
- Left sum of index `0` → `0` (no elements to the left)  
- Right sum of index `0` → `1 + (-1) = 0`  
- Since both sums are equal, **pivot index = `0`** ✅  

## 🔍 **Intuition**  

The **pivot index** is the position in the array where the left and right sums are equal.  
Instead of calculating the left and right sums separately in a nested loop (**O(N²)** complexity), we can use a **single pass approach** (**O(N)** complexity):

1. Compute the **total sum** of the array.
2. Maintain a **running left sum** as we iterate.
3. For each index `i`, check if `left_sum == total_sum - left_sum - nums[i]`.
4. If the condition holds, return `i` (leftmost index satisfying the condition).
5. If no pivot index is found, return `-1`.

## 🚀 **Optimised Approach (Single Pass, O(N))**  

### **Python Solution**  
```python
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Finds the pivot index in an array where the sum of all numbers strictly
        to the left equals the sum of all numbers strictly to the right.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The leftmost pivot index if it exists, otherwise -1.
        """

        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Initialise left sum as 0
        left_sum = 0

        # Iterate over each index and check pivot condition
        for i, num in enumerate(nums):
            # If left sum equals the right sum (total_sum - left_sum - num), return index
            if left_sum == (total_sum - left_sum - num):
                return i

            # Update left sum by adding the current element
            left_sum += num

        # If no pivot index is found, return -1
        return -1
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Compute total sum | `sum(nums)` | **O(N)** |
| Iterate over `nums` | `for i, num in enumerate(nums)` | **O(N)** |
| **Total Complexity** | **O(N)** |

✅ **Efficient solution** with a single pass approach.  
✅ **Minimal space usage** (only a few variables).  
✅ **Guaranteed correctness** (left sum is always tracked).  

## 🎯 **Why This Approach?**  

- **Uses constant space** (only a few integer variables).
- **Avoids unnecessary recomputation** (sums are updated iteratively).
- **Optimised O(N) solution** instead of brute-force O(N²).

🚀 **With this approach, you can quickly find the pivot index in a single pass!** 🎯  
