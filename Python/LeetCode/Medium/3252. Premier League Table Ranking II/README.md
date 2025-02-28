# 🏆 **LeetCode 3252: Premier League Table Ranking II**

## 📌 **Problem Overview**  

You are given a table `TeamStats` containing **team performance** statistics for a football league.  

Each team is ranked based on their **total points**, calculated as follows:  

- 🏅 **Win** = `3 points`  
- 🤝 **Draw** = `1 point`  
- ❌ **Loss** = `0 points`  

Teams with the **same number of points** share the **same position** in the ranking.

### 🔹 **Tier Ranking**  
The teams are divided into **three tiers** based on their **points**:  

1️⃣ **Tier 1:** Top **33%** of teams  
2️⃣ **Tier 2:** Middle **34%** of teams  
3️⃣ **Tier 3:** Bottom **33%** of teams  

⚠️ **Tie-breaking rule:**  
- If multiple teams have **the same number of points** on a **tier boundary**, place them in the **higher tier**.  

Return the result **ordered by points (descending)**, then by **team_name (ascending)**.

## 📝 **Example 1**  

### **Input:**
```plaintext
TeamStats table:
| team_id | team_name         | matches_played | wins | draws | losses |
|---------|------------------|---------------|------|-------|--------|
| 1       | Chelsea          | 22            | 13   | 2     | 7      |
| 2       | Nottingham Forest | 27           | 6    | 6     | 15     |
| 3       | Liverpool        | 17            | 1    | 8     | 8      |
| 4       | Aston Villa      | 20            | 3    | 6     | 11     |
| 5       | Fulham           | 31            | 18   | 1     | 12     |
| 6       | Burnley          | 26            | 6    | 9     | 11     |
| 7       | Newcastle United | 33            | 11   | 10    | 12     |
| 8       | Sheffield United | 20            | 18   | 2     | 0      |
| 9       | Luton Town       | 5             | 4    | 0     | 1      |
| 10      | Everton          | 14            | 2    | 6     | 6      |
```

### **Output:**
```plaintext
| team_name          | points | position | tier  |
|-------------------|--------|----------|------|
| Sheffield United  | 56     | 1        | Tier 1 |
| Fulham           | 55     | 2        | Tier 1 |
| Newcastle United | 43     | 3        | Tier 1 |
| Chelsea          | 41     | 4        | Tier 1 |
| Burnley         | 27     | 5        | Tier 2 |
| Nottingham Forest | 24     | 6        | Tier 2 |
| Everton         | 12     | 7        | Tier 2 |
| Luton Town      | 12     | 7        | Tier 2 |
| Liverpool       | 11     | 9        | Tier 3 |
| Aston Villa     | 9      | 10       | Tier 3 |
```

### ✅ **Explanation:**
- **Sheffield United** has `56 points` (`18 * 3 + 2 * 1`) → **Position 1**  
- **Fulham** has `55 points` (`18 * 3 + 1 * 1`) → **Position 2**  
- **Newcastle United** has `43 points` (`11 * 3 + 10 * 1`) → **Position 3**  
- **Chelsea** has `41 points` (`13 * 3 + 2 * 1`) → **Position 4**  
- **Burnley** has `27 points` → **Position 5**  
- **Nottingham Forest** has `24 points` → **Position 6**  
- **Everton** and **Luton Town** have `12 points` → **Position 7**  
- **Liverpool** has `11 points` → **Position 9**  
- **Aston Villa** has `9 points` → **Position 10**  

🔹 **Tier Calculation:**  
- **Tier 1:** Top 33% → *Sheffield United, Fulham, Newcastle United, Chelsea*  
- **Tier 2:** Middle 34% → *Burnley, Nottingham Forest, Everton, Luton Town*  
- **Tier 3:** Bottom 33% → *Liverpool, Aston Villa*  

## 🚀 **Approach & Intuition**  

### 🔹 **Steps to Solve:**
1. **Calculate points** for each team:  
   ```
   points = (wins * 3) + (draws * 1)
   ```
2. **Determine position** based on total points:  
   - Teams with the **same points share the same position** (using **`rank(method='min')`**).  
3. **Determine tier rankings:**  
   - **Top 33% → Tier 1**  
   - **Middle 34% → Tier 2**  
   - **Bottom 33% → Tier 3**  
   - If a **tie** occurs at the **tier boundary**, the team is placed in the **higher tier**.  
4. **Sort results:**  
   - First by **points (descending)**  
   - Then by **team_name (ascending)**  

## 📝 **Implementation**  

```python
import pandas as pd
import numpy as np

def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates team rankings based on points and assigns teams to tiers.

    :param team_stats: DataFrame containing team stats including wins, draws, and losses.
    :return: DataFrame with columns team_name, points, position, and tier.
    """

    # Calculate total points
    team_stats["points"] = (team_stats["wins"] * 3) + (team_stats["draws"] * 1)

    # Rank teams by points (descending), handling ties with "min" ranking
    team_stats["position"] = team_stats["points"].rank(method="min", ascending=False)

    # Determine tier cutoffs
    num_teams = team_stats["team_id"].nunique()
    top_cutoff = np.ceil(num_teams * 0.33)
    bottom_cutoff = np.ceil(num_teams * (1 - 0.33))

    # Assign tiers based on cutoffs
    team_stats["tier"] = np.where(
        team_stats["position"] <= top_cutoff, "Tier 1",
        np.where(team_stats["position"] > bottom_cutoff, "Tier 3", "Tier 2")
    )

    # Return the result sorted by points (descending), then team_name (ascending)
    return team_stats[["team_name", "points", "position", "tier"]].sort_values(
        by=["points", "team_name"], ascending=[False, True]
    )
```

## ⏳ **Time Complexity Analysis**  

| Operation | Complexity |
|-----------|------------|
| **Calculate Points** | **O(n)** |
| **Rank Teams** | **O(n log n)** |
| **Assign Tiers** | **O(n)** |
| **Overall Complexity** | **O(n log n)** ✅ |

🚀 **Mastering ranking problems like this is crucial for SQL and Data Analysis!** 🔥⚽  