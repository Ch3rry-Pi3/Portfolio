# 🧮 LeetCode 3375: Minimum Operations to Make Array Values Equal to K

## 📌 Problem Overview

You are given an integer array `nums` and an integer `k`. Your task is to transform all values in the array so that **each element becomes exactly `k`** by following a defined operation any number of times.



### 🔧 Operation Definition

You can perform the following operation any number of times:

1. Choose an integer `h` that is **valid**:
   - A valid integer `h` is such that all elements in the array **strictly greater than `h` are equal**.

2. For each index `i` where `nums[i] > h`, set `nums[i] = h`.



### 🧠 Goal

Return the **minimum number of operations** required to make **every element in `nums` equal to `k`**.

- If it is **impossible** to make all elements equal to `k`, return `-1`.



## ✅ Constraints

- All values in `nums` must be **greater than or equal to `k`** for a solution to exist.
- All values **strictly greater than `k`** must be **equal** before each reduction step.



## 💡 Examples

### Example 1

**Input:**
```python
nums = [5, 2, 5, 4, 5]
k = 2
```

**Output:** `2`

**Explanation:**
- Operation 1: Reduce all 5s and 4 to 4  
- Operation 2: Reduce all 4s to 2  
- All elements are now equal to 2.



### Example 2

**Input:**
```python
nums = [2, 1, 2]
k = 2
```

**Output:** `-1`

**Explanation:**
- The array contains a value (1) that is **less than k**, so it's impossible to reach k.



### Example 3

**Input:**
```python
nums = [9, 7, 5, 3]
k = 1
```

**Output:** `4`

**Explanation:**
- Reduce values in the order: 9 → 7 → 5 → 3 → 1  
- 4 steps required.



## 🛠 Approach & Intuition

1. Initialize a set to track **distinct values greater than `k`**.
2. If any number is **less than `k`**, it's impossible → return `-1`.
3. For each number `x` in `nums`:
   - If `x > k`, add it to the set of distinct reductions needed.
4. The **number of operations** required is the size of this set.



## 🧪 Test Cases

| Input                    | Output | Explanation                                      |
|-|--|--|
| `[5, 2, 5, 4, 5]`, `2`   | `2`    | Reduce 5 → 4, then 4 → 2                         |
| `[2, 1, 2]`, `2`         | `-1`   | 1 is smaller than k → impossible                 |
| `[9, 7, 5, 3]`, `1`      | `4`    | Reduce 9 → 7 → 5 → 3 → 1                         |
| `[3, 3, 3]`, `3`         | `0`    | Already valid                                    |
| `[4, 5, 6, 7]`, `3`      | `4`    | Four unique values need reduction               |



## 🧾 Python Code

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
```



## 🗂 Project Structure

```
min_operations_to_make_values_k/
├── main.py        # Contains the main solution and test cases
├── README.md      # This file - detailed explanation and usage
```



## 🚀 Why This Works

- Simple **set-based counting** solution.
- Efficient `O(n)` time complexity.
- Carefully handles **edge cases** (e.g. values less than `k`).
