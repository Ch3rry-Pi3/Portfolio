# ✨ **LeetCode 238: Product of Array Except Self**

## 📌 **Overview**
This project solves **LeetCode Problem 238: Product of Array Except Self** using an **efficient prefix and postfix multiplication approach** to compute results in **O(n) time complexity** without using division.

### **Problem Statement**
Given an integer array `nums`, return an array `answer` such that:
- `answer[i]` is the **product of all the elements** in `nums` **except** `nums[i]`.
- **You cannot use division**.

🔹 **Constraints:**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit integer**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation:
- The product of all elements except `nums[0]` (1) is `2*3*4 = 24`.
- The product of all elements except `nums[1]` (2) is `1*3*4 = 12`.
- The product of all elements except `nums[2]` (3) is `1*2*4 = 8`.
- The product of all elements except `nums[3]` (4) is `1*2*3 = 6`.
```

### **Example 2**
```python
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation: The presence of `0` means all values except the position with `0` become `0`.
```

## 🚀 **How It Works: Prefix and Postfix Product Approach**
### **Intuition**
If division were allowed, we could calculate the total product and divide by `nums[i]` for each index. However, since **division is not allowed**, we compute the result **without dividing**.

To do this, we break the problem into **two passes**:
1. **Prefix Product Pass** → Compute product of all elements **before** `i`.
2. **Postfix Product Pass** → Compute product of all elements **after** `i` and multiply with the prefix product.

### **Algorithm Steps**
1️⃣ **Create a result array initialised with `1`**
   ```python
   result = [1] * len(nums)
   ```
   This array will store the **final output**.

2️⃣ **Calculate Prefix Products**
   - Iterate from **left to right**, maintaining a running product.
   - Store the prefix product in `result[i]`.
   ```python
   prefix = 1
   for i in range(len(nums)):
       result[i] = prefix
       prefix *= nums[i]  # Multiply prefix by nums[i] for next iteration
   ```

3️⃣ **Calculate Postfix Products and Multiply**
   - Iterate **right to left**, maintaining a running product (`postfix`).
   - Multiply `result[i]` (which already holds prefix product) by postfix product.
   ```python
   postfix = 1
   for i in range(len(nums) - 1, -1, -1):
       result[i] *= postfix  # Multiply with postfix product
       postfix *= nums[i]  # Update postfix for next iteration
   ```

4️⃣ **Return the final result array**
   ```python
   return result
   ```

### **Implementation**
```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements except self in an array.

        :param nums: List of integers
        :return: List of integers where each element is the product of all others except itself
        """
        result = [1] * len(nums)

        # Compute prefix product for each element
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Compute postfix product and multiply it to result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|-----------------|
| **Brute Force (nested loops)** | **O(n²)** ❌ | **O(1)** |
| **Optimised Prefix & Postfix Approach** | **O(n)** ✅ | **O(1)** ✅ *(excluding output array)* |

- **Brute force** iterates through **all pairs**, making it **too slow**.
- **Prefix + Postfix approach** only makes **two passes**, making it **fast and memory-efficient**.

## 🏗 **Project Structure**

```
238. Product of Array Except Self/
├── product_except_self.py  # Efficient O(n) solution using prefix & postfix multiplication
├── README.md               # Detailed explanation
```

### 📝 **`product_except_self.py`**
- **Implements the prefix & postfix approach**.
- **Optimised for O(n) time complexity.**

```python
def main():
    """
    Demonstrates computing the product of array except self for multiple test cases.
    """
    solver = Solution()
    
    test_cases = [
        [1, 2, 3, 4],      # Expected output: [24,12,8,6]
        [-1, 1, 0, -3, 3], # Expected output: [0,0,9,0,0]
        [4, 5, 1, 8, 2],   # Expected output: [80, 64, 320, 40, 160]
        [10, 3, 5, 6, 2],  # Expected output: [180, 600, 360, 300, 900]
    ]

    for nums in test_cases:
        print(f"nums = {nums}")
        result = solver.productExceptSelf(nums)
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main()
```

## 🔥 **Key Takeaways**
✅ **Uses prefix and postfix multiplication to avoid division**
✅ **Efficient O(n) time complexity**
✅ **Only modifies the output array, achieving O(1) extra space**

## 🚀 **Try It Yourself!**
- Clone the repository.
- Run `product_except_self.py` to test the function.

```bash
python product_except_self.py
```

## 🌟 **Future Improvements**
- 🏎 **Optimise for extremely large datasets using bitwise operations**.
- 🔄 **Extend functionality to handle edge cases like multiple zeros more explicitly**.

**🚀 Master array-based problem-solving with this efficient approach!**

