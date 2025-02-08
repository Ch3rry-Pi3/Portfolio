# 📊 **LeetCode 1082: Sales Analysis I**

## 📌 **Overview**
This project solves **LeetCode Problem 1082: Sales Analysis I**. The goal is to determine the **best seller(s)** by total sales price. If multiple sellers have the same highest total sales, **all** of them should be returned.

### **Problem Statement**
You are given two tables:

1. **Product Table (`product`)**  
   - Contains information about products, including their **`product_id`**, **name**, and **unit price**.

2. **Sales Table (`sales`)**  
   - Contains transaction details, including **`seller_id`**, **`product_id`**, **sale quantity**, and **price**.

👉 The task is to find **the seller(s) with the highest total sales price**.

### **Expected Output**
- A table with the **seller_id** of the top seller(s).
- If there is a **tie**, all sellers should be included.
- The result can be returned in **any order**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
#### **Product Table**
| product_id | product_name | unit_price |
|------------|-------------|------------|
| 1          | S8          | 1000       |
| 2          | G4          | 800        |
| 3          | iPhone      | 1400       |

#### **Sales Table**
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
|-----------|------------|----------|------------|----------|--------|
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000   |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800    |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800    |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800   |

#### **Output:**
| seller_id |
|-----------|
| 1         |
| 3         |

#### **Explanation**
- Seller **1** sold **S8** (2 units for $2000) and **G4** (1 unit for $800), totaling **$2800**.
- Seller **2** sold **G4** (1 unit for $800).
- Seller **3** sold **iPhone** (2 units for $2800).
- Since sellers **1 and 3** have the highest total sales **($2800 each)**, both are included in the result.

## 🛠 **Approach**
### **1️⃣ Merge Sales & Product Data**
- Merge `sales` and `product` tables on **`product_id`**.

### **2️⃣ Aggregate Total Sales**
- **Group by** `seller_id` and **sum** the `price` column.

### **3️⃣ Find the Highest Sales**
- Find the **max total sales**.
- Filter sellers who achieved that maximum.

## 🚀 **Implementation**
```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the best seller(s) by total sales price.
    Returns a DataFrame containing the seller_id(s) with the highest sales.
    """

    # Aggregate total sales per seller
    sales_summary = sales.groupby("seller_id", as_index=False)["price"].sum()

    # Return sellers with the highest total sales
    return sales_summary.loc[sales_summary["price"] == sales_summary["price"].max(), ["seller_id"]]
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge Tables | `merge(product, sales)` | **O(N)** |
| Aggregate Sales | `groupby().sum()` | **O(N)** |
| Find Max Sales | `.max()` | **O(N)** |
| Filter Best Sellers | `.loc[]` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
sales_analysis/
├── sales_analysis.py   # Python solution
├── README.md           # This documentation
```

## 🏆 **Why This Works**
✔ **Uses Pandas' vectorised operations** for efficient aggregation.  
✔ **One-pass filtering** ensures optimal performance.  
✔ **Handles ties** in total sales correctly.  

**🚀 Now you can efficiently analyse top sellers using Pandas!** 🎯