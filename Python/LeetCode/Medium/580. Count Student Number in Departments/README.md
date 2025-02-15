# 📊 **LeetCode 580: Count Student Number in Departments**  

## 📌 **Problem Overview**  
You are given two tables:  
1. **`Student` Table**: Contains information about students, including their `dept_id`.  
2. **`Department` Table**: Contains department names with corresponding `dept_id`.  

Each student belongs to exactly **one department**. Some departments may have **no students**.  

### **Goal**  
For each department in the `Department` table, count the number of students enrolled in it.  
- **Include departments with zero students**.  
- **Sort results**:  
  - **Descending order** by the number of students (`student_number`).  
  - In case of ties, **alphabetically by `dept_name`**.  

## 📊 **Database Schema**  
### **Student Table**  
| Column Name    | Type    | Description                        |
|---------------|--------|------------------------------------|
| `student_id`  | int    | Unique ID for the student         |
| `student_name`| varchar | Name of the student               |
| `gender`      | varchar | Gender of the student             |
| `dept_id`     | int    | Foreign key linking to `Department` |

### **Department Table**  
| Column Name  | Type    | Description                          |
|-------------|--------|--------------------------------------|
| `dept_id`   | int    | Unique department ID                |
| `dept_name` | varchar | Name of the department              |

## 🛠 **Approach**  
1. **Merge the `Department` table with `Student` table** using `dept_id` (Left Join).  
   - This ensures all departments are included, even if they have no students.  
2. **Count the number of students per department** using `.groupby()`.  
3. **Sort the results**:  
   - **Descending order** by student count.  
   - **Alphabetically** by department name in case of a tie.  

## 🚀 **Python Solution**  
```python
import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of students in each department and return the result sorted by:
    - Student count in descending order.
    - Alphabetical order of department name in case of a tie.

    Args:
        student (pd.DataFrame): Contains student details with 'student_id' and 'dept_id'.
        department (pd.DataFrame): Contains department details with 'dept_id' and 'dept_name'.

    Returns:
        pd.DataFrame: A DataFrame with 'dept_name' and 'student_number' sorted accordingly.
    """
    return (
        department
        .merge(student, on="dept_id", how="left")  # Left join to include all departments
        .groupby("dept_name", as_index=False)
        .agg(student_number=("student_id", "count"))  # Count students per department
        .sort_values(by=["student_number", "dept_name"], ascending=[False, True])  # Sort results
    )

```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Student Table**  
| student_id | student_name | gender | dept_id |
|------------|-------------|--------|---------|
| 1          | Jack        | M      | 1       |
| 2          | Jane        | F      | 1       |
| 3          | Mark        | M      | 2       |

#### **Department Table**  
| dept_id | dept_name    |
|---------|-------------|
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |

### **Output**  
```python
   dept_name   student_number
0  Engineering  2
1  Science      1
2  Law          0
```

### **Explanation**  
- **Engineering** has **2 students** (Jack, Jane).  
- **Science** has **1 student** (Mark).  
- **Law** has **0 students**, but is still included in the result.  

Sorting Order:  
1. **Descending** by `student_number`.  
2. **Alphabetically** by `dept_name` in case of ties.  

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge tables | `merge(department, student, how="left")` | **O(N)** |
| Group by department | `groupby("dept_name")` | **O(N)** |
| Count students | `.agg(student_number=("student_id", "count"))` | **O(N)** |
| Sort results | `sort_values(by=["student_number", "dept_name"])` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Ensures all departments are included, even with no students**.  
✔ **Uses efficient Pandas operations** (`merge`, `groupby`, `agg`, `sort_values`).  
✔ **Guaranteed to return correctly sorted results** based on problem constraints.  

🚀 **With this approach, you can quickly determine department sizes in any dataset!** 🎯