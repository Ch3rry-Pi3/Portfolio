import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average number of items per order, rounded to 2 decimal places.

    Parameters:
    orders (pd.DataFrame): A DataFrame containing order information with columns:
                           - 'order_id' (int): Unique identifier for each order.
                           - 'item_count' (int): Number of items in the order.
                           - 'order_occurrences' (int): Number of times this order occurred.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'average_items_per_order' (float): The computed average items per order.
    """
    # Compute the weighted sum of items across all occurrences
    total_items = (orders["item_count"] * orders["order_occurrences"]).sum()

    # Compute the total number of orders
    total_orders = orders["order_occurrences"].sum()

    # Calculate the compressed mean, rounding to 2 decimal places
    avg_items_per_order = round(total_items / total_orders, 2)

    # Return as a DataFrame
    return pd.DataFrame({"average_items_per_order": [avg_items_per_order]})


def main():
    """
    Main function to demonstrate the compressed_mean function with a sample dataset.
    """
    # Sample orders data
    orders_data = {
        "order_id": [1, 10, 12, 13],
        "item_count": [1, 2, 3, 4],
        "order_occurrences": [500, 1000, 800, 1000]
    }

    # Convert dictionary to DataFrame
    orders_df = pd.DataFrame(orders_data)

    # Compute the compressed mean
    result = compressed_mean(orders_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
