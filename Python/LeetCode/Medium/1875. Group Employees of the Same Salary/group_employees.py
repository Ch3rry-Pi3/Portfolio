import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Groups employees into teams based on their salaries.

    Employees with the same salary are assigned to the same team, provided there are at least 
    two employees with that salary. Each team's ID is assigned based on the ranking of its salary.

    Args:
        employees (pd.DataFrame): A DataFrame containing the following columns:
            - "employee_id" (int): Unique ID for each employee.
            - "name" (str): Employee's name.
            - "salary" (int): Employee's salary.

    Returns:
        pd.DataFrame: A DataFrame with employees assigned to teams, sorted by "team_id" and "employee_id".
                      Columns:
                      - "employee_id" (int): Employee's ID.
                      - "name" (str): Employee's name.
                      - "salary" (int): Employee's salary.
                      - "team_id" (int): The assigned team ID.
    """

    return (
        employees
        .sort_values(by="salary", ascending=True)
        .assign(rnk=lambda x: x["salary"].rank(method="dense"))  # Assign rank based on salary
        .assign(team_count=lambda x: x.groupby("rnk")["rnk"].transform("count"))  # Count occurrences
        .query("team_count > 1")  # Keep only salaries with multiple employees
        .assign(team_id=lambda x: x["salary"].rank(method="dense"))  # Assign team IDs based on ranking
        .drop(columns=["rnk", "team_count"])  # Drop intermediate columns
        .sort_values(by=["team_id", "employee_id"])  # Sort by team_id and employee_id
    )


def main():
    """
    Demonstrates the employees_of_same_salary function with a sample dataset.
    """

    # Sample data
    data = {
        "employee_id": [1, 2, 3, 4, 5, 6, 7],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
        "salary": [5000, 6000, 5000, 7000, 6000, 8000, 5000]
    }

    # Create DataFrame
    employees_df = pd.DataFrame(data)

    # Apply function
    result_df = employees_of_same_salary(employees_df)

    # Display results
    print(result_df)


if __name__ == "__main__":
    main()
