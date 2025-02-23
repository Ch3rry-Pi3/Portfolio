import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    """
    Rearranges the Genders table so that rows alternate between 'female', 'other', and 'male',
    with user IDs sorted in ascending order within each gender.

    Args:
        genders (pd.DataFrame): A DataFrame containing:
            - "user_id" (int): The unique ID of the user.
            - "gender" (str): The gender of the user ('female', 'male', 'other').

    Returns:
        pd.DataFrame: A table with:
            - "user_id" (int): The unique user ID.
            - "gender" (str): The gender of the user.

        The table is arranged in a cyclic order of ('female', 'other', 'male') while maintaining 
        ascending order within each gender.
    """

    # Assign a rank within each gender based on user_id's ascending order
    genders['rn'] = genders.groupby('gender')['user_id'].rank(method='first', ascending=True).astype(int)

    # Assign numerical ordering for cyclic sorting: female -> 1, other -> 2, male -> 3
    genders['rn2'] = genders['gender'].map({'female': 1, 'other': 2, 'male': 3})

    # Sort by rank first, then by gender order
    genders = genders.sort_values(by=['rn', 'rn2'])

    return genders[['user_id', 'gender']]


if __name__ == "__main__":
    # Example usage
    example_data = pd.DataFrame({
        "user_id": [4, 7, 1, 5, 3, 6, 9, 8, 2],
        "gender": ["male", "female", "other", "male", "female", "other", "female", "male", "other"]
    })

    print(arrange_table(example_data))
