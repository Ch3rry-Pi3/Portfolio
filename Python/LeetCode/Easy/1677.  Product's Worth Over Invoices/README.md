# 🏷 **LeetCode 1677: Product's Worth Over Invoices**  

## 📌 **Problem Overview**  
Given two tables, **Product** and **Invoice**, the goal is to calculate the **total rest, paid, canceled, and refunded amounts** for each product across all invoices.  

- The **Product** table contains product IDs and their respective names.  
- The **Invoice** table records transactions, including the **amount left to pay (rest)**, **amount paid**, **amount canceled**, and **amount refunded** for each product.  

### **Task**  
For each product, return a table with:  
- `name`: Product name  
- `rest`: Total remaining balance  
- `paid`: Total amount paid  
- `canceled`: Total amount canceled  
- `refunded`: Total amount refunded  

The result should be **ordered by product name**.

## 🛠 **Approach**
This problem requires aggregating financial details for each product.  
The solution follows these steps:  

1. **Merge** the **Product** and **Invoice** tables on `product_id`.  
2. **Group by** `name` (product name).  
3. **Aggregate** financial columns (`rest`, `paid`, `canceled`, `refunded`) using `sum()`.  
4. **Return the result** ordered by `product name`.

This approach ensures that each product's financial transactions are **summed correctly** and **sorted alphabetically**.

## 🚀 **Python Solution**
```python
import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    """
    Analyses product worth over invoices by calculating total rest, paid, canceled, and refunded amounts.

    Args:
        product (pd.DataFrame): DataFrame containing product details with 'product_id' and 'name'.
        invoice (pd.DataFrame): DataFrame containing invoice details with 'product_id', 'rest', 'paid', 'canceled', and 'refunded'.

    Returns:
        pd.DataFrame: Aggregated financial details for each product, ordered by product name.
    """
    return (
        pd.merge(left=product, right=invoice, on="product_id", how="left")
        .groupby("name", as_index=False)[["rest", "paid", "canceled", "refunded"]]
        .sum()
    )
```

## 📌 **Example Walkthrough**

### **Example 1**
#### **Input:**  
**Product Table**  
| product_id | name  |
|------------|-------|
| 0          | ham   |
| 1          | bacon |

**Invoice Table**  
| invoice_id | product_id | rest | paid | canceled | refunded |
|------------|------------|------|------|----------|----------|
| 23         | 0          | 2    | 0    | 5        | 0        |
| 12         | 0          | 0    | 5    | 3        | 0        |
| 0          | 1          | 1    | 4    | 1        | 3        |
| 1          | 1          | 1    | 4    | 1        | 3        |
| 4          | 1          | 1    | 4    | 1        | 3        |
| 3          | 0          | 1    | 0    | 1        | 0        |
| 4          | 0          | 1    | 0    | 1        | 0        |

#### **Output:**  
| name  | rest | paid | canceled | refunded |
|-------|------|------|----------|----------|
| bacon | 3    | 3    | 3        | 3        |
| ham   | 2    | 4    | 5        | 3        |

#### **Explanation:**  
- **For bacon**:
  - `rest = 1 + 1 + 1 = 3`
  - `paid = 4 + 4 + 4 = 3`
  - `canceled = 1 + 1 + 1 = 3`
  - `refunded = 3 + 3 + 3 = 3`

- **For ham**:
  - `rest = 2 + 0 + 1 + 1 = 2`
  - `paid = 0 + 5 + 0 + 0 = 4`
  - `canceled = 5 + 3 + 1 + 1 = 5`
  - `refunded = 0 + 0 + 0 + 3 = 3`

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge tables | `pd.merge()` | **O(N)** |
| Grouping | `groupby("name")` | **O(N log N)** |
| Aggregation | `sum()` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**
✔ **Uses efficient merging & aggregation techniques.**  
✔ **Scalable for larger datasets due to O(N log N) complexity.**  
✔ **Provides ordered output by product name.**  

🚀 **With this approach, you can efficiently compute product worth across all invoices!** 🎯