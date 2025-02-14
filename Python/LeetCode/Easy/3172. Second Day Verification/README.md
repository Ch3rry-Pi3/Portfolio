# 📩 **LeetCode 3172: Second Day Verification**

## 📌 **Problem Overview**
We have two tables:
1. **Emails Table**: Contains records of user sign-ups.
2. **Texts Table**: Contains verification records.

A **user is considered verified on the second day** if:
- They signed up on **Day X**.
- They verified their sign-up on **Day X + 1**.

### 📜 **Objective**
Write a function that **finds all users who verified their sign-up exactly on the second day** and returns their `user_id` sorted in **ascending order**.

## 🛠 **Approach**
We solve this problem using **Pandas DataFrame operations**:
1. **Filter Verified Users**  
   - Keep only rows in the `texts` table where `signup_action == 'Verified'`.
  
2. **Compute Expected Sign-Up Date**  
   - For each verification date (`action_date`), compute **one day before** (`action_date - 1`).

3. **Align with Emails Table**  
   - Convert `signup_date` to date format.
   - Merge `emails` and `texts` tables on `email_id` and the **expected sign-up date**.

4. **Extract and Sort User IDs**  
   - Select only `user_id` from the merged result.
   - Remove duplicates and sort in **ascending order**.

This approach ensures an **efficient O(N) solution** using Pandas vectorised operations.

## 🚀 **Python Solution**
```python
import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    """
    Finds users who verified their sign-up on the second day after registering.

    Args:
        emails (pd.DataFrame): DataFrame containing email sign-up records with columns ['email_id', 'user_id', 'signup_date'].
        texts (pd.DataFrame): DataFrame containing text verification records with columns ['text_id', 'email_id', 'signup_action', 'action_date'].

    Returns:
        pd.DataFrame: A DataFrame containing unique user IDs who verified on the second day after signing up, sorted in ascending order.
    """

    # Filter only verified sign-up actions
    verified_texts = texts[texts['signup_action'] == 'Verified'].copy()

    # Compute the expected sign-up date as one day before the verification date
    verified_texts['signup_dt'] = (pd.to_datetime(verified_texts['action_date']) - pd.Timedelta(days=1)).dt.floor('d')

    # Convert the signup_date in emails to datetime and floor it to date
    emails['signup_dt'] = emails['signup_date'].dt.floor('d')

    # Merge on email_id and expected signup date
    merged_df = emails.merge(verified_texts, on=['email_id', 'signup_dt'], how='inner')

    # Return unique user_ids sorted in ascending order
    return merged_df[['user_id']].drop_duplicates().sort_values(by='user_id')
```

## 📌 **Example Walkthrough**

### **Example 1**
#### **Input:**
#### 📩 **Emails Table**
| email_id | user_id | signup_date       |
|----------|--------|------------------|
| 125      | 7771   | 2022-06-14 09:30 |
| 433      | 1052   | 2022-07-09 08:15 |
| 234      | 7005   | 2022-08-20 10:00 |

#### 💬 **Texts Table**
| text_id | email_id | signup_action | action_date        |
|---------|---------|---------------|-------------------|
| 1       | 125     | Verified      | 2022-06-15 08:30 |
| 2       | 433     | Not Verified  | 2022-07-10 10:45 |
| 4       | 234     | Verified      | 2022-08-21 09:30 |

#### **Output:**
| user_id |
|---------|
| 7005    |
| 7771    |

#### **Explanation:**
✔ **User 7771** signed up on **2022-06-14** and verified on **2022-06-15** (second day).  
✔ **User 7005** signed up on **2022-08-20** and verified on **2022-08-21** (second day).  
❌ **User 1052** didn't verify, so they are excluded.  

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter verified users | `texts[texts['signup_action'] == 'Verified']` | **O(N)** |
| Compute expected signup date | `pd.Timedelta(days=1)` | **O(N)** |
| Convert signup date to floor date | `.dt.floor('d')` | **O(N)** |
| Merge DataFrames | `emails.merge(texts, on=['email_id', 'signup_dt'])` | **O(N)** |
| Sort & drop duplicates | `.drop_duplicates().sort_values(by='user_id')` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** |

This ensures an **efficient vectorised approach** using Pandas!

## 🎯 **Why This Approach?**
✔ **Vectorised operations** (Pandas) → Faster than loops  
✔ **Single merge operation** → Efficient matching  
✔ **Sorting only at the end** → Minimises unnecessary computations  
✔ **Handles edge cases** (users with no verification, verification delays, etc.)  

🔹 **This approach is scalable and performant for large datasets!** 🚀

## 🏆 **Alternative Approaches**
| Approach | Complexity | Notes |
|----------|------------|-------|
| **Loop through each user** | **O(N²)** | Inefficient for large datasets |
| **SQL-style JOINs** | **O(N log N)** | Similar efficiency, but needs SQL |
| **Apply row-wise operations** | **O(N)** | Slower than vectorised Pandas |

Our approach **strikes a balance** between simplicity and efficiency using Pandas operations.

## 📝 **Edge Cases Considered**
✅ Users signing up but **never verifying**  
✅ Users verifying **after two or more days**  
✅ Multiple users signing up on the **same day**  
✅ Large datasets with **thousands of records**  

## 🏁 **How to Run**
To test the solution, use the `main()` function in **`second_day_verification.py`**:
```python
if __name__ == "__main__":
    main()
```
This executes the function with **sample data** to validate the implementation.

## 💡 **Final Thoughts**
🔹 This problem is a **real-world use case** in **email verification tracking**.  
🔹 The **Pandas-based approach** ensures **clean, efficient** computation.  
🔹 This solution can be **extended** for other verification windows (e.g., 3rd-day, 1-week verifications).  

✅ **With this, we efficiently track users who verify on the second day!** 🎯🚀

