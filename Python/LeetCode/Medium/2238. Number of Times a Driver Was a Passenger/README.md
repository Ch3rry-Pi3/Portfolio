# 🚗 **LeetCode 2238: Number of Times a Driver Was a Passenger**  

## 📌 **Problem Overview**  
Given a table of **rides**, where each row contains:  
- `ride_id` → A unique identifier for the ride.  
- `driver_id` → The ID of the driver.  
- `passenger_id` → The ID of the passenger.  

Each **driver_id** represents a person who drove at least one ride, and each **passenger_id** represents a person who rode as a passenger.  

### **Objective**  
For each **driver**, count how many times they were a **passenger** in other rides.  

**Return a table** containing:  
- `driver_id` → The unique driver IDs.  
- `cnt` → The number of times that driver appeared as a passenger.  

⚠ **If a driver was never a passenger, return `0` as their count.**  

## 🎯 **Example Walkthrough**  

### **Example 1**  
#### **Input**  
```python
rides = [
    [1, 7, 1], 
    [2, 7, 2], 
    [3, 7, 7], 
    [4, 11, 3], 
    [5, 11, 4], 
    [6, 11, 5]
]
```
#### **Output**  
```python
[
    [7, 2],
    [11, 0]
]
```
#### ✅ **Explanation**  
- Drivers: **7** and **11**  
- **Driver `7` appeared as a passenger in `2` rides** (ride `1` and ride `2`).  
- **Driver `11` never appeared as a passenger**, so their count is `0`.  

## 🚀 **Approach Explanation**  

### **1️⃣ Identify Drivers Who Were Also Passengers**  
- Extract all `passenger_id` values that **exist in `driver_id`**.  

### **2️⃣ Count How Many Times Each Driver Was a Passenger**  
- **Group by `passenger_id`** to count occurrences.  

### **3️⃣ Ensure All Drivers Appear in the Output**  
- Merge the **passenger counts** back into the list of **all drivers**.  
- Fill missing values with `0` for drivers who were **never passengers**.  

## 📝 **Python Solution**  
```python
import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of times each driver has been a passenger.

    Args:
        rides (pd.DataFrame): Contains ride data with columns:
            - "ride_id" (int): Unique ride identifier.
            - "driver_id" (int): The ID of the driver.
            - "passenger_id" (int): The ID of the passenger.

    Returns:
        pd.DataFrame: A table with:
            - "driver_id" (int): Unique driver IDs.
            - "cnt" (int): Number of times the driver was a passenger.
    """
    # Identify drivers who were also passengers
    driver_as_passenger = rides[rides['passenger_id'].isin(rides['driver_id'])]

    # Count occurrences of each driver as a passenger
    passenger_counts = driver_as_passenger.groupby('passenger_id').size().reset_index(name='cnt')

    # Extract unique drivers
    drivers = rides[['driver_id']].drop_duplicates()

    # Merge counts with drivers, fill missing values with 0
    result = (
        drivers.merge(passenger_counts, left_on='driver_id', right_on='passenger_id', how='left')
        .fillna(0)
        .drop(columns=['passenger_id'])
    )

    # Ensure count is an integer
    result['cnt'] = result['cnt'].astype(int)

    # Sort by driver_id for consistency
    return result.sort_values(by='driver_id')

```

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| **Filtering** | Finding drivers who were passengers | **O(N)** |
| **Grouping** | Counting occurrences | **O(N)** |
| **Merging** | Merging with driver list | **O(N log N)** |
| **Sorting** | Sorting results by `driver_id` | **O(N log N)** |
| **Overall Complexity** | **O(N log N)** (due to sorting) ✅ |

## 📂 **Project Structure**  
```
driver_was_passenger/
├── driver_was_passenger.py  # Python solution
├── README.md                # Explanation & approach
```

✨ **Simple, efficient, and clear!** 🚀