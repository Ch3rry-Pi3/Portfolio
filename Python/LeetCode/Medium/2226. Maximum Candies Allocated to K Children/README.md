# 🍬 **LeetCode 2226: Maximum Candies Allocated to K Children**  

## 📌 **Problem Overview**  

You are given a **0-indexed integer array** `candies`, where each element represents a **pile of candies**. You can split a pile into **smaller sub-piles**, but **you cannot merge** two piles together.  

Additionally, you are given an integer `k` representing the **number of children**. Your goal is to **allocate** piles of candies such that:  
✔️ Each child **receives the same number** of candies.  
✔️ A child **can only take from one pile** of candies.  
✔️ Some piles may **remain unused**.  

### 🔹 **Objective:**  
Return the **maximum number of candies** that each child can receive. If it is **not possible** to distribute the candies among all `k` children, return `0`.  

## ✅ **Example 1**  

```python
Input: candies = [5,8,6], k = 3
Output: 5
```

### **Explanation:**  
1. The **largest number of candies** that each child can receive is **5**.  
2. We can split `candies[1] = 8` into `5 + 3`, and `candies[2] = 6` into `5 + 1`.  
3. This gives us five piles of `[5, 5, 3, 1, 1]`.  
4. We can distribute the three piles of `5` to the **3 children**.  
5. Since no child can get **more than 5**, the **answer is 5**.  

## ✅ **Example 2**  

```python
Input: candies = [2,5], k = 11
Output: 0
```

### **Explanation:**  
- There are **11 children**, but only `7` candies in total.  
- It is **impossible** to ensure **each child receives at least one candy**.  
- Therefore, **the output is `0`**.  

## 🛠 **Approach & Intuition**  

### 🔹 **Binary Search on the Maximum Possible Allocation**  

📌 **Key Idea:** Instead of manually distributing the candies, we can use **binary search** to find the **largest** possible number of candies `x` that each child can receive.  

1. **Find the range of possible values for `x`:**  
   - The **minimum** value (`left`) starts at `1`.  
   - The **maximum** value (`right`) is the **largest pile** in `candies`.  

2. **Binary Search to Find the Maximum Candies:**  
   - Use **mid = (left + right + 1) // 2** as the potential number of candies per child.  
   - Count how many children can be served if each gets `mid` candies.  
   - If we can serve at least `k` children, try **a larger `mid`**.  
   - Otherwise, try **a smaller `mid`**.  

✅ **Why Binary Search?**  
- The answer lies **between `1` and `max(candies)`**, so **binary search** allows us to efficiently **eliminate half of the search space at each step**.  
- This ensures a **logarithmic time complexity** of **O(n log max(candies))**, which is much faster than a brute-force approach.  

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Determines the maximum number of candies each child can receive 
        while ensuring that all k children receive the same number of candies.
        
        :param candies: List of integers representing available candy piles.
        :param k: Number of children.
        :return: Maximum number of candies each child can get.
        """
        if sum(candies) < k:
            return 0  # If total candies are less than k, distribution is impossible
        
        left, right = 1, max(candies)

        # Binary search for the largest number of candies each child can get
        while left < right:
            mid = (left + right + 1) // 2
            if self._can_allocate_candies(candies, k, mid):
                left = mid  # Try a higher number
            else:
                right = mid - 1  # Reduce the number

        return left

    def _can_allocate_candies(self, candies: List[int], k: int, num_of_candies: int) -> bool:
        """
        Helper function to check if it's possible to allocate candies such that 
        each child gets exactly 'num_of_candies' candies.
        
        :param candies: List of candy piles.
        :param k: Number of children.
        :param num_of_candies: Number of candies per child.
        :return: True if possible, False otherwise.
        """
        total_children_served = sum(pile // num_of_candies for pile in candies)
        return total_children_served >= k

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Binary Search (log max_candies)** | **O(log max(candies))** ✅ |
| **Checking Valid Allocation** | **O(n)** ✅ |
| **Total Complexity** | **O(n log max(candies))** ✅ |

📌 **Why is this efficient?**  
- Instead of iterating over every possible number of candies (`1 to max(candies)`), we **use binary search**, cutting the search space **in half at each step**.  
- This ensures the solution is **scalable for large inputs** (`candies.length ≤ 10⁵` and `candies[i] ≤ 10⁷`).  

## 📂 **Project Structure**  

```
maximum_candies_allocated/
├── maximum_candies_allocated.py  # Python solution
├── README.md                     # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Binary Search Optimisation** makes this problem efficient.  
✔ **O(n log max(candies)) time complexity** ensures it scales well for large inputs.  
✔ **Greedy Allocation Strategy** ensures every child gets the maximum possible candies.  

🚀 **Master this technique for solving similar resource allocation problems!** 🔥  
