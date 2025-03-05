# 🔢 **LeetCode 2579: Count Total Number of Colored Cells**  

## 📌 **Problem Overview**  

You are given a **positive integer** `n`, representing the number of minutes in a **2D infinite grid** where you must color unit cells **blue** following these rules:  

- **At `t = 1` (minute 1):** Color any arbitrary unit cell blue.  
- **At each minute `t > 1`:** Color **every uncolored cell** that **touches** a blue cell.  

**Return the total number of colored cells after `n` minutes.**  

## 📝 **Example 1**  
```python
Input: n = 1
Output: 1
```
✅ **Explanation:**  
- At `t = 1`, we color **one** cell blue.  
- Since no other cells exist, the total number of colored cells is `1`.  

## 📝 **Example 2**  
```python
Input: n = 2
Output: 5
```
✅ **Explanation:**  
- At `t = 1`, **1** central cell is colored.  
- At `t = 2`, **4** surrounding cells are colored.  
- Total: `1 + 4 = 5` colored cells.  

## 🚀 **Approach & Intuition**  

### 🔹 **Mathematical Formula for Growth**  
- The **growth pattern follows a quadratic sequence** as the grid expands **outwards** symmetrically.  
- **Pattern Observation:**  
  - `t = 1`: **1** cell  
  - `t = 2`: **5** cells  
  - `t = 3`: **13** cells  
  - `t = 4`: **25** cells  

- **General Formula:**  

  \[
  \text{Total Colored Cells} = 1 + 4 \times \frac{n(n-1)}{2}
  \]

  - The term `4 × (n(n-1) / 2)` represents the additional layers formed around the **initial** center cell.

## 📝 **Implementation**  

```python
class Solution:
    """
    Solution to count the total number of colored cells in an infinite 2D grid after n minutes.
    """

    def coloredCells(self, n: int) -> int:
        """
        Computes the number of colored cells after n minutes.

        :param n: int - The number of minutes.
        :return: int - The total number of colored cells.
        """
        return 1 + 4 * n * (n - 1) // 2
```

---

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Mathematical Formula Calculation** | **O(1)** ✅ |

🔹 **Why is this optimal?**  
- The **direct formula computation** avoids loops, making it **constant-time O(1)**.  
- It scales efficiently up to **n = 100,000**.  

## 📂 **Project Structure**  

```
count_colored_cells/
├── count_colored_cells.py  # Python solution
├── README.md               # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Mathematical formula derivation simplifies the problem**.  
✔ **O(1) time complexity** ensures the solution is optimal.  
✔ **Handles large values efficiently** without loops or recursion.  

🚀 **Master this technique for pattern-based sequence problems!** 🔥  
