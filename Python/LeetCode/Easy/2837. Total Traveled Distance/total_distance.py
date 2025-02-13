import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total traveled distance for each user by summing up the distance from the rides dataset.
    If a user has no recorded rides, their traveled distance is set to 0.

    Parameters:
    users (pd.DataFrame): A DataFrame containing user information with columns:
                          - 'user_id' (int): Unique identifier for each user.
                          - Other user-specific attributes.

    rides (pd.DataFrame): A DataFrame containing ride details with columns:
                          - 'user_id' (int): The user associated with each ride.
                          - 'distance' (float): Distance covered in each ride.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - All columns from `users`.
                  - A new column 'traveled distance' with the total distance traveled by each user.
                  - Sorted by 'user_id' in ascending order.
    """
    # Aggregate total distance per user
    grouped = rides.groupby(by="user_id", as_index=False).agg(distance=("distance", "sum"))

    # Merge with users dataset and handle missing values
    result = (
        pd.merge(users, grouped, on="user_id", how="left")
        .sort_values(by="user_id", ascending=True)
        .fillna(0)  # Users with no rides get a traveled distance of 0
        .rename(columns={"distance": "traveled distance"})
    )

    return result


def main():
    """
    Main function to demonstrate the get_total_distance function with sample datasets.
    """
    # Sample users data
    users_data = {
        "user_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"]
    }

    # Sample rides data
    rides_data = {
        "user_id": [1, 1, 2, 2, 2, 3],
        "distance": [5.0, 10.0, 3.5, 2.0, 7.5, 8.0]
    }

    # Convert dictionaries to DataFrames
    users_df = pd.DataFrame(users_data)
    rides_df = pd.DataFrame(rides_data)

    # Compute total traveled distance per user
    result = get_total_distance(users_df, rides_df)
    
    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
