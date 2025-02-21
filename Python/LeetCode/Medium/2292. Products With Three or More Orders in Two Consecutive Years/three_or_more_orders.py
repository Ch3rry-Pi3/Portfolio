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
