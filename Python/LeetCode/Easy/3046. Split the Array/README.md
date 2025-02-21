# 🎉 **LeetCode 3046: Split the Array**  

## 📌 **Problem Overview**  
You are given an **integer array** `nums` of **even length**. You must split the array into **two equal parts**, `nums1` and `nums2`, such that:  
1. **Both subarrays have the same length:** 

   \[
   \text{len(nums1)} = \text{len(nums2)} = \frac{\text{len(nums)}}{2}
   \]

2. **All elements in `nums1` are distinct.**  
3. **All elements in `nums2` are distinct.**  

Return **`True`** if it's **possible** to split the array, otherwise return **`False`**.

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: nums = [1,1,2,2,3,4]  
Output: True  
```
✅ One possible way to split the array:  
- `nums1 = [1,2,3]`
- `nums2 = [1,2,4]`  

Since both contain **distinct** elements, the split is **valid**.

### **Example 2**  
```python
Input: nums = [1,1,1,1]  
Output: False  
```
❌ The only possible split is:  
- `nums1 = [1,1]`
- `nums2 = [1,1]`  

Since both `nums1` and `nums2` do **not** contain distinct elements, the split is **invalid**.

## 🚀 **Approach Explanation**  

### **1️⃣ Key Observations**  
- Since both `nums1` and `nums2` must have **distinct elements**, **no number can appear more than twice** in `nums`.  
- If **any number appears more than twice**, **it's impossible** to split the array.  
- Otherwise, a valid split is **always possible**.

### **2️⃣ Efficient Solution Using a Frequency Counter**  
We use **Python’s `Counter`** to count the occurrences of each number:  
- If any number appears **more than twice**, return `False`.  
- Otherwise, return `True`.

## 📝 **Python Solution**  
```python
from collections import Counter
from typing import List

class Solution:
    """
    Solution class to check if an array can be split into two parts 
    with distinct elements.
    """

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        """
        Determines whether the given array can be split into two equal-length 
        subarrays containing distinct elements.

        The approach uses a frequency counter:
        - If any element appears more than twice, it is impossible to split the array.
        - Otherwise, a valid split is always possible.

        Args:
            nums (List[int]): The input array of even length.

        Returns:
            bool: True if the array can be split, False otherwise.
        """

        # Count the occurrences of each element
        counter = Counter(nums)

        # Check if any element appears more than twice
        for frequency in counter.values():
            if frequency > 2:
                return False

        return True
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Counting Elements** | Using `Counter(nums)` | **O(n)** |
| **Checking Frequency** | Iterating over dictionary values | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses a simple frequency check** instead of brute force.  
✔ **Runs in O(n)** time, making it optimal for large inputs.  
✔ **Minimal memory usage**, only storing counts in a dictionary.  

## 📂 **Project Structure**  
```
split_array/
├── split_array.py  # Python solution
├── README.md       # Explanation & approach
```

✨ **Master frequency-based problems with this efficient approach!** 🚀  

This **README** follows the **perfect format** with:  
✅ **Problem Explanation**  
✅ **Examples with Walkthrough**  
✅ **Approach Breakdown**  
✅ **Optimised Python Solution**  
✅ **Complexity Analysis**  

Let me know if you need any **custom modifications**! 🚀🔥