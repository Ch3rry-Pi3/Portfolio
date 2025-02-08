import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the number of unique post reports for each report reason on July 4, 2019.
    Returns a DataFrame with 'report_reason' and 'report_count'.
    """
    return (
        actions
        .dropna(subset=["extra"])  # Drop rows where 'extra' is NaN
        .query("action_date == '2019-07-04' and action == 'report'")                    # Filter for July 4 reports
        .groupby("extra", as_index=False)["post_id"].nunique()                          # Count unique post_id per 'extra'
        .rename(columns={"extra": "report_reason", "post_id": "report_count"})          # Rename columns
    )

def main():
    """
    Runs an example test case for the reported_posts function.
    """
    # Example DataFrame
    data = {
        "action_date": ["2019-07-04", "2019-07-04", "2019-07-04", "2019-07-05"],
        "action": ["report", "report", "like", "report"],
        "post_id": [101, 102, 103, 104],
        "extra": ["Spam", "Harassment", None, "Spam"]
    }
    actions = pd.DataFrame(data)
    
    # Run function
    result = reported_posts(actions)
    print(result)

if __name__ == "__main__":
    main()
