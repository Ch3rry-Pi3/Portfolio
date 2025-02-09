# 🏷️ **LeetCode 1543: Fix Product Name Format**

## 📌 **Problem Overview**
The **Sales** table contains manually entered sales records from the year **2000**, where:
- `product_name` may contain **leading/trailing spaces** and is **case-insensitive**.
- `sale_date` is a **date column** but should be converted to `YYYY-MM` format.
- Each row represents a sale transaction.

### **Goal**
- Normalise the `product_name` by **removing extra spaces** and **converting to lowercase**.
- Convert `sale_date` into the **`YYYY-MM`** format.
- Count the **total number of sales** for each `(product_name, sale_date)` combination.
- Sort the result **first by `product_name` in ascending order**, then by `sale_date` in ascending order.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
| sale_id | product_name  | sale_date  |
|---------|--------------|------------|
| 1       | LCPHONE      | 2000-01-16 |
| 2       | LCPhone      | 2000-01-17 |
| 3       | LCPhoNE      | 2000-01-19 |
| 4       | LCKEyCHAiN   | 2000-02-19 |
| 5       | LCKeyChain   | 2000-02-21 |
| 6       | Matryoshka   | 2000-03-31 |

#### **Output:**
| product_name | sale_date | total |
|-------------|----------|-------|
| lckeychain  | 2000-02  | 2     |
| lcphone     | 2000-01  | 3     |
| lcphone     | 2000-02  | 1     |
| matryoshka  | 2000-03  | 1     |

#### **Explanation**
- **Normalise `product_name`**:
  - "LCPHONE", "LCPhone", and "LCPhoNE" → **"lcphone"**
  - "LCKEyCHAiN" and "LCKeyChain" → **"lckeychain"**
  - "Matryoshka" → **"matryoshka"**
- **Convert `sale_date`** to `YYYY-MM` format.
- **Group and count occurrences**.

## 🛠 **Approach**
This problem requires **string cleaning, date formatting, and grouping**:
1. **Normalise `product_name`**:
   - Convert to **lowercase**.
   - Strip **leading/trailing spaces**.
2. **Format `sale_date`** to `YYYY-MM`.
3. **Group by (`product_name`, `sale_date`)** and **count occurrences**.
4. **Sort results** by `product_name` and `sale_date`.

## 🚀 **Python Solution**
```python
import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the product name format, formats the sale date, and counts total sales per month.

    Args:
        sales (pd.DataFrame): DataFrame containing 'product_name' and 'sale_date'.

    Returns:
        pd.DataFrame: Aggregated sales count per (product_name, sale_date).
    """
    # Normalise product names: Lowercase and strip spaces
    sales['product_name'] = sales['product_name'].str.lower().str.strip()
    
    # Convert sale_date to 'YYYY-MM' format
    sales['sale_date'] = sales['sale_date'].dt.strftime('%Y-%m')
    
    # Group by product_name and sale_date, count occurrences
    result = sales.groupby(['product_name', 'sale_date']).size().reset_index(name='total')
    
    return result
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| String Normalisation | Convert to lowercase, trim spaces | **O(N)** |
| Date Formatting | Convert to `YYYY-MM` format | **O(N)** |
| Grouping | `groupby().size().reset_index()` | **O(N log N)** |
| Sorting | Sorting by product name, then by sale date | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 📁 **Project Structure**
```
fix_product_name/
├── fix_product_name.py   # Python solution
├── README.md             # Documentation
```

## 🏆 **Why This Works**
✔ **Cleans messy manual data** by normalising names and dates.  
✔ **Aggregates and counts data efficiently** using Pandas.  
✔ **Optimised complexity** ensures scalability for large datasets.  


🚀 **Now you have a structured approach to standardising and analysing sales data!** 🎯