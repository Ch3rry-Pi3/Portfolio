# 📝 **LeetCode 1132: Reported Posts II**

## 📌 **Problem Overview**
You are given two tables:  
1. **`Actions` Table**: Tracks different user interactions with posts (e.g., views, likes, reports).  
2. **`Removals` Table**: Logs posts that were removed after being reported.  

A post can be **reported as spam** in the `Actions` table (`extra = 'spam'`).  
If a post was **removed after being reported**, it will appear in the `Removals` table.  

### **Goal**
- Compute the **average daily percentage** of spam-reported posts that were later removed.  
- **Round the final result to two decimal places**.  

## 📊 **Database Schema**
### **Actions Table**
| Column Name  | Type   | Description |
|-------------|--------|-------------|
| `user_id`    | int    | ID of the user performing the action |
| `post_id`    | int    | ID of the post |
| `action_date` | date   | Date when the action occurred |
| `action`      | enum   | Type of action (`'view'`, `'like'`, `'reaction'`, `'comment'`, `'report'`, `'share'`) |
| `extra`      | varchar | Additional info about the action (e.g., `"spam"` reason for reports) |

### **Removals Table**
| Column Name  | Type   | Description |
|-------------|--------|-------------|
| `post_id`   | int    | ID of the post that was removed |
| `remove_date` | date   | Date when the post was removed |

## 🛠 **Approach**
1. **Filter out posts that were reported as spam** (`extra = "spam"`) in the `Actions` table.
2. **Remove duplicates** based on (`action_date`, `post_id`) to count each report only once per day.
3. **Merge with the `Removals` table** to identify spam-reported posts that were actually removed.
4. **Compute daily statistics**:
   - Count of spam-reported posts per `action_date`.
   - Count of removed posts per `action_date`.
5. **Calculate daily removal percentage**:

   \[
   \text{Daily Removal Percentage} = \frac{\text{Removed Spam Reports}}{\text{Total Spam Reports}} \times 100
   \]

6. **Compute the average of daily removal percentages**, rounded to **two decimal places**.

## 🚀 **Python Solution**
```python
import pandas as pd


def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average daily percentage of spam-reported posts that were removed.

    Args:
        actions (pd.DataFrame): A DataFrame containing post interactions.
        removals (pd.DataFrame): A DataFrame containing removed posts.

    Returns:
        pd.DataFrame: A DataFrame with the average daily removal percentage.
    """

    # Step 1: Filter actions to get only spam reports
    spam_reports = actions[actions["extra"] == "spam"].drop_duplicates(["action_date", "post_id"])

    # Step 2: Merge with removals to check if spam-reported posts were actually removed
    removed_spam = spam_reports.merge(removals, on="post_id", how="left")

    # Step 3: Group by action_date to count reported and removed spam posts
    daily_stats = (
        removed_spam
        .groupby("action_date", as_index=False)
        .agg(
            removed_spam=("remove_date", "count"),      # Count removed spam posts
            total_spam=("remove_date", "size")          # Count total spam reports
        )
    )

    # Step 4: Compute the daily percentage of removed spam posts
    daily_stats["daily_percent"] = (daily_stats["removed_spam"] * 100 / daily_stats["total_spam"])

    # Step 5: Compute the overall average and round to two decimal places
    avg_daily_percent = daily_stats["daily_percent"].mean().round(2)

    return pd.DataFrame({"average_daily_percent": [avg_daily_percent]})

```

## 📌 **Example Walkthrough**
### **Example Input**
#### **Actions Table**
| user_id | post_id | action_date | action  | extra  |
|---------|--------|-------------|---------|--------|
| 1       | 1      | 2019-07-01  | view    | null   |
| 1       | 1      | 2019-07-01  | like    | null   |
| 2       | 2      | 2019-07-02  | report  | spam   |
| 2       | 3      | 2019-07-03  | view    | null   |
| 3       | 3      | 2019-07-03  | report  | racism |
| 3       | 4      | 2019-07-04  | spam    | spam   |
| 4       | 4      | 2019-07-04  | view    | null   |
| 5       | 5      | 2019-07-04  | report  | racism |
| 5       | 5      | 2019-07-04  | view    | null   |
| 5       | 5      | 2019-07-04  | spam    | spam   |

#### **Removals Table**
| post_id | remove_date |
|---------|------------|
| 2       | 2019-07-20 |
| 3       | 2019-07-18 |

### **Output**
```python
   average_daily_percent
0                  75.00
```

### **Explanation**
- On **2019-07-04**, there were **2 spam reports**, but only **1 was removed** → **50% removal rate**.
- On **2019-07-02**, **1 spam post was reported and removed** → **100% removal rate**.
- Compute the **average removal rate** across days: 

  \[
  \frac{50 + 100}{2} = 75.00\%
  \]

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter spam reports | `actions[actions["extra"] == "spam"]` | **O(N)** |
| Remove duplicates | `.drop_duplicates(["action_date", "post_id"])` | **O(N log N)** |
| Merge with removals | `.merge(removals, on="post_id")` | **O(N)** |
| Group by `action_date` | `.groupby("action_date")` | **O(N)** |
| Compute daily percentages | `.assign(daily_percent=...)` | **O(N)** |
| Compute mean | `.mean().round(2)` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

---

## 🎯 **Why This Approach?**
✔ **Handles duplicate reports efficiently**.  
✔ **Uses Pandas’ vectorised operations for fast computation**.  
✔ **Ensures correct rounding and result format**.  

🚀 **With this approach, you can quickly compute spam report effectiveness in any dataset!** 🎯