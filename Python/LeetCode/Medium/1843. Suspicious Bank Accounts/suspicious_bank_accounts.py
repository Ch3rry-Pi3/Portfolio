import pandas as pd

def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies suspicious bank accounts where the total monthly income exceeds the 
    max_income for two or more consecutive months.

    Args:
        accounts (pd.DataFrame): Contains account data with columns:
            - "account_id" (int): Unique account identifier.
            - "max_income" (int): The maximum allowable monthly income for the account.

        transactions (pd.DataFrame): Contains transaction data with columns:
            - "transaction_id" (int): Unique transaction identifier.
            - "account_id" (int): The ID of the account associated with the transaction.
            - "type" (str): The type of transaction ('Creditor' for deposit, 'Debtor' for withdrawal).
            - "amount" (int): The transaction amount.
            - "day" (datetime): The date of the transaction.

    Returns:
        pd.DataFrame: A table containing:
            - "account_id" (int): The IDs of suspicious accounts.
        
        The result is sorted in ascending order.
    """

    # Convert 'day' column to represent the month (YYYY-MM format)
    transactions = transactions.assign(day=transactions["day"].dt.month)

    # Filter only 'Creditor' transactions (deposits)
    transactions = transactions[transactions["type"] == "Creditor"]

    # Aggregate monthly income per account
    monthly_income = (
        transactions.groupby(["account_id", "day"])
        .agg(amount=("amount", "sum"))
        .reset_index()
    )

    # Merge with the accounts table to get max_income for each account
    df = monthly_income.merge(accounts, how="left", on="account_id")

    # Filter rows where the monthly income exceeds the max_income
    df = df[df["amount"] > df["max_income"]]

    # Compute the difference between consecutive months per account
    df = df.assign(diff=df.groupby("account_id")["day"].diff())

    # Identify accounts where there are at least two consecutive months exceeding max_income
    suspicious_accounts = df[df["diff"] == 1][["account_id"]].drop_duplicates()

    # Return sorted results as required
    return suspicious_accounts.sort_values(by="account_id", ascending=True)


if __name__ == "__main__":
    # Example usage
    accounts_data = pd.DataFrame({
        "account_id": [3, 4],
        "max_income": [21000, 10400]
    })

    transactions_data = pd.DataFrame({
        "transaction_id": [2, 1, 4, 5, 6, 7, 3, 8, 9],
        "account_id": [3, 4, 4, 4, 4, 3, 3, 4, 3],
        "type": ["Creditor", "Creditor", "Creditor", "Creditor", "Debtor", "Creditor", "Debtor", "Creditor", "Creditor"],
        "amount": [107100, 10400, 49300, 75500, 75500, 90900, 56300, 64900, 102100],
        "day": pd.to_datetime([
            "2021-06-02", "2021-06-07", "2021-05-03", "2021-06-15", "2021-06-15",
            "2021-06-14", "2021-07-05", "2021-07-26", "2021-06-22"
        ])
    })

    print(suspicious_bank_accounts(accounts_data, transactions_data))
