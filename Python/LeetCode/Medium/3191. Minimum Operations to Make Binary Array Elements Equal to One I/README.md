# 🚀 **LeetCode 3191: Minimum Operations to Make Binary Array Elements Equal to One**  

## 📌 **Problem Overview**  

You are given a **binary array** `nums` consisting of `0`s and `1`s.  

You can **choose any 3 consecutive elements** in the array and **flip** all of them in **one operation**.  

- **Flipping** means changing `0 → 1` and `1 → 0`.  
- You need to **minimize the number of operations** required to make all elements in `nums` equal to **1**.  
- If it is **impossible** to make all elements `1`, return `-1`.  


## ✅ **Example 1**  

```python
Input: nums = [0,1,1,1,0,0]
Output: 3
```

### **Explanation:**  
We can perform the following operations:  
1. Choose elements at indices **0, 1, 2**, flipping them → `[1, 0, 0, 1, 0, 0]`.  
2. Choose elements at indices **1, 2, 3**, flipping them → `[1, 1, 1, 0, 0, 0]`.  
3. Choose elements at indices **3, 4, 5**, flipping them → `[1, 1, 1, 1, 1, 1]`.  

All elements are now `1`, so the **minimum number of operations** is **3**.  

## ✅ **Example 2**  

```python
Input: nums = [0,1,1,1]
Output: -1
```

### **Explanation:**  
It is **impossible** to make all elements `1`, so we return **-1**.  

## 🛠 **Approach & Intuition**  

### 🔹 **Greedy Strategy**  
1. **Iterate** through `nums`, checking each index `i`.  
2. If `nums[i] == 0`, **flip** elements at indices `[i, i+1, i+2]`.  
3. **Track** the number of operations performed.  
4. **Edge Case:**  
   - If the **last two elements** remain `0`, return `-1` (impossible case).  
   - Otherwise, return the **total number of operations performed**.  

📌 **Why is this efficient?**  
- **Linear time complexity O(n)** ✅  
- **Modifies `nums` in-place** ✅  
- **Uses no extra space beyond variables** ✅  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Computes the minimum number of operations required to make all elements in nums equal to 1.
        If it is impossible, returns -1.

        :param nums: A binary array (list of 0s and 1s).
        :return: The minimum number of operations or -1 if it's impossible.
        """
        n = len(nums)
        count = 0

        # Iterate through the array, flipping groups of three where needed
        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the current element and the next two
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1  # Increment the number of operations

        # If the last two elements are still 0, it's impossible
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1

        return count
```


## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating through nums** | **O(n)** ✅ |
| **Flipping elements (constant time per operation)** | **O(1)** ✅ |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- The **greedy approach** ensures minimal flips.  
- We **only traverse the array once**, keeping the **runtime linear**.  

## 📂 **Project Structure**  

```
binary_array_operations/
├── minimum_operations.py  # Python solution
├── README.md              # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Greedy approach** ensures minimal number of flips.  
✔ **Linear `O(n)` time complexity**, making it **scalable**.  
✔ **Handles impossible cases by returning `-1`**.  

🚀 **Master this technique for solving similar binary array problems!** 🔥  
