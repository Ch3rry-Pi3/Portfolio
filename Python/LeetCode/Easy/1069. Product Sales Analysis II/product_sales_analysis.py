import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total quantity sold for each product.

    The function merges the sales data with the product details and 
    calculates the total quantity sold per product.

    :param sales: DataFrame containing sales records (product_id, quantity, etc.).
    :param product: DataFrame containing product details (product_id, product_name).
    :return: DataFrame with each product's total quantity sold.
    """

    return (
        sales.merge(product, on="product_id", how="left")               # Merge product details into sales data
        .groupby("product_id", as_index=False)["quantity"].sum()        # Aggregate quantity sold per product
        .rename(columns={"quantity": "total_quantity"})                 # Rename column for clarity
    )


def main():
    """
    Demonstrates testing the sales_analysis function with sample datasets.
    """
    # Example Sales Data
    sales_data = {
        "sale_id": [1, 2, 3],
        "product_id": [100, 100, 200],
        "year": [2008, 2008, 2011],
        "quantity": [10, 15, 15],
        "price": [5000, 5000, 9000]
    }

    # Example Product Data
    product_data = {
        "product_id": [100, 200, 300],
        "product_name": ["Nokia", "Apple", "Samsung"]
    }

    # Convert dictionaries to DataFrames
    sales_df = pd.DataFrame(sales_data)
    product_df = pd.DataFrame(product_data)

    print("Sales DataFrame:")
    print(sales_df, "\n")

    print("Product DataFrame:")
    print(product_df, "\n")

    # Compute total quantity sold per product
    result = sales_analysis(sales_df, product_df)

    print("Product Sales Analysis:")
    print(result)


if __name__ == "__main__":
    main()
