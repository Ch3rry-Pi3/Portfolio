# 📊 **LeetCode 1107: New Users Daily Count**

## 📌 **Problem Overview**
You are given a `Traffic` table that tracks user activity on a website. The `activity` column records different types of actions such as `"login"`, `"logout"`, `"jobs"`, `"groups"`, and `"homepage"`.

### **Goal**
For every date within **the last 90 days from June 30, 2019**, determine the number of users who logged in for the **first time** on that date.

### **Constraints**
- A user may log in multiple times.
- Only the **first login date** for each user should be considered.
- The result should include **only dates where at least one new user logged in**.
- The output can be returned **in any order**.

## 📊 **Database Schema**
### **Traffic Table**
| Column Name     | Type    | Description |
|---------------|--------|-------------|
| `user_id`      | int    | Unique identifier for each user |
| `activity`     | ENUM   | Type of activity (`"login"`, `"logout"`, `"jobs"`, etc.) |
| `activity_date`| date   | The date when the activity occurred |

## 🛠 **Approach**
1. **Filter login events**:
   - Select only rows where `activity = "login"`.
   - Remove duplicate login attempts by keeping only the first occurrence for each user.
  
2. **Determine first login date** for each user:
   - Use `groupby("user_id")` to find the earliest `activity_date`.

3. **Restrict to the last 90 days before `"2019-06-30"`**:
   - Consider users whose first login occurred **between `"2019-04-01"` and `"2019-06-30"`**.

4. **Count the number of users logging in for the first time on each date**.

5. **Format the result**:
   - Rename `activity_date` to `login_date`.
   - Rename `user_id` count to `user_count`.

## 🚀 **Python Solution**
```python
import pandas as pd
from datetime import timedelta

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of users who logged in for the first time on each date within the last 90 days.

    Args:
        traffic (pd.DataFrame): A DataFrame containing user activity logs with columns:
            - 'user_id' (int): The unique ID of the user.
            - 'activity' (str): The type of activity ('login', 'logout', etc.).
            - 'activity_date' (datetime): The date the activity occurred.

    Returns:
        pd.DataFrame: A DataFrame with the first login date and the count of users who logged in for the first time.
    """

    # Filter only login activities and remove duplicate user entries
    df = traffic[traffic["activity"] == "login"].drop_duplicates()

    # Find the first login date for each user
    first_login = df.groupby("user_id", as_index=False)["activity_date"].min()

    # Define the date range: last 90 days before '2019-06-30'
    start_date = pd.to_datetime("2019-06-30") - timedelta(days=90)
    first_login = first_login[first_login["activity_date"].between(start_date, "2019-06-30")]

    # Count users who logged in for the first time on each date
    final = first_login.groupby("activity_date", as_index=False)["user_id"].count()

    # Rename columns for clarity
    return final.rename(columns={"activity_date": "login_date", "user_id": "user_count"})

```

## 📌 **Example Walkthrough**
### **Example Input**
#### **Traffic Table**
| user_id | activity | activity_date |
|---------|----------|--------------|
| 1       | login    | 2019-05-01   |
| 1       | homepage | 2019-05-01   |
| 1       | login    | 2019-06-21   |
| 2       | login    | 2019-06-21   |
| 3       | login    | 2019-06-21   |
| 3       | logout   | 2019-06-21   |
| 4       | login    | 2019-03-01   |
| 5       | login    | 2019-06-21   |
| 5       | login    | 2019-03-01   |

### **Processing Steps**
1. Filter **only "login" activities**.
2. Determine **each user's first login date**.
3. Consider **only first logins between 2019-04-01 and 2019-06-30**.
4. Count **the number of unique users for each date**.

### **Output**
| login_date | user_count |
|------------|-----------|
| 2019-05-01 | 1         |
| 2019-06-21 | 2         |

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter login activities | `traffic["activity"] == "login"` | **O(N)** |
| Remove duplicate logins | `.drop_duplicates()` | **O(N log N)** |
| Group by user ID to find first login | `groupby("user_id").min()` | **O(N log N)** |
| Filter last 90 days | `.between(start_date, "2019-06-30")` | **O(N)** |
| Count new users per date | `groupby("activity_date").count()` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Efficient filtering and grouping operations**.  
✔ **Ensures that only the first login per user is counted**.  
✔ **Handles edge cases where users log in multiple times**.  
✔ **Guaranteed to return correctly formatted results**.  

🚀 **With this approach, you can quickly track new user growth on any platform!** 🎯