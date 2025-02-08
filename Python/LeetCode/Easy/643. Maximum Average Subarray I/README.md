# 📊 **LeetCode 643: Maximum Average Subarray I**  

## 📌 **Overview**  
This project provides a solution for **LeetCode Problem 643: Maximum Average Subarray I**.  
The goal is to find the **contiguous subarray of length `k`** that has the **maximum average value** and return that value.  

### **Problem Statement**  
You are given:  
- An **integer array** `nums` consisting of `n` elements.  
- An **integer `k`** representing the size of the subarray.  

👉 **Find a contiguous subarray of length `k` with the maximum average value and return that value.**  

#### **Constraints**  
- The **absolute error** between your answer and the correct answer should be **less than 10⁻⁵**.  

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```python
nums = [1, 12, -5, -6, 50, 3]
k = 4
```
#### **Process:**  
- Consider all subarrays of length `k = 4`:  
  - `[1, 12, -5, -6]` → Sum = `2`, Average = `2/4 = 0.50`  
  - `[12, -5, -6, 50]` → Sum = `51`, Average = `51/4 = 12.75` ✅ **(Maximum)**
  - `[-5, -6, 50, 3]` → Sum = `42`, Average = `42/4 = 10.50`  

#### **Output:**  
```python
12.75000
```

### **Example 2**  
#### **Input:**  
```python
nums = [5]
k = 1
```
#### **Process:**  
- The only subarray is `[5]` with an average of **5.00000**.

#### **Output:**  
```python
5.00000
```

## 🛠 **Approach**  

### **1️⃣ Sliding Window Technique**
Instead of recalculating the sum for every subarray (which is **O(n × k)**),  
we use a **sliding window** to maintain a sum that updates in **O(n)** time.  

- **Step 1:** Compute the sum of the first `k` elements.  
- **Step 2:** Slide the window across the array, updating the sum efficiently.  
- **Step 3:** Track the maximum sum and return the corresponding average.  

🔹 **Time Complexity:** **O(n)**  
🔹 **Space Complexity:** **O(1)**  

## 🚀 **Implementation**  

```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Finds the maximum average of any contiguous subarray of length k.

        Args:
            nums (List[int]): List of integers.
            k (int): Length of the subarray.

        Returns:
            float: Maximum average value of a contiguous subarray of length k.
        """
        # Initialise the sum of the first k elements
        current_sum = max_sum = sum(nums[:k])

        # Use sliding window to find the maximum sum for any subarray of length k
        for i in range(len(nums) - k):
            current_sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, current_sum)

        # Return the maximum average
        return max_sum / k
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Initial Sum | `sum(nums[:k])` | **O(k)** |
| Sliding Window | `O(n - k)` updates | **O(n - k) ≈ O(n)** |
| **Total Complexity** | **O(n)** ✅ **Optimised** |

## 🏗 **Project Structure**  
```
max_average_subarray/
├── max_average_subarray.py   # Python solution
├── README.md                 # This documentation
```

## 🏆 **Why This Works**
✔ **Uses the Sliding Window approach** for efficiency.  
✔ **Optimised from O(n × k) to O(n)**.  
✔ **Handles large values and edge cases**.  

🔥 **This is the best way to find the maximum average subarray in O(n) time complexity!** 🚀  