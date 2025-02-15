# 📊 **LeetCode 614: Second Degree Follower**  

## 📌 **Problem Overview**  
A **second-degree follower** in a social network is a user who:  
- **Follows at least one user**.  
- **Is followed by at least one user**.  

You are given a **Follow** table where each row represents a connection between two users.  
The goal is to **find all second-degree followers** and count how many people follow them.  

### **Sorting Requirement**  
- Return the result ordered by **`follower` in alphabetical order**.

## 📊 **Database Schema**  
### **Follow Table**  
| Column Name | Type   | Description                               |
|------------|--------|-------------------------------------------|
| `followee` | varchar | The user who is being followed.         |
| `follower` | varchar | The user who follows another user.      |

## 🛠 **Approach**  
1. **Identify second-degree followers**:
   - A user is a second-degree follower **if they appear in both `follower` and `followee` columns**.
   - This means they **follow at least one person** and are **followed by someone**.
2. **Count the number of followers** each second-degree user has.
3. **Sort results alphabetically** by `follower` to meet the problem’s requirements.

## 🚀 **Python Solution**  
```python
import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies second-degree followers in a social network.

    Args:
        follow (pd.DataFrame): A DataFrame with columns ["followee", "follower"].

    Returns:
        pd.DataFrame: A DataFrame with ["follower", "num"], where "num" represents the count of followers.
    """
    return (
        follow[follow["followee"].isin(follow["follower"])]
        .groupby("followee", as_index=False)
        .agg(num=("follower", "count"))
        .rename(columns={"followee": "follower"})
        .sort_values(by="follower", ascending=True)
    )
```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Follow Table**
| followee | follower |
|----------|----------|
| Alice    | Bob      |
| Bob      | Cena     |
| Bob      | Donald   |
| Donald   | Edward   |

### **Output**
| follower | num |
|----------|----|
| Bob      | 1  |
| Donald   | 1  |

### **Explanation**
- **Bob** is a second-degree follower because:
  - He **follows** Donald.
  - He is **followed by** Cena.
  - He has **1 follower**.
- **Donald** is a second-degree follower because:
  - He **follows** Edward.
  - He is **followed by** Bob.
  - He has **1 follower**.

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Identify second-degree users | `followee.isin(follower)` | **O(N)** |
| Group and count followers | `groupby("followee").count()` | **O(N)** |
| Sorting results | `sort_values(by="follower")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Simple and efficient Pandas operations**.  
✔ **Handles large datasets well**.  
✔ **Guaranteed correct sorting** by `follower`.  

🚀 **With this approach, you can efficiently determine second-degree followers in any social network dataset!** 🎯