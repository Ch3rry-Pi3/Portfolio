# 🐦 **LeetCode 3150: Invalid Tweets II**

## 📌 **Problem Overview**
In a social media application, tweets are stored in a database table. A tweet is considered **invalid** if it meets any of the following conditions:

1. **Exceeds** 140 characters in length.
2. **Contains more than 3 mentions** (i.e., words starting with `@`).
3. **Includes more than 3 hashtags** (i.e., words starting with `#`).

**Goal:**  
Find all **invalid** tweets based on the criteria above and return their corresponding `tweet_id`, sorted in **ascending order**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
| tweet_id | content |
|----------|----------------------------------------------------------------|
| 1        | Traveling, exploring, and living my best life @Jane @Sara @Lisa @Mike #Foodie #Fitness #Learning |
| 2        | Just had the best dinner with friends! #foodie #friends #fun |
| 3        | Working hard on my new project #Work #Goals #Productivity #Fun |
| 4        | A short valid tweet. |

#### **Output:**
| tweet_id |
|----------|
| 1        |
| 3        |

#### **Explanation:**
- **Tweet 1** contains **4 mentions (`@Jane @Sara @Lisa @Mike`)**, making it invalid.
- **Tweet 3** contains **4 hashtags (`#Work #Goals #Productivity #Fun`)**, making it invalid.
- **Tweet 2** and **Tweet 4** do **not** exceed the limits, so they are valid.

## 🛠 **Approach**
We solve this problem using **Pandas filtering**:

1. **Use `.str.len()`** to check for tweets exceeding **140 characters**.
2. **Use `.str.count("@")`** to count the number of mentions.
3. **Use `.str.count("#")`** to count the number of hashtags.
4. **Filter tweets** that meet any of these conditions and return only their `tweet_id`.
5. **Sort the result** in ascending order.

This approach ensures a highly efficient **O(N) time complexity**, as all operations leverage vectorised Pandas functions.

## 🚀 **Python Solution**
```python
import pandas as pd

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies invalid tweets based on specific criteria.

    A tweet is considered invalid if it meets any of the following conditions:
    - Exceeds 140 characters in length.
    - Contains more than 3 mentions (indicated by '@').
    - Contains more than 3 hashtags (indicated by '#').

    Args:
        tweets (pd.DataFrame): A DataFrame containing tweet data with columns:
            - "tweet_id" (int): The unique ID of the tweet.
            - "content" (str): The text content of the tweet.

    Returns:
        pd.DataFrame: A DataFrame containing only the "tweet_id" of invalid tweets,
                      sorted in ascending order.
    """
    invalid_tweets = tweets.loc[
        (tweets["content"].str.len() > 140) |
        (tweets["content"].str.count("@") > 3) |
        (tweets["content"].str.count("#") > 3),
        ["tweet_id"]
    ].sort_values(by="tweet_id", ascending=True)

    return invalid_tweets
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Check length | `.str.len()` | **O(N)** |
| Count mentions | `.str.count("@")` | **O(N)** |
| Count hashtags | `.str.count("#")` | **O(N)** |
| **Total Complexity** | **O(N) Time, O(1) Space** | ✅ Efficient |

## 📁 **Project Structure**
```
invalid_tweets/
├── invalid_tweets.py   # Python solution
├── README.md           # Documentation
```

## 🏆 **Why This Works**
✔ **Pandas vectorised operations** make this approach **fast** and **efficient**.  
✔ **Single-pass filtering**, ensuring **O(N) complexity**.  
✔ **Scales well** even for large tweet datasets.  

🚀 **With this solution, you can efficiently detect and filter invalid tweets in a social media dataset!** 🐦