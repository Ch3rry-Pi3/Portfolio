import pandas as pd
from datetime import datetime

def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    """
    Counts the number of unique users eligible for a discount.

    A user is eligible if they made at least one purchase within the given date range
    and the purchase amount meets or exceeds the minimum required amount.

    Args:
        purchases (pd.DataFrame): DataFrame containing purchase records with columns:
            - "user_id" (int): The ID of the user.
            - "time_stamp" (datetime): The timestamp of the purchase.
            - "amount" (int): The purchase amount.
        start_date (datetime): The start of the eligible period.
        end_date (datetime): The end of the eligible period.
        min_amount (int): The minimum amount required for a purchase to be eligible.

    Returns:
        pd.DataFrame: A DataFrame with a single row and column "user_cnt" representing
        the number of users who meet the criteria.
    """
    eligible_users = purchases.loc[
        (purchases["time_stamp"] >= start_date) &
        (purchases["time_stamp"] <= end_date) &
        (purchases["amount"] >= min_amount),
        "user_id"
    ].nunique()

    return pd.DataFrame({"user_cnt": [eligible_users]})


def main():
    """
    Runs example test cases for the count_valid_users function.
    """
    # Sample purchase data
    data = {
        "user_id": [1, 2, 3, 3],
        "time_stamp": [
            "2022-03-08 09:03:00", "2022-03-19 12:39:00",
            "2022-03-18 12:03:09", "2022-03-30 09:43:42"
        ],
        "amount": [4416, 678, 4523, 626]
    }

    # Convert to DataFrame and ensure datetime format
    purchases_df = pd.DataFrame(data)
    purchases_df["time_stamp"] = pd.to_datetime(purchases_df["time_stamp"])

    # Define the time range and minimum amount
    start_date = datetime(2022, 3, 8)
    end_date = datetime(2022, 3, 20)
    min_amount = 1000

    # Get the count of eligible users
    result = count_valid_users(purchases_df, start_date, end_date, min_amount)
    print(result)


if __name__ == "__main__":
    main()
