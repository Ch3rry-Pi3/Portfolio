import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """
    Finds viewers who have viewed more than one unique article on the same date.

    Args:
        views (pd.DataFrame): A DataFrame containing article view records with columns:
            - "article_id" (int): ID of the article.
            - "author_id" (int): ID of the article's author.
            - "viewer_id" (int): ID of the user who viewed the article.
            - "view_date" (date): The date when the article was viewed.

    Returns:
        pd.DataFrame: A DataFrame containing viewer IDs who have viewed multiple articles
                      on the same date, sorted in ascending order.
    """

    # Group by viewer_id and view_date, counting the number of unique articles viewed
    grouped = views.groupby(["viewer_id", "view_date"]).agg({"article_id": "nunique"})

    # Filter to keep only those who viewed more than one unique article on the same date
    result = grouped[grouped["article_id"] > 1].reset_index()

    # Extract unique viewer IDs, sort them, and return as a DataFrame
    final_result = (
        result["viewer_id"]
        .sort_values()
        .drop_duplicates()
        .to_frame(name="id")
        .reset_index(drop=True)
    )

    return final_result


def main():
    # Sample test case
    data = {
        "article_id": [1, 3, 1, 2, 3, 4, 3, 4],
        "author_id": [3, 3, 7, 7, 6, 4, 4, 4],
        "viewer_id": [5, 5, 6, 6, 6, 4, 4, 4],
        "view_date": pd.to_datetime(
            ["2019-08-01", "2019-08-01", "2019-08-01", "2019-08-02",
             "2019-08-02", "2019-07-21", "2019-07-21", "2019-07-21"]
        ),
    }

    views_df = pd.DataFrame(data)

    # Run the function and display the result
    result = article_views(views_df)
    print(result)


if __name__ == "__main__":
    main()
