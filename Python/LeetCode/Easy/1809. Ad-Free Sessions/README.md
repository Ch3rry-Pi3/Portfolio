# 🎯 **LeetCode 1809: Ad-Free Sessions**

## 📌 **Problem Overview**
You are given two tables:  
- **`Playback`**: Contains session details, including `session_id`, `customer_id`, `start_time`, and `end_time`.  
- **`Ads`**: Contains information about ads shown to customers, including `ad_id`, `customer_id`, and `timestamp`.  

Each session runs during the **inclusive** interval `[start_time, end_time]`.  
Sessions for the same customer **do not overlap**.  

### **Goal**  
Find all **sessions** that **did not** display any ads.

### **Example Input**
#### **Playback Table**
| session_id | customer_id | start_time | end_time |
|------------|------------|------------|----------|
| 1          | 1          | 1          | 5        |
| 2          | 1          | 15         | 23       |
| 3          | 2          | 10         | 12       |
| 4          | 2          | 17         | 28       |
| 5          | 2          | 8          | 12       |

#### **Ads Table**
| ad_id | customer_id | timestamp |
|-------|------------|-----------|
| 1     | 1          | 5         |
| 2     | 2          | 17        |
| 3     | 2          | 20        |

### **Example Output**
#### **Ad-Free Sessions**
| session_id |
|------------|
| 2          |
| 3          |
| 5          |

### **Explanation**
- **Session 1** (User 1) received an ad at `timestamp = 5`, so it **is not ad-free**.
- **Session 2** (User 1) did not receive any ads **✅**.
- **Session 3** (User 2) did not receive any ads **✅**.
- **Session 4** (User 2) received ads at `timestamp = 17` and `20`, so it **is not ad-free**.
- **Session 5** (User 2) did not receive any ads **✅**.

Thus, the **ad-free sessions are 2, 3, and 5**.

## 🛠 **Approach**
This problem can be efficiently solved using **SQL-style merging and filtering** in Pandas.

1. **Join `playback` and `ads`** on `customer_id` using a **left join**.
2. **Filter sessions that received ads** using:
   ```python
   .query("start_time <= timestamp <= end_time")
   ```
   This selects all `session_id` values that received ads.
3. **Remove blocked sessions** from `playback`:
   ```python
   playback.loc[~playback["session_id"].isin(blocked)]
   ```
   This keeps only **ad-free sessions**.

### 🔹 **Key Observations**
- **Efficient filtering**: `query("start_time <= timestamp <= end_time")` avoids unnecessary looping.
- **Dropping duplicates** ensures each session is considered only once.
- **Final filtering** removes all sessions that had at least one ad.

## 🚀 **Python Solution**
```python
import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all playback sessions that did not receive any ads.

    Args:
        playback (pd.DataFrame): DataFrame containing playback session details.
        ads (pd.DataFrame): DataFrame containing ad display records.

    Returns:
        pd.DataFrame: A DataFrame containing only the `session_id` column of sessions 
                      that did not receive any ads.
    """
    return (
        playback
        .merge(ads, on="customer_id", how="left")
        .query("start_time <= timestamp <= end_time")["session_id"]
        .drop_duplicates()
        .pipe(lambda blocked: playback.loc[~playback["session_id"].isin(blocked), ["session_id"]])
    )
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge DataFrames | `playback.merge(ads, how="left")` | **O(N + M)** |
| Filter ads | `.query("start_time <= timestamp <= end_time")` | **O(N)** |
| Drop duplicates | `.drop_duplicates()` | **O(N)** |
| Remove blocked sessions | `.loc[~playback["session_id"].isin(blocked)]` | **O(N)** |
| **Total Complexity** | **O(N + M)** | ✅ **Efficient** |

## 🎯 **Why This Approach?**
✔ **Uses vectorised Pandas operations** for efficient filtering.  
✔ **Eliminates unnecessary loops**, making it scalable.  
✔ **Runs in linear time `O(N + M)`**, ensuring optimal performance.  

🚀 **With this approach, we efficiently find all sessions that never received ads!** 🎯

This **README** is well-structured and includes:
- ✅ **Problem statement**
- ✅ **Examples**
- ✅ **Approach explanation**
- ✅ **Optimised Python solution**
- ✅ **Complexity analysis**
- ✅ **Why this approach?**

Hope this helps! 🚀🔥 Let me know if you'd like any modifications! 😊