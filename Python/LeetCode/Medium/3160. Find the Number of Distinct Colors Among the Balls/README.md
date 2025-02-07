# 🎨 **LeetCode 3160: Find the Number of Distinct Colors Among the Balls**

## 📌 **Overview**
This project solves **LeetCode Problem 3160: Find the Number of Distinct Colors Among the Balls**.  
The goal is to process **a sequence of queries** where balls are **colored dynamically** and return the **number of distinct colors after each query**.

### **Problem Statement**
You are given:
- An integer **`limit`**, representing the **maximum ball index** (balls are labeled from `0` to `limit`).
- A **list of queries**, where each query `[x, y]` assigns **color `y` to ball `x`**.

Initially, all balls are **uncolored**.  
After each query, we return the **number of distinct colors present among the balls**.

🔹 **Constraints:**
- `1 <= limit <= 1000`
- `1 <= queries.length <= 10⁵`
- `1 <= queries[i][1] <= 10⁶`

## 🎯 **Example Walkthrough**
### **Example 1**
```python
Input: limit = 4, queries = [[1,4], [2,5], [1,3], [3,4]]
Output: [1, 2, 2, 3]
```
#### **Step-by-Step Breakdown**
1️⃣ **After query `[1,4]`**  
   - Ball `1` is colored **4**  
   - **Distinct Colors: {4}** → **Count: `1`**  
2️⃣ **After query `[2,5]`**  
   - Ball `2` is colored **5**  
   - **Distinct Colors: {4,5}** → **Count: `2`**  
3️⃣ **After query `[1,3]`**  
   - Ball `1` is now colored **3** (overwriting `4`)  
   - **Distinct Colors: {3,5}** → **Count: `2`**  
4️⃣ **After query `[3,4]`**  
   - Ball `3` is colored **4**  
   - **Distinct Colors: {3,5,4}** → **Count: `3`**  

**Final Output:** `[1, 2, 2, 3]` ✅

## 🎞 **Visual Representation**
To provide **clear intuition**, here’s an animation following the above example:

![Distinct Colors Animation](images/distinct_colours.gif)

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ Each ball can only have **one active color** at any time.  
✔ If a ball is **recolored**, the previous color **must be removed** if no other balls have it.  
✔ We can efficiently track the **number of balls per color** using a **dictionary** (`colour_map`).  
✔ Another dictionary (`ball_map`) tracks **which color each ball currently has**.

## 📝 **Step-by-Step Approach**
### **1️⃣ Use a Dictionary to Track Colors**
- **`ball_map[ball]`** → Stores **current color** of each ball.
- **`colour_map[color]`** → Stores **count of balls** with this color.

### **2️⃣ Process Each Query**
- If the ball already has a color, **reduce its count**.
- If a color count drops to `0`, remove it.
- Assign the new color to the ball and update its count.
- Append the number of distinct colors to the result list.

### **3️⃣ Return Result**
- The final list contains the **distinct color count after each query**.

## **💡 Implementation**
```python
from typing import List

class Solution:
    """
    This class provides an implementation of the 'Find the Number of Distinct Colors Among the Balls' problem.

    The function `queryResults` processes a sequence of queries where balls are colored, 
    and returns the number of distinct colors after each query.
    """

    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Determines the number of distinct colors among balls after each query.

        :param limit: Integer representing the highest ball index.
        :param queries: List of queries where each query is of the form [x, y], 
                        meaning ball x is assigned color y.
        :return: List of integers where result[i] represents the number of distinct colors 
                 after processing the i-th query.
        """
        n = len(queries)
        result = []                                                     # Stores the number of distinct colors after each query
        colour_map = {}                                                 # Tracks the count of each color
        ball_map = {}                                                   # Tracks the color assigned to each ball

        # Iterate through each query
        for i in range(n):
            ball, colour = queries[i]                                   # Extract ball index and new color from query

            # If the ball is already colored, decrement the count of the previous color
            if ball in ball_map:
                prev_colour = ball_map[ball]
                colour_map[prev_colour] -= 1                            # Reduce count of previous color

                # If no balls have this color anymore, remove it from colour_map
                if colour_map[prev_colour] == 0:
                    del colour_map[prev_colour]

            # Assign the new color to the ball
            ball_map[ball] = colour
            colour_map[colour] = colour_map.get(colour, 0) + 1          # Increase count of the new color

            # Append the number of distinct colors to the result list
            result.append(len(colour_map))

        return result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Dictionary-based (`O(n)`)** | **O(n)** ✅ | **O(k)** ✅ (where `k` is the number of distinct colors) |

- **Each query processes at most one ball**, making it **O(n)**.
- **Dictionaries store only necessary information**, making space **O(k) in the worst case**.

## 🏗 **Project Structure**
```
3160. Find the Number of Distinct Colors Among the Balls/
├── number_distinct_ball_colours.py    # Python implementation of the solution
├── README.md                           # Detailed explanation & walkthrough
├── images/
│   ├── distinct_colours.gif            # Animated example for visualisation
```

✨ **Master real-time color tracking with an efficient `O(n)` approach!** 🚀  