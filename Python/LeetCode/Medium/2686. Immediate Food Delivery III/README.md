# 🍽️ **LeetCode 2686: Immediate Food Delivery III**

## 📌 **Problem Overview**  
Given a **food delivery system**, each row in the `Delivery` table represents a **customer order**, specifying:  
- `order_date`: The date the order was placed.  
- `customer_pref_delivery_date`: The date the customer prefers to receive their order.  

An **"immediate"** order is one where the **order date matches the preferred delivery date**.  
The task is to **calculate the percentage** of immediate orders for each `order_date`, rounded to **two decimal places**.  

The output must be **sorted in ascending order** by `order_date`.

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input:**  
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|------------|------------|------------|-----------------------------|
| 1          | 1          | 2019-08-01 | 2019-08-01                  |
| 2          | 1          | 2019-08-01 | 2019-08-01                  |
| 3          | 2          | 2019-08-01 | 2019-08-02                  |
| 4          | 3          | 2019-08-02 | 2019-08-01                  |
| 5          | 3          | 2019-08-02 | 2019-08-02                  |
| 6          | 4          | 2019-08-02 | 2019-08-02                  |
| 7          | 4          | 2019-08-03 | 2019-08-03                  |
| 8          | 5          | 2019-08-03 | 2019-08-03                  |
| 9          | 5          | 2019-08-04 | 2019-08-05                  |
| 10         | 5          | 2019-08-04 | 2019-08-06                  |

#### **Output:**  
| order_date  | immediate_percentage |
|------------|---------------------|
| 2019-08-01 | 66.67               |
| 2019-08-02 | 66.67               |
| 2019-08-03 | 100.00              |
| 2019-08-04 | 0.00                |

#### **Explanation:**  
- **2019-08-01:** 3 orders, **2 were immediate** → **66.67%**  
- **2019-08-02:** 3 orders, **2 were immediate** → **66.67%**  
- **2019-08-03:** 2 orders, **both were immediate** → **100.00%**  
- **2019-08-04:** 2 orders, **none were immediate** → **0.00%**  

## 🚀 **Approach Explanation**  

### **1️⃣ Identify Immediate Orders**  
- If `order_date == customer_pref_delivery_date`, mark it as an **immediate order** (`1`), otherwise (`0`).  

### **2️⃣ Compute Immediate Percentage per `order_date`**  
- Group by `order_date`, calculate the **mean** of immediate orders, and multiply by `100`.  
- Round results to **two decimal places** for accuracy.  

### **3️⃣ Sort Results**  
- Ensure the output is **sorted by `order_date` in ascending order**.

## 📝 **Python Solution**  
```python
import pandas as pd
import numpy as np

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the percentage of immediate orders for each unique order_date.

    An order is considered "immediate" if the order_date matches the 
    customer_pref_delivery_date. The percentage of immediate orders per 
    order_date is rounded to two decimal places.

    Args:
        delivery (pd.DataFrame): DataFrame containing delivery orders with columns:
            - delivery_id (int): Unique delivery ID.
            - customer_id (int): Customer ID.
            - order_date (datetime): Date when the order was placed.
            - customer_pref_delivery_date (datetime): Preferred delivery date.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - order_date (datetime): The unique order date.
            - immediate_percentage (float): The percentage of immediate orders, rounded to 2 decimal places.
    """
    
    return (
        delivery
        .assign(immediate=lambda x: np.where(x["order_date"] == x["customer_pref_delivery_date"], 1, 0))
        .groupby("order_date", as_index=False)
        .agg(immediate_percentage=("immediate", "mean"))
        .assign(immediate_percentage=lambda x: round(x["immediate_percentage"] * 100, 2))
        .sort_values(by="order_date", ascending=True)
    )

if __name__ == "__main__":
    # Example data
    data = {
        "delivery_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "customer_id": [1, 1, 2, 3, 3, 4, 4, 5, 5, 5],
        "order_date": pd.to_datetime([
            "2019-08-01", "2019-08-01", "2019-08-01", "2019-08-02", "2019-08-02",
            "2019-08-02", "2019-08-03", "2019-08-03", "2019-08-04", "2019-08-04"
        ]),
        "customer_pref_delivery_date": pd.to_datetime([
            "2019-08-01", "2019-08-01", "2019-08-02", "2019-08-01", "2019-08-02",
            "2019-08-02", "2019-08-03", "2019-08-03", "2019-08-05", "2019-08-06"
        ])
    }

    delivery_df = pd.DataFrame(data)
    
    # Compute and display results
    result_df = immediate_delivery(delivery_df)
    print(result_df)
```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Mark Immediate Orders** | `np.where()` operation | **O(n)** |
| **Group and Aggregate** | `groupby` and `mean()` | **O(n)** |
| **Sorting** | `sort_values()` | **O(n log n)** |
| **Overall Complexity** | **O(n log n)** ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Efficient grouping & aggregation** using Pandas.  
✔ **Avoids loops**, relying on vectorised operations.  
✔ **Sorting ensures correct output order.**  

## 📂 **Project Structure**  
```
food_delivery/
├── food_delivery.py  # Python solution
├── README.md         # Explanation & approach
```

🚀 **Optimise food delivery tracking with this efficient data-processing solution!** 🍽️🔥