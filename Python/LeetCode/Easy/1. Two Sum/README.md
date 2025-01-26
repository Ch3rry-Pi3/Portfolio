# 🔢 **LeetCode 1: Two Sum**

## 📌 **Overview**
This project solves **LeetCode Problem 1: Two Sum** using an **efficient hashmap (dictionary) approach**.

### **Problem Statement**
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

🔹 **Constraints:**
- Each input has **exactly one solution**.
- **You may not use the same element twice**.
- **You can return the answer in any order**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so we return [0,1].
```

### **Example 2**
```python
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### **Example 3**
```python
Input: nums = [3,3], target = 6
Output: [0,1]
```

## 🚀 **How It Works: Optimised Hashmap Approach**
Instead of using a **brute-force O(n²) solution**, we use a **hashmap (dictionary)** to store numbers we’ve seen and their indices.

### **Algorithm Steps**
1. **Create an empty dictionary** (`prev_map`).
2. **Iterate through the array**:
   - Calculate `diff = target - current number`.
   - If `diff` exists in `prev_map`, return **both indices**.
   - Otherwise, store the **current number with its index** in `prev_map`.
3. **Since there is always one valid answer, we are guaranteed to return a result.**

### **Implementation**
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the list that add up to the target.

        :param nums: List of integers
        :param target: Target sum
        :return: Indices of the two numbers that add up to the target
        """
        prev_map = {}  # Dictionary to store number: index pairs

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]  # Return the indices of the two numbers
            
            prev_map[n] = i  # Store the current number with its index
        
        return []
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Optimised Hashmap Approach** | **O(n)** ✅ | **O(n)** ✅ |

- **Brute force** iterates through **all pairs** (slow).
- **Hashmap approach** stores values and looks them up in **constant time O(1)** per iteration.

## 🏗 **Project Structure**

```
leetcode_1_two_sum/
├── two_sum.py     # Efficient O(n) solution using a hashmap
├── README.md      # Detailed explanation
```

### 📝 **`two_sum.py`**
- **Implements the hashmap approach for finding two indices that sum to the target.**
- **Optimised for O(n) time complexity.**

```python
def main():
    """
    Demonstrates finding two indices that sum to a target value.
    """
    solver = Solution()
    
    test_cases = [
        ([2, 7, 11, 15], 9),    # Expected output: [0,1]
        ([3, 2, 4], 6),         # Expected output: [1,2]
        ([3, 3], 6)             # Expected output: [0,1]
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}")
        result = solver.twoSum(nums, target)
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses a hashmap for quick lookups**
✅ **Efficient O(n) time complexity**
✅ **Guaranteed to return a solution**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `two_sum.py` to test the function.

```bash
python two_sum.py
```

## 🌟 **Future Improvements**
- 🏎 **Optimize for extremely large datasets using alternative data structures**.
- 🔄 **Explore multi-solution variations** where multiple pairs might sum to `target`.

**🚀 Master array-based problem-solving with this efficient approach!**

