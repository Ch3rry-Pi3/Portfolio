import pandas as pd
from datetime import timedelta


def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of users who logged in for the first time on each date within the last 90 days.

    Args:
        traffic (pd.DataFrame): A DataFrame containing user activity logs with columns:
            - 'user_id' (int): The unique ID of the user.
            - 'activity' (str): The type of activity ('login', 'logout', etc.).
            - 'activity_date' (datetime): The date the activity occurred.

    Returns:
        pd.DataFrame: A DataFrame with the first login date and the count of users who logged in for the first time.
    """

    # Filter only login activities and remove duplicate user entries
    df = traffic[traffic["activity"] == "login"].drop_duplicates()

    # Find the first login date for each user
    first_login = df.groupby("user_id", as_index=False)["activity_date"].min()

    # Define the date range: last 90 days before '2019-06-30'
    start_date = pd.to_datetime("2019-06-30") - timedelta(days=90)
    first_login = first_login[first_login["activity_date"].between(start_date, "2019-06-30")]

    # Count users who logged in for the first time on each date
    final = first_login.groupby("activity_date", as_index=False)["user_id"].count()

    # Rename columns for clarity
    return final.rename(columns={"activity_date": "login_date", "user_id": "user_count"})


if __name__ == "__main__":
    # Example usage with a sample dataset
    sample_data = {
        "user_id": [1, 1, 1, 2, 3, 3, 4, 5, 5],
        "activity": ["login", "homepage", "login", "login", "login", "logout", "login", "login", "login"],
        "activity_date": pd.to_datetime(
            ["2019-05-01", "2019-05-01", "2019-06-21", "2019-06-21", "2019-06-21", "2019-06-21", "2019-03-01", "2019-06-21", "2019-03-01"]
        ),
    }

    traffic_df = pd.DataFrame(sample_data)
    result = new_users_daily_count(traffic_df)

    print(result)
