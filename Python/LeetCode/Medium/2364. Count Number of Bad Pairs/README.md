# 🔢 **LeetCode 2364: Count Number of Bad Pairs**  

## 📌 **Problem Overview**  
We are given a **0-indexed** integer array `nums`, and we need to count **bad pairs**.  

A **bad pair** is defined as a pair of indices `(i, j)` where:  
- `i < j`  
- `j - i ≠ nums[j] - nums[i]`  

The goal is to return **the total number of bad pairs** in `nums`.

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
```python
nums = [4, 1, 3, 3]
```
#### **Output:**  
```python
5
```
#### **Explanation:**  
The following are the **bad pairs**:  
- `(0,1)`: `1 - 0 != 1 - 4`  
- `(0,2)`: `2 - 0 != 3 - 4`  
- `(0,3)`: `3 - 0 != 3 - 4`  
- `(1,2)`: `2 - 1 != 3 - 1`  
- `(2,3)`: `3 - 2 != 3 - 3`  

Total **bad pairs** = `5`.  

### **Example 2**  
#### **Input:**  
```python
nums = [1, 2, 3, 4, 5]
```
#### **Output:**  
```python
0
```
#### **Explanation:**  
There are **no bad pairs** because each pair satisfies `j - i == nums[j] - nums[i]`.

## 🛠 **Approach**  

### 🔹 **Key Insight**  
We can rearrange the condition:  
\[
j - i \neq nums[j] - nums[i]
\]
which simplifies to:  
\[
i - nums[i] \neq j - nums[j]
\]

This means that **good pairs** have the same `(i - nums[i])` value.  
- If we **count good pairs**, then we can compute bad pairs as:
\[
\text{total pairs} - \text{good pairs}
\]

### 🔹 **Algorithm**  

1. **Initialise Variables:**  
   - `bad_pairs = 0`: Keeps track of the total bad pairs count.  
   - `diff_count = {}`: A dictionary to store the count of `(i - nums[i])`.  

2. **Iterate Through `nums`:**  
   - Compute `diff = i - nums[i]`.  
   - **Count good pairs**: Use `diff_count` to count how many times this difference has appeared.  
   - **Update bad pairs**:  
     \[
     \text{bad pairs} += \text{index} - \text{good pairs count}
     \]
   - Store the frequency of `diff` in `diff_count`.  

3. **Return `bad_pairs`**  

## 🚀 **Python Solution**  
```python
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        Counts the number of bad pairs in the given list.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The total number of bad pairs.
        """
        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            # Count of previous positions with the same difference
            good_pairs_count = diff_count.get(diff, 0)

            # Total possible pairs minus good pairs = bad pairs
            bad_pairs += pos - good_pairs_count

            # Update count of positions with this difference
            diff_count[diff] = good_pairs_count + 1

        return bad_pairs
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Iterating over `nums` | `for pos in range(len(nums))` | **O(N)** |
| Dictionary lookups and updates | `diff_count.get(diff, 0)`, `diff_count[diff] = x` | **O(1) avg** |
| **Total Complexity** | **O(N) time, O(N) space** | ✅ Efficient |

## 📁 **Project Structure**  
```
bad_pairs/
├── bad_pairs.py   # Python solution
├── README.md      # Documentation
```

## 🏆 **Why This Works**  
✔ Uses **hash maps** for efficient counting.  
✔ **Linear time complexity** ensures fast execution.  
✔ **Handles large inputs efficiently**.

🚀 **With this approach, you can efficiently count bad pairs in an array!** 🎯