# 🧾 **LeetCode 3465: Find Products with Valid Serial Numbers**  

## 📌 **Problem Overview**  

You are given a table called **products** with the following columns:  
- `product_id` (int): Unique identifier for the product.  
- `product_name` (varchar): The name of the product.  
- `description` (varchar): A text field that may contain a **valid serial number**.  

### **Valid Serial Number Rules:**  
1. Starts with the letters **SN** (case-sensitive).  
2. Followed by **exactly 4 digits**.  
3. Contains a **hyphen (-)** followed by **4 digits**.  
4. Must be **within the description** (may not necessarily start at the beginning).  

### **Objective:**  
Return a list of all products whose description contains a **valid serial number**.  
The result should be **ordered by `product_id` in ascending order**.  



## ✅ **Example**  

### **Input:**  
| product_id | product_name | description                                                |
|--|--|-|
| 1         | Widget A     | This is a sample product with SN1234-5678                    |
| 2         | Widget B     | A product with serial SN9876-1234 in the description          |
| 3         | Widget C     | Product SN1234-56789 is available now                        |
| 4         | Widget D     | No serial number here                                        |
| 5         | Widget E     | Check out SN4321-8765 in this description                     |

### **Output:**  
| product_id | product_name | description                                                |
|--|--|-|
| 1         | Widget A     | This is a sample product with SN1234-5678                    |
| 2         | Widget B     | A product with serial SN9876-1234 in the description          |
| 5         | Widget E     | Check out SN4321-8765 in this description                     |



## 🛠 **Approach & Intuition**  

### 🔍 **Step-by-Step:**  
1. **Regex Pattern:**  
   - Create a pattern to identify valid serial numbers:  
     - `SN[0-9]{4}-[0-9]{4}[^0-9]` → Matches valid serials within text.  
     - `SN[0-9]{4}-[0-9]{4}$` → Matches valid serials at the end.  

2. **Data Processing:**  
   - Use `pandas` to load the data.  
   - Filter rows where the **description** matches the valid serial number pattern using `str.contains()`.  
   - Combine both pattern checks using a logical OR (`|`).  

3. **Sorting:**  
   - Order the results by `product_id` in **ascending order**.  



## 📝 **Python Implementation**  

```python
import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Find products with a valid serial number pattern in their description.

    Args:
        products (pd.DataFrame): A DataFrame with columns:
            - product_id (int): Unique product identifier
            - product_name (str): Name of the product
            - description (str): Description with possible serial numbers

    Returns:
        pd.DataFrame: Filtered DataFrame with valid serial numbers,
                      sorted by product_id.
    """
    pattern1 = r'SN[0-9]{4}\-[0-9]{4}[^0-9]'
    pattern2 = r'SN[0-9]{4}\-[0-9]{4}$'
    return products[
        (products["description"].str.contains(pattern1, na=False)) |
        (products["description"].str.contains(pattern2, na=False))
    ].sort_values(by="product_id")
```



## 📂 **Project Structure**  

```
find_valid_serial_numbers/
├── main.py       # Python solution with example usage
├── README.md      # Problem description and explanation
```



## 💡 **Edge Cases Considered:**  
1. Descriptions with **no serial numbers**.  
2. Serial numbers that are **invalid** (e.g., incorrect format).  
3. **Empty descriptions** (handled using `na=False` in regex).  
4. **Case sensitivity** to ensure correct matching.  



## 🚀 **Why This Works:**  
- **Efficiency:** Uses vectorized operations with `pandas`, making it fast for large datasets.  
- **Accuracy:** Ensures that only valid serial numbers are captured using well-defined regex patterns.  
- **Robustness:** Handles edge cases and ensures the output is properly sorted.  



## ✅ **Test Cases:**  
- Test with **various product descriptions** to ensure that only valid serial numbers are returned.  
- Check the **ordering** of results to verify that the `product_id` is in ascending order.  