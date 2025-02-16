import pandas as pd

def count_trusted_contacts(
    customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame
) -> pd.DataFrame:
    """
    Computes the number of contacts and trusted contacts for each customer
    and returns the invoice details with the corresponding counts.

    Args:
        customers (pd.DataFrame): A DataFrame containing customer details.
        contacts (pd.DataFrame): A DataFrame containing customer contacts.
        invoices (pd.DataFrame): A DataFrame containing invoice details.

    Returns:
        pd.DataFrame: A DataFrame containing invoice details with the number of contacts
                      and trusted contacts, sorted by "invoice_id".
    """

    # Step 1: Merge contacts with customers to identify trusted contacts
    contact_customer = (
        pd.merge(
            contacts, customers, left_on="contact_email", right_on="email", how="left"
        )
        .groupby("user_id", as_index=False)
        .agg(contacts_cnt=("user_id", "count"), trusted_contacts_cnt=("email", "count"))
    )

    # Step 2: Merge invoices with customers and then with the contact_customer DataFrame
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
        .fillna(0)  # Fill missing values with 0 for customers without contacts
        .sort_values("invoice_id")  # Sort by invoice ID
    )

    # Step 3: Select and return the relevant columns
    return invoice_customer[
        ["invoice_id", "customer_name", "price", "contacts_cnt", "trusted_contacts_cnt"]
    ]

def main():
    # Example data
    customers_data = {
        "customer_id": [1, 2, 3, 6],
        "customer_name": ["Alice", "Bob", "John", "Alex"],
        "email": ["alice@leetcode.com", "bob@leetcode.com", "john@leetcode.com", "alex@leetcode.com"]
    }
    
    contacts_data = {
        "user_id": [1, 1, 1, 2, 2, 6],
        "contact_name": ["Bob", "John", "Jal", "Omar", "Meir", "Alice"],
        "contact_email": ["bob@leetcode.com", "john@leetcode.com", "jal@leetcode.com",
                          "omar@leetcode.com", "meir@leetcode.com", "alice@leetcode.com"]
    }
    
    invoices_data = {
        "invoice_id": [77, 55, 66, 77, 88, 99],
        "price": [100, 500, 400, 100, 200, 300],
        "user_id": [1, 3, 2, 1, 1, 2]
    }

    # Convert dictionaries to pandas DataFrames
    customers_df = pd.DataFrame(customers_data)
    contacts_df = pd.DataFrame(contacts_data)
    invoices_df = pd.DataFrame(invoices_data)

    # Run the function
    result = count_trusted_contacts(customers_df, contacts_df, invoices_df)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
