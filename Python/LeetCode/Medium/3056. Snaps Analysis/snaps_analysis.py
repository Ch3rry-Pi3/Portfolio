import pandas as pd
import numpy as np

def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the percentage of time spent sending and opening snaps for each age group.

    :param activities: DataFrame containing activity_id, user_id, activity_type, and time_spent.
    :param age: DataFrame containing user_id and age_bucket.
    :return: DataFrame with age_bucket, send_perc, and open_perc.
    """
    # Merge activities with age groups
    df = pd.merge(activities, age, on="user_id", how="left")

    # Compute total time spent per age group
    total_time_per_group = df.groupby("age_bucket")["time_spent"].transform("sum")

    # Compute total time spent per age group and activity type
    total_time_per_activity = df.groupby(["age_bucket", "activity_type"])["time_spent"].transform("sum")

    # Compute send and open percentages
    df["send_perc"] = np.where(df["activity_type"] == "send",
                               round((total_time_per_activity / total_time_per_group) * 100, 2), 0)

    df["open_perc"] = 100 - df["send_perc"]

    # Filter only one row per age_bucket
    result = df.query("send_perc != 0")[["age_bucket", "send_perc", "open_perc"]].drop_duplicates("age_bucket")

    return result

def main():
    """
    Runs a sample test case for snap analysis.
    """
    # Sample activities DataFrame
    activities_data = {
        "activity_id": [7274, 2425, 1413, 8564, 5235, 4251, 1435, 1436],
        "user_id": [123, 123, 456, 456, 456, 123, 789, 789],
        "activity_type": ["open", "send", "send", "send", "open", "open", "open", "send"],
        "time_spent": [4.50, 3.50, 5.67, 8.24, 3.00, 1.25, 5.25, 6.24]
    }
    activities = pd.DataFrame(activities_data)

    # Sample age DataFrame
    age_data = {
        "user_id": [123, 789, 456],
        "age_bucket": ["31-35", "21-25", "26-30"]
    }
    age = pd.DataFrame(age_data)

    # Run the snap analysis function
    result = snap_analysis(activities, age)
    
    # Display the result
    print(result)

if __name__ == "__main__":
    main()
