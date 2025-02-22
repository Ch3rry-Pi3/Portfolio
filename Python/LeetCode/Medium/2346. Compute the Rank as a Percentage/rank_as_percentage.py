import pandas as pd
import numpy as np

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the rank percentage of each student within their department.

    Args:
        students (pd.DataFrame): Contains student performance data with columns:
            - "student_id" (int): The ID of the student.
            - "department_id" (int): The ID of the department.
            - "mark" (int): The student's exam mark.

    Returns:
        pd.DataFrame: A table containing:
            - "student_id" (int): The ID of the student.
            - "department_id" (int): The department ID.
            - "percentage" (float): The rank as a percentage (rounded to two decimal places).

        The result is sorted by "department_id" and "percentage" in ascending order.
    """
    # Compute rank within each department (higher marks get a better rank)
    students = students.assign(
        rank=students.groupby("department_id")["mark"].rank(method="min", ascending=False),
        num_of_students=students.groupby("department_id")["student_id"].transform("count")
    )

    # Compute percentage based on the formula provided
    students = students.assign(
        percentage=np.where(
            students["num_of_students"] > 1,
            round((students["rank"] - 1) * 100 / (students["num_of_students"] - 1), 2),
            0.0  # If only one student in the department, percentage is 0.0
        )
    )

    # Select required columns and sort by department and percentage
    return students[["student_id", "department_id", "percentage"]].sort_values(["department_id", "percentage"])


if __name__ == "__main__":
    # Example usage
    students_data = pd.DataFrame({
        "student_id": [2, 2, 1, 7, 3],
        "department_id": [2, 2, 1, 1, 1],
        "mark": [650, 650, 610, 530, 530]
    })

    print(compute_rating(students_data))
