# 🚀 **LeetCode 1752: Check if Array Is Sorted and Rotated**

## 📌 **Overview**
This project solves **LeetCode Problem 1752: Check if Array Is Sorted and Rotated**.  
The goal is to determine whether an array was originally **sorted in non-decreasing order** and then **rotated some number of positions** (including zero).

### **Problem Statement**
Given an array `nums`, return:
- `True` if the array is a **rotated version of a sorted array**.
- `False` otherwise.

🔹 **Constraints:**
- `1 <= nums.length <= 100`
- `-10⁹ <= nums[i] <= 10⁹`
- The array may contain **duplicates**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [3, 4, 5, 1, 2]
Output: True
Explanation:
- The original sorted array was `[1, 2, 3, 4, 5]`.
- It was rotated **3 positions** to become `[3, 4, 5, 1, 2]`.
- Since this matches a valid rotation, return `True`.
```

### **Example 2**
```python
Input: nums = [2, 1, 3, 4]
Output: False
Explanation:
- The array cannot be rotated into any sorted order.
- Return `False`.
```

### **Example 3**
```python
Input: nums = [1, 2, 3]
Output: True
Explanation:
- The array is already sorted.
- A **0-position rotation** means it remains `[1, 2, 3]`.
- Return `True`.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ A **valid sorted array** should have at most **one drop** in value when traversed circularly.  
✔ If there are **two or more drops**, the array **cannot be a rotation of a sorted sequence**.  
✔ A **single-element array** is always **sorted and rotated** (`True`).  

## 🧠 **Intuition Behind the Approach**
We can visualise the problem as a **sliding window search** over a **concatenated version of the array**.

### **Step 1: Conceptualising the Sliding Window**
- **Concatenate** `nums` with itself to simulate **all possible rotations**.
- We then check if **any subarray of length `n` is sorted**.
  
**Example:**
```python
nums = [3, 4, 5, 1, 2]
concatenated = [3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
```
Now, we scan every subarray of length `n = 5`:
| Subarray  | Sorted? |
|-----------|--------|
| `[3, 4, 5, 1, 2]` | ❌ No |
| `[4, 5, 1, 2, 3]` | ❌ No |
| `[5, 1, 2, 3, 4]` | ❌ No |
| `[1, 2, 3, 4, 5]` | ✅ Yes → **Return True** |

### **Step 2: Optimising with Modulo**
Instead of physically **concatenating** the array (which takes extra space), we use **modulo indexing** to **simulate** this behavior.

- We maintain two **pointers** that iterate over the array using `% n` indexing.
- This allows us to **wrap around** without storing the duplicate array.

🔹 **Example Modulo Trick**  
Instead of creating:
```python
concatenated = [3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
```
We use:
```python
nums[i % n]
```
- `5 % 5 = 0 → nums[0] = 3`
- `7 % 5 = 2 → nums[2] = 5`
- `9 % 5 = 4 → nums[4] = 2`

This ensures we **cycle through** without extra space!

## 📝 **Step-by-Step Approach**
### **1️⃣ Traverse the Array Circularly**
- Iterate through the list **twice** to simulate rotation.
- Check for **non-decreasing order** while looping.
- If a valid sorted sequence is found within **N elements**, return `True`.

### **2️⃣ Example Walkthrough (nums = [3, 4, 5, 1, 2])**
| Index | `nums[i-1]` | `nums[i]` | Order Maintained? |
|--------|------------|----------|------------------|
| 1      | 3         | 4        | ✅ Yes |
| 2      | 4         | 5        | ✅ Yes |
| 3      | 5         | 1        | ❌ No (drop found) |
| 4      | 1         | 2        | ✅ Yes |

✔ **Only one drop** → Valid rotation → Return `True`.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Check if Array Is Sorted and Rotated' problem.

    The function `check` determines whether a given array was originally sorted in 
    non-decreasing order and then rotated some number of positions (including zero).
    """

    def check(self, nums: List[int]) -> bool:
        """
        Determines whether the given array is a rotated version of a sorted array.

        :param nums: List of integers.
        :return: `True` if the array is sorted and rotated, otherwise `False`.
        """
        N = len(nums)
        count = 1                   # Keeps track of consecutive non-decreasing elements

        # Iterate through the array in a circular manner (2 * N iterations to check all rotations)
        for i in range(1, 2 * N):
            if nums[(i - 1) % N] <= nums[i % N]:  
                count += 1          # Maintain increasing order
            else:
                count = 1           # Reset count if order breaks

            if count == N:          # If we found a full cycle maintaining order
                return True
        
        return N == 1               # Single-element arrays are trivially sorted and rotated


def main():
    """
    Demonstrates testing the check function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [3, 4, 5, 1, 2],  # Expected: True
        [2, 1, 3, 4],     # Expected: False
        [1, 2, 3],        # Expected: True
        [6, 10, 6],       # Expected: True (Duplicate elements allowed)
        [1],              # Expected: True (Single element is always sorted)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.check(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterating through `nums`** | **O(n)** ✅ | **O(1)** ✅ |

## 🏗 **Project Structure**
```
1752. Check if Array Is Sorted and Rotated/
├── check_sorted_rotated.py    # Python implementation of the solution
├── README.md                  # Detailed explanation & walkthrough
```

✨ **Master rotation-based problems with efficient logic!** 🚀  