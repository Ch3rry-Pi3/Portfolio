# 📦 **LeetCode 2292: Products With Three or More Orders in Two Consecutive Years**  

## 📌 **Problem Overview**  
Given an **Orders** table, determine which products were ordered **three or more times in two consecutive years**.

- **Orders Table**  
  - **Columns**: `order_id`, `product_id`, `quantity`, `purchase_date`
  - Each row represents a product purchase.  

### **Goal**  
Output a table containing:
- `product_id` (the ID of the product that meets the condition).

### **Example**  
**Input**:  
```
Orders Table
------------
order_id | product_id | quantity | purchase_date
1        |    1      |    7     | 2020-03-16
2        |    1      |    4     | 2021-02-02
3        |    1      |    6     | 2020-05-10
4        |    1      |    6     | 2021-12-23
5        |    2      |    6     | 2021-05-21
6        |    2      |    5     | 2021-10-11
7        |    2      |    6     | 2022-10-11
```

**Output**:  
```
product_id
----------
    1
```

✅ **Explanation**:  
- **Product 1** was ordered **3 times in 2020** and **3 times in 2021** → ✅ **Meets criteria**  
- **Product 2** was ordered **3 times in 2021** but only **once in 2022** → ❌ **Does not meet criteria**  

## 🚀 **Approach & Intuition**  

### 🔹 **Key Steps**  
1. **Extract Year** from `purchase_date` to analyse yearly order trends.  
2. **Group by `product_id` and `year`**, counting the number of orders for each product per year.  
3. **Filter** products with **three or more orders in a single year**.  
4. **Compare consecutive years**:
   - Use `shift(1)` within each `product_id` group to get the previous year.
   - Compute the **year difference**.
   - Keep products where the difference is exactly **1 year** (consecutive).  

This method ensures we efficiently check for products meeting the **"three orders in consecutive years"** rule.

## 📝 **Implementation**  

```python
# three_or_more_orders.py

import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies products that were ordered at least three times in two consecutive years.

    Args:
        orders (pd.DataFrame): Contains order data with columns:
            - "order_id" (int): Unique order identifier.
            - "product_id" (int): The ID of the product purchased.
            - "quantity" (int): The quantity of the product ordered.
            - "purchase_date" (datetime): The date the order was placed.

    Returns:
        pd.DataFrame: A table with:
            - "product_id" (int): The ID of the product(s) that were ordered three or more times
              in two consecutive years.
    """
    # Extract the year from the purchase_date
    orders = orders.assign(year=orders['purchase_date'].dt.year)

    # Count the number of orders per product per year
    yearly_counts = (
        orders.groupby(['product_id', 'year'])
        .size()
        .reset_index(name='cnt')
    )

    # Filter products that had at least 3 orders in a given year
    valid_years = yearly_counts[yearly_counts['cnt'] >= 3]

    # Identify previous order year for each product
    valid_years = valid_years.assign(
        prev_order_year=valid_years.groupby('product_id')['year'].shift(1)
    )

    # Calculate the difference between consecutive years
    valid_years = valid_years.assign(
        year_diff=valid_years['year'] - valid_years['prev_order_year']
    )

    # Filter products where the difference is exactly 1 year (consecutive years)
    result = valid_years[valid_years['year_diff'] == 1][['product_id']].drop_duplicates()

    return result


if __name__ == "__main__":
    # Example usage
    orders_data = pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5, 6, 7],
        "product_id": [1, 1, 1, 1, 2, 2, 2],
        "quantity": [7, 4, 6, 6, 6, 5, 6],
        "purchase_date": pd.to_datetime([
            "2020-03-16", "2021-02-02", "2020-05-10", "2021-12-23",
            "2021-05-21", "2021-10-11", "2022-10-11"
        ])
    })

    print(find_valid_products(orders_data))
```

## ⏳ **Time Complexity Analysis**  

| Operation                             | Complexity |
|---------------------------------------|------------|
| Extracting year from `purchase_date`  | **O(n)** |
| Grouping and counting orders          | **O(n)** |
| Filtering valid years                 | **O(n)** |
| Shift operation (previous year lookup)| **O(n)** |
| Final filtering & selection           | **O(n)** |
| **Overall Complexity**                | **O(n)** ✅ |

> Here, **n** is the number of rows in the `orders` table.  

## 📂 **Project Structure**  

```
2292. Products With Three or More Orders in Two Consecutive Years/
├── three_or_more_orders.py  # Python solution
├── README.md                # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Leverages Pandas `groupby` and `shift`** for efficient year-based filtering.  
✔ **Uses `size()` aggregation** to count orders per product-year efficiently.  
✔ **Handles consecutive year detection** using `shift(1)`.  

🚀 **Understanding this approach will help solve similar time-based aggregation problems efficiently!** 🔥