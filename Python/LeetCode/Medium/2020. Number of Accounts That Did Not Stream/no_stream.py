import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the number of accounts that subscribed in 2021 but did not have any stream session.

    Args:
        subscriptions (pd.DataFrame): A DataFrame containing subscription details with columns:
                                      - "account_id" (int): Unique account ID.
                                      - "start_date" (datetime): Subscription start date.
                                      - "end_date" (datetime): Subscription end date.
        streams (pd.DataFrame): A DataFrame containing streaming session details with columns:
                                - "session_id" (int): Unique stream session ID.
                                - "account_id" (int): Account associated with the stream.
                                - "stream_date" (datetime): Date of the stream session.

    Returns:
        pd.DataFrame: A DataFrame with one column:
                      - "accounts_count" (int): The number of accounts that subscribed in 2021 but did not stream.
    """

    # Merge subscriptions with streams to match account activities
    df = (
        pd.merge(left=subscriptions, right=streams, on="account_id", how="left")
        .assign(
            # Identify valid subscriptions in 2021
            valid_subscription=lambda x: (
                (x["start_date"].dt.year <= 2021) & (x["end_date"].dt.year >= 2021)
            ).astype(int),
            # Extract stream year
            stream_year=lambda x: x["stream_date"].dt.year
        )
        # Keep only valid subscriptions and accounts that did not stream in 2021
        .query("valid_subscription == 1 and (stream_year != 2021 or stream_year.isna())")
        # Remove duplicate accounts
        .drop_duplicates(subset="account_id")
    )

    # Count the number of accounts
    accounts_count = len(df["account_id"].unique())

    return pd.DataFrame({"accounts_count": [accounts_count]})

def main():
    # Example subscriptions data
    subscriptions_data = {
        "account_id": [9, 3, 13, 4, 15],
        "start_date": pd.to_datetime(["2020-02-18", "2021-09-21", "2020-08-24", "2021-10-26", "2020-09-11"]),
        "end_date": pd.to_datetime(["2021-10-30", "2021-11-13", "2021-09-08", "2021-09-28", "2021-01-17"])
    }

    # Example streams data
    streams_data = {
        "session_id": [14, 13, 17, 19, 13],
        "account_id": [9, 3, 13, 4, 5],
        "stream_date": pd.to_datetime(["2020-05-16", "2020-10-27", "2020-04-29", "2020-12-31", "2021-01-05"])
    }

    # Convert to DataFrame
    subscriptions_df = pd.DataFrame(subscriptions_data)
    streams_df = pd.DataFrame(streams_data)

    # Call function
    result = find_target_accounts(subscriptions_df, streams_df)

    # Display result
    print(result)

if __name__ == "__main__":
    main()
