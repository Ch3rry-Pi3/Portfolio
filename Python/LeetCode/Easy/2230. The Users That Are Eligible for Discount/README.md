# 🎯 **LeetCode 2230: The Users That Are Eligible for Discount**

## 📌 **Problem Overview**
We need to find users who qualify for a **discount** based on their purchase history.

A user is **eligible** if they made at least **one purchase** that meets the following conditions:
1. The purchase happened **within a given date range** `[startDate, endDate]` (inclusive).
2. The purchase amount was **at least** `minAmount`.

📢 The result should return a list of **unique user IDs** in **ascending order**.

## 🛠 **Approach**
We can solve this problem efficiently using **Pandas filtering** and **sorting** operations.

### 🔹 **Steps to Solve**
1. **Filter purchases within the date range**:  
   - Only consider transactions where the `time_stamp` falls between `startDate` and `endDate`.
2. **Apply the minimum amount condition**:  
   - Keep only purchases where `amount >= minAmount`.
3. **Extract unique user IDs**:  
   - Use `.drop_duplicates()` to ensure each user appears only once.
4. **Sort the result by `user_id`**.

✅ **Time Complexity**: **O(N)** (Single pass filtering & sorting)  
✅ **Space Complexity**: **O(1)** (Only storing necessary results)

## 🚀 **Python Solution**
```python
import pandas as pd
from datetime import datetime


def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    """
    Finds users eligible for a discount based on purchase conditions.

    Args:
        purchases (pd.DataFrame): DataFrame containing purchase data with columns ['user_id', 'time_stamp', 'amount'].
        start_date (datetime): The start date of the eligibility window.
        end_date (datetime): The end date of the eligibility window.
        min_amount (int): Minimum purchase amount required for discount eligibility.

    Returns:
        pd.DataFrame: A DataFrame containing unique user IDs of eligible users, sorted in ascending order.
    """

    # Filter purchases within the specified date range and minimum amount condition
    eligible_users = purchases.loc[
        (start_date <= purchases["time_stamp"]) & (purchases["time_stamp"] <= end_date) &
        (purchases["amount"] >= min_amount), 
        ["user_id"]
    ].drop_duplicates()

    # Return the sorted result by user_id
    return eligible_users.sort_values(by="user_id").reset_index(drop=True)
```

## 📌 **Example Walkthrough**
### **Example 1**
#### **Input:**
```python
purchases = [
    [1, "2022-04-20 09:03:00", 4416],
    [1, "2022-03-19 19:24:02", 678],
    [2, "2022-03-18 12:03:09", 4523],
    [3, "2022-03-30 09:43:42", 626],
    [3, "2022-03-10 08:30:00", 1500]
]
start_date = "2022-03-08"
end_date = "2022-03-20"
min_amount = 1000
```
#### **Output:**
```python
   user_id
0       2
3       3
```
#### **Explanation:**
- User **2** made a purchase of **4523** on **March 18**, which qualifies.
- User **3** made a purchase of **1500** on **March 10**, which qualifies.
- User **1** does not qualify because their purchase was **below 1000**.

## 📊 **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Date filtering | `purchases["time_stamp"] >= start_date` | **O(N)** |
| Amount filtering | `purchases["amount"] >= min_amount` | **O(N)** |
| Drop duplicates | `.drop_duplicates()` | **O(N)** |
| Sorting | `.sort_values(by="user_id")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** (due to sorting) | ✅ Efficient |

## 🎯 **Key Takeaways**
✔ **Optimised Pandas filtering** ensures efficiency.  
✔ **Single-pass filtering** makes it **O(N)** before sorting.  
✔ **Elegant & Pythonic** implementation with `.loc[]` and `.drop_duplicates()`.  
✔ **Scalable** for large datasets.

🚀 **With this approach, you can efficiently filter eligible users for discounts!** 🎯