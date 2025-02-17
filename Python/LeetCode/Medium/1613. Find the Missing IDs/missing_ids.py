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


def main():
    """ Example execution of the find_missing_ids function. """
    
    # Example input data
    customer_data = {
        "customer_id": [1, 4, 5],                    
        "customer_name": ["Alice", "Bob", "Charlie"]
    }

    # Create DataFrame
    customers_df = pd.DataFrame(customer_data)

    # Find missing IDs
    missing_ids_df = find_missing_ids(customers_df)

    # Display the result
    print(missing_ids_df)


if __name__ == "__main__":
    main()
