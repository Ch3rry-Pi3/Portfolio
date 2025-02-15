import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of students in each department and return the result sorted by student count
    in descending order. If two departments have the same number of students, sort by department name.

    Args:
        student (pd.DataFrame): DataFrame containing student details with 'student_id' and 'dept_id'.
        department (pd.DataFrame): DataFrame containing department details with 'dept_id' and 'dept_name'.

    Returns:
        pd.DataFrame: A DataFrame with 'dept_name' and 'student_number' sorted as required.
    """
    return (
        department
        .merge(student, on="dept_id", how="left")  # Merge to ensure all departments are included
        .groupby("dept_name", as_index=False)
        .agg(student_number=("student_id", "count"))  # Count students per department
        .sort_values(by=["student_number", "dept_name"], ascending=[False, True])  # Sort by requirements
    )

# Example usage
if __name__ == "__main__":
    student_data = pd.DataFrame({
        "student_id": [1, 2, 3],
        "student_name": ["Jack", "Jane", "Mark"],
        "gender": ["M", "F", "M"],
        "dept_id": [1, 1, 2]
    })

    department_data = pd.DataFrame({
        "dept_id": [1, 2, 3],
        "dept_name": ["Engineering", "Science", "Law"]
    })

    result = count_students(student_data, department_data)
    print(result)
