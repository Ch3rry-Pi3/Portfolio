# 📚 LeetCode 1534: Count Good Triplets

## 📌 Problem Overview

You are given:
- An array of integers `arr`
- Three integers `a`, `b`, and `c`

You need to **find the number of "good triplets"** in the array.

### 🛠 Definition of a Good Triplet

A triplet `(arr[i], arr[j], arr[k])` is considered **good** if the following conditions are all satisfied:
- `0 <= i < j < k < arr.length`
- `|arr[i] - arr[j]| <= a`
- `|arr[j] - arr[k]| <= b`
- `|arr[i] - arr[k]| <= c`

Where `|x|` denotes the **absolute value** of `x`.



## ✅ Example

### Example 1:
```text
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4

Explanation:
The 4 good triplets are:
- (3,0,1)
- (3,0,1)
- (3,1,1)
- (0,1,1)
```



### Example 2:
```text
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0

Explanation:
No triplet satisfies all conditions.
```



## 📜 Constraints
- `3 <= arr.length <= 100`
- `0 <= arr[i] <= 1000`
- `0 <= a, b, c <= 1000`



## 🛠️ Approach & Intuition

### 🔍 Step-by-Step:
1. **Brute Force Search**:
   - Iterate over all triplets `(i, j, k)` such that `i < j < k`.
   - For each triplet, check if the three absolute difference conditions are satisfied.
2. **Counting**:
   - If a triplet satisfies all three conditions, increment a counter.
3. **Return the counter** as the final result.

Since `arr.length <= 100`, a brute-force O(n³) solution is acceptable.



## 🧮 Python Code

```python
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        cnt += 1
        return cnt
```



## 📂 Project Structure

```
count_good_triplets/
├── main.py       # Python implementation with test cases
├── README.md     # Problem explanation and solution
```



## 💡 Why This Approach Works

- The number of possible triplets is manageable (at most around 161,700 when n=100).
- Easy to implement and directly maps to the problem description.
- No need for advanced optimizations given the problem constraints.



## 🔥 Additional Notes

- Always ensure you **respect index order**: `i < j < k`.
- Carefully apply **absolute value** when comparing the differences.
- Brute-force is not always bad — **sometimes it's the best fit** when n is small!
