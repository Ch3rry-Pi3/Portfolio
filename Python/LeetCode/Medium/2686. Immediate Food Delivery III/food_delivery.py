import pandas as pd
import numpy as np

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the percentage of immediate food deliveries for each order date.

    An order is considered immediate if the customer's preferred delivery date
    matches the order date.

    Args:
        delivery (pd.DataFrame): A DataFrame containing delivery order details with columns:
                                 - "delivery_id" (int): Unique ID for the delivery.
                                 - "customer_id" (int): Customer placing the order.
                                 - "order_date" (date): Date when the order was placed.
                                 - "customer_pref_delivery_date" (date): Preferred delivery date.

    Returns:
        pd.DataFrame: A DataFrame with columns:
                      - "order_date" (date): The date when orders were placed.
                      - "immediate_percentage" (float): Percentage of immediate deliveries
                        for that date, rounded to two decimal places.
    """

    return (
        delivery
        .assign(immediate=lambda x: np.where(x["order_date"] == x["customer_pref_delivery_date"], 1, 0))
        .groupby("order_date", as_index=False)
        .agg(immediate_percentage=("immediate", "mean"))
        .assign(immediate_percentage=lambda x: round(x["immediate_percentage"] * 100, 2))
        .sort_values(by="order_date", ascending=True)
    )


if __name__ == "__main__":
    # Example data
    data = {
        "delivery_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "customer_id": [1, 1, 1, 3, 3, 2, 2, 4, 4, 1],
        "order_date": pd.to_datetime([
            "2019-08-01", "2019-08-01", "2019-08-01",
            "2019-08-02", "2019-08-02", "2019-08-03",
            "2019-08-03", "2019-08-04", "2019-08-04",
            "2019-08-04"
        ]),
        "customer_pref_delivery_date": pd.to_datetime([
            "2019-08-01", "2019-08-01", "2019-08-02",
            "2019-08-02", "2019-08-03", "2019-08-03",
            "2019-08-03", "2019-08-04", "2019-08-05",
            "2019-08-06"
        ]),
    }

    df = pd.DataFrame(data)

    # Compute immediate delivery percentages
    result = immediate_delivery(df)

    # Display result
    print(result)
