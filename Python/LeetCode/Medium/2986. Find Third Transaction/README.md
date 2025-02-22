# 💳 **LeetCode 2986: Find Third Transaction**  

## 📌 **Problem Overview**  
Given a table of user transactions, identify the **third transaction** (if it exists) for each user, where:  
- The **spending on the preceding two transactions** is **lower** than the spending on the third transaction.
- The transactions must be considered **in chronological order**.
- The result should be **sorted by `user_id` in ascending order**.

## 🖼 **Example**  
### **Input: Transactions Table**
```
+---------+--------+---------------------+
| user_id | spend  | transaction_date    |
+---------+--------+---------------------+
|    1    | 65.56  | 2023-11-18 13:49:42 |
|    1    | 96.00  | 2023-11-30 08:47:26 |
|    1    | 49.78  | 2023-11-12 08:47:26 |
|    1    | 100.4  | 2023-11-11 06:39:34 |
|    1    | 37.43  | 2023-11-06 02:11:34 |
|    1    | 18.38  | 2023-11-02 23:56:34 |
|    3    | 100.4  | 2023-11-11 06:39:34 |
|    3    | 37.43  | 2023-11-06 02:11:34 |
|    3    | 18.38  | 2023-11-02 23:56:34 |
+---------+--------+---------------------+
```

### **Output:**
```
+---------+-----------------------+---------------------+
| user_id | third_transaction_spend | third_transaction_date |
+---------+-----------------------+---------------------+
|    1    | 65.56                 | 2023-11-18 13:49:42 |
+---------+-----------------------+---------------------+
```

✅ **Explanation:**  
1. **User 1 Transactions in Order:**
   - `18.38` → `37.43` → **`65.56` (third transaction, higher than previous two)**
   - The third transaction qualifies because:
     - `65.56 > 37.43`
     - `65.56 > 18.38`
2. **User 3:**  
   - `18.38 → 37.43 → 100.4`
   - The third transaction **(100.4)** **does not qualify**, since the first two transactions are not both lower than the third.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Chronologically Track the First Three Transactions**
1. **Sort transactions** by `user_id` and `transaction_date` to maintain order.
2. **Group by `user_id`** and **keep only the first three transactions**.
3. **Filter users** where:
   - The **third transaction** has a **higher `spend`** than both the **first** and **second transactions**.
4. **Rename columns** and **sort results by `user_id` in ascending order**.

## 📝 **Implementation**  

```python
# third_transaction.py

import pandas as pd

def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the third transaction for each user where the previous two transactions had lower spending.

    Args:
        transactions (pd.DataFrame): Contains transaction data with columns:
            - "user_id" (int): The ID of the user making the transaction.
            - "spend" (decimal): The amount spent in the transaction.
            - "transaction_date" (datetime): The date and time of the transaction.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The ID of the user.
            - "third_transaction_spend" (decimal): The spend amount of the third qualifying transaction.
            - "third_transaction_date" (datetime): The date of the third qualifying transaction.
        
        The result is sorted by "user_id" in ascending order.
    """
    # Sort transactions by user_id and transaction_date
    df = transactions.sort_values(["user_id", "transaction_date"])

    # Select only the first three transactions per user
    df = df.groupby("user_id").head(3)

    # Filter for third transactions where both previous transactions had lower spending
    df = df[
        (df["spend"] > df.shift(1)["spend"]) & (df["user_id"] == df.shift(1)["user_id"]) &
        (df["spend"] > df.shift(2)["spend"]) & (df["user_id"] == df.shift(2)["user_id"])
    ]

    # Rename columns and return only necessary fields
    return (
        df.rename(columns={"spend": "third_transaction_spend", "transaction_date": "third_transaction_date"})
        [["user_id", "third_transaction_spend", "third_transaction_date"]]
        .sort_values("user_id")
    )

```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Sorting transactions                  | **O(N log N)** |
| Grouping and filtering transactions   | **O(N)** |
| Filtering valid third transactions    | **O(N)** |
| Sorting final output                  | **O(N log N)** |
| **Overall Complexity**                 | **O(N log N)** ✅ |

> **N = number of transactions in the dataset**  

## 📂 **Project Structure**  

```
2986. Find Third Transaction/
├── third_transaction.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Sorting ensures transactions are processed in order.**  
✔ **Grouping helps isolate the first three transactions per user efficiently.**  
✔ **Shift operations allow easy comparison of past transactions.**  
✔ **Efficient approach using Pandas filtering and ranking techniques.**  

🚀 **Mastering sequential transaction filtering is crucial for financial and behavioral analytics!** 🔥