# 🔥 **LeetCode 3087: Find Trending Hashtags**  

## 📌 **Problem Overview**  

You are given a table **Tweets** containing user tweets, where each tweet contains **only one hashtag**.  

| Column Name  | Type   |
|-------------|--------|
| user_id     | int    |
| tweet_id    | int    |
| tweet_date  | date   |
| tweet       | varchar |

- Each tweet contains **exactly one hashtag** (e.g., `#TechLife`, `#WorkLife`).  
- We need to **find the top 3 trending hashtags in February 2024**.  
- If there are ties, **order them by hashtag name in descending order**.  

✅ **Return the result table ordered by hashtag count in descending order, then by hashtag in descending order.**  

## 📊 **Example 1**  

### **Input**  

**Tweets Table:**
| user_id | tweet_id | tweet                                   | tweet_date  |
|---------|---------|-----------------------------------------|------------|
| 135     | 13      | Enjoying a great start to the day! #HappyDay | 2024-02-01 |
| 140     | 17      | Exploring new tech frontiers. #TechLife  | 2024-02-04 |
| 137     | 15      | Productivity peaks! #WorkLife           | 2024-02-04 |
| 135     | 14      | Another #HappyDay with good vibes!      | 2024-02-03 |
| 140     | 19      | Innovation drives us. #TechLife        | 2024-02-07 |
| 141     | 19      | Connecting with nature's serenity. #Nature | 2024-02-09 |
| 140     | 17      | Gratitude for today's moments. #HappyDay | 2024-02-05 |

### **Output**  

| hashtag    | hashtag_count |
|------------|--------------|
| #HappyDay  | 3            |
| #TechLife  | 2            |
| #WorkLife  | 1            |

✅ **Explanation:**  
- **#HappyDay** appears **3 times**, making it the most trending hashtag.  
- **#TechLife** appears **2 times**, making it the second most trending.  
- **#WorkLife** appears **once**, making it the third most trending.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea:**  
- **Extract the hashtags** from the tweets.  
- **Count occurrences** of each hashtag.  
- **Sort the results** by count in descending order, and by hashtag name in descending order if counts are the same.  
- **Return only the top 3** hashtags.  

### 🛠 **Implementation Steps**
1. **Extract hashtags** using regex (`r'(#[\w]+)'`) from each tweet.  
2. **Group by hashtag** and count occurrences.  
3. **Sort results** by count (descending), then by hashtag name (descending).  
4. **Return the top 3** hashtags.

## 📝 **Implementation**  

```python
import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the top 3 trending hashtags in February 2024.

    :param tweets: DataFrame containing user tweets.
    :return: DataFrame with the top 3 trending hashtags.
    """
    pattern = r'(#[\w]+)'

    return (
        tweets
        .assign(HASHTAG=lambda x: x["tweet"].str.extract(pattern))
        .groupby("HASHTAG")["HASHTAG"]
        .count()
        .reset_index(name="HASHTAG_COUNT")
        .sort_values(by=["HASHTAG_COUNT", "HASHTAG"], ascending=[False, False])
        .head(3)
    )

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| Extracting hashtags | **O(N)** |
| Grouping & Counting | **O(N)** |
| Sorting results | **O(N log N)** |
| **Overall Complexity** | **O(N log N)** ✅ |

🔹 **Why is this optimal?**  
- **Efficiently extracts hashtags** using Pandas' `str.extract()`.  
- **Uses fast vectorised operations** for counting and sorting.  

## 📂 **Project Structure**  

```
find_trending_hashtags/
├── find_trending_hashtags.py  # Python solution
├── README.md                   # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Regex-based hashtag extraction** ensures accurate parsing.  
✔ **Vectorised Pandas operations** enable fast computation.  
✔ **Sorting ensures correct ranking and tie-breaking.**  

🚀 **Master this pattern for analysing text trends!** 🔥