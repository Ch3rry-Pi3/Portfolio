# 📊 **LeetCode 1069: Product Sales Analysis II**

## 📌 **Overview**
This project solves **LeetCode Problem 1069: Product Sales Analysis II**,  
where we **calculate the total quantity sold** for each product.

### **Problem Statement**
You are given two tables:

1️⃣ **Sales Table**
   - Contains **product sales data** (product ID, quantity sold, price, etc.).  
   - Each row represents a **sale of a product** in a given year.

2️⃣ **Product Table**
   - Contains **product details** (product ID, product name).  
   - Each product has **a unique product_id**.

#### **Goal:**  
📊 **Find the total quantity sold for each product.**  

## 🎯 **Example Walkthrough**
### **Example Input**
#### **Sales Table**
| sale_id | product_id | year | quantity | price |
|---------|-----------|------|----------|-------|
| 1       | 100       | 2008 | 10       | 5000  |
| 2       | 100       | 2008 | 15       | 5000  |
| 3       | 200       | 2011 | 15       | 9000  |

#### **Product Table**
| product_id | product_name |
|------------|-------------|
| 100        | Nokia       |
| 200        | Apple       |
| 300        | Samsung     |

### **Step-by-Step Breakdown**
1️⃣ **Merge the `Sales` and `Product` tables on `product_id`**  
   - This ensures that each sale is **linked to its corresponding product name**.  

2️⃣ **Group by `product_id` and sum `quantity`**  
   - This computes the **total quantity sold for each product**.  

### **Expected Output**
```python
Output:
   product_id  total_quantity
0        100              25
1        200              15
```
- **Nokia (100)** had **10 + 15 = 25** total sales.  
- **Apple (200)** had **15** total sales.  
- **Samsung (300)** had **no sales**, so it's **not included** in the output.

## 📝 **Step-by-Step Approach**
### **1️⃣ Merge Sales & Product Tables**
```python
sales.merge(product, on="product_id", how="left")
```
- **Ensures each sale has the correct product name.**

### **2️⃣ Group by `product_id` and sum `quantity`**
```python
.groupby("product_id", as_index=False)["quantity"].sum()
```
- **Aggregates total sales per product.**

### **3️⃣ Rename the Column for Clarity**
```python
.rename(columns={"quantity": "total_quantity"})
```
- **Ensures the column name is clear and meaningful.**

## **💡 Implementation**
```python
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total quantity sold for each product.

    The function merges the sales data with the product details and 
    calculates the total quantity sold per product.

    :param sales: DataFrame containing sales records (product_id, quantity, etc.).
    :param product: DataFrame containing product details (product_id, product_name).
    :return: DataFrame with each product's total quantity sold.
    """

    return (
        sales.merge(product, on="product_id", how="left")  # Merge product details into sales data
        .groupby("product_id", as_index=False)["quantity"].sum()  # Aggregate quantity sold per product
        .rename(columns={"quantity": "total_quantity"})  # Rename column for clarity
    )

```

## ⏳ **Time Complexity Analysis**
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| **Merge & GroupBy (`O(n)`)** | **O(n)** ✅ | **O(n)** ✅ |

- **Each product ID is processed once (`O(n) time complexity`).**  
- **Stores results in a new DataFrame (`O(n) space complexity`).**  

## 🏗 **Project Structure**
```
1069. Product Sales Analysis II/
├── product_sales_analysis.py    # Python implementation of the solution
├── README.md                    # Detailed explanation & walkthrough
```

✨ **Master product sales analysis with this efficient `O(n)` approach!** 🚀  
