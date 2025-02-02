# 🚀 LeetCode 66: Plus One

## 📌 Overview
This project provides a solution for **LeetCode Problem 66: Plus One**.
The task is to increment an integer represented as an **array of digits** by one and return the resulting array.

### **Problem Statement**
Given an array `digits` where each element represents a digit of an integer:
- The digits are stored in **left-to-right order** (most significant to least significant).
- The array **does not** contain any leading zeroes.

**Return** the array after incrementing the integer by one.

🔹 **Constraints:**
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`

## 🎯 Example Walkthrough

### **Example 1**
```python
Input: digits = [1,2,3]
Output: [1,2,4]
```
💡 **Explanation:** The number `123` is incremented by `1`, resulting in `124`.

### **Example 2**
```python
Input: digits = [9,9,9]
Output: [1,0,0,0]
```
💡 **Explanation:** The number `999` is incremented by `1`, resulting in `1000`.
A new digit `1` is added at the beginning.

### **Example 3**
```python
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
```
💡 **Explanation:** The number `4321` is incremented by `1`, resulting in `4322`.

## 🚀 Understanding the Problem
### **Key Observations**
✔ The last digit is incremented unless it is `9`.
✔ If a `9` is encountered, it turns into `0`, and we continue carrying over the `1`.
✔ If all digits are `9`, a new `1` is added at the front (e.g., `999 → 1000`).

## 📝 Step-by-Step Approach

### **1️⃣ Reverse the List**
We **reverse** the list to process the least significant digit first.

### **2️⃣ Add One to the First Digit**
We **initialise a carry** of `1` (since we're adding `1`). We iterate over the digits:
- If a digit is `9`, we turn it into `0` and **carry** the `1`.
- Otherwise, we **increment the digit** and set `carry = 0` to stop further processing.

### **3️⃣ Handle Extra Carry**
If, after processing all digits, **carry is still 1**, we append `1` to the end.

### **4️⃣ Reverse Back the List**
Since we processed from least to most significant, we **reverse** back to the original order.

## 🏗 Implementation
```python
from typing import List

class Solution:
    """
    Solution class for the 'Plus One' problem.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the given list of digits by one.

        :param digits: List of integers representing a number.
        :return: A new list representing the incremented number.
        """
        digits = digits[::-1]           # Reverse to process from least to most significant
        carry, i = 1, 0                 # Start with carry set to 1 since we are adding one

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0       # Set current digit to 0 if it's 9, propagate carry
                else:
                    digits[i] += 1      # Simply increment the digit if it's not 9
                    carry = 0           # Carry handled, so stop
            else:
                digits.append(1)        # If carry still remains, add a new digit at the end
                carry = 0
            i += 1                      # Move to the next digit
        
        return digits[::-1]             # Reverse back to original order
```

## ⏳ Time Complexity Analysis
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterate through digits** | **O(n)** ✅ | **O(1)** ✅ |

- **We iterate through the digits at most once**, making it **O(n)**.
- **No extra space is used apart from the input array**, making it **O(1)**.

## 🎯 Summary
✔ **Handles carry propagation efficiently.**
✔ **Does not use extra space beyond input modification.**
✔ **Reversing simplifies processing from least to most significant digit.**

🚀 **Efficient solution for incrementing a list-based integer representation!**
