# ⚽ **LeetCode 2339: All the Matches of the League**  

## 📌 **Problem Overview**  
In a football (soccer) league, each team plays against every other team twice:  
- **Once as the home team**  
- **Once as the away team**  

We are given a table `Teams`, where each row represents a unique team in the league.  
Our task is to **generate all possible matchups** while ensuring that:  
- A team **cannot play against itself**  
- Each matchup occurs **twice** (once as home, once as away)  

## 📊 **Example**  

### **Input:**
#### **Teams Table**
| team_name     |
|--------------|
| Leetcode FC  |
| Ahly SC      |
| Real Madrid  |

### **Output:**
#### **Matches Table**
| home_team     | away_team    |
|--------------|--------------|
| Real Madrid  | Leetcode FC  |
| Real Madrid  | Ahly SC      |
| Leetcode FC  | Real Madrid  |
| Leetcode FC  | Ahly SC      |
| Ahly SC      | Real Madrid  |
| Ahly SC      | Leetcode FC  |

### **Explanation:**
- **Each team plays against every other team twice**  
- **Example matchups:**  
  - **Real Madrid vs Leetcode FC** (home: Real Madrid, away: Leetcode FC)  
  - **Leetcode FC vs Real Madrid** (home: Leetcode FC, away: Real Madrid)  
  - And so on...

## 🛠 **Approach**
To solve this problem, we can use a **cross join**:
1. **Cross Join (`merge(how="cross")`)**  
   - This generates **all possible pairs** of teams.
2. **Rename Columns**  
   - Convert `team_name_home` → `home_team` and `team_name_away` → `away_team`.  
3. **Remove Self-Matches**  
   - Use `.query("home_team != away_team")` to remove cases where a team plays against itself.  

## 🚀 **Python Solution**
```python
import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    """
    Generates all possible matchups in a league where each team plays against every other team twice
    (once as the home team and once as the away team).

    Args:
        teams (pd.DataFrame): A DataFrame containing a column "team_name" with unique team names.

    Returns:
        pd.DataFrame: A DataFrame with two columns, "home_team" and "away_team", containing all possible matches.
    """

    # Perform a cross join to get all possible combinations of teams
    matches = (
        teams
        .merge(teams, how="cross", suffixes=("_home", "_away"))
        .rename(columns={"team_name_home": "home_team", "team_name_away": "away_team"})
    )

    # Remove cases where a team plays against itself
    matches = matches.query("home_team != away_team")

    return matches
```

## 📌 **Example Walkthrough**  
Let’s say we have **3 teams:**
```
["Leetcode FC", "Ahly SC", "Real Madrid"]
```
After applying the **cross join**, we get **9 total pairs**.  
By **removing self-matches**, we get **6 valid matchups** as expected.

## ⏳ **Complexity Analysis**
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Cross Join (`merge`) | **O(n²)** | **O(n²)** |
| Self-match filtering (`query`) | **O(n²)** | **O(n²)** |
| **Total Complexity** | **O(n²)** | **O(n²)** |

Since `n` is the number of teams, this approach is **efficient for small leagues**.

## 🎯 **Why This Approach?**
✔ **Simple and clear logic** using Pandas.  
✔ **No need for nested loops**—Pandas handles it efficiently.  
✔ **Scalable for small to mid-sized leagues**.  

⚡ **Now, you can generate all possible league matchups effortlessly!** ⚽

Would you like any modifications or additional explanations? 😊