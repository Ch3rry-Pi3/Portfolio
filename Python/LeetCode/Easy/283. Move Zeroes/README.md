# 🚀 **LeetCode 283: Move Zeroes**

## 📌 **Overview**
This project solves **LeetCode Problem 283: Move Zeroes**.  
The task is to move all `0`s to the end of an array while maintaining the relative order of non-zero elements.

### **Problem Statement**
Given an integer array `nums`, modify it **in-place** such that:
- All `0`s are moved to the **end** of the array.
- The **relative order** of non-zero elements is **preserved**.

🔹 **Constraints:**
- `1 <= nums.length <= 10⁴`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- Must be solved **in-place** (without creating a new array).

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```
**Explanation:**
- Move `1` to the front.
- Move `3` next.
- Move `12` after `3`.
- Append the remaining `0`s to the end.

### **Example 2**
```python
Input: nums = [0, 0, 1]
Output: [1, 0, 0]
```
**Explanation:**
- Move `1` to the front.
- Append both `0`s to the end.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ We **cannot create a new array**, meaning all modifications happen within `nums` itself.
✔ We **must maintain the order** of non-zero elements.
✔ We can solve this **in O(n) time** using the **two-pointer technique**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Two-Pointer Approach**
- Use a **left pointer** (`left`) to track where the next non-zero element should be placed.
- Use a **right pointer** (`right`) to iterate through the array.
- If `nums[right]` is **non-zero**, swap it with `nums[left]`.
- Increment `left` after every swap.

### **2️⃣ Example Walkthrough (nums = [0, 1, 0, 3, 12])**
| Step | `nums` State     | `left` | `right` | Action  |
|------|-----------------|--------|---------|---------|
| 1    | `[0, 1, 0, 3, 12]` | 0      | 0       | -       |
| 2    | `[0, 1, 0, 3, 12]` | 0      | 1       | Swap `0` and `1` |
| 3    | `[1, 0, 0, 3, 12]` | 1      | 2       | Skip `0` |
| 4    | `[1, 0, 0, 3, 12]` | 1      | 3       | Swap `0` and `3` |
| 5    | `[1, 3, 0, 0, 12]` | 2      | 4       | Swap `0` and `12` |
| 6    | `[1, 3, 12, 0, 0]` | 3      | End     | Done!  |

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    Moves all zeroes in an array to the end while preserving the order
    of the non-zero elements.
    """
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Performs in-place modification of `nums`.

        :param nums: List of integers.
        """
        left = 0  # Pointer to track position for non-zero elements
        
        for right in range(len(nums)):
            if nums[right]:         # If element is non-zero
                nums[left], nums[right] = nums[right], nums[left]
                left += 1           # Move left pointer forward

def main():
    """
    Demonstrates testing the moveZeroes function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [0, 1, 0, 3, 12],       # Expected: [1, 3, 12, 0, 0]
        [0, 0, 1],              # Expected: [1, 0, 0]
        [2, 1, 3, 0, 4, 0]      # Expected: [2, 1, 3, 4, 0, 0]
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        solver.moveZeroes(nums)
        print(f"Output: {nums}\n")

if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Two-pointer swap** | **O(n)** ✅ | **O(1)** ✅ |

- **We iterate through `nums` once**, making the approach **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
283. Move Zeroes/
├── move_zeroes.py   # Python implementation of the solution
├── README.md        # Detailed explanation & walkthrough
```

✨ **Master in-place array transformations with efficient logic!** 🚀