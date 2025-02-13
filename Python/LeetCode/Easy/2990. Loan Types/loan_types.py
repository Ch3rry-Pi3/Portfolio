import pandas as pd

def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    """
    Finds distinct user IDs that have at least one 'Refinance' loan type 
    and at least one 'Mortgage' loan type.

    Parameters:
    loans (pd.DataFrame): A DataFrame containing loan information with columns:
                          - 'loan_id' (int): Unique identifier for each loan.
                          - 'user_id' (int): Unique identifier for each user.
                          - 'loan_type' (str): Type of loan ('Mortgage', 'Refinance', etc.).

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'user_id' (int): Users who have both 'Refinance' and 'Mortgage' loans.
                  The result is sorted in ascending order by 'user_id'.
    """
    # Extract user IDs for each loan type
    refinance_users = set(loans.loc[loans["loan_type"] == "Refinance", "user_id"])
    mortgage_users = set(loans.loc[loans["loan_type"] == "Mortgage", "user_id"])

    # Find users who have both loan types
    eligible_users = sorted(refinance_users & mortgage_users)

    # Return as a DataFrame
    return pd.DataFrame({"user_id": eligible_users})


def main():
    """
    Main function to demonstrate the loan_types function with a sample dataset.
    """
    # Sample loans data
    loans_data = {
        "loan_id": [683, 218, 802, 593, 138, 193, 389],
        "user_id": [101, 101, 102, 102, 103, 103, 104],
        "loan_type": ["Mortgage", "AutoLoan", "InSchool", "Mortgage", "Refinance", "InSchool", "Mortgage"]
    }

    # Convert dictionary to DataFrame
    loans_df = pd.DataFrame(loans_data)

    # Find users with both 'Refinance' and 'Mortgage' loans
    result = loan_types(loans_df)

    # Display result
    print(result)


# Run the script only if executed directly
if __name__ == "__main__":
    main()
