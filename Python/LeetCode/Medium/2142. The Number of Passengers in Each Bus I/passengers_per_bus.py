import pandas as pd

def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of passengers who use each bus.

    A passenger boards the earliest arriving bus that is at or after their arrival time.
    A bus only picks up passengers who haven't already boarded another bus.

    Args:
        buses (pd.DataFrame): Contains bus data with columns:
            - "bus_id" (int): The unique ID of the bus.
            - "arrival_time" (int): The time the bus arrives at the station.
        passengers (pd.DataFrame): Contains passenger data with columns:
            - "passenger_id" (int): The unique ID of the passenger.
            - "arrival_time" (int): The time the passenger arrives at the station.

    Returns:
        pd.DataFrame: A table with:
            - "bus_id" (int): The unique bus ID.
            - "passengers_cnt" (int): The number of passengers that used each bus.
        
        The result is sorted by "bus_id" in ascending order.
    """

    # Merge buses and passengers using an ordered merge on arrival_time
    df = pd.merge_ordered(buses, passengers, on="arrival_time")

    # Backfill the bus_id to assign each passenger to the earliest available bus
    df["bus_id"] = df["bus_id"].bfill()

    # Group by bus_id and count the number of passengers for each bus
    result = df.groupby("bus_id", as_index=False).agg(passengers_cnt=("passenger_id", "count"))

    return result.sort_values("bus_id")


if __name__ == "__main__":
    # Example usage
    buses_data = pd.DataFrame({
        "bus_id": [1, 2, 3],
        "arrival_time": [2, 4, 7]
    })

    passengers_data = pd.DataFrame({
        "passenger_id": [11, 12, 13, 14],
        "arrival_time": [1, 5, 6, 7]
    })

    print(count_passengers_in_bus(buses_data, passengers_data))
