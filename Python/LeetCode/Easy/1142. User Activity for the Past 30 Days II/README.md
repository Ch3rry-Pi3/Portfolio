# 🎯 **LeetCode 1142: User Activity for the Past 30 Days II**

## 📌 **Problem Overview**
Given a table `Activity`, find the **average number of sessions per user** for the last **30 days** ending on `2019-07-27` (inclusive). The result should be **rounded to two decimal places**.  

A session is counted only if a user has **at least one activity** in the specified time period.

## 🗂 **Table Schema**
### 🔹 `Activity` Table:
| Column Name      | Type    | Description |
|-----------------|---------|-------------|
| `user_id`       | `int`   | The unique ID of the user. |
| `session_id`    | `int`   | The session identifier. |
| `activity_date` | `date`  | The date when the user performed an activity. |
| `activity_type` | `enum`  | The type of activity (`open_session`, `end_session`, `scroll_down`, `send_message`). |

### **Constraints:**
- The table may contain **duplicate rows**.
- Each session belongs to exactly **one user**.
- Only users **who had at least one activity in the last 30 days** should be included.

## 📌 **Example Walkthrough**

### **Example 1**
#### **Input:**
#### `Activity` table:
| user_id | session_id | activity_date | activity_type |
|---------|------------|---------------|--------------|
| 1       | 1         | 2019-07-20    | open_session |
| 1       | 1         | 2019-07-20    | scroll_down  |
| 1       | 1         | 2019-07-20    | end_session  |
| 2       | 2         | 2019-07-21    | send_message |
| 2       | 2         | 2019-07-21    | open_session |
| 3       | 3         | 2019-07-21    | open_session |
| 3       | 3         | 2019-07-21    | scroll_down  |
| 3       | 4         | 2019-07-22    | open_session |
| 3       | 4         | 2019-07-22    | end_session  |
| 4       | 5         | 2019-06-15    | send_message |
| 4       | 5         | 2019-06-16    | end_session |

#### **Query Parameters:**
- `start_date = 2019-06-28`
- `end_date = 2019-07-27`
- Count **only users who had at least one activity during this period**.

#### **Output:**
| average_sessions_per_user |
|-------------------------|
| 1.33 |

#### **Explanation:**
- Users `1` and `2` each had **1 session** in the past 30 days.
- User `3` had **2 sessions** in the past 30 days.
- The average is **(1 + 1 + 2) / 3 = 1.33**.

## 🛠 **Approach**
To efficiently solve the problem, follow these steps:

1. **Filter activities**: Select only the rows where `activity_date` falls within the **30-day period** (`2019-06-28` to `2019-07-27`).
2. **Group by `user_id`**: Count the number of unique `session_id`s for each user.
3. **Compute the mean**: Calculate the average number of sessions across all valid users.
4. **Round the result**: Ensure the final result is **rounded to two decimal places**.

## 🚀 **Python Solution**
```python
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the average number of sessions per user over a 30-day period ending on 2019-07-27.

    Args:
        activity (pd.DataFrame): A DataFrame containing user activity logs.

    Returns:
        pd.DataFrame: A DataFrame with a single column 'average_sessions_per_user', rounded to two decimal places.
    """

    return (
        (
            activity[activity["activity_date"].between("2019-06-28", "2019-07-27")]
            .groupby("user_id", as_index=False)
            .agg({"session_id": "nunique"})
            .agg(average_sessions_per_user=("session_id", "mean"))
            .round(2)
            .transpose()
        )
        if activity["activity_date"].between("2019-06-28", "2019-07-27").any()
        else pd.DataFrame({"average_sessions_per_user": [0.00]})
    )
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Filter activities** | `between(start_date, end_date)` | **O(N)** |
| **Group & aggregate** | `groupby("user_id").agg(nunique)` | **O(N)** |
| **Compute mean** | `agg("mean")` | **O(1)** |
| **Total Complexity** | **O(N), Space: O(N)** | ✅ Efficient |

## 📝 **Edge Cases Considered**
✅ **Users with multiple sessions** → Ensuring correct counting per user.  
✅ **Users with no activity in the past 30 days** → Should be excluded.  
✅ **Users with sessions spanning multiple days** → Consider only those within `2019-06-28` to `2019-07-27`.  
✅ **Case with no valid users** → Return `0.00` as the default.

## 🎯 **Summary**
- **Filtered** activities within the past 30 days.
- **Counted unique sessions** per user.
- **Computed & rounded the average**.
- **Handled edge cases** efficiently.

🚀 **Optimised for performance and clarity!** 🎯