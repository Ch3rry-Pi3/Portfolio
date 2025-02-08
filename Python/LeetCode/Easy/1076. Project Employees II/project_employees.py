import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the project(s) with the most employees assigned.

    :param project: DataFrame containing 'project_id' and 'employee_id' pairs.
    :param employee: DataFrame (not used, but included for completeness).
    :return: DataFrame containing only the project_id(s) with the highest employee count.
    """

    # Count employees per project
    df = project.groupby("project_id", as_index=False)["employee_id"].count()
    max_count = df["employee_id"].max()         # Get the highest employee count

    # Return only the project(s) with the maximum count
    return df.loc[df["employee_id"] == max_count, ["project_id"]]


def main():
    """
    Demonstrates testing the project_employees function on sample data.
    """
    # Example project data with employee assignments
    project_data = {
        "project_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
        "employee_id": [101, 102, 103, 201, 202, 301, 302, 303, 304],
    }

    # Convert to DataFrame
    project_df = pd.DataFrame(project_data)

    print("Original Project Table:")
    print(project_df, "\n")

    # Compute the project(s) with the most employees
    top_projects = project_employees(project_df, pd.DataFrame())

    print("Project(s) with the Most Employees:")
    print(top_projects)


if __name__ == "__main__":
    main()
