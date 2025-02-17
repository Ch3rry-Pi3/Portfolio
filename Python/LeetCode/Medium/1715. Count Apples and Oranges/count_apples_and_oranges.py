import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total number of apples and oranges across all boxes, 
    including fruits contained within chests.

    Args:
        boxes (pd.DataFrame): A DataFrame containing details of the boxes with columns:
                              - "box_id" (int): Unique ID for the box.
                              - "chest_id" (int, nullable): ID of the chest inside the box.
                              - "apple_count" (int): Number of apples in the box.
                              - "orange_count" (int): Number of oranges in the box.
        chests (pd.DataFrame): A DataFrame containing details of the chests with columns:
                               - "chest_id" (int): Unique ID for the chest.
                               - "apple_count" (int): Number of apples in the chest.
                               - "orange_count" (int): Number of oranges in the chest.

    Returns:
        pd.DataFrame: A DataFrame with the total count of apples and oranges.
    """
    # Merge boxes with chests to include fruit counts from chests
    merged_df = (
        pd.merge(left=boxes, right=chests, on="chest_id", how="left")
        .fillna(value={"apple_count_y": 0, "orange_count_y": 0})  # Fill NaN with 0 for chests
        .assign(
            apples=lambda x: x["apple_count_x"] + x["apple_count_y"],
            oranges=lambda x: x["orange_count_x"] + x["orange_count_y"]
        )
    )

    # Compute total sum of apples and oranges
    apples = merged_df["apples"].sum()
    oranges = merged_df["oranges"].sum()

    return pd.DataFrame({"apple_count": [apples], "orange_count": [oranges]})


def main():
    """
    Demonstrates the functionality of count_apples_and_oranges() with example data.
    """
    # Example input data
    boxes_data = {
        "box_id": [2, 18, 3, 12, 20, 8],
        "chest_id": [None, 14, 16, 3, 12, 6],
        "apple_count": [6, 4, 16, 19, 12, 9],
        "orange_count": [15, 15, 7, 20, 9, 9]
    }

    chests_data = {
        "chest_id": [6, 14, 12, 16],
        "apple_count": [5, 20, 8, 19],
        "orange_count": [6, 10, 8, 19]
    }

    # Convert dictionaries to DataFrames
    boxes_df = pd.DataFrame(boxes_data)
    chests_df = pd.DataFrame(chests_data)

    # Compute and display the result
    result_df = count_apples_and_oranges(boxes_df, chests_df)
    print(result_df)


if __name__ == "__main__":
    main()
