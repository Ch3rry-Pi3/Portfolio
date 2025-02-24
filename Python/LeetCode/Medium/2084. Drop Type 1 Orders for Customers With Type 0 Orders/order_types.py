import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Filters orders to remove type 1 orders for customers who have at least one type 0 order.
    
    :param orders: DataFrame containing order_id, customer_id, and order_type.
    :return: Filtered DataFrame with appropriate orders retained.
    """
    filtered_orders = (
        orders
        .assign(has_zero=lambda x: x.groupby("customer_id")["order_type"].transform("min"))
        .query("order_type == has_zero")
        [["order_id", "customer_id", "order_type"]]
    )
    
    return filtered_orders

def main():
    """
    Main function to demonstrate filtering logic.
    """
    # Example dataset
    data = {
        "order_id": [1, 2, 11, 12, 21, 22, 31, 32],
        "customer_id": [1, 1, 2, 2, 3, 3, 4, 4],
        "order_type": [0, 0, 1, 0, 1, 0, 1, 1],
    }
    
    orders_df = pd.DataFrame(data)
    result = drop_specific_orders(orders_df)
    
    print("Filtered Orders:")
    print(result)

if __name__ == "__main__":
    main()
