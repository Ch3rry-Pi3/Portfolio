import pandas as pd
import numpy as np

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of tasks submitted during weekends and working days.

    A task is considered:
    - A "weekend" task if it was submitted on a **Saturday (5) or Sunday (6)**.
    - A "working" task if it was submitted from **Monday (0) to Friday (4)**.

    Args:
        tasks (pd.DataFrame): A DataFrame containing task submissions with columns:
            - "task_id" (int): Unique ID for each task.
            - "assignee_id" (int): The ID of the person assigned the task.
            - "submit_date" (datetime): The date the task was submitted.

    Returns:
        pd.DataFrame: A single-row DataFrame with:
            - "weekend_cnt": Number of tasks submitted on weekends.
            - "working_cnt": Number of tasks submitted on working days.
    """

    # Categorise tasks as 'weekend' or 'working' based on the weekday
    tasks["status"] = np.where(tasks["submit_date"].dt.weekday >= 5, "weekend", "working")

    # Count the number of tasks for each category
    result = pd.DataFrame({
        "weekend_cnt": [tasks[tasks["status"] == "weekend"].shape[0]],
        "working_cnt": [tasks[tasks["status"] == "working"].shape[0]]
    })

    return result


if __name__ == "__main__":
    # Example usage
    example_data = pd.DataFrame({
        "task_id": [1, 2, 3, 4, 5, 6, 7],
        "assignee_id": [3, 6, 6, 3, 7, 7, 3],
        "submit_date": pd.to_datetime(["2022-06-13", "2022-06-14", "2022-06-15",
                                       "2022-06-18", "2022-06-18", "2022-06-19", "2022-06-19"])
    })

    print(count_tasks(example_data))
