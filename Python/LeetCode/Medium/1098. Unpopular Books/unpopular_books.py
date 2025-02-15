import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies unpopular books that sold less than 10 copies in the last year,
    excluding books available for less than one month from today (2019-06-23).

    Args:
        books (pd.DataFrame): Contains book details with 'book_id', 'name', and 'available_from'.
        orders (pd.DataFrame): Contains order details with 'book_id', 'quantity', and 'dispatch_date'.

    Returns:
        pd.DataFrame: A DataFrame with ['book_id', 'name'] of unpopular books.
    """
    # Filter books available for at least one month (before 2019-05-23)
    recent_books = books[books["available_from"] < "2019-05-23"]

    # Filter orders placed in the last year (after 2018-06-23)
    recent_orders = orders[orders["dispatch_date"] > "2018-06-23"]

    # Merge books with relevant orders and calculate total quantity sold
    sales_summary = (
        pd.merge(recent_books, recent_orders, on="book_id", how="left")
        .groupby(["book_id", "name"], as_index=False)
        .agg(total_quantity=("quantity", "sum"))
    )

    # Filter books that sold less than 10 copies
    unpopular_books = sales_summary.query("total_quantity < 10")[["book_id", "name"]]

    return unpopular_books

if __name__ == "__main__":
    # Example data
    books_data = {
        "book_id": [1, 2, 3, 4],
        "name": ["Book A", "Book B", "Book C", "Book D"],
        "available_from": ["2019-01-01", "2019-04-15", "2019-05-25", "2018-06-10"],
    }

    orders_data = {
        "order_id": [101, 102, 103, 104, 105],
        "book_id": [1, 1, 2, 3, 4],
        "quantity": [4, 3, 5, 8, 2],
        "dispatch_date": ["2018-07-01", "2019-01-15", "2019-02-20", "2019-06-01", "2018-07-10"],
    }

    # Create DataFrames
    books_df = pd.DataFrame(books_data)
    orders_df = pd.DataFrame(orders_data)

    # Compute unpopular books
    result = unpopular_books(books_df, orders_df)

    # Display result
    print(result)
