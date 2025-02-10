import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of unique orders and unique customers with invoices greater than $20
    for each different month.

    Args:
        orders (pd.DataFrame): A DataFrame containing order details with columns:
            - order_id (int): Unique identifier for each order.
            - order_date (datetime): Date when the order was placed.
            - customer_id (int): Identifier for the customer who placed the order.
            - invoice (int): Invoice amount for the order.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - month (str): The month in "YYYY-MM" format.
            - order_count (int): Count of unique orders for that month.
            - customer_count (int): Count of unique customers with invoices > $20 for that month.
    """
    # Filter orders with invoice greater than 20
    filtered_orders = orders.loc[orders["invoice"] > 20].copy()
    
    # Extract the month in "YYYY-MM" format
    filtered_orders["month"] = filtered_orders["order_date"].dt.strftime("%Y-%m")
    
    # Aggregate the data: count unique order IDs and customer IDs per month
    result = (
        filtered_orders.groupby("month", as_index=False)
        .agg(order_count=("order_id", "nunique"), customer_count=("customer_id", "nunique"))
    )
    
    return result

def main():
    """Runs example test cases for unique_orders_and_customers function."""
    data = {
        "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "order_date": pd.to_datetime([
            "2020-09-15", "2020-09-17", "2020-10-06", "2020-10-10", "2020-11-20",
            "2020-11-21", "2020-12-01", "2020-12-03", "2021-01-07", "2021-01-15"
        ]),
        "customer_id": [1, 1, 3, 1, 2, 2, 4, 4, 3, 2],
        "invoice": [30, 90, 20, 21, 10, 15, 55, 77, 31, 20]
    }
    
    orders = pd.DataFrame(data)
    result = unique_orders_and_customers(orders)
    print(result)

if __name__ == "__main__":
    main()
