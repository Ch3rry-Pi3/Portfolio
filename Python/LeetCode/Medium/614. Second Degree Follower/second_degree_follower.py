import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies second-degree followers in a social network.

    A second-degree follower is a user who:
    - Follows at least one user.
    - Is followed by at least one user.

    Args:
        follow (pd.DataFrame): A DataFrame containing social network connections with columns:
            - "followee" (str): The user being followed.
            - "follower" (str): The user following another user.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "follower" (str): The second-degree followers.
            - "num" (int): The count of their followers.
    """
    return (
        follow[follow["followee"].isin(follow["follower"])]
        .groupby("followee", as_index=False)
        .agg(num=("follower", "count"))
        .rename(columns={"followee": "follower"})
        .sort_values(by="follower", ascending=True)
    )

if __name__ == "__main__":
    # Example data
    data = {
        "followee": ["Alice", "Bob", "Bob", "Donald"],
        "follower": ["Bob", "Cena", "Donald", "Edward"]
    }
    
    follow_df = pd.DataFrame(data)
    
    # Compute second-degree followers
    result = second_degree_follower(follow_df)
    
    # Display the result
    print(result)
