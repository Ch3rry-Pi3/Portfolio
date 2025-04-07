# 🧾 **LeetCode 416: Partition Equal Subset Sum**  

## 📌 **Problem Overview**  

You are given an integer array `nums`.  
Return `true` if you can partition the array into **two subsets** such that the sum of the elements in both subsets is equal. Otherwise, return `false`.  

### **Objective:**  
Determine if the given array can be **partitioned into two subsets** with **equal sum**.  



## ✅ **Example**  

### **Input:**  
```
nums = [1,5,11,5]
```
### **Output:**  
```
true
```
### **Explanation:**  
- The array can be partitioned as `[1, 5, 5]` and `[11]`.  
- Both subsets have the **same sum** of **11**.  

### **Input:**  
```
nums = [1,2,3,5]
```
### **Output:**  
```
false
```
### **Explanation:**  
- There is **no way** to partition the array into two equal sum subsets.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  

1. **Check for Sum Parity:**  
   - If the sum of the array is **odd**, it cannot be split into two equal parts.  
   - Return `False` if the sum is odd.  

2. **Target Sum Calculation:**  
   - Calculate the **target sum** as `total_sum // 2`.  
   - We aim to find **one subset** with this sum.  

3. **Dynamic Programming Approach:**  
   - Use a **set `dp`** to track all **possible subset sums**.  
   - Initialize `dp` with `{0}` (empty subset).  
   - For each number in the array, update `dp` with both:  
     - Including the current number.  
     - Excluding the current number.  
   - If `target` is found in `dp`, return `True`.  

4. **Return Result:**  
   - If `target` is not found in `dp`, return `False`.  



## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if the given array can be partitioned into two subsets
        such that the sum of elements in both subsets is equal.
        """
        # Check if the sum of elements is odd
        if sum(nums) % 2 != 0:
            return False

        # Target sum for one subset
        target = sum(nums) // 2
        dp = set([0])  # Initialize with 0 as an achievable sum

        for num in nums:
            nextDP = set(dp)  # Create a new set to update dp without affecting current state
            for t in dp:
                if t + num == target:
                    return True
                nextDP.add(t + num)  # Include current number in subset
            dp = nextDP  # Update the dp set for the next iteration

        return target in dp
```



## 📂 **Project Structure**  

```
partition_equal_subset_sum/
├── main.py       # Python solution with example usage
├── README.md      # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Empty Input:** An empty list should return `False`.  
2. **Single Element:** An array with one element cannot be partitioned, so return `False`.  
3. **Odd Sum:** If the sum of the array is odd, partitioning is not possible.  
4. **Equal Elements:** Handle cases where all elements are the same.  
5. **Large Input:** Efficiently handles up to **1000 elements**.  



## 🚀 **Why This Works:**  
- Uses **dynamic programming** to explore all possible sums.  
- Efficiently stores **achievable sums** using a set to avoid redundant calculations.  
- Uses **early stopping** if the target sum is found.  



## ✅ **Test Cases:**  
- **Basic Cases:** `[1,5,11,5]` → `True`  
- **Edge Cases:** `[1,2,3,5]` → `False`, `[1,2,5]` → `False`  
- **Single Element:** `[1]` → `False`  
- **Equal Elements:** `[2,2,2,2]` → `True`  
- **Complex Cases:** `[3,3,3,4,5]` → `True`  