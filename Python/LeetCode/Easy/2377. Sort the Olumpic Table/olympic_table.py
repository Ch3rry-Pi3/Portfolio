import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    """
    Sorts the Olympic medal table based on the number of medals won.
    Sorting order:
        - Gold medals (Descending)
        - Silver medals (Descending)
        - Bronze medals (Descending)
        - Country name (Ascending, in case of a tie)

    Args:
        olympic (pd.DataFrame): A DataFrame containing columns "country", "gold_medals",
                                "silver_medals", and "bronze_medals".

    Returns:
        pd.DataFrame: The sorted DataFrame.
    """

    return olympic.sort_values(
        by=["gold_medals", "silver_medals", "bronze_medals", "country"],
        ascending=[False, False, False, True]
    )

def main():
    """ Example usage of the `sort_table` function. """

    # Sample data
    olympic_data = {
        "country": ["USA", "China", "Russia", "UK", "Germany"],
        "gold_medals": [39, 38, 22, 20, 17],
        "silver_medals": [41, 32, 21, 21, 20],
        "bronze_medals": [33, 18, 20, 22, 19],
    }

    # Create DataFrame
    olympic_df = pd.DataFrame(olympic_data)

    # Sort the table
    sorted_table = sort_table(olympic_df)

    # Display results
    print(sorted_table)

if __name__ == "__main__":
    main()
