# 📊 LeetCode 1399: Count Largest Group

## 📝 Problem Overview

You are given an integer `n`. Each number from `1` to `n` is grouped **according to the sum of its digits**.

> A group is defined by the same digit sum. The size of a group is the number of elements in it.

### 🎯 Goal:
Return the **number of groups that have the largest size**.

---

## 📚 Example

### Example 1:

**Input:**
```
n = 13
```

**Explanation:**

The numbers from `1` to `13` can be grouped by digit sums:
- Sum = 1: [1, 10]
- Sum = 2: [2, 11]
- Sum = 3: [3, 12]
- Sum = 4: [4, 13]
- Sum = 5: [5]
- Sum = 6: [6]
- Sum = 7: [7]
- Sum = 8: [8]
- Sum = 9: [9]

Each of the groups with sum 1, 2, 3, and 4 has 2 elements — the largest size.

**Output:**
```
4
```

### Example 2:

**Input:**
```
n = 2
```

**Groups:**  
- [1] → sum = 1  
- [2] → sum = 2  

**Output:**
```
2
```

---

## 🧠 Constraints

- \( 1 \leq n \leq 10^4 \)

---

## ⚙️ Approach

### Step-by-step Logic:

1. Create a **hash map** to count how many numbers have the same digit sum.
2. For each number `i` from 1 to `n`:
   - Compute the **sum of its digits**.
   - Increment the count for that sum in the map.
3. Find the **maximum size** among all groups.
4. Count **how many groups** have this size.
5. Return that count.

---

## 🐍 Python Code

```python
from typing import *
import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Groups numbers from 1 to n by the sum of their digits.
        Returns the number of groups with the largest size.
        """
        hashMap = collections.Counter()
        
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            hashMap[digit_sum] += 1
        
        max_group_size = max(hashMap.values())
        largest_group_count = sum(1 for size in hashMap.values() if size == max_group_size)
        
        return largest_group_count
```

---

## 🧪 Test Cases

```python
def main():
    solution = Solution()
    test_cases = [
        (13, 4),
        (2, 2),
        (24, 4),
        (1, 1),
    ]
    
    for n, expected in test_cases:
        result = solution.countLargestGroup(n)
        print(f"Input: n = {n}\nExpected: {expected}, Got: {result}\n")
```

---

## 📁 Project Structure

```
count_largest_group/
├── main.py      # Complete executable code with test cases
├── README.md    # Problem explanation and approach
```

---

## 🚀 Why This Works

- ✅ Uses a **counter** to group numbers efficiently.
- ✅ Linear time complexity O(n), suitable for \( n \leq 10^4 \)
- ✅ Easy to read and extend.
