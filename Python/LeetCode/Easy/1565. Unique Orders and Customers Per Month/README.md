# 📊 **LeetCode 1565: Unique Orders and Customers Per Month**

## 📌 **Problem Overview**
You are given an `orders` table containing information about **orders placed by customers**, including the **order date, customer ID, and invoice amount**.  

The goal is to find:
1. The **number of unique orders** per month.
2. The **number of unique customers** with **invoices greater than $20** per month.

### **Expected Output**
- A table containing:
  - **month**: The **YYYY-MM** format of the `order_date`.
  - **order_count**: The number of **unique orders** per month.
  - **customer_count**: The number of **unique customers** per month **with invoices > $20**.
- The result should be sorted **in any order**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
#### **Orders Table**
| order_id | order_date | customer_id | invoice |
|----------|------------|------------|--------|
| 1        | 2020-09-15 | 1          | 30     |
| 2        | 2020-09-17 | 3          | 90     |
| 3        | 2020-10-06 | 1          | 20     |
| 4        | 2020-10-06 | 1          | 21     |
| 5        | 2020-11-20 | 2          | 10     |
| 6        | 2020-12-01 | 4          | 55     |
| 7        | 2020-12-03 | 4          | 77     |
| 8        | 2021-01-07 | 3          | 31     |
| 9        | 2021-01-15 | 2          | 20     |

#### **Output:**
| month   | order_count | customer_count |
|---------|------------|---------------|
| 2020-09 | 2          | 2             |
| 2020-10 | 1          | 1             |
| 2020-12 | 2          | 1             |
| 2021-01 | 1          | 1             |

#### **Explanation**
- **September 2020**: 2 unique orders, **2 customers** with invoices **> $20**.
- **October 2020**: 1 unique order (since one order had `invoice = 20`), **1 customer**.
- **November 2020**: **No entry** because both invoices **≤ $20**.
- **December 2020**: 2 unique orders, **1 customer**.
- **January 2021**: 1 unique order, **1 customer**.

## 🛠 **Approach**
1. **Filter the Data**  
   - Select only rows where `invoice > 20`, as we only care about customers whose invoices exceed $20.

2. **Extract the Month from `order_date`**  
   - Convert the `order_date` into a **"YYYY-MM"** formatted string.

3. **Group by Month**  
   - Count **unique orders** per month.
   - Count **unique customers** per month.

4. **Return the Result**  
   - The result should be sorted **in any order**.

## 🚀 **Python Solution**
```python
import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of unique orders and unique customers with invoice > $20 per month.

    Args:
        orders (pd.DataFrame): A DataFrame with columns ['order_id', 'order_date', 'customer_id', 'invoice'].

    Returns:
        pd.DataFrame: A DataFrame with columns ['month', 'order_count', 'customer_count'].
    """
    return (
        orders.loc[orders["invoice"] > 20]
        .assign(month=orders["order_date"].dt.strftime("%Y-%m"))
        .groupby("month", as_index=False)
        .agg(order_count=("order_id", "nunique"), customer_count=("customer_id", "nunique"))
    )
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter rows (`invoice > 20`) | `orders.loc[...]` | **O(N)** |
| Extract month from date | `.dt.strftime()` | **O(N)** |
| Group and aggregate | `.groupby().agg()` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 📁 **Project Structure**
```
unique_orders_and_customers/
├── unique_orders_and_customers.py   # Python solution
├── README.md                        # Documentation
```

## 🏆 **Why This Works**
✔ **Vectorised Pandas operations** for filtering, transforming, and aggregating efficiently.  
✔ **Uses `.nunique()`** to count distinct orders and customers per month.  
✔ **Handles missing months naturally**, as months without qualifying orders are excluded.

🚀 **With this solution, you can efficiently compute unique orders and customers per month!** 🎯