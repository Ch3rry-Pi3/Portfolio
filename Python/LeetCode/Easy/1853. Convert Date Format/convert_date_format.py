import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the date format in the 'day' column to the specified format:
    'Day_Name, Month_Name Day, Year'.

    Args:
        days (pd.DataFrame): DataFrame containing a 'day' column with date values.

    Returns:
        pd.DataFrame: DataFrame with the formatted 'day' column.
    """
    # Convert 'day' column to the desired format
    days["day"] = days["day"].dt.strftime('%A, %B %-d, %Y')
    
    return days

def main():
    # Sample data
    data = {
        "day": pd.to_datetime(["2022-04-12", "2021-08-09", "2020-06-26"])
    }
    
    # Create DataFrame
    days_df = pd.DataFrame(data)

    # Convert date format
    formatted_df = convert_date_format(days_df)

    # Print result
    print(formatted_df)

if __name__ == "__main__":
    main()
