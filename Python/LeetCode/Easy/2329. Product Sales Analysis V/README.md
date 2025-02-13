# 📊 **LeetCode 2329: Product Sales Analysis V**

## 📌 **Problem Overview**
We have two tables:  

1. **Sales Table** (`sales`):
   - Records user purchases, including `sale_id`, `product_id`, `user_id`, and `quantity` (number of items bought).
   
2. **Product Table** (`product`):
   - Stores product prices, mapping each `product_id` to a `price`.

The goal is to compute **each user's total spending** by multiplying the number of items purchased (`quantity`) by the respective `price`.  

- **The result should be sorted**:
  - By `spending` in **descending** order.
  - If two users have the same spending, order by `user_id` in **ascending** order.

## 🛠 **Approach**
The problem can be broken down into **three key steps**:

1. **Join the Sales and Product Tables:**  
   - Use `product_id` as a key to merge the `sales` and `product` tables.
   
2. **Compute Total Spending per User:**  
   - Calculate spending per transaction:  
     $$
     \text{spending} = \text{quantity} \times \text{price}
     $$

   - Sum up all spending for each `user_id`.

3. **Sort the Results:**  
   - Sort by `spending` (descending).  
   - If there is a tie, sort by `user_id` (ascending).

## 🚀 **Python Solution**
```python
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes total spending per user based on sales transactions and product prices.

    Args:
        sales (pd.DataFrame): DataFrame containing sales data with 'product_id', 'user_id', and 'quantity'.
        product (pd.DataFrame): DataFrame containing product data with 'product_id' and 'price'.

    Returns:
        pd.DataFrame: A DataFrame containing 'user_id' and 'spending', sorted by spending (descending) and user_id (ascending).
    """
    return (
        sales.merge(product, on="product_id")
        .assign(spending=lambda df: df["quantity"] * df["price"])
        .groupby("user_id", as_index=False)["spending"]
        .sum()
        .sort_values(by=["spending", "user_id"], ascending=[False, True])
    )
```


## 📌 **Example Walkthrough**
### **Example Input**
#### **Sales Table:**
| sale_id | product_id | user_id | quantity |
|---------|-----------|---------|----------|
| 1       | 1         | 101     | 10       |
| 2       | 1         | 102     | 1        |
| 3       | 2         | 102     | 3        |
| 4       | 2         | 103     | 2        |
| 5       | 3         | 101     | 3        |

#### **Product Table:**
| product_id | price |
|------------|-------|
| 1          | 10    |
| 2          | 25    |
| 3          | 15    |

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge tables | `sales.merge(product, on="product_id")` | **O(N)** |
| Compute spending | `.assign(spending=quantity * price)` | **O(N)** |
| Group and sum | `.groupby("user_id").sum()` | **O(N)** |
| Sorting | `.sort_values(by=["spending", "user_id"])` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** |

## 🎯 **Why This Approach?**
✔ **Efficient**: Uses `merge()`, `assign()`, and `groupby()` to minimise iterations.  
✔ **Concise**: Functional, readable, and avoids unnecessary loops.  
✔ **Optimal Sorting**: Ensures correct ordering with a single `.sort_values()` call.  

## 🏆 **Final Thoughts**
This solution efficiently computes **user spending** while maintaining clarity and performance. 🚀