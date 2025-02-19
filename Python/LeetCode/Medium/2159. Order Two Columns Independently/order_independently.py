import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Independently orders two columns in a DataFrame:
    
    - 'first_col' is sorted in ascending order.
    - 'second_col' is sorted in descending order.

    Args:
        data (pd.DataFrame): A DataFrame containing:
            - "first_col" (int): Column to be sorted in ascending order.
            - "second_col" (int): Column to be sorted in descending order.

    Returns:
        pd.DataFrame: A DataFrame with "first_col" sorted in ascending order
                      and "second_col" sorted in descending order.
    """

    # Sort "first_col" in ascending order and reset index
    first_col_sorted = data[["first_col"]].sort_values(by="first_col", ascending=True)["first_col"].reset_index(drop=True)

    # Sort "second_col" in descending order and reset index
    second_col_sorted = data[["second_col"]].sort_values(by="second_col", ascending=False)["second_col"].reset_index(drop=True)

    # Combine the independently sorted columns into a new DataFrame
    return pd.DataFrame({"first_col": first_col_sorted, "second_col": second_col_sorted})


if __name__ == "__main__":
    # Example usage
    sample_data = pd.DataFrame({
        "first_col": [4, 2, 3, 1],
        "second_col": [2, 1, 4, 1]
    })

    sorted_data = order_two_columns(sample_data)
    print(sorted_data)
