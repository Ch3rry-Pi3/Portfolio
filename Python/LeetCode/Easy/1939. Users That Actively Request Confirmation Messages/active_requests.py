import pandas as pd
from datetime import timedelta


def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies users who have requested a confirmation message twice within a 24-hour window.

    Args:
        signups (pd.DataFrame): A DataFrame containing signup information with columns:
            - user_id (int): The ID of the user who signed up.
            - time_stamp (datetime): The timestamp of the signup event.
        
        confirmations (pd.DataFrame): A DataFrame containing confirmation requests with columns:
            - user_id (int): The ID of the user requesting confirmation.
            - time_stamp (datetime): The timestamp of the confirmation request.
            - action (str): The type of confirmation event ('confirmed' or 'timeout').

    Returns:
        pd.DataFrame: A DataFrame containing the user IDs of those who requested a confirmation 
                      message at least twice within a 24-hour window.
    """

    # Sort confirmation requests by timestamp
    confirmations = confirmations.sort_values("time_stamp")

    # Compute the time difference between consecutive requests per user
    confirmations["diff"] = confirmations.groupby("user_id")["time_stamp"].diff()

    # Filter users who made two requests within a 24-hour window
    confirmations = confirmations[confirmations["diff"] <= timedelta(days=1)].dropna()

    # Extract unique user IDs that meet the criteria
    return confirmations[["user_id"]].drop_duplicates()


def main():
    """
    Example usage of the find_requesting_users function.
    """

    # Sample data for signups
    signups_data = {
        "user_id": [3, 2, 7, 6],
        "time_stamp": pd.to_datetime(["2020-03-21 10:16:13", "2021-08-04 13:57:59",
                                      "2020-07-29 23:09:44", "2022-12-09 10:39:37"]),
    }
    signups = pd.DataFrame(signups_data)

    # Sample data for confirmations
    confirmations_data = {
        "user_id": [1, 2, 2, 3, 7, 7, 6, 6],
        "time_stamp": pd.to_datetime(["2021-01-06 08:30:46", "2021-01-06 03:37:45",
                                      "2021-06-12 11:57:29", "2021-06-12 11:57:30",
                                      "2021-01-22 00:00:00", "2021-01-22 00:00:01",
                                      "2021-10-23 14:14:14", "2021-10-24 14:14:13"]),
        "action": ["timeout", "timeout", "confirmed", "confirmed",
                   "confirmed", "confirmed", "confirmed", "timeout"]
    }
    confirmations = pd.DataFrame(confirmations_data)

    # Run the function and display results
    result = find_requesting_users(signups, confirmations)
    print(result)


if __name__ == "__main__":
    main()
