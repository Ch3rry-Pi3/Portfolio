import pandas as pd


def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the running total score for each gender on each day.

    Args:
        scores (pd.DataFrame): A DataFrame containing columns:
            - "player_name" (str): Name of the player.
            - "gender" (str): 'F' for female, 'M' for male.
            - "day" (datetime): Date of the game.
            - "score_points" (int): Points scored by the player.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - "gender" (str): Gender category.
            - "day" (datetime): Date of the game.
            - "total" (int): Cumulative total score per gender.
    """
    return (
        scores
        .sort_values(by=["gender", "day"], ascending=[True, True])
        .assign(total=lambda x: x.groupby("gender")["score_points"].cumsum())
        [["gender", "day", "total"]]
    )


def main():
    # Sample input data
    data = {
        "player_name": ["Aron", "Alice", "Bajrang", "Khali", "Slaman", "Joe", "Jose", "Priya", "Priyanka"],
        "gender": ["F", "F", "M", "M", "M", "M", "M", "F", "F"],
        "day": pd.to_datetime([
            "2020-01-01", "2020-01-07", "2020-01-07", "2019-12-25",
            "2019-12-30", "2019-12-31", "2019-12-18", "2019-12-31", "2019-12-30"
        ]),
        "score_points": [17, 23, 7, 11, 13, 3, 2, 23, 17],
    }

    scores_df = pd.DataFrame(data)

    # Compute running total
    result = running_total(scores_df)

    # Display results
    print(result)


if __name__ == "__main__":
    main()
