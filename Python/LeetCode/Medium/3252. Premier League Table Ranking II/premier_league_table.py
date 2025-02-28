import pandas as pd
import numpy as np

def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates team rankings based on points and assigns teams to tiers.

    :param team_stats: DataFrame containing team stats including wins, draws, and losses.
    :return: DataFrame with columns team_name, points, position, and tier.
    """

    # Calculate total points
    team_stats["points"] = (team_stats["wins"] * 3) + (team_stats["draws"] * 1)

    # Rank teams by points (descending), handling ties with "min" ranking
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False)

    # Determine tier cutoffs
    num_teams = team_stats["team_id"].nunique()
    top_cutoff = np.ceil(num_teams * 0.33)
    bottom_cutoff = np.ceil(num_teams * (1 - 0.33))

    # Assign tiers based on cutoffs
    team_stats["tier"] = np.where(
        team_stats["position"] <= top_cutoff, "Tier 1",
        np.where(team_stats["position"] > bottom_cutoff, "Tier 3", "Tier 2")
    )

    # Return the result sorted by points (descending), then team_name (ascending)
    return team_stats[["team_name", "points", "position", "tier"]].sort_values(
        by=["points", "team_name"], ascending=[False, True]
    )

# Main function for testing
def main():
    data = {
        "team_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "team_name": ["Chelsea", "Nottingham Forest", "Liverpool", "Aston Villa", 
                      "Fulham", "Burnley", "Newcastle United", "Sheffield United", 
                      "Luton Town", "Everton"],
        "matches_played": [22, 27, 17, 20, 31, 26, 33, 20, 5, 14],
        "wins": [13, 6, 1, 3, 18, 6, 11, 18, 4, 2],
        "draws": [2, 6, 8, 6, 1, 9, 10, 2, 0, 6],
        "losses": [7, 15, 8, 11, 12, 11, 12, 0, 1, 6]
    }

    team_stats = pd.DataFrame(data)
    result = calculate_team_tiers(team_stats)
    print(result)

if __name__ == "__main__":
    main()
