# 🧮 LeetCode 3169: Count Days Without Meetings

## 📘 Problem Overview

You're given:
- An integer `days` representing the **total number of working days** an employee is available (from **day 1** to **day `days`**),
- A 2D array `meetings`, where `meetings[i] = [start_i, end_i]` represents a meeting **scheduled from day `start_i` to `end_i` inclusive**.

Meetings may **overlap**, and the goal is to determine:

> 🔍 **How many days are free of meetings?**

## ✅ Examples

### Example 1

```python
Input: days = 10, meetings = [[5,7], [1,3], [9,10]]
Output: 2
```

**Explanation**:
- Busy days: 1–3, 5–7, 9–10
- Free days: 4, 8 → total = **2**

### Example 2

```python
Input: days = 5, meetings = [[2,4], [1,3]]
Output: 1
```

**Explanation**:
- Busy days: 1–4
- Free day: 5 → total = **1**

### Example 3

```python
Input: days = 6, meetings = [[1,6]]
Output: 0
```

**Explanation**:
- All days are covered by one big meeting
- No free days → **0**

## 🧠 Intuition & Strategy

This is essentially an **interval merging and gap-counting** problem:

1. **Sort all meetings** by their starting day.
2. Traverse the meetings, keeping track of the **end of the last busy period**.
3. Whenever there's a **gap** between the end of one meeting and the start of the next → add the gap length to `free_days`.
4. After all meetings, account for any **remaining days after the last meeting**.

## 🧪 Python Implementation

```python
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Counts the number of days without scheduled meetings.

        :param days: Total number of working days.
        :param meetings: List of intervals [start, end] for scheduled meetings.
        :return: Number of days without any meetings.
        """
        free_days = 0
        latest_end = 0

        # Step 1: Sort meetings by start day
        meetings.sort()

        # Step 2: Traverse meetings to track gaps
        for start, end in meetings:
            if start > latest_end + 1:
                # There's a free gap between meetings
                free_days += start - latest_end - 1

            # Update the latest occupied day
            latest_end = max(latest_end, end)

        # Step 3: Add free days after last meeting
        free_days += days - latest_end

        return free_days
```

## ⏱ Time & Space Complexity

| Metric | Value |
|--------|-------|
| 🕒 Time Complexity | **O(n log n)** – due to sorting the meeting intervals |
| 🧠 Space Complexity | **O(1)** – constant space used |

## 📂 File Structure

```
count_days_without_meetings/
├── count_days.py         # Solution implementation
├── README.md             # This file!
```

## ✨ Key Takeaways

- Efficient use of interval merging logic solves this elegantly.
- Sorting is key to traversing non-overlapping periods effectively.
- Great practice for real-world scheduling-type problems! 🗓️
