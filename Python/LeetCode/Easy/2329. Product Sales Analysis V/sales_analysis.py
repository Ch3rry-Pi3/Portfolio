import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes total spending per user based on sales transactions and product prices.

    Args:
        sales (pd.DataFrame): DataFrame containing sales data with 'product_id', 'user_id', and 'quantity'.
        product (pd.DataFrame): DataFrame containing product data with 'product_id' and 'price'.

    Returns:
        pd.DataFrame: A DataFrame containing 'user_id' and 'spending', sorted by spending (descending) and user_id (ascending).
    """
    return (
        sales.merge(product, on="product_id")
        .assign(spending=lambda df: df["quantity"] * df["price"])
        .groupby("user_id", as_index=False)["spending"]
        .sum()
        .sort_values(by=["spending", "user_id"], ascending=[False, True])
    )

def main():
    # Sample data
    sales_data = {
        "sale_id": [1, 2, 3, 4, 5],
        "product_id": [1, 1, 2, 2, 3],
        "user_id": [101, 102, 102, 103, 101],
        "quantity": [10, 1, 3, 2, 3]
    }

    product_data = {
        "product_id": [1, 2, 3],
        "price": [10, 25, 15]
    }

    # Create DataFrames
    sales_df = pd.DataFrame(sales_data)
    product_df = pd.DataFrame(product_data)

    # Run analysis
    result = product_sales_analysis(sales_df, product_df)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
