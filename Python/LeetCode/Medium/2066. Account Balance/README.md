# 💰 **LeetCode 2066: Account Balance**  

## 📌 **Problem Overview**  
We need to compute the **balance** of each account **after every transaction**. The dataset contains financial transactions, where each entry records:  
- The **account ID** (`account_id`).  
- The **transaction date** (`day`).  
- The **transaction type** (`Deposit` or `Withdraw`).  
- The **amount** of the transaction.  

### **Goal**  
For each transaction, maintain a **running balance** for each account, ensuring:  
1. **Deposits** increase the balance.  
2. **Withdrawals** decrease the balance.  
3. The balance is always **≥ 0**.  
4. The result is **sorted by** `account_id`, and within each account, by `day` in ascending order.  

## 🛠 **Database Schema**  

### **Transactions Table**  
| Column Name  | Type    | Description |
|-------------|--------|-------------|
| `account_id` | int | Unique account identifier |
| `day` | date | Date of the transaction |
| `type` | ENUM | Either `"Deposit"` or `"Withdraw"` |
| `amount` | int | Amount of the transaction |

## 🚀 **Python Solution**  

```python
import pandas as pd
import numpy as np


def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the balance of each account after each transaction.

    Given a transactions table, this function processes deposits and withdrawals,
    keeping track of the cumulative balance for each account in chronological order.

    Args:
        transactions (pd.DataFrame): A DataFrame containing transaction details:
            - "account_id" (int): Unique identifier for each account.
            - "day" (datetime): Date of the transaction.
            - "type" (str): Transaction type ("Deposit" or "Withdraw").
            - "amount" (int): Transaction amount.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - "account_id" (int): The account ID.
            - "day" (datetime): The date of the transaction.
            - "balance" (int): The running balance after each transaction.
    """

    return (
        transactions
        .sort_values(by=["account_id", "day"])                                                      # Sort by account ID and date
        .assign(
            amount=lambda x: np.where(x["type"] == "Withdraw", -x["amount"], x["amount"]),          # Convert withdrawals to negative
            balance=lambda x: x.groupby("account_id")["amount"].cumsum()                            # Compute cumulative sum per account
        )
        [["account_id", "day", "balance"]]                                                          # Select the required columns
    )
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Transactions Table**  
| account_id | day        | type     | amount |
|------------|------------|---------|--------|
| 1          | 2021-11-07 | Deposit | 2000   |
| 1          | 2021-11-09 | Withdraw | 1000  |
| 1          | 2021-11-11 | Deposit | 1000   |
| 2          | 2021-12-07 | Deposit | 7000   |
| 2          | 2021-12-12 | Withdraw | 7000  |

### **Expected Output**  

| account_id | day        | balance |
|------------|------------|---------|
| 1          | 2021-11-07 | 2000    |
| 1          | 2021-11-09 | 1000    |
| 1          | 2021-11-11 | 2000    |
| 2          | 2021-12-07 | 7000    |
| 2          | 2021-12-12 | 0       |

### **Explanation**  
- **Account 1:**  
  - Deposits **2000** → Balance = **2000**  
  - Withdraws **1000** → Balance = **1000**  
  - Deposits **1000** → Balance = **2000**  

- **Account 2:**  
  - Deposits **7000** → Balance = **7000**  
  - Withdraws **7000** → Balance = **0**  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values(by=["account_id", "day"])` | **O(N log N)** |
| Updating Amounts | `np.where()` | **O(N)** |
| Grouping & Cumulative Sum | `groupby().cumsum()` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
2066. Account Balance/
├── account_balance.py    # Python implementation of the solution
├── README.md             # Detailed explanation & walkthrough
```

## 🎯 **Key Takeaways**
✔ **Sorting ensures transactions are processed in order.**  
✔ **Withdrawals are converted to negative values using `np.where()`.**  
✔ **Balances are tracked efficiently using `groupby().cumsum()`.**  
✔ **Final output preserves `account_id` order and chronological transactions.**  

This solution is optimised for **real-time financial tracking** in banking systems, ensuring **accuracy and efficiency**. 🚀