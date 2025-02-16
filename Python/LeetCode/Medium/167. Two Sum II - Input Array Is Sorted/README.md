# 🔢 **LeetCode 167: Two Sum II - Input Array Is Sorted**  

## 📌 **Problem Overview**  
You are given a **1-indexed sorted array** of integers `numbers` and a target sum `target`.  

Find **two numbers** in `numbers` that add up to `target` and return their **indices (1-based)** as a list `[index1, index2]`.  

🔹 **Constraints:**  
- There is **exactly one solution**.  
- Each input has **only one valid answer**.  
- **Cannot use the same element twice**.  
- Must use **constant extra space**.  

## 📊 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```plaintext
numbers = [2,7,11,15], target = 9
```
#### **Output:**  
```plaintext
[1,2]
```
#### **Explanation:**  
- `2 + 7 = 9`  
- The indices are `1` and `2` (1-based).  

### **Example 2**  
#### **Input:**  
```plaintext
numbers = [2,3,4], target = 6
```
#### **Output:**  
```plaintext
[1,3]
```
#### **Explanation:**  
- `2 + 4 = 6`  
- The indices are `1` and `3` (1-based).  

### **Example 3**  
#### **Input:**  
```plaintext
numbers = [-1,0], target = -1
```
#### **Output:**  
```plaintext
[1,2]
```
#### **Explanation:**  
- `-1 + 0 = -1`  
- The indices are `1` and `2` (1-based).  

## 🛠 **Approach**  
This problem can be efficiently solved using the **two-pointer technique** since the array is **sorted**.

### **Algorithm**  
1. Initialise **two pointers**:  
   - `left = 0` (start of the list).  
   - `right = len(numbers) - 1` (end of the list).  
2. **Check the sum** of `numbers[left] + numbers[right]`:  
   - If it **equals** `target`, return `[left + 1, right + 1]` (1-based index).  
   - If it **exceeds** `target`, move `right` pointer **left** (reduce sum).  
   - If it **falls short**, move `left` pointer **right** (increase sum).  
3. Continue until the solution is found.  

This approach works in **O(n) time complexity** with **O(1) extra space**.  

## 🚀 **Python Solution**  
```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted list that sum up to the target.

        Args:
            numbers (List[int]): A 1-indexed sorted array of integers.
            target (int): The target sum.

        Returns:
            List[int]: The indices of the two numbers, incremented by one.
        """
        # Initialise two pointers
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # If the sum matches the target, return the indices (1-based)
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                # Move the right pointer left to reduce the sum
                right -= 1
            else:
                # Move the left pointer right to increase the sum
                left += 1

        # Return an invalid result (not expected, as per problem constraints)
        return [-1, -1]
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity | Space Complexity |
|------|------------|----------------|-----------------|
| **Two-pointer search** | `while left < right` | **O(n)** | **O(1)** |
| **Index calculation** | `return [left + 1, right + 1]` | **O(1)** | **O(1)** |
| **Overall Complexity** | **O(n)** | **O(1)** |

🔹 **Why This Approach?**  
✔ **Efficient**: Only a single pass with two pointers.  
✔ **Optimised for Sorted Input**: No extra sorting needed.  
✔ **Constant Extra Space**: No additional memory is used.  

🚀 **This is the optimal solution for the problem!**