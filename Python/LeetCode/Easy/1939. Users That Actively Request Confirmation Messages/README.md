# 🎯 **LeetCode 1939: Users That Actively Request Confirmation Messages**

## 📌 **Problem Overview**
We have two tables:

1. **Signups Table**  
   - Records the signup time of users.  
   - **Columns:** `user_id` (int), `time_stamp` (datetime).  

2. **Confirmations Table**  
   - Tracks when users request confirmation messages.  
   - **Columns:** `user_id` (int), `time_stamp` (datetime), `action` (enum: `"confirmed"`, `"timeout"`).  

### **Goal**
Find users who **requested a confirmation message twice within a 24-hour window**.  
Two requests exactly **24 hours apart** are **included** in the results.  

The **`action` column does not affect** the result—only the request time matters.

The output should contain **unique user IDs** of those meeting this condition.

## 🛠 **Approach**
We solve this problem efficiently using **sorting and grouping**:

1. **Sort Confirmation Requests**:  
   - Sort by `time_stamp` to track request sequences per user.

2. **Compute Time Differences**:  
   - Use `.diff()` to calculate **time gaps** between consecutive requests for each user.

3. **Filter Users with Two Requests ≤ 24 Hours**:  
   - If `diff ≤ 24 hours`, the user is included in the final result.

4. **Drop Duplicates**:  
   - Ensure each `user_id` appears **only once** in the output.

## 🚀 **Python Solution**
```python
import pandas as pd
from datetime import timedelta

def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies users who requested a confirmation message twice within a 24-hour window.

    Args:
        signups (pd.DataFrame): Signup information with columns:
            - user_id (int): User ID.
            - time_stamp (datetime): Signup timestamp.
        
        confirmations (pd.DataFrame): Confirmation requests with columns:
            - user_id (int): User requesting confirmation.
            - time_stamp (datetime): Request timestamp.
            - action (str): Type ('confirmed' or 'timeout').

    Returns:
        pd.DataFrame: Users who requested a confirmation message at least twice within 24 hours.
    """

    # Sort confirmations by time to compare requests
    confirmations = confirmations.sort_values("time_stamp")

    # Compute time differences between consecutive requests per user
    confirmations["diff"] = confirmations.groupby("user_id")["time_stamp"].diff()

    # Filter users who made two requests within 24 hours
    confirmations = confirmations[confirmations["diff"] <= timedelta(days=1)].dropna()

    # Extract unique user IDs that meet the condition
    return confirmations[["user_id"]].drop_duplicates()
```

## 📌 **Example Walkthrough**

### **Example 1**
#### **Input:**
```python
signups = [
    [3, "2020-03-21 10:16:13"],
    [2, "2021-08-04 13:57:59"],
    [7, "2020-07-29 23:09:44"],
    [6, "2022-12-09 10:39:37"]
]

confirmations = [
    [1, "2021-01-06 08:30:46", "timeout"],
    [2, "2021-01-06 03:37:45", "timeout"],
    [2, "2021-06-12 11:57:29", "confirmed"],
    [3, "2021-06-12 11:57:30", "confirmed"],
    [7, "2021-01-22 00:00:00", "confirmed"],
    [7, "2021-01-22 00:00:01", "confirmed"],
    [6, "2021-10-23 14:14:14", "confirmed"],
    [6, "2021-10-24 14:14:13", "timeout"]
]
```
#### **Output:**
```python
[
    [2],
    [3],
    [6]
]
```
#### **Explanation:**
- **User 2** made two requests **exactly 24 hours apart** → ✅ **Included**.
- **User 3** made two requests **within 6 minutes** → ✅ **Included**.
- **User 6** made two requests **within 23 hours, 59 minutes, 59 seconds** → ✅ **Included**.
- **User 7** made two requests **24 hours, 1 second apart** → ❌ **Excluded**.

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values("time_stamp")` | **O(N log N)** |
| Compute Differences | `groupby().diff()` | **O(N)** |
| Filter Requests | `df[df["diff"] <= 24 hours]` | **O(N)** |
| Drop Duplicates | `drop_duplicates()` | **O(N)** |
| **Total Complexity** | **O(N log N) (due to sorting)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Sorting + Grouping** makes tracking request intervals **efficient**.  
✔ **Diff-based filtering** ensures **only** users with **consecutive** requests ≤ 24h are included.  
✔ **O(N log N) time complexity** is optimal for large datasets.  

🚀 **With this approach, we efficiently determine which users request confirmation messages actively!** 🎯