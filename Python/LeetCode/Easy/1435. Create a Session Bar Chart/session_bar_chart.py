import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    """
    Categorizes user session durations into predefined time bins and counts the number of sessions in each bin.

    Args:
        sessions (pd.DataFrame): A DataFrame containing session durations.

    Returns:
        pd.DataFrame: A DataFrame with session bins and the count of sessions in each bin.
    """
    # Define bins based on duration in seconds
    zero_to_five = len(sessions.query("duration < 300"))
    five_to_ten = len(sessions.query("300 <= duration < 600"))
    ten_to_fifteen = len(sessions.query("600 <= duration < 900"))
    more_than_fifteen = len(sessions.query("duration >= 900"))

    # Construct the result DataFrame
    result = pd.DataFrame({
        "bin": ['[0-5>', '[5-10>', '[10-15>', '15 or more'],
        "total": [zero_to_five, five_to_ten, ten_to_fifteen, more_than_fifteen]
    })

    return result


def main():
    """
    Runs example test cases for the create_bar_chart function.
    """
    # Example session data
    session_data = {
        "session_id": [1, 2, 3, 4, 5],
        "duration": [30, 299, 199, 580, 1000]       # Durations in seconds
    }
    
    # Create DataFrame
    sessions = pd.DataFrame(session_data)

    # Run function and display result
    result = create_bar_chart(sessions)
    print(result)


if __name__ == "__main__":
    main()
