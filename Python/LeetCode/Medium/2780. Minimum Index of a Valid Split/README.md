# 🧮 LeetCode 2780: Minimum Index of a Valid Split

## 📘 Problem Overview

You are given a **0-indexed** integer array `nums` with **one dominant element**.

An element `x` is called **dominant** in an array if it appears **more than half the time**. That is:
> If `nums` has length `n`, then `x` is dominant if `count(x) > n / 2`.

Your task is to **split** the array at an index `i` such that:
- `0 <= i < n - 1`
- Both the **left** subarray `nums[0..i]` and the **right** subarray `nums[i+1..n-1]` have the **same dominant element**.

Return the **minimum index** where such a valid split exists.  
If no valid split is possible, return `-1`.



## ✅ Examples

### Example 1
```python
Input: nums = [1, 2, 2, 2]
Output: 2
```

**Explanation:**
- Split at index `2`: Left = [1, 2, 2], Right = [2]
- Dominant element in both parts is `2`



### Example 2
```python
Input: nums = [2, 1, 3, 1, 1, 7, 1, 2, 1]
Output: 4
```

**Explanation:**
- Dominant element is `1`
- Valid split found at index `4`: [2,1,3,1,1] and [7,1,2,1]



### Example 3
```python
Input: nums = [3,3,3,3,7,2,2]
Output: -1
```

**Explanation:**
- No valid index where both subarrays share the same dominant element.



## 🛠️ Approach & Intuition

### 💡 Strategy:
1. **Find the dominant element** using the **Boyer-Moore Majority Voting Algorithm**.
2. **Count its total frequency** in the array.
3. Iterate through the array:
   - Track its running frequency in the left subarray.
   - Ensure both sides maintain the dominance condition:
     - `left_freq * 2 > (i + 1)`
     - `right_freq * 2 > (n - i - 1)`

If these conditions are met, return the index.

### 🧠 Why It Works:
- The dominance condition must be preserved on both sides.
- We leverage the voting algorithm to reduce time complexity.
- No need for nested loops or brute force!



## 🧪 Python Implementation

```python
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Step 1: Find dominant element
        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1

        # Step 2: Count total occurrences of candidate
        total_count = nums.count(candidate)

        # Step 3: Try to find valid split
        left_count = 0
        for index in range(len(nums)):
            if nums[index] == candidate:
                left_count += 1

            right_count = total_count - left_count

            if left_count * 2 > index + 1 and right_count * 2 > len(nums) - index - 1:
                return index

        return -1
```



## 🧪 Example Runner

```python
def main():
    solution = Solution()
    test_cases = [
        ([1, 2, 2, 2], 2),
        ([2, 1, 3, 1, 1, 7, 1, 2, 1], 4),
        ([3, 3, 3, 3, 7, 2, 2], -1),
    ]
    
    for nums, expected in test_cases:
        result = solution.minimumIndex(nums)
        print(f"Input: {nums} → Output: {result} (Expected: {expected})")

if __name__ == "__main__":
    main()
```



## ⏱️ Time & Space Complexity

| Complexity      | Value          |
|-|-|
| Time Complexity | `O(n)`         |
| Space Complexity| `O(1)`         |



## 📂 Project Structure

```
minimum_valid_split/
├── main.py
└── README.md
```



## 🎯 Key Takeaways

- ✅ Boyer-Moore Voting is a powerful linear-time tool for identifying majority elements.
- ✅ A greedy scan helps validate splits efficiently.
- ✅ Solid practice of dominance logic and prefix-count tracking.
