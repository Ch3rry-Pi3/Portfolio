import pandas as pd
import numpy as np


def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the final credit balance of each user after processing transactions.
    Determines whether the credit limit has been breached.

    Args:
        users (pd.DataFrame): DataFrame containing user credit details with columns:
            - "user_id" (int): Unique user ID.
            - "user_name" (str): Name of the user.
            - "credit" (int): Initial credit balance.

        transactions (pd.DataFrame): DataFrame containing transaction details with columns:
            - "trans_id" (int): Unique transaction ID.
            - "paid_by" (int): User ID who sent the money.
            - "paid_to" (int): User ID who received the money.
            - "amount" (int): Transaction amount.
            - "transacted_on" (date): Date of transaction.

    Returns:
        pd.DataFrame: DataFrame with the updated credit balance and credit limit breach status.
    """

    # Compute total amount received by each user
    received_amount = transactions.groupby("paid_to", as_index=False).agg(add=("amount", "sum"))

    # Compute total amount spent by each user
    spent_amount = transactions.groupby("paid_by", as_index=False).agg(sub=("amount", "sum"))

    # Merge transactions with users and update balances
    final_balance = (
        users
        .merge(received_amount, left_on="user_id", right_on="paid_to", how="left")
        .merge(spent_amount, left_on="user_id", right_on="paid_by", how="left")
        .fillna(value={"add": 0, "sub": 0})                                                 # Fill missing values with 0
        .assign(credit=lambda x: x["credit"] + x["add"] - x["sub"])                         # Update credit balance
        .assign(credit_limit_breached=lambda x: np.where(x["credit"] < 0, "Yes", "No"))     # Breach check
        .drop(columns=["paid_to", "paid_by", "add", "sub"])                                 # Remove unnecessary columns
    )

    return final_balance


def main():
    # Example dataset
    users_data = {
        "user_id": [1, 2, 3, 4],
        "user_name": ["Moustafa", "Jonathan", "Winston", "Luis"],
        "credit": [100, 200, 10000, 800],
    }

    transactions_data = {
        "trans_id": [1, 2, 3],
        "paid_by": [1, 3, 1],
        "paid_to": [3, 2, 1],
        "amount": [400, 500, 200],
        "transacted_on": ["2020-08-01", "2020-08-02", "2020-08-03"],
    }

    users_df = pd.DataFrame(users_data)
    transactions_df = pd.DataFrame(transactions_data)

    # Compute bank account summary
    result = bank_account_summary(users_df, transactions_df)

    # Display the result
    print(result)


if __name__ == "__main__":
    main()
