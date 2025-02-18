import pandas as pd

def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the minimum score required for students to apply to each school.

    The school chooses the minimum score requirement based on:
    1. Ensuring that if every student meeting the requirement applies, the school can accept all.
    2. Maximising the possible number of students that can apply.
    3. Selecting a score that is present in the "Exam" table.
    4. If no valid score is found, return -1.

    Args:
        schools (pd.DataFrame): A DataFrame containing school information with columns:
                                - "school_id" (int): Unique school ID.
                                - "capacity" (int): Maximum number of students the school can accept.
        exam (pd.DataFrame): A DataFrame containing exam scores with columns:
                             - "score" (int): A score value in the exam.
                             - "student_count" (int): Number of students who scored at least this score.

    Returns:
        pd.DataFrame: A DataFrame containing:
                      - "school_id" (int): Unique school ID.
                      - "score" (int): The minimum score that meets the conditions, or -1 if none exist.
    """

    # Perform a cross join to associate each school with all exam records
    df = schools.merge(exam, how="cross")

    # Filter out invalid score entries where student count exceeds school capacity
    result = (
        df[df.capacity >= df.student_count]
        .groupby("school_id")["score"]
        .min()
        .reset_index()
        .merge(schools, how="right")        # Ensure all schools are included
        .fillna(-1)                         # Assign -1 if no valid score exists
    )

    # Return the final DataFrame with the required columns
    return result[["school_id", "score"]]


def main():
    """
    Demonstrates the `find_cutoff_score` function with a sample dataset.
    """

    # Sample Schools data
    schools_data = {
        "school_id": [1, 2, 3],
        "capacity": [5, 15, 20]
    }

    # Sample Exam data
    exam_data = {
        "score": [80, 90, 85, 70, 75],
        "student_count": [10, 5, 15, 20, 25]
    }

    # Create DataFrames
    schools_df = pd.DataFrame(schools_data)
    exam_df = pd.DataFrame(exam_data)

    # Apply function
    result_df = find_cutoff_score(schools_df, exam_df)

    # Display results
    print(result_df)


if __name__ == "__main__":
    main()
