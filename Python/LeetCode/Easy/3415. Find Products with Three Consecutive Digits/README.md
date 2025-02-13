# 🔢 **LeetCode 3415: Find Products with Three Consecutive Digits**  

## 📌 **Problem Overview**  
Given a dataset of **products and their names**, we need to **identify products** where:  

✔ The product name contains **exactly three consecutive digits**.  
✔ The product name **does not contain four or more consecutive digits**.  

The output should contain only the **`product_id`** and **`name`**, sorted in **ascending order** by `product_id`.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
products_data = {
    "product_id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["ABC123XYZ", "A12B34C", "Product56789", "NoDigitsHere", 
             "789Product", "Item@003Description", "Product12X34"]
}
```

### **Processing Logic:**
| Product ID | Name                  |
|------------|-----------------------|
| **1**      | ABC123XYZ             |
| **2**      | A12B34C               |
| **3**      | Product56789          |
| **4**      | NoDigitsHere          |
| **5**      | 789Product            |
| **6**      | Item@003Description   |
| **7**      | Product12X34          |

1. **Filter Products That Contain Exactly Three Consecutive Digits**  
   - ✅ **Keep**:  
     - `ABC123XYZ` (**123**)  
     - `789Product` (**789**)  
     - `Item@003Description` (**003**)  
   - ❌ **Ignore**:  
     - `Product56789` (**56789** contains **5 consecutive digits**).  
     - `A12B34C` (No **three consecutive digits in a row**).  
     - `NoDigitsHere` (No digits at all).  
     - `Product12X34` (No **three consecutive digits in a row**).  

2. **Sort by `product_id` in Ascending Order**  

3. **Final Result:**
   - **Product IDs**: `1, 5, 6`

### **Expected Output:**
```plaintext
   product_id              name
0          1        ABC123XYZ
4          5       789Product
5          6  Item@003Description
```

## 🛠 **Python Solution**
```python
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies products whose names contain a sequence of exactly three consecutive digits.

    Parameters:
    products (pd.DataFrame): A DataFrame containing product information with columns:
                             - 'product_id' (int): Unique identifier for each product.
                             - 'name' (str): Product name.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'product_id' (int): Products that contain exactly three consecutive digits in their name.
                  - 'name' (str): The corresponding product name.
                  The result is sorted in ascending order by 'product_id'.
    """
    # Filter products that contain exactly three consecutive digits but not four or more
    filtered_products = products[
        products["name"].str.contains(r"\d{3}", regex=True) & 
        ~products["name"].str.contains(r"\d{4,}", regex=True)
    ]

    # Sort results by 'product_id'
    return filtered_products.sort_values("product_id")
```

## ⏳ **Complexity Analysis**
| Step         | Operation                     | Time Complexity |
|-------------|------------------------------|----------------|
| Filtering   | `.str.contains(r"\d{3}")`     | **O(N)** |
| Filtering   | `.str.contains(r"\d{4,}")`    | **O(N)** |
| Sorting     | `.sort_values(by="product_id")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python three_consecutive_digits.py
```

### **3️⃣ Sample Output**
```plaintext
   product_id              name
0          1        ABC123XYZ
4          5       789Product
5          6  Item@003Description
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.str.contains()`** for efficient pattern matching.  
✔ Implements **regular expressions (`\d{3}` and `\d{4,}`) for precise filtering.**  
✔ Ensures **sorted ordering by `product_id`** to match problem requirements.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for finding products with exactly three consecutive digits!** 📦🔢