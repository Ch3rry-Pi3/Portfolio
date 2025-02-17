# 📊 **LeetCode 1454: Active Users**  

## 📌 **Problem Overview**  
You are given two tables:  

### **Accounts Table**  
| Column Name | Type    | Description |
|------------|--------|-------------|
| `id`       | int    | Unique user ID (Primary Key) |
| `name`     | varchar | User's name |

### **Logins Table**  
| Column Name | Type    | Description |
|------------|--------|-------------|
| `id`       | int    | User ID corresponding to a login event |
| `login_date` | date | The date the user logged in |

### **Goal**  
Find users who have **logged in for five or more consecutive days**, returning their `id` and `name`, sorted by `id`.

## 🛠 **Approach**  

1. **Remove duplicate logins**  
   - Some users might log in multiple times on the same day. Use `.drop_duplicates()` to keep only unique login dates.

2. **Sort the data**  
   - Sort by `id` (user) and `login_date` (time order).

3. **Rank each user's logins**  
   - Use `groupby("id")["login_date"].rank(method="dense")` to assign a rank based on login order.

4. **Identify consecutive login streaks**  
   - Compute a **difference column**:  
     ```python
     diff = login_date - pd.to_timedelta(rank, unit="D")
     ```
   - If consecutive logins exist, their `diff` values will be the same.

5. **Count logins in each streak**  
   - Group by `id`, `name`, and `diff`, then count occurrences.  
   - If a user has **at least 5 logins in a streak**, they are an **active user**.

6. **Return the results sorted by `id`**  

## 🚀 **Python Solution**  

```python
import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active users who have logged in for five or more consecutive days.

    Args:
        accounts (pd.DataFrame): A DataFrame containing user account details with columns:
            - id (int): Unique user ID.
            - name (str): User's name.

        logins (pd.DataFrame): A DataFrame containing user login records with columns:
            - id (int): User ID corresponding to a login event.
            - login_date (date): The date the user logged in.

    Returns:
        pd.DataFrame: A DataFrame containing the IDs and names of active users,
                      sorted by ID in ascending order.
    """
    return (
        pd.merge(
            left=logins.drop_duplicates(),                                                          # Remove duplicate logins for the same user & date
            right=accounts,
            on="id",
            how="left"
        )
        .sort_values(by=["id", "login_date"])                                                       # Sort by user ID and login date
        .assign(
            rank=lambda x: x.groupby("id")["login_date"].rank(method="dense"),                      # Rank logins per user
            diff=lambda x: x["login_date"] - pd.to_timedelta(x["rank"].astype(int), unit="D")       # Identify streaks
        )
        .groupby(["id", "name", "diff"], as_index=False)
        .count()                    # Count logins in each streak
        .query("rank >= 5")         # Keep only users with 5+ consecutive logins
        .sort_values(by="id")       # Sort by user ID
        [["id", "name"]]
        .drop_duplicates()          # Ensure unique users in the final output
    )
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Accounts Table**  
| id | name      |
|----|----------|
| 1  | Winston  |
| 7  | Jonathan |

#### **Logins Table**  
| id | login_date |
|----|------------|
| 7  | 2020-05-30 |
| 7  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 1  | 2020-06-10 |

### **Processing Steps**  
1. **Removing duplicate logins:**  
   - User `7` logs in twice on `"2020-05-30"`, keep only one.  

2. **Sorting logins by user and date:**  
   - Ensures correct rank calculation.

3. **Ranking each user's logins:**  
   - `Jonathan` (`id=7`) ranks as:
     ```
     2020-05-30 → Rank 1
     2020-05-31 → Rank 2
     2020-06-01 → Rank 3
     2020-06-02 → Rank 4
     2020-06-03 → Rank 5 ✅
     ```

4. **Finding consecutive streaks:**  
   - Since `diff` remains the same for all **5 consecutive logins**, `Jonathan` is an **active user**.

5. **Returning the result:**  
   - `Jonathan` is included in the final result.

### **Output**  
```python
   id      name
0   7  Jonathan
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Removing duplicates | `drop_duplicates()` | **O(N)** |
| Sorting | `sort_values()` | **O(N log N)** |
| Ranking logins | `groupby().rank()` | **O(N)** |
| Calculating streaks | `groupby().count()` | **O(N)** |
| Querying active users | `.query("rank >= 5")` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Handles large datasets efficiently**.  
✔ **Uses vectorised operations (`rank()`, `groupby()`) for speed**.  
✔ **Ensures correct identification of consecutive login streaks**.  

🚀 **This solution efficiently finds active users with five or more consecutive logins!** 🎯