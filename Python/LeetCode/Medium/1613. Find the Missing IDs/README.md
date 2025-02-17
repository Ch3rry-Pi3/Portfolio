# 🔍 **LeetCode 1613: Find the Missing IDs**

## 📌 **Problem Overview**  
You are given a table `Customers` that contains a list of customer IDs and names. Each `customer_id` is **unique** in the table.  

However, some IDs are **missing** in the range between **1** and the **maximum `customer_id` present** in the table.  

### **Goal**  
Find and return the **missing customer IDs** that are in the range `[1, max(customer_id)]` but **not present** in the table.  

- The **maximum** `customer_id` **does not exceed 100**.  
- The output should be sorted in **ascending order**.  

## 📊 **Database Schema**  
### **Customers Table**  
| Column Name    | Type   | Description |
|---------------|--------|-------------|
| `customer_id` | int    | Unique ID for the customer |
| `customer_name` | varchar | Name of the customer |

## 🚀 **Example Walkthrough**  

### **Example Input**  

#### **Customers Table**
| customer_id | customer_name |
|------------|--------------|
| 1          | Alice        |
| 4          | Bob          |
| 5          | Charlie      |

### **Output**
```python
   ids
0    2
1    3
```

### **Explanation**  
- The **maximum** customer ID in the table is **5**.  
- The range of valid IDs is **[1, 2, 3, 4, 5]**.  
- The IDs **2 and 3** are missing, so we return them in ascending order.  

## 🛠 **Approach**  

### **1️⃣ Generate the Full Range of IDs**
- Create a **complete list of IDs** from `1` to `max(customer_id)`.

### **2️⃣ Identify Missing IDs**
- Perform a **left join** between the full ID list and the `Customers` table.
- Check for **IDs that do not exist** in the `Customers` table.

### **3️⃣ Return the Missing IDs**
- Select only the missing IDs and sort them in **ascending order**.

## 📝 **Python Solution**  

```python
import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the missing customer IDs that are not present in the given DataFrame.

    Args:
        customers (pd.DataFrame): A DataFrame containing customer information with:
            - "customer_id" (int): Unique ID of the customer.

    Returns:
        pd.DataFrame: A DataFrame containing the missing IDs sorted in ascending order.
    """

    # Generate a complete list of IDs from 1 to the maximum customer_id
    all_ids = pd.DataFrame({"ids": range(1, customers["customer_id"].max() + 1)})

    # Merge with existing customer data and find missing IDs
    missing_ids = (
        pd.merge(all_ids, customers, left_on="ids", right_on="customer_id", how="left")
        .query("customer_id.isna()")[["ids"]]
        .sort_values(by="ids", ascending=True)
    )

    return missing_ids
```

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Generating ID Range** | `range(1, max_id + 1)` | **O(N)** |
| **Merging Data** | `merge(left, right, how="left")` | **O(N)** |
| **Filtering Missing IDs** | `query("customer_id.isna()")` | **O(N)** |
| **Sorting Output** | `sort_values(by="ids")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`merge`, `query`, `sort_values`).  
✔ **Handles large datasets effectively** with vectorised operations.  
✔ **Guaranteed correctness** by checking all IDs systematically.  

🚀 **With this approach, you can efficiently identify missing IDs in any dataset!** 🎯