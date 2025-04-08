# 🧾 **LeetCode 3396: Minimum Number of Operations to Make Elements in Array Distinct**  

## 📌 **Problem Overview**  

You are given an integer array **nums**. Your task is to ensure that the elements in the array are **distinct**.  
To achieve this, you can perform the following operation any number of times:  
- **Remove 3 elements** from the **beginning** of the array.  
- If the array has fewer than 3 elements, **remove all remaining elements**.  

### **Objective:**  
Return the **minimum number of operations** required to make the elements in the array distinct.  
If the array is **already distinct**, return **0**.  

### 💡 **Note:**  
- An **empty array** is considered to have **distinct elements**.  



## ✅ **Example**  

### **Input:**  
```
nums = [1, 2, 3, 4, 2, 3, 5, 7]
```
### **Output:**  
```
2
```
### **Explanation:**  
- **Operation 1:** Remove the first 3 elements → [4, 2, 3, 5, 7]  
- **Operation 2:** Remove the next 3 elements → [3, 5, 7]  
- The remaining elements are **distinct**.  
- Minimum operations required: **2**.  



### **Input:**  
```
nums = [4, 5, 6, 4]
```
### **Output:**  
```
2
```
### **Explanation:**  
- **Operation 1:** Remove the first 3 elements → [4]  
- **Operation 2:** Remove the last element → [] (empty array)  
- Minimum operations required: **2**.  



### **Input:**  
```
nums = [6, 7, 8, 9]
```
### **Output:**  
```
0
```
### **Explanation:**  
- The array is already **distinct**.  



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Track Seen Elements:**  
   - Use a **boolean list** to mark seen elements.  
2. **Iterate from End:**  
   - Start from the **last element** and move backwards.  
3. **Check for Duplicates:**  
   - If an element is **already seen**, calculate the number of operations needed as `i // 3 + 1`.  
   - Mark the element as **seen**.  
4. **Return Result:**  
   - If no duplicates are found, return **0**.  



## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Returns the minimum number of operations needed to make all elements in the array distinct.
        To achieve this, we remove 3 elements from the beginning of the array any number of times.
        
        Args:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations required.
        """
        seen = [False] * 128
        for i in range(len(nums) - 1, -1, -1):
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
        return 0
```



## 📂 **Project Structure**  

```
minimum_operations_to_make_distinct/
├── main.py       # Python solution with example usage
├── README.md     # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. **Empty Array:** Return **0** since it's already distinct.  
2. **Single Element:** Return **0** as it is distinct by default.  
3. **All Same Elements:** Multiple operations required.  
4. **Already Distinct:** Return **0**.  
5. **Mixed Duplicates:** Efficiently calculate the number of operations.  



## 🚀 **Why This Works:**  
- Uses a **greedy approach** to quickly determine the minimum number of operations.  
- Efficient **backward iteration** and **seen list** to track duplicates.  
- Handles **corner cases** gracefully.  



## ✅ **Test Cases:**  
- Test with **various array lengths**.  
- Check **edge cases** like single elements and empty arrays.  
- Validate with **already distinct arrays**.  
