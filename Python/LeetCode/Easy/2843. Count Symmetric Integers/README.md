# 🧮 LeetCode 2843: Count Symmetric Integers

## 📘 Problem Overview

You are given two integers:  
- `low`: The starting point of a range.  
- `high`: The ending point of a range.  

A **symmetric integer** is an integer with an **even number of digits** such that the **sum of the first half** of its digits equals the **sum of the second half**.  

🔸 **Important constraint:**  
- Numbers with **odd number of digits** are **never symmetric**.



## ✅ Objective

Return the **number of symmetric integers** in the inclusive range **[low, high]**.



## 🧠 Example

### Example 1
```
Input: low = 1, high = 100  
Output: 9  
Explanation: The symmetric integers are: 11, 22, 33, 44, 55, 66, 77, 88, 99
```

### Example 2
```
Input: low = 1200, high = 1230  
Output: 4  
Explanation: The symmetric integers are: 1203, 1212, 1221, 1230
```



## 🛠️ Approach

We iterate through each number in the given range:

1. **Check if the number has an even number of digits**:
   - For 2-digit numbers: just check if divisible by 11 (e.g. 11, 22...99).
   - For 4-digit numbers: compute left and right digit sums.
2. **Split the number** into two halves.
3. **Compare the digit sums** of both halves.
4. **Increment the counter** if it is symmetric.



## 🧪 Test Cases

| Input `(low, high)` | Output | Notes |
||--|-|
| (1, 100)            | 9      | Only 2-digit symmetric numbers |
| (1200, 1230)        | 4      | Valid 4-digit symmetric numbers |
| (1000, 1001)        | 0      | No symmetric numbers |
| (10, 10)            | 0      | Only one 2-digit number that is not symmetric |
| (1000, 9999)        | 90     | There are exactly 90 4-digit symmetric integers |



## 🧾 Python Implementation

```python
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            elif 1000 <= a < 10000:
                left = a // 1000 + (a % 1000) // 100
                right = (a % 100) // 10 + a % 10
                if left == right:
                    res += 1
        return res
```



## 🧱 Directory Structure

```
count_symmetric_integers/
├── main.py       # Full solution with test cases
├── README.md     # Problem description and solution explanation
```



## 📌 Complexity

- **Time Complexity:** O(n), where `n` is `high - low + 1`
- **Space Complexity:** O(1), using only counters and arithmetic
