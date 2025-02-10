# 🛒 **LeetCode 2205: The Number of Users That Are Eligible for Discount**

## 📌 **Problem Overview**
A business offers discounts to users who have made **at least one purchase** within a **specified time range** and with a **minimum amount spent**.

Given a dataset of purchases, determine how many unique users meet both of the following conditions:
- The purchase was made **within the inclusive time range** `[start_date, end_date]`.
- The purchase amount is **greater than or equal** to `min_amount`.

Return the total count of **eligible users** in the form of a **single-column DataFrame**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
purchases = pd.DataFrame({
    "user_id": [1, 2, 3, 3],
    "time_stamp": [
        "2022-03-08 09:03:00", "2022-03-19 12:39:00",
        "2022-03-18 12:03:09", "2022-03-30 09:43:42"
    ],
    "amount": [4416, 678, 4523, 626]
})
start_date = "2022-03-08"
end_date = "2022-03-20"
min_amount = 1000
```
#### **Output:**
```python
   user_cnt
0        1
```
#### **Explanation:**
- User **1** had a valid purchase **but outside the time range** ❌.
- User **2** had a purchase **within the time range but below the minimum amount** ❌.
- User **3** had a purchase **within the time range and meeting the minimum amount** ✅.

Thus, **only one user is eligible for a discount**.

## 🛠 **Approach**
The problem can be efficiently solved using **Pandas filtering** and **grouping**:

1. **Filter Purchases:**  
   - Keep only rows where `time_stamp` falls within `[start_date, end_date]`.
   - Ensure `amount` is at least `min_amount`.

2. **Count Unique Users:**  
   - Extract the number of distinct `user_id` values that meet the conditions.

3. **Return Result:**  
   - Wrap the count in a **single-column DataFrame** named `"user_cnt"`.

This approach runs in **O(N) time complexity**, where **N** is the number of purchases.

## 🚀 **Python Solution**
```python
import pandas as pd
from datetime import datetime

def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    """
    Counts the number of unique users eligible for a discount.

    A user is eligible if they made at least one purchase within the given date range
    and the purchase amount meets or exceeds the minimum required amount.

    Args:
        purchases (pd.DataFrame): DataFrame containing purchase records.
        start_date (datetime): The start of the eligible period.
        end_date (datetime): The end of the eligible period.
        min_amount (int): The minimum amount required for a purchase to be eligible.

    Returns:
        pd.DataFrame: A DataFrame with a single column "user_cnt" representing
        the number of users who meet the criteria.
    """
    eligible_users = purchases.loc[
        (purchases["time_stamp"] >= start_date) &
        (purchases["time_stamp"] <= end_date) &
        (purchases["amount"] >= min_amount),
        "user_id"
    ].nunique()

    return pd.DataFrame({"user_cnt": [eligible_users]})
```

## 📊 **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter purchases | `purchases.loc[...]` | **O(N)** |
| Count unique users | `.nunique()` | **O(N)** |
| Wrap in DataFrame | `pd.DataFrame({...})` | **O(1)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
eligible_for_discount/
├── eligible_for_discount.py   # Python solution
├── README.md                  # Documentation
```

## 🏆 **Why This Works**
✔ **Pandas filtering makes this a simple and efficient approach**.  
✔ **O(N) time complexity ensures scalability for large datasets**.  
✔ **Handles edge cases like no purchases or all ineligible users**.

🚀 **With this solution, you can efficiently determine the number of users eligible for a discount!** 🎯