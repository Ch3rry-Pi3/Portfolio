# 🎵 **LeetCode 2669: Spotify Artist Song Count**  

## 📌 **Problem Overview**  
In a given **Spotify dataset**, we want to **count the number of unique songs** for each artist and return the results **sorted** by:  

1. **Descending order of unique song count** (artists with more unique songs appear first).  
2. **Ascending alphabetical order of artist names** (in case of ties).  

The dataset contains the following columns:  

- **`id`** → Unique identifier for a song.  
- **`artist`** → Name of the artist who performed the song.  

## 🔍 **Sorting Criteria**
| Column    | Sorting Order  |
|-----------|---------------|
| 🎵 **Occurrences** (Song Count) | **Descending** (Highest First) |
| 🎤 **Artist Name** | **Ascending** (A-Z, in case of ties) |

---

## 🏆 **Example Walkthrough**  

### **Input:**
```python
spotify_data = {
    "id": [1, 2, 3, 4, 5, 1, 6, 7, 8, 2, 9],
    "artist": [
        "Adele", "Adele", "Drake", "Drake", "Drake", "Adele", 
        "Beyoncé", "Beyoncé", "Coldplay", "Adele", "Coldplay"
    ]
}
```

### **Processing Logic:**
| ID  | Artist   |
|-----|---------|
| 1   | Adele   |
| 2   | Adele   |
| 3   | Drake   |
| 4   | Drake   |
| 5   | Drake   |
| 1   | Adele   | (Duplicate song, ignored in count) |
| 6   | Beyoncé |
| 7   | Beyoncé |
| 8   | Coldplay|
| 2   | Adele   | (Duplicate song, ignored in count) |
| 9   | Coldplay|

- **Drake** has **3 unique songs** (`{3, 4, 5}`)  
- **Adele** has **2 unique songs** (`{1, 2}`)  
- **Beyoncé** has **2 unique songs** (`{6, 7}`)  
- **Coldplay** has **2 unique songs** (`{8, 9}`)  

### **Expected Output:**
```plaintext
     artist  occurrences
2    Drake            3
0    Adele            2
1  Beyoncé            2
3  Coldplay           2
```

## 🛠 **Python Solution**
```python
import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of unique song occurrences for each artist and sorts the result.

    Parameters:
    spotify (pd.DataFrame): A DataFrame containing song data with columns:
                            - 'id' (str/int): Unique identifier for each song.
                            - 'artist' (str): The name of the artist.

    Returns:
    pd.DataFrame: A DataFrame containing:
                  - 'artist' (str): The name of the artist.
                  - 'occurrences' (int): The number of unique songs by the artist.
                  The result is sorted by:
                  - 'occurrences' in descending order.
                  - 'artist' in ascending order (A-Z) in case of ties.
    """
    return (
        spotify
        .groupby("artist", as_index=False)["id"]
        .nunique()
        .sort_values(by=["id", "artist"], ascending=[False, True])
        .rename(columns={"id": "occurrences"})
    )
```

## ⏳ **Complexity Analysis**
| Step         | Operation                   | Time Complexity |
|-------------|----------------------------|----------------|
| Grouping    | `.groupby("artist")`        | **O(N)** |
| Counting    | `.nunique()`                 | **O(N)** |
| Sorting     | `.sort_values(by=…, ascending=…)` | **O(N log N)** |
| **Total Complexity** | **O(N log N)** | ✅ Efficient |

Since sorting dominates, the overall complexity is **O(N log N)**.

## 🚀 **How to Use**
### **1️⃣ Installation**
Ensure you have **Python 3.x** and install Pandas if not installed:  
```bash
pip install pandas
```

### **2️⃣ Running the Script**
```bash
python spotify_list.py
```

### **3️⃣ Sample Output**
```plaintext
     artist  occurrences
2    Drake            3
0    Adele            2
1  Beyoncé            2
3  Coldplay           2
```

## 🎯 **Why This Approach?**
✔ Uses **Pandas `.groupby()`** for efficient data aggregation.  
✔ Ensures **unique song count per artist** using `.nunique()`.  
✔ Implements **sorted ordering** by song count (descending) and artist name (ascending).  
✔ 🚀 **Optimised for large datasets with efficient sorting and grouping.**

🔥 **This method ensures a structured, efficient, and scalable solution for analyzing Spotify artist song counts!** 🎶🎧