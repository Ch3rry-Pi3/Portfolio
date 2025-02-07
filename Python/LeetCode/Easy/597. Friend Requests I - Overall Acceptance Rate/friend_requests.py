import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the overall friend request acceptance rate.

    The acceptance rate is calculated as:
        acceptance_rate = (Total Accepted Requests / Total Friend Requests)

    If no requests exist, the function returns 0.00.

    :param friend_request: DataFrame containing 'sender_id', 'send_to_id', and 'request_date'.
    :param request_accepted: DataFrame containing 'requester_id', 'accepter_id', and 'accept_date'.
    :return: DataFrame with a single column 'accept_rate' rounded to 2 decimal places.
    """

    # Drop duplicate requests and accepted requests to count only unique interactions
    distinct_accepted = request_accepted[['requester_id', 'accepter_id']].drop_duplicates()
    distinct_request = friend_request[['sender_id', 'send_to_id']].drop_duplicates()

    # Count distinct requests and acceptances
    accepted_count = len(distinct_accepted)
    request_count = len(distinct_request)

    # Compute acceptance rate, ensuring division by zero is handled
    accept_rate = round(accepted_count / request_count, 2) if request_count != 0 else 0.00

    # Return result as a DataFrame
    return pd.DataFrame({"accept_rate": [accept_rate]})


def main():
    """
    Demonstrates testing the acceptance_rate function on example datasets.
    """
    # Example test data
    friend_request_data = {
        "sender_id": [1, 2, 3, 3, 4, 4],
        "send_to_id": [2, 3, 4, 4, 5, 5],
        "request_date": pd.to_datetime([
            "2021-07-01", "2021-07-02", "2021-07-03",
            "2021-07-03", "2021-07-04", "2021-07-04"
        ])
    }

    request_accepted_data = {
        "requester_id": [1, 3, 3, 4],
        "accepter_id": [2, 4, 4, 5],
        "accept_date": pd.to_datetime([
            "2021-07-02", "2021-07-03", "2021-07-03", "2021-07-05"
        ])
    }

    # Convert dictionaries to DataFrames
    friend_request_df = pd.DataFrame(friend_request_data)
    request_accepted_df = pd.DataFrame(request_accepted_data)

    print("Friend Request DataFrame:")
    print(friend_request_df, "\n")

    print("Request Accepted DataFrame:")
    print(request_accepted_df, "\n")

    # Compute acceptance rate
    result = acceptance_rate(friend_request_df, request_accepted_df)

    print("Acceptance Rate:")
    print(result)


if __name__ == "__main__":
    main()
