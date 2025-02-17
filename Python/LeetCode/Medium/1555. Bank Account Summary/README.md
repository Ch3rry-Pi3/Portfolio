# 🏦 **LeetCode 1555: Bank Account Summary**  

## 📌 **Problem Overview**  
You are given two tables:  

1. **`Users` Table**: Contains user details, including their **initial credit balance**.  
2. **`Transactions` Table**: Records transactions where one user **sends money** to another user.  

Each transaction affects the credit balance of both the sender (`paid_by`) and the receiver (`paid_to`).  

### **Goal**  
For each user, compute the **final credit balance** after all transactions and determine if their **credit limit is breached**.  
- A **breach** occurs when a user's credit balance falls **below zero**.  
- Return the result with the columns:
  - `user_id`: Unique identifier for the user.  
  - `user_name`: Name of the user.  
  - `credit`: Final credit balance after transactions.  
  - `credit_limit_breached`: `"Yes"` if credit < 0, otherwise `"No"`.  

The result table can be **returned in any order**.

## 📊 **Database Schema**  

### **Users Table**  
| Column Name | Type  | Description |
|-------------|-------|-------------|
| `user_id`   | int   | Unique identifier for the user. |
| `user_name` | varchar | Name of the user. |
| `credit`    | int   | Initial credit balance of the user. |

### **Transactions Table**  
| Column Name   | Type  | Description |
|--------------|-------|-------------|
| `trans_id`   | int   | Unique transaction ID. |
| `paid_by`    | int   | ID of the user who sent the money. |
| `paid_to`    | int   | ID of the user who received the money. |
| `amount`     | int   | Amount transferred in the transaction. |
| `transacted_on` | date  | Date of the transaction. |

---

## 🛠 **Approach**  

1. **Compute the Total Received and Spent per User**  
   - Group transactions by `paid_to` to calculate **total received** by each user.  
   - Group transactions by `paid_by` to calculate **total spent** by each user.  

2. **Merge with the Users Table**  
   - Join the **received** and **spent** amounts with the `Users` table.  

3. **Calculate Final Credit Balance**  
   - **Formula**:  

     \[
     \text{Final Credit} = \text{Initial Credit} + \text{Total Received} - \text{Total Spent}
     \]

4. **Determine Credit Limit Breach**  
   - If **Final Credit < 0**, mark `"Yes"` in `credit_limit_breached`, otherwise `"No"`.  

5. **Return Required Columns**  
   - Remove unnecessary columns and format the output correctly.

## 🚀 **Python Solution**  

```python
import pandas as pd
import numpy as np

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the final credit balance for each user after transactions
    and determines if the credit limit is breached.

    Args:
        users (pd.DataFrame): Contains user details with columns:
            - "user_id" (int): Unique user ID.
            - "user_name" (str): Name of the user.
            - "credit" (int): Initial credit balance.
        transactions (pd.DataFrame): Contains transaction details with columns:
            - "trans_id" (int): Unique transaction ID.
            - "paid_by" (int): User ID who sent the money.
            - "paid_to" (int): User ID who received the money.
            - "amount" (int): Transaction amount.
            - "transacted_on" (date): Date of transaction.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "user_id": User ID.
            - "user_name": User name.
            - "credit": Updated credit balance.
            - "credit_limit_breached": "Yes" if credit < 0, otherwise "No".
    """

    # Compute total received by each user
    received_amount = transactions.groupby("paid_to", as_index=False).agg(add=("amount", "sum"))

    # Compute total spent by each user
    spent_amount = transactions.groupby("paid_by", as_index=False).agg(sub=("amount", "sum"))

    # Merge transactions with users and update balances
    final_balance = (
        users
        .merge(received_amount, left_on="user_id", right_on="paid_to", how="left")
        .merge(spent_amount, left_on="user_id", right_on="paid_by", how="left")
        .fillna(value={"add": 0, "sub": 0})  # Fill missing values with 0
        .assign(credit=lambda x: x["credit"] + x["add"] - x["sub"])  # Update credit balance
        .assign(credit_limit_breached=lambda x: np.where(x["credit"] < 0, "Yes", "No"))  # Breach check
        .drop(columns=["paid_to", "paid_by", "add", "sub"])  # Remove unnecessary columns
    )

    return final_balance
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Users Table**  
| user_id | user_name | credit |
|---------|----------|--------|
| 1       | Moustafa | 100    |
| 2       | Jonathan | 200    |
| 3       | Winston  | 10000  |
| 4       | Luis     | 800    |

#### **Transactions Table**  
| trans_id | paid_by | paid_to | amount | transacted_on |
|----------|--------|--------|--------|--------------|
| 1        | 1      | 3      | 400    | 2020-08-01  |
| 2        | 3      | 2      | 500    | 2020-08-02  |
| 3        | 1      | 1      | 200    | 2020-08-03  |

### **Output**  
```python
   user_id   user_name  credit credit_limit_breached
0        1  Moustafa    -100                 Yes
1        2  Jonathan     500                  No
2        3  Winston     9900                  No
3        4  Luis        800                   No
```

### **Explanation**  
- **Moustafa (ID 1)**  
  - Initial credit = **100**  
  - Sent **$400** to Winston (ID 3).  
  - Received **$200** from himself (irrelevant).  
  - Final balance = `100 - 400 + 200 = -100` → `"Yes"` (breached).  

- **Jonathan (ID 2)**  
  - Initial credit = **200**  
  - Received **$500** from Winston.  
  - Final balance = `200 + 500 = 500` → `"No"`.  

- **Winston (ID 3)**  
  - Initial credit = **10,000**  
  - Received **$400** from Moustafa.  
  - Sent **$500** to Jonathan.  
  - Final balance = `10,000 + 400 - 500 = 9900` → `"No"`.  

- **Luis (ID 4)**  
  - No transactions.  
  - Credit remains **800** → `"No"`.  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|----------|----------------|
| Compute received/spent transactions | `groupby()` | **O(N)** |
| Merge transactions with users | `merge()` | **O(N)** |
| Update credit balance | `assign()` | **O(N)** |
| Check credit breach | `np.where()` | **O(N)** |
| **Total Complexity** | **O(N)** ✅ |  

## 🎯 **Why This Approach?**  
✔ **Optimised with `groupby()` for efficient aggregations.**  
✔ **Avoids loops and uses Pandas vectorised operations.**  
✔ **Efficiently merges transactions and users to compute balances.**  

🚀 **With this approach, you can track user credit changes efficiently for any transaction dataset!** 🎯