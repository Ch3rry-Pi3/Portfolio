# 🏢 **LeetCode 252: Meeting Rooms**  

## 📌 **Problem Overview**  
Given an array of meeting time intervals **`intervals`**, where **`intervals[i] = [startᵢ, endᵢ]`**, determine if a person can **attend all meetings** without any overlap.

### 🔹 **Rules**  
- A person **cannot** attend overlapping meetings.
- A meeting **`[a, b]`** overlaps with **`[c, d]`** if **`b > c`** (i.e., the first meeting ends after the next one starts).  
- If no overlapping meetings exist, return **`True`**, otherwise return **`False`**.

## 📊 **Example Walkthrough**  

### **Example 1**
#### **Input:**
```python
intervals = [[0, 30], [5, 10], [15, 20]]
```
#### **Output:**
```python
False
```
#### **Explanation:**
- The second meeting **(5, 10)** overlaps with the first **(0, 30)**.
- The third meeting **(15, 20)** also overlaps with the first **(0, 30)**.
- Since there are overlaps, the function returns **`False`**.

### **Example 2**
#### **Input:**
```python
intervals = [[7, 10], [2, 4]]
```
#### **Output:**
```python
True
```
#### **Explanation:**
- The first meeting **(2, 4)** does not overlap with the second **(7, 10)**.
- Since there are **no** overlaps, the function returns **`True`**.

## 🔍 **Intuition**  
To determine if all meetings can be attended:
1. **Sort** the meetings based on **start time**.
2. **Check for overlaps**:
   - Compare the **end time** of the current meeting with the **start time** of the next meeting.
   - If **`endᵢ > startᵢ₊₁`**, there is an **overlap**, so return **`False`**.
3. If no overlaps are found, return **`True`**.

## 🛠 **Approach & Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Sorting** | `intervals.sort()` | **O(N log N)** |
| **Checking for overlaps** | **Single pass** through the intervals | **O(N)** |
| **Total Complexity** | **O(N log N) + O(N) = O(N log N)** | ✅ Efficient |

## 🚀 **Optimised Python Solution**
```python
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if a person can attend all meetings given a list of meeting time intervals.

        Args:
            intervals (List[List[int]]): A list where each element is a meeting interval [start, end].

        Returns:
            bool: True if a person can attend all meetings without overlap, otherwise False.
        """

        # Sort the intervals based on the start time
        intervals.sort()

        # Check for any overlapping meetings
        for i in range(len(intervals) - 1):
            # If the end time of the current meeting is greater than the start time of the next meeting
            if intervals[i][1] > intervals[i + 1][0]:
                return False        # Overlapping meetings found

        return True         # No overlaps, all meetings can be attended
```

## ✅ **Why This Approach?**
✔ **Sorting simplifies** overlap detection.  
✔ **Single pass check (O(N))** ensures efficiency.  
✔ **O(N log N) total time complexity**, which is optimal for this problem.  

## 🎯 **Final Thoughts**
By sorting the meetings first and checking for overlaps in a single pass, we can efficiently determine if all meetings can be attended. This approach works well for large input sizes. 🚀
