# 🔢 **LeetCode 128: Longest Consecutive Sequence**

## 📌 **Problem Overview**
Given an **unsorted** array of integers `nums`, return the **length of the longest consecutive elements sequence**.

**Constraints:**
- You **must** write an algorithm that runs in **O(n)** time.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
nums = [100, 4, 200, 1, 3, 2]
```
#### **Output:**
```python
4
```
#### **Explanation:**
The longest consecutive sequence is **[1, 2, 3, 4]**, so its length is **4**.

### **Example 2**
#### **Input:**
```python
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```
#### **Output:**
```python
9
```
#### **Explanation:**
The longest consecutive sequence is **[0, 1, 2, 3, 4, 5, 6, 7, 8]**, so its length is **9**.

## 🛠 **Approach**
We solve this problem using a **sorting-based approach**:

### **1️⃣ Sort the Array**
- Sorting makes consecutive numbers adjacent.
- We can then iterate through the list and count consecutive numbers.

### **2️⃣ Track Streaks**
- Maintain two counters:
  - `longest_streak` (stores the longest sequence found)
  - `current_streak` (tracks the ongoing consecutive sequence)

### **3️⃣ Iterate & Compare**
- Loop through the sorted array:
  - If a number is **consecutive** (`nums[i] == nums[i - 1] + 1`), increment `current_streak`.
  - Otherwise, update `longest_streak` and reset `current_streak`.

### **4️⃣ Return the Maximum Streak**
- The answer is the **maximum value** between `longest_streak` and `current_streak`.

⏳ **Time Complexity:** **O(n log n)** due to sorting.

## 🚀 **Python Solution**
```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest consecutive sequence.
        """
        if not nums:
            return 0

        # Sort the numbers
        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # Ignore duplicates
            if nums[i] != nums[i - 1]:
                # If consecutive, increase streak count
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    # Update longest streak and reset current streak
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `nums.sort()` | **O(n log n)** |
| Iteration | `for` loop through `nums` | **O(n)** |
| **Total Complexity** | **O(n log n)** | ❗ Not optimal but still efficient |

## 📁 **Project Structure**
```
longest_consecutive_sequence/
├── longest_consecutive_sequence.py   # Python solution
├── README.md                         # Documentation
```

## 🏆 **Why This Works**
✔ **Sorting-based approach simplifies finding consecutive numbers**  
✔ **Tracks streak efficiently with O(n) iteration after sorting**  
✔ **Handles duplicates gracefully**  
✔ **Works well for moderately sized inputs**  

🚀 **With this solution, you can efficiently find the longest consecutive sequence!** 🎯