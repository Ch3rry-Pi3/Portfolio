import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    """
    Finds all playback sessions that did not receive any ads.

    Args:
        playback (pd.DataFrame): DataFrame containing playback session details.
        ads (pd.DataFrame): DataFrame containing ad display records.

    Returns:
        pd.DataFrame: A DataFrame containing only the `session_id` column of sessions 
                      that did not receive any ads.
    """
    return (
        playback
        .merge(ads, on="customer_id", how="left")
        .query("start_time <= timestamp <= end_time")["session_id"]
        .drop_duplicates()
        .pipe(lambda blocked: playback.loc[~playback["session_id"].isin(blocked), ["session_id"]])
    )

def main():
    """Main function to test ad-free session identification."""
    # Sample data
    playback_data = {
        "session_id": [1, 2, 3, 4, 5],
        "customer_id": [1, 1, 2, 2, 2],
        "start_time": [1, 15, 10, 17, 8],
        "end_time": [5, 23, 12, 28, 12],
    }

    ads_data = {
        "ad_id": [1, 2, 3],
        "customer_id": [1, 2, 2],
        "timestamp": [5, 17, 20],
    }

    # Create DataFrames
    playback_df = pd.DataFrame(playback_data)
    ads_df = pd.DataFrame(ads_data)

    # Run function
    result = ad_free_sessions(playback_df, ads_df)
    
    # Display result
    print(result)

if __name__ == "__main__":
    main()
