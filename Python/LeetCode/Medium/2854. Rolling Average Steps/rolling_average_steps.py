import pandas as pd

def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the 3-day rolling average of steps for each user.

    Args:
        steps (pd.DataFrame): Contains step count data with columns:
            - "user_id" (int): The ID of the user.
            - "steps_count" (int): The number of steps taken on a given date.
            - "steps_date" (datetime): The date of recorded steps.

    Returns:
        pd.DataFrame: A table containing:
            - "user_id" (int): The ID of the user.
            - "steps_date" (datetime): The date for which the rolling average is calculated.
            - "rolling_average" (float): The computed rolling average rounded to two decimal places.
              Only rows where a valid 3-day rolling average is available are included.
    """
    # Sort data by date for correct rolling computation
    steps = steps.sort_values(by=["user_id", "steps_date"])

    # Compute rolling 3-day average per user
    steps["rolling_average"] = (
        steps.groupby("user_id")["steps_count"]
        .rolling(window=3, min_periods=3)       # Ensure at least 3 days for calculation
        .mean()
        .round(2)
        .reset_index(level=0, drop=True)        # Maintain proper indexing
    )

    # Drop rows where rolling average could not be computed
    return steps.dropna(subset=["rolling_average"])[["user_id", "steps_date", "rolling_average"]]


if __name__ == "__main__":
    # Example usage
    steps_data = pd.DataFrame({
        "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3, 3],
        "steps_count": [687, 395, 499, 153, 171, 120, 557, 840, 627, 191],
        "steps_date": pd.to_datetime([
            "2021-09-02", "2021-09-04", "2021-09-07",
            "2021-09-07", "2021-09-09",
            "2021-09-07", "2021-09-08", "2021-09-09", "2021-09-10", "2021-09-12"
        ])
    })

    print(rolling_average(steps_data))
