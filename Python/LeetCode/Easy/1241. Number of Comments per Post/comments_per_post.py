import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of comments for each post.
    Ensures posts with no comments are counted as 0.
    """

    # Get submissions that are posts (i.e., have no parent)
    posts = submissions[submissions["parent_id"].isna()]

    # Count the number of comments for each post by grouping by 'parent_id'
    comment_counts = submissions.groupby("parent_id")["sub_id"].nunique().reset_index(name="number_of_comments")

    # Merge the posts with the comment counts on 'sub_id' and 'parent_id'
    result = pd.merge(posts, comment_counts, left_on="sub_id", right_on="parent_id", how="left").drop_duplicates(subset="sub_id")

    # Handle missing values (no comments for some posts) and clean up the result
    result["number_of_comments"].fillna(0, inplace=True)
    result = result[["sub_id", "number_of_comments"]].rename(columns={"sub_id": "post_id"})

    return result.sort_values(by="post_id").reset_index(drop=True)

def main():
    """Test the function with an example dataset."""
    data = {
        "sub_id": [1, 2, 3, 4, 5, 6, 7],
        "parent_id": [None, None, 1, 1, 3, 2, None]
    }
    submissions = pd.DataFrame(data)

    # Run the function and print the result
    result = count_comments(submissions)
    print(result)

if __name__ == "__main__":
    main()
