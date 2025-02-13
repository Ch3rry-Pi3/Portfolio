import pandas as pd
from datetime import datetime


def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    """
    Finds users eligible for a discount based on purchase conditions.

    Args:
        purchases (pd.DataFrame): DataFrame containing purchase data with columns ['user_id', 'time_stamp', 'amount'].
        start_date (datetime): The start date of the eligibility window.
        end_date (datetime): The end date of the eligibility window.
        min_amount (int): Minimum purchase amount required for discount eligibility.

    Returns:
        pd.DataFrame: A DataFrame containing unique user IDs of eligible users, sorted in ascending order.
    """

    # Filter purchases within the specified date range and minimum amount condition
    eligible_users = purchases.loc[
        (start_date <= purchases["time_stamp"]) & (purchases["time_stamp"] <= end_date) &
        (purchases["amount"] >= min_amount), 
        ["user_id"]
    ].drop_duplicates()

    # Return the sorted result by user_id
    return eligible_users.sort_values(by="user_id").reset_index(drop=True)


# Example usage
if __name__ == "__main__":
    data = {
        "user_id": [1, 1, 2, 3, 3],
        "time_stamp": pd.to_datetime([
            "2022-04-20 09:03:00", "2022-03-19 19:24:02", 
            "2022-03-18 12:03:09", "2022-03-30 09:43:42", 
            "2022-03-10 08:30:00"
        ]),
        "amount": [4416, 678, 4523, 626, 1500]
    }

    purchases_df = pd.DataFrame(data)

    start_date = datetime(2022, 3, 8)
    end_date = datetime(2022, 3, 20)
    min_amount = 1000

    print(find_valid_users(purchases_df, start_date, end_date, min_amount))
