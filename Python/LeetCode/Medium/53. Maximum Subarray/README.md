# 📈 **LeetCode 53: Maximum Subarray**

## 📌 **Overview**
This project solves **LeetCode Problem 53: Maximum Subarray** using **Kadane’s Algorithm**, which efficiently finds the contiguous subarray with the largest sum in **O(n) time complexity**.

### **Problem Statement**
Given an integer array `nums`, find the contiguous subarray **(containing at least one number)** which has the **largest sum** and return **its sum**.

🔹 **Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
```

### **Example 2**
```python
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.
```

### **Example 3**
```python
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.
```

## 🚀 **How It Works: Kadane’s Algorithm**
### **Intuition**
The brute-force approach would check **all possible subarrays**, resulting in an **O(n²) time complexity**, which is too slow for large inputs. **Kadane’s Algorithm** instead **tracks the best subarray dynamically** in a **single pass**.

### **Algorithm Steps**
1️⃣ **Initialise variables:**
   - `maxSub = nums[0]` → Stores the **maximum subarray sum found**.
   - `currentSum = 0` → Tracks the **current subarray sum**.

2️⃣ **Iterate through `nums`**, checking:
   - If `currentSum < 0`, reset it to `0` (starting a new subarray).
   - Add `nums[i]` to `currentSum`.
   - Update `maxSub = max(maxSub, currentSum)`.

3️⃣ **Return `maxSub`**, the largest sum found.

### **Implementation**
```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum.

        :param nums: List of integers
        :return: Maximum sum of any contiguous subarray
        """
        maxSub = nums[0]  # Stores the maximum subarray sum found
        currentSum = 0     # Tracks the running sum of the current subarray

        for n in nums:
            if currentSum < 0:
                currentSum = 0  # Reset current sum if it becomes negative
            currentSum += n
            maxSub = max(maxSub, currentSum)  # Update max sum found
        
        return maxSub
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Kadane’s Algorithm** | **O(n)** ✅ | **O(1)** ✅ |

- **Brute force** iterates through **all pairs**, making it **too slow**.
- **Kadane’s Algorithm** only makes **one pass**, making it **fast and memory-efficient**.

## 🏗 **Project Structure**

```
53. Maximum Subarray/
├── max_subarray.py  # Efficient O(n) solution using Kadane’s Algorithm
├── README.md        # Detailed explanation
```

### 📝 **`max_subarray.py`**
- **Implements Kadane’s Algorithm**.
- **Optimised for O(n) time complexity.**

```python
def main():
    """
    Demonstrates finding the maximum subarray sum for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Expected output: 6
        [1],                              # Expected output: 1
        [5, 4, -1, 7, 8],                 # Expected output: 23
        [-1, -2, -3, -4],                 # Expected output: -1 (single largest negative)
        [8, -19, 5, -4, 20],              # Expected output: 21
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.maxSubArray(nums)
        print(f"Maximum Subarray Sum: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses Kadane’s Algorithm to find the maximum subarray sum in O(n) time**
✅ **Efficient for large inputs, only requires O(1) extra space**
✅ **Handles negative numbers and edge cases properly**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `max_subarray.py` to test the function.

```bash
python max_subarray.py
```

## 🌟 **Future Improvements**
- 🏎 **Implement the `O(n log n)` Divide & Conquer approach as an alternative**.
- 🔄 **Extend functionality to return the subarray itself, not just the sum**.

**🚀 Master array-based problem-solving with this efficient approach!**

