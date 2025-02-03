# 🚀 **LeetCode 1502: Can Make Arithmetic Progression From Sequence**

## 📌 **Overview**
This project solves **LeetCode Problem 1502: Can Make Arithmetic Progression From Sequence**.  
The goal is to determine whether the elements of a given array **can be rearranged to form an arithmetic progression**.

### **Problem Statement**
A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.  

Given an array of numbers `arr`, return:
- `True` if the array can be **rearranged** to form an **arithmetic progression**.
- `False` otherwise.

🔹 **Constraints:**
- `2 <= arr.length <= 1000`
- `-10⁶ <= arr[i] <= 10⁶`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: arr = [3, 5, 1]
Output: True
Explanation:
- We can reorder `[3,5,1]` as `[1,3,5]` or `[5,3,1]`.
- Both have a common difference of `2` and `-2`, respectively.
```

### **Example 2**
```python
Input: arr = [1, 2, 4]
Output: False
Explanation:
- No way to reorder `[1,2,4]` to form an arithmetic progression.
```

### **Example 3**
```python
Input: arr = [7, 3, 5]
Output: True
Explanation:
- We can reorder `[7,3,5]` as `[3,5,7]` with common difference `2`.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **An arithmetic progression** is a sequence where the **difference between adjacent elements is constant**.  
✔ **Sorting the array** and checking the difference between elements is one approach, but we can **optimise further**.  
✔ Instead of sorting, we can:
  - Compute the **expected common difference**.
  - Use a **set for quick lookups**.
  - Verify that all expected elements exist.

## 🧠 **Intuition Behind the Approach**
1. **Find the minimum and maximum elements** of the array.
2. **Compute the expected common difference**:
   - If the array can form an arithmetic progression, the difference between consecutive elements should be:  
     \[
     \text{diff} = \frac{\text{max} - \text{min}}{n - 1}
     \]
3. **Check if all expected elements exist**:
   - Create a **set from `arr`** for quick lookups.
   - Iterate from `min` to `max` in steps of `diff`, ensuring each element exists.

## 📝 **Step-by-Step Approach**
### **1️⃣ Compute Key Values**
- **Find `min(arr)`, `max(arr)`, and `n` (length of array).**
- **Compute the expected `diff`.**

### **2️⃣ Handle Edge Cases**
- If `diff == 0`, all elements **must be the same**.

### **3️⃣ Check for Missing Elements**
- Use a **set** for `O(1)` lookups.
- Verify that **all expected elements exist**.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Can Make Arithmetic Progression From Sequence' problem.

    The function `canMakeArithmeticProgression` determines whether the elements of a given array
    can be rearranged to form an arithmetic progression.
    """

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Determines if the given array can be rearranged to form an arithmetic progression.

        :param arr: List of integers.
        :return: `True` if the array can be rearranged into an arithmetic progression, otherwise `False`.
        """
        minimum = min(arr)          # Find the minimum element
        maximum = max(arr)          # Find the maximum element
        n = len(arr)

        # Calculate common difference
        diff = (maximum - minimum) // (n - 1)
        nums = set(arr)             # Convert list to set for quick lookups

        # Special case: If all elements are the same, the sequence is trivially arithmetic
        if diff == 0:
            return len(nums) == 1
        
        # Check if each expected element in the arithmetic progression exists in the set
        for i in range(minimum, maximum + 1, diff):
            if i not in nums:
                return False        # Missing element, cannot form arithmetic progression

        return True                 # All elements found, valid arithmetic progression


def main():
    """
    Demonstrates testing the canMakeArithmeticProgression function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 5, 1],          # Expected: True (can be rearranged to [1,3,5])
        [1, 2, 4],          # Expected: False (no valid arithmetic progression)
        [7, 3, 5],          # Expected: True (can be rearranged to [3,5,7])
        [1, 1, 1, 1],       # Expected: True (all elements are the same)
        [10, 20, 30]        # Expected: True (already in arithmetic progression)
    ]

    for arr in test_cases:
        print(f"Input: {arr}")
        result = solver.canMakeArithmeticProgression(arr)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Using Set Lookups (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- We **find min and max in O(n)**.
- **Set operations** (`O(1) per lookup`) make checking efficient.
- **Total complexity remains O(n).**

## 🏗 **Project Structure**
```
1502. Can Make Arithmetic Progression From Sequence/
├── arithmetic_progress.py    # Python implementation of the solution
├── README.md                 # Detailed explanation & walkthrough
```

✨ **Master arithmetic sequences with efficient set-based logic!** 🚀  

## 🎯 **Why This Solution?**
✔ **Avoids unnecessary sorting (`O(n log n)`)**  
✔ **Uses sets for `O(1)` lookups** instead of iterating multiple times  
✔ **Handles edge cases effectively** (e.g., all elements the same)  
✔ **Efficient and scalable for larger inputs**  

🔥 Now it's **clean, structured, and ready for your portfolio or coding practice!** 🚀😊 Let me know if you'd like any refinements, Legend!