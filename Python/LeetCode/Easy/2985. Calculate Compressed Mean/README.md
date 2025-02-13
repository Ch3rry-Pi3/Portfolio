# 📊 **LeetCode 2985: Calculate Compressed Mean**  

## 📌 **Problem Overview**  
Given a dataset of **orders**, where each order has an associated **item count** and a **number of occurrences**, we need to compute the **average number of items per order** using a **weighted mean formula**, rounded to **two decimal places**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
orders_data = {
    "order_id": [1, 10, 12, 13],
    "item_count": [1, 2, 3, 4],
    "order_occurrences": [500, 1000, 800, 1000]
}
```

## 🛠 **Python Solution**
```python
import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average number of items per order, rounded to 2 decimal places.

    Parameters:
    orders (pd.DataFrame): A DataFrame containing order information with columns:
                           - 'order_id' (int): Unique identifier for each order.
                           - 'item_count' (int): Number of items in the order.
                           - 'order_occurrences' (int): Number of times this order occurred.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'average_items_per_order' (float): The computed average items per order.
    """
    # Compute the weighted sum of items across all occurrences
    total_items = (orders["item_count"] * orders["order_occurrences"]).sum()

    # Compute the total number of orders
    total_orders = orders["order_occurrences"].sum()

    # Calculate the compressed mean, rounding to 2 decimal places
    avg_items_per_order = round(total_items / total_orders, 2)

    # Return as a DataFrame
    return pd.DataFrame({"average_items_per_order": [avg_items_per_order]})
```

## ⏳ **Complexity Analysis**
| Step         | Operation                           | Time Complexity |
|-------------|------------------------------------|----------------|
| Multiplication | `orders["item_count"] * orders["order_occurrences"]` | **O(N)** |
| Summation    | `.sum()`                           | **O(N)** |
| Division     | `total_items / total_orders`      | **O(1)** |
| DataFrame Creation | `pd.DataFrame()`           | **O(1)** |
| **Total Complexity** | **O(N)** | ✅ **Efficient** |

Since all operations run in **linear time**, this approach is optimal.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python compressed_mean.py
```

### **3️⃣ Sample Output**
```plaintext
   average_items_per_order
0                     2.70
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas vectorised operations** for efficiency.  
✔ Ensures **accurate calculation using weighted mean formula**.  
✔ Returns the result in **a properly formatted DataFrame**.  
✔ 🚀 **Optimised for large datasets with O(N) complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for computing compressed means!** 📊🔢