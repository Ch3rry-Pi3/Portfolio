# 📚 **LeetCode 2989: Class Performance**  

## 📌 **Problem Overview**  
Given a table of students' scores across **three assignments**, compute the **difference between the highest and lowest total scores** obtained by students in the class.

### **Key Requirements:**  
- Compute the **total score** for each student as: 

  \[
  \text{total\_score} = \text{assignment1} + \text{assignment2} + \text{assignment3}
  \]
  
- Find the **difference between the highest and lowest total scores**.
- Return the result as a **single row** with the column **`difference_in_score`**.

## 🖼 **Example**  
### **Input: Scores Table**
```
+------------+--------------+-------------+-------------+-------------+
| student_id | student_name | assignment1 | assignment2 | assignment3 |
+------------+--------------+-------------+-------------+-------------+
|    309     | Owen         |     88      |     47      |     87      |
|    321     | Claire       |     98      |     51      |     43      |
|    328     | Julian       |    100      |     64      |     43      |
|    111     | Peyton       |     60      |     45      |     64      |
|    896     | David        |     32      |     53      |     29      |
|    235     | Camila       |     31      |     53      |     69      |
+------------+--------------+-------------+-------------+-------------+
```

### **Output:**
```
+-------------------+
| difference_in_score |
+-------------------+
|        111       |
+-------------------+
```

✅ **Explanation:**  
1. **Calculate `total_score` for each student:**  
   ```
   Owen:    88 + 47 + 87  = 222
   Claire:  98 + 51 + 43  = 192
   Julian: 100 + 64 + 43  = 207
   Peyton:  60 + 45 + 64  = 169
   David:   32 + 53 + 29  = 114
   Camila:  31 + 53 + 69  = 153
   ```
2. **Find the highest and lowest total scores:**  
   - **Highest total score** = **222** (Owen)  
   - **Lowest total score** = **111** (David)  
   - **Difference** = `222 - 111 = 111`

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Compute Totals, Then Find the Difference**
1. **Compute `total_score` for each student** (sum of all three assignments).  
2. **Find the highest and lowest total scores** across all students.  
3. **Compute the difference** between the maximum and minimum total scores.  
4. **Return the result as a single-row DataFrame**.

## 📝 **Implementation**  

```python
# class_performance.py

import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the difference between the highest and lowest total scores 
    obtained by students in the class.

    Args:
        scores (pd.DataFrame): Contains student performance data with columns:
            - "student_id" (int): The ID of the student.
            - "student_name" (str): The name of the student.
            - "assignment1" (int): Score for Assignment 1.
            - "assignment2" (int): Score for Assignment 2.
            - "assignment3" (int): Score for Assignment 3.

    Returns:
        pd.DataFrame: A table containing:
            - "difference_in_score" (int): The difference between the highest 
              and lowest total scores in the class.
    """
    return (
        scores
        # Ensure missing values are treated as zero
        .fillna(0)
        # Compute the total score for each student
        .assign(total_score=lambda x: x["assignment1"] + x["assignment2"] + x["assignment3"])
        # Compute the difference between the highest and lowest total scores
        .assign(difference_in_score=lambda x: x["total_score"].max() - x["total_score"].min())
        # Keep only the required column
        [["difference_in_score"]]
        # Ensure only a single-row output
        .head(1)
    )
```

## ⏳ **Time Complexity Analysis**  

| Operation                                | Complexity |
|------------------------------------------|------------|
| Computing total scores for all students  | **O(N)** |
| Finding max and min total scores         | **O(N)** |
| Returning a single row result            | **O(1)** |
| **Overall Complexity**                    | **O(N)** ✅ |

> **N = number of students in the dataset**  

## 📂 **Project Structure**  

```
2989. Class Performance/
├── class_performance.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Simple Pandas operations** (`assign`, `max`, `min`) make the solution efficient.  
✔ **O(N) complexity** ensures scalability for large student datasets.  
✔ **Aggregation techniques like `max()` and `min()` are crucial for performance analysis.**  

🚀 **Mastering data aggregation techniques is key for statistical analysis!** 🔥