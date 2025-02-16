import pandas as pd

def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies activities that have neither the maximum nor the minimum number 
    of participants from the 'Friends' table.

    Args:
        friends (pd.DataFrame): A DataFrame containing friends' activities with columns:
                                - "id" (int): Unique identifier for a friend.
                                - "name" (str): Name of the friend.
                                - "activity" (str): The activity the friend participates in.
        
        activities (pd.DataFrame): A DataFrame containing all activities with columns:
                                   - "id" (int): Unique identifier for an activity.
                                   - "name" (str): The name of the activity.

    Returns:
        pd.DataFrame: A DataFrame containing only the activities that have neither 
                      the maximum nor the minimum number of participants.
    """
    return (
        friends
        .groupby("activity", as_index=False)
        .agg(counts=("activity", "count"))                      # Count participants per activity
        .sort_values(by="counts")                               # Sort activities by participant count
        .assign(
            maximum=lambda x: x["counts"].max(),
            minimum=lambda x: x["counts"].min()
        )                                                       # Assign max and min participant counts
        .query("counts != maximum and counts != minimum")       # Filter out extreme cases
        [["activity"]]                                          # Select relevant column for output
    )

def main():
    # Sample data
    friends_data = {
        "id": [1, 2, 3, 4, 5, 6],
        "name": ["Jonathan D.", "Jade W.", "Victor J.", "Elvis Q.", "Daniel A.", "Bob B."],
        "activity": ["Eating", "Singing", "Singing", "Eating", "Eating", "Horse Riding"]
    }
    
    activities_data = {
        "id": [1, 2, 3],
        "name": ["Eating", "Singing", "Horse Riding"]
    }

    # Creating DataFrames
    friends_df = pd.DataFrame(friends_data)
    activities_df = pd.DataFrame(activities_data)

    # Running the function
    result = activity_participants(friends_df, activities_df)

    # Display the result
    print(result)

if __name__ == "__main__":
    main()
