# 🚲 **LeetCode 2687: Bikes Last Time Used**

## 📌 **Problem Overview**
You are given a dataset containing **bike usage records**. Each ride has:
- A **bike_number** that identifies the bike.
- A **start_time** and an **end_time** indicating when the ride began and ended.

Your task is to **find the last time each bike was used** based on the latest recorded **end_time**.

**Requirements:**
- Return a table with **each unique bike_number** and its latest **end_time**.
- The result should be **sorted in descending order of end_time**.

## 🎯 **Example Walkthrough**

### **Example 1**
#### **Input:**
| ride_id | bike_number | start_time         | end_time           |
|---------|------------|--------------------|--------------------|
| 1       | W00576     | 2012-03-25 11:30:00 | 2012-03-25 12:40:00 |
| 2       | W00300     | 2012-03-25 10:30:00 | 2012-03-25 10:50:00 |
| 3       | W00300     | 2012-03-25 16:30:00 | 2012-03-25 17:40:00 |
| 4       | W00535     | 2012-03-25 14:00:00 | 2012-03-25 13:40:00 |
| 5       | W00535     | 2012-03-25 09:10:00 | 2012-03-25 09:18:00 |
| 6       | W00576     | 2012-03-28 02:30:00 | 2012-03-28 02:50:00 |

#### **Output:**
| bike_number | end_time           |
|------------|--------------------|
| W00576     | 2012-03-28 02:50:00 |
| W00535     | 2012-03-25 17:40:00 |
| W00300     | 2012-03-25 10:50:00 |

#### **Explanation:**
- Bike **W00576** was last used on **March 28, 2012**.
- Bike **W00535** was last used on **March 25, 2012**.
- Bike **W00300** was last used on **March 25, 2012**.

## 🛠 **Approach**
This problem can be efficiently solved using **Pandas**:

1. **Group by `bike_number`** and find the **maximum `end_time`**.
2. **Retrieve the records** corresponding to these latest `end_time` values.
3. **Sort the results** in **descending order** based on `end_time`.

This approach runs in **O(N log N)** time due to sorting.

## 🚀 **Python Solution**
```python
import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the last time each bike was used and returns the result sorted in descending order.

    Args:
        bikes (pd.DataFrame): A DataFrame containing bike usage data with columns:
            - "bike_number" (str): The bike identifier.
            - "end_time" (datetime): The end time of the bike's ride.

    Returns:
        pd.DataFrame: A DataFrame with:
            - "bike_number" (str): Unique bike identifiers.
            - "end_time" (datetime): The last recorded end time for each bike.
    """
    # Get the last used time for each bike by finding the max end_time
    last_used = bikes.loc[bikes.groupby("bike_number")["end_time"].idxmax(), ["bike_number", "end_time"]]

    # Sort results by the most recently used bikes
    last_used = last_used.sort_values(by="end_time", ascending=False).reset_index(drop=True)

    return last_used
```

## ⏳ **Complexity Analysis**
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Grouping | `groupby("bike_number")["end_time"].idxmax()` | **O(N)** |
| Sorting | `sort_values(by="end_time", ascending=False)` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 📁 **Project Structure**
```
bikes_last_time_used/
├── last_time_used.py   # Python solution
├── README.md           # Documentation
```

## 🏆 **Why This Works**
✔ **Uses Pandas efficiently** to extract the latest time for each bike.  
✔ **Runs in O(N log N) time complexity**, making it **efficient for large datasets**.  
✔ **Handles edge cases**, including bikes used multiple times and single bike datasets.

🚀 **With this solution, you can efficiently determine the last time each bike was used!** 🎯