# 📊 **LeetCode 1308: Running Total for Different Genders**  

## 📌 **Problem Overview**  
You are given a table `Scores` that contains information about players participating in a competition. Each row in the table represents:  
- A **player's name**.  
- The **gender** of the player (`'F'` for female and `'M'` for male).  
- The **date** (`day`) the player played.  
- The **score points** the player earned on that day.  

The competition includes **both male and female teams**, and we need to calculate the **running total score** for each gender on each day.  

### **Goal**  
For each **gender** and **day**, compute the cumulative (running) total score **up to that day**.  
- The result should be **ordered by gender first**, then by day in **ascending order**.  

## 📊 **Database Schema**  

### **Scores Table**  
| Column Name   | Type    | Description |
|--------------|--------|-------------|
| `player_name` | varchar | Name of the player |
| `gender`      | varchar | 'F' for female, 'M' for male |
| `day`         | date    | Date of the game |
| `score_points` | int     | Points scored by the player |

## 🛠 **Approach**  

1. **Sort the data**  
   - First by `gender` (ascending).  
   - Then by `day` (ascending).  

2. **Compute the running total**  
   - Use **cumulative sum (`cumsum()`)** grouped by `gender` to maintain the running total for each gender separately.  

3. **Select the required columns**  
   - Return the final DataFrame with `gender`, `day`, and the computed running total as `total`.  

## 🚀 **Python Solution**  

```python
import pandas as pd


def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the running total score for each gender on each day.

    Args:
        scores (pd.DataFrame): A DataFrame containing columns:
            - "player_name" (str): Name of the player.
            - "gender" (str): 'F' for female, 'M' for male.
            - "day" (datetime): Date of the game.
            - "score_points" (int): Points scored by the player.

    Returns:
        pd.DataFrame: A DataFrame with columns:
            - "gender" (str): Gender category.
            - "day" (datetime): Date of the game.
            - "total" (int): Cumulative total score per gender.
    """
    return (
        scores
        .sort_values(by=["gender", "day"], ascending=[True, True])
        .assign(total=lambda x: x.groupby("gender")["score_points"].cumsum())
        [["gender", "day", "total"]]
    )
```

## 📌 **Example Walkthrough**  

### **Example Input**  

#### **Scores Table**  
| player_name | gender | day         | score_points |
|------------|--------|------------|-------------|
| Aron       | F      | 2020-01-01 | 17          |
| Alice      | F      | 2020-01-07 | 23          |
| Bajrang    | M      | 2020-01-07 | 7           |
| Khali      | M      | 2019-12-25 | 11          |
| Slaman     | M      | 2019-12-30 | 13          |
| Joe        | M      | 2019-12-31 | 3           |
| Jose       | M      | 2019-12-18 | 2           |
| Priya      | F      | 2019-12-31 | 23          |
| Priyanka   | F      | 2019-12-30 | 17          |

### **Output**  
```python
   gender        day  total
0      F 2019-12-30     17
1      F 2019-12-31     40
2      F 2020-01-01     57
3      F 2020-01-07     80
4      M 2019-12-18      2
5      M 2019-12-25     13
6      M 2019-12-30     26
7      M 2019-12-31     29
8      M 2020-01-07     36
```

### **Explanation**  
- For **Female (`F`) players**:  
  - Priyanka scores **17** on `2019-12-30` → total = 17.  
  - Priya scores **23** on `2019-12-31` → total = 40.  
  - Aron scores **17** on `2020-01-01` → total = 57.  
  - Alice scores **23** on `2020-01-07` → total = 80.  

- For **Male (`M`) players**:  
  - Jose scores **2** on `2019-12-18` → total = 2.  
  - Khali scores **11** on `2019-12-25` → total = 13.  
  - Slaman scores **13** on `2019-12-30` → total = 26.  
  - Joe scores **3** on `2019-12-31` → total = 29.  
  - Bajrang scores **7** on `2020-01-07` → total = 36.  

## ⏳ **Complexity Analysis**  

| Step | Operation | Time Complexity |
|------|------------|----------------|
| Sorting | `sort_values(by=["gender", "day"])` | **O(N log N)** |
| Grouping | `groupby("gender")` | **O(N)** |
| Cumulative Sum | `cumsum()` | **O(N)** |
| Selecting Columns | `[['gender', 'day', 'total']]` | **O(N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

## 🎯 **Why This Approach?**  
✔ **Uses efficient Pandas operations** (`sort_values`, `groupby`, `cumsum`).  
✔ **Preserves the required ordering by gender and day**.  
✔ **Handles large datasets effectively with vectorised operations**.  

🚀 **With this approach, you can easily track the running score totals for each gender in any competition dataset!** 🎯