import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies students who have shown improvement in their scores across multiple exam dates.

    A student is considered to have improved in a subject if:
    1. They have taken exams in the same subject on at least two different dates.
    2. Their latest score in that subject is higher than their first score.

    Parameters:
    scores (pd.DataFrame): A DataFrame containing student scores with the following columns:
        - student_id (int): The ID of the student.
        - subject (str): The subject of the exam.
        - score (int): The score achieved in the exam (0 to 100).
        - exam_date (str): The date of the exam in YYYY-MM-DD format.

    Returns:
    pd.DataFrame: A DataFrame with columns:
        - student_id
        - subject
        - first_score (earliest score in the subject)
        - latest_score (most recent score in the subject)
    """

    # Sort values to ensure correct first and last scores
    scores_sorted = scores.sort_values(by=["student_id", "subject", "exam_date"], ascending=True)

    # Compute first and last score for each student-subject pair
    scores_sorted["first_score"] = scores_sorted.groupby(["student_id", "subject"])["score"].transform("first")
    scores_sorted["latest_score"] = scores_sorted.groupby(["student_id", "subject"])["score"].transform("last")

    # Filter only students who showed improvement
    improved_students = scores_sorted.query("first_score < latest_score")[["student_id", "subject", "first_score", "latest_score"]].drop_duplicates()

    return improved_students


def main():
    """
    Main function to demonstrate the find_students_who_improved() function.
    """

    # Sample data
    data = {
        "student_id": [101, 101, 101, 101, 102, 102, 103, 104, 104],
        "subject": ["Math", "Math", "Physics", "Physics", "Math", "Math", "Math", "Physics", "Physics"],
        "score": [70, 85, 65, 60, 80, 85, 90, 75, 85],
        "exam_date": ["2023-01-15", "2023-02-15", "2023-01-15", "2023-02-15",
                      "2023-01-15", "2023-02-15", "2023-02-15", "2023-01-15", "2023-02-15"]
    }

    # Create DataFrame
    scores_df = pd.DataFrame(data)

    # Call function and display result
    improved_students = find_students_who_improved(scores_df)
    print(improved_students)


if __name__ == "__main__":
    main()