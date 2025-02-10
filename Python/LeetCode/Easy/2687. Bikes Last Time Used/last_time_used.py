import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the last time each bike was used and returns the result sorted in descending order.

    Args:
        bikes (pd.DataFrame): A DataFrame containing bike usage data with columns:
            - "bike_number" (str): The bike identifier.
            - "end_time" (datetime): The end time of the bike's ride.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "bike_number" (str): Unique bike identifiers.
            - "end_time" (datetime): The last recorded end time for each bike.
    """
    # Get the last used time for each bike by finding the max end_time
    last_used = bikes.loc[bikes.groupby("bike_number")["end_time"].idxmax(), ["bike_number", "end_time"]]

    # Sort results by the most recently used bikes
    last_used = last_used.sort_values(by="end_time", ascending=False).reset_index(drop=True)

    return last_used


def main():
    """
    Runs example test cases for the last_used_time function.
    """
    # Sample bike usage data
    data = {
        "ride_id": [1, 2, 3, 4, 5, 6],
        "bike_number": ["W00576", "W00300", "W00300", "W00535", "W00535", "W00576"],
        "start_time": [
            "2012-03-25 11:30:00", "2012-03-25 10:30:00", "2012-03-25 16:30:00",
            "2012-03-25 14:00:00", "2012-03-25 09:10:00", "2012-03-28 02:30:00"
        ],
        "end_time": [
            "2012-03-25 12:40:00", "2012-03-25 10:50:00", "2012-03-25 17:40:00",
            "2012-03-25 13:40:00", "2012-03-25 09:18:00", "2012-03-28 02:50:00"
        ]
    }

    # Convert to DataFrame and ensure datetime columns
    bikes_df = pd.DataFrame(data)
    bikes_df["start_time"] = pd.to_datetime(bikes_df["start_time"])
    bikes_df["end_time"] = pd.to_datetime(bikes_df["end_time"])

    # Find last used time for each bike
    result = last_used_time(bikes_df)
    print(result)


if __name__ == "__main__":
    main()
