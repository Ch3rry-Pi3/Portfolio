# 🏁 **LeetCode 2379: Minimum Recolors to Get K Consecutive Black Blocks**  

## 📌 **Problem Overview**  

You are given a **0-indexed** string `blocks` of length `n`, where each character is either:  
- **'W'** (white block)  
- **'B'** (black block)  

You are also given an integer `k`, which represents the **desired number of consecutive black blocks**.  

### 🎯 **Goal:**  
Find the **minimum number of operations** required to recolor white blocks ('W') into black blocks ('B') so that there is **at least one** occurrence of `k` consecutive black blocks.

## 📖 **Example 1**  

```python
Input: blocks = "WBBBWBBBW", k = 7  
Output: 3  
```

✅ **Explanation:**  
One possible way to get **7 consecutive 'B' blocks** is:  
- **Recolor** the **0th, 3rd, and 4th** blocks  
- The resulting blocks become `"BBBBBBBBW"`  
- The minimum recolors needed = `3`

## 📖 **Example 2**  

```python
Input: blocks = "WBWBBBW", k = 2  
Output: 0  
```

✅ **Explanation:**  
Since `k = 2` and there already exists **2 consecutive 'B' blocks**, no recoloring is required.  
The minimum recolors needed = `0`.

## 📖 **Example 3**  

```python
Input: blocks = "WWWWWW", k = 3  
Output: 3  
```

✅ **Explanation:**  
All blocks are **white ('W')**, so we need to **recolor 3 blocks** to form at least **3 consecutive 'B'**.  
The minimum recolors needed = `3`.

## 🚀 **Approach & Intuition**  

### 🔹 **Sliding Window Technique**  

We use a **sliding window of size `k`** to efficiently track the **minimum number of 'W' blocks** that need to be recolored.

### 🔍 **Steps:**  
1. **Initialise two pointers (`left`, `right`) for a sliding window of size `k`.**  
2. **Count the number of 'W' blocks in the first window of size `k`.**  
3. **Slide the window across `blocks`, updating the count dynamically.**  
4. **Keep track of the minimum number of 'W' blocks found in any window.**  
5. **Return the minimum recolors needed.**

⏳ **Time Complexity:** **O(n)**  
📌 **Why?** We traverse the `blocks` string **once**, updating the count in **constant time O(1)** as the window slides.

## 📝 **Python Implementation**  

```python
from typing import List

class Solution:
    """
    Solution to find the minimum number of recolors needed to get
    at least one occurrence of k consecutive black blocks in a given string.
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Uses a sliding window approach to determine the minimum number of 
        white ('W') blocks that need to be recolored to get at least k consecutive black ('B') blocks.

        :param blocks: str - A binary string consisting of 'W' and 'B' characters.
        :param k: int - The required number of consecutive black blocks.
        :return: int - The minimum number of recolors needed.
        """
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Iterate through the blocks with a sliding window
        for right in range(len(blocks)):
            # Count white blocks in the current window
            if blocks[right] == "W":
                num_whites += 1

            # Once the window reaches size k
            if right - left + 1 == k:
                # Update minimum recolors needed
                num_recolors = min(num_recolors, num_whites)

                # Slide window to the right: remove the leftmost block
                if blocks[left] == "W":
                    num_whites -= 1

                left += 1       # Move left pointer

        return num_recolors
```

## ⏳ **Time Complexity Analysis**  

| **Operation**            | **Complexity** |
|-------------------------|--------------|
| **Sliding Window Traversal**  | **O(n)** |
| **Updating the Count**        | **O(1)** |
| **Overall Complexity**        | **O(n)** ✅ |

📌 **Why is this optimal?**  
- We **only traverse the list once** using the **sliding window**, reducing redundant calculations.
- **Constant space O(1)** is used since we only track `num_whites`.

## 📂 **Project Structure**  

```
minimum_recolors/
├── minimum_recolors.py  # Python solution
├── README.md            # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses an optimal O(n) sliding window approach.**  
✔ **Handles edge cases** where `k` is already satisfied.  
✔ **Easy to implement with simple logic.**  

🚀 **Master the sliding window technique for optimised solutions!**  
