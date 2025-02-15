# 📊 **LeetCode 1149: Article Views II**  

## 📌 **Problem Overview**  
You are given a table `Views` that tracks **article views** by different users on a social platform. Each row represents a record of a user (`viewer_id`) viewing an article (`article_id`) on a specific date (`view_date`).  

### **Goal**  
Find and return the **list of users who have viewed more than one article on the same date**.  
- The result should contain only **distinct `viewer_id`s**.  
- The output should be **sorted in ascending order** by `id`.  

## 📊 **Database Schema**  
### **Views Table**  
| Column Name  | Type | Description |
|-------------|------|-------------|
| `article_id` | int  | ID of the viewed article |
| `author_id`  | int  | ID of the article’s author |
| `viewer_id`  | int  | ID of the user who viewed the article |
| `view_date`  | date | Date when the article was viewed |

## 🛠 **Approach**  
1. **Group by `viewer_id` and `view_date`** to count the number of **unique articles** viewed on the same day.  
2. **Filter** out entries where the unique article count is **≤ 1** (i.e., users who viewed only one article).  
3. **Extract the unique `viewer_id`s**, sort them in **ascending order**, and return as a DataFrame.  

## 🚀 **Python Solution**  
```python
import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """
    Finds viewers who have viewed more than one unique article on the same date.

    Args:
        views (pd.DataFrame): A DataFrame containing article view records with columns:
            - "article_id" (int): ID of the article.
            - "author_id" (int): ID of the article's author.
            - "viewer_id" (int): ID of the user who viewed the article.
            - "view_date" (date): The date when the article was viewed.

    Returns:
        pd.DataFrame: A DataFrame containing viewer IDs who have viewed multiple articles
                      on the same date, sorted in ascending order.
    """

    # Group by viewer_id and view_date, counting the number of unique articles viewed
    grouped = views.groupby(["viewer_id", "view_date"]).agg({"article_id": "nunique"})

    # Filter to keep only those who viewed more than one unique article on the same date
    result = grouped[grouped["article_id"] > 1].reset_index()

    # Extract unique viewer IDs, sort them, and return as a DataFrame
    final_result = (
        result["viewer_id"]
        .sort_values()
        .drop_duplicates()
        .to_frame(name="id")
        .reset_index(drop=True)
    )

    return final_result
```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Views Table**  
| article_id | author_id | viewer_id | view_date  |
|------------|----------|-----------|------------|
| 1          | 3        | 5         | 2019-08-01 |
| 3          | 3        | 5         | 2019-08-01 |
| 1          | 7        | 6         | 2019-08-01 |
| 2          | 7        | 6         | 2019-08-02 |
| 3          | 6        | 6         | 2019-08-02 |
| 4          | 4        | 4         | 2019-07-21 |
| 3          | 4        | 4         | 2019-07-21 |
| 4          | 4        | 4         | 2019-07-21 |

### **Processing Steps**  
1. **Group by `viewer_id` and `view_date`**:  
   - Count the number of unique articles per user per day.
2. **Filter viewers with more than 1 unique article** per day.
3. **Extract unique `viewer_id`s** and **sort in ascending order**.

### **Output**  
```python
   id
0  5
1  6
```

### **Explanation**  
- **Viewer `5`** viewed articles `1` and `3` on **2019-08-01**.  
- **Viewer `6`** viewed articles `2` and `3` on **2019-08-02**.  
- **Viewer `4`** also viewed multiple articles, but since the output is **sorted**, viewer `5` and `6` appear first.  

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Group by `viewer_id`, `view_date` | `groupby(["viewer_id", "view_date"])` | **O(N)** |
| Count unique articles | `.agg({"article_id": "nunique"})` | **O(N)** |
| Filter entries | `.query("article_id > 1")` | **O(N)** |
| Sort viewer IDs | `.sort_values().drop_duplicates()` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Ensures only users who viewed multiple articles are included**.  
✔ **Uses efficient Pandas operations** (`groupby`, `agg`, `query`, `sort_values`).  
✔ **Handles duplicate records** properly.  

🚀 **With this approach, you can quickly analyse article engagement trends in any dataset!** 🎯