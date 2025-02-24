import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies the top 3 trending hashtags in February 2024.

    :param tweets: DataFrame containing user tweets.
    :return: DataFrame with the top 3 trending hashtags.
    """
    pattern = r'(#[\w]+)'

    return (
        tweets
        .assign(HASHTAG=lambda x: x["tweet"].str.extract(pattern))
        .groupby("HASHTAG")["HASHTAG"]
        .count()
        .reset_index(name="HASHTAG_COUNT")
        .sort_values(by=["HASHTAG_COUNT", "HASHTAG"], ascending=[False, False])
        .head(3)
    )

def main():
    """
    Runs a sample test case for finding trending hashtags.
    """
    data = {
        "user_id": [135, 140, 137, 135, 140, 141, 140],
        "tweet_id": [13, 17, 15, 14, 19, 19, 17],
        "tweet": [
            "Enjoying a great start to the day! #HappyDay",
            "Exploring new tech frontiers. #TechLife",
            "Productivity peaks! #WorkLife",
            "Another #HappyDay with good vibes!",
            "Innovation drives us. #TechLife",
            "Connecting with nature's serenity. #Nature",
            "Gratitude for today's moments. #HappyDay",
        ],
        "tweet_date": [
            "2024-02-01", "2024-02-04", "2024-02-04",
            "2024-02-03", "2024-02-07", "2024-02-09",
            "2024-02-05"
        ]
    }
    
    tweets_df = pd.DataFrame(data)
    result = find_trending_hashtags(tweets_df)
    print(result)

if __name__ == "__main__":
    main()
