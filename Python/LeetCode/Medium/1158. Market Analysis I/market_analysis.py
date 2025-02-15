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

def main():
    # Sample data for testing
    users_data = {
        "user_id": [1, 2, 3, 4],
        "join_date": pd.to_datetime(["2018-01-01", "2018-02-09", "2018-01-19", "2018-05-21"]),
        "favorite_brand": ["Lenovo", "Samsung", "LG", "HP"]
    }
    orders_data = {
        "order_id": [1, 2, 3, 4, 5, 6],
        "order_date": pd.to_datetime(["2019-08-01", "2018-08-02", "2019-08-03", "2019-08-04", "2019-08-05", "2018-07-10"]),
        "item_id": [1, 2, 3, 4, 2, 1],
        "buyer_id": [1, 2, 3, 1, 2, 4],
        "seller_id": [2, 3, 1, 3, 4, 2]
    }
    items_data = {
        "item_id": [1, 2, 3, 4],
        "item_brand": ["Samsung", "Lenovo", "LG", "HP"]
    }

    # Convert dictionaries to DataFrames
    users_df = pd.DataFrame(users_data)
    orders_df = pd.DataFrame(orders_data)
    items_df = pd.DataFrame(items_data)

    # Run the function and display the result
    result_df = market_analysis(users_df, orders_df, items_df)
    print(result_df)

if __name__ == "__main__":
    main()
