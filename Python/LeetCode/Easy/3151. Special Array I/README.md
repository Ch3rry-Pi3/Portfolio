# 🚀 **LeetCode 3151: Special Array I**

## 📌 **Overview**
This project solves **LeetCode Problem 3151: Special Array I**.  
The task is to determine whether an array is **special**, meaning every pair of adjacent elements contains two numbers with **different parity** (one even, one odd).

### **Problem Statement**
Given an array of integers `nums`, return:
- `True` if the array is **special**.
- `False` if there exists at least one adjacent pair with the **same parity** (both even or both odd).

🔹 **Constraints:**
- `1 <= nums.length <= 100`
- `-10⁹ <= nums[i] <= 10⁹`
- The array can contain both positive and negative numbers.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1]
Output: True
Explanation:
- Since there is only one element, there are no adjacent pairs to check.
- The array is trivially **special**.
```

### **Example 2**
```python
Input: nums = [2, 1, 4]
Output: True
Explanation:
- (2,1): `2` is even, `1` is odd → ✅ Different parity.
- (1,4): `1` is odd, `4` is even → ✅ Different parity.
- Since all pairs meet the condition, return `True`.
```

### **Example 3**
```python
Input: nums = [4, 3, 1, 6]
Output: False
Explanation:
- (4,3): `4` is even, `3` is odd → ✅ Different parity.
- (3,1): `3` is odd, `1` is odd → ❌ Same parity.
- Since there is a **violation**, return `False`.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ We iterate through the list and check each adjacent pair.  
✔ If `nums[i]` and `nums[i+1]` have different parity, we continue.  
✔ If `nums[i]` and `nums[i+1]` **have the same parity**, return `False`.  
✔ If no violations are found, return `True`.

## 📝 **Step-by-Step Approach**
### **1️⃣ Iterate Through the Array**
- If the array has only **one element**, return `True` immediately.
- Traverse from index `1` to `len(nums) - 1`.
- For each index `i`, check if:
  - `nums[i] % 2 == nums[i-1] % 2` (same parity) → return `False`.

### **2️⃣ Example Walkthrough (nums = [4, 3, 1, 6])**
| Index | `nums[i-1]` | `nums[i]` | Even/Odd Check | Result |
|--------|------------|----------|---------------|--------|
| 1      | 4 (even)  | 3 (odd)  | ✅ Different   | Continue |
| 2      | 3 (odd)   | 1 (odd)  | ❌ Same       | Return `False` |

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Special Array I' problem.

    An array is considered **special** if every pair of adjacent elements 
    contains two numbers with different parity (one even, one odd).
    
    The method `isArraySpecial` checks if a given list of integers meets 
    this condition and returns `True` if it does, otherwise `False`.
    """

    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Determines whether the given array is special.

        :param nums: List of integers to check.
        :return: `True` if the array is special, otherwise `False`.
        """
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:  # If adjacent numbers have the same parity
                return False
        
        return True


def main():
    """
    Demonstrates testing the isArraySpecial function on multiple test cases.
    """
    solver = Solution()

    # Example test cases
    test_cases = [
        [1],             # Expected: True
        [2, 1, 4],       # Expected: True
        [4, 3, 1, 6]     # Expected: False
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        result = solver.isArraySpecial(nums)
        print(f"Output: {result}\n")


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
3151. Special Array I/
├── special_array.py    # Python implementation of the solution
├── README.md           # Detailed explanation & walkthrough
```

✨ **Master parity-based problems with efficient logic!** 🚀  
