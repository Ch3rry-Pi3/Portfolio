import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies cities where the average home price exceeds the national average home price.

    Parameters:
    listings (pd.DataFrame): A DataFrame containing real estate listings with columns:
                             - 'listing_id' (int): Unique identifier for each listing.
                             - 'city' (str): Name of the city.
                             - 'price' (int): Price of the listing.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'city' (str): Cities where the average price exceeds the national average.
                  The result is sorted in ascending order by 'city'.
    """
    # Calculate the national average home price
    national_avg = listings["price"].mean()

    # Compute the average home price per city
    city_avg_prices = listings.groupby("city", as_index=False)["price"].mean()

    # Filter cities with an average price above the national average and sort alphabetically
    expensive_cities = city_avg_prices.loc[city_avg_prices["price"] > national_avg, ["city"]].sort_values(by="city")

    return expensive_cities


def main():
    """
    Main function to demonstrate the find_expensive_cities function with a sample dataset.
    """
    # Sample listings data
    listings_data = {
        "listing_id": [113, 136, 92, 60, 8, 79, 37, 15, 178, 51],
        "city": ["LosAngeles", "SanFrancisco", "Chicago", "Chicago", "Chicago", 
                 "SanFrancisco", "Chicago", "LosAngeles", "SanFrancisco", "NewYork"],
        "price": [7560386, 2380268, 9833299, 5147582, 5274441, 
                  8372065, 7395095, 4965123, 999027, 5951718]
    }

    # Convert dictionary to DataFrame
    listings_df = pd.DataFrame(listings_data)

    # Find expensive cities
    result = find_expensive_cities(listings_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
