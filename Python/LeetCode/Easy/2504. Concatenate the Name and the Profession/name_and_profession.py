import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the 'name' column by appending the first letter of the 'profession' in parentheses.
    Sorts the DataFrame in descending order by 'person_id'.

    Parameters:
    person (pd.DataFrame): A DataFrame containing columns:
                           - 'person_id' (int): Unique ID for each person.
                           - 'name' (str): Person's name.
                           - 'profession' (str): Profession of the person.

    Returns:
    pd.DataFrame: A DataFrame with two columns:
                  - 'person_id': Unique ID (sorted in descending order).
                  - 'name': Modified name in the format "Name(P)" where P is the first letter of 'profession'.
    """
    # Modify the 'name' column to include the first letter of 'profession' in parentheses
    person["name"] = person.apply(lambda x: f"{x['name']}({x['profession'][0].upper()})", axis=1)

    # Return the DataFrame with selected columns, sorted by 'person_id' in descending order
    return person[["person_id", "name"]].sort_values(by="person_id", ascending=False)


def main():
    """
    Main function to demonstrate the concatenate_info function with a sample dataset.
    """
    # Sample input data
    data = {
        "person_id": [101, 102, 103, 104],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "profession": ["engineer", "doctor", "artist", "scientist"]
    }

    # Convert dictionary to DataFrame
    person_df = pd.DataFrame(data)

    # Process and display the transformed DataFrame
    result = concatenate_info(person_df)
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
