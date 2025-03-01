# 🔢 **LeetCode 2460: Apply Operations to an Array**  

## 📌 **Problem Overview**  

You are given a **0-indexed array** `nums` of size `n`, consisting of **non-negative** integers.  

You need to apply `n - 1` operations to this array sequentially. In the `i-th` operation (0-indexed), apply the following transformation:  

- If `nums[i] == nums[i + 1]`, then:
  - Multiply `nums[i]` by **2**
  - Set `nums[i + 1]` to **0**  

- **After all operations, shift all `0`'s** to the end of the array while maintaining relative order of the non-zero elements.

### **Example 1**  
```python
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
```
✅ **Explanation:**  
1. `nums[1]` and `nums[2]` are equal (`2,2`), so multiply `nums[1]` by `2` → `[1,4,0,1,1,0]`  
2. `nums[3]` and `nums[4]` are equal (`1,1`), so multiply `nums[3]` by `2` → `[1,4,0,2,0,0]`  
3. Shift all zeros to the end → **`[1,4,2,0,0,0]`**  

### **Example 2**  
```python
Input: nums = [0,1]
Output: [1,0]
```
✅ **Explanation:**  
- No adjacent elements are equal, so no multiplication is performed.  
- The only operation is shifting the zero to the end.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Steps in the Algorithm**  
1. **Traverse the array** and apply the given operations:
   - If two **adjacent numbers** are equal, **double the first** and **set the second to zero**.  
2. **Shift all non-zero elements** to the front while maintaining their order.  

📌 **Why is this efficient?**  
- We only traverse the array **once** for operations (`O(n)`).  
- We perform another **O(n) pass** to shift non-zero elements.  
- **Overall complexity: `O(n)`**, making it optimal.  

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    Solution class for applying operations on an array.
    """

    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        Applies the given operations on the nums array.

        - If two adjacent elements are equal, multiply the first by 2 and set the second to 0.
        - Shift all non-zero elements to the front, maintaining order.

        :param nums: List[int] - The input array of non-negative integers.
        :return: List[int] - The transformed array.
        """
        n = len(nums)
        write_index = 0  # Pointer to place non-zero elements

        for index in range(n):
            # Step 1: Merge adjacent equal elements if they are non-zero
            if index < n - 1 and nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0

            # Step 2: Shift non-zero elements to the front
            if nums[index] != 0:
                if index != write_index:
                    nums[index], nums[write_index] = nums[write_index], nums[index]
                write_index += 1

        return nums
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Merging adjacent elements** | **O(n)** |
| **Shifting non-zero elements** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The algorithm **traverses the array twice**, ensuring linear time complexity.  
- **No extra space** is used apart from variables (`O(1)` space complexity).  

## 📂 **Project Structure**  

```
apply_operations/
├── apply_operations.py  # Python solution
├── README.md            # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Two-pass approach ensures efficiency (`O(n)`).**  
✔ **In-place shifting avoids extra space usage (`O(1)`).**  
✔ **Handles all edge cases, including zeros and adjacent equal elements.**  

🚀 **Master this technique for future array transformation problems!** 🔥  


Let me know if you need any further refinements! 🚀