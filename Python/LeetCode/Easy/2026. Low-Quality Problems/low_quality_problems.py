import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies low-quality problems based on the like-to-dislike ratio.

    A problem is considered low quality if its like-to-total vote ratio is below 0.6.

    :param problems: DataFrame containing 'problem_id', 'likes', and 'dislikes'.
    :return: DataFrame containing only 'problem_id' of low-quality problems, sorted by 'problem_id'.
    """

    # Compute the like-to-total vote ratio
    problems["ratio"] = problems.apply(
        lambda x: x["likes"] / (x["likes"] + x["dislikes"]), axis=1
    )

    # Filter problems with a ratio lower than 0.6 and return sorted 'problem_id'
    return problems.query("ratio < 0.6")[["problem_id"]].sort_values(by="problem_id")


def main():
    """
    Demonstrates testing the low_quality_problems function with sample datasets.
    """
    # Example Problems Data
    problems_data = {
        "problem_id": [1, 2, 3, 4, 5],
        "likes": [100, 50, 10, 200, 80],
        "dislikes": [50, 80, 100, 50, 60]
    }

    # Convert dictionary to DataFrame
    problems_df = pd.DataFrame(problems_data)

    print("Problems DataFrame:")
    print(problems_df, "\n")

    # Compute low-quality problems
    result = low_quality_problems(problems_df)

    print("Low-Quality Problems:")
    print(result)


if __name__ == "__main__":
    main()
