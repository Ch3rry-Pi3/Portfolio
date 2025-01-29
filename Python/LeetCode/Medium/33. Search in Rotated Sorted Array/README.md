# 🔍 **LeetCode 33: Search in Rotated Sorted Array**

## 📌 **Overview**

This project solves **LeetCode Problem 33: Search in Rotated Sorted Array** using an **optimized binary search approach** that runs in **O(log n) time complexity**.

### **Problem Statement**

You are given an array `nums` that was originally sorted in ascending order but then **rotated at an unknown pivot**.

Given the rotated sorted array `nums` and an integer `target`, return **the index of **`target`** if it is in **`nums`**, or **`-1`** if it is not in**`nums`.

🔹 **Constraints:**

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values in `nums` are **distinct**.

## 🎯 **Example Walkthrough**

### **Example 1**

```python
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Explanation: Target `0` is at index `4`.
```

### **Example 2**

```python
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
Explanation: Target `3` is not in the array.
```

### **Example 3**

```python
Input: nums = [1], target = 0
Output: -1
Explanation: Target `0` is not in the array.
```

## 🚀 **How It Works: Optimised Binary Search**

### **Intuition**

Since the array was originally sorted but then rotated, **binary search** can still be applied if we first determine which portion of the array (left or right) is **sorted**. This allows us to **eliminate half of the search space in each iteration**.

### **Algorithm Steps**

1️⃣ **Initialise variables:**

- `left = 0`, `right = len(nums) - 1`: Define binary search boundaries.

2️⃣ **Binary Search:**

- **Find the middle index** → `middle = (left + right) // 2`.
- **Check if **`nums[middle]`** is the target**.
- **Determine which half is sorted:**
  - If `nums[left] <= nums[middle]`, the **left half is sorted**.
  - Otherwise, the **right half is sorted**.
- **Narrow the search:**
  - If the target is **within the sorted half**, search within it.
  - Otherwise, search the **unsorted half**.

3️⃣ **Return index if found, otherwise return **`-1`**.

### **Step-by-Step Example Walkthrough**

Let's walk through the binary search process for:

```python
nums = [5, 6, 7, 1, 2, 3, 4], target = 3
```

#### **Initial Conditions**

| Step | Left | Right | Middle | nums[Middle] | Action                    |
| ---- | ---- | ----- | ------ | ------------ | ------------------------- |
| 1    | 0    | 6     | 3      | `1`          | Check right half          |
| 2    | 4    | 6     | 5      | `3`          | Found target → return `5` |

#### **Explanation:**

1️⃣ **First Iteration:**

- `left = nums[0] = 5`, `right = nums[6] = 4`, `middle[3] = 1`
- Since `nums[middle] < nums[right]`, we are in the **right-sorted** **portion** of the array.
- Since `target (3)` is in `[1, 2, 3, 4]`, search in this half (`left = middle + 1`).

2️⃣ **Second Iteration:**

- `left = nums[4] = 2`, `right = nums[6] = 4`, `middle = nums[5] = 3`
- `nums[middle]` **matches the target**, return `5`.

### **Implementation**

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        :param nums: List of unique integers sorted in ascending order but rotated
        :param target: The integer value to search for
        :return: The index of the target in nums, or -1 if not found
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if target == nums[middle]:
                return middle
            
            # Determine if we are in the left-sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1  # Search right portion
                else:
                    right = middle - 1  # Search left portion
            
            # Otherwise, we are in the right-sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1  # Search left portion
                else:
                    left = middle + 1  # Search right portion
        
        return -1  # Target not found
```

## ⏳ **Time Complexity Analysis**

| Approach                            | Time Complexity | Space Complexity |
| ----------------------------------- | --------------- | ---------------- |
| **Brute Force (scan entire array)** | **O(n)** ❌      | **O(1)** ✅       |
| **Optimised Binary Search**         | **O(log n)** ✅  | **O(1)** ✅       |

- **Brute force** checks every element, making it **slow for large arrays**.
- **Binary search** eliminates **half of the search space per iteration**, making it **fast and efficient**.

## 🏗 **Project Structure**

```
33. Search in Rotated Sorted Array/
├── search_rotated_sorted_array.py  # Efficient O(log n) solution using binary search
├── README.md                        # Detailed explanation
```

### 📝 **`search_rotated_sorted_array.py`**

- **Implements an O(log n) binary search solution.**
- **Handles cases where the array is already sorted.**

```python
def main():
    """
    Demonstrates searching for a target in rotated sorted arrays for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),  # Expected output: 4
        ([4, 5, 6, 7, 0, 1, 2], 3),  # Expected output: -1
        ([1], 0),                    # Expected output: -1
        ([1, 3], 3),                 # Expected output: 1
        ([5, 1, 3], 3),              # Expected output: 2
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}")
        result = solver.search(nums, target)
        print(f"Target Index: {result}\n")

if __name__ == "__main__":
    main()
```

**🚀 Master binary search with this efficient approach!**

