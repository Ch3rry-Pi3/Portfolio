# 🔺 **LeetCode 3053: Classifying Triangles by Lengths**

## 📌 **Problem Statement**
Given a table representing the **three sides** of a triangle, classify each triangle based on its side lengths.

Each triangle can be categorised into one of the following types:

- **Equilateral**: All three sides are of **equal** length.
- **Isosceles**: Exactly **two** sides are of equal length.
- **Scalene**: All three sides have **different** lengths.
- **Not A Triangle**: The three given sides **do not satisfy** the triangle inequality theorem.

> **Triangle Inequality Theorem**:  
> A set of three numbers **A, B, C** forms a valid triangle if and only if:  
> - \( A + B > C \)  
> - \( A + C > B \)  
> - \( B + C > A \)  

The task is to classify each set of given side lengths accordingly.

## 🛠 **Approach**
To solve this problem efficiently:
1. **Check if the sides form a valid triangle**:
   - If **triangle inequality fails**, classify as `"Not A Triangle"`.
2. **Classify triangle types**:
   - If all three sides are **equal**, it's `"Equilateral"`.
   - If exactly **two sides** are equal, it's `"Isosceles"`.
   - If all three sides are **different**, it's `"Scalene"`.
3. **Vectorised Implementation** using `numpy.where()` for efficient classification.

## 🚀 **Python Solution**
```python
import pandas as pd
import numpy as np

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    """
    Classifies triangles based on their side lengths.

    Args:
        triangles (pd.DataFrame): DataFrame with columns ['A', 'B', 'C']
                                  representing the side lengths of triangles.

    Returns:
        pd.DataFrame: A DataFrame with a single column ['triangle_type']
                      containing the classification of each triangle.
    """

    # Check if the given sides can form a valid triangle using the triangle inequality theorem
    invalid_triangle = (
        (triangles['A'] + triangles['B'] <= triangles['C']) |
        (triangles['B'] + triangles['C'] <= triangles['A']) |
        (triangles['A'] + triangles['C'] <= triangles['B'])
    )

    # Classify the triangles using NumPy's vectorised `where` function
    triangles['triangle_type'] = np.where(
        invalid_triangle, 'Not A Triangle',
        np.where(
            (triangles['A'] == triangles['B']) & (triangles['B'] == triangles['C']),
            'Equilateral',
            np.where(
                (triangles['A'] == triangles['B']) |
                (triangles['B'] == triangles['C']) |
                (triangles['A'] == triangles['C']),
                'Isosceles',
                'Scalene'
            )
        )
    )

    return triangles[['triangle_type']]
```

## 📌 **Example Walkthrough**

### ✅ **Example 1**
#### **Input:**
| A  | B  | C  |
|----|----|----|
| 5  | 5  | 8  |
| 10 | 10 | 10 |
| 6  | 6  | 9  |
| 7  | 8  | 9  |

#### **Output:**
| triangle_type  |
|---------------|
| Isosceles     |
| Equilateral   |
| Isosceles     |
| Scalene       |

#### **Explanation:**
- **Row 1:** Two equal sides → `"Isosceles"`
- **Row 2:** All sides equal → `"Equilateral"`
- **Row 3:** Two equal sides → `"Isosceles"`
- **Row 4:** All sides different → `"Scalene"`

## ⏳ **Complexity Analysis**
| Operation | Complexity |
|-----------|-----------|
| Triangle Inequality Check | **O(1)** |
| Triangle Type Classification | **O(1)** |
| Overall Complexity | **O(N)** (for N triangles) |

💡 **Why is this efficient?**  
- Uses **vectorised** NumPy operations instead of row-wise loops.
- Runs in **O(N) time**, making it highly efficient.

## 🏆 **Why This Approach?**
✔ **Handles edge cases** (e.g., invalid triangles).  
✔ **Optimised using NumPy** instead of iterative loops.  
✔ **Scales efficiently** for large datasets.  

🚀 **With this approach, you can efficiently classify any set of triangles!** 🎯
