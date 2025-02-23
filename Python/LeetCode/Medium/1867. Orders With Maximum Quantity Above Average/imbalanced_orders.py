import pandas as pd

def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies imbalanced orders where the maximum quantity of a product 
    in an order is strictly greater than the average quantity of all orders.

    Args:
        orders_details (pd.DataFrame): Contains order data with columns:
            - "order_id" (int): The ID of the order.
            - "product_id" (int): The ID of the product.
            - "quantity" (int): The quantity ordered for that product.

    Returns:
        pd.DataFrame: A table containing:
            - "order_id" (int): The IDs of imbalanced orders.
        
        The result can be returned in any order.
    """

    # Aggregate per order: total quantity, max quantity, and unique product count
    df = (
        orders_details
        .groupby("order_id")
        .agg(
            total_quantity=("quantity", "sum"),
            max_quantity=("quantity", "max"),
            unique_products=("product_id", "nunique")
        )
        .reset_index()
    )

    # Compute the average quantity per order
    df["avg"] = df["total_quantity"] / df["unique_products"]

    # Determine the maximum average quantity across all orders
    max_avg = df["avg"].max()

    # Filter orders where the max quantity exceeds max_avg
    return df[df["max_quantity"] > max_avg][["order_id"]]


if __name__ == "__main__":
    # Example usage
    orders_details_data = pd.DataFrame({
        "order_id": [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5],
        "product_id": [1, 2, 3, 4, 5, 6, 7, 5, 6, 7, 8, 9, 9, 9],
        "quantity": [12, 10, 15, 8, 4, 6, 4, 15, 18, 20, 2, 8, 9, 9]
    })

    print(orders_above_average(orders_details_data))
