# 📝 **LeetCode 1241: Number of Comments per Post**

## 📌 **Overview**
This project solves **LeetCode Problem 1241: Number of Comments per Post**. The goal is to find the **number of unique comments** for each post.

### **Problem Statement**
You are given a table:

- **Submissions Table (`submissions`)**
  - Contains both **posts** and **comments**.
  - A **post** has `parent_id = NULL`.
  - A **comment** has a `parent_id` referring to a post’s `sub_id`.

👉 The task is to count **unique comments** for each post.

### **Expected Output**
- A table with:
  - **`post_id`**: The ID of the post.
  - **`number_of_comments`**: The count of unique comments.
- Posts **without comments** should have a `number_of_comments = 0`.
- The result should be **sorted in ascending order by `post_id`**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
| sub_id | parent_id |
|--------|----------|
| 1      | NULL     |
| 2      | NULL     |
| 12     | NULL     |
| 5      | 2        |
| 3      | 1        |
| 4      | 1        |
| 9      | 1        |
| 10     | 2        |
| 6      | 7        |

#### **Output:**
| post_id | number_of_comments |
|---------|--------------------|
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |

#### **Explanation**
- **Post 1** has **3 comments**: `3, 4, 9`.
- **Post 2** has **2 comments**: `5, 10`.
- **Post 12** has **0 comments** (no linked `parent_id` entries).
- **Comment 6** refers to `parent_id = 7`, which does not exist in the table, so it is ignored.

## 🛠 **Approach**
### **1️⃣ Identify Posts**
- A **post** has `parent_id = NULL`.

### **2️⃣ Count Unique Comments**
- Group by `parent_id` to count **unique comments** for each post.

### **3️⃣ Merge Results**
- Merge posts with the counted comments and fill `NaN` values with `0`.

### **4️⃣ Sort by `post_id`**
- Return the result sorted by `post_id`.

## 🚀 **Implementation**
```python
import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of unique comments for each post.
    Returns a DataFrame containing post_id and number_of_comments.
    """

    # Identify posts (submissions with no parent_id)
    posts = submissions[submissions["parent_id"].isna()]

    # Count unique comments for each post
    comment_counts = submissions.groupby("parent_id")["sub_id"].nunique().reset_index(name="number_of_comments")

    # Merge posts with comment counts
    result = pd.merge(posts, comment_counts, left_on="sub_id", right_on="parent_id", how="left").drop_duplicates(subset="sub_id")

    # Fill NaN values for posts without comments
    result["number_of_comments"].fillna(0, inplace=True)

    # Select only required columns and rename
    result = result[["sub_id", "number_of_comments"]].rename(columns={"sub_id": "post_id"})

    return result.sort_values(by="post_id")
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Identify Posts | `submissions["parent_id"].isna()` | **O(N)** |
| Count Unique Comments | `groupby().nunique()` | **O(N)** |
| Merge with Posts | `merge(posts, comment_counts)` | **O(N)** |
| Fill NaN Values | `fillna(0)` | **O(N)** |
| Sorting | `sort_values()` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

---

## 🏗 **Project Structure**
```
comments_per_post/
├── comments_per_post.py   # Python solution
├── README.md              # This documentation
```

## 🏆 **Why This Works**
✔ **Uses Pandas' efficient groupby operations** for counting unique comments.  
✔ **Handles missing values properly**, ensuring posts without comments return `0`.  
✔ **Ensures proper sorting**, returning results in ascending order.  

**🚀 Now you can efficiently count comments per post using Pandas!** 🎯