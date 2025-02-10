import pandas as pd

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies invalid tweets based on specific criteria.

    A tweet is considered invalid if it meets any of the following conditions:
    - Exceeds 140 characters in length.
    - Contains more than 3 mentions (indicated by '@').
    - Contains more than 3 hashtags (indicated by '#').

    Args:
        tweets (pd.DataFrame): A DataFrame containing tweet data with columns:
            - "tweet_id" (int): The unique ID of the tweet.
            - "content" (str): The text content of the tweet.

    Returns:
        pd.DataFrame: A DataFrame containing only the "tweet_id" of invalid tweets,
                      sorted in ascending order.
    """
    # Filter tweets based on the given conditions
    invalid_tweets = tweets.loc[
        (tweets["content"].str.len() > 140) |
        (tweets["content"].str.count("@") > 3) |
        (tweets["content"].str.count("#") > 3),
        ["tweet_id"]
    ].sort_values(by="tweet_id", ascending=True)

    return invalid_tweets


def main():
    """
    Runs example test cases for the find_invalid_tweets function.
    """
    # Sample tweet data
    tweet_data = {
        "tweet_id": [1, 2, 3, 4],
        "content": [
            "Traveling, exploring, and living my best life @JaneSmith @SaraJohnson @LisaTaylor @MikeBrown #Foodie #Fitness #Learning",
            "Just had the best dinner with friends! #foodie #friends #fun",
            "Working hard on my new project #Work #Goals #Productivity #Fun",
            "A short valid tweet."
        ]
    }

    # Convert to DataFrame
    tweets_df = pd.DataFrame(tweet_data)

    # Find invalid tweets
    result = find_invalid_tweets(tweets_df)
    print(result)


if __name__ == "__main__":
    main()
