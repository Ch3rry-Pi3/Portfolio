# 🎯 **LeetCode 2298: Tasks Count in the Weekend**  

## 📌 **Problem Overview**  
Given a dataset of task submissions, the goal is to **count**:  
✅ The number of tasks **submitted on weekends (Saturday, Sunday)** as `weekend_cnt`.  
✅ The number of tasks **submitted on working days (Monday - Friday)** as `working_cnt`.  

The **result** should contain **only one row** with both counts.

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**
| task_id | assignee_id | submit_date |
|---------|------------|-------------|
| 1       | 3          | 2022-06-13  |
| 2       | 6          | 2022-06-14  |
| 3       | 6          | 2022-06-15  |
| 4       | 3          | 2022-06-18  |
| 5       | 7          | 2022-06-18  |
| 6       | 7          | 2022-06-19  |
| 7       | 3          | 2022-06-19  |

#### **Output:**
| weekend_cnt | working_cnt |
|-------------|------------|
| 3           | 3          |

#### **Explanation:**
- **Weekend tasks** (`weekend_cnt`):  
  ✅ `2022-06-18` (Saturday) → 2 tasks.  
  ✅ `2022-06-19` (Sunday) → 1 task.  
  **Total = 3**
- **Working day tasks** (`working_cnt`):  
  ✅ `2022-06-13` (Monday), `2022-06-14` (Tuesday), `2022-06-15` (Wednesday).  
  **Total = 3**  

## 🚀 **Approach Explanation**  

### **1️⃣ Classifying Days**
Each task's **submission date** is classified as:  
- **"weekend"** if `submit_date.weekday()` is **5 (Saturday) or 6 (Sunday)**.  
- **"working"** if `submit_date.weekday()` is **between 0 (Monday) and 4 (Friday)**.  

### **2️⃣ Counting the Tasks**
We **group** the tasks by their classification and **count** occurrences.

## 📝 **Python Solution**  
```python
import pandas as pd
import numpy as np

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of tasks submitted during weekends and working days.

    - Weekend tasks: Submitted on Saturday or Sunday.
    - Working day tasks: Submitted on Monday to Friday.

    Args:
        tasks (pd.DataFrame): Contains columns:
            - "task_id" (int): Unique task ID.
            - "assignee_id" (int): ID of the assigned person.
            - "submit_date" (datetime): Task submission date.

    Returns:
        pd.DataFrame: A single-row DataFrame with:
            - "weekend_cnt": Number of weekend submissions.
            - "working_cnt": Number of working day submissions.
    """
    tasks["status"] = np.where(tasks["submit_date"].dt.weekday >= 5, "weekend", "working")

    return pd.DataFrame({
        "weekend_cnt": [tasks[tasks["status"] == "weekend"].shape[0]],
        "working_cnt": [tasks[tasks["status"] == "working"].shape[0]]
    })
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Classify tasks** | `np.where()` classification | **O(n)** |
| **Filter & count** | `.shape[0]` for each category | **O(n)** |
| **Overall Complexity** | **O(n)** ✅ Efficient |

## 📂 **Project Structure**  
```
tasks_weekend/
├── tasks_weekend.py  # Python solution
├── README.md         # Explanation & approach
```

✨ **Master weekday classification with this simple yet powerful solution!** 🚀