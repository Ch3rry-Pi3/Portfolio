import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and formats the product name and sale date in the sales DataFrame.
    
    - Converts product names to lowercase and removes leading/trailing spaces.
    - Formats the sale_date column as 'YYYY-MM'.
    - Groups by product_name and sale_date to count total sales.
    
    Args:
        sales (pd.DataFrame): DataFrame containing sales data with columns 'product_name' and 'sale_date'.
    
    Returns:
        pd.DataFrame: A DataFrame with formatted product names, sale dates, and total sales count.
    """
    # Standardise product names (lowercase and strip spaces)
    sales["product_name"] = sales["product_name"].str.lower().str.strip()
    
    # Format sale_date to 'YYYY-MM'
    sales["sale_date"] = sales["sale_date"].dt.strftime("%Y-%m")
    
    # Group by formatted product_name and sale_date, then count occurrences
    result = sales.groupby(["product_name", "sale_date"]).size().reset_index(name="total")
    
    return result

def main():
    """Runs an example test case for the fix_name_format function."""
    # Example input DataFrame
    data = {
        "sale_id": [1, 2, 3, 4, 5, 6],
        "product_name": [" LCPHONE", "LCPhone ", " LCPhOnE ", "LCKeyCHAiN", " LCKeyChain", " Matryoshka"],
        "sale_date": pd.to_datetime(["2000-01-16", "2000-01-17", "2000-01-17", "2000-02-19", "2000-02-19", "2000-03-31"])
    }
    sales_df = pd.DataFrame(data)
    
    # Run function
    result = fix_name_format(sales_df)
    
    # Print output
    print(result)

if __name__ == "__main__":
    main()
