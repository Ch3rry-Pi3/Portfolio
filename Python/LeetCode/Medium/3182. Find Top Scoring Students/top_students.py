import pandas as pd

def find_top_scoring_students(enrollments: pd.DataFrame, students: pd.DataFrame, courses: pd.DataFrame) -> pd.DataFrame:
    """
    Finds students who have taken all courses in their major and earned an 'A' in all.
    
    :param enrollments: pd.DataFrame - Contains student_id, course_id, semester, grade.
    :param students: pd.DataFrame - Contains student_id, name, major.
    :param courses: pd.DataFrame - Contains course_id, name, credits, major.
    
    :return: pd.DataFrame - A list of student IDs who qualify as top-scoring students.
    """
    
    # Merge students with courses to determine the required courses for their major
    students_major = pd.merge(students, courses, how='inner', on='major')
    
    # Merge with enrollments to see which courses each student took and their grades
    students_grades = pd.merge(students_major, enrollments, how='left', on=['student_id', 'course_id'], indicator=True)
    
    # Find students who missed a course OR didn't get an A
    no_good_students = students_grades.query("_merge == 'left_only' or grade != 'A'")
    
    # Keep students who took all required courses and got all A's
    result = students_major[~students_major['student_id'].isin(no_good_students['student_id'])]
    
    return result[['student_id']].sort_values('student_id').drop_duplicates()


def main():
    """
    Runs a sample test case for the function.
    """
    # Sample data
    students_data = {
        "student_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "major": ["Computer Science", "Computer Science", "Mathematics", "Mathematics"],
    }
    
    courses_data = {
        "course_id": [101, 102, 103, 104],
        "name": ["Algorithms", "Data Structures", "Calculus", "Linear Algebra"],
        "credits": [3, 3, 4, 4],
        "major": ["Computer Science", "Computer Science", "Mathematics", "Mathematics"],
    }
    
    enrollments_data = {
        "student_id": [1, 1, 2, 2, 3, 3, 4],
        "course_id": [101, 102, 101, 102, 103, 104, 104],
        "semester": ["Fall 2023"] * 7,
        "grade": ["A", "A", "A", "A", "A", "A", "B"],
    }
    
    students_df = pd.DataFrame(students_data)
    courses_df = pd.DataFrame(courses_data)
    enrollments_df = pd.DataFrame(enrollments_data)
    
    # Find top-scoring students
    result = find_top_scoring_students(enrollments_df, students_df, courses_df)
    
    # Display result
    print(result)


if __name__ == "__main__":
    main()
