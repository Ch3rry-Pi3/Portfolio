# 📊 **LeetCode 1364: Number of Trusted Contacts of a Customer**  

## 📌 **Problem Overview**  
You are given three tables:  
1. **`Customers` Table**: Contains customer details such as `customer_id`, `customer_name`, and `email`.  
2. **`Contacts` Table**: Stores contact relationships between customers and their trusted contacts (`user_id`, `contact_email`).  
3. **`Invoices` Table**: Records invoices related to each `user_id` and their corresponding `price`.  

### **Goal**  
For each **invoice (`invoice_id`)**, determine:  
- **Customer Name**: The name of the customer related to the invoice.  
- **Price**: The price of the invoice.  
- **Contacts Count (`contacts_cnt`)**: The total number of contacts the customer has.  
- **Trusted Contacts Count (`trusted_contacts_cnt`)**: The number of contacts who are also customers (i.e., their email exists in the `Customers` table).  

The result should be **ordered by `invoice_id`** in ascending order.  

## 📊 **Database Schema**  

### **Customers Table**  
| Column Name    | Type    | Description                         |
|---------------|--------|-------------------------------------|
| `customer_id` | int    | Unique ID for the customer         |
| `customer_name` | varchar | Name of the customer               |
| `email`       | varchar | Email of the customer              |

### **Contacts Table**  
| Column Name     | Type    | Description                             |
|----------------|--------|-----------------------------------------|
| `user_id`      | int    | ID of the customer having a contact     |
| `contact_name` | varchar | Name of the contact                     |
| `contact_email` | varchar | Email of the contact                    |

### **Invoices Table**  
| Column Name  | Type    | Description                   |
|-------------|--------|-------------------------------|
| `invoice_id` | int    | Unique invoice ID            |
| `price`      | int    | Price of the invoice         |
| `user_id`    | int    | ID of the customer related to the invoice |

## 🛠 **Approach**  

1. **Find Total Contacts per User (`contacts_cnt`)**  
   - Merge `Contacts` with `Customers` to check if a contact exists in the customers' database.  
   - Count **total contacts** and **trusted contacts** for each `user_id`.  

2. **Merge the above data with Invoices**  
   - Merge the `Invoices` table with `Customers` to get `customer_name`.  
   - Merge again with the `contacts` data to get the total and trusted contact counts.  

3. **Format and Order the Results**  
   - Select columns `invoice_id`, `customer_name`, `price`, `contacts_cnt`, and `trusted_contacts_cnt`.  
   - Order results by `invoice_id` in ascending order.  

## 🚀 **Python Solution**  

```python
import pandas as pd

def count_trusted_contacts(
    customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes the total number of contacts and trusted contacts for each invoice.

    Args:
        customers (pd.DataFrame): Contains customer details with 'customer_id', 'customer_name', and 'email'.
        contacts (pd.DataFrame): Contains contact relationships with 'user_id' and 'contact_email'.
        invoices (pd.DataFrame): Contains invoice details with 'invoice_id', 'price', and 'user_id'.

    Returns:
        pd.DataFrame: A DataFrame containing:
            - "invoice_id" (int): Unique invoice ID.
            - "customer_name" (str): Name of the customer related to the invoice.
            - "price" (int): Price of the invoice.
            - "contacts_cnt" (int): Total number of contacts.
            - "trusted_contacts_cnt" (int): Contacts who are also customers.
    """

    # Step 1: Count contacts and trusted contacts per user
    contact_customer = (
        pd.merge(
            contacts, customers, left_on="contact_email", right_on="email", how="left"
        )
        .groupby("user_id", as_index=False)
        .agg(contacts_cnt=("user_id", "count"), trusted_contacts_cnt=("email", "count"))
    )

    # Step 2: Merge invoices with customers to get customer names
    invoice_customer = (
        pd.merge(
            pd.merge(
                invoices,
                customers,
                left_on="user_id",
                right_on="customer_id",
                how="left",
            ),
            contact_customer,
            on="user_id",
            how="left",
        )
        .fillna(0)  # Fill missing values for contacts/trusted contacts with 0
        .sort_values("invoice_id")          # Sort by invoice ID
    )

    # Step 3: Select relevant columns and return result
    return invoice_customer[
        ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"]
    ]
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Customers Table**  
| customer_id | customer_name | email               |
|------------|--------------|---------------------|
| 1          | Alice        | alice@leetcode.com |
| 2          | Bob          | bob@leetcode.com   |
| 3          | John         | john@leetcode.com  |
| 6          | Alex         | alex@leetcode.com  |

#### **Contacts Table**  
| user_id | contact_name | contact_email       |
|---------|-------------|---------------------|
| 1       | Bob         | bob@leetcode.com   |
| 1       | John        | john@leetcode.com  |
| 1       | Jal        | jal@leetcode.com   |
| 2       | Omar        | omar@leetcode.com  |
| 2       | Meir        | meir@leetcode.com  |
| 6       | Alice       | alice@leetcode.com |

#### **Invoices Table**  
| invoice_id | price | user_id |
|------------|-------|---------|
| 77         | 100   | 1       |
| 55         | 500   | 3       |
| 66         | 400   | 2       |
| 77         | 100   | 1       |
| 88         | 200   | 1       |
| 99         | 300   | 2       |

### **Output**  
```python
   invoice_id customer_name  price  contacts_cnt  trusted_contacts_cnt
0          44         Alex     60             1                    1
1          55         John    500             0                    0
2          66          Bob    400             2                    0
3          77        Alice    100             3                    2
4          88        Alice    200             3                    2
5          99          Bob    300             2                    0
```

### **Explanation**  
- **Alice** has **3** contacts:  
  - **Trusted Contacts (2)**: Bob & John (exist in `Customers` table).  
  - **Total Contacts (3)**: Bob, John, and Jal.  
- **Bob** has **2** contacts, but **none are trusted contacts**.  
- **Alex** has **1** contact, and **it is trusted (Alice)**.  
- **John has no contacts**.  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Merge contacts with customers | `merge(contacts, customers, on='contact_email')` | **O(N)** |
| Group by user ID | `groupby("user_id").agg()` | **O(N)** |
| Merge invoices with customers | `merge(invoices, customers, on='customer_id')` | **O(N)** |
| Merge invoices with contact counts | `merge(invoice_customer, contact_customer, on="user_id")` | **O(N)** |
| Sort by `invoice_id` | `sort_values("invoice_id")` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`merge`, `groupby`, `sort_values`).  
✔ **Ensures all invoices are considered, even if a customer has no contacts**.  
✔ **Handles large datasets effectively with vectorised operations**.  

🚀 **With this approach, you can efficiently determine trusted contact relationships for any invoice dataset!** 🎯