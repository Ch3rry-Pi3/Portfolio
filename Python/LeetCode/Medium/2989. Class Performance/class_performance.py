import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the difference between the highest and lowest total scores 
    obtained by students in the class.

    Args:
        scores (pd.DataFrame): Contains student performance data with columns:
            - "student_id" (int): The ID of the student.
            - "student_name" (str): The name of the student.
            - "assignment1" (int): Score for Assignment 1.
            - "assignment2" (int): Score for Assignment 2.
            - "assignment3" (int): Score for Assignment 3.

    Returns:
        pd.DataFrame: A table containing:
            - "difference_in_score" (int): The difference between the highest 
              and lowest total scores in the class.
    """
    return (
        scores
        # Ensure missing values are treated as zero
        .fillna(0)
        # Compute the total score for each student
        .assign(total_score=lambda x: x["assignment1"] + x["assignment2"] + x["assignment3"])
        # Compute the difference between the highest and lowest total scores
        .assign(difference_in_score=lambda x: x["total_score"].max() - x["total_score"].min())
        # Keep only the required column
        [["difference_in_score"]]
        # Ensure only a single-row output
        .head(1)
    )


if __name__ == "__main__":
    # Example usage
    scores_data = pd.DataFrame({
        "student_id": [309, 321, 328, 111, 896, 235],
        "student_name": ["Owen", "Claire", "Julian", "Peyton", "David", "Camila"],
        "assignment1": [88, 98, 100, 60, 32, 31],
        "assignment2": [47, 51, 64, 45, 53, 53],
        "assignment3": [87, 43, 43, 64, 29, 69]
    })

    print(class_performance(scores_data))
