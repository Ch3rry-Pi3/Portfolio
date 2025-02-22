import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total spending by users on each Friday of every week in November 2023.

    Args:
        purchases (pd.DataFrame): Contains purchase data with columns:
            - "user_id" (int): The ID of the user making the purchase.
            - "purchase_date" (datetime): The date of the purchase.
            - "amount_spend" (int): The amount spent on the purchase.

    Returns:
        pd.DataFrame: A table containing:
            - "week_of_month" (int): The week number in November 2023 (1-5).
            - "purchase_date" (datetime): The specific Friday date.
            - "total_amount" (int): The total spending on that Friday.

        The result is sorted by "week_of_month" in ascending order and only includes
        weeks where at least one purchase was made on a Friday.
    """
    # Extract weekday name and determine week of the month
    purchases = purchases.assign(
        weekday_of_week=purchases["purchase_date"].dt.day_name(),
        week_of_month=(purchases["purchase_date"].dt.day - 1) // 7 + 1
    )

    # Filter purchases to include only Fridays
    purchases = purchases[purchases["weekday_of_week"] == "Friday"]

    # Aggregate total spending for each Friday
    purchases = (
        purchases.groupby(["week_of_month", "purchase_date"])["amount_spend"]
        .sum()
        .reset_index(name="total_amount")
    )

    # Sort results by week of the month
    return purchases.sort_values(by="week_of_month")


if __name__ == "__main__":
    # Example usage
    purchases_data = pd.DataFrame({
        "user_id": [11, 15, 7, 12, 1, 3, 4],
        "purchase_date": pd.to_datetime([
            "2023-11-07", "2023-11-30", "2023-11-24",
            "2023-11-24", "2023-11-10", "2023-11-17", "2023-11-24"
        ]),
        "amount_spend": [1126, 7473, 926, 5117, 5241, 8266, 10000]
    })

    print(friday_purchases(purchases_data))
