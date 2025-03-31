import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Find products with a valid serial number pattern in their description.

    A valid serial number pattern follows these rules:
    - Starts with "SN"
    - Followed by exactly 4 digits
    - A hyphen (-) followed by exactly 4 digits
    - Must be within the description (not necessarily at the beginning)

    Args:
        products (pd.DataFrame): A DataFrame containing columns:
            - product_id (int): Unique identifier for the product
            - product_name (str): Name of the product
            - description (str): Description containing possible serial numbers

    Returns:
        pd.DataFrame: Filtered DataFrame containing only rows with valid serial numbers,
                      ordered by product_id in ascending order.
    """
    # Define the regex patterns to match valid serial numbers
    pattern1 = r'SN[0-9]{4}\-[0-9]{4}[^0-9]'
    pattern2 = r'SN[0-9]{4}\-[0-9]{4}$'

    # Filter rows containing valid serial numbers
    valid_products = products[
        (products["description"].str.contains(pattern1, na=False)) |
        (products["description"].str.contains(pattern2, na=False))
    ]

    # Sort the result by product_id in ascending order
    return valid_products.sort_values(by="product_id")


def main():
    # Example data to demonstrate functionality
    data = {
        "product_id": [1, 2, 3, 4, 5],
        "product_name": ["Widget A", "Widget B", "Widget C", "Widget D", "Widget E"],
        "description": [
            "This is a sample product with SN1234-5678",
            "A product with serial SN9876-1234 in the description",
            "Product SN1234-56789 is available now",
            "No serial number here",
            "Check out SN4321-8765 in this description"
        ]
    }

    # Create a DataFrame
    products = pd.DataFrame(data)

    # Find valid serial products
    valid_serials = find_valid_serial_products(products)

    # Print the result
    print("Valid Serial Products:")
    print(valid_serials)


if __name__ == "__main__":
    main()
