# 🧾 **LeetCode 1863: Sum of All Subset XOR Totals**  

## 📌 **Problem Overview**  

The **XOR total** of an array is defined as the **bitwise XOR** of all its elements, or `0` if the array is empty.  

### **Problem Statement:**  
Given an array `nums`, return the **sum of all XOR totals** for **every subset** of `nums`.  

### **Important Notes:**  
1. Subsets with the **same elements** should be counted **multiple times**.  
2. An array `a` is a **subset** of array `b` if `a` can be obtained from `b` by **deleting some (possibly zero) elements** of `b`.  



## ✅ **Example**  

### **Input:**  
```
nums = [1, 3]
```
### **Output:**  
```
6
```
### **Explanation:**  
The 4 subsets of `[1, 3]` are:  
- `[]` → XOR total = 0  
- `[1]` → XOR total = 1  
- `[3]` → XOR total = 3  
- `[1, 3]` → XOR total = 1 XOR 3 = 2  
```
0 + 1 + 3 + 2 = 6
```



### **Example 2:**  

#### **Input:**  
```
nums = [5, 1, 6]
```
#### **Output:**  
```
28
```
#### **Explanation:**  
The 8 subsets of `[5, 1, 6]` are:  
- `[]` → XOR total = 0  
- `[5]` → XOR total = 5  
- `[1]` → XOR total = 1  
- `[6]` → XOR total = 6  
- `[5, 1]` → XOR total = 4  
- `[5, 6]` → XOR total = 3  
- `[1, 6]` → XOR total = 7  
- `[5, 1, 6]` → XOR total = 2  
```
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
```



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Recursive Calculation:**  
   - Use a **recursive function** to calculate the XOR total for each subset.  
2. **Backtracking:**  
   - For each element, decide to either **include** it or **exclude** it from the current subset.  
3. **Base Case:**  
   - If all elements are considered, **return the current XOR total**.  
4. **Recursive Case:**  
   - Calculate the sum of XOR totals by including and excluding the current element.  
5. **Return the Sum:**  
   - Add the results from both recursive calls to get the **total XOR sum**.  



## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Calculate the sum of all subset XOR totals.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The sum of XOR totals for every subset of nums.
        """
        
        def XOR_sum(nums: List[int], index: int, current_XOR: int) -> int:
            """
            Recursive helper function to calculate the sum of XOR totals.

            Args:
                nums (List[int]): The list of integers.
                index (int): The current index in the list.
                current_XOR (int): The current XOR result.

            Returns:
                int: Sum of XOR totals for subsets including and excluding the current element.
            """
            # Base case: when all elements in nums are considered
            if index == len(nums):
                return current_XOR
            
            # Calculate sum of subset XOR with the current element included
            with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[index])
            
            # Calculate sum of subset XOR without the current element
            without_element = XOR_sum(nums, index + 1, current_XOR)
            
            # Return the sum of both possibilities
            return with_element + without_element

        return XOR_sum(nums, 0, 0)
```



## 📂 **Project Structure**  

```
sum_of_xor_totals/
├── main.py       # Python solution with example usage
├── README.md      # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Empty List:** Returns 0 as XOR of an empty list is 0.  
2. **Single Element:** Only one subset and one XOR calculation.  
3. **All Zeros:** XOR of zeros remains 0.  
4. **Large Numbers:** Handles XOR calculations efficiently.  
5. **Repetitive Numbers:** All possible subsets are correctly considered.  



## 🚀 **Why This Works:**  
- **Efficiency:** Uses a **recursive backtracking approach** to generate all subsets and calculate XOR totals.  
- **Correctness:** Ensures that **all possible combinations** are considered.  
- **Optimal Use of Recursion:** Reduces unnecessary calculations by branching only when necessary.  



## ✅ **Test Cases:**  
- Test with **small arrays** to verify correctness.  
- Test with **large arrays** to check performance.  
- Check **edge cases** like an empty list or a single element.  
- Verify cases where **all elements are identical**.  
