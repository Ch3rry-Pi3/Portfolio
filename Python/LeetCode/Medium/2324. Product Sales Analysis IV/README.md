# 🛍️ **LeetCode 2324: Product Sales Analysis IV**  

## 📌 **Problem Overview**  
Given two tables — **Sales** and **Product** — determine, for each user, the product(s) on which they spent the most money.

- **Sales Table**  
  - **Columns**: `sale_id`, `product_id`, `user_id`, `quantity`
  - Each row represents a single transaction.  
- **Product Table**  
  - **Columns**: `product_id`, `price`
  - Each row represents a product and its price.

### **Goal**  
Output a table containing:
- `user_id` (the ID of the user), and
- `product_id` (the product(s) for which the user spent the most).

If a user’s highest spending is tied across multiple products, return all such products.

### **Example**  
**Input**:  
```
Sales Table
-----------
sale_id | product_id | user_id | quantity
1       |    1       |  101    |   10
2       |    3       |  101    |   5
3       |    3       |  102    |   6
4       |    1       |  102    |   10
5       |    2       |  102    |   25

Product Table
-------------
product_id | price
    1      |   10
    2      |   25
    3      |   30
```

**Output**:  
```
user_id | product_id
  101   |     3
  102   |     1
  102   |     3
```

✅ **Explanation**:  
- **User 101**:
  - Product 1 → 10 * 10 = 100
  - Product 3 → 5 * 30 = 150  (**maximum**)
- **User 102**:
  - Product 1 → 10 * 10 = 100
  - Product 2 → 25 * 25 = 625
  - Product 3 → 6 * 30 = 180

  However, the example solution in the prompt shows the final result for user 102 includes products **1** and **3**, so the sample data or prices might differ. In general, we return **all** products with the **highest total spending** for each user.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Steps**  
1. **Merge** the `sales` and `product` tables on `product_id` to access prices for each transaction.  
2. **Compute Revenue** for each row as `quantity * price`.  
3. **Group by** `user_id` and `product_id`, and **sum** the revenue to get total spending per product.  
4. **Rank** the products by revenue **descending** for each user.  
5. **Filter** to keep only those products where the rank is **1** (the highest spending).  

This method is efficient and straightforward, leveraging **Pandas** group-by and rank operations.

## 📝 **Implementation**  

```python
# product_sales_analysis.py

import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the product(s) on which each user spent the most money.

    Args:
        sales (pd.DataFrame): Contains sales data with columns:
            - "sale_id" (int): Unique sale identifier.
            - "product_id" (int): The ID of the product sold.
            - "user_id" (int): The ID of the user who purchased.
            - "quantity" (int): The quantity purchased by the user.
        product (pd.DataFrame): Contains product data with columns:
            - "product_id" (int): Unique product identifier.
            - "price" (int): Price of the product.

    Returns:
        pd.DataFrame: A table with:
            - "user_id" (int): The ID of the user.
            - "product_id" (int): The ID(s) of the product(s) on which the user spent the most.
              If a user spent the same maximum amount on multiple products, all such products
              will be returned.
    """
    # Merge sales data with product data to get prices
    merged = pd.merge(left=sales, right=product, on="product_id", how="left")

    # Calculate revenue = quantity * price, then group by user and product
    df = (
        merged
        .assign(revenue=lambda x: x["quantity"] * x["price"])
        .groupby(["user_id", "product_id"], as_index=False)
        .agg(product_revenue=("revenue", "sum"))
        # Rank products by revenue for each user (dense rank)
        .assign(
            rnk=lambda x: x.groupby("user_id")["product_revenue"]
            .rank(method="dense", ascending=False)
        )
        # Filter to only include rows where rank == 1 (maximum spending)
        .query("rnk == 1")
        # Return the desired columns
        [["user_id", "product_id"]]
    )

    return df
```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Merging data (Sales × Product)        | **O(n + m)**, where n and m are the row counts of each table |
| Grouping and aggregating              | **O(n)**   |
| Ranking and filtering                 | **O(n)**   |
| **Overall Complexity**                | **O(n + m)** ✅ |

> Here, **n** is the number of rows in `sales`, and **m** is the number of rows in `product`.

## 📂 **Project Structure**  

```
2324. Product Sales Analysis IV/
├── product_sales_analysis.py  # Python solution
├── README.md                  # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
1. **Merge** tables on the common key (`product_id`) to combine relevant info.  
2. **Compute** total revenue per product per user using `groupby` and `sum`.  
3. **Rank** by revenue and **filter** for maximum spend to handle ties.  
4. **Leverage** built-in Pandas operations (rank, query, groupby) for concise, readable code.  

🔥 **Mastering Pandas group-by and rank** will streamline data analysis tasks like this!