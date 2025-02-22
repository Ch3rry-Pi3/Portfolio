import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the manager of the largest department(s) based on employee count.

    Args:
        employees (pd.DataFrame): Contains employee data with columns:
            - "emp_id" (int): The ID of the employee.
            - "emp_name" (str): The name of the employee.
            - "dep_id" (int): The department ID.
            - "position" (str): The job title of the employee.

    Returns:
        pd.DataFrame: A table containing:
            - "manager_name" (str): The name of the manager of the largest department(s).
            - "dep_id" (int): The department ID of the largest department(s).
        
        The result is sorted by "dep_id" in ascending order.
    """
    return (
        employees
        # Compute department employee count and maximum employee count
        .assign(
            emp_count=lambda x: x.groupby("dep_id")["emp_id"].transform("count"),
            max_emp_count=lambda x: x["emp_count"].max()
        )
        # Filter for managers in the largest department(s)
        .query("emp_count == max_emp_count and position == 'Manager'")
        # Keep only required columns and sort by department ID
        [["emp_name", "dep_id"]]
        .sort_values(by="dep_id")
        # Rename columns to match expected output
        .rename(columns={"emp_name": "manager_name"})
    )


if __name__ == "__main__":
    # Example usage
    employees_data = pd.DataFrame({
        "emp_id": [156, 112, 8, 16, 80, 67, 156, 97, 3, 13],
        "emp_name": ["Michael", "Lucas", "Isabella", "Joseph", "Aiden", "Skylar", "Stella", "Nathan", "Ethan", "Audrey"],
        "dep_id": [107, 107, 101, 100, 107, 101, 101, 101, 107, 101],
        "position": ["Manager", "Consultant", "Manager", "Manager", "Engineer", "Freelancer", "Coordinator", "Supervisor", "Administrator", "Consultant"]
    })

    print(find_manager(employees_data))
