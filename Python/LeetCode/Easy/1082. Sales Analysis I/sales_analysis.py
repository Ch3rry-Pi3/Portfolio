import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the best seller(s) by total sales price.
    Returns a DataFrame containing the seller_id(s) with the highest sales.
    """

    # Aggregate total sales per seller
    sales_summary = sales.groupby("seller_id", as_index=False)["price"].sum()

    # Return sellers with the highest total sales
    return sales_summary.loc[sales_summary["price"] == sales_summary["price"].max(), ["seller_id"]]

def main():
    """
    Runs example test case for the sales_analysis function.
    """
    # Define Product DataFrame
    product_data = {
        "product_id": [1, 2, 3],
        "product_name": ["S8", "G4", "iPhone"],
        "unit_price": [1000, 800, 1400]
    }
    product = pd.DataFrame(product_data)

    # Define Sales DataFrame
    sales_data = {
        "seller_id": [1, 1, 2, 3],
        "product_id": [1, 2, 2, 3],
        "buyer_id": [1, 2, 3, 4],
        "sale_date": ["2019-01-21", "2019-02-17", "2019-06-02", "2019-05-13"],
        "quantity": [2, 1, 1, 2],
        "price": [2000, 800, 800, 2800]
    }
    sales = pd.DataFrame(sales_data)

    # Run the function and print the result
    result = sales_analysis(product, sales)
    print(result)

if __name__ == "__main__":
    main()
