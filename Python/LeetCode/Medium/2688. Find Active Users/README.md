# 🛒 **LeetCode 2688: Find Active Users**  

## 📌 **Problem Overview**  
Given a table of user purchases, identify **active users**. A user is considered **active** if they make a second purchase **within 7 days** of any previous purchase.

### **Table Schema**  
- **Users Table**
  - `user_id` (**int**) → The ID of the user.
  - `item` (**varchar**) → The purchased item.
  - `created_at` (**datetime**) → The date of purchase.
  - `amount` (**int**) → The purchase amount.

### **Example**
#### **Input**  
```
Users Table
+---------+--------------------+------------+--------+
| user_id | item               | created_at | amount |
+---------+--------------------+------------+--------+
|    5    | Smart Crock Pot    | 2021-09-18 | 698882 |
|    6    | Smart Lock         | 2021-09-10 |  11487 |
|    6    | Smart Thermostat   | 2021-09-14 |  11467 |
|    4    | Smart Cat Feeder   | 2021-09-02 | 693745 |
|    4    | Smart Bed          | 2021-09-13 | 170249 |
+---------+--------------------+------------+--------+
```

#### **Output**  
```
+---------+
| user_id |
+---------+
|    6    |
+---------+
```

✅ **Explanation:**  
- **User 5** has only one purchase → ❌ Not active.  
- **User 6** made purchases on **Sep 10 and Sep 14** (within 4 days) → ✅ Active.  
- **User 4** made purchases on **Sep 2 and Sep 13** (11 days apart) → ❌ Not active.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Sort, Compute Differences, and Filter**
1. **Sort** the transactions by `user_id` and `created_at` to process purchases in order.
2. **Compute the difference** in days between each user's consecutive purchases.
3. **Filter users** where the difference is **≤ 7 days**.
4. **Remove duplicates**, keeping only unique `user_id`s.

## 📝 **Implementation**  

```python
# find_active_users.py

import pandas as pd

def find_active_users(users: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active users who made a second purchase within 7 days of any of their previous purchases.

    Args:
        users (pd.DataFrame): Contains transaction data with columns:
            - "user_id" (int): The ID of the user.
            - "item" (str): The purchased item.
            - "created_at" (datetime): The date of purchase.
            - "amount" (int): The purchase amount.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The list of active users who made a second purchase
              within 7 days of any other purchase.
    """
    return (
        users
        # Sort by user_id and created_at to ensure chronological order
        .sort_values(by=["user_id", "created_at"], ascending=[True, True])
        # Calculate the difference in days between consecutive purchases for each user
        .assign(date_diff=lambda x: x.groupby("user_id")["created_at"].diff().dt.days)
        # Filter users who made a purchase within 7 days of their previous transaction
        .query("date_diff <= 7")
        # Remove duplicate user_id entries
        .drop_duplicates(subset="user_id")
        # Keep only the user_id column
        [["user_id"]]
    )

```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Sorting by `user_id`, `created_at`    | **O(N log N)** |
| Computing date differences            | **O(N)** |
| Filtering & dropping duplicates       | **O(N)** |
| **Overall Complexity**                 | **O(N log N)** ✅ |

> **N = number of transactions in the dataset**  

## 📂 **Project Structure**  

```
2688. Find Active Users/
├── find_active_users.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Sorting ensures correct chronological order** before computing date differences.  
✔ **Using `diff()` allows efficient time gap calculations** for each user.  
✔ **Querying users with `date_diff ≤ 7` efficiently filters active users**.  

🚀 **Mastering time-based filtering is essential for real-world analytics!** 🔥