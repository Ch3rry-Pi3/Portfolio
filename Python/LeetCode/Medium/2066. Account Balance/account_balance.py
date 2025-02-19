import pandas as pd
import numpy as np


def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the balance of each account after each transaction.

    Given a transactions table, this function processes deposits and withdrawals,
    keeping track of the cumulative balance for each account in chronological order.

    Args:
        transactions (pd.DataFrame): A DataFrame containing transaction details:
            - "account_id" (int): Unique identifier for each account.
            - "day" (datetime): Date of the transaction.
            - "type" (str): Transaction type ("Deposit" or "Withdraw").
            - "amount" (int): Transaction amount.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - "account_id" (int): The account ID.
            - "day" (datetime): The date of the transaction.
            - "balance" (int): The running balance after each transaction.
    """

    return (
        transactions
        .sort_values(by=["account_id", "day"])                                                      # Sort by account ID and date
        .assign(
            amount=lambda x: np.where(x["type"] == "Withdraw", -x["amount"], x["amount"]),          # Convert withdrawals to negative
            balance=lambda x: x.groupby("account_id")["amount"].cumsum()                            # Compute cumulative sum per account
        )
        [["account_id", "day", "balance"]]                                                          # Select the required columns
    )


def main():
    # Sample transactions dataset
    transactions_data = {
        "account_id": [1, 1, 1, 2, 2],
        "day": pd.to_datetime(["2021-11-07", "2021-11-09", "2021-11-11", "2021-12-07", "2021-12-12"]),
        "type": ["Deposit", "Withdraw", "Deposit", "Deposit", "Withdraw"],
        "amount": [2000, 1000, 1000, 7000, 7000],
    }
    
    transactions_df = pd.DataFrame(transactions_data)

    # Compute account balances
    result = account_balance(transactions_df)
    
    # Display the output
    print(result)


if __name__ == "__main__":
    main()
