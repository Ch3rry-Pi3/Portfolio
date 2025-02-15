import pandas as pd


def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average daily percentage of posts that were removed 
    after being reported as spam, rounded to two decimal places.

    Args:
        actions (pd.DataFrame): A DataFrame containing post actions with columns:
                                - "user_id" (int): ID of the user performing the action.
                                - "post_id" (int): ID of the post.
                                - "action_date" (date): Date of the action.
                                - "action" (enum): Type of action ('view', 'like', 'reaction', 'comment', 'report', 'share').
                                - "extra" (varchar, nullable): Additional information (e.g., reason for report).

        removals (pd.DataFrame): A DataFrame containing removed posts with columns:
                                - "post_id" (int): ID of the removed post.
                                - "remove_date" (date): Date when the post was removed.

    Returns:
        pd.DataFrame: A DataFrame containing the average daily removal percentage of spam-reported posts.
    """

    # Filter actions to include only reports with 'spam' reason
    spam_reports = actions[actions["extra"] == "spam"].drop_duplicates(["action_date", "post_id"])

    # Merge with removals to check if reported spam posts were actually removed
    removed_spam = spam_reports.merge(removals, on="post_id", how="left")

    # Group by action_date to count reported and removed spam posts
    daily_stats = (
        removed_spam
        .groupby("action_date", as_index=False)
        .agg(
            removed_spam=("remove_date", "count"),          # Count removed spam posts
            total_spam=("remove_date", "size")              # Count total spam reports
        )
    )

    # Compute the daily percentage of removed spam posts
    daily_stats["daily_percent"] = (daily_stats["removed_spam"] * 100 / daily_stats["total_spam"])

    # Compute the overall average and round to two decimal places
    avg_daily_percent = daily_stats["daily_percent"].mean().round(2)

    return pd.DataFrame({"average_daily_percent": [avg_daily_percent]})


def main():
    # Sample data for testing
    actions_data = {
        "user_id": [1, 1, 2, 2, 3, 3, 4, 5, 5, 5],
        "post_id": [1, 1, 2, 3, 3, 4, 4, 5, 5, 5],
        "action_date": pd.to_datetime(
            ["2019-07-01", "2019-07-01", "2019-07-02", "2019-07-03", "2019-07-03",
             "2019-07-04", "2019-07-04", "2019-07-04", "2019-07-04", "2019-07-04"]
        ),
        "action": ["view", "like", "report", "view", "report", "spam", "view", "report", "view", "spam"],
        "extra": [None, None, "spam", None, "racism", "spam", None, "racism", None, "spam"]
    }
    
    removals_data = {
        "post_id": [2, 3],
        "remove_date": pd.to_datetime(["2019-07-20", "2019-07-18"])
    }

    # Create DataFrames
    actions_df = pd.DataFrame(actions_data)
    removals_df = pd.DataFrame(removals_data)

    # Call the function and display the result
    result = reported_posts(actions_df, removals_df)
    print(result)


if __name__ == "__main__":
    main()
