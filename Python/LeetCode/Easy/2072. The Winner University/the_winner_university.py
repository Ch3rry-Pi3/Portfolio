import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the winning university based on the number of excellent students.

    An excellent student is one who scores 90 or above.
    The university with the most excellent students wins.
    If both universities have the same number of excellent students, it's a draw.

    :param new_york: DataFrame containing New York University student scores.
    :param california: DataFrame containing California University student scores.
    :return: DataFrame with a single column 'winner' indicating the winning university.
    """

    # Count excellent students (score >= 90) in each university
    ny_excel = len(new_york[new_york['score'] >= 90])
    cal_excel = len(california[california['score'] >= 90])

    # Determine the winner based on the count
    if ny_excel > cal_excel:
        result = 'New York University'
    elif cal_excel > ny_excel:
        result = 'California University'
    else:
        result = 'No Winner'        # It's a draw

    # Return the result in a DataFrame format
    return pd.DataFrame({'winner': [result]})


def main():
    """
    Demonstrates testing the find_winner function with sample datasets.
    """
    # Example Data: New York University
    ny_data = {
        "student_id": [1, 2, 3],
        "score": [91, 80, 87]
    }

    # Example Data: California University
    cal_data = {
        "student_id": [1, 2, 3],
        "score": [89, 90, 88]
    }

    # Convert dictionaries to DataFrames
    ny_df = pd.DataFrame(ny_data)
    cal_df = pd.DataFrame(cal_data)

    print("New York University Scores:")
    print(ny_df, "\n")

    print("California University Scores:")
    print(cal_df, "\n")

    # Compute the winning university
    result = find_winner(ny_df, cal_df)

    print("Winner:")
    print(result)


if __name__ == "__main__":
    main()
