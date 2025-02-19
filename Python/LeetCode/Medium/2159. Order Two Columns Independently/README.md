# 📌 LeetCode 2159: Order Two Columns Independently

## 📝 Problem Statement

Given a table **`Data`**, write a solution to **independently** order two columns:

- **`first_col`** in **ascending order**.
- **`second_col`** in **descending order**.

Each column should be sorted **independently**, meaning their values should be rearranged without maintaining any row relationships.

📌 **The result table must be returned in the following format.**

## 📊 Example Walkthrough

### **Example 1**
#### **Input:**
| first_col | second_col |
|-----------|-----------|
| 4         | 2         |
| 2         | 1         |
| 3         | 4         |
| 1         | 1         |

#### **Output:**
| first_col | second_col |
|-----------|-----------|
| 1         | 4         |
| 2         | 3         |
| 3         | 2         |
| 4         | 1         |

### **Explanation:**
- **`first_col`** values `[4, 2, 3, 1]` are **sorted in ascending order** → `[1, 2, 3, 4]`
- **`second_col`** values `[2, 1, 4, 1]` are **sorted in descending order** → `[4, 3, 2, 1]`
- The result is formed by combining these sorted lists **independently**.

## 🔎 Approach & Solution

1. **Sort `first_col`** in **ascending order**.
2. **Sort `second_col`** in **descending order**.
3. **Combine** the independently sorted columns into a new DataFrame.

This ensures that both columns are **reordered independently** of each other.

## 🚀 Implementation

```python
import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Independently orders two columns in a DataFrame:
    
    - 'first_col' is sorted in ascending order.
    - 'second_col' is sorted in descending order.

    Args:
        data (pd.DataFrame): A DataFrame containing:
            - "first_col" (int): Column to be sorted in ascending order.
            - "second_col" (int): Column to be sorted in descending order.

    Returns:
        pd.DataFrame: A DataFrame with "first_col" sorted in ascending order
                      and "second_col" sorted in descending order.
    """

    # Sort "first_col" in ascending order and reset index
    first_col_sorted = data[["first_col"]].sort_values(by="first_col", ascending=True)["first_col"].reset_index(drop=True)

    # Sort "second_col" in descending order and reset index
    second_col_sorted = data[["second_col"]].sort_values(by="second_col", ascending=False)["second_col"].reset_index(drop=True)

    # Combine the independently sorted columns into a new DataFrame
    return pd.DataFrame({"first_col": first_col_sorted, "second_col": second_col_sorted})
```

## ⏳ **Complexity Analysis**

| Operation | Time Complexity |
|-----------|----------------|
| Sorting `first_col` | **O(N log N)** |
| Sorting `second_col` | **O(N log N)** |
| Constructing DataFrame | **O(N)** |
| **Total Complexity** | **O(N log N)** |

Since sorting takes **O(N log N)** time, the overall complexity is **O(N log N)**.

## 🏗 **Project Structure**

```
order_columns_project/
├── order_independently.py   # Python solution
├── README.md                # Explanation & walkthrough
```

## 🎯 **Key Takeaways**
✔ **Each column is sorted independently** without maintaining row relationships.  
✔ **Sorting is done efficiently using built-in Pandas functions**.  
✔ **Time complexity is O(N log N) due to sorting operations**.  

🚀 **With this approach, you can efficiently sort any two columns independently in a DataFrame!** 🎯
