# 🔢 **LeetCode 1004: Max Consecutive Ones III**

## 📌 **Problem Overview**
You are given a **binary array** `nums` consisting of **0s and 1s** and an integer `k`.  
Your task is to **return the maximum number of consecutive 1s** in `nums` **if you are allowed to flip at most `k` zeros**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```
#### **Output:**
```python
6
```
#### **Explanation:**
- We can flip at most **2 zeros**.
- The longest subarray of consecutive `1`s after flipping at most `2` zeros is **[1,1,1,0,0,1,1,1,1,1]**.
- The length of this subarray is **6**.

### **Example 2**
#### **Input:**
```python
nums = [0,0,1,1,1,0,0]
k = 0
```
#### **Output:**
```python
3
```
#### **Explanation:**
- Since we cannot flip any `0`s (`k = 0`), we can only take existing consecutive `1`s.
- The longest sequence of `1`s is `[1,1,1]`, with length **3**.

### **Example 3**
#### **Input:**
```python
nums = [0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1]
k = 3
```
#### **Output:**
```python
10
```
#### **Explanation:**
- We flip at most **3 zeros** to get the longest consecutive sequence.
- The longest subarray of `1`s after flipping is **10**.

## 🛠 **Approach**
This problem is solved using the **Sliding Window Technique**:
1. **Expand the Window**:
   - Iterate over the array with a `right` pointer.
   - If we encounter a `0`, **reduce `k`** (since flipping is allowed).
   
2. **Shrink the Window**:
   - If `k` becomes negative (i.e., more than `k` flips were used), move the `left` pointer to balance it.
   - This ensures we always have **at most `k` zeros** in our current window.

3. **Track the Maximum Window Size**:
   - The difference between `right` and `left` gives the size of the valid subarray.
   - **Update the max length** accordingly.

### 🔹 **Time Complexity**:  
- **O(N)** → We traverse the array **once** using two pointers (`left` and `right`).

### 🔹 **Space Complexity**:  
- **O(1)** → We use only a few integer variables.

## 🚀 **Python Solution**
```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum number of consecutive 1s in a binary array
        if at most k 0s can be flipped.

        Args:
            nums (List[int]): The binary array (containing 0s and 1s).
            k (int): The maximum number of 0s that can be flipped.

        Returns:
            int: The maximum length of consecutive 1s possible.
        """
        left = 0

        for right in range(len(nums)):
            # Reduce k when we include a zero in the window
            k -= 1 - nums[right]

            # If k becomes negative, move left pointer to balance the window
            if k < 0:
                k += 1 - nums[left]
                left += 1

        return right - left + 1
```

## ⏳ **Complexity Analysis**
| Step                | Operation             | Time Complexity |
|---------------------|----------------------|----------------|
| Expand window      | Iterate through `nums` with `right` pointer | **O(N)** |
| Shrink window      | Adjust `left` pointer when `k < 0` | **O(N)** |
| **Total Complexity** | **O(N) time, O(1) space** | ✅ Efficient |

## 📁 **Project Structure**
```
max_consecutive_ones/
├── max_consecutive_ones.py   # Python solution
├── README.md                 # Documentation
```

## 🏆 **Why This Works**
✔ **Sliding Window Approach** efficiently finds the longest valid subarray.  
✔ **Runs in O(N) time complexity**, making it **optimal** for large inputs.  
✔ **Handles all edge cases**, including when no `0`s can be flipped.  

🚀 **With this approach, you can efficiently determine the longest sequence of consecutive `1`s after flipping at most `k` zeros!** 🎯