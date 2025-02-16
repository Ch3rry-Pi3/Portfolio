# 🎭 **LeetCode 1355: Activity Participants**  

## 📌 **Problem Overview**  
You are given two tables:  
1. **`Friends` Table**: Contains information about friends and the activities they participate in.  
2. **`Activities` Table**: Contains a list of all available activities.  

Each friend participates in **exactly one activity**. The task is to find **all activities that have neither the maximum nor the minimum number of participants**.

### **Goal**  
Find the activities with **a number of participants that is neither the highest nor the lowest**.  
- The **maximum participant count** is the highest number of friends in any activity.  
- The **minimum participant count** is the lowest number of friends in any activity.  
- **Filter out** activities with these extreme counts and return only those in between.  

## 📊 **Database Schema**  
### **Friends Table**  
| Column Name  | Type    | Description                                      |
|-------------|--------|--------------------------------------------------|
| `id`        | int    | Unique identifier for a friend                   |
| `name`      | varchar | Name of the friend                               |
| `activity`  | varchar | The activity the friend participates in          |

### **Activities Table**  
| Column Name | Type    | Description                       |
|------------|--------|----------------------------------|
| `id`       | int    | Unique identifier for an activity |
| `name`     | varchar | The name of the activity         |

## 🛠 **Approach**  
1. **Group by `activity`** and **count** the number of participants in each activity.  
2. **Determine the maximum and minimum participant count**.  
3. **Filter out** activities with the **maximum or minimum** participant count.  
4. **Return the remaining activities**.  

## 🚀 **Python Solution**  
```python
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

```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Friends Table**  
| id | name       | activity     |
|----|-----------|-------------|
| 1  | Jonathan D. | Eating     |
| 2  | Jade W.   | Singing     |
| 3  | Victor J. | Singing     |
| 4  | Elvis Q.  | Eating      |
| 5  | Daniel A. | Eating      |
| 6  | Bob B.    | Horse Riding |

#### **Activities Table**  
| id | name         |
|----|-------------|
| 1  | Eating      |
| 2  | Singing     |
| 3  | Horse Riding |

### **Output**  
```python
   activity
0  Singing
1  Eating
```

### **Explanation**  
- **Eating** is performed by **3** friends (**Jonathan D., Elvis Q., Daniel A.**) → **Maximum count**.  
- **Horse Riding** is performed by **1** friend (**Bob B.**) → **Minimum count**.  
- **Singing** is performed by **2** friends (**Victor J. and Jade W.**) → **Valid activity**.  
- **Final result:** **Singing** and **Eating** are returned.  

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Group by activity | `groupby("activity")` | **O(N)** |
| Count participants | `.agg(counts=("activity", "count"))` | **O(N)** |
| Compute min/max | `.assign(maximum=x.max(), minimum=x.min())` | **O(N)** |
| Filter out min/max | `.query("counts != maximum and counts != minimum")` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`groupby`, `agg`, `sort_values`, `query`).  
✔ **Ensures we only return activities with participant counts that are neither max nor min**.  
✔ **Scalable for larger datasets** as it runs in **O(N) time complexity**.  

🚀 **With this approach, you can efficiently determine activities with a balanced number of participants!** 🎯