# 🛑 **LeetCode 1113: Reported Posts** 

## 📌 **Overview** 
This project solves **LeetCode Problem 1113: Reported Posts**, which requires **counting the number of posts reported** for each unique report reason on **2019-07-04**.

### **Problem Statement** 
You are given a table:

1. **Actions Table (`actions`)**  
   - Contains user interactions, including **post views, likes, comments, reactions, shares, and reports**.
   - Each row represents an action taken by a user on a specific post, along with additional metadata.
   - The **`extra`** column contains the **report reason** (e.g., `"spam"` or `"racism"`) for **reported** posts.

👉 **Goal**:  
- Count the number of **reported posts** for each unique **report reason**.
- Exclude non-reported posts (where `action != 'report'`).
- The result can be returned in **any order**.

## 🎯 **Example Walkthrough** 

### **Example 1**  
#### **Input:**
#### **Actions Table**
| user_id | post_id | action_date | action  | extra   |
|---------|--------|-------------|---------|---------|
| 1       | 1      | 2019-07-01  | view    | null    |
| 1       | 1      | 2019-07-01  | like    | null    |
| 2       | 4      | 2019-07-04  | report  | spam    |
| 3       | 5      | 2019-07-04  | report  | spam    |
| 4       | 3      | 2019-07-04  | report  | racism  |
| 5       | 5      | 2019-07-04  | report  | racism  |

#### **Output:**
| report_reason | report_count |
|--------------|-------------|
| spam         | 2           |
| racism       | 2           |

#### **Explanation**
- On **2019-07-04**, posts were reported for **spam** and **racism**.
- **Spam reports:** 2 posts.
- **Racism reports:** 2 posts.
- Other actions like "view" and "like" are ignored.

## 🛠 **Approach**
### **1️⃣ Filter Relevant Rows**
- Extract only **rows where**:
  - `action == 'report'`
  - `action_date == '2019-07-04'`
  
### **2️⃣ Group & Count Reports**
- Count **unique** `post_id`s per `extra` (report reason).

### **3️⃣ Return the Final DataFrame**
- The final result should have **columns**:
  - `report_reason`
  - `report_count`

## 🚀 **Implementation**
```python
import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a DataFrame showing the count of reported posts by reason on 2019-07-04.
    """

    # Filter for reports on 2019-07-04
    reported = actions.query("action == 'report' and action_date == '2019-07-04'")
    
    # Count unique post IDs per report reason
    report_summary = reported.groupby("extra", as_index=False)["post_id"].nunique()
    
    # Rename columns
    report_summary.rename(columns={"extra": "report_reason", "post_id": "report_count"}, inplace=True)

    return report_summary
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filtering | `.query()` | **O(N)** |
| Grouping | `.groupby().nunique()` | **O(N)** |
| Renaming Columns | `.rename()` | **O(1)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
reported_posts/
├── reported_posts.py  # Python solution
├── README.md          # This documentation
```

## 🏆 **Why This Works**
✔ **Efficient filtering** using `.query()`.  
✔ **Vectorised grouping & counting** using `.groupby().nunique()`.  
✔ **Minimal memory usage** by avoiding explicit loops.  

**🚀 Now you can efficiently analyse reported posts using Pandas!** 🎯