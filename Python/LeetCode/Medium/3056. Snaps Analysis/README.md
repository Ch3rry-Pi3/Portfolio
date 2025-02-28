# 📊 **LeetCode 3056: Snaps Analysis**

## 📌 **Problem Overview**

We have two tables:

- **Activities Table**: Records the time spent by users either **sending** or **opening snaps**.
- **Age Table**: Maps each **user_id** to an **age bucket** (e.g., `'21-25'`, `'26-30'`, `'31-35'`).

We need to compute:

- The **percentage of time spent on sending snaps** for each age group.
- The **percentage of time spent on opening snaps** for each age group.

📌 **Percentages should be rounded to 2 decimal places**.

🔹 **Return the result table in any order.**

## 📝 **Example 1**

### **Input:**
#### **Activities Table**
| activity_id | user_id | activity_type | time_spent |
|------------|---------|--------------|------------|
| 7274       | 123     | open         | 4.50       |
| 2425       | 123     | send         | 3.50       |
| 1413       | 456     | send         | 5.67       |
| 8564       | 456     | send         | 8.24       |
| 5235       | 456     | open         | 3.00       |
| 4251       | 123     | open         | 1.25       |
| 1435       | 789     | open         | 5.25       |
| 1436       | 789     | send         | 6.24       |

#### **Age Table**
| user_id | age_bucket |
|---------|-----------|
| 123     | 31-35     |
| 789     | 21-25     |
| 456     | 26-30     |

### **Output:**
| age_bucket | send_perc | open_perc |
|------------|----------|-----------|
| 31-35      | 37.84    | 62.16     |
| 26-30      | 82.26    | 17.74     |
| 21-25      | 54.31    | 45.69     |

## 🔍 **Explanation**
For **age group 31-35** (User **123**):
- Time spent **sending snaps** = `3.50`
- Time spent **opening snaps** = `4.50 + 1.25 = 5.75`
- **Total time spent** = `3.50 + 5.75 = 9.25`
- **Sending Percentage** = `(3.50 / 9.25) * 100 = 37.84%`
- **Opening Percentage** = `(5.75 / 9.25) * 100 = 62.16%`

For **age group 26-30** (User **456**):
- Time spent **sending snaps** = `5.67 + 8.24 = 13.91`
- Time spent **opening snaps** = `3.00`
- **Total time spent** = `13.91 + 3.00 = 16.91`
- **Sending Percentage** = `(13.91 / 16.91) * 100 = 82.26%`
- **Opening Percentage** = `(3.00 / 16.91) * 100 = 17.74%`

For **age group 21-25** (User **789**):
- Time spent **sending snaps** = `6.24`
- Time spent **opening snaps** = `5.25`
- **Total time spent** = `6.24 + 5.25 = 11.49`
- **Sending Percentage** = `(6.24 / 11.49) * 100 = 54.31%`
- **Opening Percentage** = `(5.25 / 11.49) * 100 = 45.69%`

## 🚀 **Approach & Solution**
### **1️⃣ Merge the tables**
We merge `activities` and `age` tables on **user_id** to link each activity to an age bucket.

### **2️⃣ Compute total times**
- **Total time per age group** → Sum of `time_spent` for each `age_bucket`.
- **Total time spent on sending & opening** → Group by `age_bucket` and `activity_type`.

### **3️⃣ Calculate percentages**
- **send_perc** = `(total time spent on sending) / (total time spent) * 100`
- **open_perc** = `100 - send_perc`

### **4️⃣ Format the result**
- Round percentages to **2 decimal places**.
- Ensure unique age buckets in the final output.

## 📝 **Implementation**
```python
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
```

## ⏳ **Time Complexity Analysis**
| Operation                         | Complexity |
|------------------------------------|------------|
| **Merging tables (users + activities)** | **O(N)** |
| **Grouping and aggregating by age bucket** | **O(N)** |
| **Computing percentages** | **O(N)** |
| **Overall Complexity** | **O(N)** ✅ |

🔹 **Why is this optimal?**
- We **merge** the tables **once** → **O(N)**
- We **group and aggregate** efficiently → **O(N)**
- We **calculate percentages** using vectorised operations → **O(N)**

## 📂 **Project Structure**
```
snaps_analysis/
├── snaps_analysis.py  # Python solution
├── README.md          # Explanation and walkthrough
```

## 🎯 **Key Takeaways**
✔ **Efficient O(N) complexity** ensures scalability.  
✔ **Merge + Grouping + Percentage Calculation** makes solution intuitive.  
✔ **Handles all age groups dynamically** without hardcoding categories.  

🚀 **Master this technique for similar data aggregation problems!** 🔥  