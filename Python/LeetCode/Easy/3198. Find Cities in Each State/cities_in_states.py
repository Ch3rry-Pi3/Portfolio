import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates all cities within each state into a single comma-separated string.

    The result is sorted by:
    - 'state' (ascending)
    - 'city' (ascending) before aggregation.

    Parameters:
    cities (pd.DataFrame): A DataFrame containing city and state information with columns:
                           - 'state' (str): Name of the state.
                           - 'city' (str): Name of the city.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'state' (str): The name of the state.
                  - 'cities' (str): A comma-separated string of city names sorted alphabetically.
                  The result is sorted by 'state' in ascending order.
    """
    # Sort cities first by state and then by city name
    sorted_cities = cities.sort_values(by=["state", "city"])

    # Group by state and concatenate city names into a comma-separated string
    grouped_cities = sorted_cities.groupby("state", as_index=False).agg(cities=("city", ", ".join))

    # Return sorted result by state
    return grouped_cities.sort_values(by="state")


def main():
    """
    Main function to demonstrate the find_cities function with a sample dataset.
    """
    # Sample cities data
    cities_data = {
        "state": [
            "California", "California", "California",
            "Texas", "Texas", "Texas",
            "New York", "New York", "New York"
        ],
        "city": [
            "Los Angeles", "San Francisco", "San Diego",
            "Houston", "Austin", "Dallas",
            "New York City", "Buffalo", "Rochester"
        ]
    }

    # Convert dictionary to DataFrame
    cities_df = pd.DataFrame(cities_data)

    # Find cities grouped by state
    result = find_cities(cities_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
