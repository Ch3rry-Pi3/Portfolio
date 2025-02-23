# 🚌 **LeetCode 2142: The Number of Passengers in Each Bus I**  

## 📌 **Problem Overview**  
At a LeetCode bus station, both **buses and passengers arrive** at specific times. Each **passenger boards the earliest bus that arrives at or after their arrival time**, and a passenger **can only board one bus**.  

Given two tables:  
- **`Buses`**: Contains bus arrival times.
- **`Passengers`**: Contains passenger arrival times.  

Return the **number of passengers each bus picks up**, sorted by `bus_id` in ascending order.

### **Example 1**  

#### **Input:**  
**Buses Table:**  
| bus_id | arrival_time |
|--------|-------------|
| 1      | 2           |
| 2      | 4           |
| 3      | 7           |

**Passengers Table:**  
| passenger_id | arrival_time |
|-------------|-------------|
| 11          | 1           |
| 12          | 5           |
| 13          | 6           |
| 14          | 7           |

#### **Output:**  
| bus_id | passengers_cnt |
|--------|---------------|
| 1      | 1             |
| 2      | 0             |
| 3      | 3             |

✅ **Explanation:**  
- **Passenger 11 arrives at time `1`** → Bus `1` (arrives at `2`) picks them up.
- **Passenger 12 arrives at `5`**, **Passenger 13 arrives at `6`** → No bus available at or before their time.
- **Passenger 14 arrives at `7`** → Bus `3` (arrives at `7`) picks up **Passengers 12, 13, and 14**.

## 🚀 **Approach & Intuition**  

### 🔹 **Key Idea: Ordered Merge & Backfill Strategy**  
To efficiently determine which passengers board which buses:  
1. **Merge** `buses` and `passengers` on `arrival_time` using an **ordered merge** (`merge_ordered`).  
2. **Backfill** `bus_id` to assign passengers to the **earliest bus available**.  
3. **Group by `bus_id`** and **count passengers** to get the final answer.  

📌 **Time Complexity:** **O(n log n)** (due to sorting and merge operations)  
📌 **Space Complexity:** **O(n)** (for storing merged data)  

## 📝 **Implementation**  

```python
# passengers_per_bus.py

import pandas as pd

def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of passengers who use each bus.

    A passenger boards the earliest arriving bus that is at or after their arrival time.
    A bus only picks up passengers who haven't already boarded another bus.

    Args:
        buses (pd.DataFrame): Contains bus data with columns:
            - "bus_id" (int): The unique ID of the bus.
            - "arrival_time" (int): The time the bus arrives at the station.
        passengers (pd.DataFrame): Contains passenger data with columns:
            - "passenger_id" (int): The unique ID of the passenger.
            - "arrival_time" (int): The time the passenger arrives at the station.

    Returns:
        pd.DataFrame: A table with:
            - "bus_id" (int): The unique bus ID.
            - "passengers_cnt" (int): The number of passengers that used each bus.
        
        The result is sorted by "bus_id" in ascending order.
    """

    # Merge buses and passengers using an ordered merge on arrival_time
    df = pd.merge_ordered(buses, passengers, on="arrival_time")

    # Backfill the bus_id to assign each passenger to the earliest available bus
    df["bus_id"] = df["bus_id"].bfill()

    # Group by bus_id and count the number of passengers for each bus
    result = df.groupby("bus_id", as_index=False).agg(passengers_cnt=("passenger_id", "count"))

    return result.sort_values("bus_id")

```

## 📂 **Project Structure**  

```
2142. The Number of Passengers in Each Bus I/
├── passengers_per_bus.py  # Python solution
├── README.md              # Explanation and walkthrough
```

## 🎯 **Key Takeaways**  
✔ **Uses `merge_ordered`** to efficiently merge and match buses to passengers.  
✔ **Backfills `bus_id`** to ensure each passenger takes the earliest available bus.  
✔ **Optimal performance** with **O(n log n) complexity**, leveraging sorting and grouping operations.  

🚀 **A great problem for mastering ordered merging and backfilling techniques!** 🔥