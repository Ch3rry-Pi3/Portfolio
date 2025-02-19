import pandas as pd

def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the change in global rankings after updating each team's points.

    Args:
        team_points (pd.DataFrame): A DataFrame containing the initial points of each team with columns:
            - "team_id" (int): Unique team identifier.
            - "name" (str): Team name.
            - "points" (int): Current ranking points.
        
        points_change (pd.DataFrame): A DataFrame containing point changes for each team with columns:
            - "team_id" (int): Unique team identifier.
            - "points_change" (int): Change in points (positive, negative, or zero).

    Returns:
        pd.DataFrame: A DataFrame containing:
            - "team_id" (int): Unique team identifier.
            - "name" (str): Team name.
            - "rank_diff" (int): Difference in ranking before and after updating points.
    """
    # Merge team points with points change
    df = pd.merge(left=team_points, right=points_change, on="team_id", how="left")

    # Rank teams based on initial points (descending order, then lexicographically by name)
    df = df.sort_values(by=["points", "name"], ascending=[False, True]).assign(
        rank_points=range(1, len(df) + 1)           # Assign initial rankings
    )

    # Update team points based on the change
    df = df.assign(new_points=lambda x: x["points"] + x["points_change"])

    # Rank teams again after updating points
    df = df.sort_values(by=["new_points", "name"], ascending=[False, True]).assign(
        rank_new_points=range(1, len(df) + 1)  # Assign new rankings
    )

    # Calculate the rank difference
    df = df.assign(rank_diff=lambda x: x["rank_points"] - x["rank_new_points"])

    # Return the final DataFrame with required columns
    return df[["team_id", "name", "rank_diff"]]

if __name__ == "__main__":
    # Example input data
    team_points_df = pd.DataFrame({
        "team_id": [3, 2, 1, 4],
        "name": ["Algeria", "Senegal", "New Zealand", "Croatia"],
        "points": [1431, 2132, 1402, 1817]
    })

    points_change_df = pd.DataFrame({
        "team_id": [3, 2, 1, 4],
        "points_change": [399, 0, 13, -22]
    })

    # Compute ranking changes
    result = global_ratings_change(team_points_df, points_change_df)

    # Print the output
    print(result)
