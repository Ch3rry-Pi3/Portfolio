# 🏢 **LeetCode 1126: Active Businesses**  

## 📌 **Problem Overview**  
You are given a table **`Events`** that tracks business activities. Each row records how often a specific **event type** occurred for a business.

### **Definitions**  
- The **average activity** for an `event_type` is the average number of `occurrences` across all businesses.  
- An **active business** is a business that has **more than one event type** where its `occurrences` are **strictly greater** than the **average occurrences** for that event type.  

### **Goal**  
Find all **active businesses** and return their `business_id`.

## 📊 **Database Schema**  
### **Events Table**  
| Column Name   | Type    | Description  |
|--------------|--------|------------------------------------------------|
| `business_id` | int    | Unique ID for the business |
| `event_type`  | varchar | The type of event that occurred |
| `occurrences` | int    | Number of times the event occurred |

## 🛠 **Approach**  
1. **Compute the average occurrences per event type** using `.groupby()`.  
2. **Merge** the computed averages back into the original events table.  
3. **Mark businesses as "active"** for each event type where their occurrences exceed the average.  
4. **Count the number of "active" event types per business** using `.groupby()`.  
5. **Filter businesses that have more than one active event type**.  

## 🚀 **Python Solution**  
```python
import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    """
    Identifies active businesses that have more than one event type 
    where their occurrences are strictly greater than the average occurrences 
    for that event type.

    Args:
        events (pd.DataFrame): A DataFrame containing event records with columns:
                               - "business_id" (int): Unique ID for the business.
                               - "event_type" (str): Type of event.
                               - "occurrences" (int): Number of times the event occurred.

    Returns:
        pd.DataFrame: A DataFrame containing a single column "business_id"
                      listing all active businesses.
    """
    # Compute the average occurrences per event type
    avg_event_counts = (
        events.groupby("event_type", as_index=False)
        .agg(avg_event_count=("occurrences", "mean"))
    )

    # Merge original events with the average occurrences
    merged_events = events.merge(avg_event_counts, on="event_type", how="left")

    # Mark events where occurrences are strictly greater than the event's average
    merged_events["active"] = (merged_events["occurrences"] > merged_events["avg_event_count"]).astype(int)

    # Count the number of active event types per business
    active_businesses = (
        merged_events.groupby("business_id", as_index=False)["active"]
        .sum()
        .query("active > 1")  # Select businesses with more than one active event type
        [["business_id"]]
    )

    return active_businesses
```

## 📌 **Example Walkthrough**  
### **Example Input**  
#### **Events Table**  
| business_id | event_type | occurrences |
|------------|------------|-------------|
| 1          | reviews    | 7           |
| 3          | reviews    | 3           |
| 3          | ads        | 11          |
| 3          | ads        | 6           |
| 3          | page views | 12          |

### **Step 1: Compute Average Occurrences**  
| event_type  | avg_event_count |
|-------------|----------------|
| reviews     | **5.0**         |
| ads         | **8.5**         |
| page views  | **12.0**        |

### **Step 2: Mark Active Events**  
| business_id | event_type | occurrences | avg_event_count | Active? |
|------------|------------|-------------|----------------|---------|
| 1          | reviews    | 7           | 5.0            | ✅ Yes  |
| 3          | reviews    | 3           | 5.0            | ❌ No   |
| 3          | ads        | 11          | 8.5            | ✅ Yes  |
| 3          | ads        | 6           | 8.5            | ❌ No   |
| 3          | page views | 12          | 12.0           | ❌ No   |

### **Step 3: Count Active Event Types per Business**  
| business_id | Active Events Count |
|------------|---------------------|
| 1          | **1** |
| 3          | **2** |

### **Step 4: Filter Businesses with More Than One Active Event Type**  
| business_id |
|------------|
| **3** |

### **Output**  
```python
   business_id
0            3
```

### **Explanation**  
- Business **3** has **2 event types** (`ads` and `reviews`) where occurrences exceed the event average.  
- Business **1** has **only 1 active event**, so it's not included.  

## ⏳ **Complexity Analysis**  
| Step | Operation | Time Complexity |
|------|------------|----------------|
| Compute average occurrences | `groupby("event_type")` | **O(N)** |
| Merge with events table | `merge(events, avg_event_counts)` | **O(N)** |
| Mark active events | `assign(active=...)` | **O(N)** |
| Count active events per business | `groupby("business_id")` | **O(N)** |
| Filter businesses with >1 active event | `query("active > 1")` | **O(N)** |
| **Total Complexity** | **O(N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses vectorised Pandas operations** (`groupby`, `merge`, `assign`, `query`).  
✔ **Handles all businesses efficiently**, even if some have fewer events.  
✔ **Ensures businesses with more than one active event are identified correctly**.  

🚀 **With this approach, you can quickly find businesses that are truly active!** 🎯