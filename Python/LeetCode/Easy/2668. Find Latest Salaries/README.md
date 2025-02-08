# 💼 **LeetCode 2668: Find Latest Salaries**  

## 📌 **Overview**  
This project solves **LeetCode Problem 2668: Find Latest Salaries**,  
where we **determine the most recent salary for each employee, assuming salaries increase yearly**.  

### **Problem Statement**  
You are given a **Salary Table** that contains **employee salary records over multiple years**.  
Each row **may contain outdated salary information**, and the **latest salary is always the highest salary recorded**.  

**Your task** is to find the **most recent salary for each employee** and return the data sorted by `emp_id`.  

## 🎯 **Example Walkthrough**  
### **Example Input**  
#### **Salary Table**
| emp_id | firstname | lastname | salary  | department_id |
|--------|----------|----------|---------|--------------|
| 1      | Todd     | Wilson   | 110000  | D105         |
| 1      | Todd     | Wilson   | 116119  | D105         |
| 2      | Justin   | Simon    | 130000  | D105         |
| 2      | Justin   | Simon    | 110985  | D105         |
| 3      | Kelly    | Rosario  | 46800   | D102         |
| 3      | Kelly    | Rosario  | 47000   | D102         |
| 4      | Patricia | Powell   | 16285   | D102         |
| 5      | Sherry   | Golden   | 44101   | D102         |
| 6      | Natasha  | Swanson  | 79928   | D104         |
| 6      | Natasha  | Swanson  | 90000   | D105         |

### **Step-by-Step Breakdown**  
1️⃣ **Identify the latest salary for each employee**  
   - **Employee 1**: **116119** (latest) ✅  
   - **Employee 2**: **130000** (latest) ✅  
   - **Employee 3**: **47000** (latest) ✅  
   - **Employee 4**: **16285** (latest) ✅  
   - **Employee 5**: **44101** (latest) ✅  
   - **Employee 6**: **90000** (latest) ✅  

2️⃣ **Return the latest salary per `emp_id`**  
   - Remove older salary records.  

3️⃣ **Sort the result by `emp_id` in ascending order.**  

### **Expected Output**  
```python
Output:
| emp_id | firstname | lastname | salary  | department_id |
|--------|----------|----------|---------|--------------|
| 1      | Todd     | Wilson   | 116119  | D105         |
| 2      | Justin   | Simon    | 130000  | D105         |
| 3      | Kelly    | Rosario  | 47000   | D102         |
| 4      | Patricia | Powell   | 16285   | D102         |
| 5      | Sherry   | Golden   | 44101   | D102         |
| 6      | Natasha  | Swanson  | 90000   | D105         |
```
🔥 **Now we have determined the most recent salaries for all employees!** 🚀  

## 📝 **Step-by-Step Approach**
### **1️⃣ Sort Salary Table by `emp_id` and `salary`**
```python
salary.sort_values(['emp_id', 'salary'])
```
- **Sorting ensures the latest salary is the last occurrence for each `emp_id`.**

### **2️⃣ Remove Older Salary Records**
```python
.drop_duplicates('emp_id', keep='last')
```
- **Keeps only the last occurrence per `emp_id`, which is the latest salary.**

### **3️⃣ Return the Processed DataFrame**
```python
return salary
```
- **Ensures a properly formatted result sorted by `emp_id`.**

## 💡 **Implementation**
```python
import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the latest salary record for each employee.

    Since salaries increase each year, the latest salary is the highest salary for each employee.
    The result is ordered by 'emp_id' in ascending order.

    :param salary: DataFrame containing employee salary records.
    :return: DataFrame with latest salary records sorted by 'emp_id'.
    """

    return (
        salary.sort_values(['emp_id', 'salary'])  # Sort by emp_id (ascending) and salary (ascending)
        .drop_duplicates('emp_id', keep='last')   # Keep the last occurrence (latest salary)
    )
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Sorting & Dropping Duplicates (`O(n log n)`)** | **O(n log n)** ✅ | **O(1)** ✅ |

- **Sorting requires `O(n log n)` complexity.**  
- **Dropping duplicates runs in `O(n)`.**  
- **Overall, the method is efficient and well-suited for large datasets.**  

---

## 🏗 **Project Structure**
```
2668. Find Latest Salaries/
├── find_latest_salaries.py  # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Optimise salary data with this efficient approach!** 🚀  
