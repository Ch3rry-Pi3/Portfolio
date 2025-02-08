# 📊 **LeetCode 1083: Sales Analysis II**

## 📌 **Overview**
This project solves **LeetCode Problem 1083: Sales Analysis II**. The goal is to find **buyers** who have purchased an **S8** but **not** an **iPhone** based on transaction data.

### **Problem Statement**
You are given two tables:

1. **Product Table (`product`)**  
   - Contains information about products, including their **`product_id`**, **name**, and **unit price**.

2. **Sales Table (`sales`)**  
   - Contains transaction details, including **`seller_id`**, **`product_id`**, **buyer_id**, **sale quantity**, and **price**.

👉 The task is to **return buyers who have purchased an S8 but not an iPhone**.

### **Expected Output**
- A table with the **buyer_id** of the qualifying buyers.
- The result table can be returned in **any order**.

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
| 1         | 3          | 3        | 2019-06-02 | 1        | 1400   |
| 3         | 3          | 1        | 2019-05-13 | 2        | 2800   |

#### **Output:**
| buyer_id |
|----------|
| 1        |

#### **Explanation**
- Buyer **1** purchased an **S8** but also purchased an **iPhone**, so they are **excluded**.
- Buyer **3** purchased an **iPhone**, but **not** an **S8**, so they are **excluded**.
- Buyer **2** did not purchase an **S8**, so they are **excluded**.
- Since **only buyer 1** meets the criteria, the final result is **buyer_id = 1**.

## 🛠 **Approach**
### **1️⃣ Merge Sales & Product Data**
- Merge `sales` and `product` tables on **`product_id`**.

### **2️⃣ Identify Buyers for Each Product**
- Filter buyers who have **purchased an S8**.
- Filter buyers who have **purchased an iPhone**.

### **3️⃣ Find Buyers Who Bought an S8 But Not an iPhone**
- Use `.isin()` to find buyers in one set but **not the other**.

## 🚀 **Implementation**
```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    """
    Finds buyers who purchased an S8 but not an iPhone.
    Returns a DataFrame containing the buyer_id(s).
    """

    # Merge product and sales DataFrames on 'product_id'
    df = pd.merge(left=product, right=sales, on="product_id", how="left")
    
    # Get buyer IDs for those who bought the S8
    s8_buyers = df[df["product_name"] == "S8"]["buyer_id"]
    
    # Get buyer IDs for those who bought the iPhone
    iphone_buyers = df[df["product_name"] == "iPhone"]["buyer_id"]
    
    # Filter buyers who bought an S8 but not an iPhone
    result = df[(df["buyer_id"].isin(s8_buyers)) & (~df["buyer_id"].isin(iphone_buyers))]
    
    # Return only the buyer_id column
    return result[["buyer_id"]].drop_duplicates()
```

## ⏳ **Time Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge Tables | `merge(product, sales)` | **O(N)** |
| Filter S8 Buyers | `.query("product_name == 'S8'")` | **O(N)** |
| Filter iPhone Buyers | `.query("product_name == 'iPhone'")` | **O(N)** |
| Find Buyers Not in iPhone List | `.isin()` and `~.isin()` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🏗 **Project Structure**
```
sales_analysis_ii/
├── sales_analysis_ii.py   # Python solution
├── README.md              # This documentation
```

## 🏆 **Why This Works**
✔ **Uses Pandas' efficient filtering** instead of nested loops.  
✔ **Handles edge cases** (buyers who bought both or neither).  
✔ **Runs in O(N) time complexity** for efficiency.  

**🚀 Now you can efficiently analyse customer purchases using Pandas!** 🎯