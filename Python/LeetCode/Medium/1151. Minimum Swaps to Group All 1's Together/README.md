# 🔄 **LeetCode 1151: Minimum Swaps to Group All 1's Together**  

## 📌 **Problem Overview**  

Given a **binary array** `data`, return the **minimum number of swaps** required to group all `1`s present in the array **together in any place** in the array.  

**Constraints:**  
- `1 <= data.length <= 10⁵`
- `data[i]` is either `0` or `1`.

## 📝 **Example 1**  
```python
Input: data = [1,0,1,0,1]
Output: 1
```
✅ **Explanation:**  
- There are **three** ways to group all `1`s together:
  - `[1,1,1,0,0]` (1 swap)
  - `[0,1,1,1,0]` (2 swaps)
  - `[0,0,1,1,1]` (1 swap)  
- The **minimum swaps required is 1**.

## 📝 **Example 2**  
```python
Input: data = [0,0,1,0]
Output: 0
```
✅ **Explanation:**  
- Since there is **only one `1`**, no swaps are required.

## 📝 **Example 3**  
```python
Input: data = [1,0,1,0,1,0,1,1,0,1]
Output: 3
```
✅ **Explanation:**  
- One possible solution that **uses 3 swaps** is:  
  `[0,0,0,0,1,1,1,1,1,1]`.

## 🚀 **Approach & Intuition**  

### 🔹 **Sliding Window Technique**
1. **Find the total count of `1`s** in the array (let's call it `ones`).
2. **Use a sliding window** of size `ones` to count how many `1`s exist in any contiguous window of that size.
3. **Find the maximum number of `1`s** in a window of size `ones`.
4. **The answer is `ones - max_ones_in_window`**, since we only need to swap `0`s with `1`s to make the window full of `1`s.

🔹 **Why is this optimal?**  
- Instead of **sorting or brute force swaps**, we use a **fixed window size** and track `1`s efficiently in **O(n) time complexity**.

## 📝 **Implementation**  

```python
from typing import List

class Solution:
    """
    Solution to find the minimum number of swaps required to group all 1's together in a binary array.
    """

    def minSwaps(self, data: List[int]) -> int:
        """
        Uses a sliding window approach to determine the minimum number of swaps 
        needed to group all 1's together in any contiguous subarray.

        :param data: List[int] - A binary array containing 0's and 1's.
        :return: int - The minimum number of swaps required.
        """
        ones = sum(data)  # Total number of 1's in the array
        cnt_one = max_one = 0
        left = right = 0

        while right < len(data):
            # Add the rightmost element to the window count
            cnt_one += data[right]
            right += 1

            # Maintain a window of size 'ones'
            if right - left > ones:
                # Remove the leftmost element from the window count
                cnt_one -= data[left]
                left += 1

            # Track the maximum number of 1's found in any window
            max_one = max(max_one, cnt_one)

        # Minimum swaps needed to group all 1's together
        return ones - max_one
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Calculating total `1`s** | **O(n)** |
| **Sliding window scan** | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ |

🔹 **Why is this optimal?**  
- **Single pass sliding window approach** ensures minimal operations.  
- **Avoids unnecessary swaps and brute-force operations.**  

## 📂 **Project Structure**  

```
minimum_swaps/
├── minimum_swaps.py  # Python solution
├── README.md         # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Sliding Window** approach reduces complexity from **O(n²) to O(n)**.  
✔ **Greedy strategy** ensures minimal swaps by maximising `1`s in a fixed window.  
✔ **Handles large constraints efficiently** within **O(n) time complexity**.  

🚀 **Master this technique for array manipulation problems!** 🔥  
