# 🔢 **LeetCode 15: 3Sum**

## 📌 **Overview**
This project solves **LeetCode Problem 15: 3Sum** using an **optimised two-pointer approach** that runs in **O(n²) time complexity**.

### **Problem Statement**
Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- The solution set must not contain **duplicate triplets**.

🔹 **Constraints:**
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation:
- (-1, 0, 1) → (-1) + 0 + 1 = 0 ✅
- (-1, -1, 2) → (-1) + (-1) + 2 = 0 ✅
```

### **Example 2**
```python
Input: nums = [0, 1, 1]
Output: []
Explanation: No triplets sum to 0.
```

### **Example 3**
```python
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
Explanation: The only possible triplet sums to 0.
```

## 🚀 **How It Works: Two-Pointer + Sorting Approach**
### **Intuition**
Instead of using a **brute force O(n³) solution**, we sort the array first and then use the **two-pointer approach** to efficiently find triplets that sum to zero.

### **Algorithm Steps**
1️⃣ **Sort the input array** → Helps in avoiding duplicates and using the two-pointer technique.
2️⃣ **Fix the first element** of the triplet by iterating through the array (`nums[i]`).
3️⃣ **Use the two-pointer technique**:
   - `left` starts at `i + 1`.
   - `right` starts at `len(nums) - 1`.
   - Move the pointers based on the sum of `nums[i] + nums[left] + nums[right]`.
   - If the sum is **too large**, move `right` **left**.
   - If the sum is **too small**, move `left` **right**.
4️⃣ **Skip duplicates** to ensure unique triplets.

## 📝 **Step-by-Step Example Walkthrough**
Let's walk through the algorithm with:
```python
nums = [-4, -1, -1, 0, 1, 2]
```
#### **Step 1: Sort the Array**
Sorted array → `[-4, -1, -1, 0, 1, 2]`

#### **Step 2: Iterate Through the Array**
| Step | i  | Left | Right | `nums[i]` | `nums[left]` | `nums[right]` | Sum  | Action |
|------|----|------|-------|----------|-------------|--------------|------|--------|
| 1    | 0  | 1    | 5     | -4       | -1          | 2            | -3   | Move `left` right |
| 2    | 0  | 2    | 5     | -4       | -1          | 2            | -3   | Move `left` right |
| 3    | 0  | 3    | 5     | -4       | 0           | 2            | -2   | Move `left` right |
| 4    | 0  | 4    | 5     | -4       | 1           | 2            | -1   | Move `left` right |
| 5    | 1  | 2    | 5     | -1       | -1          | 2            | 0    | **Triplet Found** → `[-1, -1, 2]` ✅ |
| 6    | 1  | 3    | 4     | -1       | 0           | 1            | 0    | **Triplet Found** → `[-1, 0, 1]` ✅ |

Final output: `[[ -1, -1, 2], [-1, 0, 1 ]]`

## **Implementation**
```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds unique triplets in nums where the sum is zero.

        :param nums: List of integers
        :return: List of unique triplets that sum to zero
        """
        result = []  # Stores unique triplets
        nums.sort()  # Sort the input array

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n³)** ❌ | **O(1)** ✅ |
| **Sorting + Two Pointers** | **O(n²)** ✅ | **O(1)** ✅ |

- **Sorting the array takes `O(n log n)`.**
- **Two-pointer traversal is `O(n)`, making the total time complexity `O(n²)`.**

## 🏗 **Project Structure**

```
15. 3Sum/
├── three_sum.py   # Efficient O(n²) solution using sorting + two-pointer approach
├── README.md      # Detailed explanation
```

### 📝 **`three_sum.py`**
- **Implements an O(n²) two-pointer solution.**
- **Handles duplicate values properly to avoid duplicate triplets.**

```python
def main():
    """
    Demonstrates finding all unique 3Sum triplets for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [-2, 0, 1, 1, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.threeSum(nums)
        print(f"3Sum Triplets: {result}\n")

if __name__ == "__main__":
    main()
```

**🚀 Master the 3Sum problem with this efficient approach!**

