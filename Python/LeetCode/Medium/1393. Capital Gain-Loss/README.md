# 📊 **LeetCode 1393: Capital Gain/Loss**  

## 📌 **Problem Overview**  
You are given a **`Stocks`** table that records stock transactions, where each row represents:  
- A **stock name** (`stock_name`).  
- An **operation** (`Buy` or `Sell`).  
- The **day** (`operation_day`) on which the transaction took place.  
- The **price** at which the stock was bought or sold.  

Each stock is **bought before it is sold**, and every `Buy` has a corresponding `Sell` transaction.

### **Goal**  
Calculate the **Capital Gain/Loss** for each stock by summing the profit (or loss) from each **Buy-Sell** transaction.  
- Buying a stock results in **negative capital** (`-price`).  
- Selling a stock results in **positive capital** (`+price`).  
- The **final capital gain/loss** is computed as the sum of all transactions for each stock.

## 📊 **Database Schema**  

### **Stocks Table**  
| Column Name     | Type    | Description |
|----------------|--------|-------------|
| `stock_name`   | varchar | Name of the stock |
| `operation`    | ENUM | Either `"Buy"` or `"Sell"` |
| `operation_day` | int | The day of the transaction |
| `price`        | int | Price of the stock transaction |

## 🛠 **Approach**  

1. **Sort the data**  
   - By `stock_name` (to ensure all transactions for each stock are together).  
   - By `operation_day` (to process transactions in the correct order).  

2. **Convert Buy Prices to Negative**  
   - Use `np.where()` to assign **negative values** for `Buy` operations and keep `Sell` prices as they are.  

3. **Compute the Capital Gain/Loss**  
   - Group by `stock_name` and sum up the adjusted prices.  

## 🚀 **Python Solution**  

```python
import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the capital gain or loss for each stock based on buy and sell transactions.

    Args:
        stocks (pd.DataFrame): A DataFrame containing stock transaction details with columns:
                               - "stock_name" (str): Name of the stock.
                               - "operation" (str): "Buy" or "Sell".
                               - "operation_day" (int): Day of the transaction.
                               - "price" (int): Price of the transaction.

    Returns:
        pd.DataFrame: A DataFrame with columns:
                      - "stock_name" (str): Name of the stock.
                      - "capital_gain_loss" (int): Net gain or loss after transactions.
    """
    return (
        stocks
        .sort_values(by=["stock_name", "operation_day"])                                            # Sort transactions for correct order
        .assign(price=lambda x: np.where(x["operation"] == "Buy", -x["price"], x["price"]))         # Convert "Buy" to negative
        .groupby("stock_name", as_index=False)                                                      # Group by stock
        .agg(capital_gain_loss=("price", "sum"))                                                    # Sum up gains and losses
    )

```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Stocks Table**  
| stock_name    | operation | operation_day | price  |
|--------------|----------|--------------|-------|
| Leetcode     | Buy      | 1            | 1000  |
| Corona Masks | Buy      | 2            | 10    |
| Leetcode     | Sell     | 5            | 9000  |
| Handbags     | Buy      | 17           | 30000 |
| Corona Masks | Sell     | 3            | 1010  |
| Corona Masks | Buy      | 4            | 1000  |
| Corona Masks | Sell     | 5            | 500   |
| Handbags     | Sell     | 29           | 7000  |
| Handbags     | Sell     | 10           | 10000 |

### **Output**  
```python
   stock_name   capital_gain_loss
0  Corona Masks             9500
1  Leetcode                 8000
2  Handbags               -23000
```

### **Explanation**  
- **Leetcode**: Bought at **1000$** on day `1`, sold at **9000$** on day `5`.  
  - `Capital Gain = 9000 - 1000 = 8000`.  
- **Corona Masks**:  
  - Bought at **10$** on day `2`, sold at **1010$** on day `3` → Gain = `1010 - 10 = 1000`.  
  - Bought at **1000$** on day `4`, sold at **500$** on day `5` → Loss = `500 - 1000 = -500`.  
  - **Total Gain = 1000 - 500 + 9000 = 9500$.**  
- **Handbags**: Bought at **30000$** on day `17`, sold at **7000$** on day `29`.  
  - `Capital Loss = 7000 - 30000 = -23000`.  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values(by=["stock_name", "operation_day"])` | **O(N log N)** |
| Assigning Buy as Negative | `np.where(x["operation"] == "Buy", -x["price"], x["price"])` | **O(N)** |
| Grouping & Aggregation | `groupby("stock_name").sum()` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses vectorised operations** (`np.where()`, `groupby()`, `.sum()`).  
✔ **Handles large datasets efficiently**.  
✔ **Ensures correctness by sorting transactions before processing**.  

🚀 **With this approach, you can efficiently calculate capital gain/loss for stocks across multiple transactions!** 🎯