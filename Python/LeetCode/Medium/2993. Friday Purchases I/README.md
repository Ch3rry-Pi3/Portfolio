# 🛍 **LeetCode 2993: Friday Purchases I**  

## 📌 **Problem Overview**  
Given a table of purchases made in **November 2023**, we need to compute the **total spending by users on each Friday of the month**.  

### **Key Requirements:**  
- **Filter only purchases made on Fridays**.
- **Determine the week number in November** (Week 1-5).
- **Sum the total amount spent** on each Friday.
- **Sort results by `week_of_month` in ascending order**.
- **Only include weeks where at least one purchase was made on a Friday**.

## 🖼 **Example**  
### **Input: Purchases Table**
```
+---------+---------------+--------------+
| user_id | purchase_date | amount_spend |
+---------+---------------+--------------+
|    11   | 2023-11-07    |    1126      |
|    15   | 2023-11-30    |    7473      |
|     7   | 2023-11-24    |    926       |
|    12   | 2023-11-24    |    5117      |
|     1   | 2023-11-10    |    5241      |
|     3   | 2023-11-17    |    8266      |
|     4   | 2023-11-24    |   10000      |
+---------+---------------+--------------+
```

### **Output:**
```
+--------------+---------------+--------------+
| week_of_month | purchase_date | total_amount |
+--------------+---------------+--------------+
|      1       | 2023-11-10    |    5241      |
|      3       | 2023-11-17    |    8266      |
|      4       | 2023-11-24    |   21692      |
+--------------+---------------+--------------+
```

✅ **Explanation:**  
1. **User purchases on Fridays**:
   - **Nov 10** (Week 1) → Total = **5241**
   - **Nov 17** (Week 3) → Total = **8266**
   - **Nov 24** (Week 4) → Total = **926 + 5117 + 10000 = 21692**
   - **Nov 30** (Week 5) is a Thursday → **Not included**.
2. **Sorting by `week_of_month` (ascending order).**

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Filter, Aggregate, and Sort**
1. **Extract `weekday` and `week_of_month`**  
   - Use `.dt.day_name()` to get the weekday (e.g., `"Friday"`).  
   - Compute **week of the month** using:  
     ```python
     (purchase_date.dt.day - 1) // 7 + 1
     ```
2. **Filter only purchases made on Fridays**.
3. **Group by `week_of_month` and `purchase_date`**  
   - Sum the `amount_spend` for each Friday.  
4. **Sort results by `week_of_month` in ascending order**.

## 📝 **Implementation**  

```python
# friday_purchases.py

import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total spending by users on each Friday of every week in November 2023.

    Args:
        purchases (pd.DataFrame): Contains purchase data with columns:
            - "user_id" (int): The ID of the user making the purchase.
            - "purchase_date" (datetime): The date of the purchase.
            - "amount_spend" (int): The amount spent on the purchase.

    Returns:
        pd.DataFrame: A table containing:
            - "week_of_month" (int): The week number in November 2023 (1-5).
            - "purchase_date" (datetime): The specific Friday date.
            - "total_amount" (int): The total spending on that Friday.

        The result is sorted by "week_of_month" in ascending order and only includes
        weeks where at least one purchase was made on a Friday.
    """
    # Extract weekday name and determine week of the month
    purchases = purchases.assign(
        weekday_of_week=purchases["purchase_date"].dt.day_name(),
        week_of_month=(purchases["purchase_date"].dt.day - 1) // 7 + 1
    )

    # Filter purchases to include only Fridays
    purchases = purchases[purchases["weekday_of_week"] == "Friday"]

    # Aggregate total spending for each Friday
    purchases = (
        purchases.groupby(["week_of_month", "purchase_date"])["amount_spend"]
        .sum()
        .reset_index(name="total_amount")
    )

    # Sort results by week of the month
    return purchases.sort_values(by="week_of_month")
```

## ⏳ **Time Complexity Analysis**  

| Operation                                  | Complexity |
|--------------------------------------------|------------|
| Extracting weekday and week number         | **O(N)** |
| Filtering for Fridays                      | **O(N)** |
| Grouping and summing values                | **O(N)** |
| Sorting by `week_of_month`                 | **O(N log N)** |
| **Overall Complexity**                      | **O(N log N)** ✅ |

> **N = number of records in the dataset**  

## 📂 **Project Structure**  

```
2993. Friday Purchases I/
├── friday_purchases.py  # Python solution
├── README.md            # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `dt.day_name()` to filter Fridays efficiently.**  
✔ **Computes `week_of_month` dynamically using `(day - 1) // 7 + 1`.**  
✔ **Aggregates purchases by week and sorts results correctly.**  

🚀 **Mastering time-based aggregations is crucial for real-world analytics!** 🔥