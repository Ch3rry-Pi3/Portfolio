import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of times each driver has been a passenger.

    Args:
        rides (pd.DataFrame): Contains ride data with columns:
            - "ride_id" (int): Unique ride identifier.
            - "driver_id" (int): The ID of the driver.
            - "passenger_id" (int): The ID of the passenger.

    Returns:
        pd.DataFrame: A table with:
            - "driver_id" (int): Unique driver IDs.
            - "cnt" (int): Number of times the driver was a passenger.
    """
    # Identify drivers who were also passengers
    driver_as_passenger = rides[rides['passenger_id'].isin(rides['driver_id'])]

    # Count occurrences of each driver as a passenger
    passenger_counts = driver_as_passenger.groupby('passenger_id').size().reset_index(name='cnt')

    # Extract unique drivers
    drivers = rides[['driver_id']].drop_duplicates()

    # Merge counts with drivers, fill missing values with 0
    result = (
        drivers.merge(passenger_counts, left_on='driver_id', right_on='passenger_id', how='left')
        .fillna(0)
        .drop(columns=['passenger_id'])
    )

    # Ensure count is an integer
    result['cnt'] = result['cnt'].astype(int)

    # Sort by driver_id for consistency
    return result.sort_values(by='driver_id')


if __name__ == "__main__":
    # Example usage
    example_data = pd.DataFrame({
        "ride_id": [1, 2, 3, 4, 5, 6],
        "driver_id": [7, 7, 7, 11, 11, 11],
        "passenger_id": [1, 2, 7, 3, 4, 5]
    })

    print(driver_passenger(example_data))
