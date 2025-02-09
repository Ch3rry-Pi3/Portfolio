import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    """
    Merges the queries table with the npv table on 'id' and 'year'.
    If no matching npv value is found, it assigns a default value of 0.

    Args:
        npv (pd.DataFrame): The NPV table containing 'id', 'year', and 'npv'.
        queries (pd.DataFrame): The Queries table containing 'id' and 'year'.

    Returns:
        pd.DataFrame: A DataFrame containing 'id', 'year', and the corresponding 'npv'.
    """
    return pd.merge(left=queries, right=npv, on=["id", "year"], how="left").fillna(value={"npv": 0})

def main():
    """
    Runs example test cases for the npv_queries function.
    """
    # Define the NPV DataFrame
    npv_data = {
        "id": [1, 7, 2, 1, 2, 3, 11, 7],
        "year": [2018, 2020, 2009, 2019, 2008, 2009, 2020, 2019],
        "npv": [100, 30, 40, 113, 121, 12, 99, 0]
    }
    npv = pd.DataFrame(npv_data)

    # Define the Queries DataFrame
    queries_data = {
        "id": [1, 2, 2, 7, 7, 13],
        "year": [2019, 2008, 2009, 2018, 2020, 2019]
    }
    queries = pd.DataFrame(queries_data)

    # Run the function and display the result
    result = npv_queries(npv, queries)
    print(result)

if __name__ == "__main__":
    main()
