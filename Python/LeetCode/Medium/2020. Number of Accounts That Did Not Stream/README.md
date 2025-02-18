# 📊 **LeetCode 2020: Number of Accounts That Did Not Stream**  

## 📌 **Problem Overview**  
Given two tables, **Subscriptions** and **Streams**, our task is to count the number of accounts that:  
✔ **Subscribed in 2021** (i.e., their subscription period includes the year 2021).  
✔ **Did not stream in 2021** (i.e., no record in the Streams table for that year).  

### **Table: Subscriptions**
| Column Name  | Type    | Description |
|-------------|--------|-------------|
| `account_id` | int    | Unique account ID. |
| `start_date` | date   | Subscription start date. |
| `end_date`   | date   | Subscription end date. |

### **Table: Streams**
| Column Name  | Type    | Description |
|-------------|--------|-------------|
| `session_id` | int    | Unique stream session ID. |
| `account_id` | int    | Account associated with the stream. |
| `stream_date` | date   | Date of the stream session. |

## 🎯 **Objective**  
Find the number of accounts that:  
✅ Had an **active subscription in 2021**.  
✅ **Did not stream** in 2021.  

### **Expected Output**
| Column Name    | Type | Description |
|---------------|------|-------------|
| `accounts_count` | int  | The number of accounts meeting the criteria. |

## 🛠 **Approach**  

1️⃣ **Merge** `Subscriptions` and `Streams` on `account_id` to see each account's streaming activity.  
2️⃣ **Filter** to keep only accounts that had a subscription **active in 2021**.  
3️⃣ **Identify** accounts that **did not stream** in 2021.  
4️⃣ **Count** the number of such accounts and return the result.

## 🚀 **Python Solution**  

```python
import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the number of accounts that subscribed in 2021 but did not have any stream session.

    Args:
        subscriptions (pd.DataFrame): A DataFrame containing subscription details.
        streams (pd.DataFrame): A DataFrame containing streaming session details.

    Returns:
        pd.DataFrame: A DataFrame with the count of such accounts.
    """

    # Merge subscriptions with streams to match account activities
    df = (
        pd.merge(left=subscriptions, right=streams, on="account_id", how="left")
        .assign(
            # Identify valid subscriptions in 2021
            valid_subscription=lambda x: (
                (x["start_date"].dt.year <= 2021) & (x["end_date"].dt.year >= 2021)
            ).astype(int),
            # Extract stream year
            stream_year=lambda x: x["stream_date"].dt.year
        )
        # Keep only valid subscriptions and accounts that did not stream in 2021
        .query("valid_subscription == 1 and (stream_year != 2021 or stream_year.isna())")
        # Remove duplicate accounts
        .drop_duplicates(subset="account_id")
    )

    # Count the number of accounts
    accounts_count = len(df["account_id"].unique())

    return pd.DataFrame({"accounts_count": [accounts_count]})
```

## 🔍 **Example Walkthrough**  

### **Input Data**
#### **Subscriptions Table**
| account_id | start_date | end_date   |
|------------|------------|------------|
| 9          | 2020-02-18 | 2021-10-30 |
| 3          | 2021-09-21 | 2021-11-13 |
| 13         | 2020-08-24 | 2021-09-08 |
| 4          | 2021-10-26 | 2021-09-28 |
| 15         | 2020-09-11 | 2021-01-17 |

#### **Streams Table**
| session_id | account_id | stream_date |
|------------|------------|------------|
| 14         | 9          | 2020-05-16 |
| 13         | 3          | 2020-10-27 |
| 17         | 13         | 2020-04-29 |
| 19         | 4          | 2020-12-31 |
| 13         | 5          | 2021-01-05 |

### **Processing Steps**
1. **Filter valid subscriptions**  
   - Accounts `3`, `9`, `4`, and `15` are valid for **2021**.  
2. **Check if they streamed in 2021**  
   - Account `3` has a stream in `2021`. ✅  
   - Accounts `9` and `4` **did not stream in 2021**. ❌  
3. **Count the results**  
   - **Total accounts that subscribed in 2021 but did not stream:** **2**

### **Output**
| accounts_count |
|---------------|
| 2 |

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Merge subscriptions with streams** | `O(N + M)` | ✅ Efficient |
| **Filter for 2021 subscriptions** | `O(N)` | ✅ Linear |
| **Remove duplicate accounts** | `O(N log N)` | ✅ Sorting-based |
| **Final count** | `O(1)` | ✅ Constant |

**Overall Complexity:** `O(N log N)` (due to sorting), which is optimal for this problem. 🚀

## 🏗 **Project Structure**
```
2020. Number of Accounts That Did Not Stream/
├── no_stream.py    # Python solution
├── README.md       # Detailed problem explanation
```

🚀 **This solution efficiently identifies accounts that subscribed in 2021 but never streamed!** 📊