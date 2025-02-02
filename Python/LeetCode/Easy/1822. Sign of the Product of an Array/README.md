# 🚀 **LeetCode 1822: Sign of the Product of an Array**

## 📌 **Overview**
This project solves **LeetCode Problem 1822: Sign of the Product of an Array**.
The task is to determine the **sign** of the product of all elements in an integer array **without explicitly calculating the product**.

### **Problem Statement**
Given an integer array `nums`, return:
- `1` if the **product** of all numbers is **positive**.
- `-1` if the **product** of all numbers is **negative**.
- `0` if **any number in the array is `0`** (since multiplying by `0` results in `0`).

🔹 **Constraints:**
- `1 <= nums.length <= 1000`
- `-100 <= nums[i] <= 100`
- The product of any prefix or suffix of `nums` will **fit in a 32-bit integer**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [-1, -2, -3, -4, 3, 2, 1]
Output: 1
```
🔹 **Explanation:**
- The product is `(-1) * (-2) * (-3) * (-4) * 3 * 2 * 1 = 144`.
- Since `144 > 0`, we return `1`.

### **Example 2**
```python
Input: nums = [1, 5, 0, 2, -3]
Output: 0
```
🔹 **Explanation:**
- The product contains `0`, making the result `0`.

### **Example 3**
```python
Input: nums = [-1, 1, -1, 1, -1]
Output: -1
```
🔹 **Explanation:**
- The product is `(-1) * 1 * (-1) * 1 * (-1) = -1`.
- Since `-1 < 0`, we return `-1`.

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ Multiplication can result in **large numbers**, so we avoid directly computing the product.
✔ The **sign of the product** depends on:
  - If **any number is `0`**, return `0` immediately.
  - Count how many **negative numbers** exist:
    - If **odd**, return `-1` (negative product).
    - If **even**, return `1` (positive product).

## 📝 **Step-by-Step Approach**
### **1️⃣ Iterate Through the Array**
- Initialise `negatives = 0`.
- Traverse `nums`:
  - If `nums[i] == 0`, return `0` immediately.
  - If `nums[i] < 0`, increment `negatives`.

### **2️⃣ Determine the Result**
- If `negatives` count is **even**, return `1`.
- If `negatives` count is **odd**, return `-1`.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Sign of the Product of an Array' problem.
    
    The `arraySign` method determines the sign of the product of an integer array without
    computing the product explicitly.
    """

    def arraySign(self, nums: List[int]) -> int:
        """
        Determines the sign of the product of all elements in the array.

        :param nums: List of integers.
        :return:
            - 1 if the product is positive.
            - -1 if the product is negative.
            - 0 if the product is zero.
        """
        negatives = 0                           # Count of negative numbers

        for n in nums:
            if n == 0:                          # If any number is zero, the product is zero
                return 0
            negatives += (1 if n < 0 else 0)    # Count negative numbers

        return -1 if negatives % 2 else 1       # Even negatives = positive, odd negatives = negative


def main():
    """
    Demonstrates testing the arraySign function on multiple test cases.
    """
    solver = Solution()

    test_cases = [
        ([-1, -2, -3, -4, 3, 2, 1], 1),   # Product is positive (144)
        ([1, 5, 0, 2, -3], 0),            # Product is zero
        ([-1, 1, -1, 1, -1], -1)          # Product is negative (-1)
    ]

    for nums, expected in test_cases:
        result = solver.arraySign(nums)
        print(f"Input: {nums} -> Output: {result} | Expected: {expected}")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterating through `nums`** | **O(n)** ✅ | **O(1)** ✅ |

- **We iterate through `nums` once**, making the approach **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
1822. Sign of the Product of an Array/
├── sign_product_array.py    # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Master sign-based problems with efficient logic!** 🚀

