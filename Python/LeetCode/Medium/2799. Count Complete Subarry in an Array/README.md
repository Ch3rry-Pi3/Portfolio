# 📘 LeetCode 2799: Count Complete Subarrays in an Array

## 📌 Problem Overview

You are given an array of **positive integers** called `nums`.

We define a subarray of `nums` to be **complete** if:
- The number of **distinct elements** in the subarray is equal to the number of distinct elements in the **entire array**.

Your task is to **return the number of complete subarrays**.



## ✅ Example

### Example 1:
**Input:**  
`nums = [1, 3, 1, 2, 2]`  
**Output:** `4`  
**Explanation:**  
Complete subarrays are:
- `[1, 3, 1, 2]`
- `[1, 3, 1, 2, 2]`
- `[3, 1, 2]`
- `[3, 1, 2, 2]`



### Example 2:
**Input:**  
`nums = [5, 5, 5, 5]`  
**Output:** `10`  
**Explanation:**  
Every subarray is complete because the array only contains one distinct number.



## 🛠 Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2000`



## 🧠 Approach & Intuition

### Key Insight:
A complete subarray must contain **all unique elements** that appear in the full array.

### Strategy:
- First, calculate how many **distinct elements** are in the full array.
- Use a **sliding window** with a frequency map (`cnt`) to track distinct elements in the current subarray.
- Move the window while counting how many suffixes starting at the current `left` index form complete subarrays.

### Time Complexity:
- **O(n)** for the main loop
- **O(n)** to compute the number of distinct elements



## 🧪 Sample Test Cases

| Input                    | Output | Notes                                             |
|-|--||
| `[1, 3, 1, 2, 2]`        | 4      | 4 complete subarrays exist                       |
| `[5, 5, 5, 5]`           | 10     | All subarrays are complete                       |
| `[1, 2, 3, 4]`           | 10     | Every subarray with all 4 elements is complete   |
| `[2]`                   | 1      | Single-element array → single complete subarray |
| `[1, 1, 1]`             | 6      | All possible subarrays are complete              |



## 🧾 Python Implementation

```python
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        cnt = {}
        n = len(nums)
        right = 0
        distinct = len(set(nums))

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                cnt[remove] -= 1
                if cnt[remove] == 0:
                    cnt.pop(remove)

            while right < n and len(cnt) < distinct:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1

            if len(cnt) == distinct:
                res += n - right + 1

        return res
```



## 📂 Project Structure

```
count_complete_subarrays/
├── main.py       # Implementation and test cases
├── README.md     # Problem description and explanation
```



## 🚀 Why This Works

- Efficient sliding window ensures we don't reprocess unnecessary parts of the array.
- Frequency map ensures fast checks on distinct element counts.
- Handles edge cases like all duplicates or single-element arrays seamlessly.