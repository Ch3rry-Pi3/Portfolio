# 🏦 **LeetCode 1843: Suspicious Bank Accounts**  

## 📌 **Problem Overview**  
A bank account is considered **suspicious** if the total monthly income exceeds its **max_income** for **two or more consecutive months**.  

### **Key Requirements:**  
- The **total income** for a month is **the sum of all 'Creditor' transactions** (deposits).  
- If an account exceeds its **max_income** for **two consecutive months**, it is marked as **suspicious**.  
- The result should contain the **account IDs** of all suspicious accounts **sorted in ascending order**.

## 🖼 **Example**  
### **Input: Accounts Table**
```
+------------+------------+
| account_id | max_income |
+------------+------------+
|     3      |   21000    |
|     4      |   10400    |
+------------+------------+
```

### **Input: Transactions Table**
```
+---------------+------------+----------+--------+------------+
| transaction_id | account_id |  type   | amount |    day    |
+---------------+------------+----------+--------+------------+
|       2       |     3      | Creditor | 107100 | 2021-06-02 |
|       1       |     4      | Creditor | 10400  | 2021-06-07 |
|       4       |     4      | Creditor | 49300  | 2021-05-03 |
|       5       |     4      | Creditor | 75500  | 2021-06-15 |
|       6       |     4      | Debtor   | 75500  | 2021-06-15 |
|       7       |     3      | Creditor | 90900  | 2021-06-14 |
|       3       |     3      | Debtor   | 56300  | 2021-07-05 |
|       8       |     4      | Creditor | 64900  | 2021-07-26 |
|       9       |     3      | Creditor | 102100 | 2021-06-22 |
+---------------+------------+----------+--------+------------+
```

### **Output:**
```
+------------+
| account_id |
+------------+
|     3      |
+------------+
```

✅ **Explanation:**  
1. **For Account 3 (`account_id = 3`)**:  
   - **June 2021**: `107100 + 102100 + 90900 = 300100` (exceeds `21000`) ✅  
   - **July 2021**: `64900` (exceeds `21000`) ✅  
   - Since this occurred **for two consecutive months**, **account 3 is suspicious**.

2. **For Account 4 (`account_id = 4`)**:  
   - **May 2021**: `49300` (exceeds `10400`) ✅  
   - **June 2021**: `10400` (does not exceed `10400`) ❌  
   - **July 2021**: `56300` (exceeds `10400`) ✅  
   - Since the **exceedance was not consecutive**, **account 4 is NOT included**.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Aggregate Monthly Income & Identify Consecutive Violations**
1. **Filter 'Creditor' transactions** to **compute deposits** per month.  
2. **Group by `account_id` and month**, summing up deposit amounts.  
3. **Merge with the `accounts` table** to retrieve `max_income`.  
4. **Filter months where income exceeds `max_income`**.  
5. **Detect consecutive violations** (i.e., exceeding `max_income` for at least **two consecutive months**).  
6. **Return the list of suspicious accounts, sorted in ascending order**.

## 📝 **Implementation**  

```python
# suspicious_bank_accounts.py

import pandas as pd

def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies suspicious bank accounts where the total monthly income exceeds the 
    max_income for two or more consecutive months.

    Args:
        accounts (pd.DataFrame): Contains account data with columns:
            - "account_id" (int): Unique account identifier.
            - "max_income" (int): The maximum allowable monthly income for the account.

        transactions (pd.DataFrame): Contains transaction data with columns:
            - "transaction_id" (int): Unique transaction identifier.
            - "account_id" (int): The ID of the account associated with the transaction.
            - "type" (str): The type of transaction ('Creditor' for deposit, 'Debtor' for withdrawal).
            - "amount" (int): The transaction amount.
            - "day" (datetime): The date of the transaction.

    Returns:
        pd.DataFrame: A table containing:
            - "account_id" (int): The IDs of suspicious accounts.
        
        The result is sorted in ascending order.
    """

    # Convert 'day' column to represent the month (YYYY-MM format)
    transactions = transactions.assign(day=transactions["day"].dt.month)

    # Filter only 'Creditor' transactions (deposits)
    transactions = transactions[transactions["type"] == "Creditor"]

    # Aggregate monthly income per account
    monthly_income = (
        transactions.groupby(["account_id", "day"])
        .agg(amount=("amount", "sum"))
        .reset_index()
    )

    # Merge with the accounts table to get max_income for each account
    df = monthly_income.merge(accounts, how="left", on="account_id")

    # Filter rows where the monthly income exceeds the max_income
    df = df[df["amount"] > df["max_income"]]

    # Compute the difference between consecutive months per account
    df = df.assign(diff=df.groupby("account_id")["day"].diff())

    # Identify accounts where there are at least two consecutive months exceeding max_income
    suspicious_accounts = df[df["diff"] == 1][["account_id"]].drop_duplicates()

    # Return sorted results as required
    return suspicious_accounts.sort_values(by="account_id", ascending=True)

```

## ⏳ **Time Complexity Analysis**  

| Operation                                | Complexity |
|------------------------------------------|------------|
| Filtering creditor transactions          | **O(N)** |
| Grouping and summing monthly deposits    | **O(N log N)** |
| Merging with `accounts` data             | **O(N)** |
| Filtering months exceeding `max_income`  | **O(N)** |
| Identifying consecutive violations       | **O(N)** |
| Sorting the results                      | **O(N log N)** |
| **Overall Complexity**                    | **O(N log N)** ✅ |

> **N = number of transactions in the dataset**  

## 📂 **Project Structure**  

```
1843. Suspicious Bank Accounts/
├── suspicious_bank_accounts.py  # Python solution
├── README.md                    # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Efficient Pandas operations** for aggregation and filtering.  
✔ **Handles large-scale banking data efficiently**.  
✔ **Demonstrates financial fraud detection logic**.  

🚀 **Mastering transaction analysis is key for financial security!** 🔥