# 📊 **LeetCode 1421: NPV Queries**  

## 📌 **Problem Overview**  
You are given two tables:  

1. **NPV Table (`npv`)**  
   - Contains information about the **Net Present Value (NPV)** of inventories for different years.
   - Each row consists of:
     - `id` (inventory ID)
     - `year` (year of the inventory)
     - `npv` (Net Present Value for that inventory and year)

2. **Queries Table (`queries`)**  
   - Contains a list of queries asking for the `npv` of a specific inventory (`id`) for a given `year`.

👉 **Goal:**  
For each query in the `queries` table, **find the corresponding `npv` from the `npv` table**.  
- If the `(id, year)` pair is **present**, return the corresponding `npv`.  
- If the `(id, year)` pair is **missing**, return `0`.  
- The result table can be returned in **any order**.  

## 🎯 **Example Walkthrough**  

### **Example 1**  

#### **Input:**  

##### **NPV Table**  
| id | year | npv  |
|----|------|------|
| 1  | 2018 | 100  |
| 7  | 2020 | 30   |
| 2  | 2009 | 40   |
| 1  | 2019 | 113  |
| 2  | 2008 | 121  |
| 3  | 2009 | 12   |
| 11 | 2020 | 99   |
| 7  | 2019 | 0    |

##### **Queries Table**  
| id | year |
|----|------|
| 1  | 2019 |
| 2  | 2008 |
| 2  | 2009 |
| 7  | 2018 |
| 7  | 2020 |
| 13 | 2019 |

#### **Output:**  
| id | year | npv  |
|----|------|------|
| 1  | 2019 | 113  |
| 2  | 2008 | 121  |
| 2  | 2009 | 12   |
| 7  | 2018 | 0    |
| 7  | 2020 | 30   |
| 13 | 2019 | 0    |

#### **Explanation:**  
- `(1, 2019)`, `(2, 2008)`, and `(2, 2009)` exist in the `npv` table, so their values are retrieved.  
- `(7, 2018)` and `(13, 2019)` **do not exist**, so they are assigned `0`.  
- `(7, 2020)` is present in `npv`, so it retains its value `30`.  

## 🛠 **Approach**  

### **1️⃣ Merge the Tables**  
- Perform a **left join** (`how="left"`) between `queries` and `npv` on `id` and `year`.  
- This ensures that all rows in `queries` remain in the result, with `npv` values added where available.  

### **2️⃣ Handle Missing Values**  
- If an `(id, year)` pair **does not exist** in `npv`, Pandas assigns `NaN`.  
- We replace these `NaN` values with `0` using `.fillna(value={"npv": 0})`.  

This approach ensures that **all queries are answered** and missing values are handled correctly.

## 🚀 **Python Solution**  

```python
import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the queries table with the npv table on 'id' and 'year'.
    If no matching npv value is found, it assigns a default value of 0.

    Args:
        npv (pd.DataFrame): The NPV table containing 'id', 'year', and 'npv'.
        queries (pd.DataFrame): The Queries table containing 'id' and 'year'.

    Returns:
        pd.DataFrame: A DataFrame containing 'id', 'year', and the corresponding 'npv'.
    """
    return pd.merge(left=queries, right=npv, on=["id", "year"], how="left").fillna(value={"npv": 0})
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge Tables | `pd.merge(queries, npv, on=["id", "year"], how="left")` | **O(N + M)** |
| Handle Missing Values | `.fillna(value={"npv": 0})` | **O(N)** |
| **Total Complexity** | **O(N + M) Time, O(N) Space** | ✅ Efficient |

Where:  
- `N` = number of rows in `queries`  
- `M` = number of rows in `npv`  

## 📁 **Project Structure**  

```
npv_queries/
├── npv_queries.py   # Python solution
├── README.md        # Documentation
```

## 🏆 **Why This Works**  

✔ **Uses Pandas' efficient `merge()` function** for fast lookup.  
✔ **Handles missing values elegantly** with `.fillna(0)`.  
✔ **Runs in O(N + M) time complexity**, making it **scalable for large datasets**.  

🚀 **Now you can efficiently retrieve NPVs for any given queries!** 🎯  
