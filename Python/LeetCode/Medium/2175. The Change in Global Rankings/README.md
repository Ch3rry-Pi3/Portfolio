# 🏆 **LeetCode 2175: The Change in Global Rankings**  

## 📌 **Problem Overview**  
We are given two tables:  

### **1️⃣ TeamPoints Table**  
This table contains details about national teams and their current ranking points.  

| Column Name | Type  | Description |
|------------|------|-------------|
| `team_id`  | int  | Unique ID of the team |
| `name`     | str  | Name of the country |
| `points`   | int  | Ranking points |

### **2️⃣ PointsChange Table**  
This table records how each team's ranking points change.  

| Column Name     | Type  | Description |
|----------------|------|-------------|
| `team_id`      | int  | Unique ID of the team |
| `points_change` | int  | Change in points (+/-) |

## 🎯 **Goal**  
1️⃣ **Update each team's points** using the `points_change` column.  
2️⃣ **Rank teams based on updated points** (higher points → better rank).  
3️⃣ **If points are the same, rank alphabetically** by `name` (lexicographically).  
4️⃣ **Calculate the ranking difference (`rank_diff`)** by comparing **old and new rankings**.  

## 🛠 **Approach**  

### 🔹 **Step 1: Merge `TeamPoints` with `PointsChange`**
- This ensures each team’s points are updated correctly.

### 🔹 **Step 2: Assign Initial Ranking (`rank_points`)**
- Sort by `points` (descending).  
- If points are equal, sort by `name` (ascending).  
- Use `range(1, len(df) + 1)` to assign rankings.

### 🔹 **Step 3: Update the Points**
- Add `points_change` to `points` to get `new_points`.

### 🔹 **Step 4: Assign New Ranking (`rank_new_points`)**
- Sort by `new_points` and `name` (same rules as Step 2).
- Assign new rankings.

### 🔹 **Step 5: Compute `rank_diff`**
- **Formula:** `rank_diff = rank_points - rank_new_points`  
- A **positive value** means the team moved **up** in the ranking.  
- A **negative value** means the team dropped **down** in the ranking.  

## 🚀 **Python Solution**  

```python
import pandas as pd

def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the change in global rankings after updating each team's points.

    Args:
        team_points (pd.DataFrame): Table containing team ranking points.
        points_change (pd.DataFrame): Table containing points change for each team.

    Returns:
        pd.DataFrame: A DataFrame with `team_id`, `name`, and `rank_diff`.
    """
    # Merge team points with points change
    df = pd.merge(left=team_points, right=points_change, on="team_id", how="left")

    # Rank teams before updating points
    df = df.sort_values(by=["points", "name"], ascending=[False, True]).assign(
        rank_points=range(1, len(df) + 1)
    )

    # Update points
    df = df.assign(new_points=lambda x: x["points"] + x["points_change"])

    # Rank teams after updating points
    df = df.sort_values(by=["new_points", "name"], ascending=[False, True]).assign(
        rank_new_points=range(1, len(df) + 1)
    )

    # Compute ranking difference
    df = df.assign(rank_diff=lambda x: x["rank_points"] - x["rank_new_points"])

    # Return final results
    return df[["team_id", "name", "rank_diff"]]
```

## 🎯 **Example Walkthrough**
### **Input Data**  

#### **TeamPoints Table**
| team_id | name        | points |
|---------|------------|--------|
| 3       | Algeria    | 1431   |
| 2       | Senegal    | 2132   |
| 1       | New Zealand | 1402  |
| 4       | Croatia    | 1817   |

#### **PointsChange Table**
| team_id | points_change |
|---------|--------------|
| 3       | 399          |
| 2       | 0            |
| 1       | 13           |
| 4       | -22          |

### **Processing**
1️⃣ **Initial Ranking (`rank_points`)**
| team_id | name        | points | rank_points |
|---------|------------|--------|------------|
| 2       | Senegal    | 2132   | 1          |
| 4       | Croatia    | 1817   | 2          |
| 3       | Algeria    | 1431   | 3          |
| 1       | New Zealand | 1402   | 4          |

2️⃣ **Update Points**
| team_id | name        | new_points |
|---------|------------|------------|
| 3       | Algeria    | 1431 + 399 = 1830 |
| 4       | Croatia    | 1817 - 22 = 1795  |
| 1       | New Zealand | 1402 + 13 = 1415 |
| 2       | Senegal    | 2132 + 0 = 2132 |

3️⃣ **New Ranking (`rank_new_points`)**
| team_id | name        | new_points | rank_new_points |
|---------|------------|------------|----------------|
| 2       | Senegal    | 2132       | 1 |
| 3       | Algeria    | 1830       | 2 |
| 4       | Croatia    | 1795       | 3 |
| 1       | New Zealand | 1415       | 4 |

4️⃣ **Compute `rank_diff`** (`rank_diff = rank_points - rank_new_points`)
| team_id | name        | rank_diff |
|---------|------------|-----------|
| 2       | Senegal    | 1 - 1 = 0 |
| 3       | Algeria    | 3 - 2 = 1 |
| 4       | Croatia    | 2 - 3 = -1 |
| 1       | New Zealand | 4 - 4 = 0 |

### **Final Output**
| team_id | name        | rank_diff |
|---------|------------|-----------|
| 2       | Senegal    | 0         |
| 3       | Algeria    | 1         |
| 4       | Croatia    | -1        |
| 1       | New Zealand | 0         |

## ⏳ **Complexity Analysis**  

| Step | Time Complexity |
|------|----------------|
| Merging Tables | **O(N)** |
| Sorting (Twice) | **O(N log N)** |
| Assigning Ranks | **O(N)** |
| Final Computations | **O(N)** |
| **Overall Complexity** | **O(N log N)** |


## 📁 **Project Structure**  

```
global_ranking_change/
├── change_in_ranking.py  # Python solution
├── README.md             # Documentation
```
