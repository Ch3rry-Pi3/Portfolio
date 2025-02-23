# 🛍 **LeetCode 3118: Friday Purchase III**  

## 📌 **Problem Overview**  
We have two tables:  
- **Purchases**: Contains records of purchases made by users, including **purchase date** and **amount spent**.  
- **Users**: Contains user details, including their **membership type** (`Standard`, `Premium`, `VIP`).  

### **Task:**  
Calculate the **total spending** by **Premium** and **VIP** users on each **Friday of November 2023**.  
- If **no purchases** were made on a particular Friday by **Premium** or **VIP** members, the total spending should be **0**.  
- The result must be **ordered by the week of the month** and then by **membership type (ascending)**.  

## 🖼 **Example 1**  

### **Input: Purchases Table**
```
+---------+---------------+--------------+
| user_id | purchase_date | amount_spend |
+---------+---------------+--------------+
|   11    |  2023-11-03   |    1126      |
|   15    |  2023-11-10   |    7473      |
|   17    |  2023-11-17   |    2414      |
|   12    |  2023-11-17   |    9562      |
|    1    |  2023-11-24   |    5117      |
|   10    |  2023-11-24   |    5241      |
|   13    |  2023-11-21   |   12000      |
+---------+---------------+--------------+
```

### **Input: Users Table**
```
+---------+------------+
| user_id | membership |
+---------+------------+
|   11    |  Premium   |
|   15    |    VIP     |
|   17    |  Standard  |
|   12    |    VIP     |
|    1    |  Premium   |
|   10    |    VIP     |
|   13    |  Premium   |
+---------+------------+
```

### **Output:**
```
+--------------+------------+--------------+
| week_of_month | membership | total_amount |
+--------------+------------+--------------+
|       1      |  Premium   |    1126      |
|       1      |    VIP     |      0       |
|       2      |  Premium   |      0       |
|       2      |    VIP     |    7473      |
|       3      |  Premium   |      0       |
|       3      |    VIP     |   12000      |
|       4      |  Premium   |    5117      |
|       4      |    VIP     |    5241      |
+--------------+------------+--------------+
```

✅ **Explanation:**  
- **Week 1 (Nov 3)**:
  - `Premium`: **1126** (user `11`).
  - `VIP`: **0** (no VIP purchases).  
- **Week 2 (Nov 10)**:
  - `Premium`: **0** (no Premium purchases).  
  - `VIP`: **7473** (user `15`).  
- **Week 3 (Nov 17)**:
  - `Premium`: **0** (no Premium purchases).  
  - `VIP`: **12000** (`2414 + 9562` from user `17` & `12`).  
- **Week 4 (Nov 24)**:
  - `Premium`: **5117** (user `1`).  
  - `VIP`: **5241** (user `10`).  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Aggregate Premium & VIP Purchases by Friday**
1. **Find all Fridays in November 2023**.
2. **Create a mapping** of each **Friday to its corresponding week number**.
3. **Filter purchases** to include only those made **on a Friday**.
4. **Merge with the users table** to keep only **Premium and VIP** users.
5. **Group by week_of_month and membership**, summing the total amount spent.
6. **Ensure missing combinations are filled with 0**.
7. **Sort by week_of_month and membership type**.

## 📝 **Implementation**  

```python
import pandas as pd

def friday_purchases(purchases: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total spending by Premium and VIP users on each Friday of November 2023.

    If there are no purchases on a given Friday by Premium or VIP members, 
    the spending for that date should be recorded as 0.

    Args:
        purchases (pd.DataFrame): Contains purchase data with columns:
            - "user_id" (int): The ID of the user making the purchase.
            - "purchase_date" (date): The date of purchase.
            - "amount_spend" (int): The total amount spent.
        users (pd.DataFrame): Contains user data with columns:
            - "user_id" (int): The ID of the user.
            - "membership" (enum): Membership type ('Standard', 'Premium', 'VIP').

    Returns:
        pd.DataFrame: A table containing:
            - "week_of_month" (int): The week number in November.
            - "membership" (str): The membership type.
            - "total_amount" (int): Total spending by the membership type.
        
        The result is sorted by "week_of_month" in ascending order, 
        and then by "membership" in ascending order.
    """

    # Define all Fridays in November 2023
    fridays = pd.date_range(start="2023-11-01", end="2023-11-30", freq="W-FRI")

    # Create a mapping from each Friday date to its corresponding week number
    week_map = {date: i + 1 for i, date in enumerate(fridays)}

    # Map each purchase to the corresponding week of the month
    purchases["week_of_month"] = purchases["purchase_date"].map(week_map)

    # Filter purchases to only include those made on a Friday
    purchases = purchases[purchases["purchase_date"].isin(fridays)]

    # Merge with users table to get membership type
    merged = purchases.merge(users, on="user_id")

    # Keep only purchases made by Premium and VIP members
    merged = merged[merged["membership"].isin(["Premium", "VIP"])]

    # Group by week_of_month and membership, summing the amount spent
    agg = (
        merged.groupby(["week_of_month", "membership"])["amount_spend"]
        .sum()
        .reset_index(name="total_amount")
    )

    # Create a full grid of weeks and membership types to ensure missing values are filled with 0
    weeks = list(week_map.values())
    memberships = ["Premium", "VIP"]
    full_grid = pd.MultiIndex.from_product([weeks, memberships], names=["week_of_month", "membership"])

    # Ensure all week-membership combinations are represented, filling missing values with 0
    result = agg.set_index(["week_of_month", "membership"]).reindex(full_grid, fill_value=0).reset_index()

    # Sort by week_of_month and membership type
    return result.sort_values(by=["week_of_month", "membership"])

```

## 📂 **Project Structure**  

```
3118. Friday Purchase III/
├── friday_purchases.py  # Python solution
├── README.md            # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Combines multiple tables using Pandas merge operations**.  
✔ **Efficiently filters and groups data to compute spending per membership type**.  
✔ **Ensures missing values are properly handled** with **MultiIndex reindexing**.  

🚀 **A great problem for mastering data aggregation with Pandas!** 🔥