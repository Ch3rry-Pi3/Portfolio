# 🏢 **LeetCode 1075: Project Employees II**  

## 📌 **Overview**  
This project solves **LeetCode Problem 1075: Project Employees II**,  
where we determine **which project(s) have the most employees assigned**.  

### **Problem Statement**  
You are given a table with **employee-project assignments**.  
Each row contains a `project_id` and `employee_id`, meaning an employee is assigned to that project.  

**Your task** is to return the `project_id(s)` with the highest number of employees.  

## 🎯 **Example Walkthrough**  
### **Example Input**  
#### **Project Table**
| project_id | employee_id |
|------------|------------|
| 1          | 101        |
| 1          | 102        |
| 1          | 103        |
| 2          | 201        |
| 2          | 202        |
| 3          | 301        |
| 3          | 302        |
| 3          | 303        |
| 3          | 304        |

### **Step-by-Step Breakdown**  
1️⃣ **Count how many employees are assigned to each project**  
   - **Project 1** → **3 employees** ✅  
   - **Project 2** → **2 employees** ✅  
   - **Project 3** → **4 employees** ✅  

2️⃣ **Find the project(s) with the highest count**  
   - **Maximum employee count** = **4**  
   - **Only Project 3 has 4 employees**  

3️⃣ **Return the project(s) with the maximum count**  

### **Expected Output**  
```python
Output:
| project_id |
|------------|
| 3          |
```
🔥 **Only Project 3 has the highest number of employees (4), so it is returned.** 🚀  

## 📝 **Step-by-Step Approach**
### **1️⃣ Group by `project_id` and Count Employees**
```python
df = project.groupby("project_id", as_index=False)["employee_id"].count()
```
- **Groups by `project_id` and counts employees for each project**  
- **Creates a DataFrame with two columns: `project_id` and `employee_count`**

### **2️⃣ Find the Maximum Employee Count**
```python
max_count = df["employee_id"].max()
```
- **Finds the highest number of employees assigned to any project**  

### **3️⃣ Filter Only Projects with the Maximum Employee Count**
```python
df.loc[df["employee_id"] == max_count, ["project_id"]]
```
- **Filters only the projects that have the maximum number of employees**

## 💡 **Implementation**
```python
import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the project(s) with the most employees assigned.

    :param project: DataFrame containing 'project_id' and 'employee_id' pairs.
    :param employee: DataFrame (not used, but included for completeness).
    :return: DataFrame containing only the project_id(s) with the highest employee count.
    """

    # Count employees per project
    df = project.groupby("project_id", as_index=False)["employee_id"].count()
    max_count = df["employee_id"].max()  # Get the highest employee count

    # Return only the project(s) with the maximum count
    return df.loc[df["employee_id"] == max_count, ["project_id"]]
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Grouping + Filtering (`O(n)`)** | **O(n)** ✅ | **O(1)** ✅ |

- **Grouping by `project_id` takes `O(n)`.**  
- **Finding the max and filtering is `O(n)`.**  
- **No extra space is used (`O(1)`).**  

## 🏗 **Project Structure**
```
1075. Project Employees II/
├── project_employees.py   # Python implementation of the solution
├── README.md              # Detailed explanation & walkthrough
```

🚀 **Efficiently find the most employee-heavy projects with this solution!** 🔥  
