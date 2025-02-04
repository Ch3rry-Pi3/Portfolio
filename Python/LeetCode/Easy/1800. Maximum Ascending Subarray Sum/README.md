# 🚀 **LeetCode 1800: Maximum Ascending Subarray Sum**

## 📌 **Overview**
This project solves **LeetCode Problem 1800: Maximum Ascending Subarray Sum**.  
The goal is to determine the **maximum possible sum of a contiguous ascending subarray** in `nums`.

### **Problem Statement**
A **subarray** is defined as a contiguous sequence of numbers in an array.  
A **subarray is ascending** if for every index `i`:
\[
nums[i] < nums[i+1]
\]
  
Given an array of positive integers `nums`, return:
- The **maximum sum** of an **ascending subarray**.

🔹 **Constraints:**
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [10, 20, 30, 5, 10, 50]
Output: 65
Explanation:
- The ascending subarray `[10,50]` has the maximum sum of **65**.
```

### **Example 2**
```python
Input: nums = [10, 20, 30, 40, 50]
Output: 150
Explanation:
- The entire array `[10,20,30,40,50]` is already ascending.
- Its sum is **150**.
```

### **Example 3**
```python
Input: nums = [12, 17, 15, 13, 10, 11, 12]
Output: 33
Explanation:
- The ascending subarray `[10,11,12]` has the maximum sum of **33**.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **A subarray is contiguous**, meaning elements must be adjacent.  
✔ The problem requires finding the **maximum sum of an increasing subarray**.  
✔ If an element is **smaller than or equal to the previous**, the subarray **resets**.  
✔ We must **track the highest sum** while traversing the array.

## 🧠 **Intuition Behind the Approach**
### **1️⃣ Traverse `nums` and Track an Ascending Sum**
- Iterate through `nums` while keeping track of the **current ascending subarray sum**.
- If `nums[i] > nums[i-1]`, **add** `nums[i]` to the current sum.
- If `nums[i] <= nums[i-1]`, **reset** the current sum.

### **2️⃣ Continuously Update the Maximum Found**
- **Maintain `result`**, which stores the **highest sum encountered**.
- If a new ascending subarray starts, compare and **update `result`**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Initialise Tracking Variables**
- `current` → stores the current ascending subarray sum.
- `result` → stores the **maximum** ascending sum found so far.

### **2️⃣ Iterate Over `nums`**
- **If `nums[i] > nums[i-1]`** → continue summing (`current += nums[i]`).
- **If `nums[i] <= nums[i-1]`** → reset (`current = nums[i]`).
- **Always update `result`**.

### **3️⃣ Example Walkthrough (`nums = [10, 20, 30, 5, 10, 50]`)**
| Index | `nums[i-1]` | `nums[i]` | Action        | `current` Sum | `result` Max |
|--------|------------|----------|--------------|--------------|--------------|
| 1      | 10         | 20       | **Add**      | 30           | 30           |
| 2      | 20         | 30       | **Add**      | 60           | 60           |
| 3      | 30         | 5        | **Reset**    | 5            | 60           |
| 4      | 5          | 10       | **Add**      | 15           | 60           |
| 5      | 10         | 50       | **Add**      | 65           | **65** ✅ |

✔ **Final max sum is `65`**, so return **`65`**.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Maximum Ascending Subarray Sum' problem.

    The function `maxAscendingSum` finds the maximum possible sum of an ascending subarray in `nums`.
    """

    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Determines the maximum sum of a contiguous ascending subarray.

        :param nums: List of positive integers.
        :return: The maximum sum of any strictly increasing subarray.
        """
        current = nums[0]                       # Initialise current subarray sum
        result = current                        # Initialise maximum found sum

        # Iterate through the array, tracking ascending subarrays
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:           # Continue ascending subarray
                current += nums[i]
            else:  # Reset sum if order breaks
                current = nums[i]

            result = max(result, current)       # Update max sum found

        return result


def main():
    """
    Demonstrates testing the maxAscendingSum function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [10, 20, 30, 5, 10, 50],            # Expected: 65
        [10, 20, 30, 40, 50],               # Expected: 150
        [12, 17, 15, 13, 10, 11, 12],       # Expected: 33
        [5, 5, 5, 5],                       # Expected: 5 (no increasing subarray)
        [1, 2, 3, 4, 5, 6],                 # Expected: 21 (entire array is ascending)
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.maxAscendingSum(nums)
        print(f"Output: {result}\n")


if __name__ == "__main__":
    main()
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Iterating through `nums`** | **O(n)** ✅ | **O(1)** ✅ |

- **We iterate through `nums` once**, making it **O(n)**.
- **No extra space** is used apart from variables, making it **O(1)**.

## 🏗 **Project Structure**
```
1800. Maximum Ascending Subarray Sum/
├── max_asc_subarray_sum.py    # Python implementation of the solution
├── README.md                  # Detailed explanation & walkthrough
```

✨ **Master ascending subarrays with efficient logic!** 🚀  
