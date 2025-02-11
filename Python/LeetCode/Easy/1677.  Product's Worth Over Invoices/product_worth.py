import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes product worth over invoices by calculating total rest, paid, canceled, and refunded amounts.

    Args:
        product (pd.DataFrame): DataFrame containing product details with 'product_id' and 'name'.
        invoice (pd.DataFrame): DataFrame containing invoice details with 'product_id', 'rest', 'paid', 'canceled', and 'refunded'.

    Returns:
        pd.DataFrame: Aggregated financial details for each product, ordered by product name.
    """
    return (
        pd.merge(left=product, right=invoice, on="product_id", how="left")
        .groupby("name", as_index=False)[["rest", "paid", "canceled", "refunded"]]
        .sum()
    )

def main():
    # Sample data
    product_data = {
        "product_id": [0, 1],
        "name": ["ham", "bacon"]
    }
    
    invoice_data = {
        "invoice_id": [23, 12, 0, 1, 4, 3, 4],
        "product_id": [0, 0, 1, 1, 1, 0, 0],
        "rest": [2, 0, 1, 1, 1, 1, 1],
        "paid": [0, 5, 4, 4, 4, 0, 0],
        "canceled": [5, 3, 1, 1, 1, 1, 1],
        "refunded": [0, 0, 3, 3, 3, 0, 0]
    }

    product_df = pd.DataFrame(product_data)
    invoice_df = pd.DataFrame(invoice_data)

    result = analyze_products(product_df, invoice_df)
    print(result)

if __name__ == "__main__":
    main()
