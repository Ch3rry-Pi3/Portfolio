# 🏠 **LeetCode 198: House Robber**

## 📌 **Problem Overview**
A professional robber is planning to rob houses along a street. Each house contains some amount of money. However, **if two adjacent houses are robbed on the same night, the police will be alerted**. 

**Goal:** Given an integer array `nums` where `nums[i]` represents the amount of money stored in house `i`, return the **maximum amount of money** that can be robbed **without alerting the police**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
nums = [1,2,3,1]
```
#### **Output:**
```python
4
```
#### **Explanation:**
- The best strategy is to rob **house 1** (money = **1**) and **house 3** (money = **3**).
- This gives a total of **1 + 3 = 4**.

### **Example 2**
#### **Input:**
```python
nums = [2,7,9,3,1]
```
#### **Output:**
```python
12
```
#### **Explanation:**
- The best strategy is to rob **house 1** (**2**), **house 3** (**9**), and **house 5** (**1**).
- This gives a total of **2 + 9 + 1 = 12**.

## 🛠 **Approach**
We solve this problem using **Dynamic Programming**:

1. **Define Two Variables:**  
   - `rob1`: Tracks the maximum amount robbed **excluding** the current house.
   - `rob2`: Tracks the maximum amount robbed **including** the current house.

2. **Iterate Through the Houses:**  
   - At each step, determine whether to rob the current house or not.
   - Update `rob1` and `rob2` accordingly.

3. **Return the Maximum Amount Robbed.**

This approach runs in **O(N) time complexity** and **O(1) space complexity**.

## 🚀 **Python Solution**
```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solves the House Robber problem using dynamic programming.

        Args:
            nums (List[int]): A list of non-negative integers representing the amount of money at each house.

        Returns:
            int: The maximum amount of money that can be robbed without alerting the police.
        """
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterate through houses | `for n in nums` | **O(N)** |
| Update `rob1` and `rob2` | Constant operations per house | **O(1)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
house_robber/
├── house_robber.py   # Python solution
├── README.md         # Documentation
```

## 🏆 **Why This Works**
✔ **Dynamic Programming Approach** ensures optimal decision-making at each step.  
✔ **Runs in O(N) time complexity**, making it **efficient for large inputs**.  
✔ **Handles edge cases**, including empty lists and single-element lists.

🚀 **With this solution, you can efficiently determine the maximum money a robber can steal!** 🎯