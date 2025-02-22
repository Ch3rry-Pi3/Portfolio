import pandas as pd

def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies users whose first and last calls on any given day were with the same person.

    Calls are counted regardless of whether the user is the caller or the recipient.

    :param calls: DataFrame containing 'caller_id', 'recipient_id', and 'call_time' columns.
    :return: DataFrame with a single column 'user_id' listing the relevant users.
    """

    # Duplicate the dataset by swapping 'caller_id' and 'recipient_id' to create bidirectional call records
    df_call = pd.concat([calls, calls.rename(columns={'recipient_id': 'caller_id', 'caller_id': 'recipient_id'})])

    # Extract the call date (YYYY-MM-DD) from 'call_time' for daily grouping
    df_call['day'] = df_call['call_time'].dt.strftime('%Y-%m-%d')

    # Compute the first (earliest) and last (latest) call times per user per day
    df_call = df_call.assign(
        max_time=df_call.groupby(['day', 'caller_id'])['call_time'].transform('max'),
        min_time=df_call.groupby(['day', 'caller_id'])['call_time'].transform('min')
    )

    # Identify the last call per user per day
    df_max = df_call.loc[df_call['call_time'] == df_call['max_time'], ['caller_id', 'recipient_id', 'day']]

    # Identify the first call per user per day
    df_min = df_call.loc[df_call['call_time'] == df_call['min_time'], ['caller_id', 'recipient_id', 'day']]

    # Find users whose first and last calls were with the same recipient on the same day
    df_result = pd.merge(df_max, df_min, how='inner', on=['caller_id', 'recipient_id', 'day'])[['caller_id']]

    # Remove duplicates and rename the column for final output
    df_result = df_result.drop_duplicates().rename(columns={'caller_id': 'user_id'})

    return df_result


def main():
    """
    Demonstrates testing the same_day_calls function on an example dataset.
    """
    # Example test data
    data = {
        "caller_id": [8, 8, 8, 5, 5, 11, 8],
        "recipient_id": [4, 4, 4, 3, 3, 3, 11],
        "call_time": pd.to_datetime([
            "2021-08-24 17:46:07", "2021-08-24 19:57:13", "2021-08-11 05:28:14",
            "2021-08-17 04:04:15", "2021-08-17 13:07:00", "2021-08-11 13:06:00",
            "2021-08-17 22:22:22"
        ])
    }

    calls_df = pd.DataFrame(data)

    print("Input DataFrame:")
    print(calls_df, "\n")

    # Compute first and last calls on the same day
    result = same_day_calls(calls_df)

    print("Output DataFrame:")
    print(result)


if __name__ == "__main__":
    main()
