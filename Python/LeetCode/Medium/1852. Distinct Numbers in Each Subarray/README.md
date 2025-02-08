# 🔢 **LeetCode 1852: Distinct Numbers in Each Subarray**

## 📌 **Problem Overview**
Given an integer array `nums` and an integer `k`, the goal is to construct an array `ans` of size `n - k + 1` where:

\[
ans[i] = \text{number of distinct elements in the subarray } nums[i:i+k-1]
\]

**Return the array `ans`.**

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
nums = [1, 2, 3, 2, 2, 1, 3]
k = 3
```
#### **Output:**
```python
[3, 2, 2, 2, 3]
```
#### **Explanation:**
We analyse each subarray of length `k=3`:
- `nums[0:3] = [1, 2, 3] → distinct count = 3`
- `nums[1:4] = [2, 3, 2] → distinct count = 2`
- `nums[2:5] = [3, 2, 2] → distinct count = 2`
- `nums[3:6] = [2, 2, 1] → distinct count = 2`
- `nums[4:7] = [2, 1, 3] → distinct count = 3`

Thus, the result is `[3, 2, 2, 2, 3]`.

### **Example 2**
#### **Input:**
```python
nums = [1, 1, 1, 1, 2, 3, 4]
k = 4
```
#### **Output:**
```python
[1, 2, 3, 4]
```
#### **Explanation:**
- `nums[0:4] = [1, 1, 1, 1] → distinct count = 1`
- `nums[1:5] = [1, 1, 1, 2] → distinct count = 2`
- `nums[2:6] = [1, 1, 2, 3] → distinct count = 3`
- `nums[3:7] = [1, 2, 3, 4] → distinct count = 4`

Result: `[1, 2, 3, 4]`.

## 🛠 **Approach**
This problem can be efficiently solved using the **Sliding Window** technique:

1. **Use a frequency dictionary** to track the number of occurrences of elements in the current window.
2. **Initialise the first window of size `k`** and compute the number of distinct elements.
3. **Slide the window**:
   - Remove the leftmost element.
   - Add the new rightmost element.
   - Update the count of distinct elements.
4. **Store the distinct element count** for each window in the result.

This approach runs in **O(N) time complexity** due to efficient dictionary operations.

## 🚀 **Python Solution**
```python
from typing import List

class Solution:
    """
    A class to find the number of distinct numbers in each subarray of length k.
    """

    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        """
        Computes the number of distinct elements in each subarray of size k.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The size of the subarray.

        Returns:
            List[int]: A list containing the number of distinct elements in each subarray.
        """

        len_nums = len(nums)
        answer = [0] * (len_nums - k + 1)

        # Dictionary to track frequency of numbers in current window
        freq = {}

        # Initialise first window
        for num in nums[:k]:
            freq[num] = freq.get(num, 0) + 1
        answer[0] = len(freq)

        # Slide the window and update counts
        for pos in range(k, len_nums):
            # Remove leftmost element from the window
            left = nums[pos - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

            # Add rightmost element to the window
            right = nums[pos]
            freq[right] = freq.get(right, 0) + 1

            # Store the count of distinct elements
            answer[pos - k + 1] = len(freq)

        return answer
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Initialise dictionary | `freq = {}` | **O(1)** |
| First window processing | `for num in nums[:k]` | **O(k)** |
| Sliding window updates | `for pos in range(k, len_nums)` | **O(N - k)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 📁 **Project Structure**
```
distinct_numbers/
├── distinct_numbers.py   # Python solution
├── README.md             # Documentation
```

## 🏆 **Why This Works**
✔ **Sliding Window Technique** ensures optimal efficiency.  
✔ **Dictionary-based frequency tracking** enables fast updates.  
✔ **O(N) time complexity** ensures it scales well for large inputs.  

🚀 **Now you can efficiently compute distinct numbers in each subarray!** 🎯