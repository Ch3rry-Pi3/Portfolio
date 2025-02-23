# 📦 **LeetCode 1867: Orders With Maximum Quantity Above Average**  

## 📌 **Problem Overview**  
In an e-commerce system, each order consists of multiple products, with each product having a specific **quantity**.  

We need to **identify imbalanced orders**:  
- An order is **imbalanced** if its **maximum quantity** (i.e., the highest quantity of any product in that order)  
  is **strictly greater** than the **average quantity of every order** (including itself).  
- The **average quantity of an order** is calculated as:  

\[
\text{average quantity} = \frac{\text{total quantity of all products in the order}}{\text{number of different products in the order}}
\]


## 🖼 **Example 1**  
### **Input: OrdersDetails Table**
```
+----------+------------+----------+
| order_id | product_id | quantity |
+----------+------------+----------+
|    1     |     1      |    12    |
|    1     |     2      |    10    |
|    1     |     3      |    15    |
|    2     |     4      |    8     |
|    2     |     5      |    4     |
|    2     |     6      |    6     |
|    2     |     7      |    4     |
|    3     |     5      |    15    |
|    3     |     6      |    18    |
|    3     |     7      |    20    |
|    4     |     8      |    2     |
|    4     |     9      |    8     |
|    5     |     9      |    9     |
|    5     |     9      |    9     |
+----------+------------+----------+
```

### **Output:**  
```
+----------+
| order_id |
+----------+
|    1     |
|    3     |
+----------+
```

✅ **Explanation:**  
| Order ID | Total Quantity | Unique Products | Average Quantity | Maximum Quantity | Imbalanced? |
|----------|---------------|-----------------|------------------|------------------|-------------|
| **1** | (12 + 10 + 15) = 37 | 3 | **12.33** | **15** | ✅ **Yes** |
| **2** | (8 + 4 + 6 + 4) = 22 | 4 | **5.5** | **8** | ❌ No |
| **3** | (15 + 18 + 20) = 53 | 3 | **14.33** | **20** | ✅ **Yes** |
| **4** | (2 + 8) = 10 | 2 | **5.0** | **8** | ❌ No |
| **5** | (9 + 9) = 18 | 2 | **9.0** | **9** | ❌ No |

- **Maximum Average Across All Orders**: `max(12.33, 5.5, 14.33, 5.0, 9.0) = 14.33`
- **Orders 1 and 3** have a **maximum quantity greater than 14.33**, so they are **imbalanced**.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Aggregate Per Order & Compare Max Quantity**
1. **Compute total quantity per order**.  
2. **Compute the average quantity per order**:
   - Divide total quantity by **number of unique products**.  
3. **Determine the maximum average quantity across all orders**.  
4. **Identify orders where the maximum quantity of any product exceeds this value**.  

## 📝 **Implementation**  

```python
# imbalanced_orders.py

import pandas as pd

def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies imbalanced orders where the maximum quantity of a product 
    in an order is strictly greater than the average quantity of all orders.

    Args:
        orders_details (pd.DataFrame): Contains order data with columns:
            - "order_id" (int): The ID of the order.
            - "product_id" (int): The ID of the product.
            - "quantity" (int): The quantity ordered for that product.

    Returns:
        pd.DataFrame: A table containing:
            - "order_id" (int): The IDs of imbalanced orders.
        
        The result can be returned in any order.
    """

    # Aggregate per order: total quantity, max quantity, and unique product count
    df = (
        orders_details
        .groupby("order_id")
        .agg(
            total_quantity=("quantity", "sum"),
            max_quantity=("quantity", "max"),
            unique_products=("product_id", "nunique")
        )
        .reset_index()
    )

    # Compute the average quantity per order
    df["avg"] = df["total_quantity"] / df["unique_products"]

    # Determine the maximum average quantity across all orders
    max_avg = df["avg"].max()

    # Filter orders where the max quantity exceeds max_avg
    return df[df["max_quantity"] > max_avg][["order_id"]]

```

## ⏳ **Time Complexity Analysis**  

| Operation                                | Complexity |
|------------------------------------------|------------|
| Grouping by `order_id` and aggregating   | **O(N log N)** |
| Computing `max` and `average` quantities | **O(N)** |
| Identifying imbalanced orders            | **O(N)** |
| **Overall Complexity**                    | **O(N log N)** ✅ |

> **N = number of rows in `orders_details`**  

## 📂 **Project Structure**  

```
1867. Orders With Maximum Quantity Above Average/
├── imbalanced_orders.py  # Python solution
├── README.md             # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Efficient Pandas-based aggregation**.  
✔ **Straightforward method to analyse e-commerce orders**.  
✔ **Demonstrates detecting imbalances in transactional data**.  

🚀 **Great for mastering Pandas groupby operations in data analysis!** 📊