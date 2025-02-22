import pandas as pd

def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the third transaction for each user where the previous two transactions had lower spending.

    Args:
        transactions (pd.DataFrame): Contains transaction data with columns:
            - "user_id" (int): The ID of the user making the transaction.
            - "spend" (decimal): The amount spent in the transaction.
            - "transaction_date" (datetime): The date and time of the transaction.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The ID of the user.
            - "third_transaction_spend" (decimal): The spend amount of the third qualifying transaction.
            - "third_transaction_date" (datetime): The date of the third qualifying transaction.
        
        The result is sorted by "user_id" in ascending order.
    """
    # Sort transactions by user_id and transaction_date
    df = transactions.sort_values(["user_id", "transaction_date"])

    # Select only the first three transactions per user
    df = df.groupby("user_id").head(3)

    # Filter for third transactions where both previous transactions had lower spending
    df = df[
        (df["spend"] > df.shift(1)["spend"]) & (df["user_id"] == df.shift(1)["user_id"]) &
        (df["spend"] > df.shift(2)["spend"]) & (df["user_id"] == df.shift(2)["user_id"])
    ]

    # Rename columns and return only necessary fields
    return (
        df.rename(columns={"spend": "third_transaction_spend", "transaction_date": "third_transaction_date"})
        [["user_id", "third_transaction_spend", "third_transaction_date"]]
        .sort_values("user_id")
    )


if __name__ == "__main__":
    # Example usage
    transactions_data = pd.DataFrame({
        "user_id": [1, 1, 1, 1, 1, 1, 3, 3, 3],
        "spend": [65.56, 96.0, 49.78, 100.4, 37.43, 18.38, 100.4, 37.43, 18.38],
        "transaction_date": pd.to_datetime([
            "2023-11-18 13:49:42", "2023-11-30 08:47:26", "2023-11-12 08:47:26",
            "2023-11-11 06:39:34", "2023-11-06 02:11:34", "2023-11-02 23:56:34",
            "2023-11-11 06:39:34", "2023-11-06 02:11:34", "2023-11-02 23:56:34"
        ])
    })

    print(find_third_transaction(transactions_data))
