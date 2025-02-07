# 🔢 **LeetCode 1679: Max Number of K-Sum Pairs**

## 📌 **Overview**
This project solves **LeetCode Problem 1679: Max Number of K-Sum Pairs**.  
The goal is to find **the maximum number of operations** where two numbers in an array sum up to `k` and are then removed.

### **Problem Statement**
Given:
- An **integer array** `nums`
- An **integer** `k`

You can perform an **operation** by:
1. Picking **two numbers** from `nums` whose sum equals `k`.
2. Removing them from the array.

**Return the maximum number of such operations** that can be performed.

🔹 **Constraints:**
- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`
- `1 <= k <= 10⁹`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1,2,3,4], k = 5
Output: 2
```
#### **Step-by-Step Breakdown**
1️⃣ **Starting with `nums = [1,2,3,4]`**  
   - Remove **1 and 4** → `nums = [2,3]`
   - Remove **2 and 3** → `nums = []`  
   
✅ **Total operations: `2`**

### **Example 2**
```python
Input: nums = [3,1,3,4,3], k = 6
Output: 1
```
#### **Step-by-Step Breakdown**
1️⃣ **Starting with `nums = [3,1,3,4,3]`**  
   - Remove **the first two `3`s`** → `nums = [1,4,3]`  
   
✅ **Total operations: `1`** (No more pairs summing to `6` exist)

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ The **order of elements doesn’t matter**, only **pairs that sum to `k`**.  
✔ A **brute-force approach (`O(n²)`)** would be too slow.  
✔ A **dictionary-based approach (`O(n)`)** efficiently finds valid pairs.  

## 📝 **Step-by-Step Approach**
### **1️⃣ Use a Dictionary to Track Counts**
- **`count_map[num]`** → Stores how many times `num` appears.

### **2️⃣ Iterate Through the Array**
- For each `num`, check if `k - num` (its complement) is in `count_map`.
- If the complement exists, **form a pair** and **decrease the count**.
- Otherwise, **store `num` in the dictionary**.

### **3️⃣ Return the Total Pair Count**
- Each valid pair increments the **`pairs`** counter.

## **💡 Implementation**
```python
from typing import List
from collections import defaultdict

class Solution:
    """
    This class provides an implementation of the 'Max Number of K-Sum Pairs' problem.

    The function `maxOperations` finds the maximum number of operations where 
    we remove two numbers that sum up to `k`.
    """

    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Determines the maximum number of operations where two elements sum to `k`.

        :param nums: List of integers.
        :param k: Target sum for pairs.
        :return: Maximum number of operations possible.
        """
        count_map = defaultdict(int)                # Dictionary to store counts of seen numbers
        pairs = 0                                   # Counter for valid k-sum pairs

        # Iterate through the numbers
        for num in nums:
            complement = k - num                    # Find the complement needed to form sum `k`

            if count_map[complement] > 0:           # Check if complement exists
                pairs += 1                          # Increment pair count
                count_map[complement] -= 1          # Use up one occurrence of the complement
            else:
                count_map[num] += 1                 # Store the number in the dictionary

        return pairs                                # Return total number of valid k-sum pairs
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Dictionary-based (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each element is processed once**, making it **O(n)**.
- **The dictionary stores at most `O(n)` elements**, making space complexity **O(n)**.

## 🏗 **Project Structure**
```
1679. Max Number of K-Sum Pairs/
├── max_num_ksum_pairs.py    # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Master pair-matching with an efficient `O(n)` approach!** 🚀  