# ⚽ **LeetCode 3246: Premier League Table Ranking**  

## 📌 **Problem Overview**  
Given a dataset of **Premier League teams and their match records**, we need to **calculate the points and ranking for each team** based on the following rules:  

✔ **Points Calculation:**  
   - **Win** → **3 points**  
   - **Draw** → **1 point**  
   - **Loss** → **0 points**  

✔ **Ranking Rules:**  
   - Teams with the **same points** must have the **same rank**.  
   - The table is sorted **by `points` in descending order**.  
   - If teams have the same points, they are sorted **alphabetically by `team_name`**.  

## 🔍 **Example Walkthrough**  

### **Input:**
```python
team_stats_data = {
    "team_id": [1, 2, 3, 4, 5],
    "team_name": ["Manchester City", "Liverpool", "Chelsea", "Arsenal", "Tottenham"],
    "matches_played": [10, 10, 10, 10, 10],
    "wins": [6, 6, 5, 4, 3],
    "draws": [2, 2, 3, 4, 5],
    "losses": [2, 2, 2, 2, 2],
}
```

### **Processing Logic:**
| Team ID | Team Name        | Wins | Draws | Losses | **Points** |
|---------|-----------------|------|-------|--------|---------|
| **1**   | Manchester City | 6    | 2     | 2      | **(6×3) + (2×1) = 20** |
| **2**   | Liverpool       | 6    | 2     | 2      | **(6×3) + (2×1) = 20** |
| **3**   | Chelsea         | 5    | 3     | 2      | **(5×3) + (3×1) = 18** |
| **4**   | Arsenal         | 4    | 4     | 2      | **(4×3) + (4×1) = 16** |
| **5**   | Tottenham       | 3    | 5     | 2      | **(3×3) + (5×1) = 14** |

1. **Assign rankings based on points:**  
   - Liverpool and Manchester City both have **20 points**, so they are ranked **1st**.  
   - Chelsea is next with **18 points** (Rank **3**).  
   - Arsenal follows with **16 points** (Rank **4**).  
   - Tottenham is last with **14 points** (Rank **5**).  

2. **Sort by `points` (Descending), then `team_name` (Ascending):**  

### **Final Result:**
| Team ID | Team Name         | Points | Rank |
|---------|------------------|--------|------|
| **2**   | Liverpool        | **20** | 1    |
| **1**   | Manchester City  | **20** | 1    |
| **3**   | Chelsea          | **18** | 3    |
| **4**   | Arsenal          | **16** | 4    |
| **5**   | Tottenham        | **14** | 5    |

## 🛠 **Python Solution**
```python
import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the points and ranking for each team in the league.

    Points are awarded as follows:
    - 3 points for a win
    - 1 point for a draw
    - 0 points for a loss

    Teams with the same points must have the same ranking, and results should be ordered
    by points (descending), then by team name (ascending).

    Parameters:
    team_stats (pd.DataFrame): A DataFrame containing team performance statistics with columns:
                               - 'team_id' (int): Unique identifier for each team.
                               - 'team_name' (str): Name of the football team.
                               - 'matches_played' (int): Total matches played.
                               - 'wins' (int): Number of wins.
                               - 'draws' (int): Number of draws.
                               - 'losses' (int): Number of losses.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'team_id' (int): Unique team identifier.
                  - 'team_name' (str): Name of the football team.
                  - 'points' (int): Total points based on wins and draws.
                  - 'position' (int): Rank based on points (same points = same rank).
                  The result is sorted by 'points' (descending) and then by 'team_name' (ascending).
    """
    # Calculate total points: 3 points per win, 1 point per draw, 0 points per loss
    team_stats["points"] = team_stats["wins"] * 3 + team_stats["draws"]

    # Assign ranking based on points (descending order), using "min" method to handle ties
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False).astype(int)

    # Select relevant columns and sort the results
    return team_stats[["team_id", "team_name", "points", "position"]].sort_values(
        by=["points", "team_name"], ascending=[False, True]
    )
```

## ⏳ **Complexity Analysis**
| Step         | Operation                     | Time Complexity |
|-------------|------------------------------|----------------|
| Computing Points | `team_stats["wins"] * 3 + team_stats["draws"]` | **O(N)** |
| Ranking Teams | `.rank(method="min", ascending=False)` | **O(N log N)** |
| Sorting Results | `.sort_values(by=["points", "team_name"])` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

---

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python premier_league_table.py
```

### **3️⃣ Sample Output**
```plaintext
   team_id         team_name  points  position
1       2        Liverpool      20         1
0       1  Manchester City      20         1
2       3          Chelsea      18         3
3       4          Arsenal      16         4
4       5        Tottenham      14         5
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas vectorised operations (`wins * 3 + draws`)** for efficient calculations.  
✔ Implements **`.rank(method="min")`** to handle ranking ties correctly.  
✔ Ensures **sorted ordering by `points` (descending) and `team_name` (ascending)** to match problem requirements.  
✔ 🚀 **Optimised for large datasets with `O(N log N)` complexity.**  

🔥 **This method ensures a structured, efficient, and scalable solution for ranking Premier League teams!** ⚽🏆🚀