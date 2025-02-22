import pandas as pd

def find_active_users(users: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active users who made a second purchase within 7 days of any of their previous purchases.

    Args:
        users (pd.DataFrame): Contains transaction data with columns:
            - "user_id" (int): The ID of the user.
            - "item" (str): The purchased item.
            - "created_at" (datetime): The date of purchase.
            - "amount" (int): The purchase amount.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The list of active users who made a second purchase
              within 7 days of any other purchase.
    """
    return (
        users
        # Sort by user_id and created_at to ensure chronological order
        .sort_values(by=["user_id", "created_at"], ascending=[True, True])
        # Calculate the difference in days between consecutive purchases for each user
        .assign(date_diff=lambda x: x.groupby("user_id")["created_at"].diff().dt.days)
        # Filter users who made a purchase within 7 days of their previous transaction
        .query("date_diff <= 7")
        # Remove duplicate user_id entries
        .drop_duplicates(subset="user_id")
        # Keep only the user_id column
        [["user_id"]]
    )


if __name__ == "__main__":
    # Example usage
    users_data = pd.DataFrame({
        "user_id": [5, 6, 6, 4, 4],
        "item": ["Smart Crock Pot", "Smart Lock", "Smart Thermostat", "Smart Cat Feeder", "Smart Bed"],
        "created_at": pd.to_datetime(["2021-09-18", "2021-09-10", "2021-09-14", "2021-09-02", "2021-09-13"]),
        "amount": [698882, 11487, 11467, 693745, 170249]
    })

    print(find_active_users(users_data))
