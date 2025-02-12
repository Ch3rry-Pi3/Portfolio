import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the absolute difference between the highest salaries in the 
    Engineering and Marketing departments.

    Args:
        salaries (pd.DataFrame): A DataFrame with columns:
            - emp_name (str): Employee name.
            - department (str): Department name.
            - salary (int): Employee's salary.

    Returns:
        pd.DataFrame: A DataFrame containing a single column 'salary_difference' 
                      representing the absolute difference between the highest 
                      salaries in the two departments.
    """
    
    # Group by department and get the highest salary for each department
    df = salaries.groupby("department", as_index=False)["salary"].max()
    
    # Compute the absolute salary difference between Engineering and Marketing
    df["salary_difference"] = abs(
        df.loc[df.department == "Engineering", "salary"].values[0] - 
        df.loc[df.department == "Marketing", "salary"].values[0]
    )
    
    # Return the result in the required format
    return df[["salary_difference"]].drop_duplicates()

if __name__ == "__main__":
    # Example usage with sample data
    data = {
        "emp_name": ["Kathy", "Roy", "Charles", "Jack", "Benjamin", 
                     "Anthony", "Edward", "Terry", "Evelyn", "Arthur"],
        "department": ["Engineering", "Marketing", "Engineering", "Engineering", 
                       "Marketing", "Marketing", "Engineering", "Engineering", 
                       "Marketing", "Engineering"],
        "salary": [50000, 30000, 45000, 55000, 34000, 42000, 110000, 102000, 53000, 120000]
    }

    salaries_df = pd.DataFrame(data)
    result = salaries_difference(salaries_df)
    print(result)
