# 📚 **LeetCode 1098: Unpopular Books**  

## 📌 **Problem Overview**  
You are given two tables:  

1. **`Books` Table**: Contains details about books, including their **availability date**.  
2. **`Orders` Table**: Contains order information, including the **number of copies sold** and their dispatch dates.  

### **Goal**  
Identify **unpopular books** that:  
✔ **Sold fewer than 10 copies in the last year** (from **2018-06-23** to **2019-06-23**).  
✔ **Have been available for at least a month** (published **before 2019-05-23**).  
✔ **Exclude books available for less than one month** from today (**2019-06-23**).  

## 📊 **Database Schema**  
### **Books Table**  
| Column Name      | Type  | Description                                    |
|-----------------|------|------------------------------------------------|
| `book_id`       | int  | Unique book ID                                |
| `name`          | varchar | Name of the book                           |
| `available_from`| date  | Date the book became available for sale     |

### **Orders Table**  
| Column Name     | Type  | Description                                      |
|---------------|------|--------------------------------------------------|
| `order_id`   | int  | Unique order ID                                 |
| `book_id`    | int  | Foreign key linking to `Books.book_id`         |
| `quantity`   | int  | Number of copies sold in that order             |
| `dispatch_date`| date  | Date the book was dispatched to the customer  |

## 🛠 **Approach**  
1. **Filter Books Published At Least a Month Ago**  
   - Only consider books available before **2019-05-23**.  

2. **Filter Orders Placed in the Last Year**  
   - Only consider orders with `dispatch_date > 2018-06-23`.  

3. **Compute Total Sales Per Book**  
   - Group by `book_id` and `name`, then sum `quantity`.  

4. **Find Books with Less Than 10 Sales**  
   - Extract books where `total_quantity < 10`.  

## 🚀 **Python Solution**  
```python
import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies unpopular books that sold less than 10 copies in the last year,
    excluding books available for less than one month from today (2019-06-23).

    Args:
        books (pd.DataFrame): Contains book details with 'book_id', 'name', and 'available_from'.
        orders (pd.DataFrame): Contains order details with 'book_id', 'quantity', and 'dispatch_date'.

    Returns:
        pd.DataFrame: A DataFrame with ['book_id', 'name'] of unpopular books.
    """
    # Filter books available for at least one month (before 2019-05-23)
    recent_books = books[books["available_from"] < "2019-05-23"]

    # Filter orders placed in the last year (after 2018-06-23)
    recent_orders = orders[orders["dispatch_date"] > "2018-06-23"]

    # Merge books with relevant orders and calculate total quantity sold
    sales_summary = (
        pd.merge(recent_books, recent_orders, on="book_id", how="left")
        .groupby(["book_id", "name"], as_index=False)
        .agg(total_quantity=("quantity", "sum"))
    )

    # Filter books that sold less than 10 copies
    unpopular_books = sales_summary.query("total_quantity < 10")[["book_id", "name"]]

    return unpopular_books
```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Books Table**  
| book_id | name       | available_from |
|---------|------------|---------------|
| 1       | "Book A"   | 2019-01-01    |
| 2       | "Book B"   | 2019-04-15    |
| 3       | "Book C"   | 2019-05-25    |
| 4       | "Book D"   | 2018-06-10    |

#### **Orders Table**  
| order_id | book_id | quantity | dispatch_date |
|---------|--------|----------|--------------|
| 101     | 1      | 4        | 2018-07-01   |
| 102     | 1      | 3        | 2019-01-15   |
| 103     | 2      | 5        | 2019-02-20   |
| 104     | 3      | 8        | 2019-06-01   |
| 105     | 4      | 2        | 2018-07-10   |

---

### **Output**  
```python
   book_id    name
0        4    "Book D"
```

### **Explanation**  
- **Book A**: **Sold 7 copies** (4+3) → **Not Unpopular**  
- **Book B**: **Sold 5 copies** → **Considered Unpopular**  
- **Book C**: **Not considered** (Available after 2019-05-23)  
- **Book D**: **Sold 2 copies** → **Considered Unpopular**  

Only **"Book D"** meets all conditions.

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Filter books | `books[books["available_from"] < "2019-05-23"]` | **O(N)** |
| Filter orders | `orders[orders["dispatch_date"] > "2018-06-23"]` | **O(M)** |
| Merge datasets | `merge(books, orders, on="book_id", how="left")` | **O(N + M)** |
| Group by book_id | `groupby(["book_id", "name"])` | **O(N)** |
| Filter results | `query("total_quantity < 10")` | **O(N)** |
| **Total Complexity** | **O(N + M)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Handles missing sales data correctly** using `how="left"`.  
✔ **Ensures only books available for at least a month are considered**.  
✔ **Efficient filtering using vectorised Pandas operations**.  

🚀 **This approach efficiently identifies books that are struggling in sales!** 📚