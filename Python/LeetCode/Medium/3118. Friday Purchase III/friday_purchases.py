import pandas as pd

def friday_purchases(purchases: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total spending by Premium and VIP users on each Friday of November 2023.

    If there are no purchases on a given Friday by Premium or VIP members, 
    the spending for that date should be recorded as 0.

    Args:
        purchases (pd.DataFrame): Contains purchase data with columns:
            - "user_id" (int): The ID of the user making the purchase.
            - "purchase_date" (date): The date of purchase.
            - "amount_spend" (int): The total amount spent.
        users (pd.DataFrame): Contains user data with columns:
            - "user_id" (int): The ID of the user.
            - "membership" (enum): Membership type ('Standard', 'Premium', 'VIP').

    Returns:
        pd.DataFrame: A table containing:
            - "week_of_month" (int): The week number in November.
            - "membership" (str): The membership type.
            - "total_amount" (int): Total spending by the membership type.
        
        The result is sorted by "week_of_month" in ascending order, 
        and then by "membership" in ascending order.
    """

    # Define all Fridays in November 2023
    fridays = pd.date_range(start="2023-11-01", end="2023-11-30", freq="W-FRI")

    # Create a mapping from each Friday date to its corresponding week number
    week_map = {date: i + 1 for i, date in enumerate(fridays)}

    # Map each purchase to the corresponding week of the month
    purchases["week_of_month"] = purchases["purchase_date"].map(week_map)

    # Filter purchases to only include those made on a Friday
    purchases = purchases[purchases["purchase_date"].isin(fridays)]

    # Merge with users table to get membership type
    merged = purchases.merge(users, on="user_id")

    # Keep only purchases made by Premium and VIP members
    merged = merged[merged["membership"].isin(["Premium", "VIP"])]

    # Group by week_of_month and membership, summing the amount spent
    agg = (
        merged.groupby(["week_of_month", "membership"])["amount_spend"]
        .sum()
        .reset_index(name="total_amount")
    )

    # Create a full grid of weeks and membership types to ensure missing values are filled with 0
    weeks = list(week_map.values())
    memberships = ["Premium", "VIP"]
    full_grid = pd.MultiIndex.from_product([weeks, memberships], names=["week_of_month", "membership"])

    # Ensure all week-membership combinations are represented, filling missing values with 0
    result = agg.set_index(["week_of_month", "membership"]).reindex(full_grid, fill_value=0).reset_index()

    # Sort by week_of_month and membership type
    return result.sort_values(by=["week_of_month", "membership"])


if __name__ == "__main__":
    # Example usage
    purchases_data = pd.DataFrame({
        "user_id": [11, 15, 17, 12, 1, 10, 13],
        "purchase_date": pd.to_datetime(["2023-11-03", "2023-11-10", "2023-11-17", 
                                         "2023-11-17", "2023-11-24", "2023-11-24", "2023-11-21"]),
        "amount_spend": [1126, 7473, 2414, 9562, 5117, 5241, 12000]
    })

    users_data = pd.DataFrame({
        "user_id": [11, 15, 17, 12, 1, 10, 13],
        "membership": ["Premium", "VIP", "Standard", "VIP", "Premium", "VIP", "Premium"]
    })

    print(friday_purchases(purchases_data, users_data))
