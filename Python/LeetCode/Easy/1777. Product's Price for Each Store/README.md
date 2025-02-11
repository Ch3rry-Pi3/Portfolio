# 🛒 **LeetCode 1777: Product's Price for Each Store**

## 📌 **Problem Overview**
We have a table `Products` containing information about product prices at different stores. The goal is to **pivot the data** so that each **store** has its own column, and the prices for each product are aligned accordingly.

### **Table Schema**
| Column Name  | Type   |
|-------------|--------|
| product_id  | int    |
| store       | enum   |
| price       | int    |

- `(product_id, store)` is the **primary key**.
- The `store` column can have values: `'store1'`, `'store2'`, `'store3'`.
- The `price` column represents the price of the product at that store.

## 🎯 **Goal**
Convert the table so that each `product_id` appears **once per row**, and the **stores become column headers**.

## 🛠 **Approach**
To **reshape** the given `Products` table, we need to **pivot** the `store` column so that:
1. **Each store becomes a column header.**
2. **Prices are placed correctly under their respective stores.**
3. **If a product is not available at a store, it should show `null` (NaN in Pandas).**

We use the Pandas **`.pivot()`** function to achieve this transformation:
- `index="product_id"` → Each unique `product_id` remains a row.
- `columns="store"` → Each store becomes a column.
- `values="price"` → The price values are placed correctly.

### **Example**
#### **Input:**
| product_id | store  | price |
|------------|--------|-------|
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store3 | 80    |
| 1          | store1 | 70    |

#### **Output:**
| product_id | store1 | store2 | store3 |
|------------|--------|--------|--------|
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |

#### **Explanation:**
- Product `0` is available in **all stores** (`store1`, `store2`, `store3`).
- Product `1` is **missing from store2**, so it appears as `null`.

## 🚀 **Python Solution**
```python
import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the product price table by pivoting the 'store' column 
    to create a table where each store has its own column.

    Args:
        products (pd.DataFrame): A DataFrame containing product prices at different stores.
                                 It has columns ['product_id', 'store', 'price'].

    Returns:
        pd.DataFrame: A DataFrame where each row represents a unique product_id,
                      and the columns represent the price of the product at each store.
    """

    return (
        products
        .pivot(index="product_id", columns="store", values="price")
        .reset_index()
    )
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Pivot the table | `.pivot(index="product_id", columns="store", values="price")` | **O(N)** |
| Reset index | `.reset_index()` | **O(1)** |
| **Total Complexity** | **O(N), Space: O(N)** | ✅ Efficient |

## 📌 **Key Takeaways**
✔ **Pivoting Data**: `pivot()` allows transforming rows into columns efficiently.  
✔ **Handles Missing Data**: If a product isn’t available in a store, it appears as `null`.  
✔ **O(N) Complexity**: Efficient for handling large datasets.  

🚀 **With this approach, you can quickly reshape product price data for multiple stores!** 🎯

Let me know if you'd like any modifications! 🚀📊