import pandas as pd

def get_top_performing_drivers(drivers_df, vehicles_df, trips_df):
    """
    Returns the top-performing driver for each fuel type based on:
    1. Average rating (rounded to 2 decimal places)
    2. Total distance traveled (if rating is the same)
    3. Fewest accidents (if both rating and distance are the same)

    The result is ordered by fuel_type in ascending order.
    """
    # Step 1: Merge the DataFrames
    merged_df = pd.merge(trips_df, vehicles_df, on='vehicle_id', how='inner')
    merged_df = pd.merge(merged_df, drivers_df, on='driver_id', how='inner')

    # Step 2: Group by fuel_type, driver_id, and accidents to calculate avg_rating and total_distance
    performance_df = merged_df.groupby(['fuel_type', 'driver_id', 'accidents']).agg(
        avg_rating=('rating', lambda x: round(x.mean(), 2)),
        total_distance=('distance', 'sum')
    ).reset_index()

    # Step 3: Sort by fuel_type, avg_rating (descending), total_distance (descending), and accidents (ascending)
    performance_df = performance_df.sort_values(
        by=['fuel_type', 'avg_rating', 'total_distance', 'accidents'],
        ascending=[True, False, False, True]
    )

    # Step 4: Rank drivers per fuel_type (selecting the top one for each fuel_type)
    top_performers_df = performance_df.groupby('fuel_type').head(1).reset_index(drop=True)

    # Step 5: Return the final result with the required columns
    result_df = top_performers_df[['fuel_type', 'driver_id', 'avg_rating', 'total_distance']]
    result_df.rename(columns={'avg_rating': 'rating', 'total_distance': 'distance'}, inplace=True)

    return result_df


def main():
    # Example data for testing
    drivers_data = {
        'driver_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [34, 45, 28],
        'experience': [10, 20, 5],
        'accidents': [3, 1, 0]
    }

    vehicles_data = {
        'vehicle_id': [100, 101, 102],
        'driver_id': [1, 2, 3],
        'model': ['Sedan', 'SUV', 'Coupe'],
        'fuel_type': ['Gasoline', 'Electric', 'Gasoline'],
        'mileage': [20000, 30000, 15000]
    }

    trips_data = {
        'trip_id': [201, 202, 203, 204, 205],
        'vehicle_id': [100, 100, 101, 102, 102],
        'distance': [50, 60, 30, 40, 60],
        'duration': [30, 40, 20, 40, 40],
        'rating': [5, 4, 5, 5, 5]
    }

    # Create DataFrames
    drivers_df = pd.DataFrame(drivers_data)
    vehicles_df = pd.DataFrame(vehicles_data)
    trips_df = pd.DataFrame(trips_data)

    # Get the top-performing drivers
    result_df = get_top_performing_drivers(drivers_df, vehicles_df, trips_df)

    # Display the result
    print("Top Performing Drivers:")
    print(result_df)


if __name__ == "__main__":
    main()
