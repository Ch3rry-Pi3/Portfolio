# 🚀 **LeetCode 896: Monotonic Array**

## 📌 **Overview**
This project solves **LeetCode Problem 896: Monotonic Array**.  
The goal is to determine whether an array is **monotonic**, meaning it is either entirely **non-increasing** or **non-decreasing**.

### **Problem Statement**
An array is **monotonic** if it is either:
- **Monotonic Increasing** → Each element is **greater than or equal** to the previous one.
- **Monotonic Decreasing** → Each element is **less than or equal** to the previous one.

Given an array `nums`, return:
- `True` if `nums` is **monotonic**.
- `False` otherwise.

🔹 **Constraints:**
- `1 <= nums.length <= 10⁵`
- `-10⁵ <= nums[i] <= 10⁵`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1, 2, 2, 3]
Output: True
Explanation:
- The array is **monotonic increasing** because `1 ≤ 2 ≤ 2 ≤ 3`.
```

### **Example 2**
```python
Input: nums = [6, 5, 4, 4]
Output: True
Explanation:
- The array is **monotonic decreasing** because `6 ≥ 5 ≥ 4 ≥ 4`.
```

### **Example 3**
```python
Input: nums = [1, 3, 2]
Output: False
Explanation:
- The array **increases, then decreases**, so it is **not monotonic**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **A monotonic array must be entirely increasing or entirely decreasing.**  
✔ **Duplicate elements are allowed.**  
✔ **If an array has only one element, it is trivially monotonic.**  
✔ **An `O(n)` single-pass check is sufficient for large inputs.**  

## 🧠 **Intuition Behind the Approach**
### **1️⃣ Check for Increasing or Decreasing Trend**
- Iterate through `nums` and **compare adjacent elements**.
- Track whether the array is **monotonic increasing** or **monotonic decreasing**.
- If both conditions are violated, return `False`.

### **2️⃣ Example Walkthrough (`nums = [1, 2, 2, 3]`)**
| Step | `nums[i]` | `nums[i+1]` | Comparison | Monotonic? |
|------|----------|------------|------------|------------|
| 1    | `1`      | `2`        | ✅ `1 ≤ 2` | Increasing ✅ |
| 2    | `2`      | `2`        | ✅ `2 ≤ 2` | Increasing ✅ |
| 3    | `2`      | `3`        | ✅ `2 ≤ 3` | Increasing ✅ |

✔ **Since no decreasing pair was found, return `True`.**

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Monotonic Array' problem.

    The function `isMonotonic` checks whether a given array is monotonic,
    meaning it is either entirely non-increasing or non-decreasing.
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Determines if the given array is monotonic.

        :param nums: List of integers.
        :return: `True` if `nums` is monotonic, otherwise `False`.
        """
        # Reverse the list if it is decreasing
        if nums[-1] - nums[0] < 0:
            nums.reverse()

        # Check if the array is non-decreasing
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:       # A decreasing pair breaks monotonicity
                return False

        return True                         # If no violations were found, the array is monotonic


def main():
    """
    Demonstrates testing the isMonotonic function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 2, 2, 3],           # Expected: True (Monotonic increasing)
        [6, 5, 4, 4],           # Expected: True (Monotonic decreasing)
        [1, 3, 2],              # Expected: False (Not monotonic)
        [1, 1, 1, 1],           # Expected: True (All elements are the same)
        [10, 20, 30],           # Expected: True (Strictly increasing)
        [30, 20, 10],           # Expected: True (Strictly decreasing)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.isMonotonic(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Single-pass check (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- We **iterate through `nums` once**, making it **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
896. Monotonic Array/
├── monotonic_array.py    # Python implementation of the solution
├── README.md             # Detailed explanation & walkthrough
```

✨ **Master monotonic array detection with an efficient `O(n)` check!** 🚀  