# 📊 **LeetCode 1205: Monthly Transactions II**  

## 📌 **Problem Overview**  
You are given two tables:  
1. **Transactions**: Contains transaction records, including transaction ID, country, state (approved/declined), amount, and transaction date.  
2. **Chargebacks**: Contains chargeback transactions associated with transactions in the **Transactions** table.  

### **Goal**  
For each **month and country**, compute:  
- The number of **approved transactions** and their total amount.  
- The number of **chargebacks** and their total amount.  

🔹 **Ignore rows where all values are zero** in the final output.  

## 📊 **Database Schema**  

### **Transactions Table**  
| Column Name  | Type    | Description |
|-------------|--------|-------------|
| `id`        | int    | Unique transaction ID |
| `country`   | varchar | Country where the transaction occurred |
| `state`     | enum   | `"approved"` or `"declined"` |
| `amount`    | int    | Transaction amount |
| `trans_date` | date   | Date of the transaction |

### **Chargebacks Table**  
| Column Name  | Type    | Description |
|-------------|--------|-------------|
| `trans_id`  | int    | Foreign key referencing transaction ID |
| `trans_date` | date   | Date of the chargeback |

## 🛠 **Approach**  

1. **Merge transactions with chargebacks**  
   - Use a **left join** on `transactions.id = chargebacks.trans_id` to align chargebacks with their corresponding transactions.  

2. **Extract the month**  
   - Convert `trans_date` to a **"YYYY-MM"** format for both transactions and chargebacks.  

3. **Compute Approved Transactions**  
   - Filter transactions with `"approved"` state.  
   - Group by `month` and `country`.  
   - Compute **count** of approved transactions and **sum** of approved amounts.  

4. **Compute Chargebacks**  
   - Group by `month` and `country`.  
   - Compute **count** of chargebacks and **sum** of chargeback amounts.  

5. **Merge Results**  
   - Combine approved transactions and chargebacks into one table.  
   - Fill missing values with `0`.  

## 🚀 **Python Solution**  

```python
import pandas as pd


def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the monthly transaction summary for each country.

    This function calculates the number of approved transactions, their total amount,
    and the number and total amount of chargebacks for each month and country.

    Args:
        transactions (pd.DataFrame): DataFrame containing transaction details with columns:
            - "id" (int): Unique transaction ID.
            - "country" (str): Country where the transaction occurred.
            - "state" (str): Transaction state ("approved" or "declined").
            - "amount" (int): Transaction amount.
            - "trans_date" (datetime): Transaction date.
        
        chargebacks (pd.DataFrame): DataFrame containing chargeback details with columns:
            - "trans_id" (int): Reference to transaction ID.
            - "trans_date" (datetime): Chargeback transaction date.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - "month" (str): Year-Month in "YYYY-MM" format.
            - "country" (str): Country where the transaction occurred.
            - "approved_count" (int): Count of approved transactions.
            - "approved_amount" (int): Sum of approved transaction amounts.
            - "chargeback_count" (int): Count of chargebacks.
            - "chargeback_amount" (int): Sum of chargeback amounts.
    """
    # Merge transactions with chargebacks to align data
    df = transactions.merge(chargebacks, left_on="id", right_on="trans_id", how="left")

    # Extract month from transaction and chargeback dates
    df["month_transaction"] = df["trans_date_x"].dt.strftime("%Y-%m")
    df["month_chargeback"] = df["trans_date_y"].dt.strftime("%Y-%m")

    # Compute approved transactions per month and country
    df1 = (
        df[df["state"] == "approved"]
        .groupby(["month_transaction", "country"], as_index=False)
        .agg(
            approved_count=("amount", "count"),
            approved_amount=("amount", "sum"),
        )
        .rename(columns={"month_transaction": "month"})
    )

    # Compute chargebacks per month and country
    df2 = (
        df.groupby(["month_chargeback", "country"], as_index=False)
        .agg(
            chargeback_count=("amount", "count"),
            chargeback_amount=("amount", "sum"),
        )
        .rename(columns={"month_chargeback": "month"})
    )

    # Merge both tables and fill missing values with zero
    df3 = df1.merge(df2, how="outer", on=["month", "country"]).fillna(0)

    return df3
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Transactions Table**  
| id  | country | state    | amount | trans_date |
|-----|---------|----------|--------|------------|
| 101 | US      | approved | 1000   | 2019-05-18 |
| 102 | US      | declined | 2000   | 2019-05-19 |
| 103 | US      | approved | 3000   | 2019-06-10 |
| 104 | US      | declined | 4000   | 2019-06-13 |
| 105 | US      | approved | 5000   | 2019-06-15 |

#### **Chargebacks Table**  
| trans_id | trans_date |
|----------|------------|
| 102      | 2019-05-29 |
| 101      | 2019-06-30 |
| 105      | 2019-09-18 |

### **Output**  
```python
   month country  approved_count  approved_amount  chargeback_count  chargeback_amount
0  2019-05      US               1            1000                1              2000
1  2019-06      US               2            8000                1              1000
2  2019-09      US               0               0                1              5000
```

### **Explanation**  
- **May 2019**:  
  - 1 **approved transaction** (`1000`).  
  - 1 **chargeback** (`2000`).  
- **June 2019**:  
  - 2 **approved transactions** (`3000 + 5000 = 8000`).  
  - 1 **chargeback** (`1000`).  
- **September 2019**:  
  - No approved transactions.  
  - 1 chargeback (`5000`).  

### ✅ **Complexity Analysis**  
| Step  | Complexity |
|--------|------------|
| Merging Transactions & Chargebacks | **O(N)** |
| Grouping & Aggregation | **O(N log N)** |
| Final Merge & Cleanup | **O(N)** |

🚀 **Efficiently computes monthly summaries for approved transactions and chargebacks.**