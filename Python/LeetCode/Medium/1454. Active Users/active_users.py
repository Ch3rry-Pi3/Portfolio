import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active users who have logged in for five or more consecutive days.

    Args:
        accounts (pd.DataFrame): A DataFrame containing user account details with columns:
            - id (int): Unique user ID.
            - name (str): User's name.

        logins (pd.DataFrame): A DataFrame containing user login records with columns:
            - id (int): User ID corresponding to a login event.
            - login_date (date): The date the user logged in.

    Returns:
        pd.DataFrame: A DataFrame containing the IDs and names of active users,
                      sorted by ID in ascending order.
    """
    return (
        pd.merge(
            left=logins.drop_duplicates(),                                                          # Remove duplicate logins for the same user & date
            right=accounts,
            on="id",
            how="left"
        )
        .sort_values(by=["id", "login_date"])                                                       # Sort by user ID and login date
        .assign(
            rank=lambda x: x.groupby("id")["login_date"].rank(method="dense"),                      # Rank logins per user
            diff=lambda x: x["login_date"] - pd.to_timedelta(x["rank"].astype(int), unit="D")       # Identify streaks
        )
        .groupby(["id", "name", "diff"], as_index=False)
        .count()                    # Count logins in each streak
        .query("rank >= 5")         # Keep only users with 5+ consecutive logins
        .sort_values(by="id")       # Sort by user ID
        [["id", "name"]]
        .drop_duplicates()          # Ensure unique users in the final output
    )


if __name__ == "__main__":
    # Example usage with sample data
    accounts_df = pd.DataFrame({
        "id": [1, 7],
        "name": ["Winston", "Jonathan"]
    })

    logins_df = pd.DataFrame({
        "id": [7, 7, 7, 7, 7, 7, 1, 1],
        "login_date": pd.to_datetime([
            "2020-05-30", "2020-05-30", "2020-05-31",
            "2020-06-01", "2020-06-02", "2020-06-03",
            "2020-06-07", "2020-06-10"
        ])
    })

    result = active_users(accounts_df, logins_df)
    print(result)
