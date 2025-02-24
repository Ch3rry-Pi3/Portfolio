# 🔢 **LeetCode 2084: Drop Type 1 Orders for Customers With Type 0 Orders**  

## 📌 **Problem Overview**  

You are given a table **Orders** with the following structure:

| Column Name  | Type  |
|-------------|------|
| order_id    | int  |
| customer_id | int  |
| order_type  | int  |

- Each **customer** may have multiple orders, uniquely identified by `order_id`.  
- Orders can be of **two types**:  
  - **0** (Type 0 order)  
  - **1** (Type 1 order)  

### 🔹 **Goal**  
We need to **return only specific orders** based on the following rules:

1. **If a customer has at least one type 0 order**, do **NOT** return any of their type 1 orders.
2. Otherwise, return **all** of the customer's orders.

✅ **Return the result in any order.**  

## 📊 **Example 1**  

### **Input**  

**Orders Table:**
| order_id | customer_id | order_type |
|----------|------------|------------|
| 1        | 1          | 0          |
| 2        | 1          | 0          |
| 11       | 2          | 1          |
| 12       | 2          | 0          |
| 21       | 3          | 1          |
| 22       | 3          | 0          |
| 31       | 4          | 1          |
| 32       | 4          | 1          |

### **Output**  

| order_id | customer_id | order_type |
|----------|------------|------------|
| 1        | 1          | 0          |
| 2        | 1          | 0          |
| 12       | 2          | 0          |
| 22       | 3          | 0          |
| 31       | 4          | 1          |
| 32       | 4          | 1          |

✅ **Explanation:**  
- **Customer 1** has **only type 0 orders**, so we return both.  
- **Customer 2** has **one type 0 order and one type 1 order**, so we only return the type 0 order.  
- **Customer 3** has **one type 0 order and one type 1 order**, so we only return the type 0 order.  
- **Customer 4** has **only type 1 orders**, so we return both.  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea:**  
- **Identify** customers who have at least one type 0 order.
- **Filter out** type 1 orders for these customers.
- **Keep all orders** for customers who do not have any type 0 orders.

### 🛠 **Implementation Details**
1. **Use `groupby("customer_id")["order_type"].transform("min")`**  
   - This ensures that for each customer, we get the **minimum order type (0 or 1)**.
   - If the minimum order type is **0**, we know the customer has at least one type 0 order.
  
2. **Use `.query("order_type == has_zero")`**  
   - Retains orders **only** where `order_type` is the same as the customer's minimum order type.
   - This effectively **removes type 1 orders** for customers with at least one type 0 order.

## 📝 **Implementation**  

```python
import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Filters out Type 1 orders for customers who have at least one Type 0 order.

    :param orders: DataFrame containing order_id, customer_id, and order_type.
    :return: DataFrame with filtered orders.
    """

    return (
        orders
        .assign(has_zero = lambda x: x.groupby("customer_id")["order_type"].transform("min"))
        .query("order_type == has_zero")
        [["order_id", "customer_id", "order_type"]]
    )

```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| Grouping customers | **O(N)** |
| Filtering rows | **O(N)** |
| **Overall Complexity** | **O(N)** ✅ |

🔹 **Why is this efficient?**  
- The algorithm **visits each row only once**, ensuring linear time complexity.
- **Vectorised operations** in Pandas make it faster than explicit loops.

## 📂 **Project Structure**  

```
order_types/
├── order_types.py  # Python solution
├── README.md       # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `groupby()` to efficiently check for type 0 orders.**  
✔ **Applies `.query()` for a clean filtering step.**  
✔ **Achieves O(N) complexity with an efficient Pandas approach.**  

🚀 **Master this pattern for filtering grouped data!** 🔥  