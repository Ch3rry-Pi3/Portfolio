# 🧾 **LeetCode 368: Largest Divisible Subset**  

## 📌 **Problem Overview**  

Given a set of **distinct positive integers** `nums`, return the **largest subset** such that every pair \((x, y)\) of elements in this subset satisfies:  
1. \(x \% y == 0\) or \(y \% x == 0\)  

If there are **multiple solutions**, return **any** of them.  



### **Objective:**  
Find the **largest divisible subset** from the given list of distinct positive integers.  



## ✅ **Example**  

### **Input:**  
```
nums = [1, 2, 3]
```

### **Output:**  
```
[1, 2] or [1, 3]
```

### **Explanation:**  
Both subsets are valid since:
- \(2 \% 1 == 0\)  
- \(3 \% 1 == 0\)  



### **Input:**  
```
nums = [1, 2, 4, 8]
```

### **Output:**  
```
[1, 2, 4, 8]
```

### **Explanation:**  
The largest divisible subset is:
- \(2 \% 1 == 0\)  
- \(4 \% 2 == 0\)  
- \(8 \% 4 == 0\)  



## 💡 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Sorting:**  
   - Start by **sorting** the input list to maintain order.  
   
2. **Dynamic Programming with HashMap:**  
   - Use a **dictionary** to store the largest subset for each element, with `-1` as the base case (empty set).  
   
3. **Building Subsets:**  
   - For each number, find the **largest valid subset** it can extend.  
   - Update the dictionary by adding the current number to the best existing subset.  

4. **Returning the Result:**  
   - Return the **maximum subset** from the dictionary.  



## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        Finds the largest divisible subset from a list of distinct positive integers.

        Args:
            nums (List[int]): A list of distinct positive integers.

        Returns:
            List[int]: The largest divisible subset.
        """
        # Dictionary to store the largest subset ending with each number
        subsets = {-1: set()}
        
        # Process each number in the sorted order
        for num in sorted(nums):
            # Find the largest subset that num can extend
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        # Return the largest subset found
        return list(max(subsets.values(), key=len))
```



## 📂 **Project Structure**  

```
largest_divisible_subset/
├── main.py       # Python solution with example usage
├── README.md      # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Empty list:** Return an empty list.  
2. **Single element list:** Return the element itself.  
3. **Multiple valid subsets:** Return **any one** valid subset.  
4. **Prime numbers only:** Return the **first element** as no other numbers are divisible.  
5. **Already sorted numbers:** Check efficiency.  



## 🚀 **Why This Works:**  
- **Efficiency:** Uses **dynamic programming** to build optimal solutions step-by-step.  
- **Accuracy:** Always returns the **largest valid subset**.  
- **Flexibility:** Handles edge cases and **multiple valid outputs** efficiently.  



## ✅ **Test Cases:**  
- **Basic cases:** `[1, 2, 3]`, `[1, 2, 4, 8]`  
- **Edge cases:** `[1]`, `[2, 3, 5]`  
- **Large input:** Up to **1000 elements** to ensure performance.  