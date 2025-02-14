# 🏆 LeetCode 2239: Find Closest Number to Zero

## 📌 Problem Statement
Given an integer array `nums`, return **the number closest to** `0`.  
If there are multiple answers, return **the number with the largest value**.

### 🔹 Constraints:
- `nums` **is non-empty**.
- There will always be at least **one number** in `nums`.

## 🔍 Understanding the Problem

We need to:
1. **Find the number whose absolute value is closest to zero**.
2. **If there is a tie (same absolute value), return the larger number**.

💡 **Example Insight**  
Consider the array `[-4, -2, 1, 4, 8]`:
- The absolute distances from `0` are `[4, 2, 1, 4, 8]`.
- The closest number is `1`.

For `nums = [2, -1, 1]`:
- The closest numbers are `1` and `-1`.
- Since `1` is larger, we return `1`.

## 📝 Examples

### **Example 1**
#### **Input:**
```python
nums = [-4, -2, 1, 4, 8]
```
#### **Output:**
```python
1
```
#### **Explanation:**
- The distances from `0` are `[4, 2, 1, 4, 8]`.
- The closest number is `1`.

### **Example 2**
#### **Input:**
```python
nums = [2, -1, 1]
```
#### **Output:**
```python
1
```
#### **Explanation:**
- Both `1` and `-1` are equally close to `0`.
- We return `1` since it is larger.

## 🚀 Approach

### **1️⃣ Brute Force Approach**
- Iterate over each number.
- Track the closest number based on absolute distance.
- If there’s a tie, pick the larger number.

### **2️⃣ Optimised Approach (One Pass)**
✅ **Key Observations:**
- If `|num|` is smaller than `|closest|`, update `closest`.
- If `|num|` is equal to `|closest|`, update `closest` **only if `num` is larger**.

⏳ **Time Complexity:** `O(n)`  
📦 **Space Complexity:** `O(1)`

## 💡 Python Solution

```python
from typing import List

class Solution:
    """
    A class to find the closest number to zero in a list.
    If multiple numbers have the same distance to zero, the largest number is returned.
    """

    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Finds the closest number to zero from a given list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The number closest to zero. If multiple numbers have the same 
                 distance, return the larger number.
        """
        # Initialize 'closest' with the first element in the list
        closest = nums[0]

        # Iterate through the list to find the closest number to zero
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num

        return closest
```

## 🏆 Why This Works
✔ **Handles positive and negative numbers**  
✔ **Ensures the larger number is returned in case of a tie**  
✔ **Efficient, single pass approach (`O(n)`)**  

🎯 **Now your solution is clean, readable, and efficient!** 🚀