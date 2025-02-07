# 📞 **LeetCode 1972: First and Last Call on the Same Day**

## 📌 **Overview**
This project solves **LeetCode Problem 1972: First and Last Call on the Same Day**.  
The goal is to **identify users whose first and last calls on any given day were with the same person**.  

### **Problem Statement**
Each row in the dataset represents a **phone call** between two users. Calls are stored as `(caller_id, recipient_id, call_time)`, and each combination is **unique**.

#### **Rules:**
- A **user must have made their first and last call of a day with the same person**.
- Calls **are counted bidirectionally**, meaning if `A` calls `B`, it is equivalent to `B` calling `A`.
- Return **the list of user IDs** who meet the condition.

## 🎯 **Example Walkthrough**
### **Example Input**
```python
Input:
caller_id  recipient_id    call_time
8          4              2021-08-24 17:46:07
8          4              2021-08-24 19:57:13
8          4              2021-08-11 05:28:14
5          3              2021-08-17 04:04:15
5          3              2021-08-17 13:07:00
11         3              2021-08-11 13:07:00
8          11             2021-08-17 22:22:22
```

### **Step-by-Step Breakdown**
1️⃣ **Extract the call date (YYYY-MM-DD)** from `call_time` to **group by day**.  
2️⃣ **Find the first and last call per user per day.**  
   - **Example:** On `2021-08-24`, `user 8` had calls **only with `user 4`** → ✅  
3️⃣ **Ensure both calls involved the same person.**  
4️⃣ **Return unique user IDs.**

### **Expected Output**
```python
Output:
user_id
8
4
5
```

## 🧠 **Intuition Behind the Approach**
### **Key Observations**
✔ **Calls are bidirectional**, meaning `(A, B)` is the same as `(B, A)`.  
✔ **We must track first and last calls per day** for each user.  
✔ **Sorting calls by time helps find first and last calls efficiently**.  

---

## 📝 **Step-by-Step Approach**
### **1️⃣ Create a Bidirectional Call Table**
- Duplicate the dataset, swapping `caller_id` and `recipient_id` to **count calls from both perspectives**.

### **2️⃣ Extract Call Dates**
- Convert `call_time` into a **date-only column** (`YYYY-MM-DD`).

### **3️⃣ Find First & Last Calls for Each User Per Day**
- Compute **earliest (`min_time`)** and **latest (`max_time`)** calls per user per day.

### **4️⃣ Identify Users Who Meet the Criteria**
- Extract users whose **first and last calls were with the same person**.
- Remove duplicates.

## **💡 Implementation**
```python
import pandas as pd

def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies users whose first and last calls on any given day were with the same person.

    Calls are counted regardless of whether the user is the caller or the recipient.

    :param calls: DataFrame containing 'caller_id', 'recipient_id', and 'call_time' columns.
    :return: DataFrame with a single column 'user_id' listing the relevant users.
    """

    # Duplicate the dataset by swapping 'caller_id' and 'recipient_id' to create bidirectional call records
    df_call = pd.concat([calls, calls.rename(columns={'recipient_id': 'caller_id', 'caller_id': 'recipient_id'})])

    # Extract the call date (YYYY-MM-DD) from 'call_time' for daily grouping
    df_call['day'] = df_call['call_time'].dt.strftime('%Y-%m-%d')

    # Compute the first (earliest) and last (latest) call times per user per day
    df_call = df_call.assign(
        max_time=df_call.groupby(['day', 'caller_id'])['call_time'].transform('max'),
        min_time=df_call.groupby(['day', 'caller_id'])['call_time'].transform('min')
    )

    # Identify the last call per user per day
    df_max = df_call.loc[df_call['call_time'] == df_call['max_time'], ['caller_id', 'recipient_id', 'day']]

    # Identify the first call per user per day
    df_min = df_call.loc[df_call['call_time'] == df_call['min_time'], ['caller_id', 'recipient_id', 'day']]

    # Find users whose first and last calls were with the same recipient on the same day
    df_result = pd.merge(df_max, df_min, how='inner', on=['caller_id', 'recipient_id', 'day'])[['caller_id']]

    # Remove duplicates and rename the column for final output
    df_result = df_result.drop_duplicates().rename(columns={'caller_id': 'user_id'})

    return df_result
```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Grouping & Filtering (`O(n)`)** | **O(n log n)** ✅ | **O(n)** ✅ |

- **Sorting calls by time (`O(n log n)`)** helps efficiently extract first and last calls.
- **Storing results in a DataFrame (`O(n)`)** ensures efficient lookups.

## 🏗 **Project Structure**
```
1972. First and Last Call/
├── first_and_last_call.py   # Python implementation of the solution
├── README.md                # Detailed explanation & walkthrough
```

✨ **Master call data processing with this efficient `O(n log n)` approach!** 🚀  