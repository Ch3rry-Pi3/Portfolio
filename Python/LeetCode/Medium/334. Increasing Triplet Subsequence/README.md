# 🚀 **LeetCode 334: Increasing Triplet Subsequence**

## 📌 **Overview**
This project solves **LeetCode Problem 334: Increasing Triplet Subsequence**.  
The goal is to determine if there exists a **strictly increasing subsequence of length 3** in a given list.

### **Problem Statement**
Given an integer array `nums`, return:
- `True` if **there exists a subsequence of length 3** such that:
  \[
  nums[i] < nums[j] < nums[k] \quad \text{where} \quad i < j < k
  \]
- `False` otherwise.

🔹 **Constraints:**
- `1 <= nums.length <= 5 * 10⁵`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- **Must run in `O(n)` time complexity**.

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: nums = [1, 2, 3, 4, 5]
Output: True
Explanation:
- The increasing triplet `1 < 2 < 3` exists.
```

### **Example 2**
```python
Input: nums = [5, 4, 3, 2, 1]
Output: False
Explanation:
- The numbers are in **decreasing order**, so no increasing triplet exists.
```

### **Example 3**
```python
Input: nums = [2, 1, 5, 0, 4, 6]
Output: True
Explanation:
- The increasing triplet `1 < 4 < 6` exists.
```

## 🚀 **Understanding the Problem**
### **Key Observations**
✔ **We are not looking for consecutive elements**—they only need to appear in increasing order.  
✔ **Sorting is NOT allowed** because the subsequence must maintain its relative order.  
✔ **We must solve it in `O(n)` time**, so nested loops (`O(n²)`) are not efficient.  

## 🧠 **Intuition Behind the Approach**
### **Step-by-Step Walkthrough**
Let's take `nums = [2, 1, 5, 0, 4, 6]` and see how we track the smallest elements.

#### **Step 1️⃣: Initialize Two Smallest Values**
We maintain:
- `num_i` → **smallest number seen so far** (`inf` initially).
- `num_j` → **second smallest number seen so far** (`inf` initially).

| Step | `num_i` | `num_j` | Current Number | Action |
|------|--------|--------|---------------|--------|
| 1️⃣   | `inf`  | `inf`  | `2`           | `num_i = 2` |
| 2️⃣   | `1`    | `inf`  | `1`           | `num_i = 1` (updated to smaller value) |
| 3️⃣   | `1`    | `5`    | `5`           | `num_j = 5` (found a second increasing number) |
| 4️⃣   | `1`    | `5`    | `0`           | Ignore (smaller than `num_i`, but no impact) |
| 5️⃣   | `1`    | `4`    | `4`           | `num_j = 4` (updated since `4 < 5`) |
| 6️⃣   | `1`    | `4`    | `6`           | **Found `6` > `num_j` → Triplet exists! ✅** |

✔ **We found the triplet** `1 < 4 < 6`, so return `True`.

## 📝 **Step-by-Step Approach**
### **1️⃣ Maintain Two Tracking Variables**
- `num_i` → Stores the **smallest** number seen so far.
- `num_j` → Stores the **second smallest** number found.

### **2️⃣ Traverse the Array**
- If `num <= num_i`, update `num_i`.
- Else if `num <= num_j`, update `num_j`.
- Else, if `num > num_j`, return `True` (triplet found).

### **3️⃣ Return `False` if No Triplet Exists**
- If we finish iterating without finding a valid triplet, return `False`.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Increasing Triplet Subsequence' problem.

    The function `increasingTriplet` checks whether there exists an increasing triplet 
    (three increasing elements in order) in the given list.
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Determines if there exists an increasing subsequence of length 3.

        :param nums: List of integers.
        :return: `True` if an increasing triplet exists, otherwise `False`.
        """
        num_i = num_j = float('inf')        # Initialize two smallest elements

        # Iterate through the array to find an increasing triplet
        for num in nums:
            if num <= num_i:
                num_i = num                 # Update the smallest value
            elif num <= num_j:
                num_j = num                 # Update the second smallest value
            else:
                return True                 # A valid increasing triplet is found

        return False                        # No increasing triplet found

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Two-pointer tracking (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Each element is processed once**, making it **O(n)**.
- **No extra space is used**, making it **O(1)**.

## 🏗 **Project Structure**
```
334. Increasing Triplet Subsequence/
├── increasing_triplet_subsequence.py    # Python implementation of the solution
├── README.md                             # Detailed explanation & walkthrough
```

✨ **Master greedy tracking with an efficient `O(n)` two-variable approach!** 🚀  
