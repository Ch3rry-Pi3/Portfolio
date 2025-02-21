import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the product(s) on which each user spent the most money.

    Args:
        sales (pd.DataFrame): Contains sales data with columns:
            - "sale_id" (int): Unique sale identifier.
            - "product_id" (int): The ID of the product sold.
            - "user_id" (int): The ID of the user who purchased.
            - "quantity" (int): The quantity purchased by the user.
        product (pd.DataFrame): Contains product data with columns:
            - "product_id" (int): Unique product identifier.
            - "price" (int): Price of the product.

    Returns:
        pd.DataFrame: A table with:
            - "user_id" (int): The ID of the user.
            - "product_id" (int): The ID(s) of the product(s) on which the user spent the most.
              If a user spent the same maximum amount on multiple products, all such products
              will be returned.
    """
    # Merge sales data with product data to get prices
    merged = pd.merge(left=sales, right=product, on="product_id", how="left")

    # Calculate revenue = quantity * price, then group by user and product
    df = (
        merged
        .assign(revenue=lambda x: x["quantity"] * x["price"])
        .groupby(["user_id", "product_id"], as_index=False)
        .agg(product_revenue=("revenue", "sum"))
        # Rank products by revenue for each user (dense rank)
        .assign(
            rnk=lambda x: x.groupby("user_id")["product_revenue"]
            .rank(method="dense", ascending=False)
        )
        # Filter to only include rows where rank == 1 (maximum spending)
        .query("rnk == 1")
        # Return the desired columns
        [["user_id", "product_id"]]
    )

    return df


if __name__ == "__main__":
    # Example usage
    sales_data = pd.DataFrame({
        "sale_id": [1, 2, 3, 4, 5],
        "product_id": [1, 3, 3, 1, 2],
        "user_id": [101, 101, 102, 102, 102],
        "quantity": [10, 5, 6, 10, 25]
    })

    product_data = pd.DataFrame({
        "product_id": [1, 2, 3],
        "price": [10, 25, 30]
    })

    print(product_sales_analysis(sales_data, product_data))
