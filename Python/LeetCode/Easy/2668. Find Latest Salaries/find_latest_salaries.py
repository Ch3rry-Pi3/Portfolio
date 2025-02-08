import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the latest salary record for each employee.

    Since salaries increase each year, the latest salary is the highest salary for each employee.
    The result is ordered by 'emp_id' in ascending order.

    :param salary: DataFrame containing employee salary records.
    :return: DataFrame with latest salary records sorted by 'emp_id'.
    """

    return (
        salary.sort_values(['emp_id', 'salary'])        # Sort by emp_id (ascending) and salary (ascending)
        .drop_duplicates('emp_id', keep='last')         # Keep the last occurrence (latest salary)
    )


def main():
    """
    Demonstrates testing the find_latest_salaries function on sample data.
    """
    # Example salary data with outdated salaries
    salary_data = {
        "emp_id": [1, 1, 2, 2, 3, 3, 4, 5, 6, 6],
        "firstname": ["Todd", "Todd", "Justin", "Justin", "Kelly", "Kelly", "Patricia", "Sherry", "Natasha", "Natasha"],
        "lastname": ["Wilson", "Wilson", "Simon", "Simon", "Rosario", "Rosario", "Powell", "Golden", "Swanson", "Swanson"],
        "salary": [110000, 116119, 130000, 110985, 46800, 47000, 16285, 44101, 79928, 90000],
        "department_id": ["D105", "D105", "D105", "D105", "D102", "D102", "D102", "D102", "D104", "D105"]
    }

    # Convert to DataFrame
    salary_df = pd.DataFrame(salary_data)

    print("Original Salary Table:")
    print(salary_df, "\n")

    # Compute the latest salaries
    latest_salaries = find_latest_salaries(salary_df)

    print("Latest Salary Table:")
    print(latest_salaries)


if __name__ == "__main__":
    main()
