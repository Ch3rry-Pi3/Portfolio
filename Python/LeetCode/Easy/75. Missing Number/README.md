# 🚀 **LeetCode 268: Missing Number**

## 📌 **Overview**
This project provides a solution to **LeetCode Problem 268: Missing Number**. The problem requires finding the missing integer in an array containing `n` distinct numbers from the range `[0, n]`.

### **Problem Statement**
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only missing number**.

🔹 **Constraints:**
- `n == nums.length`
- `1 <= n <= 10⁴`
- `0 <= nums[i] <= n`
- All values in `nums` are unique.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [3, 0, 1]
Output: 2
Explanation: The numbers from 0 to 3 should be [0,1,2,3].
              Since 2 is missing, return 2.
```

### **Example 2**
```python
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: The numbers from 0 to 9 should be [0,1,2,3,4,5,6,7,8,9].
              Since 8 is missing, return 8.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ We have `n` numbers, meaning the range **should contain all numbers from `0` to `n`**.
✔ One number is missing, and we need to **find it efficiently**.
✔ A naive solution using sorting or extra storage would take **O(n log n) or O(n) space**, but we can do better!

## 📝 **Step-by-Step Approach**
### **1️⃣ Mathematical Index Sum Approach**
- **Initialise `result = n`**: Since the numbers go from `0` to `n`, the missing value could be `n`.
- **Iterate through `nums`**, adjusting `result` dynamically:
  ```
  result = n
  for i in range(n):
      result += (i - nums[i])
  ```
  - The sum of indices should match the sum of values in `nums`, except for the missing one.
  - By adding `i` and subtracting `nums[i]`, we naturally identify the missing number.

## **Implementation**
```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in the range [0, n] using a mathematical sum approach.

        :param nums: List of distinct numbers from the range [0, n]
        :return: The missing number in the sequence
        """
        result = len(nums)  # Start with n (as it's a possible missing value)

        for i in range(len(nums)):
            result += (i - nums[i])  # Adjust by adding index and subtracting actual value

        return result
```

## **🔍 Step-by-Step Execution**
#### **Example: `nums = [3, 0, 1]`**
✅ **Step 1: Initialise `result = n`**
```python
result = 3
```

✅ **Step 2: Iterate through `nums`**
| `i`  | `nums[i]` | `i - nums[i]` | `result` (updated) |
|------|----------|--------------|------------------|
| 0    | 3        | `0 - 3 = -3`  | `3 + (-3) = 0`  |
| 1    | 0        | `1 - 0 = 1`   | `0 + 1 = 1`     |
| 2    | 1        | `2 - 1 = 1`   | `1 + 1 = 2`     |

✅ **Step 3: Return the final `result = 2`** 🎯
- **`2` is the missing number** in the range `[0, 3]`.

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Sorting & Checking** | **O(n log n)** ❌ | **O(1)** ✅ |
| **Using a HashSet** | **O(n)** ✅ | **O(n)** ❌ |
| **Mathematical Approach** | **O(n)** ✅ | **O(1)** ✅ |

✔ **This approach runs in `O(n)`, making it optimal for large values of `n`.**
✔ **Only `O(1)` extra space is required, making it highly efficient.**

## 🏗 **Project Structure**
```
268. Missing Number/
├── missing_nums.py     # Efficient O(n) sum approach
├── README.md           # Detailed explanation & walkthrough
```

**🚀 Efficiently Find the Missing Number in O(n) Time!**