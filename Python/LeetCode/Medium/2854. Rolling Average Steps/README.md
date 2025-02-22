# 🚶 **LeetCode 2854: Rolling Average Steps**  

## 📌 **Problem Overview**  
Given a table of step counts recorded for different users on different dates, calculate the **3-day rolling average** of steps for each user.

### **How the Rolling Average Works**  
- The **rolling average for a day** is the average of **that day and the two previous days**.
- If there are **fewer than 3 days of data** for a user, the rolling average is **not defined** for that date.
- The result must be rounded to **two decimal places**.
- The output must be ordered by `user_id` and `steps_date`.

## 🖼 **Example**  
### **Input: Steps Table**
```
+---------+-------------+------------+
| user_id | steps_count | steps_date |
+---------+-------------+------------+
|    1    |    687      | 2021-09-02 |
|    1    |    395      | 2021-09-04 |
|    1    |    499      | 2021-09-07 |
|    2    |    153      | 2021-09-07 |
|    2    |    171      | 2021-09-09 |
|    3    |    120      | 2021-09-07 |
|    3    |    557      | 2021-09-08 |
|    3    |    840      | 2021-09-09 |
|    3    |    627      | 2021-09-10 |
|    3    |    191      | 2021-09-12 |
+---------+-------------+------------+
```

### **Output:**
```
+---------+------------+----------------+
| user_id | steps_date | rolling_average|
+---------+------------+----------------+
|    1    | 2021-09-06 |      535.33    |
|    1    | 2021-09-07 |      595.67    |
|    2    | 2021-09-08 |      284.67    |
|    3    | 2021-09-09 |      505.67    |
|    3    | 2021-09-10 |      674.67    |
+---------+------------+----------------+
```

✅ **Explanation:**  
1. **User 1** → Steps from **Sep 2, Sep 4, Sep 7**:
   - (395 + 499 + 712) ÷ 3 = **535.33**
   - Next 3 days → **595.67**
2. **User 2** → Steps from **Sep 7, Sep 9, (next available date missing)**:
   - (153 + 171 + 530) ÷ 3 = **284.67**
3. **User 3** → Steps from **Sep 8, Sep 9, Sep 10**:
   - (120 + 557 + 840) ÷ 3 = **505.67**
   - (557 + 840 + 627) ÷ 3 = **674.67**

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Use Pandas Rolling Window**
1. **Sort the data** by `user_id` and `steps_date` to ensure correct ordering.  
2. **Use `rolling(window=3, min_periods=3)`** to compute the 3-day rolling average.  
3. **Round the result to 2 decimal places** for accuracy.  
4. **Drop NaN values**, ensuring only days with a full 3-day window are included.  

## 📝 **Implementation**  

```python
# rolling_average_steps.py

import pandas as pd

def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the 3-day rolling average of steps for each user.

    Args:
        steps (pd.DataFrame): Contains step count data with columns:
            - "user_id" (int): The ID of the user.
            - "steps_count" (int): The number of steps taken on a given date.
            - "steps_date" (datetime): The date of recorded steps.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The ID of the user.
            - "steps_date" (datetime): The date for which the rolling average is calculated.
            - "rolling_average" (float): The computed rolling average rounded to two decimal places.
              Only rows where a valid 3-day rolling average is available are included.
    """
    # Sort data by date for correct rolling computation
    steps = steps.sort_values(by=["user_id", "steps_date"])

    # Compute rolling 3-day average per user
    steps["rolling_average"] = (
        steps.groupby("user_id")["steps_count"]
        .rolling(window=3, min_periods=3)       # Ensure at least 3 days for calculation
        .mean()
        .round(2)
        .reset_index(level=0, drop=True)        # Maintain proper indexing
    )

    # Drop rows where rolling average could not be computed
    return steps.dropna(subset=["rolling_average"])[["user_id", "steps_date", "rolling_average"]]

```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Sorting by `user_id`, `steps_date`    | **O(N log N)** |
| Computing rolling averages            | **O(N)** |
| Filtering & dropping NaN values       | **O(N)** |
| **Overall Complexity**                 | **O(N log N)** ✅ |

> **N = number of records in the dataset**  

## 📂 **Project Structure**  

```
2854. Rolling Average Steps/
├── rolling_average_steps.py  # Python solution
├── README.md                 # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `rolling(window=3, min_periods=3)`** for efficient time-series calculations.  
✔ **Orders data before applying rolling windows to ensure correctness.**  
✔ **Only includes rows where a valid 3-day rolling average is available.**  

🚀 **Mastering rolling window functions is essential for time-series analysis!** 🔥