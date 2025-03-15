# 🏠 **LeetCode 2560: House Robber IV**  

## 📌 **Problem Overview**  

A robber wants to steal from **at least `k` houses** along a street, but **he cannot steal from two adjacent houses**.  
Each house contains some **money**, represented as an integer array `nums`, where:  

- `nums[i]` is the **amount of money** in the `i-th` house.
- The **robber's capability** is defined as the **maximum** amount of money stolen from any single house.
- The goal is to **minimize the robber's capability** while ensuring he **steals from at least `k` houses**.

## ✅ **Example 1**  

```python
Input: nums = [2,3,5,9], k = 2
Output: 5
```

### **Explanation:**  
There are **three ways** to rob at least **2** houses:  
- **Rob houses `[0, 2]`** → max(`nums[0]`, `nums[2]`) = **5**  
- **Rob houses `[0, 3]`** → max(`nums[0]`, `nums[3]`) = **9**  
- **Rob houses `[1, 3]`** → max(`nums[1]`, `nums[3]`) = **9**  
- The **minimum capability** of the robber is **5**.

## ✅ **Example 2**  

```python
Input: nums = [2,7,9,3,1], k = 2
Output: 2
```

### **Explanation:**  
- The **optimal way** is to rob houses **0 and 4**, with a maximum stolen amount of **2**.
- **Output:** **2**

## 🛠 **Approach & Intuition**  

### 🔹 **Binary Search on Capability**  
Since the **capability** (maximum stolen money from a house) must be minimized, we can **use binary search**:

1. **Define search space**:  
   - The **lower bound** is `1` (since house values are positive).
   - The **upper bound** is `max(nums)` (worst case: rob the most expensive house).
  
2. **Binary Search Process**:  
   - Check if it's **possible** to rob **at least `k` houses** while keeping the **maximum amount per house ≤ mid**.
   - If possible, **try a lower capability**.
   - If not, **increase the capability**.
  
3. **Greedy House Selection**:  
   - Iterate over `nums`, selecting houses **greedily** while maintaining the **non-adjacent** rule.
   - Count how many houses can be robbed under the current capability.

### 📌 **Why Binary Search?**  
- **O(n log max(nums))** complexity is **efficient** given `nums.length ≤ 10⁵`.
- Allows us to **find the optimal solution** in **logarithmic time**.

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum capability of the robber for at least k houses.
        
        :param nums: List of integers representing money stored in houses.
        :param k: The minimum number of houses the robber must steal from.
        :return: The minimum capability required.
        """

        # Define the search space for binary search
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        # Perform binary search to find the optimal minimum capability
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0
            index = 0

            # Greedily check how many houses can be robbed with current mid_reward
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2  # Skip the next house to maintain non-adjacent condition
                else:
                    index += 1

            # If we can rob at least k houses, try a lower capability
            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Binary Search Range (`log max(nums)`)** | **O(log max(nums))** ✅ |
| **Greedy House Selection (`O(n)`)** | **O(n)** ✅ |
| **Overall Complexity** | **O(n log max(nums))** ✅ |

🔹 **Why is this efficient?**  
- Binary search ensures we **minimize the search space exponentially**.  
- The **greedy selection** ensures we **pick the most optimal houses**.  

## 📂 **Project Structure**  

```
2260. House Robber IV/
├── house_robber.py  # Python solution
├── README.md        # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses Binary Search to minimize capability.**  
✔ **Greedy approach ensures optimal house selection.**  
✔ **Efficient O(n log max(nums)) complexity.**  

🚀 **Master this technique for similar problems!** 🔥  
