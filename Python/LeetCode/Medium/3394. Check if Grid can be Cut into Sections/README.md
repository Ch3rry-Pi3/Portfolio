
# ✂️ LeetCode 3394: Check if Grid Can Be Cut into Sections

## 📌 Problem Summary

You are given:
- An integer `n`, representing the dimensions of an `n x n` grid.
- A list of **non-overlapping rectangles** on this grid.
- Each rectangle is represented by a 4-element list:  
  `[startx, starty, endx, endy]`  
  where:
  - `(startx, starty)` is the **bottom-left** corner.
  - `(endx, endy)` is the **top-right** corner.

Your task is to determine whether it's possible to make **two horizontal** or **two vertical cuts** such that:

1. The cuts divide the grid into **three distinct regions**.
2. Each region contains **at least one rectangle**.
3. Each rectangle is **entirely contained** within **exactly one** region.



## ✅ Examples

### Example 1:

```python
Input: n = 5,
rectangles = [
    [1, 0, 5, 2],
    [0, 2, 2, 4],
    [3, 2, 5, 3],
    [0, 4, 4, 5]
]

Output: True
```

**Explanation**:  
We can make **horizontal cuts** at `y = 2` and `y = 4`, splitting the rectangles cleanly across the height of the grid.



### Example 2:

```python
Input: n = 4,
rectangles = [
    [0, 0, 1, 1],
    [2, 0, 3, 4],
    [0, 2, 2, 3],
    [3, 0, 4, 3]
]

Output: True
```

**Explanation**:  
We can make **vertical cuts** at `x = 2` and `x = 3`, and all rectangles belong to exactly one region.



### Example 3:

```python
Input: n = 4,
rectangles = [
    [0, 2, 2, 4],
    [1, 0, 3, 2],
    [2, 2, 3, 4],
    [3, 0, 4, 2],
    [3, 2, 4, 4]
]

Output: False
```

**Explanation**:  
There’s no valid pair of cuts (horizontal or vertical) that can divide the grid into **three** valid regions where all rectangles are contained within one region and none are left out.



## 🧠 Intuition & Strategy

- Sort the rectangles based on `x` or `y` positions.
- Track the furthest endpoint seen so far.
- Each **non-overlapping segment** between rectangles becomes a **cut candidate**.
- If you can find **two or more such gaps**, you can place two cuts and satisfy the condition.



## 🧪 Python Implementation

```python
from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def _check_cuts(rectangles: List[List[int]], dim: int) -> bool:
            gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])
            furthest_end = rectangles[0][dim + 2]

            for i in range(1, len(rectangles)):
                if furthest_end <= rectangles[i][dim]:
                    gap_count += 1
                furthest_end = max(furthest_end, rectangles[i][dim + 2])

            return gap_count >= 2

        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)
```

## ⏱️ Time & Space Complexity

| Metric         | Complexity        |
|-|-|
| Time Complexity | $O(n \log n)$ due to sorting |
| Space Complexity | $O(1)$ auxiliary (excluding input) |



## 📂 File Structure

```
cut_grid_sections/
├── main.py       # Python implementation
├── README.md     # Problem explanation, examples, intuition
```



## 🎯 Key Takeaways

- Identify **gaps** in sorted rectangles to place cuts.
- You only need to validate **two possible dimensions** (x or y).
- Sorting is the key to solving this elegantly.
