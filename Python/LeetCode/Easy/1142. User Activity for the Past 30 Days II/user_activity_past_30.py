import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the average number of sessions per user over a 30-day period ending on 2019-07-27.

    Args:
        activity (pd.DataFrame): A DataFrame containing user activity logs with columns:
                                 - 'user_id' (int): The user identifier.
                                 - 'session_id' (int): The session identifier.
                                 - 'activity_date' (datetime): The date of the activity.
                                 - 'activity_type' (str): Type of activity.

    Returns:
        pd.DataFrame: A DataFrame with a single column 'average_sessions_per_user', rounded to two decimal places.
    """

    return (
        (
            activity[activity["activity_date"].between("2019-06-28", "2019-07-27")]
            .groupby("user_id", as_index=False)
            .agg({"session_id": "nunique"})
            .agg(average_sessions_per_user=("session_id", "mean"))
            .round(2)
            .transpose()
        )
        if activity["activity_date"].between("2019-06-28", "2019-07-27").any()
        else pd.DataFrame({"average_sessions_per_user": [0.00]})
    )

def main():
    # Sample dataset for testing
    data = {
        "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4],
        "session_id": [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        "activity_date": pd.to_datetime([
            "2019-07-20", "2019-07-20", "2019-07-20",
            "2019-07-21", "2019-07-21",
            "2019-07-21", "2019-07-21", "2019-07-22", "2019-07-22",
            "2019-06-15", "2019-06-16"
        ]),
        "activity_type": [
            "open_session", "scroll_down", "end_session",
            "send_message", "open_session",
            "open_session", "scroll_down", "open_session", "end_session",
            "send_message", "end_session"
        ]
    }

    # Convert data to DataFrame
    activity_df = pd.DataFrame(data)

    # Call the function and display the output
    result = user_activity(activity_df)
    print(result)

if __name__ == "__main__":
    main()
