# 🏢 **LeetCode 1875: Group Employees of the Same Salary**  

## 📌 **Problem Overview**  

A company wants to divide employees into **teams** where:  
- Each team consists of **at least two employees**.  
- All employees in a team have the **same salary**.  
- Employees with unique salaries **are not assigned to any team**.  
- **Team IDs** are assigned based on the **rank of the salary**, where the lowest salary has `team_id = 1`.  
- If two teams have the same salary, they belong to the same team ID.  
- The result must be **sorted** by `team_id` (ascending). If there is a tie, sort by `employee_id`.  

## 📊 **Database Schema**  

### **Employees Table**  
| Column Name  | Type   | Description |
|-------------|--------|-------------|
| `employee_id` | int  | Unique ID for each employee |
| `name`       | varchar | Employee's name |
| `salary`     | int    | Employee's salary |

## 🎯 **Example Walkthrough**  

### **Example 1**  

#### **Input: Employees Table**  
| employee_id | name    | salary |
|------------|--------|--------|
| 1          | Alice  | 5000   |
| 2          | Bob    | 6000   |
| 3          | Charlie | 5000  |
| 4          | David  | 7000   |
| 5          | Eve    | 6000   |
| 6          | Frank  | 8000   |
| 7          | Grace  | 5000   |

#### **Output: Employees with Assigned Teams**  
| employee_id | name    | salary | team_id |
|------------|--------|--------|---------|
| 1          | Alice  | 5000   | 1       |
| 3          | Charlie | 5000  | 1       |
| 7          | Grace  | 5000   | 1       |
| 2          | Bob    | 6000   | 2       |
| 5          | Eve    | 6000   | 2       |

#### **Explanation:**  
- Employees **Alice, Charlie, and Grace** share a salary of **5000**, so they form `team_id = 1`.  
- Employees **Bob and Eve** share a salary of **6000**, so they form `team_id = 2`.  
- **David (7000) and Frank (8000) are not included** because their salaries are unique.  
- Team IDs are assigned based on the **ranking of salaries** (`5000 → 1`, `6000 → 2`).  

## 🛠 **Approach**  

1️⃣ **Sort Employees by Salary**  
- Order employees by `salary` (ascending).  

2️⃣ **Rank Salary Groups**  
- Assign **dense ranking** to each unique salary (`rank(method="dense")`).  

3️⃣ **Filter Out Unique Salaries**  
- Employees with **unique salaries** are **excluded** from teams.  

4️⃣ **Assign Team IDs**  
- Assign a **team ID** based on the **salary rank**.  

5️⃣ **Sort the Output**  
- Order by **`team_id`**, then by **`employee_id`**.  

## 🚀 **Python Solution**  

```python
import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Groups employees into teams based on their salaries.

    Employees with the same salary are assigned to the same team, provided there are at least 
    two employees with that salary. Each team's ID is assigned based on the ranking of its salary.

    Args:
        employees (pd.DataFrame): A DataFrame containing:
            - "employee_id" (int): Unique ID for each employee.
            - "name" (str): Employee's name.
            - "salary" (int): Employee's salary.

    Returns:
        pd.DataFrame: A DataFrame with employees assigned to teams, sorted by "team_id" and "employee_id".
                      Columns:
                      - "employee_id" (int): Employee's ID.
                      - "name" (str): Employee's name.
                      - "salary" (int): Employee's salary.
                      - "team_id" (int): The assigned team ID.
    """

    return (
        employees
        .sort_values(by="salary", ascending=True)
        .assign(rnk=lambda x: x["salary"].rank(method="dense"))                         # Assign rank based on salary
        .assign(team_count=lambda x: x.groupby("rnk")["rnk"].transform("count"))        # Count occurrences
        .query("team_count > 1")                                                        # Keep only salaries with multiple employees
        .assign(team_id=lambda x: x["salary"].rank(method="dense"))                     # Assign team IDs based on ranking
        .drop(columns=["rnk", "team_count"])                                            # Drop intermediate columns
        .sort_values(by=["team_id", "employee_id"])                                     # Sort by team_id and employee_id
    )
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values(by="salary")` | **O(N log N)** |
| Grouping | `groupby("rnk")` | **O(N)** |
| Ranking | `rank(method="dense")` | **O(N)** |
| Filtering | `query("team_count > 1")` | **O(N)** |
| Sorting Output | `sort_values(by=["team_id", "employee_id"])` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses Pandas vectorised operations** (`rank()`, `groupby()`, `query()`) for efficiency.  
✔ **Filters out unique salaries dynamically** before assigning teams.  
✔ **Sorts the result in the required order** (`team_id`, then `employee_id`).  
✔ **Handles large datasets efficiently** with `O(N log N)` complexity.  

🚀 **This solution ensures efficient employee grouping with proper team ID assignment!** 🎯