import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the product price table by pivoting the 'store' column 
    to create a table where each store has its own column.

    Args:
        products (pd.DataFrame): A DataFrame containing product prices at different stores.
                                 It has columns ['product_id', 'store', 'price'].

    Returns:
        pd.DataFrame: A DataFrame where each row represents a unique product_id,
                      and the columns represent the price of the product at each store.
    """

    return (
        products
        .pivot(index="product_id", columns="store", values="price")
        .reset_index()
    )

def main():
    """Main function to test the products_price function with sample data."""
    
    # Sample data
    data = {
        "product_id": [0, 0, 0, 1, 1],
        "store": ["store1", "store2", "store3", "store3", "store1"],
        "price": [95, 100, 105, 80, 70]
    }

    # Create DataFrame
    products_df = pd.DataFrame(data)

    # Apply function and display result
    result = products_price(products_df)
    print(result)

if __name__ == "__main__":
    main()
