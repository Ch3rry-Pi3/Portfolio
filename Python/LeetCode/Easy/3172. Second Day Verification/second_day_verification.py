import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    """
    Finds users who verified their sign-up on the second day after registering.

    Args:
        emails (pd.DataFrame): DataFrame containing email sign-up records with columns ['email_id', 'user_id', 'signup_date'].
        texts (pd.DataFrame): DataFrame containing text verification records with columns ['text_id', 'email_id', 'signup_action', 'action_date'].

    Returns:
        pd.DataFrame: A DataFrame containing unique user IDs who verified on the second day after signing up, sorted in ascending order.
    """

    # Filter only verified sign-up actions
    verified_texts = texts[texts['signup_action'] == 'Verified'].copy()

    # Compute the expected sign-up date as one day before the verification date
    verified_texts['signup_dt'] = (pd.to_datetime(verified_texts['action_date']) - pd.Timedelta(days=1)).dt.floor('d')

    # Convert the signup_date in emails to datetime and floor it to date
    emails['signup_dt'] = emails['signup_date'].dt.floor('d')

    # Merge on email_id and expected signup date
    merged_df = emails.merge(verified_texts, on=['email_id', 'signup_dt'], how='inner')

    # Return unique user_ids sorted in ascending order
    return merged_df[['user_id']].drop_duplicates().sort_values(by='user_id')


def main():
    """ Main function to test the `find_second_day_signups` function with example data. """

    # Sample emails DataFrame
    emails_data = {
        "email_id": [125, 433, 234],
        "user_id": [7771, 1052, 7005],
        "signup_date": pd.to_datetime(["2022-06-14 09:30:00", "2022-07-09 08:15:00", "2022-08-20 10:00:00"])
    }
    emails_df = pd.DataFrame(emails_data)

    # Sample texts DataFrame
    texts_data = {
        "text_id": [1, 2, 4],
        "email_id": [125, 433, 234],
        "signup_action": ["Verified", "Not Verified", "Verified"],
        "action_date": pd.to_datetime(["2022-06-15 08:30:00", "2022-07-10 10:45:00", "2022-08-21 09:30:00"])
    }
    texts_df = pd.DataFrame(texts_data)

    # Call function and print result
    result = find_second_day_signups(emails_df, texts_df)
    print(result)


if __name__ == "__main__":
    main()
