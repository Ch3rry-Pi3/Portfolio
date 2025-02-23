# 🔢 **LeetCode 487: Max Consecutive Ones II**  

## 📌 **Problem Overview**  
Given a **binary array** `nums`, return the **maximum number of consecutive `1`s** in the array **if you can flip at most one `0`**.

### **Example 1**  
```python
Input: nums = [1, 0, 1, 1, 0, 1]
Output: 4
```
✅ **Explanation:**  
- If we flip the **first zero**, `nums` becomes `[1, 1, 1, 1, 0, 1]` → **4 consecutive 1s**.
- If we flip the **second zero**, `nums` becomes `[1, 0, 1, 1, 1, 1]` → **4 consecutive 1s**.
- The **maximum number of consecutive ones** is **4**.

### **Example 2**  
```python
Input: nums = [1, 0, 1, 1, 0, 1, 1]
Output: 4
```
✅ **Explanation:**  
- If we flip the **first zero**, `nums` becomes `[1, 1, 1, 1, 0, 1, 1]` → **4 consecutive 1s**.
- If we flip the **second zero**, `nums` becomes `[1, 0, 1, 1, 1, 1, 1]` → **4 consecutive 1s**.
- The **maximum number of consecutive ones** is **4**.

### **Constraints**  
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Sliding Window Technique**  
To efficiently find the **longest sequence of consecutive 1s** when we can flip at most **one 0**, we can use a **two-pointer sliding window** approach.

1. **Expand the right pointer** (`right`) while counting the number of `0`s.
2. If the number of `0`s **exceeds 1**, move the left pointer (`left`) **to shrink the window** until we have at most one `0`.
3. **Keep track of the longest valid window** (`right - left + 1`).

📌 **Time Complexity:** **O(n)**  
- We traverse the array **once** with a two-pointer approach, making it **linear time**.

📌 **Space Complexity:** **O(1)**  
- We only use a few integer variables.

## 📝 **Implementation**  

```python
# max_consecutive_ones.py

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Finds the maximum number of consecutive 1's in a binary array
        when at most one 0 can be flipped to 1.

        Args:
            nums (List[int]): A binary list consisting of 0s and 1s.

        Returns:
            int: The maximum number of consecutive 1's achievable after flipping at most one 0.
        """

        longest_sequence = 0        # Stores the maximum sequence of consecutive 1's
        left, right = 0, 0          # Two-pointer window
        num_zeroes = 0              # Tracks the number of zeros in the window

        while right < len(nums):  
            if nums[right] == 0:            # Count zero if present
                num_zeroes += 1

            while num_zeroes == 2:          # If there are more than one zero, contract the window
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            # Update the maximum sequence length
            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1          # Expand the window

        return longest_sequence
```

## 📂 **Project Structure**  

```
487. Max Consecutive Ones II/
├── max_consecutive_ones.py  # Python solution
├── README.md                # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses the two-pointer sliding window approach** for optimal efficiency.  
✔ **Handles large inputs (`10^5`) efficiently** with an **O(n) time complexity**.  
✔ **Tracks the longest valid sequence dynamically**, ensuring correctness.

🚀 **A great problem for mastering sliding window techniques!** 🔥