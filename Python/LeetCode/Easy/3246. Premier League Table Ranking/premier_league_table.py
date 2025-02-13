import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the points and ranking for each team in the league.

    Points are awarded as follows:
    - 3 points for a win
    - 1 point for a draw
    - 0 points for a loss

    Teams with the same points must have the same ranking, and results should be ordered
    by points (descending), then by team name (ascending).

    Parameters:
    team_stats (pd.DataFrame): A DataFrame containing team performance statistics with columns:
                               - 'team_id' (int): Unique identifier for each team.
                               - 'team_name' (str): Name of the football team.
                               - 'matches_played' (int): Total matches played.
                               - 'wins' (int): Number of wins.
                               - 'draws' (int): Number of draws.
                               - 'losses' (int): Number of losses.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'team_id' (int): Unique team identifier.
                  - 'team_name' (str): Name of the football team.
                  - 'points' (int): Total points based on wins and draws.
                  - 'position' (int): Rank based on points (same points = same rank).
                  The result is sorted by 'points' (descending) and then by 'team_name' (ascending).
    """
    # Calculate total points: 3 points per win, 1 point per draw, 0 points per loss
    team_stats["points"] = team_stats["wins"] * 3 + team_stats["draws"]

    # Assign ranking based on points (descending order), using "min" method to handle ties
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False).astype(int)

    # Select relevant columns and sort the results
    return team_stats[["team_id", "team_name", "points", "position"]].sort_values(
        by=["points", "team_name"], ascending=[False, True]
    )


def main():
    """
    Main function to demonstrate the calculate_team_standings function with a sample dataset.
    """
    # Sample team statistics data
    team_stats_data = {
        "team_id": [1, 2, 3, 4, 5],
        "team_name": ["Manchester City", "Liverpool", "Chelsea", "Arsenal", "Tottenham"],
        "matches_played": [10, 10, 10, 10, 10],
        "wins": [6, 6, 5, 4, 3],
        "draws": [2, 2, 3, 4, 5],
        "losses": [2, 2, 2, 2, 2],
    }

    # Convert dictionary to DataFrame
    team_stats_df = pd.DataFrame(team_stats_data)

    # Calculate team standings
    result = calculate_team_standings(team_stats_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
