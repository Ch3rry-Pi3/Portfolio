# 🎯 **LeetCode 39: Combination Sum**

## 📌 **Overview**
This project solves **LeetCode Problem 39: Combination Sum**.  
The goal is to find **all unique combinations** of numbers from a given list (`candidates`) that sum up to a target value.  
Each number **can be used multiple times** in a combination.

### **Problem Statement**
Given:
- A list of **distinct integers** `candidates`
- A **target integer** `target`

Return **all unique combinations** of `candidates` where the chosen numbers sum to `target`.  
Each number in `candidates` may be **used an unlimited number of times**.

**You may return the combinations in any order.**

🔹 **Constraints:**
- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- `1 <= target <= 500`
- All numbers in `candidates` are **distinct**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3], [7]]
```
#### **Step-by-Step Breakdown**
1️⃣ **Starting with `target = 7`**  
   - Try `2`: Remaining sum `7 - 2 = 5`
   - Try `2` again: Remaining sum `5 - 2 = 3`
   - Try `3`: Remaining sum `3 - 3 = 0` ✅ (Valid combination: `[2,2,3]`)  
   - Try `7`: Remaining sum `7 - 7 = 0` ✅ (Valid combination: `[7]`)  

✅ **Final Output: `[[2,2,3], [7]]`**  

### **Example 2**
```python
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2], [2,3,3], [3,5]]
```
#### **Step-by-Step Breakdown**
1️⃣ **Using `2`**  
   - `[2,2,2,2]` → ✅  

2️⃣ **Using `3`**  
   - `[2,3,3]` → ✅  

3️⃣ **Using `5`**  
   - `[3,5]` → ✅  

✅ **Final Output: `[[2,2,2,2], [2,3,3], [3,5]]`**  

### **Example 3**
```python
Input: candidates = [2], target = 1
Output: []
```
#### **Explanation:**
- The only candidate `2` is greater than `target = 1`, so no valid combinations exist.

✅ **Final Output: `[]`**

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ Each number **can be reused** → **Backtracking is ideal**.  
✔ Order of elements **doesn’t matter** (`[2,3,2]` is the same as `[2,2,3]`).  
✔ A **brute-force approach (`O(2ⁿ)`)** would be inefficient for large inputs.  
✔ **Recursive depth-first search (DFS) with backtracking** ensures all possibilities are explored efficiently.

## 📝 **Step-by-Step Approach**
### **1️⃣ Use DFS to Explore Possible Combinations**
- Start with an **empty combination** and `target`.
- Try **each candidate**, reducing `target` accordingly.
- **Recurse deeper** while ensuring numbers can be reused.

### **2️⃣ Backtrack When Target is Met or Exceeded**
- If `target == 0` → **Valid combination found**.
- If `target < 0` → **Stop searching (prune the branch).**

### **3️⃣ Store Unique Combinations**
- Only append **new valid combinations** to the result list.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Combination Sum' problem.

    The function `combinationSum` finds all unique combinations of numbers from `candidates` 
    that sum up to `target`, where each number can be used an unlimited number of times.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations where the sum equals `target` using numbers from `candidates`.
        
        :param candidates: List of distinct integers.
        :param target: Target sum for the combinations.
        :return: List of all unique combinations that sum to `target`.
        """
        results = []  # Stores valid combinations

        def dfs(remaining_sum: int, combination: List[int], cursor_start: int):
            """
            Depth-first search (DFS) helper function to explore combinations.
            
            :param remaining_sum: Remaining value to reach the target.
            :param combination: Current combination of numbers.
            :param cursor_start: Index to start the search (ensures numbers can be reused).
            """
            if remaining_sum == 0:
                # Found a valid combination, store a copy of it
                results.append(list(combination))
                return
            elif remaining_sum < 0:
                # If the sum exceeds target, stop searching
                return

            # Iterate over candidates starting from cursor_start
            for i in range(cursor_start, len(candidates)):
                # Add candidate[i] to the current combination
                combination.append(candidates[i])
                # Recursively explore further with the updated sum and same index (allow reuse)
                dfs(remaining_sum - candidates[i], combination, i)
                # Backtrack: Remove the last added number to explore other possibilities
                combination.pop()

        # Start DFS with an empty combination
        dfs(remaining_sum=target, combination=[], cursor_start=0)

        return results
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Backtracking DFS (`O(2ⁿ)`)** | **O(2ⁿ)** ❌ | **O(n)** ✅ |

- **Worst case:** Exploring all possible combinations → **Exponential growth (`O(2ⁿ)`)**.
- **Space complexity is `O(n)`,** since recursion depth **depends on `target`**.

## 🏗 **Project Structure**
```
39. Combination Sum/
├── combination_sum.py    # Python implementation of the solution
├── README.md             # Detailed explanation & walkthrough
```

✨ **Master backtracking with an efficient recursive approach!** 🚀  
