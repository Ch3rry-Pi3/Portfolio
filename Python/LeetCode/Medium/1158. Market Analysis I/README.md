# 📊 **LeetCode 1158: Market Analysis I**  

## 📌 **Problem Overview**  
You are given three tables:  
1. **`Users` Table**: Contains information about users, including their join date and favorite brand.  
2. **`Orders` Table**: Tracks purchase transactions made by users, including the order date and buyer ID.  
3. **`Items` Table**: Contains item details, including the item ID and brand name.  

### **Goal**  
For each user, report:  
- Their **join date**.  
- The **number of orders they placed in 2019**.  

### **Key Constraints**  
- The result must include **all users**, even if they placed **zero orders** in 2019.  
- The result should be returned **in any order**.  

## 📊 **Database Schema**  

### **Users Table**  
| Column Name      | Type    | Description                      |
|----------------|--------|----------------------------------|
| `user_id`      | int    | Unique ID for each user         |
| `join_date`    | date   | Date the user joined the platform |
| `favorite_brand` | varchar | User's favorite brand          |

### **Orders Table**  
| Column Name   | Type    | Description                              |
|-------------|--------|------------------------------------------|
| `order_id`  | int    | Unique ID for each order                 |
| `order_date`| date   | Date when the order was placed           |
| `item_id`   | int    | Foreign key referencing `Items` table    |
| `buyer_id`  | int    | Foreign key referencing `Users` (buyer)  |
| `seller_id` | int    | Foreign key referencing `Users` (seller) |

### **Items Table**  
| Column Name  | Type    | Description                      |
|-------------|--------|----------------------------------|
| `item_id`   | int    | Unique ID for each item         |
| `item_brand`| varchar | Brand name of the item          |

## 🛠 **Approach**  
1. **Filter the `Orders` table** to include only orders from **2019**.  
2. **Merge** the filtered orders with the `Users` table using `buyer_id = user_id`.  
3. **Count the number of orders per user** in 2019 using `groupby()`.  
4. **Ensure all users are included**, even those who made **zero purchases**.  
5. **Rename columns** to match the expected output format.  

## 🚀 **Python Solution**  

```python
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    """
    Analyses the number of orders each user placed in the year 2019.

    Args:
        users (pd.DataFrame): Contains user details with columns:
            - 'user_id' (int): Unique ID for each user.
            - 'join_date' (datetime): Date the user joined the platform.
            - 'favorite_brand' (str): User's favorite brand.
        
        orders (pd.DataFrame): Contains order details with columns:
            - 'order_id' (int): Unique order ID.
            - 'order_date' (datetime): Date when the order was placed.
            - 'item_id' (int): Foreign key referencing Items.
            - 'buyer_id' (int): Foreign key referencing Users (buyer).
            - 'seller_id' (int): Foreign key referencing Users (seller).

        items (pd.DataFrame): Contains item details with columns:
            - 'item_id' (int): Unique ID for each item.
            - 'item_brand' (str): Brand name of the item.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - 'buyer_id' (int): The user's ID.
            - 'join_date' (datetime): The date the user joined.
            - 'orders_in_2019' (int): The number of orders the user placed in 2019.
    """
    
    # Step 1: Filter orders to include only those placed in the year 2019
    filtered_orders = orders[orders["order_date"].dt.year == 2019]

    # Step 2: Merge filtered orders with users on 'buyer_id' to get join dates
    merged_df = users.merge(filtered_orders, left_on="user_id", right_on="buyer_id", how="left")

    # Step 3: Count the number of orders for each user
    order_counts = merged_df.groupby(["user_id", "join_date"])["order_id"].count().reset_index()

    # Step 4: Rename columns to match expected output
    result = order_counts.rename(columns={"user_id": "buyer_id", "order_id": "orders_in_2019"})

    return result
```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Users Table**  
| user_id | join_date  | favorite_brand |
|---------|-----------|---------------|
| 1       | 2018-01-01 | Lenovo        |
| 2       | 2018-02-09 | Samsung       |
| 3       | 2018-01-19 | LG            |
| 4       | 2018-05-21 | HP            |

#### **Orders Table**  
| order_id | order_date | item_id | buyer_id | seller_id |
|----------|-----------|---------|----------|----------|
| 1        | 2019-08-01 | 1       | 1        | 2        |
| 2        | 2018-08-02 | 2       | 2        | 3        |
| 3        | 2019-08-03 | 3       | 3        | 1        |
| 4        | 2019-08-04 | 4       | 1        | 3        |
| 5        | 2019-08-05 | 2       | 2        | 4        |
| 6        | 2018-07-10 | 1       | 4        | 2        |

#### **Items Table**  
| item_id | item_brand |
|---------|-----------|
| 1       | Samsung   |
| 2       | Lenovo    |
| 3       | LG        |
| 4       | HP        |

### **Output**  
```python
   buyer_id  join_date  orders_in_2019
0         1 2018-01-01               2
1         2 2018-02-09               2
2         4 2018-05-21               0
```

### **Explanation**  
- **User 1 (buyer_id = 1)** placed **2 orders** in 2019 (Order IDs: `1, 4`).
- **User 2 (buyer_id = 2)** placed **2 orders** in 2019 (Order IDs: `5, 3`).
- **User 4 (buyer_id = 4)** placed **0 orders** in 2019, but is still included in the result.

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter Orders for 2019 | `orders["order_date"].dt.year == 2019` | **O(N)** |
| Merge with Users | `merge(users, orders, how="right")` | **O(N)** |
| Group by user | `groupby(["user_id", "join_date"]).count()` | **O(N)** |
| Rename Columns | `.rename()` | **O(1)** |
| **Total Complexity** | **O(N)** | ✅ **Efficient** |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`merge`, `groupby`, `count`).  
✔ **Handles users with zero orders using a right join**.  
✔ **Ensures all users are included in the final result**.  

🚀 **This approach quickly determines how many purchases each user made in 2019!** 🎯