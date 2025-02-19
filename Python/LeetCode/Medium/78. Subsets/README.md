# 🎉 **LeetCode 78: Subsets**  

## 📌 **Problem Overview**  
Given an integer array `nums` of **unique** elements, return **all possible subsets** (the power set).  
- The solution **must not** contain duplicate subsets.  
- The subsets can be returned **in any order**.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
```python
Input: nums = [1,2,3]  
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]  
```
✅ The power set contains **all** possible subsets, including the **empty set**.

### **Example 2**  
```python
Input: nums = [0]  
Output: [[], [0]]  
```
✅ The power set includes the **empty set** and the set containing `0`.

## 🚀 **Approach Explanation**  

### **Backtracking Approach**  
Backtracking is used to **explore all possible subset combinations**.  
1. Start with an **empty subset**.  
2. Recursively **include/exclude** elements.  
3. Store each subset **when reaching the end** of the input list.  


## 📝 **Python Solution**  
```python
from typing import List

class Solution:
    """
    This class provides a recursive backtracking solution to generate all subsets of a given list.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all subsets (power set) of the given list.

        :param nums: List of unique integers.
        :return: List of all possible subsets.
        """

        n = len(nums)
        result, solution = [], []

        def backtrack(i):
            if i == n:
                result.append(solution[:])
                return
            
            # Exclude nums[i]
            backtrack(i + 1)

            # Include nums[i]
            solution.append(nums[i])
            backtrack(i + 1)
            solution.pop()

        backtrack(0)
        return result
```

---

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Backtracking** | Generate `2^n` subsets | **O(2^n)** |
| **Copying Subsets** | Copy list to `result` | **O(n * 2^n)** |
| **Overall Complexity** | **O(n * 2^n)** ✅ Expected for generating power sets |

## 🎯 **Why This Approach?**  
✔ **Generates all possible subsets** using recursion.  
✔ **Avoids unnecessary duplicate calculations**.  
✔ **Maintains correct lexicographical ordering of subsets**.  

## 📂 **Project Structure**  
```
subsets/
├── subsets.py  # Python solution
├── README.md   # Explanation & approach
```

✨ **Master recursion & backtracking with this power set generation!** 🚀  