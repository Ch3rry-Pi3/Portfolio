# 🚀 **LeetCode 152: Maximum Product Subarray**

## 📌 **Overview**
This project solves **LeetCode Problem 152: Maximum Product Subarray** using an **efficient dynamic programming approach** that maintains both **minimum and maximum products** while iterating through the array in **O(n) time complexity**.

### **Problem Statement**
Given an integer array `nums`, find a contiguous subarray **(containing at least one number)** that has the **largest product** and return **the product**.

🔹 **Constraints:**
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit integer**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the largest product = 6.
```

### **Example 2**
```python
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2 because [-2,-1] is not a contiguous subarray.
```

### **Example 3**
```python
Input: nums = [-1,-3,-10,0,60]
Output: 60
Explanation: The subarray [60] has the largest product = 60.
```

## 🚀 **How It Works: Tracking Min & Max Products**
### **Intuition**
Unlike the **maximum sum subarray** problem (which can be solved with Kadane’s Algorithm), the **product subarray problem is trickier** because:
- **Negative numbers can become positive** when multiplied.
- **Zero resets the product**, splitting the array into separate subarrays.
- **A high positive product can quickly become negative** if multiplied by a negative value.

### **Algorithm Steps**
1️⃣ **Initialise variables:**
   - `result = max(nums)`: Start with the maximum value in `nums` (handles cases where the largest product is a single negative number).
   - `currentMin, currentMax = 1, 1`: Track the **minimum and maximum products** dynamically.

2️⃣ **Iterate through `nums`**, computing:
   - `tempMax = currentMax * n` (stores `currentMax` before modifying).
   - Update `currentMax` using `max(n * currentMax, n * currentMin, n)`, considering the three possibilities:
     - Multiplying with the previous `currentMax`.
     - Multiplying with the previous `currentMin` (useful when `n` is negative).
     - Starting fresh with `n` itself.
   - Update `currentMin` using `min(tempMax, n * currentMin, n)`.
   - Update `result = max(result, currentMax)`.

### **Implementation**
```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest product.

        :param nums: List of integers
        :return: Maximum product of any contiguous subarray
        """
        result = max(nums)              # Start with the maximum value in nums
        currentMin, currentMax = 1, 1   # Initialise min and max product

        for n in nums:
            tempMax = currentMax * n  # Store currentMax before modifying
            
            # Update currentMax and currentMin considering n
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(tempMax, n * currentMin, n)

            # Update the result with the largest product found so far
            result = max(result, currentMax)

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Optimised Dynamic Tracking** | **O(n)** ✅ | **O(1)** ✅ |

- **Brute force** iterates through **all pairs**, making it **too slow**.
- **Optimised approach** tracks min/max products in **one pass**, making it **fast and memory-efficient**.

## 🏗 **Project Structure**

```
152. Maximum Product Subarray/
├── max_product_subarray.py  # Efficient O(n) solution using dynamic tracking
├── README.md                # Detailed explanation
```

### 📝 **`max_product_subarray.py`**
- **Implements an O(n) solution using dynamic tracking.**
- **Handles negative numbers and zero cases properly.**

```python
def main():
    """
    Demonstrates finding the maximum product subarray for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [2, 3, -2, 4],       # Expected output: 6
        [-2, 0, -1],         # Expected output: 0
        [1, -2, -3, 4],      # Expected output: 12
        [-1, -3, -10, 0, 60],# Expected output: 60
        [2, -5, 3, 1, -4, 0, -2], # Expected output: 120
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.maxProduct(nums)
        print(f"Maximum Product Subarray: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses dynamic tracking of min & max products to handle negatives**
✅ **Efficient O(n) time complexity**
✅ **Only requires O(1) extra space**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `max_product_subarray.py` to test the function.

```bash
python max_product_subarray.py
```

## 🌟 **Future Improvements**
- 🏎 **Implement a Divide & Conquer approach for educational comparison**.
- 🔄 **Extend functionality to return the actual subarray, not just the product**.

**🚀 Master array-based problem-solving with this efficient approach!**

