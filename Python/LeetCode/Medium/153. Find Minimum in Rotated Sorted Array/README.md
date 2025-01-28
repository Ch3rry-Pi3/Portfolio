# 🔍 **LeetCode 153: Find Minimum in Rotated Sorted Array**

## 📌 **Overview**
This project solves **LeetCode Problem 153: Find Minimum in Rotated Sorted Array** using an **optimised binary search approach** that runs in **O(log n) time complexity**.

### **Problem Statement**
You are given an array of unique integers `nums` that is **sorted in ascending order** but then **rotated** at some unknown pivot.

Your task is to **find the minimum element** in this rotated sorted array.

🔹 **Constraints:**
- `1 <= nums.length <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers in `nums` are **unique**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5], rotated 3 times.
```

### **Example 2**
```python
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7], rotated 4 times.
```

### **Example 3**
```python
Input: nums = [11,13,15,17]
Output: 11
Explanation: The array was not rotated.
```

## 🚀 **How It Works: Optimised Binary Search**
### **Intuition**
A **brute-force** approach would scan the entire array in **O(n) time**, but since the array is **sorted and rotated**, we can leverage **binary search** to find the minimum in **O(log n) time**.

### **Algorithm Steps**
1️⃣ **Initialise variables:**
   - `result = nums[0]`: Start by assuming the first element is the smallest.
   - `left = 0`, `right = len(nums) - 1`: Define binary search boundaries.

2️⃣ **Binary Search:**
   - **If `nums[left] < nums[right]`**, the array is already sorted, so return `nums[left]`.
   - **Find the middle index** → `middle = (left + right) // 2`.
   - **Update `result`** → Store the minimum of `result` and `nums[middle]`.
   - **Determine which half to search next:**
     - If `nums[middle] >= nums[left]`, search the **right half** (`left = middle + 1`).
     - Otherwise, search the **left half** (`right = middle - 1`).

3️⃣ **Return `result`**, which now holds the smallest element.

### **Implementation**
```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        :param nums: List of unique integers sorted in ascending order but rotated
        :return: The minimum element in the array
        """
        result = nums[0]  # Initialise result with the first element
        left, right = 0, len(nums) - 1

        while left <= right:
            # If the array is already sorted, return the leftmost element
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right) // 2  # Find the middle index
            result = min(result, nums[middle])  # Update result with the middle element
            
            # Determine which half to search next
            if nums[middle] >= nums[left]:  # Left half is sorted, search right half
                left = middle + 1
            else:  # Right half is sorted, search left half
                right = middle - 1
        
        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (scan entire array)** | **O(n)** ❌ | **O(1)** ✅ |
| **Optimised Binary Search** | **O(log n)** ✅ | **O(1)** ✅ |

- **Brute force** checks every element, making it **slow for large arrays**.
- **Binary search** only checks **log(n) elements**, making it **fast and efficient**.

## 🏗 **Project Structure**

```
153. Find Minimum in Rotated Sorted Array/
├── min_in_sorted_array.py  # Efficient O(log n) solution using binary search
├── README.md               # Detailed explanation
```

### 📝 **`min_in_sorted_array.py`**
- **Implements an O(log n) binary search solution.**
- **Handles cases where the array is already sorted.**

```python
def main():
    """
    Demonstrates finding the minimum element in rotated sorted arrays for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [3, 4, 5, 1, 2],  # Expected output: 1
        [4, 5, 6, 7, 0, 1, 2],  # Expected output: 0
        [11, 13, 15, 17],  # Expected output: 11
        [2, 1],  # Expected output: 1
        [1],  # Expected output: 1
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.findMin(nums)
        print(f"Minimum Element: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses binary search for O(log n) efficiency**
✅ **Only requires O(1) extra space**
✅ **Handles cases where the array is already sorted**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `min_in_sorted_array.py` to test the function.

```bash
python min_in_sorted_array.py
```

## 🌟 **Future Improvements**
- 🏎 **Implement variations where duplicate elements exist in the array**.
- 🔄 **Extend functionality to return the number of rotations needed to restore order**.

**🚀 Master array-based problem-solving with this efficient approach!**

