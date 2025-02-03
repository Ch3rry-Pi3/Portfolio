# 🚀 **LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray**

## 📌 **Overview**
This project solves **LeetCode Problem 3105: Longest Strictly Increasing or Strictly Decreasing Subarray**.  
The goal is to determine the **length of the longest contiguous subarray** in `nums` that is either **strictly increasing** or **strictly decreasing**.

### **Problem Statement**
Given an array `nums`, return:
- The **length** of the longest contiguous subarray that is **either strictly increasing or strictly decreasing**.

🔹 **Constraints:**
- `1 <= nums.length <= 100`
- `-10⁹ <= nums[i] <= 10⁹`
- The array may contain **duplicates**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1, 4, 3, 3, 2]
Output: 2
Explanation:
- The strictly increasing subarrays are: `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[1, 4]`
- The strictly decreasing subarrays are: `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, `[4,3]`
- The longest strictly increasing or decreasing subarray has length **2**.
```

### **Example 2**
```python
Input: nums = [3, 3, 3, 3]
Output: 1
Explanation:
- No strictly increasing or decreasing subarrays longer than **1** exist.
- Hence, return **1**.
```

### **Example 3**
```python
Input: nums = [3, 2, 1]
Output: 3
Explanation:
- The strictly increasing subarrays are: `[3]`, `[2]`, `[1]`
- The strictly decreasing subarrays are: `[3]`, `[2]`, `[1]`, `[3, 2]`, `[2, 1]`, `[3, 2, 1]`
- The longest strictly decreasing subarray is `[3, 2, 1]` of length **3**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **A subarray is a contiguous part of an array**, meaning elements must be adjacent.  
✔ The problem requires **either strictly increasing or strictly decreasing subarrays**, but **not mixed trends**.  
✔ If two consecutive elements are **equal**, the sequence is broken and must restart.  
✔ We need to **efficiently track trends (increasing or decreasing)** while iterating.

## 🧠 **Intuition Behind the Approach**
We traverse the array and track:
1. **Current subarray length** (`current`) – how long the current increasing/decreasing sequence is.
2. **Max subarray length** (`result`) – the longest sequence found so far.
3. **Trend direction** (`increasing`):
   - `1` → Currently in an increasing sequence.
   - `-1` → Currently in a decreasing sequence.
   - `0` → No active sequence (resets on duplicates).

## 📝 **Step-by-Step Approach**
### **1️⃣ Iterate Through `nums`**
- Compare each `nums[i]` with `nums[i-1]`:
  - If `nums[i] > nums[i-1]` → **Increasing trend** (extend or reset `current`).
  - If `nums[i] < nums[i-1]` → **Decreasing trend** (extend or reset `current`).
  - If `nums[i] == nums[i-1]` → **Reset `current` to 1** (sequence breaks).
- Update `result` with the max found length.

### **2️⃣ Example Walkthrough (nums = [3, 2, 1])**
| Index | `nums[i-1]` | `nums[i]` | Trend  | Current Length | Max Length (`result`) |
|--------|------------|----------|--------|----------------|------------------------|
| 1      | 3         | 2        | 🔽 Decreasing | 2 | 2 |
| 2      | 2         | 1        | 🔽 Decreasing | 3 | 3 |

✔ **Final max length is `3`**, so return `3`.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Longest Strictly Increasing or Strictly Decreasing Subarray' problem.

    The function `longestMonotonicSubarray` finds the length of the longest contiguous subarray that is either
    strictly increasing or strictly decreasing.
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Determines the length of the longest strictly increasing or strictly decreasing subarray.

        :param nums: List of integers.
        :return: Length of the longest monotonic subarray.
        """
        current = result = 1  # Tracks current subarray length and max length found
        increasing = 0  # 1 for increasing, -1 for decreasing, 0 for neutral (start)

        # Iterate through the list to find the longest monotonic subarray
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:                               # Case 1: Increasing sequence
                current = current + 1 if increasing == 1 else 2     # Extend or reset count
                increasing = 1                                      # Mark increasing trend
            elif nums[i] < nums[i - 1]:                             # Case 2: Decreasing sequence
                current = current + 1 if increasing == -1 else 2    # Extend or reset count
                increasing = -1                                     # Mark decreasing trend
            else:                                                   # Case 3: Equal values, reset tracking
                current = 1
                increasing = 0                                      # Reset trend indicator

            result = max(result, current)                           # Update max length if needed

        return result


def main():
    """
    Demonstrates testing the longestMonotonicSubarray function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1, 4, 3, 3, 2],            # Expected: 2
        [3, 3, 3, 3],               # Expected: 1
        [3, 2, 1],                  # Expected: 3
        [1, 2, 3, 2, 1],            # Expected: 3
        [5, 6, 7, 8, 9]             # Expected: 5
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.longestMonotonicSubarray(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterating through `nums`** | **O(n)** ✅ | **O(1)** ✅ |

- We iterate **once** through `nums`, making it **O(n)**.
- No extra space is used apart from variables, making it **O(1)**.

## 🏗 **Project Structure**
```
3105. Longest Strictly Increasing or Strictly Decreasing Subarray/
├── longest_inc_dec_subarray.py    # Python implementation of the solution
├── README.md                      # Detailed explanation & walkthrough
```

✨ **Master monotonic subarrays with efficient logic!** 🚀  
