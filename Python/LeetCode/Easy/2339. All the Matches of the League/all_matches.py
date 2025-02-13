import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    """
    Generates all possible matchups in a league where each team plays against every other team twice
    (once as the home team and once as the away team).

    Args:
        teams (pd.DataFrame): A DataFrame containing a column "team_name" with unique team names.

    Returns:
        pd.DataFrame: A DataFrame with two columns, "home_team" and "away_team", containing all possible matches.
    """

    # Perform a cross join to get all possible combinations of teams
    matches = (
        teams
        .merge(teams, how="cross", suffixes=("_home", "_away"))
        .rename(columns={"team_name_home": "home_team", "team_name_away": "away_team"})
    )

    # Remove cases where a team plays against itself
    matches = matches.query("home_team != away_team")

    return matches

def main():
    # Sample data
    teams_data = {
        "team_name": ["Real Madrid", "Leetcode FC", "Ahly SC"]
    }

    # Create DataFrame
    teams_df = pd.DataFrame(teams_data)

    # Find all matches
    result = find_all_matches(teams_df)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
