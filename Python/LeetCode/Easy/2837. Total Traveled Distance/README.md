# 🚗 **LeetCode 2901: Total Distance Traveled by Users**  

## 📌 **Problem Overview**  
Given a dataset of users and their **ride history**, the goal is to compute the **total distance traveled** by each user.  

1. If a user has multiple rides, their total distance is the **sum of all ride distances**.  
2. If a user has **no recorded rides**, their traveled distance should be **0**.  
3. The output should include all users, even those without rides, and should be **sorted by `user_id` in ascending order**.  

## 🔍 **Sorting Criteria**
| Column | Sorting Order |
|--------|--------------|
| 🔢 **User ID** | **Ascending** (Lowest First) |

## 🏆 **Example Walkthrough**  

### **Input:**
```python
users_data = {
    "user_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"]
}

rides_data = {
    "user_id": [1, 1, 2, 2, 2, 3],
    "distance": [5.0, 10.0, 3.5, 2.0, 7.5, 8.0]
}
```

### **Processing Logic:**
| User ID | Ride Distance |
|---------|--------------|
| **1**   | **5.0**      |
| **1**   | **10.0**     |
| **2**   | **3.5**      |
| **2**   | **2.0**      |
| **2**   | **7.5**      |
| **3**   | **8.0**      |
| **4**   | *(No rides, should default to 0)* |

- **Alice (`user_id = 1`)** traveled **5.0 + 10.0 = 15.0** km.  
- **Bob (`user_id = 2`)** traveled **3.5 + 2.0 + 7.5 = 13.0** km.  
- **Charlie (`user_id = 3`)** traveled **8.0** km.  
- **David (`user_id = 4`)** has **no recorded rides** → traveled distance = **0.0** km.  

### **Expected Output:**
```plaintext
   user_id     name  traveled distance
0       1   Alice               15.0
1       2     Bob               13.0
2       3  Charlie               8.0
3       4   David                0.0
```

## 🛠 **Python Solution**
```python
import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the total traveled distance for each user by summing up the distance from the rides dataset.
    If a user has no recorded rides, their traveled distance is set to 0.

    Parameters:
    users (pd.DataFrame): A DataFrame containing user information with columns:
                          - 'user_id' (int): Unique identifier for each user.
                          - Other user-specific attributes.

    rides (pd.DataFrame): A DataFrame containing ride details with columns:
                          - 'user_id' (int): The user associated with each ride.
                          - 'distance' (float): Distance covered in each ride.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - All columns from `users`.
                  - A new column 'traveled distance' with the total distance traveled by each user.
                  - Sorted by 'user_id' in ascending order.
    """
    # Aggregate total distance per user
    grouped = rides.groupby(by="user_id", as_index=False).agg(distance=("distance", "sum"))

    # Merge with users dataset and handle missing values
    result = (
        pd.merge(users, grouped, on="user_id", how="left")
        .sort_values(by="user_id", ascending=True)
        .fillna(0)  # Users with no rides get a traveled distance of 0
        .rename(columns={"distance": "traveled distance"})
    )

    return result
```

## ⏳ **Complexity Analysis**
| Step         | Operation                           | Time Complexity |
|-------------|------------------------------------|----------------|
| Grouping    | `.groupby("user_id")`              | **O(N)** |
| Aggregation | `.agg(sum)`                         | **O(N)** |
| Merging     | `pd.merge(users, grouped, how="left")` | **O(N)** |
| Sorting     | `.sort_values(by="user_id")`        | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates the complexity, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python total_distance.py
```

### **3️⃣ Sample Output**
```plaintext
   user_id     name  traveled distance
0       1   Alice               15.0
1       2     Bob               13.0
2       3  Charlie               8.0
3       4   David                0.0
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.groupby()`** for efficient data aggregation.  
✔ Ensures **missing values (users with no rides) are properly filled with `0`**.  
✔ Implements **sorted ordering** by `user_id`.  
✔ 🚀 **Optimised for large datasets with efficient merging and grouping.**  

🔥 **This method ensures a structured, efficient, and scalable solution for analysing user travel distances!** 🚗📊