import pandas as pd
import numpy as np

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the post-tax salary for each employee based on company tax rates.

    Args:
        salaries (pd.DataFrame): A DataFrame containing:
            - "company_id" (int): The company ID.
            - "employee_id" (int): The employee ID.
            - "employee_name" (str): The name of the employee.
            - "salary" (int): The pre-tax salary of the employee.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "company_id" (int)
            - "employee_id" (int)
            - "employee_name" (str)
            - "salary" (int): The post-tax salary (rounded).
    """

    # Step 1: Find the max salary for each company
    salaries["max_sal"] = salaries.groupby("company_id")["salary"].transform("max")

    # Step 2: Assign tax rates based on max salary
    salaries["tax_rate"] = salaries["max_sal"].apply(
        lambda x: 1 if x < 1000 else 0.76 if x <= 10000 else 0.51
    )

    # Step 3: Apply tax rate to calculate post-tax salary
    salaries["post_tax"] = (salaries["salary"] * salaries["tax_rate"]).apply(
        lambda x: round(x) if x % 1 != 0.5 else np.ceil(x)
    )

    # Step 4: Clean up the DataFrame
    salaries = salaries.drop(columns=["salary", "max_sal", "tax_rate"]).rename(
        columns={"post_tax": "salary"}
    )

    return salaries


def main():
    """Main function to test calculate_salaries with an example dataset."""

    # Example input DataFrame
    data = {
        "company_id": [1, 1, 1, 1, 1, 2, 3, 3, 3, 3],
        "employee_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "employee_name": [
            "Tony", "Pronub", "Tyrrox", "Pam", "Bassem",
            "Hermione", "Bocaben", "Ognjen", "Nyancat", "Morningcat"
        ],
        "salary": [2000, 21300, 13000, 9000, 450, 700, 100, 3200, 7777, 7777],
    }

    salaries_df = pd.DataFrame(data)

    # Compute post-tax salaries
    result = calculate_salaries(salaries_df)

    # Display the output
    print(result)


if __name__ == "__main__":
    main()
