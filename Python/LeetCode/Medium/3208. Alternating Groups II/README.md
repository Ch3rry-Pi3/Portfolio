# 🔄 **LeetCode 3208: Alternating Groups II**  

## 📌 **Problem Overview**  

You are given a **circular sequence** of **red (0) and blue (1) tiles**, represented by an array **`colors`**, and an integer **`k`**.  

A **valid alternating group** is any sequence of **k** consecutive tiles in the circle that **strictly alternate** between red and blue.  

- **Alternating means:**  
  - Each tile in the group must be different from its **adjacent** tiles.
  - The **first and last tiles** of the group are also considered adjacent due to the circular structure.  

🔹 **Your Task:** Count the number of alternating groups of **length k** in the circular array.  

## 📝 **Example 1**  
```python
Input: colors = [0,1,0,1,0], k = 3
Output: 3
```
✅ **Explanation:**  
- The valid alternating groups of **length k = 3** are:  
  **[0,1,0]**, **[1,0,1]**, and **[0,1,0]** (circular wrap-around).  
- There are **3** such groups, so we return **3**.

## 📝 **Example 2**  
```python
Input: colors = [1,0,1,0,1,0,1], k = 4
Output: 4
```
✅ **Explanation:**  
- The valid alternating groups are:  
  **[1,0,1,0]**, **[0,1,0,1]**, **[1,0,1,0]**, **[0,1,0,1]**  
- There are **4** such groups.

## 📝 **Example 3**  
```python
Input: colors = [0,0,1,1,0,1,0], k = 3
Output: 3
```
✅ **Explanation:**  
- The valid alternating groups are **[0,1,0]**, **[1,0,1]**, **[0,1,0]**.  
- We return **3**.

## 💡 **Approach & Intuition**  

### 🔹 **Sliding Window with Circular Traversal**  
- Use a **circular traversal** by applying the **modulo operator (`%`)** to handle the **wrap-around condition**.  
- Maintain a **count** of consecutive alternating elements.  
- Whenever we reach a group of length **`k`**, increase the result count.  

🔹 **Key Observations:**  
1. We iterate through **`colors`** while treating it as a **circular array**.  
2. **Modulo (`%`) indexing** ensures that **the last element connects to the first**.  
3. Keep track of a **running count** of alternating sequences.  
4. If a sequence **breaks**, reset the count and restart.  

## 🚀 **Implementation**  

```python
from typing import List

class Solution:
    """
    Solution to count the number of alternating groups of length k in a circular array.
    """

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        Counts the number of alternating groups of size k in a circular sequence of red and blue tiles.

        :param colors: List[int] - A list where colors[i] is 0 (red) or 1 (blue).
        :param k: int - The required length of an alternating group.
        :return: int - The number of valid alternating groups in the circular sequence.
        """
        length = len(colors)
        result = 0
        alternating_elements_count = 1  # Length of current alternating sequence
        last_color = colors[0]  # Previous color

        # Loop through array with circular traversal
        for i in range(1, length + k - 1):
            index = i % length          # Wrap around using modulo

            # Check if current color is the same as the last color
            if colors[index] == last_color:
                # Pattern breaks, reset sequence length
                alternating_elements_count = 1
                last_color = colors[index]
                continue

            # Extend sequence
            alternating_elements_count += 1

            # If sequence length reaches at least k, count it
            if alternating_elements_count >= k:
                result += 1

            last_color = colors[index]

        return result

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Iterating through colors** | **O(n + k)** |
| **Circular traversal using `%`** | **O(1)** |
| **Overall Complexity** | **O(n + k)** ✅ |

🔹 **Why is this efficient?**  
- The algorithm processes each element **once** while maintaining a **sliding window**.  
- **Modulo indexing** ensures **constant-time lookups** for circular traversal.  

## 📂 **Project Structure**  

```
alternating_groups/
├── alternating_groups.py  # Python solution
├── README.md              # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses efficient sliding window technique** for alternating patterns.  
✔ **Handles circular arrays seamlessly** with modulo indexing.  
✔ **Scales well** due to **O(n + k) complexity**.  

🚀 **Master this approach to solve similar problems efficiently!** 🔄🔥  
