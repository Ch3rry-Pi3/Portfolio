import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies products whose names contain a sequence of exactly three consecutive digits.

    Parameters:
    products (pd.DataFrame): A DataFrame containing product information with columns:
                             - 'product_id' (int): Unique identifier for each product.
                             - 'name' (str): Product name.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'product_id' (int): Products that contain exactly three consecutive digits in their name.
                  - 'name' (str): The corresponding product name.
                  The result is sorted in ascending order by 'product_id'.
    """
    # Filter products that contain exactly three consecutive digits but not four or more
    filtered_products = products[
        products["name"].str.contains(r"\d{3}", regex=True) & 
        ~products["name"].str.contains(r"\d{4,}", regex=True)
    ]

    # Sort results by 'product_id'
    return filtered_products.sort_values("product_id")


def main():
    """
    Main function to demonstrate the find_products function with a sample dataset.
    """
    # Sample products data
    products_data = {
        "product_id": [1, 2, 3, 4, 5, 6, 7],
        "name": ["ABC123XYZ", "A12B34C", "Product56789", "NoDigitsHere", 
                 "789Product", "Item@003Description", "Product12X34"]
    }

    # Convert dictionary to DataFrame
    products_df = pd.DataFrame(products_data)

    # Find products with exactly three consecutive digits in their name
    result = find_products(products_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
