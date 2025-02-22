# 📊 **LeetCode 2346: Compute the Rank as a Percentage**  

## 📌 **Problem Overview**  
Given a table of students and their **exam marks**, compute the **rank of each student** within their department as a **percentage** using the formula:

\[
\text{percentage} = \frac{(\text{student rank} - 1) \times 100}{\text{total students in department} - 1}
\]

where:  
- **Ranking is determined by descending `mark`** (higher scores get better ranks).
- **Students with the same mark share the same rank**.
- If a **department has only one student**, the percentage should be **0.0**.
- The result should be sorted by **`department_id` and `percentage` in ascending order**.

## 🖼 **Example**  
### **Input: Students Table**
```
+------------+--------------+------+
| student_id | department_id | mark |
+------------+--------------+------+
|     2      |      2       | 650  |
|     2      |      2       | 650  |
|     1      |      1       | 610  |
|     7      |      1       | 530  |
|     3      |      1       | 530  |
+------------+--------------+------+
```

### **Output:**
```
+------------+--------------+------------+
| student_id | department_id | percentage |
+------------+--------------+------------+
|     7      |      1       |     0.0    |
|     3      |      1       |     0.0    |
|     1      |      1       |   100.0    |
|     2      |      2       |     0.0    |
+------------+--------------+------------+
```

✅ **Explanation:**  
1. **Department 1 (`dep_id = 1`)** has **3 students**:
   - `610` (Rank **1**)
   - `530, 530` (Rank **2** for both)
   - Percentage calculation:  
     - **Rank 1** → \(\frac{(1-1) \times 100}{3-1} = 0.0\)
     - **Rank 2** → \(\frac{(2-1) \times 100}{3-1} = 100.0\)
2. **Department 2 (`dep_id = 2`)** has **only 1 student**:
   - **Percentage = 0.0 (by default)**.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Rank, Count Students, Compute Percentage**
1. **Compute `rank` within each department** using `.groupby("department_id")["mark"].rank(method="min", ascending=False)`.
2. **Count the number of students per department** using `.transform("count")`.
3. **Apply the percentage formula**, ensuring a **0.0% for departments with only one student**.
4. **Sort by `department_id` and `percentage` in ascending order**.

## 📝 **Implementation**  

```python
# rank_as_percentage.py

import pandas as pd
import numpy as np

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the rank percentage of each student within their department.

    Args:
        students (pd.DataFrame): Contains student performance data with columns:
            - "student_id" (int): The ID of the student.
            - "department_id" (int): The ID of the department.
            - "mark" (int): The student's exam mark.

    Returns:
        pd.DataFrame: A table containing:
            - "student_id" (int): The ID of the student.
            - "department_id" (int): The department ID.
            - "percentage" (float): The rank as a percentage (rounded to two decimal places).

        The result is sorted by "department_id" and "percentage" in ascending order.
    """
    # Compute rank within each department (higher marks get a better rank)
    students = students.assign(
        rank=students.groupby("department_id")["mark"].rank(method="min", ascending=False),
        num_of_students=students.groupby("department_id")["student_id"].transform("count")
    )

    # Compute percentage based on the formula provided
    students = students.assign(
        percentage=np.where(
            students["num_of_students"] > 1,
            round((students["rank"] - 1) * 100 / (students["num_of_students"] - 1), 2),
            0.0  # If only one student in the department, percentage is 0.0
        )
    )

    # Select required columns and sort by department and percentage
    return students[["student_id", "department_id", "percentage"]].sort_values(["department_id", "percentage"])

```

## ⏳ **Time Complexity Analysis**  

| Operation                              | Complexity |
|----------------------------------------|------------|
| Ranking students within departments    | **O(N log N)** |
| Counting students per department       | **O(N)** |
| Computing percentage                    | **O(N)** |
| Sorting results                         | **O(N log N)** |
| **Overall Complexity**                   | **O(N log N)** ✅ |

> **N = number of students in the dataset**  

## 📂 **Project Structure**  

```
2346. Compute the Rank as a Percentage/
├── rank_as_percentage.py  # Python solution
├── README.md              # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses Pandas `.rank()` function for efficient ranking.**  
✔ **Handles tied ranks correctly using `"min"` ranking method.**  
✔ **Ensures departments with only one student return `0.0%`.**  
✔ **Scales well for large datasets with multiple departments.**  

🚀 **Mastering ranking techniques is essential for performance analysis!** 🔥