# 🏢 **LeetCode 2988: Manager of the Largest Department**  

## 📌 **Problem Overview**  
Given a table of employees and their **departments**, we need to **identify the manager** of the **largest department(s)** (i.e., the department(s) with the most employees).  

### **Key Requirements:**  
- Determine **the department(s) with the highest employee count**.  
- Select only **employees with the title "Manager"** from those departments.  
- If multiple departments have the **same maximum size**, return all of them.  
- Sort results by **`dep_id` in ascending order**.

## 🖼 **Example**  
### **Input: Employees Table**
```
+--------+-----------+--------+-------------+
| emp_id | emp_name  | dep_id |  position   |
+--------+-----------+--------+-------------+
|  156   | Michael   |  107   |  Manager    |
|  112   | Lucas     |  107   |  Consultant |
|    8   | Isabella  |  101   |  Manager    |
|   16   | Joseph    |  100   |  Manager    |
|   80   | Aiden     |  107   |  Engineer   |
|   67   | Skylar    |  101   |  Freelancer |
|  156   | Stella    |  101   |  Coordinator|
|   97   | Nathan    |  101   |  Supervisor |
|    3   | Ethan     |  107   |  Administrator |
|   13   | Audrey    |  101   |  Consultant |
+--------+-----------+--------+-------------+
```

### **Output:**
```
+--------------+--------+
| manager_name | dep_id |
+--------------+--------+
|   Joseph     |  100   |
|  Isabella    |  101   |
+--------------+--------+
```

✅ **Explanation:**  
1. **Count employees in each department**:  
   ```
   dep_id 100 → 1 employee  
   dep_id 101 → 5 employees  
   dep_id 107 → 4 employees  
   ```
   - The **largest department is `101` (5 employees)**.
   - The **next largest is `107` (4 employees)**.
2. **Filter managers in the largest department** (`101`):  
   - `Isabella` (Manager) in `101`.
3. **Since department `100` has only one employee (who is a manager), it's included**:  
   - `Joseph` (Manager) in `100`.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Count Employees Per Department, Find Managers in the Largest Department(s)**
1. **Calculate the number of employees in each department** using `.groupby("dep_id").count()`.  
2. **Find the maximum department size**.  
3. **Filter managers (`position == 'Manager'`) in those largest departments**.  
4. **Sort by `dep_id` in ascending order**.

## 📝 **Implementation**  

```python
# manager_largest_department.py

import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the manager of the largest department(s) based on employee count.

    Args:
        employees (pd.DataFrame): Contains employee data with columns:
            - "emp_id" (int): The ID of the employee.
            - "emp_name" (str): The name of the employee.
            - "dep_id" (int): The department ID.
            - "position" (str): The job title of the employee.

    Returns:
        pd.DataFrame: A table containing:
            - "manager_name" (str): The name of the manager of the largest department(s).
            - "dep_id" (int): The department ID of the largest department(s).
        
        The result is sorted by "dep_id" in ascending order.
    """
    return (
        employees
        # Compute department employee count and maximum employee count
        .assign(
            emp_count=lambda x: x.groupby("dep_id")["emp_id"].transform("count"),
            max_emp_count=lambda x: x["emp_count"].max()
        )
        # Filter for managers in the largest department(s)
        .query("emp_count == max_emp_count and position == 'Manager'")
        # Keep only required columns and sort by department ID
        [["emp_name", "dep_id"]]
        .sort_values(by="dep_id")
        # Rename columns to match expected output
        .rename(columns={"emp_name": "manager_name"})
    )
```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Counting employees per department     | **O(N)** |
| Finding the largest department(s)     | **O(N)** |
| Filtering for managers                | **O(N)** |
| Sorting the final result              | **O(N log N)** |
| **Overall Complexity**                 | **O(N log N)** ✅ |

> **N = number of employees in the dataset**  

## 📂 **Project Structure**  

```
2988. Manager of the Largest Department/
├── manager_largest_department.py  # Python solution
├── README.md                      # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses Pandas `.groupby()` and `.transform("count")`** for efficient employee count calculation.  
✔ **Filters only managers in the largest department(s).**  
✔ **Sorting ensures output is correctly formatted.**  
✔ **Scales well for large datasets with multiple departments.**  

🚀 **Mastering filtering and aggregation techniques is crucial for organisational analytics!** 🔥