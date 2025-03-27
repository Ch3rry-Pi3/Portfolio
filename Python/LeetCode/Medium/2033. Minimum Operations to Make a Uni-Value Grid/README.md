# 🧮 LeetCode 2033: Minimum Operations to Make a Uni-Value Grid

## 📌 Problem Overview

You are given a 2D grid of integers `grid` and an integer `x`.

In one operation, you can **add or subtract `x`** from **any element** in the grid.

A **uni-value grid** is a grid where **all elements are equal**.

Your task is to **return the minimum number of operations** required to make the grid a uni-value grid.

If it is **impossible**, return `-1`.



## ✅ Example 1

```
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
```

### Explanation:
We can make every element equal to 4 with the following operations:

- Add 2 to 2 → 4
- Subtract 2 from 6 → 4
- Subtract 2 twice from 8 → 6 → 4

**Total operations**: 4



## ✅ Example 2

```
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
```

### Explanation:
We can make every element equal to 3:

- 1 → 2 → 3 → 2 operations  
- 2 → 3 → 1 operation  
- 5 → 4 → 3 → 2 operations

**Total operations**: 5



## ❌ Example 3

```
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
```

### Explanation:
All elements must be equal. But here, you cannot make all numbers equal using only `+2` or `-2`.



## 🧠 Intuition & Strategy

To solve the problem:

1. **Flatten the grid** into a 1D list of numbers.
2. **Check feasibility**: All numbers must give the same remainder modulo `x`.
3. **Minimise operations**: Use the **median** as the target value to reduce total cost (minimises the sum of absolute differences).
4. **Sum all operations** as the number of times each number differs from the target, divided by `x`.



## 🧮 Python Implementation

```python
from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_array = [num for row in grid for num in row]
        nums_array.sort()
        target = nums_array[len(nums_array) // 2]
        result = 0

        for number in nums_array:
            if (number - target) % x != 0:
                return -1
            result += abs(number - target) // x

        return result
```
## ⏱️ Time & Space Complexity

| Metric             | Complexity      |
|--|--|
| Time Complexity    | `O(m * n log(mn))` — Sorting the grid |
| Space Complexity   | `O(m * n)` — For flattened grid         |



## 📂 Project Structure

```
2033. Minimum Operations to Make a Uni-Value Grid/
├── main.py
├── README.md
```



## 🎯 Key Takeaways

- Use **median** to minimise sum of absolute differences.
- Ensure all values have **equal modulo x** to be reachable.
- Use **flattening + greedy + math** approach for clean logic.
