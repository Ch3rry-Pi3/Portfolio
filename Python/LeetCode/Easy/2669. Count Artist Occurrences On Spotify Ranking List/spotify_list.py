import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of unique song occurrences for each artist and sorts the result.

    Parameters:
    spotify (pd.DataFrame): A DataFrame containing song data with columns:
                            - 'id' (str/int): Unique identifier for each song.
                            - 'artist' (str): The name of the artist.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'artist' (str): The name of the artist.
                  - 'occurrences' (int): The number of unique songs by the artist.
                  The result is sorted by:
                  - 'occurrences' in descending order.
                  - 'artist' in ascending order (A-Z) in case of ties.
    """
    return (
        spotify
        .groupby("artist", as_index=False)["id"]
        .nunique()
        .sort_values(by=["id", "artist"], ascending=[False, True])
        .rename(columns={"id": "occurrences"})
    )


def main():
    """
    Main function to demonstrate the count_occurrences function with a sample dataset.
    """
    # Sample input data
    data = {
        "id": [1, 2, 3, 4, 5, 1, 6, 7, 8, 2, 9],
        "artist": [
            "Adele", "Adele", "Drake", "Drake", "Drake", "Adele", 
            "Beyoncé", "Beyoncé", "Coldplay", "Adele", "Coldplay"
        ]
    }

    # Convert dictionary to DataFrame
    spotify_df = pd.DataFrame(data)

    # Process and display the transformed DataFrame
    result = count_occurrences(spotify_df)
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
