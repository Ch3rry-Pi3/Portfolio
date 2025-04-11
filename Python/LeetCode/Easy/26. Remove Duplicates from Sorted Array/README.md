# 📌 LeetCode 26: Remove Duplicates from Sorted Array

## 🧠 Problem Summary

You're given a **sorted array** `nums` in non-decreasing order. Your task is to:

- **Remove the duplicates in-place** so that each unique element appears **only once**.
- **Return the number of unique elements**, `k`.
- The first `k` elements of `nums` must contain the result.
- The remaining elements beyond `k` don’t matter.

> The solution **must not use extra space for another array**.



## ✅ Example

### Input:
```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

### Output:
```
k = 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

### Explanation:
- The first 5 elements of `nums` must be the **unique** values.
- The underscores `_` denote values that can be anything beyond `k`.



## 🧮 Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing order**



## 💡 Approach & Intuition

This problem is efficiently solved using a **two-pointer approach**:

1. **Pointer `i`** scans through the array.
2. **Pointer `insertIndex`** tracks where to place the next unique element.
3. Whenever a **new unique number** is found:
   - We place it at `nums[insertIndex]`.
   - Then increment `insertIndex`.

> Because the array is already sorted, duplicates will always be **next to each other**, which allows this efficient in-place update.



## 🧪 Sample Python Implementation

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
```



## 🧾 Example Usage

```python
nums = [1,1,2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"Unique elements count: {k}")
print(f"Resulting array: {nums[:k]}")
```

### Output:
```
Unique elements count: 2
Resulting array: [1, 2]
```



## 🗂️ Project Structure

```
remove_duplicates_sorted_array/
├── main.py       # Python implementation with test cases
├── README.md     # Problem description and explanation
```



## 📊 Time & Space Complexity

| Complexity      | Value         |
|-||
| Time            | O(n)          |
| Space (extra)   | O(1) — In-place |



## 🌟 Why This Works

- ✅ Exploits **sorted property** of the input array.
- ✅ No additional memory used — all updates are **in-place**.
- ✅ One-pass linear scan for efficiency.



## 🧠 Additional Test Cases

- Empty array → `[]` → returns 0
- All duplicates → `[2,2,2,2]` → returns 1
- All unique → `[1,2,3]` → returns 3