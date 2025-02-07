import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the Click-Through Rate (CTR) for each ad.

    CTR is calculated as:
        CTR = (Total Clicks / (Total Clicks + Total Views)) * 100
    If there are no clicks and views, CTR is set to 0.00.

    The results are:
    - Rounded to two decimal places.
    - Sorted by `ctr` in descending order.
    - Sorted by `ad_id` in ascending order in case of a tie.

    :param ads: DataFrame containing ad_id, user_id, and action columns.
    :return: DataFrame with ad_id and corresponding CTR.
    """

    # Group by 'ad_id' and calculate the CTR for each group
    ctr = ads.groupby('ad_id')['action'].apply(
        lambda x: round(
            (sum(x == 'Clicked') / (sum(x == 'Clicked') + sum(x == 'Viewed')) * 100)
            if (sum(x == 'Clicked') + sum(x == 'Viewed')) > 0 else 0.00, 
            2
        )
    ).reset_index()

    # Rename the column to 'ctr'
    ctr.columns = ['ad_id', 'ctr']
    
    # Sort the results by 'ctr' in descending order and by 'ad_id' in ascending order
    result = ctr.sort_values(by=['ctr', 'ad_id'], ascending=[False, True])

    return result


def main():
    """
    Demonstrates testing the ads_performance function on an example dataset.
    """
    # Example test data
    data = {
        "ad_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
        "user_id": [101, 102, 103, 201, 202, 301, 302, 303, 304],
        "action": ["Clicked", "Viewed", "Clicked", "Viewed", "Viewed", "Clicked", "Viewed", "Viewed", "Clicked"]
    }

    ads_df = pd.DataFrame(data)

    print("Input DataFrame:")
    print(ads_df, "\n")

    # Compute ad performance
    result = ads_performance(ads_df)

    print("Output DataFrame:")
    print(result)


if __name__ == "__main__":
    main()
